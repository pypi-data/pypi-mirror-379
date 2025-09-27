# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_codepipeline import type_defs as bs_td


class CODEPIPELINECaster:

    def acknowledge_job(
        self,
        res: "bs_td.AcknowledgeJobOutputTypeDef",
    ) -> "dc_td.AcknowledgeJobOutput":
        return dc_td.AcknowledgeJobOutput.make_one(res)

    def acknowledge_third_party_job(
        self,
        res: "bs_td.AcknowledgeThirdPartyJobOutputTypeDef",
    ) -> "dc_td.AcknowledgeThirdPartyJobOutput":
        return dc_td.AcknowledgeThirdPartyJobOutput.make_one(res)

    def create_custom_action_type(
        self,
        res: "bs_td.CreateCustomActionTypeOutputTypeDef",
    ) -> "dc_td.CreateCustomActionTypeOutput":
        return dc_td.CreateCustomActionTypeOutput.make_one(res)

    def create_pipeline(
        self,
        res: "bs_td.CreatePipelineOutputTypeDef",
    ) -> "dc_td.CreatePipelineOutput":
        return dc_td.CreatePipelineOutput.make_one(res)

    def delete_custom_action_type(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_pipeline(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def disable_stage_transition(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def enable_stage_transition(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def get_action_type(
        self,
        res: "bs_td.GetActionTypeOutputTypeDef",
    ) -> "dc_td.GetActionTypeOutput":
        return dc_td.GetActionTypeOutput.make_one(res)

    def get_job_details(
        self,
        res: "bs_td.GetJobDetailsOutputTypeDef",
    ) -> "dc_td.GetJobDetailsOutput":
        return dc_td.GetJobDetailsOutput.make_one(res)

    def get_pipeline(
        self,
        res: "bs_td.GetPipelineOutputTypeDef",
    ) -> "dc_td.GetPipelineOutput":
        return dc_td.GetPipelineOutput.make_one(res)

    def get_pipeline_execution(
        self,
        res: "bs_td.GetPipelineExecutionOutputTypeDef",
    ) -> "dc_td.GetPipelineExecutionOutput":
        return dc_td.GetPipelineExecutionOutput.make_one(res)

    def get_pipeline_state(
        self,
        res: "bs_td.GetPipelineStateOutputTypeDef",
    ) -> "dc_td.GetPipelineStateOutput":
        return dc_td.GetPipelineStateOutput.make_one(res)

    def get_third_party_job_details(
        self,
        res: "bs_td.GetThirdPartyJobDetailsOutputTypeDef",
    ) -> "dc_td.GetThirdPartyJobDetailsOutput":
        return dc_td.GetThirdPartyJobDetailsOutput.make_one(res)

    def list_action_executions(
        self,
        res: "bs_td.ListActionExecutionsOutputTypeDef",
    ) -> "dc_td.ListActionExecutionsOutput":
        return dc_td.ListActionExecutionsOutput.make_one(res)

    def list_action_types(
        self,
        res: "bs_td.ListActionTypesOutputTypeDef",
    ) -> "dc_td.ListActionTypesOutput":
        return dc_td.ListActionTypesOutput.make_one(res)

    def list_deploy_action_execution_targets(
        self,
        res: "bs_td.ListDeployActionExecutionTargetsOutputTypeDef",
    ) -> "dc_td.ListDeployActionExecutionTargetsOutput":
        return dc_td.ListDeployActionExecutionTargetsOutput.make_one(res)

    def list_pipeline_executions(
        self,
        res: "bs_td.ListPipelineExecutionsOutputTypeDef",
    ) -> "dc_td.ListPipelineExecutionsOutput":
        return dc_td.ListPipelineExecutionsOutput.make_one(res)

    def list_pipelines(
        self,
        res: "bs_td.ListPipelinesOutputTypeDef",
    ) -> "dc_td.ListPipelinesOutput":
        return dc_td.ListPipelinesOutput.make_one(res)

    def list_rule_executions(
        self,
        res: "bs_td.ListRuleExecutionsOutputTypeDef",
    ) -> "dc_td.ListRuleExecutionsOutput":
        return dc_td.ListRuleExecutionsOutput.make_one(res)

    def list_rule_types(
        self,
        res: "bs_td.ListRuleTypesOutputTypeDef",
    ) -> "dc_td.ListRuleTypesOutput":
        return dc_td.ListRuleTypesOutput.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceOutputTypeDef",
    ) -> "dc_td.ListTagsForResourceOutput":
        return dc_td.ListTagsForResourceOutput.make_one(res)

    def list_webhooks(
        self,
        res: "bs_td.ListWebhooksOutputTypeDef",
    ) -> "dc_td.ListWebhooksOutput":
        return dc_td.ListWebhooksOutput.make_one(res)

    def override_stage_condition(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def poll_for_jobs(
        self,
        res: "bs_td.PollForJobsOutputTypeDef",
    ) -> "dc_td.PollForJobsOutput":
        return dc_td.PollForJobsOutput.make_one(res)

    def poll_for_third_party_jobs(
        self,
        res: "bs_td.PollForThirdPartyJobsOutputTypeDef",
    ) -> "dc_td.PollForThirdPartyJobsOutput":
        return dc_td.PollForThirdPartyJobsOutput.make_one(res)

    def put_action_revision(
        self,
        res: "bs_td.PutActionRevisionOutputTypeDef",
    ) -> "dc_td.PutActionRevisionOutput":
        return dc_td.PutActionRevisionOutput.make_one(res)

    def put_approval_result(
        self,
        res: "bs_td.PutApprovalResultOutputTypeDef",
    ) -> "dc_td.PutApprovalResultOutput":
        return dc_td.PutApprovalResultOutput.make_one(res)

    def put_job_failure_result(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def put_job_success_result(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def put_third_party_job_failure_result(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def put_third_party_job_success_result(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def put_webhook(
        self,
        res: "bs_td.PutWebhookOutputTypeDef",
    ) -> "dc_td.PutWebhookOutput":
        return dc_td.PutWebhookOutput.make_one(res)

    def retry_stage_execution(
        self,
        res: "bs_td.RetryStageExecutionOutputTypeDef",
    ) -> "dc_td.RetryStageExecutionOutput":
        return dc_td.RetryStageExecutionOutput.make_one(res)

    def rollback_stage(
        self,
        res: "bs_td.RollbackStageOutputTypeDef",
    ) -> "dc_td.RollbackStageOutput":
        return dc_td.RollbackStageOutput.make_one(res)

    def start_pipeline_execution(
        self,
        res: "bs_td.StartPipelineExecutionOutputTypeDef",
    ) -> "dc_td.StartPipelineExecutionOutput":
        return dc_td.StartPipelineExecutionOutput.make_one(res)

    def stop_pipeline_execution(
        self,
        res: "bs_td.StopPipelineExecutionOutputTypeDef",
    ) -> "dc_td.StopPipelineExecutionOutput":
        return dc_td.StopPipelineExecutionOutput.make_one(res)

    def update_action_type(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_pipeline(
        self,
        res: "bs_td.UpdatePipelineOutputTypeDef",
    ) -> "dc_td.UpdatePipelineOutput":
        return dc_td.UpdatePipelineOutput.make_one(res)


codepipeline_caster = CODEPIPELINECaster()
