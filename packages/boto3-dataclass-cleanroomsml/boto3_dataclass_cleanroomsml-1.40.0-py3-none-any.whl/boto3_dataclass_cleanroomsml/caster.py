# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_cleanroomsml import type_defs as bs_td


class CLEANROOMSMLCaster:

    def cancel_trained_model(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def cancel_trained_model_inference_job(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def create_audience_model(
        self,
        res: "bs_td.CreateAudienceModelResponseTypeDef",
    ) -> "dc_td.CreateAudienceModelResponse":
        return dc_td.CreateAudienceModelResponse.make_one(res)

    def create_configured_audience_model(
        self,
        res: "bs_td.CreateConfiguredAudienceModelResponseTypeDef",
    ) -> "dc_td.CreateConfiguredAudienceModelResponse":
        return dc_td.CreateConfiguredAudienceModelResponse.make_one(res)

    def create_configured_model_algorithm(
        self,
        res: "bs_td.CreateConfiguredModelAlgorithmResponseTypeDef",
    ) -> "dc_td.CreateConfiguredModelAlgorithmResponse":
        return dc_td.CreateConfiguredModelAlgorithmResponse.make_one(res)

    def create_configured_model_algorithm_association(
        self,
        res: "bs_td.CreateConfiguredModelAlgorithmAssociationResponseTypeDef",
    ) -> "dc_td.CreateConfiguredModelAlgorithmAssociationResponse":
        return dc_td.CreateConfiguredModelAlgorithmAssociationResponse.make_one(res)

    def create_ml_input_channel(
        self,
        res: "bs_td.CreateMLInputChannelResponseTypeDef",
    ) -> "dc_td.CreateMLInputChannelResponse":
        return dc_td.CreateMLInputChannelResponse.make_one(res)

    def create_trained_model(
        self,
        res: "bs_td.CreateTrainedModelResponseTypeDef",
    ) -> "dc_td.CreateTrainedModelResponse":
        return dc_td.CreateTrainedModelResponse.make_one(res)

    def create_training_dataset(
        self,
        res: "bs_td.CreateTrainingDatasetResponseTypeDef",
    ) -> "dc_td.CreateTrainingDatasetResponse":
        return dc_td.CreateTrainingDatasetResponse.make_one(res)

    def delete_audience_generation_job(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_audience_model(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_configured_audience_model(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_configured_audience_model_policy(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_configured_model_algorithm(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_configured_model_algorithm_association(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_ml_configuration(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_ml_input_channel_data(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_trained_model_output(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_training_dataset(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def get_audience_generation_job(
        self,
        res: "bs_td.GetAudienceGenerationJobResponseTypeDef",
    ) -> "dc_td.GetAudienceGenerationJobResponse":
        return dc_td.GetAudienceGenerationJobResponse.make_one(res)

    def get_audience_model(
        self,
        res: "bs_td.GetAudienceModelResponseTypeDef",
    ) -> "dc_td.GetAudienceModelResponse":
        return dc_td.GetAudienceModelResponse.make_one(res)

    def get_collaboration_configured_model_algorithm_association(
        self,
        res: "bs_td.GetCollaborationConfiguredModelAlgorithmAssociationResponseTypeDef",
    ) -> "dc_td.GetCollaborationConfiguredModelAlgorithmAssociationResponse":
        return (
            dc_td.GetCollaborationConfiguredModelAlgorithmAssociationResponse.make_one(
                res
            )
        )

    def get_collaboration_ml_input_channel(
        self,
        res: "bs_td.GetCollaborationMLInputChannelResponseTypeDef",
    ) -> "dc_td.GetCollaborationMLInputChannelResponse":
        return dc_td.GetCollaborationMLInputChannelResponse.make_one(res)

    def get_collaboration_trained_model(
        self,
        res: "bs_td.GetCollaborationTrainedModelResponseTypeDef",
    ) -> "dc_td.GetCollaborationTrainedModelResponse":
        return dc_td.GetCollaborationTrainedModelResponse.make_one(res)

    def get_configured_audience_model(
        self,
        res: "bs_td.GetConfiguredAudienceModelResponseTypeDef",
    ) -> "dc_td.GetConfiguredAudienceModelResponse":
        return dc_td.GetConfiguredAudienceModelResponse.make_one(res)

    def get_configured_audience_model_policy(
        self,
        res: "bs_td.GetConfiguredAudienceModelPolicyResponseTypeDef",
    ) -> "dc_td.GetConfiguredAudienceModelPolicyResponse":
        return dc_td.GetConfiguredAudienceModelPolicyResponse.make_one(res)

    def get_configured_model_algorithm(
        self,
        res: "bs_td.GetConfiguredModelAlgorithmResponseTypeDef",
    ) -> "dc_td.GetConfiguredModelAlgorithmResponse":
        return dc_td.GetConfiguredModelAlgorithmResponse.make_one(res)

    def get_configured_model_algorithm_association(
        self,
        res: "bs_td.GetConfiguredModelAlgorithmAssociationResponseTypeDef",
    ) -> "dc_td.GetConfiguredModelAlgorithmAssociationResponse":
        return dc_td.GetConfiguredModelAlgorithmAssociationResponse.make_one(res)

    def get_ml_configuration(
        self,
        res: "bs_td.GetMLConfigurationResponseTypeDef",
    ) -> "dc_td.GetMLConfigurationResponse":
        return dc_td.GetMLConfigurationResponse.make_one(res)

    def get_ml_input_channel(
        self,
        res: "bs_td.GetMLInputChannelResponseTypeDef",
    ) -> "dc_td.GetMLInputChannelResponse":
        return dc_td.GetMLInputChannelResponse.make_one(res)

    def get_trained_model(
        self,
        res: "bs_td.GetTrainedModelResponseTypeDef",
    ) -> "dc_td.GetTrainedModelResponse":
        return dc_td.GetTrainedModelResponse.make_one(res)

    def get_trained_model_inference_job(
        self,
        res: "bs_td.GetTrainedModelInferenceJobResponseTypeDef",
    ) -> "dc_td.GetTrainedModelInferenceJobResponse":
        return dc_td.GetTrainedModelInferenceJobResponse.make_one(res)

    def get_training_dataset(
        self,
        res: "bs_td.GetTrainingDatasetResponseTypeDef",
    ) -> "dc_td.GetTrainingDatasetResponse":
        return dc_td.GetTrainingDatasetResponse.make_one(res)

    def list_audience_export_jobs(
        self,
        res: "bs_td.ListAudienceExportJobsResponseTypeDef",
    ) -> "dc_td.ListAudienceExportJobsResponse":
        return dc_td.ListAudienceExportJobsResponse.make_one(res)

    def list_audience_generation_jobs(
        self,
        res: "bs_td.ListAudienceGenerationJobsResponseTypeDef",
    ) -> "dc_td.ListAudienceGenerationJobsResponse":
        return dc_td.ListAudienceGenerationJobsResponse.make_one(res)

    def list_audience_models(
        self,
        res: "bs_td.ListAudienceModelsResponseTypeDef",
    ) -> "dc_td.ListAudienceModelsResponse":
        return dc_td.ListAudienceModelsResponse.make_one(res)

    def list_collaboration_configured_model_algorithm_associations(
        self,
        res: "bs_td.ListCollaborationConfiguredModelAlgorithmAssociationsResponseTypeDef",
    ) -> "dc_td.ListCollaborationConfiguredModelAlgorithmAssociationsResponse":
        return dc_td.ListCollaborationConfiguredModelAlgorithmAssociationsResponse.make_one(
            res
        )

    def list_collaboration_ml_input_channels(
        self,
        res: "bs_td.ListCollaborationMLInputChannelsResponseTypeDef",
    ) -> "dc_td.ListCollaborationMLInputChannelsResponse":
        return dc_td.ListCollaborationMLInputChannelsResponse.make_one(res)

    def list_collaboration_trained_model_export_jobs(
        self,
        res: "bs_td.ListCollaborationTrainedModelExportJobsResponseTypeDef",
    ) -> "dc_td.ListCollaborationTrainedModelExportJobsResponse":
        return dc_td.ListCollaborationTrainedModelExportJobsResponse.make_one(res)

    def list_collaboration_trained_model_inference_jobs(
        self,
        res: "bs_td.ListCollaborationTrainedModelInferenceJobsResponseTypeDef",
    ) -> "dc_td.ListCollaborationTrainedModelInferenceJobsResponse":
        return dc_td.ListCollaborationTrainedModelInferenceJobsResponse.make_one(res)

    def list_collaboration_trained_models(
        self,
        res: "bs_td.ListCollaborationTrainedModelsResponseTypeDef",
    ) -> "dc_td.ListCollaborationTrainedModelsResponse":
        return dc_td.ListCollaborationTrainedModelsResponse.make_one(res)

    def list_configured_audience_models(
        self,
        res: "bs_td.ListConfiguredAudienceModelsResponseTypeDef",
    ) -> "dc_td.ListConfiguredAudienceModelsResponse":
        return dc_td.ListConfiguredAudienceModelsResponse.make_one(res)

    def list_configured_model_algorithm_associations(
        self,
        res: "bs_td.ListConfiguredModelAlgorithmAssociationsResponseTypeDef",
    ) -> "dc_td.ListConfiguredModelAlgorithmAssociationsResponse":
        return dc_td.ListConfiguredModelAlgorithmAssociationsResponse.make_one(res)

    def list_configured_model_algorithms(
        self,
        res: "bs_td.ListConfiguredModelAlgorithmsResponseTypeDef",
    ) -> "dc_td.ListConfiguredModelAlgorithmsResponse":
        return dc_td.ListConfiguredModelAlgorithmsResponse.make_one(res)

    def list_ml_input_channels(
        self,
        res: "bs_td.ListMLInputChannelsResponseTypeDef",
    ) -> "dc_td.ListMLInputChannelsResponse":
        return dc_td.ListMLInputChannelsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def list_trained_model_inference_jobs(
        self,
        res: "bs_td.ListTrainedModelInferenceJobsResponseTypeDef",
    ) -> "dc_td.ListTrainedModelInferenceJobsResponse":
        return dc_td.ListTrainedModelInferenceJobsResponse.make_one(res)

    def list_trained_model_versions(
        self,
        res: "bs_td.ListTrainedModelVersionsResponseTypeDef",
    ) -> "dc_td.ListTrainedModelVersionsResponse":
        return dc_td.ListTrainedModelVersionsResponse.make_one(res)

    def list_trained_models(
        self,
        res: "bs_td.ListTrainedModelsResponseTypeDef",
    ) -> "dc_td.ListTrainedModelsResponse":
        return dc_td.ListTrainedModelsResponse.make_one(res)

    def list_training_datasets(
        self,
        res: "bs_td.ListTrainingDatasetsResponseTypeDef",
    ) -> "dc_td.ListTrainingDatasetsResponse":
        return dc_td.ListTrainingDatasetsResponse.make_one(res)

    def put_configured_audience_model_policy(
        self,
        res: "bs_td.PutConfiguredAudienceModelPolicyResponseTypeDef",
    ) -> "dc_td.PutConfiguredAudienceModelPolicyResponse":
        return dc_td.PutConfiguredAudienceModelPolicyResponse.make_one(res)

    def put_ml_configuration(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def start_audience_export_job(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def start_audience_generation_job(
        self,
        res: "bs_td.StartAudienceGenerationJobResponseTypeDef",
    ) -> "dc_td.StartAudienceGenerationJobResponse":
        return dc_td.StartAudienceGenerationJobResponse.make_one(res)

    def start_trained_model_export_job(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def start_trained_model_inference_job(
        self,
        res: "bs_td.StartTrainedModelInferenceJobResponseTypeDef",
    ) -> "dc_td.StartTrainedModelInferenceJobResponse":
        return dc_td.StartTrainedModelInferenceJobResponse.make_one(res)

    def update_configured_audience_model(
        self,
        res: "bs_td.UpdateConfiguredAudienceModelResponseTypeDef",
    ) -> "dc_td.UpdateConfiguredAudienceModelResponse":
        return dc_td.UpdateConfiguredAudienceModelResponse.make_one(res)


cleanroomsml_caster = CLEANROOMSMLCaster()
