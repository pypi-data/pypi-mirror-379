from datetime import datetime
from typing import List


class TectonValidationError(ValueError):
    """
    Exception that indicates a problem in validating user inputs against
    the data in the system. Typically recoverable by the user.
    """

    def __init__(self, message, can_drop_traceback=False):
        """
        Traceback of this exception can be potentially dropped by sdk decorators
        if flag is set accordingly.
        """
        super().__init__(message)
        self.can_drop_traceback = can_drop_traceback


class AccessError(ValueError):
    """
    Exception that indicates a problem in accessing raw data. Information about connecting to data sources can be found here:
    https://docs.tecton.ai/docs/setting-up-tecton/connecting-data-sources
    """


class TectonInternalError(RuntimeError):
    """
    Exception that indicates an unexpected error within Tecton.
    Can be persistent or transient. Recovery typically requires involving
    Tecton support.
    """


class InvalidDatabricksTokenError(Exception):
    """
    Exception that indicates user's databricks token is invalid.
    """


class TectonSnowflakeNotImplementedError(NotImplementedError):
    """
    Exception that indicates a feature is not yet implemented with Snowflake compute.
    """


class TectonAPIValidationError(ValueError):
    """
    Exception that indicates a problem in validating user inputs against
    the data in the system. Typically recoverable by the user.
    """


class TectonNotFoundError(Exception):
    """
    Exception that indicates that the user's request cannot be found in the system.
    """


class TectonAPIInaccessibleError(Exception):
    """
    Exception that indicates a problem connecting to Tecton cluster.
    """


class FailedPreconditionError(Exception):
    """
    Exception that indicates some prequisite has not been met (e.g the CLI/SDK needs to be updated).
    """


class FailedDependencyDownloadError(Exception):
    """
    Exception that indicates a failure during dependency download(s) while creating an environment.
    """


def SCHEMA_VALIDATION_INVALID_COLUMNS(
    actual_columns: List[str],
    expected_columns: List[str],
    missing_columns: List[str],
    extraneous_columns: List[str],
) -> TectonValidationError:
    msg = f"Dataframe schema does not match expected schema. Got columns: {', '.join(actual_columns)}. Expected columns: {', '.join(expected_columns)}."
    if missing_columns:
        msg += f" (Missing columns: {', '.join(missing_columns)}.)"
    if extraneous_columns:
        msg += f" (Extraneous columns: {', '.join(extraneous_columns)}.)"
    return TectonValidationError(msg)


def SCHEMA_VALIDATION_COLUMN_TYPE_MISMATCH_ERROR(
    column_name: str, expected_type: str, actual_type: str
) -> TectonValidationError:
    return TectonValidationError(
        f"The schema does not match the resulting dataframe schema. There is a column type mismatch for column '{column_name}', expected {expected_type}, got {actual_type}"
    )


def UDF_ERROR(error: Exception) -> TectonValidationError:
    return TectonValidationError(
        "UDF Error: please review and ensure the correctness of your feature definition and the input data passed in. Otherwise please contact Tecton Support for assistance."
        + f" Running the transformation resulted in the following error: {type(error).__name__}: {str(error)} "
    )


def UDF_TYPE_ERROR(error: Exception) -> TectonValidationError:
    return TectonValidationError(
        "UDF Type Error: please ensure that your UDF correctly handles the typing of row values. Make sure to cast dataframe values to the correct type and ensure that you are handling"
        + f" null column values correctly in your UDF. Running the transformation resulted in the following error: {type(error).__name__}: {str(error)} "
    )


def MISSING_SNOWFAKE_CONNECTION_REQUIREMENTS(param: str) -> TectonValidationError:
    return TectonValidationError(
        f"Snowflake connection is missing the variable {param}. Please ensure the following parameters are set when creating your snowflake connection:  database, warehouse, and schema. "
    )


def INVALID_SPINE_SQL(error: Exception) -> TectonValidationError:
    return TectonValidationError(
        f"Invalid SQL: please review your SQL for the spine passed in. Received error: {type(error).__name__}: {str(error)} "
    )


def START_TIME_NOT_BEFORE_END_TIME(start_time: datetime, end_time: datetime) -> TectonValidationError:
    return TectonValidationError(f"start_time ({start_time}) must be less than end_time ({end_time}).")


def DS_ARGS_MISSING_FIELD(ds_type: str, field: str) -> TectonValidationError:
    return TectonValidationError(f"{ds_type} data source args must contain field {field}.")


REDSHIFT_DS_EITHER_TABLE_OR_QUERY = TectonValidationError(
    "Redshift data source must contain either table or query, but not both."
)


REDSHIFT_DS_MISSING_SPARK_TEMP_DIR = TectonValidationError(
    'Cannot use a locally defined Redshift data source without a tempdir, e.g. spark.read.format("redshift").option("tempdir", "s3a:///"). See the tempdir that Tecton should use via tecton.conf.set("SPARK_REDSHIFT_TEMP_DIR", <your path>) or by setting the SPARK_REDSHIFT_TEMP_DIR= as an environment variable.'
)


class TectonAthenaValidationError(TectonValidationError):
    """
    Exception that indicates a ValidationError with Athena.
    """


class TectonAthenaNotImplementedError(NotImplementedError):
    """
    Exception that indicates a feature is not yet implemented with Athena compute.
    """


FV_BFC_SINGLE_FROM_SOURCE = TectonValidationError(
    "Computing features from source is not supported for Batch Feature Views with incremental_backfills set to True. "
    + "Enable offline materialization for this feature view in a live workspace to use `get_historical_features()`. Alternatively, use `run()` to test this feature view without materializing data."
)


def FV_NEEDS_TO_BE_MATERIALIZED(fv_name: str) -> TectonValidationError:
    return TectonValidationError(
        f"Feature View '{fv_name}' has not been configured for materialization. "
        + "Please use from_source=True when getting features or "
        + "configure offline materialization for this Feature View in a live workspace."
    )


FT_DF_TOO_LARGE = TectonValidationError(
    "Dataframe too large for a single ingestion, consider splitting into smaller ones"
)


def FT_UPLOAD_FAILED(reason: str) -> TectonValidationError:
    return TectonValidationError(f"Failed to upload dataframe: {reason}")


SNOWFLAKE_CONNECTION_NOT_SET = TectonValidationError(
    "Snowflake connection not configured. Please set Snowflake connection using tecton.snowflake_context.set_connection(connection). https://docs.tecton.ai/docs/setting-up-tecton/connecting-to-a-data-platform/tecton-on-snowflake/connecting-notebooks-to-snowflake"
)
