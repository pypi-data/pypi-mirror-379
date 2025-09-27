# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_datapipeline import type_defs as bs_td


class DATAPIPELINECaster:

    def create_pipeline(
        self,
        res: "bs_td.CreatePipelineOutputTypeDef",
    ) -> "dc_td.CreatePipelineOutput":
        return dc_td.CreatePipelineOutput.make_one(res)

    def delete_pipeline(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def describe_objects(
        self,
        res: "bs_td.DescribeObjectsOutputTypeDef",
    ) -> "dc_td.DescribeObjectsOutput":
        return dc_td.DescribeObjectsOutput.make_one(res)

    def describe_pipelines(
        self,
        res: "bs_td.DescribePipelinesOutputTypeDef",
    ) -> "dc_td.DescribePipelinesOutput":
        return dc_td.DescribePipelinesOutput.make_one(res)

    def evaluate_expression(
        self,
        res: "bs_td.EvaluateExpressionOutputTypeDef",
    ) -> "dc_td.EvaluateExpressionOutput":
        return dc_td.EvaluateExpressionOutput.make_one(res)

    def get_pipeline_definition(
        self,
        res: "bs_td.GetPipelineDefinitionOutputTypeDef",
    ) -> "dc_td.GetPipelineDefinitionOutput":
        return dc_td.GetPipelineDefinitionOutput.make_one(res)

    def list_pipelines(
        self,
        res: "bs_td.ListPipelinesOutputTypeDef",
    ) -> "dc_td.ListPipelinesOutput":
        return dc_td.ListPipelinesOutput.make_one(res)

    def poll_for_task(
        self,
        res: "bs_td.PollForTaskOutputTypeDef",
    ) -> "dc_td.PollForTaskOutput":
        return dc_td.PollForTaskOutput.make_one(res)

    def put_pipeline_definition(
        self,
        res: "bs_td.PutPipelineDefinitionOutputTypeDef",
    ) -> "dc_td.PutPipelineDefinitionOutput":
        return dc_td.PutPipelineDefinitionOutput.make_one(res)

    def query_objects(
        self,
        res: "bs_td.QueryObjectsOutputTypeDef",
    ) -> "dc_td.QueryObjectsOutput":
        return dc_td.QueryObjectsOutput.make_one(res)

    def report_task_progress(
        self,
        res: "bs_td.ReportTaskProgressOutputTypeDef",
    ) -> "dc_td.ReportTaskProgressOutput":
        return dc_td.ReportTaskProgressOutput.make_one(res)

    def report_task_runner_heartbeat(
        self,
        res: "bs_td.ReportTaskRunnerHeartbeatOutputTypeDef",
    ) -> "dc_td.ReportTaskRunnerHeartbeatOutput":
        return dc_td.ReportTaskRunnerHeartbeatOutput.make_one(res)

    def set_status(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def validate_pipeline_definition(
        self,
        res: "bs_td.ValidatePipelineDefinitionOutputTypeDef",
    ) -> "dc_td.ValidatePipelineDefinitionOutput":
        return dc_td.ValidatePipelineDefinitionOutput.make_one(res)


datapipeline_caster = DATAPIPELINECaster()
