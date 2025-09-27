# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_chime_sdk_media_pipelines import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class ActiveSpeakerOnlyConfiguration:
    boto3_raw_data: "type_defs.ActiveSpeakerOnlyConfigurationTypeDef" = (
        dataclasses.field()
    )

    ActiveSpeakerPosition = field("ActiveSpeakerPosition")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ActiveSpeakerOnlyConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActiveSpeakerOnlyConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PostCallAnalyticsSettings:
    boto3_raw_data: "type_defs.PostCallAnalyticsSettingsTypeDef" = dataclasses.field()

    OutputLocation = field("OutputLocation")
    DataAccessRoleArn = field("DataAccessRoleArn")
    ContentRedactionOutput = field("ContentRedactionOutput")
    OutputEncryptionKMSKeyId = field("OutputEncryptionKMSKeyId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PostCallAnalyticsSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PostCallAnalyticsSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AmazonTranscribeProcessorConfiguration:
    boto3_raw_data: "type_defs.AmazonTranscribeProcessorConfigurationTypeDef" = (
        dataclasses.field()
    )

    LanguageCode = field("LanguageCode")
    VocabularyName = field("VocabularyName")
    VocabularyFilterName = field("VocabularyFilterName")
    VocabularyFilterMethod = field("VocabularyFilterMethod")
    ShowSpeakerLabel = field("ShowSpeakerLabel")
    EnablePartialResultsStabilization = field("EnablePartialResultsStabilization")
    PartialResultsStability = field("PartialResultsStability")
    ContentIdentificationType = field("ContentIdentificationType")
    ContentRedactionType = field("ContentRedactionType")
    PiiEntityTypes = field("PiiEntityTypes")
    LanguageModelName = field("LanguageModelName")
    FilterPartialResults = field("FilterPartialResults")
    IdentifyLanguage = field("IdentifyLanguage")
    IdentifyMultipleLanguages = field("IdentifyMultipleLanguages")
    LanguageOptions = field("LanguageOptions")
    PreferredLanguage = field("PreferredLanguage")
    VocabularyNames = field("VocabularyNames")
    VocabularyFilterNames = field("VocabularyFilterNames")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AmazonTranscribeProcessorConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AmazonTranscribeProcessorConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AudioConcatenationConfiguration:
    boto3_raw_data: "type_defs.AudioConcatenationConfigurationTypeDef" = (
        dataclasses.field()
    )

    State = field("State")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AudioConcatenationConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AudioConcatenationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CompositedVideoConcatenationConfiguration:
    boto3_raw_data: "type_defs.CompositedVideoConcatenationConfigurationTypeDef" = (
        dataclasses.field()
    )

    State = field("State")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CompositedVideoConcatenationConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CompositedVideoConcatenationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContentConcatenationConfiguration:
    boto3_raw_data: "type_defs.ContentConcatenationConfigurationTypeDef" = (
        dataclasses.field()
    )

    State = field("State")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ContentConcatenationConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContentConcatenationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataChannelConcatenationConfiguration:
    boto3_raw_data: "type_defs.DataChannelConcatenationConfigurationTypeDef" = (
        dataclasses.field()
    )

    State = field("State")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DataChannelConcatenationConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataChannelConcatenationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MeetingEventsConcatenationConfiguration:
    boto3_raw_data: "type_defs.MeetingEventsConcatenationConfigurationTypeDef" = (
        dataclasses.field()
    )

    State = field("State")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MeetingEventsConcatenationConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MeetingEventsConcatenationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TranscriptionMessagesConcatenationConfiguration:
    boto3_raw_data: (
        "type_defs.TranscriptionMessagesConcatenationConfigurationTypeDef"
    ) = dataclasses.field()

    State = field("State")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.TranscriptionMessagesConcatenationConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.TranscriptionMessagesConcatenationConfigurationTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VideoConcatenationConfiguration:
    boto3_raw_data: "type_defs.VideoConcatenationConfigurationTypeDef" = (
        dataclasses.field()
    )

    State = field("State")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.VideoConcatenationConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VideoConcatenationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AudioArtifactsConfiguration:
    boto3_raw_data: "type_defs.AudioArtifactsConfigurationTypeDef" = dataclasses.field()

    MuxType = field("MuxType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AudioArtifactsConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AudioArtifactsConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContentArtifactsConfiguration:
    boto3_raw_data: "type_defs.ContentArtifactsConfigurationTypeDef" = (
        dataclasses.field()
    )

    State = field("State")
    MuxType = field("MuxType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ContentArtifactsConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContentArtifactsConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VideoArtifactsConfiguration:
    boto3_raw_data: "type_defs.VideoArtifactsConfigurationTypeDef" = dataclasses.field()

    State = field("State")
    MuxType = field("MuxType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VideoArtifactsConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VideoArtifactsConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChannelDefinition:
    boto3_raw_data: "type_defs.ChannelDefinitionTypeDef" = dataclasses.field()

    ChannelId = field("ChannelId")
    ParticipantRole = field("ParticipantRole")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ChannelDefinitionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ChannelDefinitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3BucketSinkConfiguration:
    boto3_raw_data: "type_defs.S3BucketSinkConfigurationTypeDef" = dataclasses.field()

    Destination = field("Destination")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3BucketSinkConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3BucketSinkConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SseAwsKeyManagementParams:
    boto3_raw_data: "type_defs.SseAwsKeyManagementParamsTypeDef" = dataclasses.field()

    AwsKmsKeyId = field("AwsKmsKeyId")
    AwsKmsEncryptionContext = field("AwsKmsEncryptionContext")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SseAwsKeyManagementParamsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SseAwsKeyManagementParamsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Tag:
    boto3_raw_data: "type_defs.TagTypeDef" = dataclasses.field()

    Key = field("Key")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TagTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TagTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResponseMetadata:
    boto3_raw_data: "type_defs.ResponseMetadataTypeDef" = dataclasses.field()

    RequestId = field("RequestId")
    HTTPStatusCode = field("HTTPStatusCode")
    HTTPHeaders = field("HTTPHeaders")
    RetryAttempts = field("RetryAttempts")
    HostId = field("HostId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResponseMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResponseMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3RecordingSinkRuntimeConfiguration:
    boto3_raw_data: "type_defs.S3RecordingSinkRuntimeConfigurationTypeDef" = (
        dataclasses.field()
    )

    Destination = field("Destination")
    RecordingFileFormat = field("RecordingFileFormat")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.S3RecordingSinkRuntimeConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3RecordingSinkRuntimeConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KinesisVideoStreamConfiguration:
    boto3_raw_data: "type_defs.KinesisVideoStreamConfigurationTypeDef" = (
        dataclasses.field()
    )

    Region = field("Region")
    DataRetentionInHours = field("DataRetentionInHours")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.KinesisVideoStreamConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KinesisVideoStreamConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MediaStreamSink:
    boto3_raw_data: "type_defs.MediaStreamSinkTypeDef" = dataclasses.field()

    SinkArn = field("SinkArn")
    SinkType = field("SinkType")
    ReservedStreamCapacity = field("ReservedStreamCapacity")
    MediaStreamType = field("MediaStreamType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MediaStreamSinkTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MediaStreamSinkTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MediaStreamSource:
    boto3_raw_data: "type_defs.MediaStreamSourceTypeDef" = dataclasses.field()

    SourceType = field("SourceType")
    SourceArn = field("SourceArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MediaStreamSourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MediaStreamSourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteMediaCapturePipelineRequest:
    boto3_raw_data: "type_defs.DeleteMediaCapturePipelineRequestTypeDef" = (
        dataclasses.field()
    )

    MediaPipelineId = field("MediaPipelineId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteMediaCapturePipelineRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteMediaCapturePipelineRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteMediaInsightsPipelineConfigurationRequest:
    boto3_raw_data: (
        "type_defs.DeleteMediaInsightsPipelineConfigurationRequestTypeDef"
    ) = dataclasses.field()

    Identifier = field("Identifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteMediaInsightsPipelineConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.DeleteMediaInsightsPipelineConfigurationRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteMediaPipelineKinesisVideoStreamPoolRequest:
    boto3_raw_data: (
        "type_defs.DeleteMediaPipelineKinesisVideoStreamPoolRequestTypeDef"
    ) = dataclasses.field()

    Identifier = field("Identifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteMediaPipelineKinesisVideoStreamPoolRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.DeleteMediaPipelineKinesisVideoStreamPoolRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteMediaPipelineRequest:
    boto3_raw_data: "type_defs.DeleteMediaPipelineRequestTypeDef" = dataclasses.field()

    MediaPipelineId = field("MediaPipelineId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteMediaPipelineRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteMediaPipelineRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TimestampRangeOutput:
    boto3_raw_data: "type_defs.TimestampRangeOutputTypeDef" = dataclasses.field()

    StartTimestamp = field("StartTimestamp")
    EndTimestamp = field("EndTimestamp")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TimestampRangeOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TimestampRangeOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMediaCapturePipelineRequest:
    boto3_raw_data: "type_defs.GetMediaCapturePipelineRequestTypeDef" = (
        dataclasses.field()
    )

    MediaPipelineId = field("MediaPipelineId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetMediaCapturePipelineRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMediaCapturePipelineRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMediaInsightsPipelineConfigurationRequest:
    boto3_raw_data: "type_defs.GetMediaInsightsPipelineConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    Identifier = field("Identifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetMediaInsightsPipelineConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMediaInsightsPipelineConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMediaPipelineKinesisVideoStreamPoolRequest:
    boto3_raw_data: "type_defs.GetMediaPipelineKinesisVideoStreamPoolRequestTypeDef" = (
        dataclasses.field()
    )

    Identifier = field("Identifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetMediaPipelineKinesisVideoStreamPoolRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMediaPipelineKinesisVideoStreamPoolRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMediaPipelineRequest:
    boto3_raw_data: "type_defs.GetMediaPipelineRequestTypeDef" = dataclasses.field()

    MediaPipelineId = field("MediaPipelineId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMediaPipelineRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMediaPipelineRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSpeakerSearchTaskRequest:
    boto3_raw_data: "type_defs.GetSpeakerSearchTaskRequestTypeDef" = dataclasses.field()

    Identifier = field("Identifier")
    SpeakerSearchTaskId = field("SpeakerSearchTaskId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSpeakerSearchTaskRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSpeakerSearchTaskRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SpeakerSearchTask:
    boto3_raw_data: "type_defs.SpeakerSearchTaskTypeDef" = dataclasses.field()

    SpeakerSearchTaskId = field("SpeakerSearchTaskId")
    SpeakerSearchTaskStatus = field("SpeakerSearchTaskStatus")
    CreatedTimestamp = field("CreatedTimestamp")
    UpdatedTimestamp = field("UpdatedTimestamp")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SpeakerSearchTaskTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SpeakerSearchTaskTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetVoiceToneAnalysisTaskRequest:
    boto3_raw_data: "type_defs.GetVoiceToneAnalysisTaskRequestTypeDef" = (
        dataclasses.field()
    )

    Identifier = field("Identifier")
    VoiceToneAnalysisTaskId = field("VoiceToneAnalysisTaskId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetVoiceToneAnalysisTaskRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetVoiceToneAnalysisTaskRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VoiceToneAnalysisTask:
    boto3_raw_data: "type_defs.VoiceToneAnalysisTaskTypeDef" = dataclasses.field()

    VoiceToneAnalysisTaskId = field("VoiceToneAnalysisTaskId")
    VoiceToneAnalysisTaskStatus = field("VoiceToneAnalysisTaskStatus")
    CreatedTimestamp = field("CreatedTimestamp")
    UpdatedTimestamp = field("UpdatedTimestamp")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VoiceToneAnalysisTaskTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VoiceToneAnalysisTaskTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HorizontalLayoutConfiguration:
    boto3_raw_data: "type_defs.HorizontalLayoutConfigurationTypeDef" = (
        dataclasses.field()
    )

    TileOrder = field("TileOrder")
    TilePosition = field("TilePosition")
    TileCount = field("TileCount")
    TileAspectRatio = field("TileAspectRatio")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.HorizontalLayoutConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HorizontalLayoutConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PresenterOnlyConfiguration:
    boto3_raw_data: "type_defs.PresenterOnlyConfigurationTypeDef" = dataclasses.field()

    PresenterPosition = field("PresenterPosition")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PresenterOnlyConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PresenterOnlyConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VerticalLayoutConfiguration:
    boto3_raw_data: "type_defs.VerticalLayoutConfigurationTypeDef" = dataclasses.field()

    TileOrder = field("TileOrder")
    TilePosition = field("TilePosition")
    TileCount = field("TileCount")
    TileAspectRatio = field("TileAspectRatio")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VerticalLayoutConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VerticalLayoutConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VideoAttribute:
    boto3_raw_data: "type_defs.VideoAttributeTypeDef" = dataclasses.field()

    CornerRadius = field("CornerRadius")
    BorderColor = field("BorderColor")
    HighlightColor = field("HighlightColor")
    BorderThickness = field("BorderThickness")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VideoAttributeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VideoAttributeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IssueDetectionConfiguration:
    boto3_raw_data: "type_defs.IssueDetectionConfigurationTypeDef" = dataclasses.field()

    RuleName = field("RuleName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IssueDetectionConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IssueDetectionConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KeywordMatchConfigurationOutput:
    boto3_raw_data: "type_defs.KeywordMatchConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    RuleName = field("RuleName")
    Keywords = field("Keywords")
    Negate = field("Negate")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.KeywordMatchConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KeywordMatchConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KeywordMatchConfiguration:
    boto3_raw_data: "type_defs.KeywordMatchConfigurationTypeDef" = dataclasses.field()

    RuleName = field("RuleName")
    Keywords = field("Keywords")
    Negate = field("Negate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KeywordMatchConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KeywordMatchConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KinesisDataStreamSinkConfiguration:
    boto3_raw_data: "type_defs.KinesisDataStreamSinkConfigurationTypeDef" = (
        dataclasses.field()
    )

    InsightsTarget = field("InsightsTarget")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.KinesisDataStreamSinkConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KinesisDataStreamSinkConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KinesisVideoStreamConfigurationUpdate:
    boto3_raw_data: "type_defs.KinesisVideoStreamConfigurationUpdateTypeDef" = (
        dataclasses.field()
    )

    DataRetentionInHours = field("DataRetentionInHours")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.KinesisVideoStreamConfigurationUpdateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KinesisVideoStreamConfigurationUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KinesisVideoStreamPoolSummary:
    boto3_raw_data: "type_defs.KinesisVideoStreamPoolSummaryTypeDef" = (
        dataclasses.field()
    )

    PoolName = field("PoolName")
    PoolId = field("PoolId")
    PoolArn = field("PoolArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.KinesisVideoStreamPoolSummaryTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KinesisVideoStreamPoolSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecordingStreamConfiguration:
    boto3_raw_data: "type_defs.RecordingStreamConfigurationTypeDef" = (
        dataclasses.field()
    )

    StreamArn = field("StreamArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RecordingStreamConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecordingStreamConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KinesisVideoStreamSourceTaskConfiguration:
    boto3_raw_data: "type_defs.KinesisVideoStreamSourceTaskConfigurationTypeDef" = (
        dataclasses.field()
    )

    StreamArn = field("StreamArn")
    ChannelId = field("ChannelId")
    FragmentNumber = field("FragmentNumber")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.KinesisVideoStreamSourceTaskConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KinesisVideoStreamSourceTaskConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LambdaFunctionSinkConfiguration:
    boto3_raw_data: "type_defs.LambdaFunctionSinkConfigurationTypeDef" = (
        dataclasses.field()
    )

    InsightsTarget = field("InsightsTarget")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.LambdaFunctionSinkConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LambdaFunctionSinkConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMediaCapturePipelinesRequest:
    boto3_raw_data: "type_defs.ListMediaCapturePipelinesRequestTypeDef" = (
        dataclasses.field()
    )

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListMediaCapturePipelinesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMediaCapturePipelinesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MediaCapturePipelineSummary:
    boto3_raw_data: "type_defs.MediaCapturePipelineSummaryTypeDef" = dataclasses.field()

    MediaPipelineId = field("MediaPipelineId")
    MediaPipelineArn = field("MediaPipelineArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MediaCapturePipelineSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MediaCapturePipelineSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMediaInsightsPipelineConfigurationsRequest:
    boto3_raw_data: (
        "type_defs.ListMediaInsightsPipelineConfigurationsRequestTypeDef"
    ) = dataclasses.field()

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListMediaInsightsPipelineConfigurationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.ListMediaInsightsPipelineConfigurationsRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MediaInsightsPipelineConfigurationSummary:
    boto3_raw_data: "type_defs.MediaInsightsPipelineConfigurationSummaryTypeDef" = (
        dataclasses.field()
    )

    MediaInsightsPipelineConfigurationName = field(
        "MediaInsightsPipelineConfigurationName"
    )
    MediaInsightsPipelineConfigurationId = field("MediaInsightsPipelineConfigurationId")
    MediaInsightsPipelineConfigurationArn = field(
        "MediaInsightsPipelineConfigurationArn"
    )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MediaInsightsPipelineConfigurationSummaryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MediaInsightsPipelineConfigurationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMediaPipelineKinesisVideoStreamPoolsRequest:
    boto3_raw_data: (
        "type_defs.ListMediaPipelineKinesisVideoStreamPoolsRequestTypeDef"
    ) = dataclasses.field()

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListMediaPipelineKinesisVideoStreamPoolsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.ListMediaPipelineKinesisVideoStreamPoolsRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMediaPipelinesRequest:
    boto3_raw_data: "type_defs.ListMediaPipelinesRequestTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMediaPipelinesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMediaPipelinesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MediaPipelineSummary:
    boto3_raw_data: "type_defs.MediaPipelineSummaryTypeDef" = dataclasses.field()

    MediaPipelineId = field("MediaPipelineId")
    MediaPipelineArn = field("MediaPipelineArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MediaPipelineSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MediaPipelineSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceRequest:
    boto3_raw_data: "type_defs.ListTagsForResourceRequestTypeDef" = dataclasses.field()

    ResourceARN = field("ResourceARN")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForResourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LiveConnectorRTMPConfiguration:
    boto3_raw_data: "type_defs.LiveConnectorRTMPConfigurationTypeDef" = (
        dataclasses.field()
    )

    Url = field("Url")
    AudioChannels = field("AudioChannels")
    AudioSampleRate = field("AudioSampleRate")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.LiveConnectorRTMPConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LiveConnectorRTMPConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3RecordingSinkConfiguration:
    boto3_raw_data: "type_defs.S3RecordingSinkConfigurationTypeDef" = (
        dataclasses.field()
    )

    Destination = field("Destination")
    RecordingFileFormat = field("RecordingFileFormat")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3RecordingSinkConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3RecordingSinkConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SnsTopicSinkConfiguration:
    boto3_raw_data: "type_defs.SnsTopicSinkConfigurationTypeDef" = dataclasses.field()

    InsightsTarget = field("InsightsTarget")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SnsTopicSinkConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SnsTopicSinkConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SqsQueueSinkConfiguration:
    boto3_raw_data: "type_defs.SqsQueueSinkConfigurationTypeDef" = dataclasses.field()

    InsightsTarget = field("InsightsTarget")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SqsQueueSinkConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SqsQueueSinkConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VoiceAnalyticsProcessorConfiguration:
    boto3_raw_data: "type_defs.VoiceAnalyticsProcessorConfigurationTypeDef" = (
        dataclasses.field()
    )

    SpeakerSearchStatus = field("SpeakerSearchStatus")
    VoiceToneAnalysisStatus = field("VoiceToneAnalysisStatus")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.VoiceAnalyticsProcessorConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VoiceAnalyticsProcessorConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VoiceEnhancementSinkConfiguration:
    boto3_raw_data: "type_defs.VoiceEnhancementSinkConfigurationTypeDef" = (
        dataclasses.field()
    )

    Disabled = field("Disabled")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.VoiceEnhancementSinkConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VoiceEnhancementSinkConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MediaInsightsPipelineElementStatus:
    boto3_raw_data: "type_defs.MediaInsightsPipelineElementStatusTypeDef" = (
        dataclasses.field()
    )

    Type = field("Type")
    Status = field("Status")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MediaInsightsPipelineElementStatusTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MediaInsightsPipelineElementStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SentimentConfiguration:
    boto3_raw_data: "type_defs.SentimentConfigurationTypeDef" = dataclasses.field()

    RuleName = field("RuleName")
    SentimentType = field("SentimentType")
    TimePeriod = field("TimePeriod")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SentimentConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SentimentConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SelectedVideoStreamsOutput:
    boto3_raw_data: "type_defs.SelectedVideoStreamsOutputTypeDef" = dataclasses.field()

    AttendeeIds = field("AttendeeIds")
    ExternalUserIds = field("ExternalUserIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SelectedVideoStreamsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SelectedVideoStreamsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SelectedVideoStreams:
    boto3_raw_data: "type_defs.SelectedVideoStreamsTypeDef" = dataclasses.field()

    AttendeeIds = field("AttendeeIds")
    ExternalUserIds = field("ExternalUserIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SelectedVideoStreamsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SelectedVideoStreamsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopSpeakerSearchTaskRequest:
    boto3_raw_data: "type_defs.StopSpeakerSearchTaskRequestTypeDef" = (
        dataclasses.field()
    )

    Identifier = field("Identifier")
    SpeakerSearchTaskId = field("SpeakerSearchTaskId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopSpeakerSearchTaskRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopSpeakerSearchTaskRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopVoiceToneAnalysisTaskRequest:
    boto3_raw_data: "type_defs.StopVoiceToneAnalysisTaskRequestTypeDef" = (
        dataclasses.field()
    )

    Identifier = field("Identifier")
    VoiceToneAnalysisTaskId = field("VoiceToneAnalysisTaskId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StopVoiceToneAnalysisTaskRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopVoiceToneAnalysisTaskRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UntagResourceRequest:
    boto3_raw_data: "type_defs.UntagResourceRequestTypeDef" = dataclasses.field()

    ResourceARN = field("ResourceARN")
    TagKeys = field("TagKeys")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UntagResourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UntagResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateMediaInsightsPipelineStatusRequest:
    boto3_raw_data: "type_defs.UpdateMediaInsightsPipelineStatusRequestTypeDef" = (
        dataclasses.field()
    )

    Identifier = field("Identifier")
    UpdateStatus = field("UpdateStatus")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateMediaInsightsPipelineStatusRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateMediaInsightsPipelineStatusRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AmazonTranscribeCallAnalyticsProcessorConfigurationOutput:
    boto3_raw_data: (
        "type_defs.AmazonTranscribeCallAnalyticsProcessorConfigurationOutputTypeDef"
    ) = dataclasses.field()

    LanguageCode = field("LanguageCode")
    VocabularyName = field("VocabularyName")
    VocabularyFilterName = field("VocabularyFilterName")
    VocabularyFilterMethod = field("VocabularyFilterMethod")
    LanguageModelName = field("LanguageModelName")
    EnablePartialResultsStabilization = field("EnablePartialResultsStabilization")
    PartialResultsStability = field("PartialResultsStability")
    ContentIdentificationType = field("ContentIdentificationType")
    ContentRedactionType = field("ContentRedactionType")
    PiiEntityTypes = field("PiiEntityTypes")
    FilterPartialResults = field("FilterPartialResults")

    @cached_property
    def PostCallAnalyticsSettings(self):  # pragma: no cover
        return PostCallAnalyticsSettings.make_one(
            self.boto3_raw_data["PostCallAnalyticsSettings"]
        )

    CallAnalyticsStreamCategories = field("CallAnalyticsStreamCategories")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AmazonTranscribeCallAnalyticsProcessorConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.AmazonTranscribeCallAnalyticsProcessorConfigurationOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AmazonTranscribeCallAnalyticsProcessorConfiguration:
    boto3_raw_data: (
        "type_defs.AmazonTranscribeCallAnalyticsProcessorConfigurationTypeDef"
    ) = dataclasses.field()

    LanguageCode = field("LanguageCode")
    VocabularyName = field("VocabularyName")
    VocabularyFilterName = field("VocabularyFilterName")
    VocabularyFilterMethod = field("VocabularyFilterMethod")
    LanguageModelName = field("LanguageModelName")
    EnablePartialResultsStabilization = field("EnablePartialResultsStabilization")
    PartialResultsStability = field("PartialResultsStability")
    ContentIdentificationType = field("ContentIdentificationType")
    ContentRedactionType = field("ContentRedactionType")
    PiiEntityTypes = field("PiiEntityTypes")
    FilterPartialResults = field("FilterPartialResults")

    @cached_property
    def PostCallAnalyticsSettings(self):  # pragma: no cover
        return PostCallAnalyticsSettings.make_one(
            self.boto3_raw_data["PostCallAnalyticsSettings"]
        )

    CallAnalyticsStreamCategories = field("CallAnalyticsStreamCategories")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AmazonTranscribeCallAnalyticsProcessorConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.AmazonTranscribeCallAnalyticsProcessorConfigurationTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ArtifactsConcatenationConfiguration:
    boto3_raw_data: "type_defs.ArtifactsConcatenationConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Audio(self):  # pragma: no cover
        return AudioConcatenationConfiguration.make_one(self.boto3_raw_data["Audio"])

    @cached_property
    def Video(self):  # pragma: no cover
        return VideoConcatenationConfiguration.make_one(self.boto3_raw_data["Video"])

    @cached_property
    def Content(self):  # pragma: no cover
        return ContentConcatenationConfiguration.make_one(
            self.boto3_raw_data["Content"]
        )

    @cached_property
    def DataChannel(self):  # pragma: no cover
        return DataChannelConcatenationConfiguration.make_one(
            self.boto3_raw_data["DataChannel"]
        )

    @cached_property
    def TranscriptionMessages(self):  # pragma: no cover
        return TranscriptionMessagesConcatenationConfiguration.make_one(
            self.boto3_raw_data["TranscriptionMessages"]
        )

    @cached_property
    def MeetingEvents(self):  # pragma: no cover
        return MeetingEventsConcatenationConfiguration.make_one(
            self.boto3_raw_data["MeetingEvents"]
        )

    @cached_property
    def CompositedVideo(self):  # pragma: no cover
        return CompositedVideoConcatenationConfiguration.make_one(
            self.boto3_raw_data["CompositedVideo"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ArtifactsConcatenationConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ArtifactsConcatenationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StreamChannelDefinitionOutput:
    boto3_raw_data: "type_defs.StreamChannelDefinitionOutputTypeDef" = (
        dataclasses.field()
    )

    NumberOfChannels = field("NumberOfChannels")

    @cached_property
    def ChannelDefinitions(self):  # pragma: no cover
        return ChannelDefinition.make_many(self.boto3_raw_data["ChannelDefinitions"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StreamChannelDefinitionOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StreamChannelDefinitionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StreamChannelDefinition:
    boto3_raw_data: "type_defs.StreamChannelDefinitionTypeDef" = dataclasses.field()

    NumberOfChannels = field("NumberOfChannels")

    @cached_property
    def ChannelDefinitions(self):  # pragma: no cover
        return ChannelDefinition.make_many(self.boto3_raw_data["ChannelDefinitions"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StreamChannelDefinitionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StreamChannelDefinitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConcatenationSink:
    boto3_raw_data: "type_defs.ConcatenationSinkTypeDef" = dataclasses.field()

    Type = field("Type")

    @cached_property
    def S3BucketSinkConfiguration(self):  # pragma: no cover
        return S3BucketSinkConfiguration.make_one(
            self.boto3_raw_data["S3BucketSinkConfiguration"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConcatenationSinkTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConcatenationSinkTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagResourceRequest:
    boto3_raw_data: "type_defs.TagResourceRequestTypeDef" = dataclasses.field()

    ResourceARN = field("ResourceARN")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TagResourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TagResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EmptyResponseMetadata:
    boto3_raw_data: "type_defs.EmptyResponseMetadataTypeDef" = dataclasses.field()

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EmptyResponseMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EmptyResponseMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceResponse:
    boto3_raw_data: "type_defs.ListTagsForResourceResponseTypeDef" = dataclasses.field()

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForResourceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMediaPipelineKinesisVideoStreamPoolRequest:
    boto3_raw_data: (
        "type_defs.CreateMediaPipelineKinesisVideoStreamPoolRequestTypeDef"
    ) = dataclasses.field()

    @cached_property
    def StreamConfiguration(self):  # pragma: no cover
        return KinesisVideoStreamConfiguration.make_one(
            self.boto3_raw_data["StreamConfiguration"]
        )

    PoolName = field("PoolName")
    ClientRequestToken = field("ClientRequestToken")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateMediaPipelineKinesisVideoStreamPoolRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.CreateMediaPipelineKinesisVideoStreamPoolRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KinesisVideoStreamPoolConfiguration:
    boto3_raw_data: "type_defs.KinesisVideoStreamPoolConfigurationTypeDef" = (
        dataclasses.field()
    )

    PoolArn = field("PoolArn")
    PoolName = field("PoolName")
    PoolId = field("PoolId")
    PoolStatus = field("PoolStatus")
    PoolSize = field("PoolSize")

    @cached_property
    def StreamConfiguration(self):  # pragma: no cover
        return KinesisVideoStreamConfiguration.make_one(
            self.boto3_raw_data["StreamConfiguration"]
        )

    CreatedTimestamp = field("CreatedTimestamp")
    UpdatedTimestamp = field("UpdatedTimestamp")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.KinesisVideoStreamPoolConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KinesisVideoStreamPoolConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMediaStreamPipelineRequest:
    boto3_raw_data: "type_defs.CreateMediaStreamPipelineRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Sources(self):  # pragma: no cover
        return MediaStreamSource.make_many(self.boto3_raw_data["Sources"])

    @cached_property
    def Sinks(self):  # pragma: no cover
        return MediaStreamSink.make_many(self.boto3_raw_data["Sinks"])

    ClientRequestToken = field("ClientRequestToken")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateMediaStreamPipelineRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMediaStreamPipelineRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MediaStreamPipeline:
    boto3_raw_data: "type_defs.MediaStreamPipelineTypeDef" = dataclasses.field()

    MediaPipelineId = field("MediaPipelineId")
    MediaPipelineArn = field("MediaPipelineArn")
    CreatedTimestamp = field("CreatedTimestamp")
    UpdatedTimestamp = field("UpdatedTimestamp")
    Status = field("Status")

    @cached_property
    def Sources(self):  # pragma: no cover
        return MediaStreamSource.make_many(self.boto3_raw_data["Sources"])

    @cached_property
    def Sinks(self):  # pragma: no cover
        return MediaStreamSink.make_many(self.boto3_raw_data["Sinks"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MediaStreamPipelineTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MediaStreamPipelineTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FragmentSelectorOutput:
    boto3_raw_data: "type_defs.FragmentSelectorOutputTypeDef" = dataclasses.field()

    FragmentSelectorType = field("FragmentSelectorType")

    @cached_property
    def TimestampRange(self):  # pragma: no cover
        return TimestampRangeOutput.make_one(self.boto3_raw_data["TimestampRange"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FragmentSelectorOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FragmentSelectorOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSpeakerSearchTaskResponse:
    boto3_raw_data: "type_defs.GetSpeakerSearchTaskResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def SpeakerSearchTask(self):  # pragma: no cover
        return SpeakerSearchTask.make_one(self.boto3_raw_data["SpeakerSearchTask"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSpeakerSearchTaskResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSpeakerSearchTaskResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartSpeakerSearchTaskResponse:
    boto3_raw_data: "type_defs.StartSpeakerSearchTaskResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def SpeakerSearchTask(self):  # pragma: no cover
        return SpeakerSearchTask.make_one(self.boto3_raw_data["SpeakerSearchTask"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartSpeakerSearchTaskResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartSpeakerSearchTaskResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetVoiceToneAnalysisTaskResponse:
    boto3_raw_data: "type_defs.GetVoiceToneAnalysisTaskResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def VoiceToneAnalysisTask(self):  # pragma: no cover
        return VoiceToneAnalysisTask.make_one(
            self.boto3_raw_data["VoiceToneAnalysisTask"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetVoiceToneAnalysisTaskResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetVoiceToneAnalysisTaskResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartVoiceToneAnalysisTaskResponse:
    boto3_raw_data: "type_defs.StartVoiceToneAnalysisTaskResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def VoiceToneAnalysisTask(self):  # pragma: no cover
        return VoiceToneAnalysisTask.make_one(
            self.boto3_raw_data["VoiceToneAnalysisTask"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartVoiceToneAnalysisTaskResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartVoiceToneAnalysisTaskResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GridViewConfiguration:
    boto3_raw_data: "type_defs.GridViewConfigurationTypeDef" = dataclasses.field()

    ContentShareLayout = field("ContentShareLayout")

    @cached_property
    def PresenterOnlyConfiguration(self):  # pragma: no cover
        return PresenterOnlyConfiguration.make_one(
            self.boto3_raw_data["PresenterOnlyConfiguration"]
        )

    @cached_property
    def ActiveSpeakerOnlyConfiguration(self):  # pragma: no cover
        return ActiveSpeakerOnlyConfiguration.make_one(
            self.boto3_raw_data["ActiveSpeakerOnlyConfiguration"]
        )

    @cached_property
    def HorizontalLayoutConfiguration(self):  # pragma: no cover
        return HorizontalLayoutConfiguration.make_one(
            self.boto3_raw_data["HorizontalLayoutConfiguration"]
        )

    @cached_property
    def VerticalLayoutConfiguration(self):  # pragma: no cover
        return VerticalLayoutConfiguration.make_one(
            self.boto3_raw_data["VerticalLayoutConfiguration"]
        )

    @cached_property
    def VideoAttribute(self):  # pragma: no cover
        return VideoAttribute.make_one(self.boto3_raw_data["VideoAttribute"])

    CanvasOrientation = field("CanvasOrientation")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GridViewConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GridViewConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateMediaPipelineKinesisVideoStreamPoolRequest:
    boto3_raw_data: (
        "type_defs.UpdateMediaPipelineKinesisVideoStreamPoolRequestTypeDef"
    ) = dataclasses.field()

    Identifier = field("Identifier")

    @cached_property
    def StreamConfiguration(self):  # pragma: no cover
        return KinesisVideoStreamConfigurationUpdate.make_one(
            self.boto3_raw_data["StreamConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateMediaPipelineKinesisVideoStreamPoolRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.UpdateMediaPipelineKinesisVideoStreamPoolRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMediaPipelineKinesisVideoStreamPoolsResponse:
    boto3_raw_data: (
        "type_defs.ListMediaPipelineKinesisVideoStreamPoolsResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def KinesisVideoStreamPools(self):  # pragma: no cover
        return KinesisVideoStreamPoolSummary.make_many(
            self.boto3_raw_data["KinesisVideoStreamPools"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListMediaPipelineKinesisVideoStreamPoolsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.ListMediaPipelineKinesisVideoStreamPoolsResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartSpeakerSearchTaskRequest:
    boto3_raw_data: "type_defs.StartSpeakerSearchTaskRequestTypeDef" = (
        dataclasses.field()
    )

    Identifier = field("Identifier")
    VoiceProfileDomainArn = field("VoiceProfileDomainArn")

    @cached_property
    def KinesisVideoStreamSourceTaskConfiguration(self):  # pragma: no cover
        return KinesisVideoStreamSourceTaskConfiguration.make_one(
            self.boto3_raw_data["KinesisVideoStreamSourceTaskConfiguration"]
        )

    ClientRequestToken = field("ClientRequestToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartSpeakerSearchTaskRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartSpeakerSearchTaskRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartVoiceToneAnalysisTaskRequest:
    boto3_raw_data: "type_defs.StartVoiceToneAnalysisTaskRequestTypeDef" = (
        dataclasses.field()
    )

    Identifier = field("Identifier")
    LanguageCode = field("LanguageCode")

    @cached_property
    def KinesisVideoStreamSourceTaskConfiguration(self):  # pragma: no cover
        return KinesisVideoStreamSourceTaskConfiguration.make_one(
            self.boto3_raw_data["KinesisVideoStreamSourceTaskConfiguration"]
        )

    ClientRequestToken = field("ClientRequestToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartVoiceToneAnalysisTaskRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartVoiceToneAnalysisTaskRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMediaCapturePipelinesResponse:
    boto3_raw_data: "type_defs.ListMediaCapturePipelinesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def MediaCapturePipelines(self):  # pragma: no cover
        return MediaCapturePipelineSummary.make_many(
            self.boto3_raw_data["MediaCapturePipelines"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListMediaCapturePipelinesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMediaCapturePipelinesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMediaInsightsPipelineConfigurationsResponse:
    boto3_raw_data: (
        "type_defs.ListMediaInsightsPipelineConfigurationsResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def MediaInsightsPipelineConfigurations(self):  # pragma: no cover
        return MediaInsightsPipelineConfigurationSummary.make_many(
            self.boto3_raw_data["MediaInsightsPipelineConfigurations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListMediaInsightsPipelineConfigurationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.ListMediaInsightsPipelineConfigurationsResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMediaPipelinesResponse:
    boto3_raw_data: "type_defs.ListMediaPipelinesResponseTypeDef" = dataclasses.field()

    @cached_property
    def MediaPipelines(self):  # pragma: no cover
        return MediaPipelineSummary.make_many(self.boto3_raw_data["MediaPipelines"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMediaPipelinesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMediaPipelinesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LiveConnectorSinkConfiguration:
    boto3_raw_data: "type_defs.LiveConnectorSinkConfigurationTypeDef" = (
        dataclasses.field()
    )

    SinkType = field("SinkType")

    @cached_property
    def RTMPConfiguration(self):  # pragma: no cover
        return LiveConnectorRTMPConfiguration.make_one(
            self.boto3_raw_data["RTMPConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.LiveConnectorSinkConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LiveConnectorSinkConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RealTimeAlertRuleOutput:
    boto3_raw_data: "type_defs.RealTimeAlertRuleOutputTypeDef" = dataclasses.field()

    Type = field("Type")

    @cached_property
    def KeywordMatchConfiguration(self):  # pragma: no cover
        return KeywordMatchConfigurationOutput.make_one(
            self.boto3_raw_data["KeywordMatchConfiguration"]
        )

    @cached_property
    def SentimentConfiguration(self):  # pragma: no cover
        return SentimentConfiguration.make_one(
            self.boto3_raw_data["SentimentConfiguration"]
        )

    @cached_property
    def IssueDetectionConfiguration(self):  # pragma: no cover
        return IssueDetectionConfiguration.make_one(
            self.boto3_raw_data["IssueDetectionConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RealTimeAlertRuleOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RealTimeAlertRuleOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RealTimeAlertRule:
    boto3_raw_data: "type_defs.RealTimeAlertRuleTypeDef" = dataclasses.field()

    Type = field("Type")

    @cached_property
    def KeywordMatchConfiguration(self):  # pragma: no cover
        return KeywordMatchConfiguration.make_one(
            self.boto3_raw_data["KeywordMatchConfiguration"]
        )

    @cached_property
    def SentimentConfiguration(self):  # pragma: no cover
        return SentimentConfiguration.make_one(
            self.boto3_raw_data["SentimentConfiguration"]
        )

    @cached_property
    def IssueDetectionConfiguration(self):  # pragma: no cover
        return IssueDetectionConfiguration.make_one(
            self.boto3_raw_data["IssueDetectionConfiguration"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RealTimeAlertRuleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RealTimeAlertRuleTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SourceConfigurationOutput:
    boto3_raw_data: "type_defs.SourceConfigurationOutputTypeDef" = dataclasses.field()

    @cached_property
    def SelectedVideoStreams(self):  # pragma: no cover
        return SelectedVideoStreamsOutput.make_one(
            self.boto3_raw_data["SelectedVideoStreams"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SourceConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SourceConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TimestampRange:
    boto3_raw_data: "type_defs.TimestampRangeTypeDef" = dataclasses.field()

    StartTimestamp = field("StartTimestamp")
    EndTimestamp = field("EndTimestamp")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TimestampRangeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TimestampRangeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MediaInsightsPipelineConfigurationElementOutput:
    boto3_raw_data: (
        "type_defs.MediaInsightsPipelineConfigurationElementOutputTypeDef"
    ) = dataclasses.field()

    Type = field("Type")

    @cached_property
    def AmazonTranscribeCallAnalyticsProcessorConfiguration(self):  # pragma: no cover
        return AmazonTranscribeCallAnalyticsProcessorConfigurationOutput.make_one(
            self.boto3_raw_data["AmazonTranscribeCallAnalyticsProcessorConfiguration"]
        )

    @cached_property
    def AmazonTranscribeProcessorConfiguration(self):  # pragma: no cover
        return AmazonTranscribeProcessorConfiguration.make_one(
            self.boto3_raw_data["AmazonTranscribeProcessorConfiguration"]
        )

    @cached_property
    def KinesisDataStreamSinkConfiguration(self):  # pragma: no cover
        return KinesisDataStreamSinkConfiguration.make_one(
            self.boto3_raw_data["KinesisDataStreamSinkConfiguration"]
        )

    @cached_property
    def S3RecordingSinkConfiguration(self):  # pragma: no cover
        return S3RecordingSinkConfiguration.make_one(
            self.boto3_raw_data["S3RecordingSinkConfiguration"]
        )

    @cached_property
    def VoiceAnalyticsProcessorConfiguration(self):  # pragma: no cover
        return VoiceAnalyticsProcessorConfiguration.make_one(
            self.boto3_raw_data["VoiceAnalyticsProcessorConfiguration"]
        )

    @cached_property
    def LambdaFunctionSinkConfiguration(self):  # pragma: no cover
        return LambdaFunctionSinkConfiguration.make_one(
            self.boto3_raw_data["LambdaFunctionSinkConfiguration"]
        )

    @cached_property
    def SqsQueueSinkConfiguration(self):  # pragma: no cover
        return SqsQueueSinkConfiguration.make_one(
            self.boto3_raw_data["SqsQueueSinkConfiguration"]
        )

    @cached_property
    def SnsTopicSinkConfiguration(self):  # pragma: no cover
        return SnsTopicSinkConfiguration.make_one(
            self.boto3_raw_data["SnsTopicSinkConfiguration"]
        )

    @cached_property
    def VoiceEnhancementSinkConfiguration(self):  # pragma: no cover
        return VoiceEnhancementSinkConfiguration.make_one(
            self.boto3_raw_data["VoiceEnhancementSinkConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MediaInsightsPipelineConfigurationElementOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.MediaInsightsPipelineConfigurationElementOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChimeSdkMeetingConcatenationConfiguration:
    boto3_raw_data: "type_defs.ChimeSdkMeetingConcatenationConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ArtifactsConfiguration(self):  # pragma: no cover
        return ArtifactsConcatenationConfiguration.make_one(
            self.boto3_raw_data["ArtifactsConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ChimeSdkMeetingConcatenationConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ChimeSdkMeetingConcatenationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StreamConfigurationOutput:
    boto3_raw_data: "type_defs.StreamConfigurationOutputTypeDef" = dataclasses.field()

    StreamArn = field("StreamArn")

    @cached_property
    def StreamChannelDefinition(self):  # pragma: no cover
        return StreamChannelDefinitionOutput.make_one(
            self.boto3_raw_data["StreamChannelDefinition"]
        )

    FragmentNumber = field("FragmentNumber")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StreamConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StreamConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StreamConfiguration:
    boto3_raw_data: "type_defs.StreamConfigurationTypeDef" = dataclasses.field()

    StreamArn = field("StreamArn")

    @cached_property
    def StreamChannelDefinition(self):  # pragma: no cover
        return StreamChannelDefinition.make_one(
            self.boto3_raw_data["StreamChannelDefinition"]
        )

    FragmentNumber = field("FragmentNumber")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StreamConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StreamConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMediaPipelineKinesisVideoStreamPoolResponse:
    boto3_raw_data: (
        "type_defs.CreateMediaPipelineKinesisVideoStreamPoolResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def KinesisVideoStreamPoolConfiguration(self):  # pragma: no cover
        return KinesisVideoStreamPoolConfiguration.make_one(
            self.boto3_raw_data["KinesisVideoStreamPoolConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateMediaPipelineKinesisVideoStreamPoolResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.CreateMediaPipelineKinesisVideoStreamPoolResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMediaPipelineKinesisVideoStreamPoolResponse:
    boto3_raw_data: (
        "type_defs.GetMediaPipelineKinesisVideoStreamPoolResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def KinesisVideoStreamPoolConfiguration(self):  # pragma: no cover
        return KinesisVideoStreamPoolConfiguration.make_one(
            self.boto3_raw_data["KinesisVideoStreamPoolConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetMediaPipelineKinesisVideoStreamPoolResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.GetMediaPipelineKinesisVideoStreamPoolResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateMediaPipelineKinesisVideoStreamPoolResponse:
    boto3_raw_data: (
        "type_defs.UpdateMediaPipelineKinesisVideoStreamPoolResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def KinesisVideoStreamPoolConfiguration(self):  # pragma: no cover
        return KinesisVideoStreamPoolConfiguration.make_one(
            self.boto3_raw_data["KinesisVideoStreamPoolConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateMediaPipelineKinesisVideoStreamPoolResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.UpdateMediaPipelineKinesisVideoStreamPoolResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMediaStreamPipelineResponse:
    boto3_raw_data: "type_defs.CreateMediaStreamPipelineResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def MediaStreamPipeline(self):  # pragma: no cover
        return MediaStreamPipeline.make_one(self.boto3_raw_data["MediaStreamPipeline"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateMediaStreamPipelineResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMediaStreamPipelineResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KinesisVideoStreamRecordingSourceRuntimeConfigurationOutput:
    boto3_raw_data: (
        "type_defs.KinesisVideoStreamRecordingSourceRuntimeConfigurationOutputTypeDef"
    ) = dataclasses.field()

    @cached_property
    def Streams(self):  # pragma: no cover
        return RecordingStreamConfiguration.make_many(self.boto3_raw_data["Streams"])

    @cached_property
    def FragmentSelector(self):  # pragma: no cover
        return FragmentSelectorOutput.make_one(self.boto3_raw_data["FragmentSelector"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.KinesisVideoStreamRecordingSourceRuntimeConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.KinesisVideoStreamRecordingSourceRuntimeConfigurationOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CompositedVideoArtifactsConfiguration:
    boto3_raw_data: "type_defs.CompositedVideoArtifactsConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def GridViewConfiguration(self):  # pragma: no cover
        return GridViewConfiguration.make_one(
            self.boto3_raw_data["GridViewConfiguration"]
        )

    Layout = field("Layout")
    Resolution = field("Resolution")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CompositedVideoArtifactsConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CompositedVideoArtifactsConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RealTimeAlertConfigurationOutput:
    boto3_raw_data: "type_defs.RealTimeAlertConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    Disabled = field("Disabled")

    @cached_property
    def Rules(self):  # pragma: no cover
        return RealTimeAlertRuleOutput.make_many(self.boto3_raw_data["Rules"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RealTimeAlertConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RealTimeAlertConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RealTimeAlertConfiguration:
    boto3_raw_data: "type_defs.RealTimeAlertConfigurationTypeDef" = dataclasses.field()

    Disabled = field("Disabled")

    @cached_property
    def Rules(self):  # pragma: no cover
        return RealTimeAlertRule.make_many(self.boto3_raw_data["Rules"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RealTimeAlertConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RealTimeAlertConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SourceConfiguration:
    boto3_raw_data: "type_defs.SourceConfigurationTypeDef" = dataclasses.field()

    SelectedVideoStreams = field("SelectedVideoStreams")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SourceConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SourceConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FragmentSelector:
    boto3_raw_data: "type_defs.FragmentSelectorTypeDef" = dataclasses.field()

    FragmentSelectorType = field("FragmentSelectorType")

    @cached_property
    def TimestampRange(self):  # pragma: no cover
        return TimestampRange.make_one(self.boto3_raw_data["TimestampRange"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FragmentSelectorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FragmentSelectorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MediaInsightsPipelineConfigurationElement:
    boto3_raw_data: "type_defs.MediaInsightsPipelineConfigurationElementTypeDef" = (
        dataclasses.field()
    )

    Type = field("Type")
    AmazonTranscribeCallAnalyticsProcessorConfiguration = field(
        "AmazonTranscribeCallAnalyticsProcessorConfiguration"
    )

    @cached_property
    def AmazonTranscribeProcessorConfiguration(self):  # pragma: no cover
        return AmazonTranscribeProcessorConfiguration.make_one(
            self.boto3_raw_data["AmazonTranscribeProcessorConfiguration"]
        )

    @cached_property
    def KinesisDataStreamSinkConfiguration(self):  # pragma: no cover
        return KinesisDataStreamSinkConfiguration.make_one(
            self.boto3_raw_data["KinesisDataStreamSinkConfiguration"]
        )

    @cached_property
    def S3RecordingSinkConfiguration(self):  # pragma: no cover
        return S3RecordingSinkConfiguration.make_one(
            self.boto3_raw_data["S3RecordingSinkConfiguration"]
        )

    @cached_property
    def VoiceAnalyticsProcessorConfiguration(self):  # pragma: no cover
        return VoiceAnalyticsProcessorConfiguration.make_one(
            self.boto3_raw_data["VoiceAnalyticsProcessorConfiguration"]
        )

    @cached_property
    def LambdaFunctionSinkConfiguration(self):  # pragma: no cover
        return LambdaFunctionSinkConfiguration.make_one(
            self.boto3_raw_data["LambdaFunctionSinkConfiguration"]
        )

    @cached_property
    def SqsQueueSinkConfiguration(self):  # pragma: no cover
        return SqsQueueSinkConfiguration.make_one(
            self.boto3_raw_data["SqsQueueSinkConfiguration"]
        )

    @cached_property
    def SnsTopicSinkConfiguration(self):  # pragma: no cover
        return SnsTopicSinkConfiguration.make_one(
            self.boto3_raw_data["SnsTopicSinkConfiguration"]
        )

    @cached_property
    def VoiceEnhancementSinkConfiguration(self):  # pragma: no cover
        return VoiceEnhancementSinkConfiguration.make_one(
            self.boto3_raw_data["VoiceEnhancementSinkConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MediaInsightsPipelineConfigurationElementTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MediaInsightsPipelineConfigurationElementTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MediaCapturePipelineSourceConfiguration:
    boto3_raw_data: "type_defs.MediaCapturePipelineSourceConfigurationTypeDef" = (
        dataclasses.field()
    )

    MediaPipelineArn = field("MediaPipelineArn")

    @cached_property
    def ChimeSdkMeetingConfiguration(self):  # pragma: no cover
        return ChimeSdkMeetingConcatenationConfiguration.make_one(
            self.boto3_raw_data["ChimeSdkMeetingConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MediaCapturePipelineSourceConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MediaCapturePipelineSourceConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KinesisVideoStreamSourceRuntimeConfigurationOutput:
    boto3_raw_data: (
        "type_defs.KinesisVideoStreamSourceRuntimeConfigurationOutputTypeDef"
    ) = dataclasses.field()

    @cached_property
    def Streams(self):  # pragma: no cover
        return StreamConfigurationOutput.make_many(self.boto3_raw_data["Streams"])

    MediaEncoding = field("MediaEncoding")
    MediaSampleRate = field("MediaSampleRate")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.KinesisVideoStreamSourceRuntimeConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.KinesisVideoStreamSourceRuntimeConfigurationOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KinesisVideoStreamSourceRuntimeConfiguration:
    boto3_raw_data: "type_defs.KinesisVideoStreamSourceRuntimeConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Streams(self):  # pragma: no cover
        return StreamConfiguration.make_many(self.boto3_raw_data["Streams"])

    MediaEncoding = field("MediaEncoding")
    MediaSampleRate = field("MediaSampleRate")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.KinesisVideoStreamSourceRuntimeConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KinesisVideoStreamSourceRuntimeConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ArtifactsConfiguration:
    boto3_raw_data: "type_defs.ArtifactsConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def Audio(self):  # pragma: no cover
        return AudioArtifactsConfiguration.make_one(self.boto3_raw_data["Audio"])

    @cached_property
    def Video(self):  # pragma: no cover
        return VideoArtifactsConfiguration.make_one(self.boto3_raw_data["Video"])

    @cached_property
    def Content(self):  # pragma: no cover
        return ContentArtifactsConfiguration.make_one(self.boto3_raw_data["Content"])

    @cached_property
    def CompositedVideo(self):  # pragma: no cover
        return CompositedVideoArtifactsConfiguration.make_one(
            self.boto3_raw_data["CompositedVideo"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ArtifactsConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ArtifactsConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChimeSdkMeetingLiveConnectorConfigurationOutput:
    boto3_raw_data: (
        "type_defs.ChimeSdkMeetingLiveConnectorConfigurationOutputTypeDef"
    ) = dataclasses.field()

    Arn = field("Arn")
    MuxType = field("MuxType")

    @cached_property
    def CompositedVideo(self):  # pragma: no cover
        return CompositedVideoArtifactsConfiguration.make_one(
            self.boto3_raw_data["CompositedVideo"]
        )

    @cached_property
    def SourceConfiguration(self):  # pragma: no cover
        return SourceConfigurationOutput.make_one(
            self.boto3_raw_data["SourceConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ChimeSdkMeetingLiveConnectorConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.ChimeSdkMeetingLiveConnectorConfigurationOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MediaInsightsPipelineConfiguration:
    boto3_raw_data: "type_defs.MediaInsightsPipelineConfigurationTypeDef" = (
        dataclasses.field()
    )

    MediaInsightsPipelineConfigurationName = field(
        "MediaInsightsPipelineConfigurationName"
    )
    MediaInsightsPipelineConfigurationArn = field(
        "MediaInsightsPipelineConfigurationArn"
    )
    ResourceAccessRoleArn = field("ResourceAccessRoleArn")

    @cached_property
    def RealTimeAlertConfiguration(self):  # pragma: no cover
        return RealTimeAlertConfigurationOutput.make_one(
            self.boto3_raw_data["RealTimeAlertConfiguration"]
        )

    @cached_property
    def Elements(self):  # pragma: no cover
        return MediaInsightsPipelineConfigurationElementOutput.make_many(
            self.boto3_raw_data["Elements"]
        )

    MediaInsightsPipelineConfigurationId = field("MediaInsightsPipelineConfigurationId")
    CreatedTimestamp = field("CreatedTimestamp")
    UpdatedTimestamp = field("UpdatedTimestamp")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MediaInsightsPipelineConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MediaInsightsPipelineConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KinesisVideoStreamRecordingSourceRuntimeConfiguration:
    boto3_raw_data: (
        "type_defs.KinesisVideoStreamRecordingSourceRuntimeConfigurationTypeDef"
    ) = dataclasses.field()

    @cached_property
    def Streams(self):  # pragma: no cover
        return RecordingStreamConfiguration.make_many(self.boto3_raw_data["Streams"])

    @cached_property
    def FragmentSelector(self):  # pragma: no cover
        return FragmentSelector.make_one(self.boto3_raw_data["FragmentSelector"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.KinesisVideoStreamRecordingSourceRuntimeConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.KinesisVideoStreamRecordingSourceRuntimeConfigurationTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConcatenationSource:
    boto3_raw_data: "type_defs.ConcatenationSourceTypeDef" = dataclasses.field()

    Type = field("Type")

    @cached_property
    def MediaCapturePipelineSourceConfiguration(self):  # pragma: no cover
        return MediaCapturePipelineSourceConfiguration.make_one(
            self.boto3_raw_data["MediaCapturePipelineSourceConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConcatenationSourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConcatenationSourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MediaInsightsPipeline:
    boto3_raw_data: "type_defs.MediaInsightsPipelineTypeDef" = dataclasses.field()

    MediaPipelineId = field("MediaPipelineId")
    MediaPipelineArn = field("MediaPipelineArn")
    MediaInsightsPipelineConfigurationArn = field(
        "MediaInsightsPipelineConfigurationArn"
    )
    Status = field("Status")

    @cached_property
    def KinesisVideoStreamSourceRuntimeConfiguration(self):  # pragma: no cover
        return KinesisVideoStreamSourceRuntimeConfigurationOutput.make_one(
            self.boto3_raw_data["KinesisVideoStreamSourceRuntimeConfiguration"]
        )

    MediaInsightsRuntimeMetadata = field("MediaInsightsRuntimeMetadata")

    @cached_property
    def KinesisVideoStreamRecordingSourceRuntimeConfiguration(self):  # pragma: no cover
        return KinesisVideoStreamRecordingSourceRuntimeConfigurationOutput.make_one(
            self.boto3_raw_data["KinesisVideoStreamRecordingSourceRuntimeConfiguration"]
        )

    @cached_property
    def S3RecordingSinkRuntimeConfiguration(self):  # pragma: no cover
        return S3RecordingSinkRuntimeConfiguration.make_one(
            self.boto3_raw_data["S3RecordingSinkRuntimeConfiguration"]
        )

    CreatedTimestamp = field("CreatedTimestamp")

    @cached_property
    def ElementStatuses(self):  # pragma: no cover
        return MediaInsightsPipelineElementStatus.make_many(
            self.boto3_raw_data["ElementStatuses"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MediaInsightsPipelineTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MediaInsightsPipelineTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChimeSdkMeetingConfigurationOutput:
    boto3_raw_data: "type_defs.ChimeSdkMeetingConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def SourceConfiguration(self):  # pragma: no cover
        return SourceConfigurationOutput.make_one(
            self.boto3_raw_data["SourceConfiguration"]
        )

    @cached_property
    def ArtifactsConfiguration(self):  # pragma: no cover
        return ArtifactsConfiguration.make_one(
            self.boto3_raw_data["ArtifactsConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ChimeSdkMeetingConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ChimeSdkMeetingConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChimeSdkMeetingConfiguration:
    boto3_raw_data: "type_defs.ChimeSdkMeetingConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def SourceConfiguration(self):  # pragma: no cover
        return SourceConfiguration.make_one(self.boto3_raw_data["SourceConfiguration"])

    @cached_property
    def ArtifactsConfiguration(self):  # pragma: no cover
        return ArtifactsConfiguration.make_one(
            self.boto3_raw_data["ArtifactsConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ChimeSdkMeetingConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ChimeSdkMeetingConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LiveConnectorSourceConfigurationOutput:
    boto3_raw_data: "type_defs.LiveConnectorSourceConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    SourceType = field("SourceType")

    @cached_property
    def ChimeSdkMeetingLiveConnectorConfiguration(self):  # pragma: no cover
        return ChimeSdkMeetingLiveConnectorConfigurationOutput.make_one(
            self.boto3_raw_data["ChimeSdkMeetingLiveConnectorConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.LiveConnectorSourceConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LiveConnectorSourceConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMediaInsightsPipelineConfigurationResponse:
    boto3_raw_data: (
        "type_defs.CreateMediaInsightsPipelineConfigurationResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def MediaInsightsPipelineConfiguration(self):  # pragma: no cover
        return MediaInsightsPipelineConfiguration.make_one(
            self.boto3_raw_data["MediaInsightsPipelineConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateMediaInsightsPipelineConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.CreateMediaInsightsPipelineConfigurationResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMediaInsightsPipelineConfigurationResponse:
    boto3_raw_data: "type_defs.GetMediaInsightsPipelineConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def MediaInsightsPipelineConfiguration(self):  # pragma: no cover
        return MediaInsightsPipelineConfiguration.make_one(
            self.boto3_raw_data["MediaInsightsPipelineConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetMediaInsightsPipelineConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMediaInsightsPipelineConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateMediaInsightsPipelineConfigurationResponse:
    boto3_raw_data: (
        "type_defs.UpdateMediaInsightsPipelineConfigurationResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def MediaInsightsPipelineConfiguration(self):  # pragma: no cover
        return MediaInsightsPipelineConfiguration.make_one(
            self.boto3_raw_data["MediaInsightsPipelineConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateMediaInsightsPipelineConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.UpdateMediaInsightsPipelineConfigurationResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChimeSdkMeetingLiveConnectorConfiguration:
    boto3_raw_data: "type_defs.ChimeSdkMeetingLiveConnectorConfigurationTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    MuxType = field("MuxType")

    @cached_property
    def CompositedVideo(self):  # pragma: no cover
        return CompositedVideoArtifactsConfiguration.make_one(
            self.boto3_raw_data["CompositedVideo"]
        )

    SourceConfiguration = field("SourceConfiguration")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ChimeSdkMeetingLiveConnectorConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ChimeSdkMeetingLiveConnectorConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMediaInsightsPipelineConfigurationRequest:
    boto3_raw_data: (
        "type_defs.CreateMediaInsightsPipelineConfigurationRequestTypeDef"
    ) = dataclasses.field()

    MediaInsightsPipelineConfigurationName = field(
        "MediaInsightsPipelineConfigurationName"
    )
    ResourceAccessRoleArn = field("ResourceAccessRoleArn")
    Elements = field("Elements")
    RealTimeAlertConfiguration = field("RealTimeAlertConfiguration")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    ClientRequestToken = field("ClientRequestToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateMediaInsightsPipelineConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.CreateMediaInsightsPipelineConfigurationRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateMediaInsightsPipelineConfigurationRequest:
    boto3_raw_data: (
        "type_defs.UpdateMediaInsightsPipelineConfigurationRequestTypeDef"
    ) = dataclasses.field()

    Identifier = field("Identifier")
    ResourceAccessRoleArn = field("ResourceAccessRoleArn")
    Elements = field("Elements")
    RealTimeAlertConfiguration = field("RealTimeAlertConfiguration")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateMediaInsightsPipelineConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.UpdateMediaInsightsPipelineConfigurationRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMediaConcatenationPipelineRequest:
    boto3_raw_data: "type_defs.CreateMediaConcatenationPipelineRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Sources(self):  # pragma: no cover
        return ConcatenationSource.make_many(self.boto3_raw_data["Sources"])

    @cached_property
    def Sinks(self):  # pragma: no cover
        return ConcatenationSink.make_many(self.boto3_raw_data["Sinks"])

    ClientRequestToken = field("ClientRequestToken")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateMediaConcatenationPipelineRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMediaConcatenationPipelineRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MediaConcatenationPipeline:
    boto3_raw_data: "type_defs.MediaConcatenationPipelineTypeDef" = dataclasses.field()

    MediaPipelineId = field("MediaPipelineId")
    MediaPipelineArn = field("MediaPipelineArn")

    @cached_property
    def Sources(self):  # pragma: no cover
        return ConcatenationSource.make_many(self.boto3_raw_data["Sources"])

    @cached_property
    def Sinks(self):  # pragma: no cover
        return ConcatenationSink.make_many(self.boto3_raw_data["Sinks"])

    Status = field("Status")
    CreatedTimestamp = field("CreatedTimestamp")
    UpdatedTimestamp = field("UpdatedTimestamp")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MediaConcatenationPipelineTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MediaConcatenationPipelineTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMediaInsightsPipelineResponse:
    boto3_raw_data: "type_defs.CreateMediaInsightsPipelineResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def MediaInsightsPipeline(self):  # pragma: no cover
        return MediaInsightsPipeline.make_one(
            self.boto3_raw_data["MediaInsightsPipeline"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateMediaInsightsPipelineResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMediaInsightsPipelineResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MediaCapturePipeline:
    boto3_raw_data: "type_defs.MediaCapturePipelineTypeDef" = dataclasses.field()

    MediaPipelineId = field("MediaPipelineId")
    MediaPipelineArn = field("MediaPipelineArn")
    SourceType = field("SourceType")
    SourceArn = field("SourceArn")
    Status = field("Status")
    SinkType = field("SinkType")
    SinkArn = field("SinkArn")
    CreatedTimestamp = field("CreatedTimestamp")
    UpdatedTimestamp = field("UpdatedTimestamp")

    @cached_property
    def ChimeSdkMeetingConfiguration(self):  # pragma: no cover
        return ChimeSdkMeetingConfigurationOutput.make_one(
            self.boto3_raw_data["ChimeSdkMeetingConfiguration"]
        )

    @cached_property
    def SseAwsKeyManagementParams(self):  # pragma: no cover
        return SseAwsKeyManagementParams.make_one(
            self.boto3_raw_data["SseAwsKeyManagementParams"]
        )

    SinkIamRoleArn = field("SinkIamRoleArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MediaCapturePipelineTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MediaCapturePipelineTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MediaLiveConnectorPipeline:
    boto3_raw_data: "type_defs.MediaLiveConnectorPipelineTypeDef" = dataclasses.field()

    @cached_property
    def Sources(self):  # pragma: no cover
        return LiveConnectorSourceConfigurationOutput.make_many(
            self.boto3_raw_data["Sources"]
        )

    @cached_property
    def Sinks(self):  # pragma: no cover
        return LiveConnectorSinkConfiguration.make_many(self.boto3_raw_data["Sinks"])

    MediaPipelineId = field("MediaPipelineId")
    MediaPipelineArn = field("MediaPipelineArn")
    Status = field("Status")
    CreatedTimestamp = field("CreatedTimestamp")
    UpdatedTimestamp = field("UpdatedTimestamp")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MediaLiveConnectorPipelineTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MediaLiveConnectorPipelineTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMediaInsightsPipelineRequest:
    boto3_raw_data: "type_defs.CreateMediaInsightsPipelineRequestTypeDef" = (
        dataclasses.field()
    )

    MediaInsightsPipelineConfigurationArn = field(
        "MediaInsightsPipelineConfigurationArn"
    )
    KinesisVideoStreamSourceRuntimeConfiguration = field(
        "KinesisVideoStreamSourceRuntimeConfiguration"
    )
    MediaInsightsRuntimeMetadata = field("MediaInsightsRuntimeMetadata")
    KinesisVideoStreamRecordingSourceRuntimeConfiguration = field(
        "KinesisVideoStreamRecordingSourceRuntimeConfiguration"
    )

    @cached_property
    def S3RecordingSinkRuntimeConfiguration(self):  # pragma: no cover
        return S3RecordingSinkRuntimeConfiguration.make_one(
            self.boto3_raw_data["S3RecordingSinkRuntimeConfiguration"]
        )

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    ClientRequestToken = field("ClientRequestToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateMediaInsightsPipelineRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMediaInsightsPipelineRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMediaConcatenationPipelineResponse:
    boto3_raw_data: "type_defs.CreateMediaConcatenationPipelineResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def MediaConcatenationPipeline(self):  # pragma: no cover
        return MediaConcatenationPipeline.make_one(
            self.boto3_raw_data["MediaConcatenationPipeline"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateMediaConcatenationPipelineResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMediaConcatenationPipelineResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMediaCapturePipelineResponse:
    boto3_raw_data: "type_defs.CreateMediaCapturePipelineResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def MediaCapturePipeline(self):  # pragma: no cover
        return MediaCapturePipeline.make_one(
            self.boto3_raw_data["MediaCapturePipeline"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateMediaCapturePipelineResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMediaCapturePipelineResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMediaCapturePipelineResponse:
    boto3_raw_data: "type_defs.GetMediaCapturePipelineResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def MediaCapturePipeline(self):  # pragma: no cover
        return MediaCapturePipeline.make_one(
            self.boto3_raw_data["MediaCapturePipeline"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetMediaCapturePipelineResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMediaCapturePipelineResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMediaCapturePipelineRequest:
    boto3_raw_data: "type_defs.CreateMediaCapturePipelineRequestTypeDef" = (
        dataclasses.field()
    )

    SourceType = field("SourceType")
    SourceArn = field("SourceArn")
    SinkType = field("SinkType")
    SinkArn = field("SinkArn")
    ClientRequestToken = field("ClientRequestToken")
    ChimeSdkMeetingConfiguration = field("ChimeSdkMeetingConfiguration")

    @cached_property
    def SseAwsKeyManagementParams(self):  # pragma: no cover
        return SseAwsKeyManagementParams.make_one(
            self.boto3_raw_data["SseAwsKeyManagementParams"]
        )

    SinkIamRoleArn = field("SinkIamRoleArn")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateMediaCapturePipelineRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMediaCapturePipelineRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMediaLiveConnectorPipelineResponse:
    boto3_raw_data: "type_defs.CreateMediaLiveConnectorPipelineResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def MediaLiveConnectorPipeline(self):  # pragma: no cover
        return MediaLiveConnectorPipeline.make_one(
            self.boto3_raw_data["MediaLiveConnectorPipeline"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateMediaLiveConnectorPipelineResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMediaLiveConnectorPipelineResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MediaPipeline:
    boto3_raw_data: "type_defs.MediaPipelineTypeDef" = dataclasses.field()

    @cached_property
    def MediaCapturePipeline(self):  # pragma: no cover
        return MediaCapturePipeline.make_one(
            self.boto3_raw_data["MediaCapturePipeline"]
        )

    @cached_property
    def MediaLiveConnectorPipeline(self):  # pragma: no cover
        return MediaLiveConnectorPipeline.make_one(
            self.boto3_raw_data["MediaLiveConnectorPipeline"]
        )

    @cached_property
    def MediaConcatenationPipeline(self):  # pragma: no cover
        return MediaConcatenationPipeline.make_one(
            self.boto3_raw_data["MediaConcatenationPipeline"]
        )

    @cached_property
    def MediaInsightsPipeline(self):  # pragma: no cover
        return MediaInsightsPipeline.make_one(
            self.boto3_raw_data["MediaInsightsPipeline"]
        )

    @cached_property
    def MediaStreamPipeline(self):  # pragma: no cover
        return MediaStreamPipeline.make_one(self.boto3_raw_data["MediaStreamPipeline"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MediaPipelineTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MediaPipelineTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LiveConnectorSourceConfiguration:
    boto3_raw_data: "type_defs.LiveConnectorSourceConfigurationTypeDef" = (
        dataclasses.field()
    )

    SourceType = field("SourceType")
    ChimeSdkMeetingLiveConnectorConfiguration = field(
        "ChimeSdkMeetingLiveConnectorConfiguration"
    )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.LiveConnectorSourceConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LiveConnectorSourceConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMediaPipelineResponse:
    boto3_raw_data: "type_defs.GetMediaPipelineResponseTypeDef" = dataclasses.field()

    @cached_property
    def MediaPipeline(self):  # pragma: no cover
        return MediaPipeline.make_one(self.boto3_raw_data["MediaPipeline"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMediaPipelineResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMediaPipelineResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMediaLiveConnectorPipelineRequest:
    boto3_raw_data: "type_defs.CreateMediaLiveConnectorPipelineRequestTypeDef" = (
        dataclasses.field()
    )

    Sources = field("Sources")

    @cached_property
    def Sinks(self):  # pragma: no cover
        return LiveConnectorSinkConfiguration.make_many(self.boto3_raw_data["Sinks"])

    ClientRequestToken = field("ClientRequestToken")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateMediaLiveConnectorPipelineRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMediaLiveConnectorPipelineRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
