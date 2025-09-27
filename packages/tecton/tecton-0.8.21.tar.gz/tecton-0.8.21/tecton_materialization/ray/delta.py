import dataclasses
import os
import typing
import uuid
from typing import Callable
from typing import List
from typing import Optional

import pyarrow
import pyarrow.dataset
import pyarrow.fs
import ray
from google.protobuf import timestamp_pb2

from tecton_core import offline_store
from tecton_core.arrow import PARQUET_WRITE_OPTIONS
from tecton_core.compute_mode import ComputeMode
from tecton_core.duckdb_context import DuckDBContext
from tecton_core.feature_definition_wrapper import FeatureDefinitionWrapper
from tecton_core.query.dialect import Dialect
from tecton_core.query.nodes import AddAnchorTimeNode
from tecton_core.query.nodes import StagedTableScanNode
from tecton_materialization.ray.nodes import AddTimePartitionNode
from tecton_materialization.ray.nodes import TimeSpec
from tecton_proto.common import data_type_pb2
from tecton_proto.common import schema_pb2
from tecton_proto.offlinestore.delta import metadata_pb2
from tecton_proto.offlinestore.delta import transaction_writer_pb2


class TimeInterval(typing.NamedTuple):
    start: timestamp_pb2.Timestamp
    end: timestamp_pb2.Timestamp


class JavaActorWrapper:
    """Blocking wrapper around a Java actor."""

    def __init__(self, class_name):
        self.actor = ray.cross_language.java_actor_class(class_name).remote()

    def __getattr__(self, item):
        def f(*args):
            return ray.get(getattr(self.actor, item).remote(*args))

        return f


class TransactionWriter:
    """Wrapper around TransactionWriter actor which handles (de)serialization of parameters and return values."""

    def __init__(self, args: transaction_writer_pb2.InitializeArgs):
        self.actor = JavaActorWrapper("com.tecton.offlinestore.delta.TransactionWriterActor")
        self.actor.initialize(args.SerializeToString())

    def has_commit_with_metadata(self, metadata: metadata_pb2.TectonDeltaMetadata) -> bool:
        return self.actor.hasCommitWithMetadata(metadata.SerializeToString())

    def read_for_update(self, predicate: transaction_writer_pb2.Expression) -> List[str]:
        result_bytes = self.actor.readForUpdate(
            transaction_writer_pb2.ReadForUpdateArgs(read_predicate=predicate).SerializeToString()
        )
        result = transaction_writer_pb2.ReadForUpdateResult()
        result.ParseFromString(result_bytes)
        return result.uris

    def update(self, args: transaction_writer_pb2.UpdateArgs):
        self.actor.update(args.SerializeToString())


def _pyarrow_literal(table: pyarrow.Table, column: schema_pb2.Column, row: int) -> transaction_writer_pb2.Expression:
    """Returns a Delta literal Expression for the given row and column within table."""
    pa_column = next((c for (name, c) in zip(table.column_names, table.columns) if name == column.name))
    pa_value = pa_column[row]

    def assert_type(t: pyarrow.DataType):
        assert pa_column.type == t, f"Type error for {column.name}. Expected {t}; got {pa_column.type}"

    if column.offline_data_type.type == data_type_pb2.DataTypeEnum.DATA_TYPE_INT64:
        assert_type(pyarrow.int64())
        lit = transaction_writer_pb2.Expression.Literal(int64=pa_value.as_py())
    elif column.offline_data_type.type == data_type_pb2.DataTypeEnum.DATA_TYPE_STRING:
        assert_type(pyarrow.string())
        lit = transaction_writer_pb2.Expression.Literal(str=pa_value.as_py())
    elif column.offline_data_type.type == data_type_pb2.DataTypeEnum.DATA_TYPE_TIMESTAMP:
        assert_type(pyarrow.timestamp("us"))
        lit = transaction_writer_pb2.Expression.Literal()
        lit.timestamp.FromDatetime(pa_value.as_py())
    else:
        msg = f"Unsupported type {column.offline_data_type.type} in column {column.name}"
        raise Exception(msg)
    return transaction_writer_pb2.Expression(literal=lit)


