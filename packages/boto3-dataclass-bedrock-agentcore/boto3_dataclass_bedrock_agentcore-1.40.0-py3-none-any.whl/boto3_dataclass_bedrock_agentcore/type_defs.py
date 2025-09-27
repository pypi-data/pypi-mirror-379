# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_bedrock_agentcore import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AccessDeniedException:
    boto3_raw_data: "type_defs.AccessDeniedExceptionTypeDef" = dataclasses.field()

    message = field("message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AccessDeniedExceptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccessDeniedExceptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActorSummary:
    boto3_raw_data: "type_defs.ActorSummaryTypeDef" = dataclasses.field()

    actorId = field("actorId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ActorSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ActorSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomationStream:
    boto3_raw_data: "type_defs.AutomationStreamTypeDef" = dataclasses.field()

    streamEndpoint = field("streamEndpoint")
    streamStatus = field("streamStatus")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AutomationStreamTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutomationStreamTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomationStreamUpdate:
    boto3_raw_data: "type_defs.AutomationStreamUpdateTypeDef" = dataclasses.field()

    streamStatus = field("streamStatus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AutomationStreamUpdateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutomationStreamUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BranchFilter:
    boto3_raw_data: "type_defs.BranchFilterTypeDef" = dataclasses.field()

    name = field("name")
    includeParentBranches = field("includeParentBranches")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BranchFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BranchFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Branch:
    boto3_raw_data: "type_defs.BranchTypeDef" = dataclasses.field()

    name = field("name")
    rootEventId = field("rootEventId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BranchTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BranchTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LiveViewStream:
    boto3_raw_data: "type_defs.LiveViewStreamTypeDef" = dataclasses.field()

    streamEndpoint = field("streamEndpoint")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LiveViewStreamTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LiveViewStreamTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BrowserSessionSummary:
    boto3_raw_data: "type_defs.BrowserSessionSummaryTypeDef" = dataclasses.field()

    browserIdentifier = field("browserIdentifier")
    sessionId = field("sessionId")
    status = field("status")
    createdAt = field("createdAt")
    name = field("name")
    lastUpdatedAt = field("lastUpdatedAt")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BrowserSessionSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BrowserSessionSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ToolResultStructuredContent:
    boto3_raw_data: "type_defs.ToolResultStructuredContentTypeDef" = dataclasses.field()

    taskId = field("taskId")
    taskStatus = field("taskStatus")
    stdout = field("stdout")
    stderr = field("stderr")
    exitCode = field("exitCode")
    executionTime = field("executionTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ToolResultStructuredContentTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ToolResultStructuredContentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CodeInterpreterSessionSummary:
    boto3_raw_data: "type_defs.CodeInterpreterSessionSummaryTypeDef" = (
        dataclasses.field()
    )

    codeInterpreterIdentifier = field("codeInterpreterIdentifier")
    sessionId = field("sessionId")
    status = field("status")
    createdAt = field("createdAt")
    name = field("name")
    lastUpdatedAt = field("lastUpdatedAt")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CodeInterpreterSessionSummaryTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CodeInterpreterSessionSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConflictException:
    boto3_raw_data: "type_defs.ConflictExceptionTypeDef" = dataclasses.field()

    message = field("message")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConflictExceptionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConflictExceptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InternalServerException:
    boto3_raw_data: "type_defs.InternalServerExceptionTypeDef" = dataclasses.field()

    message = field("message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InternalServerExceptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InternalServerExceptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceNotFoundException:
    boto3_raw_data: "type_defs.ResourceNotFoundExceptionTypeDef" = dataclasses.field()

    message = field("message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResourceNotFoundExceptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceNotFoundExceptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceQuotaExceededException:
    boto3_raw_data: "type_defs.ServiceQuotaExceededExceptionTypeDef" = (
        dataclasses.field()
    )

    message = field("message")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ServiceQuotaExceededExceptionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceQuotaExceededExceptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ThrottlingException:
    boto3_raw_data: "type_defs.ThrottlingExceptionTypeDef" = dataclasses.field()

    message = field("message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ThrottlingExceptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ThrottlingExceptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceContent:
    boto3_raw_data: "type_defs.ResourceContentTypeDef" = dataclasses.field()

    type = field("type")
    uri = field("uri")
    mimeType = field("mimeType")
    text = field("text")
    blob = field("blob")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResourceContentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResourceContentTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Content:
    boto3_raw_data: "type_defs.ContentTypeDef" = dataclasses.field()

    text = field("text")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ContentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ContentTypeDef"]]
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
class DeleteEventInput:
    boto3_raw_data: "type_defs.DeleteEventInputTypeDef" = dataclasses.field()

    memoryId = field("memoryId")
    sessionId = field("sessionId")
    eventId = field("eventId")
    actorId = field("actorId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteEventInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteEventInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteMemoryRecordInput:
    boto3_raw_data: "type_defs.DeleteMemoryRecordInputTypeDef" = dataclasses.field()

    memoryId = field("memoryId")
    memoryRecordId = field("memoryRecordId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteMemoryRecordInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteMemoryRecordInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBrowserSessionRequest:
    boto3_raw_data: "type_defs.GetBrowserSessionRequestTypeDef" = dataclasses.field()

    browserIdentifier = field("browserIdentifier")
    sessionId = field("sessionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBrowserSessionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBrowserSessionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ViewPort:
    boto3_raw_data: "type_defs.ViewPortTypeDef" = dataclasses.field()

    width = field("width")
    height = field("height")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ViewPortTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ViewPortTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCodeInterpreterSessionRequest:
    boto3_raw_data: "type_defs.GetCodeInterpreterSessionRequestTypeDef" = (
        dataclasses.field()
    )

    codeInterpreterIdentifier = field("codeInterpreterIdentifier")
    sessionId = field("sessionId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetCodeInterpreterSessionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCodeInterpreterSessionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEventInput:
    boto3_raw_data: "type_defs.GetEventInputTypeDef" = dataclasses.field()

    memoryId = field("memoryId")
    sessionId = field("sessionId")
    actorId = field("actorId")
    eventId = field("eventId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetEventInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetEventInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMemoryRecordInput:
    boto3_raw_data: "type_defs.GetMemoryRecordInputTypeDef" = dataclasses.field()

    memoryId = field("memoryId")
    memoryRecordId = field("memoryRecordId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMemoryRecordInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMemoryRecordInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResourceApiKeyRequest:
    boto3_raw_data: "type_defs.GetResourceApiKeyRequestTypeDef" = dataclasses.field()

    workloadIdentityToken = field("workloadIdentityToken")
    resourceCredentialProviderName = field("resourceCredentialProviderName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetResourceApiKeyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResourceApiKeyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResourceOauth2TokenRequest:
    boto3_raw_data: "type_defs.GetResourceOauth2TokenRequestTypeDef" = (
        dataclasses.field()
    )

    workloadIdentityToken = field("workloadIdentityToken")
    resourceCredentialProviderName = field("resourceCredentialProviderName")
    scopes = field("scopes")
    oauth2Flow = field("oauth2Flow")
    resourceOauth2ReturnUrl = field("resourceOauth2ReturnUrl")
    forceAuthentication = field("forceAuthentication")
    customParameters = field("customParameters")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetResourceOauth2TokenRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResourceOauth2TokenRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetWorkloadAccessTokenForJWTRequest:
    boto3_raw_data: "type_defs.GetWorkloadAccessTokenForJWTRequestTypeDef" = (
        dataclasses.field()
    )

    workloadName = field("workloadName")
    userToken = field("userToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetWorkloadAccessTokenForJWTRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetWorkloadAccessTokenForJWTRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetWorkloadAccessTokenForUserIdRequest:
    boto3_raw_data: "type_defs.GetWorkloadAccessTokenForUserIdRequestTypeDef" = (
        dataclasses.field()
    )

    workloadName = field("workloadName")
    userId = field("userId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetWorkloadAccessTokenForUserIdRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetWorkloadAccessTokenForUserIdRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetWorkloadAccessTokenRequest:
    boto3_raw_data: "type_defs.GetWorkloadAccessTokenRequestTypeDef" = (
        dataclasses.field()
    )

    workloadName = field("workloadName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetWorkloadAccessTokenRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetWorkloadAccessTokenRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PaginatorConfig:
    boto3_raw_data: "type_defs.PaginatorConfigTypeDef" = dataclasses.field()

    MaxItems = field("MaxItems")
    PageSize = field("PageSize")
    StartingToken = field("StartingToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PaginatorConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PaginatorConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListActorsInput:
    boto3_raw_data: "type_defs.ListActorsInputTypeDef" = dataclasses.field()

    memoryId = field("memoryId")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListActorsInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListActorsInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBrowserSessionsRequest:
    boto3_raw_data: "type_defs.ListBrowserSessionsRequestTypeDef" = dataclasses.field()

    browserIdentifier = field("browserIdentifier")
    maxResults = field("maxResults")
    nextToken = field("nextToken")
    status = field("status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBrowserSessionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBrowserSessionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCodeInterpreterSessionsRequest:
    boto3_raw_data: "type_defs.ListCodeInterpreterSessionsRequestTypeDef" = (
        dataclasses.field()
    )

    codeInterpreterIdentifier = field("codeInterpreterIdentifier")
    maxResults = field("maxResults")
    nextToken = field("nextToken")
    status = field("status")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCodeInterpreterSessionsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCodeInterpreterSessionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMemoryRecordsInput:
    boto3_raw_data: "type_defs.ListMemoryRecordsInputTypeDef" = dataclasses.field()

    memoryId = field("memoryId")
    namespace = field("namespace")
    memoryStrategyId = field("memoryStrategyId")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMemoryRecordsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMemoryRecordsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSessionsInput:
    boto3_raw_data: "type_defs.ListSessionsInputTypeDef" = dataclasses.field()

    memoryId = field("memoryId")
    actorId = field("actorId")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListSessionsInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSessionsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SessionSummary:
    boto3_raw_data: "type_defs.SessionSummaryTypeDef" = dataclasses.field()

    sessionId = field("sessionId")
    actorId = field("actorId")
    createdAt = field("createdAt")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SessionSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SessionSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MemoryContent:
    boto3_raw_data: "type_defs.MemoryContentTypeDef" = dataclasses.field()

    text = field("text")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MemoryContentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MemoryContentTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchCriteria:
    boto3_raw_data: "type_defs.SearchCriteriaTypeDef" = dataclasses.field()

    searchQuery = field("searchQuery")
    memoryStrategyId = field("memoryStrategyId")
    topK = field("topK")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SearchCriteriaTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SearchCriteriaTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartCodeInterpreterSessionRequest:
    boto3_raw_data: "type_defs.StartCodeInterpreterSessionRequestTypeDef" = (
        dataclasses.field()
    )

    codeInterpreterIdentifier = field("codeInterpreterIdentifier")
    name = field("name")
    sessionTimeoutSeconds = field("sessionTimeoutSeconds")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartCodeInterpreterSessionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartCodeInterpreterSessionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopBrowserSessionRequest:
    boto3_raw_data: "type_defs.StopBrowserSessionRequestTypeDef" = dataclasses.field()

    browserIdentifier = field("browserIdentifier")
    sessionId = field("sessionId")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopBrowserSessionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopBrowserSessionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopCodeInterpreterSessionRequest:
    boto3_raw_data: "type_defs.StopCodeInterpreterSessionRequestTypeDef" = (
        dataclasses.field()
    )

    codeInterpreterIdentifier = field("codeInterpreterIdentifier")
    sessionId = field("sessionId")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StopCodeInterpreterSessionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopCodeInterpreterSessionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ValidationExceptionField:
    boto3_raw_data: "type_defs.ValidationExceptionFieldTypeDef" = dataclasses.field()

    name = field("name")
    message = field("message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ValidationExceptionFieldTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ValidationExceptionFieldTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StreamUpdate:
    boto3_raw_data: "type_defs.StreamUpdateTypeDef" = dataclasses.field()

    @cached_property
    def automationStreamUpdate(self):  # pragma: no cover
        return AutomationStreamUpdate.make_one(
            self.boto3_raw_data["automationStreamUpdate"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StreamUpdateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StreamUpdateTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputContentBlock:
    boto3_raw_data: "type_defs.InputContentBlockTypeDef" = dataclasses.field()

    path = field("path")
    text = field("text")
    blob = field("blob")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InputContentBlockTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InputContentBlockTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InvokeAgentRuntimeRequest:
    boto3_raw_data: "type_defs.InvokeAgentRuntimeRequestTypeDef" = dataclasses.field()

    agentRuntimeArn = field("agentRuntimeArn")
    payload = field("payload")
    contentType = field("contentType")
    accept = field("accept")
    mcpSessionId = field("mcpSessionId")
    runtimeSessionId = field("runtimeSessionId")
    mcpProtocolVersion = field("mcpProtocolVersion")
    runtimeUserId = field("runtimeUserId")
    traceId = field("traceId")
    traceParent = field("traceParent")
    traceState = field("traceState")
    baggage = field("baggage")
    qualifier = field("qualifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InvokeAgentRuntimeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InvokeAgentRuntimeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FilterInput:
    boto3_raw_data: "type_defs.FilterInputTypeDef" = dataclasses.field()

    @cached_property
    def branch(self):  # pragma: no cover
        return BranchFilter.make_one(self.boto3_raw_data["branch"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FilterInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FilterInputTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BrowserSessionStream:
    boto3_raw_data: "type_defs.BrowserSessionStreamTypeDef" = dataclasses.field()

    @cached_property
    def automationStream(self):  # pragma: no cover
        return AutomationStream.make_one(self.boto3_raw_data["automationStream"])

    @cached_property
    def liveViewStream(self):  # pragma: no cover
        return LiveViewStream.make_one(self.boto3_raw_data["liveViewStream"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BrowserSessionStreamTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BrowserSessionStreamTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContentBlock:
    boto3_raw_data: "type_defs.ContentBlockTypeDef" = dataclasses.field()

    type = field("type")
    text = field("text")
    data = field("data")
    mimeType = field("mimeType")
    uri = field("uri")
    name = field("name")
    description = field("description")
    size = field("size")

    @cached_property
    def resource(self):  # pragma: no cover
        return ResourceContent.make_one(self.boto3_raw_data["resource"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ContentBlockTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ContentBlockTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Conversational:
    boto3_raw_data: "type_defs.ConversationalTypeDef" = dataclasses.field()

    @cached_property
    def content(self):  # pragma: no cover
        return Content.make_one(self.boto3_raw_data["content"])

    role = field("role")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConversationalTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ConversationalTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteEventOutput:
    boto3_raw_data: "type_defs.DeleteEventOutputTypeDef" = dataclasses.field()

    eventId = field("eventId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteEventOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteEventOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteMemoryRecordOutput:
    boto3_raw_data: "type_defs.DeleteMemoryRecordOutputTypeDef" = dataclasses.field()

    memoryRecordId = field("memoryRecordId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteMemoryRecordOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteMemoryRecordOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCodeInterpreterSessionResponse:
    boto3_raw_data: "type_defs.GetCodeInterpreterSessionResponseTypeDef" = (
        dataclasses.field()
    )

    codeInterpreterIdentifier = field("codeInterpreterIdentifier")
    sessionId = field("sessionId")
    name = field("name")
    createdAt = field("createdAt")
    sessionTimeoutSeconds = field("sessionTimeoutSeconds")
    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCodeInterpreterSessionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCodeInterpreterSessionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResourceApiKeyResponse:
    boto3_raw_data: "type_defs.GetResourceApiKeyResponseTypeDef" = dataclasses.field()

    apiKey = field("apiKey")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetResourceApiKeyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResourceApiKeyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResourceOauth2TokenResponse:
    boto3_raw_data: "type_defs.GetResourceOauth2TokenResponseTypeDef" = (
        dataclasses.field()
    )

    authorizationUrl = field("authorizationUrl")
    accessToken = field("accessToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetResourceOauth2TokenResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResourceOauth2TokenResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetWorkloadAccessTokenForJWTResponse:
    boto3_raw_data: "type_defs.GetWorkloadAccessTokenForJWTResponseTypeDef" = (
        dataclasses.field()
    )

    workloadAccessToken = field("workloadAccessToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetWorkloadAccessTokenForJWTResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetWorkloadAccessTokenForJWTResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetWorkloadAccessTokenForUserIdResponse:
    boto3_raw_data: "type_defs.GetWorkloadAccessTokenForUserIdResponseTypeDef" = (
        dataclasses.field()
    )

    workloadAccessToken = field("workloadAccessToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetWorkloadAccessTokenForUserIdResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetWorkloadAccessTokenForUserIdResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetWorkloadAccessTokenResponse:
    boto3_raw_data: "type_defs.GetWorkloadAccessTokenResponseTypeDef" = (
        dataclasses.field()
    )

    workloadAccessToken = field("workloadAccessToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetWorkloadAccessTokenResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetWorkloadAccessTokenResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InvokeAgentRuntimeResponse:
    boto3_raw_data: "type_defs.InvokeAgentRuntimeResponseTypeDef" = dataclasses.field()

    runtimeSessionId = field("runtimeSessionId")
    mcpSessionId = field("mcpSessionId")
    mcpProtocolVersion = field("mcpProtocolVersion")
    traceId = field("traceId")
    traceParent = field("traceParent")
    traceState = field("traceState")
    baggage = field("baggage")
    contentType = field("contentType")
    response = field("response")
    statusCode = field("statusCode")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InvokeAgentRuntimeResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InvokeAgentRuntimeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListActorsOutput:
    boto3_raw_data: "type_defs.ListActorsOutputTypeDef" = dataclasses.field()

    @cached_property
    def actorSummaries(self):  # pragma: no cover
        return ActorSummary.make_many(self.boto3_raw_data["actorSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListActorsOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListActorsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBrowserSessionsResponse:
    boto3_raw_data: "type_defs.ListBrowserSessionsResponseTypeDef" = dataclasses.field()

    @cached_property
    def items(self):  # pragma: no cover
        return BrowserSessionSummary.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBrowserSessionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBrowserSessionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCodeInterpreterSessionsResponse:
    boto3_raw_data: "type_defs.ListCodeInterpreterSessionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def items(self):  # pragma: no cover
        return CodeInterpreterSessionSummary.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCodeInterpreterSessionsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCodeInterpreterSessionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartCodeInterpreterSessionResponse:
    boto3_raw_data: "type_defs.StartCodeInterpreterSessionResponseTypeDef" = (
        dataclasses.field()
    )

    codeInterpreterIdentifier = field("codeInterpreterIdentifier")
    sessionId = field("sessionId")
    createdAt = field("createdAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartCodeInterpreterSessionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartCodeInterpreterSessionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopBrowserSessionResponse:
    boto3_raw_data: "type_defs.StopBrowserSessionResponseTypeDef" = dataclasses.field()

    browserIdentifier = field("browserIdentifier")
    sessionId = field("sessionId")
    lastUpdatedAt = field("lastUpdatedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopBrowserSessionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopBrowserSessionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopCodeInterpreterSessionResponse:
    boto3_raw_data: "type_defs.StopCodeInterpreterSessionResponseTypeDef" = (
        dataclasses.field()
    )

    codeInterpreterIdentifier = field("codeInterpreterIdentifier")
    sessionId = field("sessionId")
    lastUpdatedAt = field("lastUpdatedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StopCodeInterpreterSessionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopCodeInterpreterSessionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartBrowserSessionRequest:
    boto3_raw_data: "type_defs.StartBrowserSessionRequestTypeDef" = dataclasses.field()

    browserIdentifier = field("browserIdentifier")
    name = field("name")
    sessionTimeoutSeconds = field("sessionTimeoutSeconds")

    @cached_property
    def viewPort(self):  # pragma: no cover
        return ViewPort.make_one(self.boto3_raw_data["viewPort"])

    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartBrowserSessionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartBrowserSessionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListActorsInputPaginate:
    boto3_raw_data: "type_defs.ListActorsInputPaginateTypeDef" = dataclasses.field()

    memoryId = field("memoryId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListActorsInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListActorsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMemoryRecordsInputPaginate:
    boto3_raw_data: "type_defs.ListMemoryRecordsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    memoryId = field("memoryId")
    namespace = field("namespace")
    memoryStrategyId = field("memoryStrategyId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListMemoryRecordsInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMemoryRecordsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSessionsInputPaginate:
    boto3_raw_data: "type_defs.ListSessionsInputPaginateTypeDef" = dataclasses.field()

    memoryId = field("memoryId")
    actorId = field("actorId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSessionsInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSessionsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSessionsOutput:
    boto3_raw_data: "type_defs.ListSessionsOutputTypeDef" = dataclasses.field()

    @cached_property
    def sessionSummaries(self):  # pragma: no cover
        return SessionSummary.make_many(self.boto3_raw_data["sessionSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSessionsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSessionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MemoryRecordSummary:
    boto3_raw_data: "type_defs.MemoryRecordSummaryTypeDef" = dataclasses.field()

    memoryRecordId = field("memoryRecordId")

    @cached_property
    def content(self):  # pragma: no cover
        return MemoryContent.make_one(self.boto3_raw_data["content"])

    memoryStrategyId = field("memoryStrategyId")
    namespaces = field("namespaces")
    createdAt = field("createdAt")
    score = field("score")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MemoryRecordSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MemoryRecordSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MemoryRecord:
    boto3_raw_data: "type_defs.MemoryRecordTypeDef" = dataclasses.field()

    memoryRecordId = field("memoryRecordId")

    @cached_property
    def content(self):  # pragma: no cover
        return MemoryContent.make_one(self.boto3_raw_data["content"])

    memoryStrategyId = field("memoryStrategyId")
    namespaces = field("namespaces")
    createdAt = field("createdAt")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MemoryRecordTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MemoryRecordTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RetrieveMemoryRecordsInputPaginate:
    boto3_raw_data: "type_defs.RetrieveMemoryRecordsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    memoryId = field("memoryId")
    namespace = field("namespace")

    @cached_property
    def searchCriteria(self):  # pragma: no cover
        return SearchCriteria.make_one(self.boto3_raw_data["searchCriteria"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RetrieveMemoryRecordsInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RetrieveMemoryRecordsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RetrieveMemoryRecordsInput:
    boto3_raw_data: "type_defs.RetrieveMemoryRecordsInputTypeDef" = dataclasses.field()

    memoryId = field("memoryId")
    namespace = field("namespace")

    @cached_property
    def searchCriteria(self):  # pragma: no cover
        return SearchCriteria.make_one(self.boto3_raw_data["searchCriteria"])

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RetrieveMemoryRecordsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RetrieveMemoryRecordsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ValidationException:
    boto3_raw_data: "type_defs.ValidationExceptionTypeDef" = dataclasses.field()

    message = field("message")
    reason = field("reason")

    @cached_property
    def fieldList(self):  # pragma: no cover
        return ValidationExceptionField.make_many(self.boto3_raw_data["fieldList"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ValidationExceptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ValidationExceptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateBrowserStreamRequest:
    boto3_raw_data: "type_defs.UpdateBrowserStreamRequestTypeDef" = dataclasses.field()

    browserIdentifier = field("browserIdentifier")
    sessionId = field("sessionId")

    @cached_property
    def streamUpdate(self):  # pragma: no cover
        return StreamUpdate.make_one(self.boto3_raw_data["streamUpdate"])

    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateBrowserStreamRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateBrowserStreamRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ToolArguments:
    boto3_raw_data: "type_defs.ToolArgumentsTypeDef" = dataclasses.field()

    code = field("code")
    language = field("language")
    clearContext = field("clearContext")
    command = field("command")
    path = field("path")
    paths = field("paths")

    @cached_property
    def content(self):  # pragma: no cover
        return InputContentBlock.make_many(self.boto3_raw_data["content"])

    directoryPath = field("directoryPath")
    taskId = field("taskId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ToolArgumentsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ToolArgumentsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEventsInputPaginate:
    boto3_raw_data: "type_defs.ListEventsInputPaginateTypeDef" = dataclasses.field()

    memoryId = field("memoryId")
    sessionId = field("sessionId")
    actorId = field("actorId")
    includePayloads = field("includePayloads")

    @cached_property
    def filter(self):  # pragma: no cover
        return FilterInput.make_one(self.boto3_raw_data["filter"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEventsInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEventsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEventsInput:
    boto3_raw_data: "type_defs.ListEventsInputTypeDef" = dataclasses.field()

    memoryId = field("memoryId")
    sessionId = field("sessionId")
    actorId = field("actorId")
    includePayloads = field("includePayloads")

    @cached_property
    def filter(self):  # pragma: no cover
        return FilterInput.make_one(self.boto3_raw_data["filter"])

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListEventsInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListEventsInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBrowserSessionResponse:
    boto3_raw_data: "type_defs.GetBrowserSessionResponseTypeDef" = dataclasses.field()

    browserIdentifier = field("browserIdentifier")
    sessionId = field("sessionId")
    name = field("name")
    createdAt = field("createdAt")

    @cached_property
    def viewPort(self):  # pragma: no cover
        return ViewPort.make_one(self.boto3_raw_data["viewPort"])

    sessionTimeoutSeconds = field("sessionTimeoutSeconds")
    status = field("status")

    @cached_property
    def streams(self):  # pragma: no cover
        return BrowserSessionStream.make_one(self.boto3_raw_data["streams"])

    sessionReplayArtifact = field("sessionReplayArtifact")
    lastUpdatedAt = field("lastUpdatedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBrowserSessionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBrowserSessionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartBrowserSessionResponse:
    boto3_raw_data: "type_defs.StartBrowserSessionResponseTypeDef" = dataclasses.field()

    browserIdentifier = field("browserIdentifier")
    sessionId = field("sessionId")
    createdAt = field("createdAt")

    @cached_property
    def streams(self):  # pragma: no cover
        return BrowserSessionStream.make_one(self.boto3_raw_data["streams"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartBrowserSessionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartBrowserSessionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateBrowserStreamResponse:
    boto3_raw_data: "type_defs.UpdateBrowserStreamResponseTypeDef" = dataclasses.field()

    browserIdentifier = field("browserIdentifier")
    sessionId = field("sessionId")

    @cached_property
    def streams(self):  # pragma: no cover
        return BrowserSessionStream.make_one(self.boto3_raw_data["streams"])

    updatedAt = field("updatedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateBrowserStreamResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateBrowserStreamResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CodeInterpreterResult:
    boto3_raw_data: "type_defs.CodeInterpreterResultTypeDef" = dataclasses.field()

    @cached_property
    def content(self):  # pragma: no cover
        return ContentBlock.make_many(self.boto3_raw_data["content"])

    @cached_property
    def structuredContent(self):  # pragma: no cover
        return ToolResultStructuredContent.make_one(
            self.boto3_raw_data["structuredContent"]
        )

    isError = field("isError")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CodeInterpreterResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CodeInterpreterResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PayloadTypeOutput:
    boto3_raw_data: "type_defs.PayloadTypeOutputTypeDef" = dataclasses.field()

    @cached_property
    def conversational(self):  # pragma: no cover
        return Conversational.make_one(self.boto3_raw_data["conversational"])

    blob = field("blob")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PayloadTypeOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PayloadTypeOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PayloadType:
    boto3_raw_data: "type_defs.PayloadTypeTypeDef" = dataclasses.field()

    @cached_property
    def conversational(self):  # pragma: no cover
        return Conversational.make_one(self.boto3_raw_data["conversational"])

    blob = field("blob")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PayloadTypeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PayloadTypeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMemoryRecordsOutput:
    boto3_raw_data: "type_defs.ListMemoryRecordsOutputTypeDef" = dataclasses.field()

    @cached_property
    def memoryRecordSummaries(self):  # pragma: no cover
        return MemoryRecordSummary.make_many(
            self.boto3_raw_data["memoryRecordSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMemoryRecordsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMemoryRecordsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RetrieveMemoryRecordsOutput:
    boto3_raw_data: "type_defs.RetrieveMemoryRecordsOutputTypeDef" = dataclasses.field()

    @cached_property
    def memoryRecordSummaries(self):  # pragma: no cover
        return MemoryRecordSummary.make_many(
            self.boto3_raw_data["memoryRecordSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RetrieveMemoryRecordsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RetrieveMemoryRecordsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMemoryRecordOutput:
    boto3_raw_data: "type_defs.GetMemoryRecordOutputTypeDef" = dataclasses.field()

    @cached_property
    def memoryRecord(self):  # pragma: no cover
        return MemoryRecord.make_one(self.boto3_raw_data["memoryRecord"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMemoryRecordOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMemoryRecordOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InvokeCodeInterpreterRequest:
    boto3_raw_data: "type_defs.InvokeCodeInterpreterRequestTypeDef" = (
        dataclasses.field()
    )

    codeInterpreterIdentifier = field("codeInterpreterIdentifier")
    name = field("name")
    sessionId = field("sessionId")

    @cached_property
    def arguments(self):  # pragma: no cover
        return ToolArguments.make_one(self.boto3_raw_data["arguments"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InvokeCodeInterpreterRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InvokeCodeInterpreterRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CodeInterpreterStreamOutput:
    boto3_raw_data: "type_defs.CodeInterpreterStreamOutputTypeDef" = dataclasses.field()

    @cached_property
    def result(self):  # pragma: no cover
        return CodeInterpreterResult.make_one(self.boto3_raw_data["result"])

    @cached_property
    def accessDeniedException(self):  # pragma: no cover
        return AccessDeniedException.make_one(
            self.boto3_raw_data["accessDeniedException"]
        )

    @cached_property
    def conflictException(self):  # pragma: no cover
        return ConflictException.make_one(self.boto3_raw_data["conflictException"])

    @cached_property
    def internalServerException(self):  # pragma: no cover
        return InternalServerException.make_one(
            self.boto3_raw_data["internalServerException"]
        )

    @cached_property
    def resourceNotFoundException(self):  # pragma: no cover
        return ResourceNotFoundException.make_one(
            self.boto3_raw_data["resourceNotFoundException"]
        )

    @cached_property
    def serviceQuotaExceededException(self):  # pragma: no cover
        return ServiceQuotaExceededException.make_one(
            self.boto3_raw_data["serviceQuotaExceededException"]
        )

    @cached_property
    def throttlingException(self):  # pragma: no cover
        return ThrottlingException.make_one(self.boto3_raw_data["throttlingException"])

    @cached_property
    def validationException(self):  # pragma: no cover
        return ValidationException.make_one(self.boto3_raw_data["validationException"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CodeInterpreterStreamOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CodeInterpreterStreamOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Event:
    boto3_raw_data: "type_defs.EventTypeDef" = dataclasses.field()

    memoryId = field("memoryId")
    actorId = field("actorId")
    sessionId = field("sessionId")
    eventId = field("eventId")
    eventTimestamp = field("eventTimestamp")

    @cached_property
    def payload(self):  # pragma: no cover
        return PayloadTypeOutput.make_many(self.boto3_raw_data["payload"])

    @cached_property
    def branch(self):  # pragma: no cover
        return Branch.make_one(self.boto3_raw_data["branch"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EventTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EventTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InvokeCodeInterpreterResponse:
    boto3_raw_data: "type_defs.InvokeCodeInterpreterResponseTypeDef" = (
        dataclasses.field()
    )

    sessionId = field("sessionId")
    stream = field("stream")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.InvokeCodeInterpreterResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InvokeCodeInterpreterResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEventOutput:
    boto3_raw_data: "type_defs.CreateEventOutputTypeDef" = dataclasses.field()

    @cached_property
    def event(self):  # pragma: no cover
        return Event.make_one(self.boto3_raw_data["event"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateEventOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEventOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEventOutput:
    boto3_raw_data: "type_defs.GetEventOutputTypeDef" = dataclasses.field()

    @cached_property
    def event(self):  # pragma: no cover
        return Event.make_one(self.boto3_raw_data["event"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetEventOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetEventOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEventsOutput:
    boto3_raw_data: "type_defs.ListEventsOutputTypeDef" = dataclasses.field()

    @cached_property
    def events(self):  # pragma: no cover
        return Event.make_many(self.boto3_raw_data["events"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListEventsOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEventsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEventInput:
    boto3_raw_data: "type_defs.CreateEventInputTypeDef" = dataclasses.field()

    memoryId = field("memoryId")
    actorId = field("actorId")
    eventTimestamp = field("eventTimestamp")
    payload = field("payload")
    sessionId = field("sessionId")

    @cached_property
    def branch(self):  # pragma: no cover
        return Branch.make_one(self.boto3_raw_data["branch"])

    clientToken = field("clientToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateEventInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEventInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
