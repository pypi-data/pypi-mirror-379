import logging
import time
from typing import Optional

import pyspark
from pyspark.sql import SparkSession

from tecton_core import specs
from tecton_core.feature_definition_wrapper import FeatureDefinitionWrapper as FeatureDefinition
from tecton_core.id_helper import IdHelper
from tecton_materialization.job_metadata import get_job_exec
from tecton_materialization.job_metadata import update_job_exec
from tecton_materialization.materialization_utils import df_to_online_store_msg
from tecton_materialization.materialization_utils import fco_container_from_task_params
from tecton_materialization.materialization_utils import set_up_online_store_sink
from tecton_proto.materialization.job_metadata_pb2 import JobMetadata
from tecton_proto.materialization.params_pb2 import MaterializationTaskParams
from tecton_spark import materialization_plan


logger = logging.getLogger(__name__)


def _start_stream_job_with_online_store_sink(
    spark: SparkSession, dataframe, materialization_task_params, sink
) -> "pyspark.sql.streaming.StreamingQuery":
    canary_id = materialization_task_params.canary_id if materialization_task_params.HasField("canary_id") else None
    # TODO(amargvela): For SFV add feature timestamp as MATERIALIZED_RAW_DATA_END_TIME column.
    fco_container = fco_container_from_task_params(materialization_task_params)
    fv_spec = specs.create_feature_view_spec_from_data_proto(materialization_task_params.feature_view)
    fd = FeatureDefinition(fv_spec, fco_container)

    stream_task_info = materialization_task_params.stream_task_info

    if stream_task_info.HasField("streaming_trigger_interval_override"):
        processing_time = stream_task_info.streaming_trigger_interval_override
    elif fd.is_continuous:
        processing_time = "0 seconds"
    else:
        processing_time = "30 seconds"

    write_df = df_to_online_store_msg(dataframe, fd.id, is_batch=False, is_status=False, canary_id=canary_id)

    logger.info(f"Starting stream write to Tecton Online Store for FV {fd.id}")
    trigger = spark._jvm.org.apache.spark.sql.streaming.Trigger.ProcessingTime(processing_time)
    writer = (
        write_df._jdf.writeStream()
        .queryName("tecton_osw_sink")
        .foreach(sink)
        .option(
            "checkpointLocation", f"{stream_task_info.streaming_checkpoint_path}-k"
        )  # append -k to differentiate from Dynamo checkpoint path; keep this in sync with the Canary process.
        .outputMode("update")
        .trigger(trigger)
    )
    return writer.start()


def _start_stream_materialization(
    spark: SparkSession,
    materialization_task_params: MaterializationTaskParams,
    sink,
) -> "pyspark.sql.streaming.StreamingQuery":
    logger.info(
        f"Starting materialization task {materialization_task_params.materialization_task_id} for feature view {IdHelper.to_string(materialization_task_params.feature_view.feature_view_id)}"
    )

    fco_container = fco_container_from_task_params(materialization_task_params)
    fv_spec = specs.create_feature_view_spec_from_data_proto(materialization_task_params.feature_view)
    fd = FeatureDefinition(fv_spec, fco_container)

    plan = materialization_plan.get_stream_materialization_plan(
        spark=spark,
        feature_definition=fd,
    )
    spark_df = plan.online_store_data_frame

    _handle_stream_handoff(materialization_task_params)

    online_store_query = _start_stream_job_with_online_store_sink(spark, spark_df, materialization_task_params, sink)

    return online_store_query


def _watch_stream_query(
    materialization_task_params: MaterializationTaskParams, stream_query: "pyspark.sql.streaming.StreamingQuery"
):
    def set_terminated_state(job_metadata: JobMetadata) -> Optional[JobMetadata]:
        new_proto = JobMetadata()
        new_proto.CopyFrom(job_metadata)
        new_proto.spark_execution_info.stream_handoff_synchronization_info.query_cancellation_complete = True
        return new_proto

    stream_params = materialization_task_params.stream_task_info.stream_parameters
    if stream_params.stream_handoff_config.enabled:
        while stream_query.isActive():
            job_metadata, _ = get_job_exec(materialization_task_params)
            # check if the materialization task has been cancelled
            if job_metadata.spark_execution_info.stream_handoff_synchronization_info.query_cancellation_requested:
                logger.info("Stream query cancellation requested. Stopping stream query.")
                try:
                    stream_query.stop()
                    stream_query.awaitTermination()
                finally:
                    logger.info("Query cancellation complete")
                    update_job_exec(materialization_task_params, set_terminated_state)
                return
            time.sleep(60)
        # returns immediately or throws exception, given that isActive() is false
        stream_query.awaitTermination()
    else:
        stream_query.awaitTermination()


def _handle_stream_handoff(materialization_task_params):
    """
    If stream handoff is enabled, we need to wait for the previous job to finish before starting the next one.
    """

    def set_ready_state(job_metadata: JobMetadata) -> Optional[JobMetadata]:
        new_proto = JobMetadata()
        new_proto.CopyFrom(job_metadata)
        new_proto.spark_execution_info.stream_handoff_synchronization_info.new_cluster_started = True
        return new_proto

    if materialization_task_params.stream_task_info.stream_parameters.stream_handoff_config.enabled:
        start_time = time.time()
        update_job_exec(materialization_task_params, set_ready_state)
        logger.info("Using stream handoff; waiting for ready state...")
        job_metadata, _ = get_job_exec(materialization_task_params)
        while not job_metadata.spark_execution_info.stream_handoff_synchronization_info.stream_query_start_allowed:
            if time.time() - start_time > 3600.0:
                msg = "Timed out waiting for ready state"
                raise Exception(msg)
            time.sleep(1)
            job_metadata, _ = get_job_exec(materialization_task_params)
        logger.info("Ready state reached; starting streaming query")


def stream_materialize_from_params(
    spark: SparkSession,
    materialization_task_params: MaterializationTaskParams,
):
    sink = set_up_online_store_sink(spark, materialization_task_params)
    online_store_sink = _start_stream_materialization(spark, materialization_task_params, sink)

    should_publish_stream_metrics = spark.conf.get("spark.tecton.publish_stream_metrics", "true") == "true"

    if should_publish_stream_metrics:
        metricsReportingListener = spark._jvm.com.tecton.onlinestorewriter.MetricsReportingListener(
            materialization_task_params.SerializeToString()
        )
        spark.streams._jsqm.addListener(metricsReportingListener)

    _watch_stream_query(materialization_task_params, online_store_sink)
    if sink is not None:
        sink.closeGlobalResources()
