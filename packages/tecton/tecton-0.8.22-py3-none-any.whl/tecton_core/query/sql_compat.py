import typing
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Union

import pypika
from pypika import AliasedQuery
from pypika import Field
from pypika import Interval
from pypika import Table
from pypika import analytics
from pypika.dialects import MySQLQuery
from pypika.dialects import PostgreSQLQuery
from pypika.dialects import SnowflakeQuery
from pypika.functions import Cast
from pypika.functions import DateAdd
from pypika.functions import Floor
from pypika.queries import Query
from pypika.queries import Selectable
from pypika.terms import AnalyticFunction
from pypika.terms import Function
from pypika.terms import LiteralValue
from pypika.terms import Term
from pypika.utils import format_alias_sql

from tecton_core.compute_mode import ComputeMode
from tecton_core.compute_mode import offline_retrieval_compute_mode
from tecton_core.data_types import DataType
from tecton_core.query.dialect import Dialect
from tecton_proto.data.feature_store_pb2 import FeatureStoreFormatVersion


class CaseSensitiveSnowflakeQueryBuilder(pypika.dialects.SnowflakeQueryBuilder):
    QUOTE_CHAR = '"'


class CaseSensitiveSnowflakeQuery(pypika.queries.Query):
    @classmethod
    def _builder(cls, **kwargs: Any) -> CaseSensitiveSnowflakeQueryBuilder:
        return CaseSensitiveSnowflakeQueryBuilder(**kwargs)


class DuckDBQuery(pypika.queries.Query):
    @classmethod
    def _builder(cls, **kwargs: Any) -> "DuckDBQueryBuilder":
        return DuckDBQueryBuilder(**kwargs)


class DuckDBQueryBuilder(pypika.dialects.PostgreSQLQueryBuilder):
    ALIAS_QUOTE_CHAR = None

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(as_keyword=True, **kwargs)


class CaseInsensitiveSnowflakeQueryBuilder(pypika.dialects.SnowflakeQueryBuilder):
    QUOTE_CHAR = None
    ALIAS_QUOTE_CHAR = None
    QUERY_ALIAS_QUOTE_CHAR = ""
    QUERY_CLS = SnowflakeQuery


class CaseInsensitiveSnowflakeQuery(pypika.queries.Query):
    @classmethod
    def _builder(cls, **kwargs: Any) -> CaseInsensitiveSnowflakeQueryBuilder:
        return CaseInsensitiveSnowflakeQueryBuilder(**kwargs)


class CustomQuery(pypika.queries.QueryBuilder):
    """
    Defines a custom-query class. It's needed for us to wrap some user-defined sql string from transformations in a QueryBuilder object.
    """

    def __init__(self, sql: str) -> None:
        super().__init__()
        self.sql = sql
        self.withs: List[Selectable] = []

    def with_(self, selectable: Selectable, name: str) -> "CustomQuery":
        """
        overrides QueryBuilder.with_
        """
        t = AliasedQuery(name, selectable)
        self.withs.append(t)
        return self

    def get_sql(self, with_alias: bool = False, subquery: bool = False, **kwargs: Any) -> str:
        """
        overrides QueryBuilder.get_sql
        """
        sql = ""
        if self.withs:
            sql += "WITH " + ",".join(
                clause.name + " AS (" + clause.get_sql(subquery=False, with_alias=False, **kwargs) + ") "
                for clause in self.withs
            )
        sql += self.sql
        if with_alias:
            self.alias = "sq0"
            sql = f"({sql})"
            return format_alias_sql(sql, self.alias or self._table_name, **kwargs)
        return sql


