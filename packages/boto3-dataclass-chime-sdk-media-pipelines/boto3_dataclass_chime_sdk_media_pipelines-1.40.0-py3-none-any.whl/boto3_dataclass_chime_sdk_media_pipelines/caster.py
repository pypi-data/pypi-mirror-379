# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_chime_sdk_media_pipelines import type_defs as bs_td


class CHIME_SDK_MEDIA_PIPELINESCaster:

    def create_media_capture_pipeline(
        self,
        res: "bs_td.CreateMediaCapturePipelineResponseTypeDef",
    ) -> "dc_td.CreateMediaCapturePipelineResponse":
        return dc_td.CreateMediaCapturePipelineResponse.make_one(res)

    def create_media_concatenation_pipeline(
        self,
        res: "bs_td.CreateMediaConcatenationPipelineResponseTypeDef",
    ) -> "dc_td.CreateMediaConcatenationPipelineResponse":
        return dc_td.CreateMediaConcatenationPipelineResponse.make_one(res)

    def create_media_insights_pipeline(
        self,
        res: "bs_td.CreateMediaInsightsPipelineResponseTypeDef",
    ) -> "dc_td.CreateMediaInsightsPipelineResponse":
        return dc_td.CreateMediaInsightsPipelineResponse.make_one(res)

    def create_media_insights_pipeline_configuration(
        self,
        res: "bs_td.CreateMediaInsightsPipelineConfigurationResponseTypeDef",
    ) -> "dc_td.CreateMediaInsightsPipelineConfigurationResponse":
        return dc_td.CreateMediaInsightsPipelineConfigurationResponse.make_one(res)

    def create_media_live_connector_pipeline(
        self,
        res: "bs_td.CreateMediaLiveConnectorPipelineResponseTypeDef",
    ) -> "dc_td.CreateMediaLiveConnectorPipelineResponse":
        return dc_td.CreateMediaLiveConnectorPipelineResponse.make_one(res)

    def create_media_pipeline_kinesis_video_stream_pool(
        self,
        res: "bs_td.CreateMediaPipelineKinesisVideoStreamPoolResponseTypeDef",
    ) -> "dc_td.CreateMediaPipelineKinesisVideoStreamPoolResponse":
        return dc_td.CreateMediaPipelineKinesisVideoStreamPoolResponse.make_one(res)

    def create_media_stream_pipeline(
        self,
        res: "bs_td.CreateMediaStreamPipelineResponseTypeDef",
    ) -> "dc_td.CreateMediaStreamPipelineResponse":
        return dc_td.CreateMediaStreamPipelineResponse.make_one(res)

    def delete_media_capture_pipeline(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_media_insights_pipeline_configuration(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_media_pipeline(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_media_pipeline_kinesis_video_stream_pool(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def get_media_capture_pipeline(
        self,
        res: "bs_td.GetMediaCapturePipelineResponseTypeDef",
    ) -> "dc_td.GetMediaCapturePipelineResponse":
        return dc_td.GetMediaCapturePipelineResponse.make_one(res)

    def get_media_insights_pipeline_configuration(
        self,
        res: "bs_td.GetMediaInsightsPipelineConfigurationResponseTypeDef",
    ) -> "dc_td.GetMediaInsightsPipelineConfigurationResponse":
        return dc_td.GetMediaInsightsPipelineConfigurationResponse.make_one(res)

    def get_media_pipeline(
        self,
        res: "bs_td.GetMediaPipelineResponseTypeDef",
    ) -> "dc_td.GetMediaPipelineResponse":
        return dc_td.GetMediaPipelineResponse.make_one(res)

    def get_media_pipeline_kinesis_video_stream_pool(
        self,
        res: "bs_td.GetMediaPipelineKinesisVideoStreamPoolResponseTypeDef",
    ) -> "dc_td.GetMediaPipelineKinesisVideoStreamPoolResponse":
        return dc_td.GetMediaPipelineKinesisVideoStreamPoolResponse.make_one(res)

    def get_speaker_search_task(
        self,
        res: "bs_td.GetSpeakerSearchTaskResponseTypeDef",
    ) -> "dc_td.GetSpeakerSearchTaskResponse":
        return dc_td.GetSpeakerSearchTaskResponse.make_one(res)

    def get_voice_tone_analysis_task(
        self,
        res: "bs_td.GetVoiceToneAnalysisTaskResponseTypeDef",
    ) -> "dc_td.GetVoiceToneAnalysisTaskResponse":
        return dc_td.GetVoiceToneAnalysisTaskResponse.make_one(res)

    def list_media_capture_pipelines(
        self,
        res: "bs_td.ListMediaCapturePipelinesResponseTypeDef",
    ) -> "dc_td.ListMediaCapturePipelinesResponse":
        return dc_td.ListMediaCapturePipelinesResponse.make_one(res)

    def list_media_insights_pipeline_configurations(
        self,
        res: "bs_td.ListMediaInsightsPipelineConfigurationsResponseTypeDef",
    ) -> "dc_td.ListMediaInsightsPipelineConfigurationsResponse":
        return dc_td.ListMediaInsightsPipelineConfigurationsResponse.make_one(res)

    def list_media_pipeline_kinesis_video_stream_pools(
        self,
        res: "bs_td.ListMediaPipelineKinesisVideoStreamPoolsResponseTypeDef",
    ) -> "dc_td.ListMediaPipelineKinesisVideoStreamPoolsResponse":
        return dc_td.ListMediaPipelineKinesisVideoStreamPoolsResponse.make_one(res)

    def list_media_pipelines(
        self,
        res: "bs_td.ListMediaPipelinesResponseTypeDef",
    ) -> "dc_td.ListMediaPipelinesResponse":
        return dc_td.ListMediaPipelinesResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def start_speaker_search_task(
        self,
        res: "bs_td.StartSpeakerSearchTaskResponseTypeDef",
    ) -> "dc_td.StartSpeakerSearchTaskResponse":
        return dc_td.StartSpeakerSearchTaskResponse.make_one(res)

    def start_voice_tone_analysis_task(
        self,
        res: "bs_td.StartVoiceToneAnalysisTaskResponseTypeDef",
    ) -> "dc_td.StartVoiceToneAnalysisTaskResponse":
        return dc_td.StartVoiceToneAnalysisTaskResponse.make_one(res)

    def stop_speaker_search_task(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def stop_voice_tone_analysis_task(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_media_insights_pipeline_configuration(
        self,
        res: "bs_td.UpdateMediaInsightsPipelineConfigurationResponseTypeDef",
    ) -> "dc_td.UpdateMediaInsightsPipelineConfigurationResponse":
        return dc_td.UpdateMediaInsightsPipelineConfigurationResponse.make_one(res)

    def update_media_insights_pipeline_status(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_media_pipeline_kinesis_video_stream_pool(
        self,
        res: "bs_td.UpdateMediaPipelineKinesisVideoStreamPoolResponseTypeDef",
    ) -> "dc_td.UpdateMediaPipelineKinesisVideoStreamPoolResponse":
        return dc_td.UpdateMediaPipelineKinesisVideoStreamPoolResponse.make_one(res)


chime_sdk_media_pipelines_caster = CHIME_SDK_MEDIA_PIPELINESCaster()
