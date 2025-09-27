import logging
from datetime import datetime
from typing import Dict
from typing import Optional

import attrs
import pendulum
import pyspark

from tecton_core import specs
from tecton_core.feature_definition_wrapper import FeatureDefinitionWrapper
from tecton_core.query.node_interface import DataframeWrapper
from tecton_proto.args.pipeline_pb2 import DataSourceNode
from tecton_spark import data_source_helper
from tecton_spark import offline_store
from tecton_spark.query.node import SparkExecNode


logger = logging.getLogger(__name__)


@attrs.frozen
class UserSpecifiedDataSparkNode(SparkExecNode):
    data: DataframeWrapper
    metadata: Optional[Dict[str, any]]

    def _to_dataframe(self, spark: pyspark.sql.SparkSession) -> pyspark.sql.DataFrame:
        return self.data.to_spark()


@attrs.frozen
class DataSparkNode(SparkExecNode):
    data: DataframeWrapper
    metadata: Optional[Dict[str, any]]

    def _to_dataframe(self, spark: pyspark.sql.SparkSession) -> pyspark.sql.DataFrame:
        return self.data.to_spark()


@attrs.frozen
class MockDataSourceScanSparkNode(SparkExecNode):
    data: SparkExecNode
    ds: specs.DataSourceSpec
    start_time: Optional[datetime]
    end_time: Optional[datetime]

    def _to_dataframe(self, spark: pyspark.sql.SparkSession) -> pyspark.sql.DataFrame:
        df = self.data.to_dataframe(spark)
        df = data_source_helper.apply_partition_and_timestamp_filter(
            df, self.ds.batch_source, self.start_time, self.end_time
        )
        return df


@attrs.frozen
class DataSourceScanSparkNode(SparkExecNode):
    ds: specs.DataSourceSpec
    is_stream: bool
    start_time: Optional[datetime]
    end_time: Optional[datetime]
    ds_node: Optional[DataSourceNode]

    def _to_dataframe(self, spark: pyspark.sql.SparkSession) -> pyspark.sql.DataFrame:
        df = data_source_helper.get_ds_dataframe(
            spark,
            self.ds,
            consume_streaming_data_source=self.is_stream,
            start_time=self.start_time,
            end_time=self.end_time,
        )
        return df


# This is used for debugging method.
@attrs.frozen
class RawDataSourceScanSparkNode(SparkExecNode):
    ds: specs.DataSourceSpec

    def _to_dataframe(self, spark: pyspark.sql.SparkSession) -> pyspark.sql.DataFrame:
        df = data_source_helper.get_non_dsf_raw_dataframe(spark, self.ds.batch_source)
        return df


@attrs.frozen
class OfflineStoreScanSparkNode(SparkExecNode):
    feature_definition_wrapper: FeatureDefinitionWrapper
    partition_time_filter: Optional[pendulum.Period]

    def _to_dataframe(self, spark: pyspark.sql.SparkSession) -> pyspark.sql.DataFrame:
        offline_reader = offline_store.get_offline_store_reader(spark, self.feature_definition_wrapper)
        try:
            # None implies no timestamp filtering. When we implement time filter pushdown, it will go here
            df = offline_reader.read(self.partition_time_filter)
            return df
        except pyspark.sql.utils.AnalysisException as e:
            logger.warning(
                f"Failed to read from the Offline Store. Please ensure that materialization backfills have completed for Feature View '{self.feature_definition_wrapper.name}' or set `from_source=True`."
            )
            raise e