class LastValue(analytics.LastValue):
    """
    Fixed version of pypika's LastValue to handle Snowflake and Athena wanting "ignore nulls"
     to be outside the parens of the window func, and Spark using a bool param.
    """

    def __init__(self, dialect: "Dialect", *args: Any, **kwargs: Any) -> None:
        self._dialect = dialect
        super().__init__(*args, **kwargs)

    def get_special_params_sql(self, **kwargs: Any) -> Optional[str]:
        if self._dialect == Dialect.SPARK:
            # see: https://docs.databricks.com/sql/language-manual/functions/last_value.html
            # for sparkSQL syntax
            return f", {self._ignore_nulls}"
        elif self._dialect == Dialect.DUCKDB and self._ignore_nulls:
            # see: https://duckdb.org/docs/sql/window_functions.html
            # for DuckDB syntax
            return " IGNORE NULLS"
        # Snowflake does not support adding a function param to indicate "ignore nulls"
        # It looks like LAST_VALUE(...) IGNORE NULLS OVER(...)
        # see: https://docs.snowflake.com/en/sql-reference/functions/last_value.html
        # Nor does Athena - Athena docs don't make this clear though.
        else:
            return None

    def get_function_sql(self, **kwargs: Any) -> str:
        if self._dialect == Dialect.SPARK or self._dialect == Dialect.DUCKDB:
            return super(LastValue, self).get_function_sql(**kwargs)
        else:
            function_sql = super(AnalyticFunction, self).get_function_sql(**kwargs)
            partition_sql = self.get_partition_sql(**kwargs)

            sql = function_sql
            if self._ignore_nulls:
                sql += " IGNORE NULLS"
            if self._include_over:
                sql += " OVER({partition_sql})".format(partition_sql=partition_sql)
            return sql


class CompatFunctions:
    def __init__(self, compute_mode: ComputeMode) -> None:
        self.compute_mode = compute_mode

    @staticmethod
    def for_dialect(d: Dialect, compute_mode: Optional[ComputeMode] = None) -> "CompatFunctions":
        compute_mode = offline_retrieval_compute_mode(compute_mode)
        if d == Dialect.SPARK:
            return _Spark(compute_mode=compute_mode)
        elif d == Dialect.DUCKDB:
            return _DuckDB(compute_mode=compute_mode)
        elif d == Dialect.SNOWFLAKE:
            return _Snowflake(compute_mode=compute_mode)
        elif d == Dialect.ATHENA:
            return _Athena(compute_mode=compute_mode)
        msg = f"Unexpected dialect {d}"
        raise Exception(msg)

    @classmethod
    def query(cls) -> typing.Type[Query]:
        raise NotImplementedError()

    @classmethod
    def struct(cls, field_names: List[str]) -> Term:
        raise NotImplementedError()

    @classmethod
    def struct_extract(
        cls, name: str, field_names: List[str], aliases: List[str], schema: Dict[str, DataType]
    ) -> List[Field]:
        raise NotImplementedError()

    @classmethod
    def to_timestamp(cls, time_str: str) -> Term:
        raise NotImplementedError()

    @classmethod
    def date_add(cls, interval: str, amount: int, time_field: Term) -> Term:
        raise NotImplementedError()

    @classmethod
    def to_unixtime(cls, timestamp: Term) -> Term:
        raise NotImplementedError()

    @classmethod
    def to_utc(cls, timestamp: Term) -> Term:
        raise NotImplementedError()

    @classmethod
    def from_unixtime(cls, unix_timestamp: Term) -> Term:
        raise NotImplementedError()

    @classmethod
    def strftime(cls, timestamp: Term, fmt: Union[Term, str]) -> Term:
        raise NotImplementedError()

    @classmethod
    def int_div(cls, a: Union[Term, int], b: Union[Term, int]) -> Term:
        raise NotImplementedError()

    @classmethod
    def convert_epoch_term_in_seconds(
        cls, timestamp: Term, time_stamp_feature_store_format_version: FeatureStoreFormatVersion
    ) -> Term:
        """
        Converts an epoch term to a timestamp column
        :param timestamp: epoch column [V0 : Seconds, V1 : Nanoseconds]
        :param time_stamp_feature_store_format_version: Feature Store Format Version
        :return: epoch in seconds
        """
        if time_stamp_feature_store_format_version == FeatureStoreFormatVersion.FEATURE_STORE_FORMAT_VERSION_DEFAULT:
            return timestamp
        # Cast explicitly to an integer (which is the expectation), since otherwise SQL will often treat integer
        # division as outputting a double, which is incompatible with to_timestamp(epoch_seconds) functions
        return Cast(timestamp / int(1e9), as_type="bigint")

    @classmethod
    def convert_epoch_seconds_to_feature_store_format_version(
        cls, timestamp: Term, feature_store_format_version: FeatureStoreFormatVersion
    ) -> Term:
        if feature_store_format_version == FeatureStoreFormatVersion.FEATURE_STORE_FORMAT_VERSION_DEFAULT:
            return timestamp
        return timestamp * int(1e9)


