# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_bedrock import type_defs as bs_td


class BEDROCKCaster:

    def batch_delete_evaluation_job(
        self,
        res: "bs_td.BatchDeleteEvaluationJobResponseTypeDef",
    ) -> "dc_td.BatchDeleteEvaluationJobResponse":
        return dc_td.BatchDeleteEvaluationJobResponse.make_one(res)

    def create_automated_reasoning_policy(
        self,
        res: "bs_td.CreateAutomatedReasoningPolicyResponseTypeDef",
    ) -> "dc_td.CreateAutomatedReasoningPolicyResponse":
        return dc_td.CreateAutomatedReasoningPolicyResponse.make_one(res)

    def create_automated_reasoning_policy_test_case(
        self,
        res: "bs_td.CreateAutomatedReasoningPolicyTestCaseResponseTypeDef",
    ) -> "dc_td.CreateAutomatedReasoningPolicyTestCaseResponse":
        return dc_td.CreateAutomatedReasoningPolicyTestCaseResponse.make_one(res)

    def create_automated_reasoning_policy_version(
        self,
        res: "bs_td.CreateAutomatedReasoningPolicyVersionResponseTypeDef",
    ) -> "dc_td.CreateAutomatedReasoningPolicyVersionResponse":
        return dc_td.CreateAutomatedReasoningPolicyVersionResponse.make_one(res)

    def create_custom_model(
        self,
        res: "bs_td.CreateCustomModelResponseTypeDef",
    ) -> "dc_td.CreateCustomModelResponse":
        return dc_td.CreateCustomModelResponse.make_one(res)

    def create_custom_model_deployment(
        self,
        res: "bs_td.CreateCustomModelDeploymentResponseTypeDef",
    ) -> "dc_td.CreateCustomModelDeploymentResponse":
        return dc_td.CreateCustomModelDeploymentResponse.make_one(res)

    def create_evaluation_job(
        self,
        res: "bs_td.CreateEvaluationJobResponseTypeDef",
    ) -> "dc_td.CreateEvaluationJobResponse":
        return dc_td.CreateEvaluationJobResponse.make_one(res)

    def create_foundation_model_agreement(
        self,
        res: "bs_td.CreateFoundationModelAgreementResponseTypeDef",
    ) -> "dc_td.CreateFoundationModelAgreementResponse":
        return dc_td.CreateFoundationModelAgreementResponse.make_one(res)

    def create_guardrail(
        self,
        res: "bs_td.CreateGuardrailResponseTypeDef",
    ) -> "dc_td.CreateGuardrailResponse":
        return dc_td.CreateGuardrailResponse.make_one(res)

    def create_guardrail_version(
        self,
        res: "bs_td.CreateGuardrailVersionResponseTypeDef",
    ) -> "dc_td.CreateGuardrailVersionResponse":
        return dc_td.CreateGuardrailVersionResponse.make_one(res)

    def create_inference_profile(
        self,
        res: "bs_td.CreateInferenceProfileResponseTypeDef",
    ) -> "dc_td.CreateInferenceProfileResponse":
        return dc_td.CreateInferenceProfileResponse.make_one(res)

    def create_marketplace_model_endpoint(
        self,
        res: "bs_td.CreateMarketplaceModelEndpointResponseTypeDef",
    ) -> "dc_td.CreateMarketplaceModelEndpointResponse":
        return dc_td.CreateMarketplaceModelEndpointResponse.make_one(res)

    def create_model_copy_job(
        self,
        res: "bs_td.CreateModelCopyJobResponseTypeDef",
    ) -> "dc_td.CreateModelCopyJobResponse":
        return dc_td.CreateModelCopyJobResponse.make_one(res)

    def create_model_customization_job(
        self,
        res: "bs_td.CreateModelCustomizationJobResponseTypeDef",
    ) -> "dc_td.CreateModelCustomizationJobResponse":
        return dc_td.CreateModelCustomizationJobResponse.make_one(res)

    def create_model_import_job(
        self,
        res: "bs_td.CreateModelImportJobResponseTypeDef",
    ) -> "dc_td.CreateModelImportJobResponse":
        return dc_td.CreateModelImportJobResponse.make_one(res)

    def create_model_invocation_job(
        self,
        res: "bs_td.CreateModelInvocationJobResponseTypeDef",
    ) -> "dc_td.CreateModelInvocationJobResponse":
        return dc_td.CreateModelInvocationJobResponse.make_one(res)

    def create_prompt_router(
        self,
        res: "bs_td.CreatePromptRouterResponseTypeDef",
    ) -> "dc_td.CreatePromptRouterResponse":
        return dc_td.CreatePromptRouterResponse.make_one(res)

    def create_provisioned_model_throughput(
        self,
        res: "bs_td.CreateProvisionedModelThroughputResponseTypeDef",
    ) -> "dc_td.CreateProvisionedModelThroughputResponse":
        return dc_td.CreateProvisionedModelThroughputResponse.make_one(res)

    def export_automated_reasoning_policy_version(
        self,
        res: "bs_td.ExportAutomatedReasoningPolicyVersionResponseTypeDef",
    ) -> "dc_td.ExportAutomatedReasoningPolicyVersionResponse":
        return dc_td.ExportAutomatedReasoningPolicyVersionResponse.make_one(res)

    def get_automated_reasoning_policy(
        self,
        res: "bs_td.GetAutomatedReasoningPolicyResponseTypeDef",
    ) -> "dc_td.GetAutomatedReasoningPolicyResponse":
        return dc_td.GetAutomatedReasoningPolicyResponse.make_one(res)

    def get_automated_reasoning_policy_annotations(
        self,
        res: "bs_td.GetAutomatedReasoningPolicyAnnotationsResponseTypeDef",
    ) -> "dc_td.GetAutomatedReasoningPolicyAnnotationsResponse":
        return dc_td.GetAutomatedReasoningPolicyAnnotationsResponse.make_one(res)

    def get_automated_reasoning_policy_build_workflow(
        self,
        res: "bs_td.GetAutomatedReasoningPolicyBuildWorkflowResponseTypeDef",
    ) -> "dc_td.GetAutomatedReasoningPolicyBuildWorkflowResponse":
        return dc_td.GetAutomatedReasoningPolicyBuildWorkflowResponse.make_one(res)

    def get_automated_reasoning_policy_build_workflow_result_assets(
        self,
        res: "bs_td.GetAutomatedReasoningPolicyBuildWorkflowResultAssetsResponseTypeDef",
    ) -> "dc_td.GetAutomatedReasoningPolicyBuildWorkflowResultAssetsResponse":
        return (
            dc_td.GetAutomatedReasoningPolicyBuildWorkflowResultAssetsResponse.make_one(
                res
            )
        )

    def get_automated_reasoning_policy_next_scenario(
        self,
        res: "bs_td.GetAutomatedReasoningPolicyNextScenarioResponseTypeDef",
    ) -> "dc_td.GetAutomatedReasoningPolicyNextScenarioResponse":
        return dc_td.GetAutomatedReasoningPolicyNextScenarioResponse.make_one(res)

    def get_automated_reasoning_policy_test_case(
        self,
        res: "bs_td.GetAutomatedReasoningPolicyTestCaseResponseTypeDef",
    ) -> "dc_td.GetAutomatedReasoningPolicyTestCaseResponse":
        return dc_td.GetAutomatedReasoningPolicyTestCaseResponse.make_one(res)

    def get_automated_reasoning_policy_test_result(
        self,
        res: "bs_td.GetAutomatedReasoningPolicyTestResultResponseTypeDef",
    ) -> "dc_td.GetAutomatedReasoningPolicyTestResultResponse":
        return dc_td.GetAutomatedReasoningPolicyTestResultResponse.make_one(res)

    def get_custom_model(
        self,
        res: "bs_td.GetCustomModelResponseTypeDef",
    ) -> "dc_td.GetCustomModelResponse":
        return dc_td.GetCustomModelResponse.make_one(res)

    def get_custom_model_deployment(
        self,
        res: "bs_td.GetCustomModelDeploymentResponseTypeDef",
    ) -> "dc_td.GetCustomModelDeploymentResponse":
        return dc_td.GetCustomModelDeploymentResponse.make_one(res)

    def get_evaluation_job(
        self,
        res: "bs_td.GetEvaluationJobResponseTypeDef",
    ) -> "dc_td.GetEvaluationJobResponse":
        return dc_td.GetEvaluationJobResponse.make_one(res)

    def get_foundation_model(
        self,
        res: "bs_td.GetFoundationModelResponseTypeDef",
    ) -> "dc_td.GetFoundationModelResponse":
        return dc_td.GetFoundationModelResponse.make_one(res)

    def get_foundation_model_availability(
        self,
        res: "bs_td.GetFoundationModelAvailabilityResponseTypeDef",
    ) -> "dc_td.GetFoundationModelAvailabilityResponse":
        return dc_td.GetFoundationModelAvailabilityResponse.make_one(res)

    def get_guardrail(
        self,
        res: "bs_td.GetGuardrailResponseTypeDef",
    ) -> "dc_td.GetGuardrailResponse":
        return dc_td.GetGuardrailResponse.make_one(res)

    def get_imported_model(
        self,
        res: "bs_td.GetImportedModelResponseTypeDef",
    ) -> "dc_td.GetImportedModelResponse":
        return dc_td.GetImportedModelResponse.make_one(res)

    def get_inference_profile(
        self,
        res: "bs_td.GetInferenceProfileResponseTypeDef",
    ) -> "dc_td.GetInferenceProfileResponse":
        return dc_td.GetInferenceProfileResponse.make_one(res)

    def get_marketplace_model_endpoint(
        self,
        res: "bs_td.GetMarketplaceModelEndpointResponseTypeDef",
    ) -> "dc_td.GetMarketplaceModelEndpointResponse":
        return dc_td.GetMarketplaceModelEndpointResponse.make_one(res)

    def get_model_copy_job(
        self,
        res: "bs_td.GetModelCopyJobResponseTypeDef",
    ) -> "dc_td.GetModelCopyJobResponse":
        return dc_td.GetModelCopyJobResponse.make_one(res)

    def get_model_customization_job(
        self,
        res: "bs_td.GetModelCustomizationJobResponseTypeDef",
    ) -> "dc_td.GetModelCustomizationJobResponse":
        return dc_td.GetModelCustomizationJobResponse.make_one(res)

    def get_model_import_job(
        self,
        res: "bs_td.GetModelImportJobResponseTypeDef",
    ) -> "dc_td.GetModelImportJobResponse":
        return dc_td.GetModelImportJobResponse.make_one(res)

    def get_model_invocation_job(
        self,
        res: "bs_td.GetModelInvocationJobResponseTypeDef",
    ) -> "dc_td.GetModelInvocationJobResponse":
        return dc_td.GetModelInvocationJobResponse.make_one(res)

    def get_model_invocation_logging_configuration(
        self,
        res: "bs_td.GetModelInvocationLoggingConfigurationResponseTypeDef",
    ) -> "dc_td.GetModelInvocationLoggingConfigurationResponse":
        return dc_td.GetModelInvocationLoggingConfigurationResponse.make_one(res)

    def get_prompt_router(
        self,
        res: "bs_td.GetPromptRouterResponseTypeDef",
    ) -> "dc_td.GetPromptRouterResponse":
        return dc_td.GetPromptRouterResponse.make_one(res)

    def get_provisioned_model_throughput(
        self,
        res: "bs_td.GetProvisionedModelThroughputResponseTypeDef",
    ) -> "dc_td.GetProvisionedModelThroughputResponse":
        return dc_td.GetProvisionedModelThroughputResponse.make_one(res)

    def get_use_case_for_model_access(
        self,
        res: "bs_td.GetUseCaseForModelAccessResponseTypeDef",
    ) -> "dc_td.GetUseCaseForModelAccessResponse":
        return dc_td.GetUseCaseForModelAccessResponse.make_one(res)

    def list_automated_reasoning_policies(
        self,
        res: "bs_td.ListAutomatedReasoningPoliciesResponseTypeDef",
    ) -> "dc_td.ListAutomatedReasoningPoliciesResponse":
        return dc_td.ListAutomatedReasoningPoliciesResponse.make_one(res)

    def list_automated_reasoning_policy_build_workflows(
        self,
        res: "bs_td.ListAutomatedReasoningPolicyBuildWorkflowsResponseTypeDef",
    ) -> "dc_td.ListAutomatedReasoningPolicyBuildWorkflowsResponse":
        return dc_td.ListAutomatedReasoningPolicyBuildWorkflowsResponse.make_one(res)

    def list_automated_reasoning_policy_test_cases(
        self,
        res: "bs_td.ListAutomatedReasoningPolicyTestCasesResponseTypeDef",
    ) -> "dc_td.ListAutomatedReasoningPolicyTestCasesResponse":
        return dc_td.ListAutomatedReasoningPolicyTestCasesResponse.make_one(res)

    def list_automated_reasoning_policy_test_results(
        self,
        res: "bs_td.ListAutomatedReasoningPolicyTestResultsResponseTypeDef",
    ) -> "dc_td.ListAutomatedReasoningPolicyTestResultsResponse":
        return dc_td.ListAutomatedReasoningPolicyTestResultsResponse.make_one(res)

    def list_custom_model_deployments(
        self,
        res: "bs_td.ListCustomModelDeploymentsResponseTypeDef",
    ) -> "dc_td.ListCustomModelDeploymentsResponse":
        return dc_td.ListCustomModelDeploymentsResponse.make_one(res)

    def list_custom_models(
        self,
        res: "bs_td.ListCustomModelsResponseTypeDef",
    ) -> "dc_td.ListCustomModelsResponse":
        return dc_td.ListCustomModelsResponse.make_one(res)

    def list_evaluation_jobs(
        self,
        res: "bs_td.ListEvaluationJobsResponseTypeDef",
    ) -> "dc_td.ListEvaluationJobsResponse":
        return dc_td.ListEvaluationJobsResponse.make_one(res)

    def list_foundation_model_agreement_offers(
        self,
        res: "bs_td.ListFoundationModelAgreementOffersResponseTypeDef",
    ) -> "dc_td.ListFoundationModelAgreementOffersResponse":
        return dc_td.ListFoundationModelAgreementOffersResponse.make_one(res)

    def list_foundation_models(
        self,
        res: "bs_td.ListFoundationModelsResponseTypeDef",
    ) -> "dc_td.ListFoundationModelsResponse":
        return dc_td.ListFoundationModelsResponse.make_one(res)

    def list_guardrails(
        self,
        res: "bs_td.ListGuardrailsResponseTypeDef",
    ) -> "dc_td.ListGuardrailsResponse":
        return dc_td.ListGuardrailsResponse.make_one(res)

    def list_imported_models(
        self,
        res: "bs_td.ListImportedModelsResponseTypeDef",
    ) -> "dc_td.ListImportedModelsResponse":
        return dc_td.ListImportedModelsResponse.make_one(res)

    def list_inference_profiles(
        self,
        res: "bs_td.ListInferenceProfilesResponseTypeDef",
    ) -> "dc_td.ListInferenceProfilesResponse":
        return dc_td.ListInferenceProfilesResponse.make_one(res)

    def list_marketplace_model_endpoints(
        self,
        res: "bs_td.ListMarketplaceModelEndpointsResponseTypeDef",
    ) -> "dc_td.ListMarketplaceModelEndpointsResponse":
        return dc_td.ListMarketplaceModelEndpointsResponse.make_one(res)

    def list_model_copy_jobs(
        self,
        res: "bs_td.ListModelCopyJobsResponseTypeDef",
    ) -> "dc_td.ListModelCopyJobsResponse":
        return dc_td.ListModelCopyJobsResponse.make_one(res)

    def list_model_customization_jobs(
        self,
        res: "bs_td.ListModelCustomizationJobsResponseTypeDef",
    ) -> "dc_td.ListModelCustomizationJobsResponse":
        return dc_td.ListModelCustomizationJobsResponse.make_one(res)

    def list_model_import_jobs(
        self,
        res: "bs_td.ListModelImportJobsResponseTypeDef",
    ) -> "dc_td.ListModelImportJobsResponse":
        return dc_td.ListModelImportJobsResponse.make_one(res)

    def list_model_invocation_jobs(
        self,
        res: "bs_td.ListModelInvocationJobsResponseTypeDef",
    ) -> "dc_td.ListModelInvocationJobsResponse":
        return dc_td.ListModelInvocationJobsResponse.make_one(res)

    def list_prompt_routers(
        self,
        res: "bs_td.ListPromptRoutersResponseTypeDef",
    ) -> "dc_td.ListPromptRoutersResponse":
        return dc_td.ListPromptRoutersResponse.make_one(res)

    def list_provisioned_model_throughputs(
        self,
        res: "bs_td.ListProvisionedModelThroughputsResponseTypeDef",
    ) -> "dc_td.ListProvisionedModelThroughputsResponse":
        return dc_td.ListProvisionedModelThroughputsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def register_marketplace_model_endpoint(
        self,
        res: "bs_td.RegisterMarketplaceModelEndpointResponseTypeDef",
    ) -> "dc_td.RegisterMarketplaceModelEndpointResponse":
        return dc_td.RegisterMarketplaceModelEndpointResponse.make_one(res)

    def start_automated_reasoning_policy_build_workflow(
        self,
        res: "bs_td.StartAutomatedReasoningPolicyBuildWorkflowResponseTypeDef",
    ) -> "dc_td.StartAutomatedReasoningPolicyBuildWorkflowResponse":
        return dc_td.StartAutomatedReasoningPolicyBuildWorkflowResponse.make_one(res)

    def start_automated_reasoning_policy_test_workflow(
        self,
        res: "bs_td.StartAutomatedReasoningPolicyTestWorkflowResponseTypeDef",
    ) -> "dc_td.StartAutomatedReasoningPolicyTestWorkflowResponse":
        return dc_td.StartAutomatedReasoningPolicyTestWorkflowResponse.make_one(res)

    def update_automated_reasoning_policy(
        self,
        res: "bs_td.UpdateAutomatedReasoningPolicyResponseTypeDef",
    ) -> "dc_td.UpdateAutomatedReasoningPolicyResponse":
        return dc_td.UpdateAutomatedReasoningPolicyResponse.make_one(res)

    def update_automated_reasoning_policy_annotations(
        self,
        res: "bs_td.UpdateAutomatedReasoningPolicyAnnotationsResponseTypeDef",
    ) -> "dc_td.UpdateAutomatedReasoningPolicyAnnotationsResponse":
        return dc_td.UpdateAutomatedReasoningPolicyAnnotationsResponse.make_one(res)

    def update_automated_reasoning_policy_test_case(
        self,
        res: "bs_td.UpdateAutomatedReasoningPolicyTestCaseResponseTypeDef",
    ) -> "dc_td.UpdateAutomatedReasoningPolicyTestCaseResponse":
        return dc_td.UpdateAutomatedReasoningPolicyTestCaseResponse.make_one(res)

    def update_guardrail(
        self,
        res: "bs_td.UpdateGuardrailResponseTypeDef",
    ) -> "dc_td.UpdateGuardrailResponse":
        return dc_td.UpdateGuardrailResponse.make_one(res)

    def update_marketplace_model_endpoint(
        self,
        res: "bs_td.UpdateMarketplaceModelEndpointResponseTypeDef",
    ) -> "dc_td.UpdateMarketplaceModelEndpointResponse":
        return dc_td.UpdateMarketplaceModelEndpointResponse.make_one(res)


bedrock_caster = BEDROCKCaster()
