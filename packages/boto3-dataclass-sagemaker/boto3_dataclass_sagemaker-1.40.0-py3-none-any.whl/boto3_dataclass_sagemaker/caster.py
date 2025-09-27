# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_sagemaker import type_defs as bs_td


class SAGEMAKERCaster:

    def add_association(
        self,
        res: "bs_td.AddAssociationResponseTypeDef",
    ) -> "dc_td.AddAssociationResponse":
        return dc_td.AddAssociationResponse.make_one(res)

    def add_tags(
        self,
        res: "bs_td.AddTagsOutputTypeDef",
    ) -> "dc_td.AddTagsOutput":
        return dc_td.AddTagsOutput.make_one(res)

    def associate_trial_component(
        self,
        res: "bs_td.AssociateTrialComponentResponseTypeDef",
    ) -> "dc_td.AssociateTrialComponentResponse":
        return dc_td.AssociateTrialComponentResponse.make_one(res)

    def attach_cluster_node_volume(
        self,
        res: "bs_td.AttachClusterNodeVolumeResponseTypeDef",
    ) -> "dc_td.AttachClusterNodeVolumeResponse":
        return dc_td.AttachClusterNodeVolumeResponse.make_one(res)

    def batch_add_cluster_nodes(
        self,
        res: "bs_td.BatchAddClusterNodesResponseTypeDef",
    ) -> "dc_td.BatchAddClusterNodesResponse":
        return dc_td.BatchAddClusterNodesResponse.make_one(res)

    def batch_delete_cluster_nodes(
        self,
        res: "bs_td.BatchDeleteClusterNodesResponseTypeDef",
    ) -> "dc_td.BatchDeleteClusterNodesResponse":
        return dc_td.BatchDeleteClusterNodesResponse.make_one(res)

    def batch_describe_model_package(
        self,
        res: "bs_td.BatchDescribeModelPackageOutputTypeDef",
    ) -> "dc_td.BatchDescribeModelPackageOutput":
        return dc_td.BatchDescribeModelPackageOutput.make_one(res)

    def create_action(
        self,
        res: "bs_td.CreateActionResponseTypeDef",
    ) -> "dc_td.CreateActionResponse":
        return dc_td.CreateActionResponse.make_one(res)

    def create_algorithm(
        self,
        res: "bs_td.CreateAlgorithmOutputTypeDef",
    ) -> "dc_td.CreateAlgorithmOutput":
        return dc_td.CreateAlgorithmOutput.make_one(res)

    def create_app(
        self,
        res: "bs_td.CreateAppResponseTypeDef",
    ) -> "dc_td.CreateAppResponse":
        return dc_td.CreateAppResponse.make_one(res)

    def create_app_image_config(
        self,
        res: "bs_td.CreateAppImageConfigResponseTypeDef",
    ) -> "dc_td.CreateAppImageConfigResponse":
        return dc_td.CreateAppImageConfigResponse.make_one(res)

    def create_artifact(
        self,
        res: "bs_td.CreateArtifactResponseTypeDef",
    ) -> "dc_td.CreateArtifactResponse":
        return dc_td.CreateArtifactResponse.make_one(res)

    def create_auto_ml_job(
        self,
        res: "bs_td.CreateAutoMLJobResponseTypeDef",
    ) -> "dc_td.CreateAutoMLJobResponse":
        return dc_td.CreateAutoMLJobResponse.make_one(res)

    def create_auto_ml_job_v2(
        self,
        res: "bs_td.CreateAutoMLJobV2ResponseTypeDef",
    ) -> "dc_td.CreateAutoMLJobV2Response":
        return dc_td.CreateAutoMLJobV2Response.make_one(res)

    def create_cluster(
        self,
        res: "bs_td.CreateClusterResponseTypeDef",
    ) -> "dc_td.CreateClusterResponse":
        return dc_td.CreateClusterResponse.make_one(res)

    def create_cluster_scheduler_config(
        self,
        res: "bs_td.CreateClusterSchedulerConfigResponseTypeDef",
    ) -> "dc_td.CreateClusterSchedulerConfigResponse":
        return dc_td.CreateClusterSchedulerConfigResponse.make_one(res)

    def create_code_repository(
        self,
        res: "bs_td.CreateCodeRepositoryOutputTypeDef",
    ) -> "dc_td.CreateCodeRepositoryOutput":
        return dc_td.CreateCodeRepositoryOutput.make_one(res)

    def create_compilation_job(
        self,
        res: "bs_td.CreateCompilationJobResponseTypeDef",
    ) -> "dc_td.CreateCompilationJobResponse":
        return dc_td.CreateCompilationJobResponse.make_one(res)

    def create_compute_quota(
        self,
        res: "bs_td.CreateComputeQuotaResponseTypeDef",
    ) -> "dc_td.CreateComputeQuotaResponse":
        return dc_td.CreateComputeQuotaResponse.make_one(res)

    def create_context(
        self,
        res: "bs_td.CreateContextResponseTypeDef",
    ) -> "dc_td.CreateContextResponse":
        return dc_td.CreateContextResponse.make_one(res)

    def create_data_quality_job_definition(
        self,
        res: "bs_td.CreateDataQualityJobDefinitionResponseTypeDef",
    ) -> "dc_td.CreateDataQualityJobDefinitionResponse":
        return dc_td.CreateDataQualityJobDefinitionResponse.make_one(res)

    def create_device_fleet(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def create_domain(
        self,
        res: "bs_td.CreateDomainResponseTypeDef",
    ) -> "dc_td.CreateDomainResponse":
        return dc_td.CreateDomainResponse.make_one(res)

    def create_edge_deployment_plan(
        self,
        res: "bs_td.CreateEdgeDeploymentPlanResponseTypeDef",
    ) -> "dc_td.CreateEdgeDeploymentPlanResponse":
        return dc_td.CreateEdgeDeploymentPlanResponse.make_one(res)

    def create_edge_deployment_stage(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def create_edge_packaging_job(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def create_endpoint(
        self,
        res: "bs_td.CreateEndpointOutputTypeDef",
    ) -> "dc_td.CreateEndpointOutput":
        return dc_td.CreateEndpointOutput.make_one(res)

    def create_endpoint_config(
        self,
        res: "bs_td.CreateEndpointConfigOutputTypeDef",
    ) -> "dc_td.CreateEndpointConfigOutput":
        return dc_td.CreateEndpointConfigOutput.make_one(res)

    def create_experiment(
        self,
        res: "bs_td.CreateExperimentResponseTypeDef",
    ) -> "dc_td.CreateExperimentResponse":
        return dc_td.CreateExperimentResponse.make_one(res)

    def create_feature_group(
        self,
        res: "bs_td.CreateFeatureGroupResponseTypeDef",
    ) -> "dc_td.CreateFeatureGroupResponse":
        return dc_td.CreateFeatureGroupResponse.make_one(res)

    def create_flow_definition(
        self,
        res: "bs_td.CreateFlowDefinitionResponseTypeDef",
    ) -> "dc_td.CreateFlowDefinitionResponse":
        return dc_td.CreateFlowDefinitionResponse.make_one(res)

    def create_hub(
        self,
        res: "bs_td.CreateHubResponseTypeDef",
    ) -> "dc_td.CreateHubResponse":
        return dc_td.CreateHubResponse.make_one(res)

    def create_hub_content_presigned_urls(
        self,
        res: "bs_td.CreateHubContentPresignedUrlsResponseTypeDef",
    ) -> "dc_td.CreateHubContentPresignedUrlsResponse":
        return dc_td.CreateHubContentPresignedUrlsResponse.make_one(res)

    def create_hub_content_reference(
        self,
        res: "bs_td.CreateHubContentReferenceResponseTypeDef",
    ) -> "dc_td.CreateHubContentReferenceResponse":
        return dc_td.CreateHubContentReferenceResponse.make_one(res)

    def create_human_task_ui(
        self,
        res: "bs_td.CreateHumanTaskUiResponseTypeDef",
    ) -> "dc_td.CreateHumanTaskUiResponse":
        return dc_td.CreateHumanTaskUiResponse.make_one(res)

    def create_hyper_parameter_tuning_job(
        self,
        res: "bs_td.CreateHyperParameterTuningJobResponseTypeDef",
    ) -> "dc_td.CreateHyperParameterTuningJobResponse":
        return dc_td.CreateHyperParameterTuningJobResponse.make_one(res)

    def create_image(
        self,
        res: "bs_td.CreateImageResponseTypeDef",
    ) -> "dc_td.CreateImageResponse":
        return dc_td.CreateImageResponse.make_one(res)

    def create_image_version(
        self,
        res: "bs_td.CreateImageVersionResponseTypeDef",
    ) -> "dc_td.CreateImageVersionResponse":
        return dc_td.CreateImageVersionResponse.make_one(res)

    def create_inference_component(
        self,
        res: "bs_td.CreateInferenceComponentOutputTypeDef",
    ) -> "dc_td.CreateInferenceComponentOutput":
        return dc_td.CreateInferenceComponentOutput.make_one(res)

    def create_inference_experiment(
        self,
        res: "bs_td.CreateInferenceExperimentResponseTypeDef",
    ) -> "dc_td.CreateInferenceExperimentResponse":
        return dc_td.CreateInferenceExperimentResponse.make_one(res)

    def create_inference_recommendations_job(
        self,
        res: "bs_td.CreateInferenceRecommendationsJobResponseTypeDef",
    ) -> "dc_td.CreateInferenceRecommendationsJobResponse":
        return dc_td.CreateInferenceRecommendationsJobResponse.make_one(res)

    def create_labeling_job(
        self,
        res: "bs_td.CreateLabelingJobResponseTypeDef",
    ) -> "dc_td.CreateLabelingJobResponse":
        return dc_td.CreateLabelingJobResponse.make_one(res)

    def create_mlflow_tracking_server(
        self,
        res: "bs_td.CreateMlflowTrackingServerResponseTypeDef",
    ) -> "dc_td.CreateMlflowTrackingServerResponse":
        return dc_td.CreateMlflowTrackingServerResponse.make_one(res)

    def create_model(
        self,
        res: "bs_td.CreateModelOutputTypeDef",
    ) -> "dc_td.CreateModelOutput":
        return dc_td.CreateModelOutput.make_one(res)

    def create_model_bias_job_definition(
        self,
        res: "bs_td.CreateModelBiasJobDefinitionResponseTypeDef",
    ) -> "dc_td.CreateModelBiasJobDefinitionResponse":
        return dc_td.CreateModelBiasJobDefinitionResponse.make_one(res)

    def create_model_card(
        self,
        res: "bs_td.CreateModelCardResponseTypeDef",
    ) -> "dc_td.CreateModelCardResponse":
        return dc_td.CreateModelCardResponse.make_one(res)

    def create_model_card_export_job(
        self,
        res: "bs_td.CreateModelCardExportJobResponseTypeDef",
    ) -> "dc_td.CreateModelCardExportJobResponse":
        return dc_td.CreateModelCardExportJobResponse.make_one(res)

    def create_model_explainability_job_definition(
        self,
        res: "bs_td.CreateModelExplainabilityJobDefinitionResponseTypeDef",
    ) -> "dc_td.CreateModelExplainabilityJobDefinitionResponse":
        return dc_td.CreateModelExplainabilityJobDefinitionResponse.make_one(res)

    def create_model_package(
        self,
        res: "bs_td.CreateModelPackageOutputTypeDef",
    ) -> "dc_td.CreateModelPackageOutput":
        return dc_td.CreateModelPackageOutput.make_one(res)

    def create_model_package_group(
        self,
        res: "bs_td.CreateModelPackageGroupOutputTypeDef",
    ) -> "dc_td.CreateModelPackageGroupOutput":
        return dc_td.CreateModelPackageGroupOutput.make_one(res)

    def create_model_quality_job_definition(
        self,
        res: "bs_td.CreateModelQualityJobDefinitionResponseTypeDef",
    ) -> "dc_td.CreateModelQualityJobDefinitionResponse":
        return dc_td.CreateModelQualityJobDefinitionResponse.make_one(res)

    def create_monitoring_schedule(
        self,
        res: "bs_td.CreateMonitoringScheduleResponseTypeDef",
    ) -> "dc_td.CreateMonitoringScheduleResponse":
        return dc_td.CreateMonitoringScheduleResponse.make_one(res)

    def create_notebook_instance(
        self,
        res: "bs_td.CreateNotebookInstanceOutputTypeDef",
    ) -> "dc_td.CreateNotebookInstanceOutput":
        return dc_td.CreateNotebookInstanceOutput.make_one(res)

    def create_notebook_instance_lifecycle_config(
        self,
        res: "bs_td.CreateNotebookInstanceLifecycleConfigOutputTypeDef",
    ) -> "dc_td.CreateNotebookInstanceLifecycleConfigOutput":
        return dc_td.CreateNotebookInstanceLifecycleConfigOutput.make_one(res)

    def create_optimization_job(
        self,
        res: "bs_td.CreateOptimizationJobResponseTypeDef",
    ) -> "dc_td.CreateOptimizationJobResponse":
        return dc_td.CreateOptimizationJobResponse.make_one(res)

    def create_partner_app(
        self,
        res: "bs_td.CreatePartnerAppResponseTypeDef",
    ) -> "dc_td.CreatePartnerAppResponse":
        return dc_td.CreatePartnerAppResponse.make_one(res)

    def create_partner_app_presigned_url(
        self,
        res: "bs_td.CreatePartnerAppPresignedUrlResponseTypeDef",
    ) -> "dc_td.CreatePartnerAppPresignedUrlResponse":
        return dc_td.CreatePartnerAppPresignedUrlResponse.make_one(res)

    def create_pipeline(
        self,
        res: "bs_td.CreatePipelineResponseTypeDef",
    ) -> "dc_td.CreatePipelineResponse":
        return dc_td.CreatePipelineResponse.make_one(res)

    def create_presigned_domain_url(
        self,
        res: "bs_td.CreatePresignedDomainUrlResponseTypeDef",
    ) -> "dc_td.CreatePresignedDomainUrlResponse":
        return dc_td.CreatePresignedDomainUrlResponse.make_one(res)

    def create_presigned_mlflow_tracking_server_url(
        self,
        res: "bs_td.CreatePresignedMlflowTrackingServerUrlResponseTypeDef",
    ) -> "dc_td.CreatePresignedMlflowTrackingServerUrlResponse":
        return dc_td.CreatePresignedMlflowTrackingServerUrlResponse.make_one(res)

    def create_presigned_notebook_instance_url(
        self,
        res: "bs_td.CreatePresignedNotebookInstanceUrlOutputTypeDef",
    ) -> "dc_td.CreatePresignedNotebookInstanceUrlOutput":
        return dc_td.CreatePresignedNotebookInstanceUrlOutput.make_one(res)

    def create_processing_job(
        self,
        res: "bs_td.CreateProcessingJobResponseTypeDef",
    ) -> "dc_td.CreateProcessingJobResponse":
        return dc_td.CreateProcessingJobResponse.make_one(res)

    def create_project(
        self,
        res: "bs_td.CreateProjectOutputTypeDef",
    ) -> "dc_td.CreateProjectOutput":
        return dc_td.CreateProjectOutput.make_one(res)

    def create_space(
        self,
        res: "bs_td.CreateSpaceResponseTypeDef",
    ) -> "dc_td.CreateSpaceResponse":
        return dc_td.CreateSpaceResponse.make_one(res)

    def create_studio_lifecycle_config(
        self,
        res: "bs_td.CreateStudioLifecycleConfigResponseTypeDef",
    ) -> "dc_td.CreateStudioLifecycleConfigResponse":
        return dc_td.CreateStudioLifecycleConfigResponse.make_one(res)

    def create_training_job(
        self,
        res: "bs_td.CreateTrainingJobResponseTypeDef",
    ) -> "dc_td.CreateTrainingJobResponse":
        return dc_td.CreateTrainingJobResponse.make_one(res)

    def create_training_plan(
        self,
        res: "bs_td.CreateTrainingPlanResponseTypeDef",
    ) -> "dc_td.CreateTrainingPlanResponse":
        return dc_td.CreateTrainingPlanResponse.make_one(res)

    def create_transform_job(
        self,
        res: "bs_td.CreateTransformJobResponseTypeDef",
    ) -> "dc_td.CreateTransformJobResponse":
        return dc_td.CreateTransformJobResponse.make_one(res)

    def create_trial(
        self,
        res: "bs_td.CreateTrialResponseTypeDef",
    ) -> "dc_td.CreateTrialResponse":
        return dc_td.CreateTrialResponse.make_one(res)

    def create_trial_component(
        self,
        res: "bs_td.CreateTrialComponentResponseTypeDef",
    ) -> "dc_td.CreateTrialComponentResponse":
        return dc_td.CreateTrialComponentResponse.make_one(res)

    def create_user_profile(
        self,
        res: "bs_td.CreateUserProfileResponseTypeDef",
    ) -> "dc_td.CreateUserProfileResponse":
        return dc_td.CreateUserProfileResponse.make_one(res)

    def create_workforce(
        self,
        res: "bs_td.CreateWorkforceResponseTypeDef",
    ) -> "dc_td.CreateWorkforceResponse":
        return dc_td.CreateWorkforceResponse.make_one(res)

    def create_workteam(
        self,
        res: "bs_td.CreateWorkteamResponseTypeDef",
    ) -> "dc_td.CreateWorkteamResponse":
        return dc_td.CreateWorkteamResponse.make_one(res)

    def delete_action(
        self,
        res: "bs_td.DeleteActionResponseTypeDef",
    ) -> "dc_td.DeleteActionResponse":
        return dc_td.DeleteActionResponse.make_one(res)

    def delete_algorithm(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_app(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_app_image_config(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_artifact(
        self,
        res: "bs_td.DeleteArtifactResponseTypeDef",
    ) -> "dc_td.DeleteArtifactResponse":
        return dc_td.DeleteArtifactResponse.make_one(res)

    def delete_association(
        self,
        res: "bs_td.DeleteAssociationResponseTypeDef",
    ) -> "dc_td.DeleteAssociationResponse":
        return dc_td.DeleteAssociationResponse.make_one(res)

    def delete_cluster(
        self,
        res: "bs_td.DeleteClusterResponseTypeDef",
    ) -> "dc_td.DeleteClusterResponse":
        return dc_td.DeleteClusterResponse.make_one(res)

    def delete_cluster_scheduler_config(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_code_repository(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_compilation_job(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_compute_quota(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_context(
        self,
        res: "bs_td.DeleteContextResponseTypeDef",
    ) -> "dc_td.DeleteContextResponse":
        return dc_td.DeleteContextResponse.make_one(res)

    def delete_data_quality_job_definition(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_device_fleet(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_domain(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_edge_deployment_plan(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_edge_deployment_stage(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_endpoint(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_endpoint_config(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_experiment(
        self,
        res: "bs_td.DeleteExperimentResponseTypeDef",
    ) -> "dc_td.DeleteExperimentResponse":
        return dc_td.DeleteExperimentResponse.make_one(res)

    def delete_feature_group(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_hub(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_hub_content(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_hub_content_reference(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_hyper_parameter_tuning_job(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_inference_component(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_inference_experiment(
        self,
        res: "bs_td.DeleteInferenceExperimentResponseTypeDef",
    ) -> "dc_td.DeleteInferenceExperimentResponse":
        return dc_td.DeleteInferenceExperimentResponse.make_one(res)

    def delete_mlflow_tracking_server(
        self,
        res: "bs_td.DeleteMlflowTrackingServerResponseTypeDef",
    ) -> "dc_td.DeleteMlflowTrackingServerResponse":
        return dc_td.DeleteMlflowTrackingServerResponse.make_one(res)

    def delete_model(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_model_bias_job_definition(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_model_card(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_model_explainability_job_definition(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_model_package(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_model_package_group(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_model_package_group_policy(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_model_quality_job_definition(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_monitoring_schedule(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_notebook_instance(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_notebook_instance_lifecycle_config(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_optimization_job(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_partner_app(
        self,
        res: "bs_td.DeletePartnerAppResponseTypeDef",
    ) -> "dc_td.DeletePartnerAppResponse":
        return dc_td.DeletePartnerAppResponse.make_one(res)

    def delete_pipeline(
        self,
        res: "bs_td.DeletePipelineResponseTypeDef",
    ) -> "dc_td.DeletePipelineResponse":
        return dc_td.DeletePipelineResponse.make_one(res)

    def delete_project(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_space(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_studio_lifecycle_config(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_trial(
        self,
        res: "bs_td.DeleteTrialResponseTypeDef",
    ) -> "dc_td.DeleteTrialResponse":
        return dc_td.DeleteTrialResponse.make_one(res)

    def delete_trial_component(
        self,
        res: "bs_td.DeleteTrialComponentResponseTypeDef",
    ) -> "dc_td.DeleteTrialComponentResponse":
        return dc_td.DeleteTrialComponentResponse.make_one(res)

    def delete_user_profile(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_workteam(
        self,
        res: "bs_td.DeleteWorkteamResponseTypeDef",
    ) -> "dc_td.DeleteWorkteamResponse":
        return dc_td.DeleteWorkteamResponse.make_one(res)

    def deregister_devices(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def describe_action(
        self,
        res: "bs_td.DescribeActionResponseTypeDef",
    ) -> "dc_td.DescribeActionResponse":
        return dc_td.DescribeActionResponse.make_one(res)

    def describe_algorithm(
        self,
        res: "bs_td.DescribeAlgorithmOutputTypeDef",
    ) -> "dc_td.DescribeAlgorithmOutput":
        return dc_td.DescribeAlgorithmOutput.make_one(res)

    def describe_app(
        self,
        res: "bs_td.DescribeAppResponseTypeDef",
    ) -> "dc_td.DescribeAppResponse":
        return dc_td.DescribeAppResponse.make_one(res)

    def describe_app_image_config(
        self,
        res: "bs_td.DescribeAppImageConfigResponseTypeDef",
    ) -> "dc_td.DescribeAppImageConfigResponse":
        return dc_td.DescribeAppImageConfigResponse.make_one(res)

    def describe_artifact(
        self,
        res: "bs_td.DescribeArtifactResponseTypeDef",
    ) -> "dc_td.DescribeArtifactResponse":
        return dc_td.DescribeArtifactResponse.make_one(res)

    def describe_auto_ml_job(
        self,
        res: "bs_td.DescribeAutoMLJobResponseTypeDef",
    ) -> "dc_td.DescribeAutoMLJobResponse":
        return dc_td.DescribeAutoMLJobResponse.make_one(res)

    def describe_auto_ml_job_v2(
        self,
        res: "bs_td.DescribeAutoMLJobV2ResponseTypeDef",
    ) -> "dc_td.DescribeAutoMLJobV2Response":
        return dc_td.DescribeAutoMLJobV2Response.make_one(res)

    def describe_cluster(
        self,
        res: "bs_td.DescribeClusterResponseTypeDef",
    ) -> "dc_td.DescribeClusterResponse":
        return dc_td.DescribeClusterResponse.make_one(res)

    def describe_cluster_event(
        self,
        res: "bs_td.DescribeClusterEventResponseTypeDef",
    ) -> "dc_td.DescribeClusterEventResponse":
        return dc_td.DescribeClusterEventResponse.make_one(res)

    def describe_cluster_node(
        self,
        res: "bs_td.DescribeClusterNodeResponseTypeDef",
    ) -> "dc_td.DescribeClusterNodeResponse":
        return dc_td.DescribeClusterNodeResponse.make_one(res)

    def describe_cluster_scheduler_config(
        self,
        res: "bs_td.DescribeClusterSchedulerConfigResponseTypeDef",
    ) -> "dc_td.DescribeClusterSchedulerConfigResponse":
        return dc_td.DescribeClusterSchedulerConfigResponse.make_one(res)

    def describe_code_repository(
        self,
        res: "bs_td.DescribeCodeRepositoryOutputTypeDef",
    ) -> "dc_td.DescribeCodeRepositoryOutput":
        return dc_td.DescribeCodeRepositoryOutput.make_one(res)

    def describe_compilation_job(
        self,
        res: "bs_td.DescribeCompilationJobResponseTypeDef",
    ) -> "dc_td.DescribeCompilationJobResponse":
        return dc_td.DescribeCompilationJobResponse.make_one(res)

    def describe_compute_quota(
        self,
        res: "bs_td.DescribeComputeQuotaResponseTypeDef",
    ) -> "dc_td.DescribeComputeQuotaResponse":
        return dc_td.DescribeComputeQuotaResponse.make_one(res)

    def describe_context(
        self,
        res: "bs_td.DescribeContextResponseTypeDef",
    ) -> "dc_td.DescribeContextResponse":
        return dc_td.DescribeContextResponse.make_one(res)

    def describe_data_quality_job_definition(
        self,
        res: "bs_td.DescribeDataQualityJobDefinitionResponseTypeDef",
    ) -> "dc_td.DescribeDataQualityJobDefinitionResponse":
        return dc_td.DescribeDataQualityJobDefinitionResponse.make_one(res)

    def describe_device(
        self,
        res: "bs_td.DescribeDeviceResponseTypeDef",
    ) -> "dc_td.DescribeDeviceResponse":
        return dc_td.DescribeDeviceResponse.make_one(res)

    def describe_device_fleet(
        self,
        res: "bs_td.DescribeDeviceFleetResponseTypeDef",
    ) -> "dc_td.DescribeDeviceFleetResponse":
        return dc_td.DescribeDeviceFleetResponse.make_one(res)

    def describe_domain(
        self,
        res: "bs_td.DescribeDomainResponseTypeDef",
    ) -> "dc_td.DescribeDomainResponse":
        return dc_td.DescribeDomainResponse.make_one(res)

    def describe_edge_deployment_plan(
        self,
        res: "bs_td.DescribeEdgeDeploymentPlanResponseTypeDef",
    ) -> "dc_td.DescribeEdgeDeploymentPlanResponse":
        return dc_td.DescribeEdgeDeploymentPlanResponse.make_one(res)

    def describe_edge_packaging_job(
        self,
        res: "bs_td.DescribeEdgePackagingJobResponseTypeDef",
    ) -> "dc_td.DescribeEdgePackagingJobResponse":
        return dc_td.DescribeEdgePackagingJobResponse.make_one(res)

    def describe_endpoint(
        self,
        res: "bs_td.DescribeEndpointOutputTypeDef",
    ) -> "dc_td.DescribeEndpointOutput":
        return dc_td.DescribeEndpointOutput.make_one(res)

    def describe_endpoint_config(
        self,
        res: "bs_td.DescribeEndpointConfigOutputTypeDef",
    ) -> "dc_td.DescribeEndpointConfigOutput":
        return dc_td.DescribeEndpointConfigOutput.make_one(res)

    def describe_experiment(
        self,
        res: "bs_td.DescribeExperimentResponseTypeDef",
    ) -> "dc_td.DescribeExperimentResponse":
        return dc_td.DescribeExperimentResponse.make_one(res)

    def describe_feature_group(
        self,
        res: "bs_td.DescribeFeatureGroupResponseTypeDef",
    ) -> "dc_td.DescribeFeatureGroupResponse":
        return dc_td.DescribeFeatureGroupResponse.make_one(res)

    def describe_feature_metadata(
        self,
        res: "bs_td.DescribeFeatureMetadataResponseTypeDef",
    ) -> "dc_td.DescribeFeatureMetadataResponse":
        return dc_td.DescribeFeatureMetadataResponse.make_one(res)

    def describe_flow_definition(
        self,
        res: "bs_td.DescribeFlowDefinitionResponseTypeDef",
    ) -> "dc_td.DescribeFlowDefinitionResponse":
        return dc_td.DescribeFlowDefinitionResponse.make_one(res)

    def describe_hub(
        self,
        res: "bs_td.DescribeHubResponseTypeDef",
    ) -> "dc_td.DescribeHubResponse":
        return dc_td.DescribeHubResponse.make_one(res)

    def describe_hub_content(
        self,
        res: "bs_td.DescribeHubContentResponseTypeDef",
    ) -> "dc_td.DescribeHubContentResponse":
        return dc_td.DescribeHubContentResponse.make_one(res)

    def describe_human_task_ui(
        self,
        res: "bs_td.DescribeHumanTaskUiResponseTypeDef",
    ) -> "dc_td.DescribeHumanTaskUiResponse":
        return dc_td.DescribeHumanTaskUiResponse.make_one(res)

    def describe_hyper_parameter_tuning_job(
        self,
        res: "bs_td.DescribeHyperParameterTuningJobResponseTypeDef",
    ) -> "dc_td.DescribeHyperParameterTuningJobResponse":
        return dc_td.DescribeHyperParameterTuningJobResponse.make_one(res)

    def describe_image(
        self,
        res: "bs_td.DescribeImageResponseTypeDef",
    ) -> "dc_td.DescribeImageResponse":
        return dc_td.DescribeImageResponse.make_one(res)

    def describe_image_version(
        self,
        res: "bs_td.DescribeImageVersionResponseTypeDef",
    ) -> "dc_td.DescribeImageVersionResponse":
        return dc_td.DescribeImageVersionResponse.make_one(res)

    def describe_inference_component(
        self,
        res: "bs_td.DescribeInferenceComponentOutputTypeDef",
    ) -> "dc_td.DescribeInferenceComponentOutput":
        return dc_td.DescribeInferenceComponentOutput.make_one(res)

    def describe_inference_experiment(
        self,
        res: "bs_td.DescribeInferenceExperimentResponseTypeDef",
    ) -> "dc_td.DescribeInferenceExperimentResponse":
        return dc_td.DescribeInferenceExperimentResponse.make_one(res)

    def describe_inference_recommendations_job(
        self,
        res: "bs_td.DescribeInferenceRecommendationsJobResponseTypeDef",
    ) -> "dc_td.DescribeInferenceRecommendationsJobResponse":
        return dc_td.DescribeInferenceRecommendationsJobResponse.make_one(res)

    def describe_labeling_job(
        self,
        res: "bs_td.DescribeLabelingJobResponseTypeDef",
    ) -> "dc_td.DescribeLabelingJobResponse":
        return dc_td.DescribeLabelingJobResponse.make_one(res)

    def describe_lineage_group(
        self,
        res: "bs_td.DescribeLineageGroupResponseTypeDef",
    ) -> "dc_td.DescribeLineageGroupResponse":
        return dc_td.DescribeLineageGroupResponse.make_one(res)

    def describe_mlflow_tracking_server(
        self,
        res: "bs_td.DescribeMlflowTrackingServerResponseTypeDef",
    ) -> "dc_td.DescribeMlflowTrackingServerResponse":
        return dc_td.DescribeMlflowTrackingServerResponse.make_one(res)

    def describe_model(
        self,
        res: "bs_td.DescribeModelOutputTypeDef",
    ) -> "dc_td.DescribeModelOutput":
        return dc_td.DescribeModelOutput.make_one(res)

    def describe_model_bias_job_definition(
        self,
        res: "bs_td.DescribeModelBiasJobDefinitionResponseTypeDef",
    ) -> "dc_td.DescribeModelBiasJobDefinitionResponse":
        return dc_td.DescribeModelBiasJobDefinitionResponse.make_one(res)

    def describe_model_card(
        self,
        res: "bs_td.DescribeModelCardResponseTypeDef",
    ) -> "dc_td.DescribeModelCardResponse":
        return dc_td.DescribeModelCardResponse.make_one(res)

    def describe_model_card_export_job(
        self,
        res: "bs_td.DescribeModelCardExportJobResponseTypeDef",
    ) -> "dc_td.DescribeModelCardExportJobResponse":
        return dc_td.DescribeModelCardExportJobResponse.make_one(res)

    def describe_model_explainability_job_definition(
        self,
        res: "bs_td.DescribeModelExplainabilityJobDefinitionResponseTypeDef",
    ) -> "dc_td.DescribeModelExplainabilityJobDefinitionResponse":
        return dc_td.DescribeModelExplainabilityJobDefinitionResponse.make_one(res)

    def describe_model_package(
        self,
        res: "bs_td.DescribeModelPackageOutputTypeDef",
    ) -> "dc_td.DescribeModelPackageOutput":
        return dc_td.DescribeModelPackageOutput.make_one(res)

    def describe_model_package_group(
        self,
        res: "bs_td.DescribeModelPackageGroupOutputTypeDef",
    ) -> "dc_td.DescribeModelPackageGroupOutput":
        return dc_td.DescribeModelPackageGroupOutput.make_one(res)

    def describe_model_quality_job_definition(
        self,
        res: "bs_td.DescribeModelQualityJobDefinitionResponseTypeDef",
    ) -> "dc_td.DescribeModelQualityJobDefinitionResponse":
        return dc_td.DescribeModelQualityJobDefinitionResponse.make_one(res)

    def describe_monitoring_schedule(
        self,
        res: "bs_td.DescribeMonitoringScheduleResponseTypeDef",
    ) -> "dc_td.DescribeMonitoringScheduleResponse":
        return dc_td.DescribeMonitoringScheduleResponse.make_one(res)

    def describe_notebook_instance(
        self,
        res: "bs_td.DescribeNotebookInstanceOutputTypeDef",
    ) -> "dc_td.DescribeNotebookInstanceOutput":
        return dc_td.DescribeNotebookInstanceOutput.make_one(res)

    def describe_notebook_instance_lifecycle_config(
        self,
        res: "bs_td.DescribeNotebookInstanceLifecycleConfigOutputTypeDef",
    ) -> "dc_td.DescribeNotebookInstanceLifecycleConfigOutput":
        return dc_td.DescribeNotebookInstanceLifecycleConfigOutput.make_one(res)

    def describe_optimization_job(
        self,
        res: "bs_td.DescribeOptimizationJobResponseTypeDef",
    ) -> "dc_td.DescribeOptimizationJobResponse":
        return dc_td.DescribeOptimizationJobResponse.make_one(res)

    def describe_partner_app(
        self,
        res: "bs_td.DescribePartnerAppResponseTypeDef",
    ) -> "dc_td.DescribePartnerAppResponse":
        return dc_td.DescribePartnerAppResponse.make_one(res)

    def describe_pipeline(
        self,
        res: "bs_td.DescribePipelineResponseTypeDef",
    ) -> "dc_td.DescribePipelineResponse":
        return dc_td.DescribePipelineResponse.make_one(res)

    def describe_pipeline_definition_for_execution(
        self,
        res: "bs_td.DescribePipelineDefinitionForExecutionResponseTypeDef",
    ) -> "dc_td.DescribePipelineDefinitionForExecutionResponse":
        return dc_td.DescribePipelineDefinitionForExecutionResponse.make_one(res)

    def describe_pipeline_execution(
        self,
        res: "bs_td.DescribePipelineExecutionResponseTypeDef",
    ) -> "dc_td.DescribePipelineExecutionResponse":
        return dc_td.DescribePipelineExecutionResponse.make_one(res)

    def describe_processing_job(
        self,
        res: "bs_td.DescribeProcessingJobResponseTypeDef",
    ) -> "dc_td.DescribeProcessingJobResponse":
        return dc_td.DescribeProcessingJobResponse.make_one(res)

    def describe_project(
        self,
        res: "bs_td.DescribeProjectOutputTypeDef",
    ) -> "dc_td.DescribeProjectOutput":
        return dc_td.DescribeProjectOutput.make_one(res)

    def describe_reserved_capacity(
        self,
        res: "bs_td.DescribeReservedCapacityResponseTypeDef",
    ) -> "dc_td.DescribeReservedCapacityResponse":
        return dc_td.DescribeReservedCapacityResponse.make_one(res)

    def describe_space(
        self,
        res: "bs_td.DescribeSpaceResponseTypeDef",
    ) -> "dc_td.DescribeSpaceResponse":
        return dc_td.DescribeSpaceResponse.make_one(res)

    def describe_studio_lifecycle_config(
        self,
        res: "bs_td.DescribeStudioLifecycleConfigResponseTypeDef",
    ) -> "dc_td.DescribeStudioLifecycleConfigResponse":
        return dc_td.DescribeStudioLifecycleConfigResponse.make_one(res)

    def describe_subscribed_workteam(
        self,
        res: "bs_td.DescribeSubscribedWorkteamResponseTypeDef",
    ) -> "dc_td.DescribeSubscribedWorkteamResponse":
        return dc_td.DescribeSubscribedWorkteamResponse.make_one(res)

    def describe_training_job(
        self,
        res: "bs_td.DescribeTrainingJobResponseTypeDef",
    ) -> "dc_td.DescribeTrainingJobResponse":
        return dc_td.DescribeTrainingJobResponse.make_one(res)

    def describe_training_plan(
        self,
        res: "bs_td.DescribeTrainingPlanResponseTypeDef",
    ) -> "dc_td.DescribeTrainingPlanResponse":
        return dc_td.DescribeTrainingPlanResponse.make_one(res)

    def describe_transform_job(
        self,
        res: "bs_td.DescribeTransformJobResponseTypeDef",
    ) -> "dc_td.DescribeTransformJobResponse":
        return dc_td.DescribeTransformJobResponse.make_one(res)

    def describe_trial(
        self,
        res: "bs_td.DescribeTrialResponseTypeDef",
    ) -> "dc_td.DescribeTrialResponse":
        return dc_td.DescribeTrialResponse.make_one(res)

    def describe_trial_component(
        self,
        res: "bs_td.DescribeTrialComponentResponseTypeDef",
    ) -> "dc_td.DescribeTrialComponentResponse":
        return dc_td.DescribeTrialComponentResponse.make_one(res)

    def describe_user_profile(
        self,
        res: "bs_td.DescribeUserProfileResponseTypeDef",
    ) -> "dc_td.DescribeUserProfileResponse":
        return dc_td.DescribeUserProfileResponse.make_one(res)

    def describe_workforce(
        self,
        res: "bs_td.DescribeWorkforceResponseTypeDef",
    ) -> "dc_td.DescribeWorkforceResponse":
        return dc_td.DescribeWorkforceResponse.make_one(res)

    def describe_workteam(
        self,
        res: "bs_td.DescribeWorkteamResponseTypeDef",
    ) -> "dc_td.DescribeWorkteamResponse":
        return dc_td.DescribeWorkteamResponse.make_one(res)

    def detach_cluster_node_volume(
        self,
        res: "bs_td.DetachClusterNodeVolumeResponseTypeDef",
    ) -> "dc_td.DetachClusterNodeVolumeResponse":
        return dc_td.DetachClusterNodeVolumeResponse.make_one(res)

    def disassociate_trial_component(
        self,
        res: "bs_td.DisassociateTrialComponentResponseTypeDef",
    ) -> "dc_td.DisassociateTrialComponentResponse":
        return dc_td.DisassociateTrialComponentResponse.make_one(res)

    def get_device_fleet_report(
        self,
        res: "bs_td.GetDeviceFleetReportResponseTypeDef",
    ) -> "dc_td.GetDeviceFleetReportResponse":
        return dc_td.GetDeviceFleetReportResponse.make_one(res)

    def get_lineage_group_policy(
        self,
        res: "bs_td.GetLineageGroupPolicyResponseTypeDef",
    ) -> "dc_td.GetLineageGroupPolicyResponse":
        return dc_td.GetLineageGroupPolicyResponse.make_one(res)

    def get_model_package_group_policy(
        self,
        res: "bs_td.GetModelPackageGroupPolicyOutputTypeDef",
    ) -> "dc_td.GetModelPackageGroupPolicyOutput":
        return dc_td.GetModelPackageGroupPolicyOutput.make_one(res)

    def get_sagemaker_servicecatalog_portfolio_status(
        self,
        res: "bs_td.GetSagemakerServicecatalogPortfolioStatusOutputTypeDef",
    ) -> "dc_td.GetSagemakerServicecatalogPortfolioStatusOutput":
        return dc_td.GetSagemakerServicecatalogPortfolioStatusOutput.make_one(res)

    def get_scaling_configuration_recommendation(
        self,
        res: "bs_td.GetScalingConfigurationRecommendationResponseTypeDef",
    ) -> "dc_td.GetScalingConfigurationRecommendationResponse":
        return dc_td.GetScalingConfigurationRecommendationResponse.make_one(res)

    def get_search_suggestions(
        self,
        res: "bs_td.GetSearchSuggestionsResponseTypeDef",
    ) -> "dc_td.GetSearchSuggestionsResponse":
        return dc_td.GetSearchSuggestionsResponse.make_one(res)

    def import_hub_content(
        self,
        res: "bs_td.ImportHubContentResponseTypeDef",
    ) -> "dc_td.ImportHubContentResponse":
        return dc_td.ImportHubContentResponse.make_one(res)

    def list_actions(
        self,
        res: "bs_td.ListActionsResponseTypeDef",
    ) -> "dc_td.ListActionsResponse":
        return dc_td.ListActionsResponse.make_one(res)

    def list_algorithms(
        self,
        res: "bs_td.ListAlgorithmsOutputTypeDef",
    ) -> "dc_td.ListAlgorithmsOutput":
        return dc_td.ListAlgorithmsOutput.make_one(res)

    def list_aliases(
        self,
        res: "bs_td.ListAliasesResponseTypeDef",
    ) -> "dc_td.ListAliasesResponse":
        return dc_td.ListAliasesResponse.make_one(res)

    def list_app_image_configs(
        self,
        res: "bs_td.ListAppImageConfigsResponseTypeDef",
    ) -> "dc_td.ListAppImageConfigsResponse":
        return dc_td.ListAppImageConfigsResponse.make_one(res)

    def list_apps(
        self,
        res: "bs_td.ListAppsResponseTypeDef",
    ) -> "dc_td.ListAppsResponse":
        return dc_td.ListAppsResponse.make_one(res)

    def list_artifacts(
        self,
        res: "bs_td.ListArtifactsResponseTypeDef",
    ) -> "dc_td.ListArtifactsResponse":
        return dc_td.ListArtifactsResponse.make_one(res)

    def list_associations(
        self,
        res: "bs_td.ListAssociationsResponseTypeDef",
    ) -> "dc_td.ListAssociationsResponse":
        return dc_td.ListAssociationsResponse.make_one(res)

    def list_auto_ml_jobs(
        self,
        res: "bs_td.ListAutoMLJobsResponseTypeDef",
    ) -> "dc_td.ListAutoMLJobsResponse":
        return dc_td.ListAutoMLJobsResponse.make_one(res)

    def list_candidates_for_auto_ml_job(
        self,
        res: "bs_td.ListCandidatesForAutoMLJobResponseTypeDef",
    ) -> "dc_td.ListCandidatesForAutoMLJobResponse":
        return dc_td.ListCandidatesForAutoMLJobResponse.make_one(res)

    def list_cluster_events(
        self,
        res: "bs_td.ListClusterEventsResponseTypeDef",
    ) -> "dc_td.ListClusterEventsResponse":
        return dc_td.ListClusterEventsResponse.make_one(res)

    def list_cluster_nodes(
        self,
        res: "bs_td.ListClusterNodesResponseTypeDef",
    ) -> "dc_td.ListClusterNodesResponse":
        return dc_td.ListClusterNodesResponse.make_one(res)

    def list_cluster_scheduler_configs(
        self,
        res: "bs_td.ListClusterSchedulerConfigsResponseTypeDef",
    ) -> "dc_td.ListClusterSchedulerConfigsResponse":
        return dc_td.ListClusterSchedulerConfigsResponse.make_one(res)

    def list_clusters(
        self,
        res: "bs_td.ListClustersResponseTypeDef",
    ) -> "dc_td.ListClustersResponse":
        return dc_td.ListClustersResponse.make_one(res)

    def list_code_repositories(
        self,
        res: "bs_td.ListCodeRepositoriesOutputTypeDef",
    ) -> "dc_td.ListCodeRepositoriesOutput":
        return dc_td.ListCodeRepositoriesOutput.make_one(res)

    def list_compilation_jobs(
        self,
        res: "bs_td.ListCompilationJobsResponseTypeDef",
    ) -> "dc_td.ListCompilationJobsResponse":
        return dc_td.ListCompilationJobsResponse.make_one(res)

    def list_compute_quotas(
        self,
        res: "bs_td.ListComputeQuotasResponseTypeDef",
    ) -> "dc_td.ListComputeQuotasResponse":
        return dc_td.ListComputeQuotasResponse.make_one(res)

    def list_contexts(
        self,
        res: "bs_td.ListContextsResponseTypeDef",
    ) -> "dc_td.ListContextsResponse":
        return dc_td.ListContextsResponse.make_one(res)

    def list_data_quality_job_definitions(
        self,
        res: "bs_td.ListDataQualityJobDefinitionsResponseTypeDef",
    ) -> "dc_td.ListDataQualityJobDefinitionsResponse":
        return dc_td.ListDataQualityJobDefinitionsResponse.make_one(res)

    def list_device_fleets(
        self,
        res: "bs_td.ListDeviceFleetsResponseTypeDef",
    ) -> "dc_td.ListDeviceFleetsResponse":
        return dc_td.ListDeviceFleetsResponse.make_one(res)

    def list_devices(
        self,
        res: "bs_td.ListDevicesResponseTypeDef",
    ) -> "dc_td.ListDevicesResponse":
        return dc_td.ListDevicesResponse.make_one(res)

    def list_domains(
        self,
        res: "bs_td.ListDomainsResponseTypeDef",
    ) -> "dc_td.ListDomainsResponse":
        return dc_td.ListDomainsResponse.make_one(res)

    def list_edge_deployment_plans(
        self,
        res: "bs_td.ListEdgeDeploymentPlansResponseTypeDef",
    ) -> "dc_td.ListEdgeDeploymentPlansResponse":
        return dc_td.ListEdgeDeploymentPlansResponse.make_one(res)

    def list_edge_packaging_jobs(
        self,
        res: "bs_td.ListEdgePackagingJobsResponseTypeDef",
    ) -> "dc_td.ListEdgePackagingJobsResponse":
        return dc_td.ListEdgePackagingJobsResponse.make_one(res)

    def list_endpoint_configs(
        self,
        res: "bs_td.ListEndpointConfigsOutputTypeDef",
    ) -> "dc_td.ListEndpointConfigsOutput":
        return dc_td.ListEndpointConfigsOutput.make_one(res)

    def list_endpoints(
        self,
        res: "bs_td.ListEndpointsOutputTypeDef",
    ) -> "dc_td.ListEndpointsOutput":
        return dc_td.ListEndpointsOutput.make_one(res)

    def list_experiments(
        self,
        res: "bs_td.ListExperimentsResponseTypeDef",
    ) -> "dc_td.ListExperimentsResponse":
        return dc_td.ListExperimentsResponse.make_one(res)

    def list_feature_groups(
        self,
        res: "bs_td.ListFeatureGroupsResponseTypeDef",
    ) -> "dc_td.ListFeatureGroupsResponse":
        return dc_td.ListFeatureGroupsResponse.make_one(res)

    def list_flow_definitions(
        self,
        res: "bs_td.ListFlowDefinitionsResponseTypeDef",
    ) -> "dc_td.ListFlowDefinitionsResponse":
        return dc_td.ListFlowDefinitionsResponse.make_one(res)

    def list_hub_content_versions(
        self,
        res: "bs_td.ListHubContentVersionsResponseTypeDef",
    ) -> "dc_td.ListHubContentVersionsResponse":
        return dc_td.ListHubContentVersionsResponse.make_one(res)

    def list_hub_contents(
        self,
        res: "bs_td.ListHubContentsResponseTypeDef",
    ) -> "dc_td.ListHubContentsResponse":
        return dc_td.ListHubContentsResponse.make_one(res)

    def list_hubs(
        self,
        res: "bs_td.ListHubsResponseTypeDef",
    ) -> "dc_td.ListHubsResponse":
        return dc_td.ListHubsResponse.make_one(res)

    def list_human_task_uis(
        self,
        res: "bs_td.ListHumanTaskUisResponseTypeDef",
    ) -> "dc_td.ListHumanTaskUisResponse":
        return dc_td.ListHumanTaskUisResponse.make_one(res)

    def list_hyper_parameter_tuning_jobs(
        self,
        res: "bs_td.ListHyperParameterTuningJobsResponseTypeDef",
    ) -> "dc_td.ListHyperParameterTuningJobsResponse":
        return dc_td.ListHyperParameterTuningJobsResponse.make_one(res)

    def list_image_versions(
        self,
        res: "bs_td.ListImageVersionsResponseTypeDef",
    ) -> "dc_td.ListImageVersionsResponse":
        return dc_td.ListImageVersionsResponse.make_one(res)

    def list_images(
        self,
        res: "bs_td.ListImagesResponseTypeDef",
    ) -> "dc_td.ListImagesResponse":
        return dc_td.ListImagesResponse.make_one(res)

    def list_inference_components(
        self,
        res: "bs_td.ListInferenceComponentsOutputTypeDef",
    ) -> "dc_td.ListInferenceComponentsOutput":
        return dc_td.ListInferenceComponentsOutput.make_one(res)

    def list_inference_experiments(
        self,
        res: "bs_td.ListInferenceExperimentsResponseTypeDef",
    ) -> "dc_td.ListInferenceExperimentsResponse":
        return dc_td.ListInferenceExperimentsResponse.make_one(res)

    def list_inference_recommendations_job_steps(
        self,
        res: "bs_td.ListInferenceRecommendationsJobStepsResponseTypeDef",
    ) -> "dc_td.ListInferenceRecommendationsJobStepsResponse":
        return dc_td.ListInferenceRecommendationsJobStepsResponse.make_one(res)

    def list_inference_recommendations_jobs(
        self,
        res: "bs_td.ListInferenceRecommendationsJobsResponseTypeDef",
    ) -> "dc_td.ListInferenceRecommendationsJobsResponse":
        return dc_td.ListInferenceRecommendationsJobsResponse.make_one(res)

    def list_labeling_jobs(
        self,
        res: "bs_td.ListLabelingJobsResponseTypeDef",
    ) -> "dc_td.ListLabelingJobsResponse":
        return dc_td.ListLabelingJobsResponse.make_one(res)

    def list_labeling_jobs_for_workteam(
        self,
        res: "bs_td.ListLabelingJobsForWorkteamResponseTypeDef",
    ) -> "dc_td.ListLabelingJobsForWorkteamResponse":
        return dc_td.ListLabelingJobsForWorkteamResponse.make_one(res)

    def list_lineage_groups(
        self,
        res: "bs_td.ListLineageGroupsResponseTypeDef",
    ) -> "dc_td.ListLineageGroupsResponse":
        return dc_td.ListLineageGroupsResponse.make_one(res)

    def list_mlflow_tracking_servers(
        self,
        res: "bs_td.ListMlflowTrackingServersResponseTypeDef",
    ) -> "dc_td.ListMlflowTrackingServersResponse":
        return dc_td.ListMlflowTrackingServersResponse.make_one(res)

    def list_model_bias_job_definitions(
        self,
        res: "bs_td.ListModelBiasJobDefinitionsResponseTypeDef",
    ) -> "dc_td.ListModelBiasJobDefinitionsResponse":
        return dc_td.ListModelBiasJobDefinitionsResponse.make_one(res)

    def list_model_card_export_jobs(
        self,
        res: "bs_td.ListModelCardExportJobsResponseTypeDef",
    ) -> "dc_td.ListModelCardExportJobsResponse":
        return dc_td.ListModelCardExportJobsResponse.make_one(res)

    def list_model_card_versions(
        self,
        res: "bs_td.ListModelCardVersionsResponseTypeDef",
    ) -> "dc_td.ListModelCardVersionsResponse":
        return dc_td.ListModelCardVersionsResponse.make_one(res)

    def list_model_cards(
        self,
        res: "bs_td.ListModelCardsResponseTypeDef",
    ) -> "dc_td.ListModelCardsResponse":
        return dc_td.ListModelCardsResponse.make_one(res)

    def list_model_explainability_job_definitions(
        self,
        res: "bs_td.ListModelExplainabilityJobDefinitionsResponseTypeDef",
    ) -> "dc_td.ListModelExplainabilityJobDefinitionsResponse":
        return dc_td.ListModelExplainabilityJobDefinitionsResponse.make_one(res)

    def list_model_metadata(
        self,
        res: "bs_td.ListModelMetadataResponseTypeDef",
    ) -> "dc_td.ListModelMetadataResponse":
        return dc_td.ListModelMetadataResponse.make_one(res)

    def list_model_package_groups(
        self,
        res: "bs_td.ListModelPackageGroupsOutputTypeDef",
    ) -> "dc_td.ListModelPackageGroupsOutput":
        return dc_td.ListModelPackageGroupsOutput.make_one(res)

    def list_model_packages(
        self,
        res: "bs_td.ListModelPackagesOutputTypeDef",
    ) -> "dc_td.ListModelPackagesOutput":
        return dc_td.ListModelPackagesOutput.make_one(res)

    def list_model_quality_job_definitions(
        self,
        res: "bs_td.ListModelQualityJobDefinitionsResponseTypeDef",
    ) -> "dc_td.ListModelQualityJobDefinitionsResponse":
        return dc_td.ListModelQualityJobDefinitionsResponse.make_one(res)

    def list_models(
        self,
        res: "bs_td.ListModelsOutputTypeDef",
    ) -> "dc_td.ListModelsOutput":
        return dc_td.ListModelsOutput.make_one(res)

    def list_monitoring_alert_history(
        self,
        res: "bs_td.ListMonitoringAlertHistoryResponseTypeDef",
    ) -> "dc_td.ListMonitoringAlertHistoryResponse":
        return dc_td.ListMonitoringAlertHistoryResponse.make_one(res)

    def list_monitoring_alerts(
        self,
        res: "bs_td.ListMonitoringAlertsResponseTypeDef",
    ) -> "dc_td.ListMonitoringAlertsResponse":
        return dc_td.ListMonitoringAlertsResponse.make_one(res)

    def list_monitoring_executions(
        self,
        res: "bs_td.ListMonitoringExecutionsResponseTypeDef",
    ) -> "dc_td.ListMonitoringExecutionsResponse":
        return dc_td.ListMonitoringExecutionsResponse.make_one(res)

    def list_monitoring_schedules(
        self,
        res: "bs_td.ListMonitoringSchedulesResponseTypeDef",
    ) -> "dc_td.ListMonitoringSchedulesResponse":
        return dc_td.ListMonitoringSchedulesResponse.make_one(res)

    def list_notebook_instance_lifecycle_configs(
        self,
        res: "bs_td.ListNotebookInstanceLifecycleConfigsOutputTypeDef",
    ) -> "dc_td.ListNotebookInstanceLifecycleConfigsOutput":
        return dc_td.ListNotebookInstanceLifecycleConfigsOutput.make_one(res)

    def list_notebook_instances(
        self,
        res: "bs_td.ListNotebookInstancesOutputTypeDef",
    ) -> "dc_td.ListNotebookInstancesOutput":
        return dc_td.ListNotebookInstancesOutput.make_one(res)

    def list_optimization_jobs(
        self,
        res: "bs_td.ListOptimizationJobsResponseTypeDef",
    ) -> "dc_td.ListOptimizationJobsResponse":
        return dc_td.ListOptimizationJobsResponse.make_one(res)

    def list_partner_apps(
        self,
        res: "bs_td.ListPartnerAppsResponseTypeDef",
    ) -> "dc_td.ListPartnerAppsResponse":
        return dc_td.ListPartnerAppsResponse.make_one(res)

    def list_pipeline_execution_steps(
        self,
        res: "bs_td.ListPipelineExecutionStepsResponseTypeDef",
    ) -> "dc_td.ListPipelineExecutionStepsResponse":
        return dc_td.ListPipelineExecutionStepsResponse.make_one(res)

    def list_pipeline_executions(
        self,
        res: "bs_td.ListPipelineExecutionsResponseTypeDef",
    ) -> "dc_td.ListPipelineExecutionsResponse":
        return dc_td.ListPipelineExecutionsResponse.make_one(res)

    def list_pipeline_parameters_for_execution(
        self,
        res: "bs_td.ListPipelineParametersForExecutionResponseTypeDef",
    ) -> "dc_td.ListPipelineParametersForExecutionResponse":
        return dc_td.ListPipelineParametersForExecutionResponse.make_one(res)

    def list_pipeline_versions(
        self,
        res: "bs_td.ListPipelineVersionsResponseTypeDef",
    ) -> "dc_td.ListPipelineVersionsResponse":
        return dc_td.ListPipelineVersionsResponse.make_one(res)

    def list_pipelines(
        self,
        res: "bs_td.ListPipelinesResponseTypeDef",
    ) -> "dc_td.ListPipelinesResponse":
        return dc_td.ListPipelinesResponse.make_one(res)

    def list_processing_jobs(
        self,
        res: "bs_td.ListProcessingJobsResponseTypeDef",
    ) -> "dc_td.ListProcessingJobsResponse":
        return dc_td.ListProcessingJobsResponse.make_one(res)

    def list_projects(
        self,
        res: "bs_td.ListProjectsOutputTypeDef",
    ) -> "dc_td.ListProjectsOutput":
        return dc_td.ListProjectsOutput.make_one(res)

    def list_resource_catalogs(
        self,
        res: "bs_td.ListResourceCatalogsResponseTypeDef",
    ) -> "dc_td.ListResourceCatalogsResponse":
        return dc_td.ListResourceCatalogsResponse.make_one(res)

    def list_spaces(
        self,
        res: "bs_td.ListSpacesResponseTypeDef",
    ) -> "dc_td.ListSpacesResponse":
        return dc_td.ListSpacesResponse.make_one(res)

    def list_stage_devices(
        self,
        res: "bs_td.ListStageDevicesResponseTypeDef",
    ) -> "dc_td.ListStageDevicesResponse":
        return dc_td.ListStageDevicesResponse.make_one(res)

    def list_studio_lifecycle_configs(
        self,
        res: "bs_td.ListStudioLifecycleConfigsResponseTypeDef",
    ) -> "dc_td.ListStudioLifecycleConfigsResponse":
        return dc_td.ListStudioLifecycleConfigsResponse.make_one(res)

    def list_subscribed_workteams(
        self,
        res: "bs_td.ListSubscribedWorkteamsResponseTypeDef",
    ) -> "dc_td.ListSubscribedWorkteamsResponse":
        return dc_td.ListSubscribedWorkteamsResponse.make_one(res)

    def list_tags(
        self,
        res: "bs_td.ListTagsOutputTypeDef",
    ) -> "dc_td.ListTagsOutput":
        return dc_td.ListTagsOutput.make_one(res)

    def list_training_jobs(
        self,
        res: "bs_td.ListTrainingJobsResponseTypeDef",
    ) -> "dc_td.ListTrainingJobsResponse":
        return dc_td.ListTrainingJobsResponse.make_one(res)

    def list_training_jobs_for_hyper_parameter_tuning_job(
        self,
        res: "bs_td.ListTrainingJobsForHyperParameterTuningJobResponseTypeDef",
    ) -> "dc_td.ListTrainingJobsForHyperParameterTuningJobResponse":
        return dc_td.ListTrainingJobsForHyperParameterTuningJobResponse.make_one(res)

    def list_training_plans(
        self,
        res: "bs_td.ListTrainingPlansResponseTypeDef",
    ) -> "dc_td.ListTrainingPlansResponse":
        return dc_td.ListTrainingPlansResponse.make_one(res)

    def list_transform_jobs(
        self,
        res: "bs_td.ListTransformJobsResponseTypeDef",
    ) -> "dc_td.ListTransformJobsResponse":
        return dc_td.ListTransformJobsResponse.make_one(res)

    def list_trial_components(
        self,
        res: "bs_td.ListTrialComponentsResponseTypeDef",
    ) -> "dc_td.ListTrialComponentsResponse":
        return dc_td.ListTrialComponentsResponse.make_one(res)

    def list_trials(
        self,
        res: "bs_td.ListTrialsResponseTypeDef",
    ) -> "dc_td.ListTrialsResponse":
        return dc_td.ListTrialsResponse.make_one(res)

    def list_ultra_servers_by_reserved_capacity(
        self,
        res: "bs_td.ListUltraServersByReservedCapacityResponseTypeDef",
    ) -> "dc_td.ListUltraServersByReservedCapacityResponse":
        return dc_td.ListUltraServersByReservedCapacityResponse.make_one(res)

    def list_user_profiles(
        self,
        res: "bs_td.ListUserProfilesResponseTypeDef",
    ) -> "dc_td.ListUserProfilesResponse":
        return dc_td.ListUserProfilesResponse.make_one(res)

    def list_workforces(
        self,
        res: "bs_td.ListWorkforcesResponseTypeDef",
    ) -> "dc_td.ListWorkforcesResponse":
        return dc_td.ListWorkforcesResponse.make_one(res)

    def list_workteams(
        self,
        res: "bs_td.ListWorkteamsResponseTypeDef",
    ) -> "dc_td.ListWorkteamsResponse":
        return dc_td.ListWorkteamsResponse.make_one(res)

    def put_model_package_group_policy(
        self,
        res: "bs_td.PutModelPackageGroupPolicyOutputTypeDef",
    ) -> "dc_td.PutModelPackageGroupPolicyOutput":
        return dc_td.PutModelPackageGroupPolicyOutput.make_one(res)

    def query_lineage(
        self,
        res: "bs_td.QueryLineageResponseTypeDef",
    ) -> "dc_td.QueryLineageResponse":
        return dc_td.QueryLineageResponse.make_one(res)

    def register_devices(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def render_ui_template(
        self,
        res: "bs_td.RenderUiTemplateResponseTypeDef",
    ) -> "dc_td.RenderUiTemplateResponse":
        return dc_td.RenderUiTemplateResponse.make_one(res)

    def retry_pipeline_execution(
        self,
        res: "bs_td.RetryPipelineExecutionResponseTypeDef",
    ) -> "dc_td.RetryPipelineExecutionResponse":
        return dc_td.RetryPipelineExecutionResponse.make_one(res)

    def search(
        self,
        res: "bs_td.SearchResponseTypeDef",
    ) -> "dc_td.SearchResponse":
        return dc_td.SearchResponse.make_one(res)

    def search_training_plan_offerings(
        self,
        res: "bs_td.SearchTrainingPlanOfferingsResponseTypeDef",
    ) -> "dc_td.SearchTrainingPlanOfferingsResponse":
        return dc_td.SearchTrainingPlanOfferingsResponse.make_one(res)

    def send_pipeline_execution_step_failure(
        self,
        res: "bs_td.SendPipelineExecutionStepFailureResponseTypeDef",
    ) -> "dc_td.SendPipelineExecutionStepFailureResponse":
        return dc_td.SendPipelineExecutionStepFailureResponse.make_one(res)

    def send_pipeline_execution_step_success(
        self,
        res: "bs_td.SendPipelineExecutionStepSuccessResponseTypeDef",
    ) -> "dc_td.SendPipelineExecutionStepSuccessResponse":
        return dc_td.SendPipelineExecutionStepSuccessResponse.make_one(res)

    def start_edge_deployment_stage(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def start_inference_experiment(
        self,
        res: "bs_td.StartInferenceExperimentResponseTypeDef",
    ) -> "dc_td.StartInferenceExperimentResponse":
        return dc_td.StartInferenceExperimentResponse.make_one(res)

    def start_mlflow_tracking_server(
        self,
        res: "bs_td.StartMlflowTrackingServerResponseTypeDef",
    ) -> "dc_td.StartMlflowTrackingServerResponse":
        return dc_td.StartMlflowTrackingServerResponse.make_one(res)

    def start_monitoring_schedule(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def start_notebook_instance(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def start_pipeline_execution(
        self,
        res: "bs_td.StartPipelineExecutionResponseTypeDef",
    ) -> "dc_td.StartPipelineExecutionResponse":
        return dc_td.StartPipelineExecutionResponse.make_one(res)

    def start_session(
        self,
        res: "bs_td.StartSessionResponseTypeDef",
    ) -> "dc_td.StartSessionResponse":
        return dc_td.StartSessionResponse.make_one(res)

    def stop_auto_ml_job(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def stop_compilation_job(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def stop_edge_deployment_stage(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def stop_edge_packaging_job(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def stop_hyper_parameter_tuning_job(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def stop_inference_experiment(
        self,
        res: "bs_td.StopInferenceExperimentResponseTypeDef",
    ) -> "dc_td.StopInferenceExperimentResponse":
        return dc_td.StopInferenceExperimentResponse.make_one(res)

    def stop_inference_recommendations_job(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def stop_labeling_job(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def stop_mlflow_tracking_server(
        self,
        res: "bs_td.StopMlflowTrackingServerResponseTypeDef",
    ) -> "dc_td.StopMlflowTrackingServerResponse":
        return dc_td.StopMlflowTrackingServerResponse.make_one(res)

    def stop_monitoring_schedule(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def stop_notebook_instance(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def stop_optimization_job(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def stop_pipeline_execution(
        self,
        res: "bs_td.StopPipelineExecutionResponseTypeDef",
    ) -> "dc_td.StopPipelineExecutionResponse":
        return dc_td.StopPipelineExecutionResponse.make_one(res)

    def stop_processing_job(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def stop_training_job(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def stop_transform_job(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_action(
        self,
        res: "bs_td.UpdateActionResponseTypeDef",
    ) -> "dc_td.UpdateActionResponse":
        return dc_td.UpdateActionResponse.make_one(res)

    def update_app_image_config(
        self,
        res: "bs_td.UpdateAppImageConfigResponseTypeDef",
    ) -> "dc_td.UpdateAppImageConfigResponse":
        return dc_td.UpdateAppImageConfigResponse.make_one(res)

    def update_artifact(
        self,
        res: "bs_td.UpdateArtifactResponseTypeDef",
    ) -> "dc_td.UpdateArtifactResponse":
        return dc_td.UpdateArtifactResponse.make_one(res)

    def update_cluster(
        self,
        res: "bs_td.UpdateClusterResponseTypeDef",
    ) -> "dc_td.UpdateClusterResponse":
        return dc_td.UpdateClusterResponse.make_one(res)

    def update_cluster_scheduler_config(
        self,
        res: "bs_td.UpdateClusterSchedulerConfigResponseTypeDef",
    ) -> "dc_td.UpdateClusterSchedulerConfigResponse":
        return dc_td.UpdateClusterSchedulerConfigResponse.make_one(res)

    def update_cluster_software(
        self,
        res: "bs_td.UpdateClusterSoftwareResponseTypeDef",
    ) -> "dc_td.UpdateClusterSoftwareResponse":
        return dc_td.UpdateClusterSoftwareResponse.make_one(res)

    def update_code_repository(
        self,
        res: "bs_td.UpdateCodeRepositoryOutputTypeDef",
    ) -> "dc_td.UpdateCodeRepositoryOutput":
        return dc_td.UpdateCodeRepositoryOutput.make_one(res)

    def update_compute_quota(
        self,
        res: "bs_td.UpdateComputeQuotaResponseTypeDef",
    ) -> "dc_td.UpdateComputeQuotaResponse":
        return dc_td.UpdateComputeQuotaResponse.make_one(res)

    def update_context(
        self,
        res: "bs_td.UpdateContextResponseTypeDef",
    ) -> "dc_td.UpdateContextResponse":
        return dc_td.UpdateContextResponse.make_one(res)

    def update_device_fleet(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_devices(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_domain(
        self,
        res: "bs_td.UpdateDomainResponseTypeDef",
    ) -> "dc_td.UpdateDomainResponse":
        return dc_td.UpdateDomainResponse.make_one(res)

    def update_endpoint(
        self,
        res: "bs_td.UpdateEndpointOutputTypeDef",
    ) -> "dc_td.UpdateEndpointOutput":
        return dc_td.UpdateEndpointOutput.make_one(res)

    def update_endpoint_weights_and_capacities(
        self,
        res: "bs_td.UpdateEndpointWeightsAndCapacitiesOutputTypeDef",
    ) -> "dc_td.UpdateEndpointWeightsAndCapacitiesOutput":
        return dc_td.UpdateEndpointWeightsAndCapacitiesOutput.make_one(res)

    def update_experiment(
        self,
        res: "bs_td.UpdateExperimentResponseTypeDef",
    ) -> "dc_td.UpdateExperimentResponse":
        return dc_td.UpdateExperimentResponse.make_one(res)

    def update_feature_group(
        self,
        res: "bs_td.UpdateFeatureGroupResponseTypeDef",
    ) -> "dc_td.UpdateFeatureGroupResponse":
        return dc_td.UpdateFeatureGroupResponse.make_one(res)

    def update_feature_metadata(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_hub(
        self,
        res: "bs_td.UpdateHubResponseTypeDef",
    ) -> "dc_td.UpdateHubResponse":
        return dc_td.UpdateHubResponse.make_one(res)

    def update_hub_content(
        self,
        res: "bs_td.UpdateHubContentResponseTypeDef",
    ) -> "dc_td.UpdateHubContentResponse":
        return dc_td.UpdateHubContentResponse.make_one(res)

    def update_hub_content_reference(
        self,
        res: "bs_td.UpdateHubContentReferenceResponseTypeDef",
    ) -> "dc_td.UpdateHubContentReferenceResponse":
        return dc_td.UpdateHubContentReferenceResponse.make_one(res)

    def update_image(
        self,
        res: "bs_td.UpdateImageResponseTypeDef",
    ) -> "dc_td.UpdateImageResponse":
        return dc_td.UpdateImageResponse.make_one(res)

    def update_image_version(
        self,
        res: "bs_td.UpdateImageVersionResponseTypeDef",
    ) -> "dc_td.UpdateImageVersionResponse":
        return dc_td.UpdateImageVersionResponse.make_one(res)

    def update_inference_component(
        self,
        res: "bs_td.UpdateInferenceComponentOutputTypeDef",
    ) -> "dc_td.UpdateInferenceComponentOutput":
        return dc_td.UpdateInferenceComponentOutput.make_one(res)

    def update_inference_component_runtime_config(
        self,
        res: "bs_td.UpdateInferenceComponentRuntimeConfigOutputTypeDef",
    ) -> "dc_td.UpdateInferenceComponentRuntimeConfigOutput":
        return dc_td.UpdateInferenceComponentRuntimeConfigOutput.make_one(res)

    def update_inference_experiment(
        self,
        res: "bs_td.UpdateInferenceExperimentResponseTypeDef",
    ) -> "dc_td.UpdateInferenceExperimentResponse":
        return dc_td.UpdateInferenceExperimentResponse.make_one(res)

    def update_mlflow_tracking_server(
        self,
        res: "bs_td.UpdateMlflowTrackingServerResponseTypeDef",
    ) -> "dc_td.UpdateMlflowTrackingServerResponse":
        return dc_td.UpdateMlflowTrackingServerResponse.make_one(res)

    def update_model_card(
        self,
        res: "bs_td.UpdateModelCardResponseTypeDef",
    ) -> "dc_td.UpdateModelCardResponse":
        return dc_td.UpdateModelCardResponse.make_one(res)

    def update_model_package(
        self,
        res: "bs_td.UpdateModelPackageOutputTypeDef",
    ) -> "dc_td.UpdateModelPackageOutput":
        return dc_td.UpdateModelPackageOutput.make_one(res)

    def update_monitoring_alert(
        self,
        res: "bs_td.UpdateMonitoringAlertResponseTypeDef",
    ) -> "dc_td.UpdateMonitoringAlertResponse":
        return dc_td.UpdateMonitoringAlertResponse.make_one(res)

    def update_monitoring_schedule(
        self,
        res: "bs_td.UpdateMonitoringScheduleResponseTypeDef",
    ) -> "dc_td.UpdateMonitoringScheduleResponse":
        return dc_td.UpdateMonitoringScheduleResponse.make_one(res)

    def update_partner_app(
        self,
        res: "bs_td.UpdatePartnerAppResponseTypeDef",
    ) -> "dc_td.UpdatePartnerAppResponse":
        return dc_td.UpdatePartnerAppResponse.make_one(res)

    def update_pipeline(
        self,
        res: "bs_td.UpdatePipelineResponseTypeDef",
    ) -> "dc_td.UpdatePipelineResponse":
        return dc_td.UpdatePipelineResponse.make_one(res)

    def update_pipeline_execution(
        self,
        res: "bs_td.UpdatePipelineExecutionResponseTypeDef",
    ) -> "dc_td.UpdatePipelineExecutionResponse":
        return dc_td.UpdatePipelineExecutionResponse.make_one(res)

    def update_pipeline_version(
        self,
        res: "bs_td.UpdatePipelineVersionResponseTypeDef",
    ) -> "dc_td.UpdatePipelineVersionResponse":
        return dc_td.UpdatePipelineVersionResponse.make_one(res)

    def update_project(
        self,
        res: "bs_td.UpdateProjectOutputTypeDef",
    ) -> "dc_td.UpdateProjectOutput":
        return dc_td.UpdateProjectOutput.make_one(res)

    def update_space(
        self,
        res: "bs_td.UpdateSpaceResponseTypeDef",
    ) -> "dc_td.UpdateSpaceResponse":
        return dc_td.UpdateSpaceResponse.make_one(res)

    def update_training_job(
        self,
        res: "bs_td.UpdateTrainingJobResponseTypeDef",
    ) -> "dc_td.UpdateTrainingJobResponse":
        return dc_td.UpdateTrainingJobResponse.make_one(res)

    def update_trial(
        self,
        res: "bs_td.UpdateTrialResponseTypeDef",
    ) -> "dc_td.UpdateTrialResponse":
        return dc_td.UpdateTrialResponse.make_one(res)

    def update_trial_component(
        self,
        res: "bs_td.UpdateTrialComponentResponseTypeDef",
    ) -> "dc_td.UpdateTrialComponentResponse":
        return dc_td.UpdateTrialComponentResponse.make_one(res)

    def update_user_profile(
        self,
        res: "bs_td.UpdateUserProfileResponseTypeDef",
    ) -> "dc_td.UpdateUserProfileResponse":
        return dc_td.UpdateUserProfileResponse.make_one(res)

    def update_workforce(
        self,
        res: "bs_td.UpdateWorkforceResponseTypeDef",
    ) -> "dc_td.UpdateWorkforceResponse":
        return dc_td.UpdateWorkforceResponse.make_one(res)

    def update_workteam(
        self,
        res: "bs_td.UpdateWorkteamResponseTypeDef",
    ) -> "dc_td.UpdateWorkteamResponse":
        return dc_td.UpdateWorkteamResponse.make_one(res)


sagemaker_caster = SAGEMAKERCaster()