class _Snowflake(CompatFunctions):
    def query(self) -> typing.Type[Query]:
        # Compute.SNOWFLAKE is "legacy" snowflake, executing snowflake queries in unified Tecton mode will have
        # ComputeMode.DUCK_DB
        return (
            CaseInsensitiveSnowflakeQuery if self.compute_mode == ComputeMode.SNOWFLAKE else CaseSensitiveSnowflakeQuery
        )

    @classmethod
    def struct(cls, field_names: List[str]) -> Term:
        return Function("array_construct", *[Field(n) for n in field_names])

    @classmethod
    def struct_extract(
        cls, name: str, field_names: List[str], aliases: List[str], schema: Dict[str, DataType]
    ) -> List[Field]:
        res = []
        for idx in range(len(aliases)):
            val = Function("get", Field(name), idx)
            if field_names[idx] in schema:
                feature_type = schema[field_names[idx]].sql_type
                val = Cast(val, feature_type)
            res.append(val.as_(aliases[idx]))
        return res

    @classmethod
    def to_timestamp(cls, time_str: str) -> Term:
        return Function("to_timestamp", time_str)

    @classmethod
    def date_add(cls, interval: str, amount: int, time_field: Term) -> Term:
        # snowflake uses dateadd rather than date_add;
        # https://docs.snowflake.com/en/sql-reference/functions/dateadd.html

        # LiteralValue will not put quotes around.
        # So we get dateadd(second, ...)
        interval = LiteralValue(interval)
        return Function("dateadd", interval, amount, time_field)

    @classmethod
    def to_unixtime(cls, timestamp: Term) -> Term:
        return Function("date_part", Field("epoch_second"), timestamp)

    @classmethod
    def from_unixtime(cls, unix_timestamp: Term) -> Term:
        return Function("to_timestamp", unix_timestamp)

    @classmethod
    def strftime(cls, timestamp: Term, fmt: Union[Term, str]) -> Term:
        raise NotImplementedError()

    @classmethod
    def int_div(cls, a: Union[Term, int], b: Union[Term, int]) -> Term:
        raise NotImplementedError()


class DuckDBStruct(Term):
    def __init__(self, *fields: Field) -> None:
        super().__init__()
        self.fields = fields

    def get_sql(self, **kwargs: Any) -> str:
        """
        Returns explicit form of struct definition (ie, {"colum": "column"})
        since row function is loosing keys starting 0.9.0
        """
        sql = "{{{}}}".format(",".join(f"{term.get_sql(**kwargs)}: {term.get_sql(**kwargs)}" for term in self.fields))
        return format_alias_sql(sql, self.alias, **kwargs)


class _DuckDB(CompatFunctions):
    @classmethod
    def query(cls) -> typing.Type[Query]:
        return DuckDBQuery

    @classmethod
    def struct(cls, field_names: List[str]) -> Term:
        return DuckDBStruct(*[Field(n) for n in field_names])

    @classmethod
    def struct_extract(
        cls, name: str, field_names: List[str], aliases: List[str], schema: Dict[str, DataType]
    ) -> List[Field]:
        assert len(field_names) == len(aliases)
        return [getattr(Table(name), field).as_(alias) for (field, alias) in zip(field_names, aliases)]

    @classmethod
    def to_timestamp(cls, time_col: Union[Term, str]) -> Term:
        return Cast(time_col, as_type="timestamp")

    @classmethod
    def date_add(cls, interval: str, amount: int, time_field: Term) -> Term:
        return _Spark.date_add(interval, amount, time_field)

    @classmethod
    def to_unixtime(cls, timestamp: Term) -> Term:
        return Cast(Floor(Function("date_part", "epoch", cls.to_timestamp(timestamp))), as_type="int64")

    @classmethod
    def to_utc(cls, timestamp: Term) -> Term:
        return Function("timezone", "UTC", timestamp)

    @classmethod
    def from_unixtime(cls, unix_timestamp: Term) -> Term:
        """
        Function `to_timestamp` returns timezone-aware results starting version 0.9.0.
        That's why we need to cast it to Timestamp (w/o timezone).
        We rely on the fact that DuckDB global timezone is set to UTC in DuckDBCompute.
        """
        return Cast(Function("to_timestamp", unix_timestamp), as_type="timestamp")

    @classmethod
    def int_div(cls, a: Union[Term, int], b: Union[Term, int]) -> Term:
        return Function("_tecton_int_div", a, b)

    @classmethod
    def strftime(cls, timestamp: Term, fmt: Union[Term, str]) -> Term:
        return Function("strftime", timestamp, fmt)


