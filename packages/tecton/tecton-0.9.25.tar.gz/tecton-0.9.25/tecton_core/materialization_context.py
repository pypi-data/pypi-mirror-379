import typing
from dataclasses import dataclass
from typing import Optional
from typing import Union

import pendulum
from typeguard import typechecked

from tecton_core.errors import TectonValidationError


if typing.TYPE_CHECKING:
    import pyspark


@dataclass
class BaseMaterializationContext:
    _feature_start_time_DONT_ACCESS_DIRECTLY: pendulum.DateTime
    _feature_end_time_DONT_ACCESS_DIRECTLY: pendulum.DateTime
    _batch_schedule_DONT_ACCESS_DIRECTLY: pendulum.Duration

    @property
    def start_time(self) -> pendulum.DateTime:
        return self._feature_start_time_DONT_ACCESS_DIRECTLY

    @property
    def end_time(self) -> pendulum.DateTime:
        return self._feature_end_time_DONT_ACCESS_DIRECTLY

    @property
    def batch_schedule(self) -> pendulum.Duration:
        return self._batch_schedule_DONT_ACCESS_DIRECTLY

    @typechecked
    def time_filter_sql(self, timestamp_expr: str) -> str:
        # Use atom string to include the timezone.
        return f"('{self.start_time.to_atom_string()}' <= ({timestamp_expr}) AND ({timestamp_expr}) < '{self.end_time.to_atom_string()}')"

    def time_filter_pyspark(self, timestamp_expr: Union[str, "pyspark.sql.Column"]) -> "pyspark.sql.Column":  # type: ignore
        from pyspark.sql.functions import expr
        from pyspark.sql.functions import lit

        if isinstance(timestamp_expr, str):
            timestamp_expr = expr(timestamp_expr)

        # Use atom string to include the timezone.
        return (lit(self.start_time.to_atom_string()) <= timestamp_expr) & (
            timestamp_expr < lit(self.end_time.to_atom_string())
        )

    def feature_time_filter_pyspark(self, timestamp_expr: Union[str, "pyspark.sql.Column"]) -> "pyspark.sql.Column":  # type: ignore
        return self.time_filter_pyspark(timestamp_expr)

    # EVERTHING BELOW IS DEPRECATED
    @property
    def feature_start_time(self) -> pendulum.DateTime:
        return self._feature_start_time_DONT_ACCESS_DIRECTLY

    @property
    def feature_end_time(self) -> pendulum.DateTime:
        return self._feature_end_time_DONT_ACCESS_DIRECTLY

    @property
    def feature_start_time_string(self) -> str:
        return self.feature_start_time.to_datetime_string()

    @property
    def feature_end_time_string(self) -> str:
        return self.feature_end_time.to_datetime_string()

    @typechecked
    def feature_time_filter_sql(self, timestamp_expr: str) -> str:
        return self.time_filter_sql(timestamp_expr)


@dataclass
class UnboundMaterializationContext(BaseMaterializationContext):
    """
    This is only meant for instantiation in transformation default args. Using it directly will fail.
    """

    @property
    def batch_schedule(self):
        msg = "tecton.materialization_context() must be passed in via a kwarg default only. Instantiation in function body is not allowed."
        raise TectonValidationError(msg)

    @property
    def start_time(self):
        msg = "tecton.materialization_context() must be passed in via a kwarg default only. Instantiation in function body is not allowed."
        raise TectonValidationError(msg)

    @property
    def end_time(self):
        msg = "tecton.materialization_context() must be passed in via a kwarg default only. Instantiation in function body is not allowed."
        raise TectonValidationError(msg)

    @property
    def feature_start_time(self):
        msg = "tecton.materialization_context() must be passed in via a kwarg default only. Instantiation in function body is not allowed."
        raise TectonValidationError(msg)

    @property
    def feature_end_time(self):
        msg = "tecton.materialization_context() must be passed in via a kwarg default only. Instantiation in function body is not allowed."
        raise TectonValidationError(msg)


@dataclass
class BoundMaterializationContext(BaseMaterializationContext):
    @classmethod
    def create(cls, feature_start_time, feature_end_time):
        # user facing version
        return BoundMaterializationContext(
            _feature_start_time_DONT_ACCESS_DIRECTLY=feature_start_time,
            _feature_end_time_DONT_ACCESS_DIRECTLY=feature_end_time,
            # batch_schedule is passed by pipeline helper
            _batch_schedule_DONT_ACCESS_DIRECTLY=pendulum.duration(seconds=0),
        )

    @classmethod
    def _create_internal(cls, feature_start_time, feature_end_time, batch_schedule):
        # should only be used in pipeline_helper
        return BoundMaterializationContext(
            _feature_start_time_DONT_ACCESS_DIRECTLY=feature_start_time,
            _feature_end_time_DONT_ACCESS_DIRECTLY=feature_end_time,
            _batch_schedule_DONT_ACCESS_DIRECTLY=batch_schedule,
        )

    @classmethod
    def _create_from_period(
        cls, feature_time_limits: Optional[pendulum.Period], batch_schedule: pendulum.Duration
    ) -> "BoundMaterializationContext":
        feature_start_time = (
            feature_time_limits.start
            if feature_time_limits is not None
            else pendulum.from_timestamp(0, pendulum.tz.UTC)
        )
        feature_end_time = feature_time_limits.end if feature_time_limits is not None else pendulum.datetime(2100, 1, 1)
        return BoundMaterializationContext(
            _feature_start_time_DONT_ACCESS_DIRECTLY=feature_start_time,
            _feature_end_time_DONT_ACCESS_DIRECTLY=feature_end_time,
            _batch_schedule_DONT_ACCESS_DIRECTLY=batch_schedule,
        )


def materialization_context():
    """
    Used as a default value for a Feature View or Transformation with a materialization context parameter.

    ``context.start_time`` and ``context.end_time`` return a :class:`datetime.datetime` object equal to the beginning and end of the period being materialized respectively. For example for a batch feature view materializing data from May 1st, 2022, ``context.start_time = datetime(2022, 5, 1)`` and ``context.end_time = datetime(2022, 5, 2)``.

    The datetimes can be used in SQL query strings directly (the datetime object will be cast to an atom-formatted timestamp string and inlined as a constant in the SQL query).

    Example usage:

    .. code-block:: python

        from tecton import batch_feature_view, materialization_context
        from datetime import datetime, timedelta

        @batch_feature_view(
            sources=[transactions],
            entities=[user],
            mode='spark_sql',
            batch_schedule=timedelta(days=1),
            feature_start_time=datetime(2020, 10, 10),
        )
        def user_last_transaction_amount(transactions, context=materialization_context()):
            return f'''
                SELECT
                    USER_ID,
                    AMOUNT,
                    TIMESTAMP
                FROM
                    {transactions}
                WHERE TIMESTAMP >= TO_TIMESTAMP("{context.start_time}") -- e.g. TO_TIMESTAMP("2022-05-01T00:00:00+00:00")
                    AND TIMESTAMP < TO_TIMESTAMP("{context.end_time}") -- e.g. TO_TIMESTAMP("2022-05-02T00:00:00+00:00")
                '''
    """
    dummy_time = pendulum.datetime(1970, 1, 1)
    dummy_period = pendulum.duration()
    return UnboundMaterializationContext(
        _feature_start_time_DONT_ACCESS_DIRECTLY=dummy_time,
        _feature_end_time_DONT_ACCESS_DIRECTLY=dummy_time,
        _batch_schedule_DONT_ACCESS_DIRECTLY=dummy_period,
    )
