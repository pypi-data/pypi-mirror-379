# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_chime_sdk_meetings import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AttendeeCapabilities:
    boto3_raw_data: "type_defs.AttendeeCapabilitiesTypeDef" = dataclasses.field()

    Audio = field("Audio")
    Video = field("Video")
    Content = field("Content")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AttendeeCapabilitiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttendeeCapabilitiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttendeeFeatures:
    boto3_raw_data: "type_defs.AttendeeFeaturesTypeDef" = dataclasses.field()

    MaxCount = field("MaxCount")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AttendeeFeaturesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttendeeFeaturesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttendeeIdItem:
    boto3_raw_data: "type_defs.AttendeeIdItemTypeDef" = dataclasses.field()

    AttendeeId = field("AttendeeId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AttendeeIdItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AttendeeIdItemTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AudioFeatures:
    boto3_raw_data: "type_defs.AudioFeaturesTypeDef" = dataclasses.field()

    EchoReduction = field("EchoReduction")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AudioFeaturesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AudioFeaturesTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAttendeeError:
    boto3_raw_data: "type_defs.CreateAttendeeErrorTypeDef" = dataclasses.field()

    ExternalUserId = field("ExternalUserId")
    ErrorCode = field("ErrorCode")
    ErrorMessage = field("ErrorMessage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAttendeeErrorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAttendeeErrorTypeDef"]
        ],
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
class ContentFeatures:
    boto3_raw_data: "type_defs.ContentFeaturesTypeDef" = dataclasses.field()

    MaxResolution = field("MaxResolution")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ContentFeaturesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ContentFeaturesTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NotificationsConfiguration:
    boto3_raw_data: "type_defs.NotificationsConfigurationTypeDef" = dataclasses.field()

    LambdaFunctionArn = field("LambdaFunctionArn")
    SnsTopicArn = field("SnsTopicArn")
    SqsQueueArn = field("SqsQueueArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NotificationsConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NotificationsConfigurationTypeDef"]
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
class DeleteAttendeeRequest:
    boto3_raw_data: "type_defs.DeleteAttendeeRequestTypeDef" = dataclasses.field()

    MeetingId = field("MeetingId")
    AttendeeId = field("AttendeeId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAttendeeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAttendeeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteMeetingRequest:
    boto3_raw_data: "type_defs.DeleteMeetingRequestTypeDef" = dataclasses.field()

    MeetingId = field("MeetingId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteMeetingRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteMeetingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EngineTranscribeMedicalSettings:
    boto3_raw_data: "type_defs.EngineTranscribeMedicalSettingsTypeDef" = (
        dataclasses.field()
    )

    LanguageCode = field("LanguageCode")
    Specialty = field("Specialty")
    Type = field("Type")
    VocabularyName = field("VocabularyName")
    Region = field("Region")
    ContentIdentificationType = field("ContentIdentificationType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.EngineTranscribeMedicalSettingsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EngineTranscribeMedicalSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EngineTranscribeSettings:
    boto3_raw_data: "type_defs.EngineTranscribeSettingsTypeDef" = dataclasses.field()

    LanguageCode = field("LanguageCode")
    VocabularyFilterMethod = field("VocabularyFilterMethod")
    VocabularyFilterName = field("VocabularyFilterName")
    VocabularyName = field("VocabularyName")
    Region = field("Region")
    EnablePartialResultsStabilization = field("EnablePartialResultsStabilization")
    PartialResultsStability = field("PartialResultsStability")
    ContentIdentificationType = field("ContentIdentificationType")
    ContentRedactionType = field("ContentRedactionType")
    PiiEntityTypes = field("PiiEntityTypes")
    LanguageModelName = field("LanguageModelName")
    IdentifyLanguage = field("IdentifyLanguage")
    LanguageOptions = field("LanguageOptions")
    PreferredLanguage = field("PreferredLanguage")
    VocabularyNames = field("VocabularyNames")
    VocabularyFilterNames = field("VocabularyFilterNames")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EngineTranscribeSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EngineTranscribeSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAttendeeRequest:
    boto3_raw_data: "type_defs.GetAttendeeRequestTypeDef" = dataclasses.field()

    MeetingId = field("MeetingId")
    AttendeeId = field("AttendeeId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAttendeeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAttendeeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMeetingRequest:
    boto3_raw_data: "type_defs.GetMeetingRequestTypeDef" = dataclasses.field()

    MeetingId = field("MeetingId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetMeetingRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMeetingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAttendeesRequest:
    boto3_raw_data: "type_defs.ListAttendeesRequestTypeDef" = dataclasses.field()

    MeetingId = field("MeetingId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAttendeesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAttendeesRequestTypeDef"]
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
class MediaPlacement:
    boto3_raw_data: "type_defs.MediaPlacementTypeDef" = dataclasses.field()

    AudioHostUrl = field("AudioHostUrl")
    AudioFallbackUrl = field("AudioFallbackUrl")
    SignalingUrl = field("SignalingUrl")
    TurnControlUrl = field("TurnControlUrl")
    ScreenDataUrl = field("ScreenDataUrl")
    ScreenViewingUrl = field("ScreenViewingUrl")
    ScreenSharingUrl = field("ScreenSharingUrl")
    EventIngestionUrl = field("EventIngestionUrl")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MediaPlacementTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MediaPlacementTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VideoFeatures:
    boto3_raw_data: "type_defs.VideoFeaturesTypeDef" = dataclasses.field()

    MaxResolution = field("MaxResolution")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VideoFeaturesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VideoFeaturesTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopMeetingTranscriptionRequest:
    boto3_raw_data: "type_defs.StopMeetingTranscriptionRequestTypeDef" = (
        dataclasses.field()
    )

    MeetingId = field("MeetingId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StopMeetingTranscriptionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopMeetingTranscriptionRequestTypeDef"]
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
class Attendee:
    boto3_raw_data: "type_defs.AttendeeTypeDef" = dataclasses.field()

    ExternalUserId = field("ExternalUserId")
    AttendeeId = field("AttendeeId")
    JoinToken = field("JoinToken")

    @cached_property
    def Capabilities(self):  # pragma: no cover
        return AttendeeCapabilities.make_one(self.boto3_raw_data["Capabilities"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AttendeeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AttendeeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAttendeeRequestItem:
    boto3_raw_data: "type_defs.CreateAttendeeRequestItemTypeDef" = dataclasses.field()

    ExternalUserId = field("ExternalUserId")

    @cached_property
    def Capabilities(self):  # pragma: no cover
        return AttendeeCapabilities.make_one(self.boto3_raw_data["Capabilities"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAttendeeRequestItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAttendeeRequestItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAttendeeRequest:
    boto3_raw_data: "type_defs.CreateAttendeeRequestTypeDef" = dataclasses.field()

    MeetingId = field("MeetingId")
    ExternalUserId = field("ExternalUserId")

    @cached_property
    def Capabilities(self):  # pragma: no cover
        return AttendeeCapabilities.make_one(self.boto3_raw_data["Capabilities"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAttendeeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAttendeeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAttendeeCapabilitiesRequest:
    boto3_raw_data: "type_defs.UpdateAttendeeCapabilitiesRequestTypeDef" = (
        dataclasses.field()
    )

    MeetingId = field("MeetingId")
    AttendeeId = field("AttendeeId")

    @cached_property
    def Capabilities(self):  # pragma: no cover
        return AttendeeCapabilities.make_one(self.boto3_raw_data["Capabilities"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateAttendeeCapabilitiesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAttendeeCapabilitiesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchUpdateAttendeeCapabilitiesExceptRequest:
    boto3_raw_data: "type_defs.BatchUpdateAttendeeCapabilitiesExceptRequestTypeDef" = (
        dataclasses.field()
    )

    MeetingId = field("MeetingId")

    @cached_property
    def ExcludedAttendeeIds(self):  # pragma: no cover
        return AttendeeIdItem.make_many(self.boto3_raw_data["ExcludedAttendeeIds"])

    @cached_property
    def Capabilities(self):  # pragma: no cover
        return AttendeeCapabilities.make_one(self.boto3_raw_data["Capabilities"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchUpdateAttendeeCapabilitiesExceptRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchUpdateAttendeeCapabilitiesExceptRequestTypeDef"]
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
class TranscriptionConfiguration:
    boto3_raw_data: "type_defs.TranscriptionConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def EngineTranscribeSettings(self):  # pragma: no cover
        return EngineTranscribeSettings.make_one(
            self.boto3_raw_data["EngineTranscribeSettings"]
        )

    @cached_property
    def EngineTranscribeMedicalSettings(self):  # pragma: no cover
        return EngineTranscribeMedicalSettings.make_one(
            self.boto3_raw_data["EngineTranscribeMedicalSettings"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TranscriptionConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TranscriptionConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MeetingFeaturesConfiguration:
    boto3_raw_data: "type_defs.MeetingFeaturesConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Audio(self):  # pragma: no cover
        return AudioFeatures.make_one(self.boto3_raw_data["Audio"])

    @cached_property
    def Video(self):  # pragma: no cover
        return VideoFeatures.make_one(self.boto3_raw_data["Video"])

    @cached_property
    def Content(self):  # pragma: no cover
        return ContentFeatures.make_one(self.boto3_raw_data["Content"])

    @cached_property
    def Attendee(self):  # pragma: no cover
        return AttendeeFeatures.make_one(self.boto3_raw_data["Attendee"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MeetingFeaturesConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MeetingFeaturesConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchCreateAttendeeResponse:
    boto3_raw_data: "type_defs.BatchCreateAttendeeResponseTypeDef" = dataclasses.field()

    @cached_property
    def Attendees(self):  # pragma: no cover
        return Attendee.make_many(self.boto3_raw_data["Attendees"])

    @cached_property
    def Errors(self):  # pragma: no cover
        return CreateAttendeeError.make_many(self.boto3_raw_data["Errors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchCreateAttendeeResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchCreateAttendeeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAttendeeResponse:
    boto3_raw_data: "type_defs.CreateAttendeeResponseTypeDef" = dataclasses.field()

    @cached_property
    def Attendee(self):  # pragma: no cover
        return Attendee.make_one(self.boto3_raw_data["Attendee"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAttendeeResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAttendeeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAttendeeResponse:
    boto3_raw_data: "type_defs.GetAttendeeResponseTypeDef" = dataclasses.field()

    @cached_property
    def Attendee(self):  # pragma: no cover
        return Attendee.make_one(self.boto3_raw_data["Attendee"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAttendeeResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAttendeeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAttendeesResponse:
    boto3_raw_data: "type_defs.ListAttendeesResponseTypeDef" = dataclasses.field()

    @cached_property
    def Attendees(self):  # pragma: no cover
        return Attendee.make_many(self.boto3_raw_data["Attendees"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAttendeesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAttendeesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAttendeeCapabilitiesResponse:
    boto3_raw_data: "type_defs.UpdateAttendeeCapabilitiesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Attendee(self):  # pragma: no cover
        return Attendee.make_one(self.boto3_raw_data["Attendee"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateAttendeeCapabilitiesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAttendeeCapabilitiesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchCreateAttendeeRequest:
    boto3_raw_data: "type_defs.BatchCreateAttendeeRequestTypeDef" = dataclasses.field()

    MeetingId = field("MeetingId")

    @cached_property
    def Attendees(self):  # pragma: no cover
        return CreateAttendeeRequestItem.make_many(self.boto3_raw_data["Attendees"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchCreateAttendeeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchCreateAttendeeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartMeetingTranscriptionRequest:
    boto3_raw_data: "type_defs.StartMeetingTranscriptionRequestTypeDef" = (
        dataclasses.field()
    )

    MeetingId = field("MeetingId")

    @cached_property
    def TranscriptionConfiguration(self):  # pragma: no cover
        return TranscriptionConfiguration.make_one(
            self.boto3_raw_data["TranscriptionConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartMeetingTranscriptionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartMeetingTranscriptionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMeetingRequest:
    boto3_raw_data: "type_defs.CreateMeetingRequestTypeDef" = dataclasses.field()

    ClientRequestToken = field("ClientRequestToken")
    MediaRegion = field("MediaRegion")
    ExternalMeetingId = field("ExternalMeetingId")
    MeetingHostId = field("MeetingHostId")

    @cached_property
    def NotificationsConfiguration(self):  # pragma: no cover
        return NotificationsConfiguration.make_one(
            self.boto3_raw_data["NotificationsConfiguration"]
        )

    @cached_property
    def MeetingFeatures(self):  # pragma: no cover
        return MeetingFeaturesConfiguration.make_one(
            self.boto3_raw_data["MeetingFeatures"]
        )

    PrimaryMeetingId = field("PrimaryMeetingId")
    TenantIds = field("TenantIds")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateMeetingRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMeetingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMeetingWithAttendeesRequest:
    boto3_raw_data: "type_defs.CreateMeetingWithAttendeesRequestTypeDef" = (
        dataclasses.field()
    )

    ClientRequestToken = field("ClientRequestToken")
    MediaRegion = field("MediaRegion")
    ExternalMeetingId = field("ExternalMeetingId")

    @cached_property
    def Attendees(self):  # pragma: no cover
        return CreateAttendeeRequestItem.make_many(self.boto3_raw_data["Attendees"])

    MeetingHostId = field("MeetingHostId")

    @cached_property
    def MeetingFeatures(self):  # pragma: no cover
        return MeetingFeaturesConfiguration.make_one(
            self.boto3_raw_data["MeetingFeatures"]
        )

    @cached_property
    def NotificationsConfiguration(self):  # pragma: no cover
        return NotificationsConfiguration.make_one(
            self.boto3_raw_data["NotificationsConfiguration"]
        )

    PrimaryMeetingId = field("PrimaryMeetingId")
    TenantIds = field("TenantIds")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateMeetingWithAttendeesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMeetingWithAttendeesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Meeting:
    boto3_raw_data: "type_defs.MeetingTypeDef" = dataclasses.field()

    MeetingId = field("MeetingId")
    MeetingHostId = field("MeetingHostId")
    ExternalMeetingId = field("ExternalMeetingId")
    MediaRegion = field("MediaRegion")

    @cached_property
    def MediaPlacement(self):  # pragma: no cover
        return MediaPlacement.make_one(self.boto3_raw_data["MediaPlacement"])

    @cached_property
    def MeetingFeatures(self):  # pragma: no cover
        return MeetingFeaturesConfiguration.make_one(
            self.boto3_raw_data["MeetingFeatures"]
        )

    PrimaryMeetingId = field("PrimaryMeetingId")
    TenantIds = field("TenantIds")
    MeetingArn = field("MeetingArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MeetingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MeetingTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMeetingResponse:
    boto3_raw_data: "type_defs.CreateMeetingResponseTypeDef" = dataclasses.field()

    @cached_property
    def Meeting(self):  # pragma: no cover
        return Meeting.make_one(self.boto3_raw_data["Meeting"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateMeetingResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMeetingResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMeetingWithAttendeesResponse:
    boto3_raw_data: "type_defs.CreateMeetingWithAttendeesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Meeting(self):  # pragma: no cover
        return Meeting.make_one(self.boto3_raw_data["Meeting"])

    @cached_property
    def Attendees(self):  # pragma: no cover
        return Attendee.make_many(self.boto3_raw_data["Attendees"])

    @cached_property
    def Errors(self):  # pragma: no cover
        return CreateAttendeeError.make_many(self.boto3_raw_data["Errors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateMeetingWithAttendeesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMeetingWithAttendeesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMeetingResponse:
    boto3_raw_data: "type_defs.GetMeetingResponseTypeDef" = dataclasses.field()

    @cached_property
    def Meeting(self):  # pragma: no cover
        return Meeting.make_one(self.boto3_raw_data["Meeting"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMeetingResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMeetingResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