class _Spark(CompatFunctions):
    @classmethod
    def query(cls) -> typing.Type[Query]:
        # Spark (similar to HiveSQL) uses backticks like MySQL
        return MySQLQuery

    @classmethod
    def struct(cls, field_names: List[str]) -> Term:
        return Function("struct", *[Field(n) for n in field_names])

    @classmethod
    def struct_extract(
        cls, name: str, field_names: List[str], aliases: List[str], schema: Dict[str, DataType]
    ) -> List[Field]:
        assert len(field_names) == len(aliases)
        return [getattr(Table(name), field).as_(alias) for (field, alias) in zip(field_names, aliases)]

    @classmethod
    def to_timestamp(cls, time_str: str) -> Term:
        return Function("to_timestamp", time_str)

    @classmethod
    def date_add(cls, interval: str, amount: int, time_field: Term) -> Term:
        if interval == "second":
            return time_field + Interval(seconds=amount)
        elif interval == "millisecond":
            # Note: PyPika has a bug where for microseconds, it does not correctly respect negative values
            if amount >= 0:
                return time_field + Interval(microseconds=amount * 1000)
            else:
                return time_field - Interval(microseconds=abs(amount) * 1000)
        else:
            msg = f"Unexpected date_add interval {interval}"
            raise NotImplementedError(msg)

    @classmethod
    def to_unixtime(cls, timestamp: Term) -> Term:
        return Function("unix_timestamp", timestamp)

    @classmethod
    def from_unixtime(cls, unix_timestamp: Term) -> Term:
        return Cast(Function("from_unixtime", unix_timestamp), as_type="timestamp")

    @classmethod
    def strftime(cls, timestamp: Term, fmt: Union[Term, str]) -> Term:
        raise NotImplementedError()

    @classmethod
    def int_div(cls, a: Union[Term, int], b: Union[Term, int]) -> Term:
        raise NotImplementedError()


class _Athena(CompatFunctions):
    @classmethod
    def query(cls) -> typing.Type[Query]:
        # Athena (similar to PrestoSQL) uses doublequotes like Postgres
        return PostgreSQLQuery

    @classmethod
    def struct(cls, field_names: List[str]) -> Term:
        return Function("row", *[Field(n) for n in field_names])

    @classmethod
    def struct_extract(
        cls, name: str, field_names: List[str], aliases: List[str], schema: Dict[str, DataType]
    ) -> List[Field]:
        return [getattr(Table(name), f"field{idx}").as_(aliases[idx]) for idx in range(len(aliases))]

    @classmethod
    def to_timestamp(cls, time_str: str) -> Term:
        return Function("from_iso8601_timestamp", time_str)

    @classmethod
    def date_add(cls, interval: str, amount: int, time_field: Term) -> Term:
        interval = f"'{interval}'"
        return DateAdd(interval, amount, time_field)

    @classmethod
    def to_unixtime(cls, timestamp: Term) -> Term:
        return Function("to_unixtime", timestamp)

    @classmethod
    def from_unixtime(cls, unix_timestamp: Term) -> Term:
        return Function("from_unixtime", unix_timestamp)

    @classmethod
    def strftime(cls, timestamp: Term, fmt: Union[Term, str]) -> Term:
        raise NotImplementedError()

    @classmethod
    def int_div(cls, a: Union[Term, int], b: Union[Term, int]) -> Term:
        raise NotImplementedError()