def _binary_expr(
    op: transaction_writer_pb2.Expression.Binary.Op,
    left: transaction_writer_pb2.Expression,
    right: transaction_writer_pb2.Expression,
) -> transaction_writer_pb2.Expression:
    return transaction_writer_pb2.Expression(
        binary=transaction_writer_pb2.Expression.Binary(op=op, left=left, right=right)
    )


TRUE = transaction_writer_pb2.Expression(literal=transaction_writer_pb2.Expression.Literal(bool=True))


def _in_range(
    table: pyarrow.Table, column: schema_pb2.Column, end_inclusive: bool
) -> transaction_writer_pb2.Expression:
    """Returns a predicate Expression for values which are within the limits of the given column of the given limits table.

    :param table: The table
    :param: column: The column to test in this expression
    :param: Whether the predicate should include the end value
    """
    start_cond = _binary_expr(
        op=transaction_writer_pb2.Expression.Binary.OP_LE,
        left=_pyarrow_literal(table, column, row=0),
        right=transaction_writer_pb2.Expression(column=column),
    )
    end_cond = _binary_expr(
        op=transaction_writer_pb2.Expression.Binary.OP_LE
        if end_inclusive
        else transaction_writer_pb2.Expression.Binary.OP_LT,
        left=transaction_writer_pb2.Expression(column=column),
        right=_pyarrow_literal(table, column, row=1),
    )
    return _binary_expr(op=transaction_writer_pb2.Expression.Binary.OP_AND, left=start_cond, right=end_cond)


