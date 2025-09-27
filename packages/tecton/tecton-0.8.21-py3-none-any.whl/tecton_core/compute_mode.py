from enum import Enum
from typing import Optional
from typing import Union

from tecton_core import conf
from tecton_core.errors import TectonValidationError
from tecton_core.query.dialect import Dialect
from tecton_proto.common import compute_mode_pb2


class ComputeMode(str, Enum):
    """Represents the compute mode for training data generation queries."""

    SPARK = "spark"
    SNOWFLAKE = "snowflake"
    ATHENA = "athena"
    RIFT = "rift"

    def default_dialect(self) -> Dialect:
        return _COMPUTE_MODE_TO_DIALECT[self]


_COMPUTE_MODE_TO_DIALECT = {
    ComputeMode.SPARK: Dialect.SPARK,
    ComputeMode.SNOWFLAKE: Dialect.SNOWFLAKE,
    ComputeMode.ATHENA: Dialect.ATHENA,
    ComputeMode.RIFT: Dialect.DUCKDB,
}


class ComputeModeValueError(ValueError):
    def __init__(self, compute_mode_str: str) -> None:
        msg = f"Invalid compute mode: {compute_mode_str}. Must be one of {[e.value for e in ComputeMode]}"
        super().__init__(msg)


def _parse_compute_mode(compute_mode_str: str) -> ComputeMode:
    try:
        return ComputeMode(compute_mode_str.lower())
    except ValueError:
        raise ComputeModeValueError(compute_mode_str)


def _default_offline_retrieval_compute_mode() -> ComputeMode:
    offline_retrieval_mode = conf.get_or_none("TECTON_OFFLINE_RETRIEVAL_COMPUTE_MODE")
    if offline_retrieval_mode is not None:
        return _parse_compute_mode(offline_retrieval_mode)
    else:
        # TODO(meastham): Delete me after #16346 is released and we're confident it won't roll back
        compute_mode = conf.get_or_raise("TECTON_COMPUTE_MODE")
        if compute_mode == ComputeMode.RIFT:
            return ComputeMode.RIFT
        elif conf.get_bool("ALPHA_SNOWFLAKE_COMPUTE_ENABLED") or compute_mode == ComputeMode.SNOWFLAKE:
            return ComputeMode.SNOWFLAKE
        elif conf.get_bool("ALPHA_ATHENA_COMPUTE_ENABLED") or compute_mode == ComputeMode.ATHENA:
            return ComputeMode.ATHENA
        elif compute_mode == ComputeMode.SPARK:
            return ComputeMode.SPARK
        else:
            raise ComputeModeValueError(compute_mode)


def offline_retrieval_compute_mode(raw_function_override: Optional[Union[ComputeMode, str]]) -> ComputeMode:
    """Returns offline retrieval compute mode based on the given function-level override and the environment."""
    default = _default_offline_retrieval_compute_mode()
    if raw_function_override is not None:
        function_override = _parse_compute_mode(raw_function_override)
        if function_override == ComputeMode.SNOWFLAKE and default != ComputeMode.SNOWFLAKE:
            raise TectonValidationError(
                "Snowflake offline retrieval cannot be enabled at a function level; it must be enabled globally. "
                + "Try setting TECTON_OFFLINE_RETRIEVAL_MODE to snowflake in your environment variables, "
                + 'or running tecton.conf.set("TECTON_OFFLINE_RETRIEVAL_MODE", "snowflake"))'
            )
        if function_override != ComputeMode.SNOWFLAKE and default == ComputeMode.SNOWFLAKE:
            raise TectonValidationError(
                "Snowflake offline retrieval cannot be overridden at a function level when it is enabled globally. "
                + f"Try setting TECTON_OFFLINE_RETRIEVAL_MODE to {function_override.value} in your environment variables, "
                + f'or running tecton.conf.set("TECTON_OFFLINE_RETRIEVAL_MODE", "{function_override.value}"))'
            )
        return function_override
    else:
        return default


class BatchComputeMode(Enum):
    """Represents that compute mode for batch jobs associated with a FeatureView."""

    SPARK = compute_mode_pb2.BatchComputeMode.BATCH_COMPUTE_MODE_SPARK
    SNOWFLAKE = compute_mode_pb2.BatchComputeMode.BATCH_COMPUTE_MODE_SNOWFLAKE
    RIFT = compute_mode_pb2.BatchComputeMode.BATCH_COMPUTE_MODE_RIFT

    @property
    def value(self) -> compute_mode_pb2.BatchComputeMode:
        return super().value


_COMPUTE_MODE_TO_BATCH = {
    ComputeMode.SPARK: BatchComputeMode.SPARK,
    ComputeMode.SNOWFLAKE: BatchComputeMode.SNOWFLAKE,
    ComputeMode.RIFT: BatchComputeMode.RIFT,
}

_STR_TO_BATCH = {
    "spark": BatchComputeMode.SPARK,
    "snowflake": BatchComputeMode.SNOWFLAKE,
    "rift": BatchComputeMode.RIFT,
}


def default_batch_compute_mode() -> BatchComputeMode:
    compute_mode = conf.get_or_none("TECTON_BATCH_COMPUTE_MODE")
    if compute_mode is not None:
        return _STR_TO_BATCH[compute_mode.lower()]
    else:
        # TODO(meastham): Delete me after #16346 is released and we're confident it won't roll back
        return _COMPUTE_MODE_TO_BATCH[_default_offline_retrieval_compute_mode()]
