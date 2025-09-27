# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_connectparticipant import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AttachmentItem:
    boto3_raw_data: "type_defs.AttachmentItemTypeDef" = dataclasses.field()

    ContentType = field("ContentType")
    AttachmentId = field("AttachmentId")
    AttachmentName = field("AttachmentName")
    Status = field("Status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AttachmentItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AttachmentItemTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Attendee:
    boto3_raw_data: "type_defs.AttendeeTypeDef" = dataclasses.field()

    AttendeeId = field("AttendeeId")
    JoinToken = field("JoinToken")

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
class CancelParticipantAuthenticationRequest:
    boto3_raw_data: "type_defs.CancelParticipantAuthenticationRequestTypeDef" = (
        dataclasses.field()
    )

    SessionId = field("SessionId")
    ConnectionToken = field("ConnectionToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CancelParticipantAuthenticationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelParticipantAuthenticationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CompleteAttachmentUploadRequest:
    boto3_raw_data: "type_defs.CompleteAttachmentUploadRequestTypeDef" = (
        dataclasses.field()
    )

    AttachmentIds = field("AttachmentIds")
    ClientToken = field("ClientToken")
    ConnectionToken = field("ConnectionToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CompleteAttachmentUploadRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CompleteAttachmentUploadRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConnectionCredentials:
    boto3_raw_data: "type_defs.ConnectionCredentialsTypeDef" = dataclasses.field()

    ConnectionToken = field("ConnectionToken")
    Expiry = field("Expiry")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConnectionCredentialsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConnectionCredentialsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateParticipantConnectionRequest:
    boto3_raw_data: "type_defs.CreateParticipantConnectionRequestTypeDef" = (
        dataclasses.field()
    )

    ParticipantToken = field("ParticipantToken")
    Type = field("Type")
    ConnectParticipant = field("ConnectParticipant")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateParticipantConnectionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateParticipantConnectionRequestTypeDef"]
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
class Websocket:
    boto3_raw_data: "type_defs.WebsocketTypeDef" = dataclasses.field()

    Url = field("Url")
    ConnectionExpiry = field("ConnectionExpiry")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WebsocketTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WebsocketTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeViewRequest:
    boto3_raw_data: "type_defs.DescribeViewRequestTypeDef" = dataclasses.field()

    ViewToken = field("ViewToken")
    ConnectionToken = field("ConnectionToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeViewRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeViewRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisconnectParticipantRequest:
    boto3_raw_data: "type_defs.DisconnectParticipantRequestTypeDef" = (
        dataclasses.field()
    )

    ConnectionToken = field("ConnectionToken")
    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DisconnectParticipantRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisconnectParticipantRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAttachmentRequest:
    boto3_raw_data: "type_defs.GetAttachmentRequestTypeDef" = dataclasses.field()

    AttachmentId = field("AttachmentId")
    ConnectionToken = field("ConnectionToken")
    UrlExpiryInSeconds = field("UrlExpiryInSeconds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAttachmentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAttachmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAuthenticationUrlRequest:
    boto3_raw_data: "type_defs.GetAuthenticationUrlRequestTypeDef" = dataclasses.field()

    SessionId = field("SessionId")
    RedirectUri = field("RedirectUri")
    ConnectionToken = field("ConnectionToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAuthenticationUrlRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAuthenticationUrlRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartPosition:
    boto3_raw_data: "type_defs.StartPositionTypeDef" = dataclasses.field()

    Id = field("Id")
    AbsoluteTime = field("AbsoluteTime")
    MostRecent = field("MostRecent")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StartPositionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StartPositionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Receipt:
    boto3_raw_data: "type_defs.ReceiptTypeDef" = dataclasses.field()

    DeliveredTimestamp = field("DeliveredTimestamp")
    ReadTimestamp = field("ReadTimestamp")
    RecipientParticipantId = field("RecipientParticipantId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReceiptTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ReceiptTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SendEventRequest:
    boto3_raw_data: "type_defs.SendEventRequestTypeDef" = dataclasses.field()

    ContentType = field("ContentType")
    ConnectionToken = field("ConnectionToken")
    Content = field("Content")
    ClientToken = field("ClientToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SendEventRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SendEventRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SendMessageRequest:
    boto3_raw_data: "type_defs.SendMessageRequestTypeDef" = dataclasses.field()

    ContentType = field("ContentType")
    Content = field("Content")
    ConnectionToken = field("ConnectionToken")
    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SendMessageRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SendMessageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartAttachmentUploadRequest:
    boto3_raw_data: "type_defs.StartAttachmentUploadRequestTypeDef" = (
        dataclasses.field()
    )

    ContentType = field("ContentType")
    AttachmentSizeInBytes = field("AttachmentSizeInBytes")
    AttachmentName = field("AttachmentName")
    ClientToken = field("ClientToken")
    ConnectionToken = field("ConnectionToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartAttachmentUploadRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartAttachmentUploadRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UploadMetadata:
    boto3_raw_data: "type_defs.UploadMetadataTypeDef" = dataclasses.field()

    Url = field("Url")
    UrlExpiry = field("UrlExpiry")
    HeadersToInclude = field("HeadersToInclude")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UploadMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UploadMetadataTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ViewContent:
    boto3_raw_data: "type_defs.ViewContentTypeDef" = dataclasses.field()

    InputSchema = field("InputSchema")
    Template = field("Template")
    Actions = field("Actions")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ViewContentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ViewContentTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WebRTCMediaPlacement:
    boto3_raw_data: "type_defs.WebRTCMediaPlacementTypeDef" = dataclasses.field()

    AudioHostUrl = field("AudioHostUrl")
    AudioFallbackUrl = field("AudioFallbackUrl")
    SignalingUrl = field("SignalingUrl")
    EventIngestionUrl = field("EventIngestionUrl")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WebRTCMediaPlacementTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WebRTCMediaPlacementTypeDef"]
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
class GetAttachmentResponse:
    boto3_raw_data: "type_defs.GetAttachmentResponseTypeDef" = dataclasses.field()

    Url = field("Url")
    UrlExpiry = field("UrlExpiry")
    AttachmentSizeInBytes = field("AttachmentSizeInBytes")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAttachmentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAttachmentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAuthenticationUrlResponse:
    boto3_raw_data: "type_defs.GetAuthenticationUrlResponseTypeDef" = (
        dataclasses.field()
    )

    AuthenticationUrl = field("AuthenticationUrl")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAuthenticationUrlResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAuthenticationUrlResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SendEventResponse:
    boto3_raw_data: "type_defs.SendEventResponseTypeDef" = dataclasses.field()

    Id = field("Id")
    AbsoluteTime = field("AbsoluteTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SendEventResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SendEventResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SendMessageResponse:
    boto3_raw_data: "type_defs.SendMessageResponseTypeDef" = dataclasses.field()

    Id = field("Id")
    AbsoluteTime = field("AbsoluteTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SendMessageResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SendMessageResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTranscriptRequest:
    boto3_raw_data: "type_defs.GetTranscriptRequestTypeDef" = dataclasses.field()

    ConnectionToken = field("ConnectionToken")
    ContactId = field("ContactId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    ScanDirection = field("ScanDirection")
    SortOrder = field("SortOrder")

    @cached_property
    def StartPosition(self):  # pragma: no cover
        return StartPosition.make_one(self.boto3_raw_data["StartPosition"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTranscriptRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTranscriptRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MessageMetadata:
    boto3_raw_data: "type_defs.MessageMetadataTypeDef" = dataclasses.field()

    MessageId = field("MessageId")

    @cached_property
    def Receipts(self):  # pragma: no cover
        return Receipt.make_many(self.boto3_raw_data["Receipts"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MessageMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MessageMetadataTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartAttachmentUploadResponse:
    boto3_raw_data: "type_defs.StartAttachmentUploadResponseTypeDef" = (
        dataclasses.field()
    )

    AttachmentId = field("AttachmentId")

    @cached_property
    def UploadMetadata(self):  # pragma: no cover
        return UploadMetadata.make_one(self.boto3_raw_data["UploadMetadata"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartAttachmentUploadResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartAttachmentUploadResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class View:
    boto3_raw_data: "type_defs.ViewTypeDef" = dataclasses.field()

    Id = field("Id")
    Arn = field("Arn")
    Name = field("Name")
    Version = field("Version")

    @cached_property
    def Content(self):  # pragma: no cover
        return ViewContent.make_one(self.boto3_raw_data["Content"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ViewTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ViewTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WebRTCMeeting:
    boto3_raw_data: "type_defs.WebRTCMeetingTypeDef" = dataclasses.field()

    @cached_property
    def MediaPlacement(self):  # pragma: no cover
        return WebRTCMediaPlacement.make_one(self.boto3_raw_data["MediaPlacement"])

    @cached_property
    def MeetingFeatures(self):  # pragma: no cover
        return MeetingFeaturesConfiguration.make_one(
            self.boto3_raw_data["MeetingFeatures"]
        )

    MeetingId = field("MeetingId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WebRTCMeetingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WebRTCMeetingTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Item:
    boto3_raw_data: "type_defs.ItemTypeDef" = dataclasses.field()

    AbsoluteTime = field("AbsoluteTime")
    Content = field("Content")
    ContentType = field("ContentType")
    Id = field("Id")
    Type = field("Type")
    ParticipantId = field("ParticipantId")
    DisplayName = field("DisplayName")
    ParticipantRole = field("ParticipantRole")

    @cached_property
    def Attachments(self):  # pragma: no cover
        return AttachmentItem.make_many(self.boto3_raw_data["Attachments"])

    @cached_property
    def MessageMetadata(self):  # pragma: no cover
        return MessageMetadata.make_one(self.boto3_raw_data["MessageMetadata"])

    RelatedContactId = field("RelatedContactId")
    ContactId = field("ContactId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ItemTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeViewResponse:
    boto3_raw_data: "type_defs.DescribeViewResponseTypeDef" = dataclasses.field()

    @cached_property
    def View(self):  # pragma: no cover
        return View.make_one(self.boto3_raw_data["View"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeViewResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeViewResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WebRTCConnection:
    boto3_raw_data: "type_defs.WebRTCConnectionTypeDef" = dataclasses.field()

    @cached_property
    def Attendee(self):  # pragma: no cover
        return Attendee.make_one(self.boto3_raw_data["Attendee"])

    @cached_property
    def Meeting(self):  # pragma: no cover
        return WebRTCMeeting.make_one(self.boto3_raw_data["Meeting"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WebRTCConnectionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WebRTCConnectionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTranscriptResponse:
    boto3_raw_data: "type_defs.GetTranscriptResponseTypeDef" = dataclasses.field()

    InitialContactId = field("InitialContactId")

    @cached_property
    def Transcript(self):  # pragma: no cover
        return Item.make_many(self.boto3_raw_data["Transcript"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTranscriptResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTranscriptResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateParticipantConnectionResponse:
    boto3_raw_data: "type_defs.CreateParticipantConnectionResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Websocket(self):  # pragma: no cover
        return Websocket.make_one(self.boto3_raw_data["Websocket"])

    @cached_property
    def ConnectionCredentials(self):  # pragma: no cover
        return ConnectionCredentials.make_one(
            self.boto3_raw_data["ConnectionCredentials"]
        )

    @cached_property
    def WebRTCConnection(self):  # pragma: no cover
        return WebRTCConnection.make_one(self.boto3_raw_data["WebRTCConnection"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateParticipantConnectionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateParticipantConnectionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