@dataclasses.dataclass
class DeltaWriter:
    def __init__(
        self,
        fd: FeatureDefinitionWrapper,
        table_uri: str,
        dynamodb_log_table_name: str,
        dynamodb_log_table_region: str,
        progress_callback: Callable[[float], None],
    ):
        self._fd = fd
        self._table_uri = table_uri
        self._fs, self._base_path = pyarrow.fs.FileSystem.from_uri(self._table_uri)
        self._adds: List[transaction_writer_pb2.AddFile] = []
        self._delete_uris: List[str] = []
        self._dynamodb_log_table_name = dynamodb_log_table_name
        self._dynamodb_log_table_region = dynamodb_log_table_region
        self._current_transaction_writer: Optional[TransactionWriter] = None
        self._partitioning = pyarrow.dataset.partitioning(
            pyarrow.schema([(offline_store.TIME_PARTITION, pyarrow.string())]), flavor="hive"
        )
        self._progress_callack = progress_callback

    def _transaction_writer(self) -> TransactionWriter:
        if not self._current_transaction_writer:
            schema = self._fd.materialization_schema.to_proto()
            partition_column = schema_pb2.Column(
                name=offline_store.TIME_PARTITION,
                offline_data_type=data_type_pb2.DataType(type=data_type_pb2.DataTypeEnum.DATA_TYPE_STRING),
            )
            schema.columns.append(partition_column)
            init_args = transaction_writer_pb2.InitializeArgs(
                path=self._table_uri,
                id=self._fd.id,
                name=self._fd.name,
                description=f"Offline store for FeatureView {self._fd.id} ({self._fd.name})",
                schema=schema,
                partition_columns=[offline_store.TIME_PARTITION],
                dynamodb_log_table_name=self._dynamodb_log_table_name,
                dynamodb_log_table_region=self._dynamodb_log_table_region,
            )
            self._current_transaction_writer = TransactionWriter(init_args)
        return self._current_transaction_writer

    def _time_limits(self, time_interval: TimeInterval) -> pyarrow.Table:
        """Returns a Table specifying the limits of data affected by a materialization job.

        :param time_interval: The feature time interval
        :returns: A relation with one column for the timestamp key or anchor time, and one with the partition value
            corresponding to the first column. The first row will be the values for feature start time and the second for
            feature end time.
        """
        timestamp_table = pyarrow.table(
            {self._fd.timestamp_key: [time_interval.start.ToDatetime(), time_interval.end.ToDatetime()]}
        )
        tree = AddTimePartitionNode.for_feature_definition(
            self._fd,
            AddAnchorTimeNode.for_feature_definition(
                dialect=Dialect.DUCKDB,
                compute_mode=ComputeMode.RIFT,
                fd=self._fd,
                input_node=StagedTableScanNode(
                    dialect=Dialect.DUCKDB,
                    compute_mode=ComputeMode.RIFT,
                    staged_columns=(self._fd.timestamp_key,),
                    staging_table_name="timestamp_table",
                ).as_ref(),
            ),
        )
        conn = DuckDBContext.get_instance().get_connection()
        return conn.sql(tree.to_sql()).arrow()

    def _time_limit_predicate(self, interval: TimeInterval) -> transaction_writer_pb2.Expression:
        """Returns a predicate Expression matching offline store rows for materialization of the given interval."""
        table = self._time_limits(interval)
        time_spec = TimeSpec.for_feature_definition(self._fd)
        time_column = next(
            (col for col in self._fd.materialization_schema.proto.columns if col.name == time_spec.time_column)
        )
        partition_column = schema_pb2.Column(
            name=offline_store.TIME_PARTITION,
            offline_data_type=data_type_pb2.DataType(type=data_type_pb2.DataTypeEnum.DATA_TYPE_STRING),
        )
        predicate = _binary_expr(
            op=transaction_writer_pb2.Expression.Binary.OP_AND,
            left=_in_range(table, time_column, end_inclusive=False),
            right=_in_range(table, partition_column, end_inclusive=True),
        )
        return predicate

    def _filter_files(
        self,
        predicate: transaction_writer_pb2.Expression,
        filter_table: Callable[[pyarrow.dataset.Dataset], pyarrow.Table],
    ):
        paths = self._transaction_writer().read_for_update(predicate)
        deletes = []
        for path in paths:
            input_table = pyarrow.dataset.dataset(
                source=os.path.join(self._base_path, path),
                filesystem=self._fs,
                partitioning=self._partitioning,
            ).to_table()
            output_table = filter_table(input_table)
            if input_table.num_rows != output_table.num_rows:
                deletes.append(path)
                self.write(output_table)
        self._delete_uris.extend(deletes)

    def _filter_materialized_range(self, interval: TimeInterval) -> None:
        """Filters data within a materialized time range from parquet files in the offline store.

        :param interval: The feature data time interval to delete
        """
        time_spec = TimeSpec.for_feature_definition(self._fd)
        conn = DuckDBContext.get_instance().get_connection()

        def table_filter(input_table: pyarrow.dataset.Dataset) -> pyarrow.Table:
            time_limit_table = self._time_limits(interval)
            # Not using pypika because it lacks support for ANTI JOIN
            return conn.sql(
                f"""
                WITH flattened_limits AS(
                    SELECT MIN("{time_spec.time_column}") AS start, MAX("{time_spec.time_column}") AS end
                    FROM time_limit_table
                )
                SELECT * FROM input_table
                ANTI JOIN flattened_limits
                ON input_table."{time_spec.time_column}" >= flattened_limits.start
                OR input_table."{time_spec.time_column}" <  flattened_limits.end
            """
            ).arrow()

        predicate = self._time_limit_predicate(interval)
        self._filter_files(predicate, table_filter)

    def maybe_delete_time_range(self, interval: TimeInterval) -> None:
        """Deletes previously materialized data within the interval if we find a commit with matching metadata.

        High level process:
        1. Construct a Delta predicate expression matching the data we want to delete. This includes both a partition
           predicate to limit the files we have to look at, and a predicate on timestamp/anchor time which doesn't limit
           the files we have to consider, but can help with limit transaction conflicts.
        2. Mark files matching the predicate as read in the Delta transaction. This returns a list of files possibly
           matching the predicate.
        3. For each file:
           3a. Open it, filter out all data matching the predicate, and write out remaining data (if any) to a
               new file.
           3b. If any data was filtered out, add the old file to the list of deletes in the transaction. If any data remains,
               add the new file to the transaction.

        Implementation notes:
        1. This is racy if there is another job running at the same time. This behavior is the same as in Spark.
        2. We have corrected a bug that exists in Spark where we're not correctly selecting the data to delete: TEC-16681
        """
        metadata = metadata_pb2.TectonDeltaMetadata(feature_start_time=interval.start)
        if self._transaction_writer().has_commit_with_metadata(metadata):
            print(f"Found previous commit with metadata {metadata}; clearing prior data")
            # If we have run committed with matching time interval before, delete the previous data.
            self._filter_materialized_range(interval)

    def write(self, table: pyarrow.Table) -> List[str]:
        """Writes a pyarrow Table to the Delta table at base_uri partitioned by the TIME_PARTITION column.

        Returns a list of URIs for the written file(s).

        This does NOT commit to the Delta log. Call commit() after calling this to commit your changes.
        """
        if table.num_rows < 1:
            return []

        adds = []
        failed = False

        def visit_file(f):
            try:
                path = f.path
                _, prefix, relative = path.partition(self._base_path)
                assert prefix == self._base_path, f"Written path is not relative to base path: {path}"
                path_pieces = relative.split("/")
                partition = path_pieces[1]
                k, eq, v = partition.partition("=")
                assert k == offline_store.TIME_PARTITION and eq == "=", f"Unexpected partition format: {path}"
                adds.append(
                    transaction_writer_pb2.AddFile(
                        uri=self._table_uri + relative,
                        partition_values={k: v},
                    )
                )
            except Exception as e:
                # Pyarrow logs and swallows exceptions from this function, so we need some other way of knowing there
                # was a # failure
                nonlocal failed
                failed = True
                raise e

        pyarrow.dataset.write_dataset(
            data=table,
            filesystem=self._fs,
            base_dir=self._base_path,
            format=pyarrow.dataset.ParquetFileFormat(),
            file_options=PARQUET_WRITE_OPTIONS,
            basename_template=f"{uuid.uuid4()}-part-{{i}}.parquet",
            partitioning=self._partitioning,
            file_visitor=visit_file,
            existing_data_behavior="overwrite_or_ignore",
        )

        if failed:
            msg = "file visitor failed"
            raise Exception(msg)

        self._adds.extend(adds)
        return [add.uri for add in adds]

    def delete_keys(self, keys: pyarrow.Table):
        def filter_table(input_table: pyarrow.dataset.Dataset) -> pyarrow.Table:
            conn = DuckDBContext.get_instance().get_connection()
            return conn.sql(
                f"""
                SELECT * FROM input_table
                ANTI JOIN keys
                USING ({", ".join(keys.column_names)})
                """
            ).arrow()

        # It's necessary to scan the entire table anyway, so we just use True as the predicate.
        #
        # In theory this might be missing out on some optimizations to avoid conflicting queries, but in
        # practice the only types of conflicts we could avoid would be key deletion operations on
        # disjoint sets of keys and also end up only touching disjoint sets of files. This is probably not very likely
        # to occur.
        return self._filter_files(TRUE, filter_table)

    def commit(self, metadata: Optional[metadata_pb2.TectonDeltaMetadata] = None):
        args = transaction_writer_pb2.UpdateArgs(
            add_files=self._adds, delete_uris=self._delete_uris, user_metadata=metadata
        )
        self._transaction_writer().update(args)
        self._current_transaction_writer = None
