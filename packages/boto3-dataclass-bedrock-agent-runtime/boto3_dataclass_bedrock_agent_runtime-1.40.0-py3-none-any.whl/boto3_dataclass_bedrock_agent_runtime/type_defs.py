# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_bedrock_agent_runtime import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class S3Identifier:
    boto3_raw_data: "type_defs.S3IdentifierTypeDef" = dataclasses.field()

    s3BucketName = field("s3BucketName")
    s3ObjectKey = field("s3ObjectKey")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3IdentifierTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3IdentifierTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


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
class ActionGroupExecutor:
    boto3_raw_data: "type_defs.ActionGroupExecutorTypeDef" = dataclasses.field()

    customControl = field("customControl")
    lambda_ = field("lambda")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ActionGroupExecutorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActionGroupExecutorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Parameter:
    boto3_raw_data: "type_defs.ParameterTypeDef" = dataclasses.field()

    name = field("name")
    type = field("type")
    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ParameterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ParameterTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalyzePromptEvent:
    boto3_raw_data: "type_defs.AnalyzePromptEventTypeDef" = dataclasses.field()

    message = field("message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnalyzePromptEventTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnalyzePromptEventTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApiParameter:
    boto3_raw_data: "type_defs.ApiParameterTypeDef" = dataclasses.field()

    name = field("name")
    type = field("type")
    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ApiParameterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ApiParameterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BadGatewayException:
    boto3_raw_data: "type_defs.BadGatewayExceptionTypeDef" = dataclasses.field()

    message = field("message")
    resourceName = field("resourceName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BadGatewayExceptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BadGatewayExceptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PerformanceConfiguration:
    boto3_raw_data: "type_defs.PerformanceConfigurationTypeDef" = dataclasses.field()

    latency = field("latency")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PerformanceConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PerformanceConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BedrockRerankingModelConfiguration:
    boto3_raw_data: "type_defs.BedrockRerankingModelConfigurationTypeDef" = (
        dataclasses.field()
    )

    modelArn = field("modelArn")
    additionalModelRequestFields = field("additionalModelRequestFields")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BedrockRerankingModelConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BedrockRerankingModelConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Caller:
    boto3_raw_data: "type_defs.CallerTypeDef" = dataclasses.field()

    agentAliasArn = field("agentAliasArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CallerTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CallerTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CodeInterpreterInvocationInput:
    boto3_raw_data: "type_defs.CodeInterpreterInvocationInputTypeDef" = (
        dataclasses.field()
    )

    code = field("code")
    files = field("files")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CodeInterpreterInvocationInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CodeInterpreterInvocationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CollaboratorConfiguration:
    boto3_raw_data: "type_defs.CollaboratorConfigurationTypeDef" = dataclasses.field()

    collaboratorInstruction = field("collaboratorInstruction")
    collaboratorName = field("collaboratorName")
    agentAliasArn = field("agentAliasArn")
    relayConversationHistory = field("relayConversationHistory")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CollaboratorConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CollaboratorConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailConfigurationWithArn:
    boto3_raw_data: "type_defs.GuardrailConfigurationWithArnTypeDef" = (
        dataclasses.field()
    )

    guardrailIdentifier = field("guardrailIdentifier")
    guardrailVersion = field("guardrailVersion")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GuardrailConfigurationWithArnTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GuardrailConfigurationWithArnTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SatisfiedCondition:
    boto3_raw_data: "type_defs.SatisfiedConditionTypeDef" = dataclasses.field()

    conditionName = field("conditionName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SatisfiedConditionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SatisfiedConditionTypeDef"]
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
class ContentBlock:
    boto3_raw_data: "type_defs.ContentBlockTypeDef" = dataclasses.field()

    text = field("text")

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
class CreateInvocationRequest:
    boto3_raw_data: "type_defs.CreateInvocationRequestTypeDef" = dataclasses.field()

    sessionIdentifier = field("sessionIdentifier")
    description = field("description")
    invocationId = field("invocationId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateInvocationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateInvocationRequestTypeDef"]
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
class CreateSessionRequest:
    boto3_raw_data: "type_defs.CreateSessionRequestTypeDef" = dataclasses.field()

    encryptionKeyArn = field("encryptionKeyArn")
    sessionMetadata = field("sessionMetadata")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSessionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSessionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomOrchestrationTraceEvent:
    boto3_raw_data: "type_defs.CustomOrchestrationTraceEventTypeDef" = (
        dataclasses.field()
    )

    text = field("text")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CustomOrchestrationTraceEventTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomOrchestrationTraceEventTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OrchestrationExecutor:
    boto3_raw_data: "type_defs.OrchestrationExecutorTypeDef" = dataclasses.field()

    lambda_ = field("lambda")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OrchestrationExecutorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OrchestrationExecutorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAgentMemoryRequest:
    boto3_raw_data: "type_defs.DeleteAgentMemoryRequestTypeDef" = dataclasses.field()

    agentAliasId = field("agentAliasId")
    agentId = field("agentId")
    memoryId = field("memoryId")
    sessionId = field("sessionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAgentMemoryRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAgentMemoryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSessionRequest:
    boto3_raw_data: "type_defs.DeleteSessionRequestTypeDef" = dataclasses.field()

    sessionIdentifier = field("sessionIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteSessionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSessionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DependencyFailedException:
    boto3_raw_data: "type_defs.DependencyFailedExceptionTypeDef" = dataclasses.field()

    message = field("message")
    resourceName = field("resourceName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DependencyFailedExceptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DependencyFailedExceptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EndSessionRequest:
    boto3_raw_data: "type_defs.EndSessionRequestTypeDef" = dataclasses.field()

    sessionIdentifier = field("sessionIdentifier")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EndSessionRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EndSessionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3ObjectDoc:
    boto3_raw_data: "type_defs.S3ObjectDocTypeDef" = dataclasses.field()

    uri = field("uri")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3ObjectDocTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3ObjectDocTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailConfiguration:
    boto3_raw_data: "type_defs.GuardrailConfigurationTypeDef" = dataclasses.field()

    guardrailId = field("guardrailId")
    guardrailVersion = field("guardrailVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GuardrailConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GuardrailConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PromptTemplate:
    boto3_raw_data: "type_defs.PromptTemplateTypeDef" = dataclasses.field()

    textPromptTemplate = field("textPromptTemplate")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PromptTemplateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PromptTemplateTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FieldForReranking:
    boto3_raw_data: "type_defs.FieldForRerankingTypeDef" = dataclasses.field()

    fieldName = field("fieldName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FieldForRerankingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FieldForRerankingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OutputFile:
    boto3_raw_data: "type_defs.OutputFileTypeDef" = dataclasses.field()

    bytes = field("bytes")
    name = field("name")
    type = field("type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OutputFileTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OutputFileTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3ObjectFile:
    boto3_raw_data: "type_defs.S3ObjectFileTypeDef" = dataclasses.field()

    uri = field("uri")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3ObjectFileTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3ObjectFileTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FilterAttribute:
    boto3_raw_data: "type_defs.FilterAttributeTypeDef" = dataclasses.field()

    key = field("key")
    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FilterAttributeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FilterAttributeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FlowCompletionEvent:
    boto3_raw_data: "type_defs.FlowCompletionEventTypeDef" = dataclasses.field()

    completionReason = field("completionReason")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FlowCompletionEventTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FlowCompletionEventTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FlowExecutionContent:
    boto3_raw_data: "type_defs.FlowExecutionContentTypeDef" = dataclasses.field()

    document = field("document")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FlowExecutionContentTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FlowExecutionContentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FlowExecutionError:
    boto3_raw_data: "type_defs.FlowExecutionErrorTypeDef" = dataclasses.field()

    error = field("error")
    message = field("message")
    nodeName = field("nodeName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FlowExecutionErrorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FlowExecutionErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FlowFailureEvent:
    boto3_raw_data: "type_defs.FlowFailureEventTypeDef" = dataclasses.field()

    errorCode = field("errorCode")
    errorMessage = field("errorMessage")
    timestamp = field("timestamp")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FlowFailureEventTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FlowFailureEventTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NodeFailureEvent:
    boto3_raw_data: "type_defs.NodeFailureEventTypeDef" = dataclasses.field()

    errorCode = field("errorCode")
    errorMessage = field("errorMessage")
    nodeName = field("nodeName")
    timestamp = field("timestamp")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NodeFailureEventTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NodeFailureEventTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FlowExecutionSummary:
    boto3_raw_data: "type_defs.FlowExecutionSummaryTypeDef" = dataclasses.field()

    createdAt = field("createdAt")
    executionArn = field("executionArn")
    flowAliasIdentifier = field("flowAliasIdentifier")
    flowIdentifier = field("flowIdentifier")
    flowVersion = field("flowVersion")
    status = field("status")
    endedAt = field("endedAt")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FlowExecutionSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FlowExecutionSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FlowInputContent:
    boto3_raw_data: "type_defs.FlowInputContentTypeDef" = dataclasses.field()

    document = field("document")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FlowInputContentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FlowInputContentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FlowMultiTurnInputContent:
    boto3_raw_data: "type_defs.FlowMultiTurnInputContentTypeDef" = dataclasses.field()

    document = field("document")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FlowMultiTurnInputContentTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FlowMultiTurnInputContentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FlowOutputContent:
    boto3_raw_data: "type_defs.FlowOutputContentTypeDef" = dataclasses.field()

    document = field("document")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FlowOutputContentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FlowOutputContentTypeDef"]
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
    reason = field("reason")

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
class ValidationException:
    boto3_raw_data: "type_defs.ValidationExceptionTypeDef" = dataclasses.field()

    message = field("message")

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
class FlowTraceCondition:
    boto3_raw_data: "type_defs.FlowTraceConditionTypeDef" = dataclasses.field()

    conditionName = field("conditionName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FlowTraceConditionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FlowTraceConditionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FlowTraceNodeActionEvent:
    boto3_raw_data: "type_defs.FlowTraceNodeActionEventTypeDef" = dataclasses.field()

    nodeName = field("nodeName")
    operationName = field("operationName")
    requestId = field("requestId")
    serviceName = field("serviceName")
    timestamp = field("timestamp")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FlowTraceNodeActionEventTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FlowTraceNodeActionEventTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FlowTraceNodeInputContent:
    boto3_raw_data: "type_defs.FlowTraceNodeInputContentTypeDef" = dataclasses.field()

    document = field("document")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FlowTraceNodeInputContentTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FlowTraceNodeInputContentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FlowTraceNodeOutputContent:
    boto3_raw_data: "type_defs.FlowTraceNodeOutputContentTypeDef" = dataclasses.field()

    document = field("document")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FlowTraceNodeOutputContentTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FlowTraceNodeOutputContentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ParameterDetail:
    boto3_raw_data: "type_defs.ParameterDetailTypeDef" = dataclasses.field()

    type = field("type")
    description = field("description")
    required = field("required")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ParameterDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ParameterDetailTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FunctionParameter:
    boto3_raw_data: "type_defs.FunctionParameterTypeDef" = dataclasses.field()

    name = field("name")
    type = field("type")
    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FunctionParameterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FunctionParameterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryGenerationInput:
    boto3_raw_data: "type_defs.QueryGenerationInputTypeDef" = dataclasses.field()

    text = field("text")
    type = field("type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.QueryGenerationInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QueryGenerationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GeneratedQuery:
    boto3_raw_data: "type_defs.GeneratedQueryTypeDef" = dataclasses.field()

    sql = field("sql")
    type = field("type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GeneratedQueryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GeneratedQueryTypeDef"]],
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
class GetAgentMemoryRequest:
    boto3_raw_data: "type_defs.GetAgentMemoryRequestTypeDef" = dataclasses.field()

    agentAliasId = field("agentAliasId")
    agentId = field("agentId")
    memoryId = field("memoryId")
    memoryType = field("memoryType")
    maxItems = field("maxItems")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAgentMemoryRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAgentMemoryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetExecutionFlowSnapshotRequest:
    boto3_raw_data: "type_defs.GetExecutionFlowSnapshotRequestTypeDef" = (
        dataclasses.field()
    )

    executionIdentifier = field("executionIdentifier")
    flowAliasIdentifier = field("flowAliasIdentifier")
    flowIdentifier = field("flowIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetExecutionFlowSnapshotRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetExecutionFlowSnapshotRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFlowExecutionRequest:
    boto3_raw_data: "type_defs.GetFlowExecutionRequestTypeDef" = dataclasses.field()

    executionIdentifier = field("executionIdentifier")
    flowAliasIdentifier = field("flowAliasIdentifier")
    flowIdentifier = field("flowIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetFlowExecutionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFlowExecutionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetInvocationStepRequest:
    boto3_raw_data: "type_defs.GetInvocationStepRequestTypeDef" = dataclasses.field()

    invocationIdentifier = field("invocationIdentifier")
    invocationStepId = field("invocationStepId")
    sessionIdentifier = field("sessionIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetInvocationStepRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetInvocationStepRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSessionRequest:
    boto3_raw_data: "type_defs.GetSessionRequestTypeDef" = dataclasses.field()

    sessionIdentifier = field("sessionIdentifier")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetSessionRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSessionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailContentFilter:
    boto3_raw_data: "type_defs.GuardrailContentFilterTypeDef" = dataclasses.field()

    action = field("action")
    confidence = field("confidence")
    type = field("type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GuardrailContentFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GuardrailContentFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailCustomWord:
    boto3_raw_data: "type_defs.GuardrailCustomWordTypeDef" = dataclasses.field()

    action = field("action")
    match = field("match")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GuardrailCustomWordTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GuardrailCustomWordTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailEvent:
    boto3_raw_data: "type_defs.GuardrailEventTypeDef" = dataclasses.field()

    action = field("action")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GuardrailEventTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GuardrailEventTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailManagedWord:
    boto3_raw_data: "type_defs.GuardrailManagedWordTypeDef" = dataclasses.field()

    action = field("action")
    match = field("match")
    type = field("type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GuardrailManagedWordTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GuardrailManagedWordTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailPiiEntityFilter:
    boto3_raw_data: "type_defs.GuardrailPiiEntityFilterTypeDef" = dataclasses.field()

    action = field("action")
    match = field("match")
    type = field("type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GuardrailPiiEntityFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GuardrailPiiEntityFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailRegexFilter:
    boto3_raw_data: "type_defs.GuardrailRegexFilterTypeDef" = dataclasses.field()

    action = field("action")
    match = field("match")
    name = field("name")
    regex = field("regex")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GuardrailRegexFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GuardrailRegexFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailTopic:
    boto3_raw_data: "type_defs.GuardrailTopicTypeDef" = dataclasses.field()

    action = field("action")
    name = field("name")
    type = field("type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GuardrailTopicTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GuardrailTopicTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImageInputSourceOutput:
    boto3_raw_data: "type_defs.ImageInputSourceOutputTypeDef" = dataclasses.field()

    bytes = field("bytes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImageInputSourceOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImageInputSourceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3Location:
    boto3_raw_data: "type_defs.S3LocationTypeDef" = dataclasses.field()

    uri = field("uri")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3LocationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3LocationTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetadataAttributeSchema:
    boto3_raw_data: "type_defs.MetadataAttributeSchemaTypeDef" = dataclasses.field()

    description = field("description")
    key = field("key")
    type = field("type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MetadataAttributeSchemaTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MetadataAttributeSchemaTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TextInferenceConfig:
    boto3_raw_data: "type_defs.TextInferenceConfigTypeDef" = dataclasses.field()

    maxTokens = field("maxTokens")
    stopSequences = field("stopSequences")
    temperature = field("temperature")
    topP = field("topP")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TextInferenceConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TextInferenceConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InferenceConfigurationOutput:
    boto3_raw_data: "type_defs.InferenceConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    maximumLength = field("maximumLength")
    stopSequences = field("stopSequences")
    temperature = field("temperature")
    topK = field("topK")
    topP = field("topP")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InferenceConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InferenceConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InferenceConfiguration:
    boto3_raw_data: "type_defs.InferenceConfigurationTypeDef" = dataclasses.field()

    maximumLength = field("maximumLength")
    stopSequences = field("stopSequences")
    temperature = field("temperature")
    topK = field("topK")
    topP = field("topP")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InferenceConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InferenceConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TextPrompt:
    boto3_raw_data: "type_defs.TextPromptTypeDef" = dataclasses.field()

    text = field("text")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TextPromptTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TextPromptTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KnowledgeBaseLookupInput:
    boto3_raw_data: "type_defs.KnowledgeBaseLookupInputTypeDef" = dataclasses.field()

    knowledgeBaseId = field("knowledgeBaseId")
    text = field("text")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KnowledgeBaseLookupInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KnowledgeBaseLookupInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InvocationStepSummary:
    boto3_raw_data: "type_defs.InvocationStepSummaryTypeDef" = dataclasses.field()

    invocationId = field("invocationId")
    invocationStepId = field("invocationStepId")
    invocationStepTime = field("invocationStepTime")
    sessionId = field("sessionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InvocationStepSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InvocationStepSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InvocationSummary:
    boto3_raw_data: "type_defs.InvocationSummaryTypeDef" = dataclasses.field()

    createdAt = field("createdAt")
    invocationId = field("invocationId")
    sessionId = field("sessionId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InvocationSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InvocationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PromptCreationConfigurations:
    boto3_raw_data: "type_defs.PromptCreationConfigurationsTypeDef" = (
        dataclasses.field()
    )

    excludePreviousThinkingSteps = field("excludePreviousThinkingSteps")
    previousConversationTurnsToInclude = field("previousConversationTurnsToInclude")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PromptCreationConfigurationsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PromptCreationConfigurationsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StreamingConfigurations:
    boto3_raw_data: "type_defs.StreamingConfigurationsTypeDef" = dataclasses.field()

    applyGuardrailInterval = field("applyGuardrailInterval")
    streamFinalResponse = field("streamFinalResponse")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StreamingConfigurationsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StreamingConfigurationsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KnowledgeBaseQuery:
    boto3_raw_data: "type_defs.KnowledgeBaseQueryTypeDef" = dataclasses.field()

    text = field("text")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KnowledgeBaseQueryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KnowledgeBaseQueryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFlowExecutionEventsRequest:
    boto3_raw_data: "type_defs.ListFlowExecutionEventsRequestTypeDef" = (
        dataclasses.field()
    )

    eventType = field("eventType")
    executionIdentifier = field("executionIdentifier")
    flowAliasIdentifier = field("flowAliasIdentifier")
    flowIdentifier = field("flowIdentifier")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListFlowExecutionEventsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFlowExecutionEventsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFlowExecutionsRequest:
    boto3_raw_data: "type_defs.ListFlowExecutionsRequestTypeDef" = dataclasses.field()

    flowIdentifier = field("flowIdentifier")
    flowAliasIdentifier = field("flowAliasIdentifier")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFlowExecutionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFlowExecutionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInvocationStepsRequest:
    boto3_raw_data: "type_defs.ListInvocationStepsRequestTypeDef" = dataclasses.field()

    sessionIdentifier = field("sessionIdentifier")
    invocationIdentifier = field("invocationIdentifier")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListInvocationStepsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInvocationStepsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInvocationsRequest:
    boto3_raw_data: "type_defs.ListInvocationsRequestTypeDef" = dataclasses.field()

    sessionIdentifier = field("sessionIdentifier")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListInvocationsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInvocationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSessionsRequest:
    boto3_raw_data: "type_defs.ListSessionsRequestTypeDef" = dataclasses.field()

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSessionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSessionsRequestTypeDef"]
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

    createdAt = field("createdAt")
    lastUpdatedAt = field("lastUpdatedAt")
    sessionArn = field("sessionArn")
    sessionId = field("sessionId")
    sessionStatus = field("sessionStatus")

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
class ListTagsForResourceRequest:
    boto3_raw_data: "type_defs.ListTagsForResourceRequestTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")

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
class MemorySessionSummary:
    boto3_raw_data: "type_defs.MemorySessionSummaryTypeDef" = dataclasses.field()

    memoryId = field("memoryId")
    sessionExpiryTime = field("sessionExpiryTime")
    sessionId = field("sessionId")
    sessionStartTime = field("sessionStartTime")
    summaryText = field("summaryText")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MemorySessionSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MemorySessionSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Usage:
    boto3_raw_data: "type_defs.UsageTypeDef" = dataclasses.field()

    inputTokens = field("inputTokens")
    outputTokens = field("outputTokens")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UsageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UsageTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModelNotReadyException:
    boto3_raw_data: "type_defs.ModelNotReadyExceptionTypeDef" = dataclasses.field()

    message = field("message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModelNotReadyExceptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModelNotReadyExceptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NodeExecutionContent:
    boto3_raw_data: "type_defs.NodeExecutionContentTypeDef" = dataclasses.field()

    document = field("document")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NodeExecutionContentTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NodeExecutionContentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RepromptResponse:
    boto3_raw_data: "type_defs.RepromptResponseTypeDef" = dataclasses.field()

    source = field("source")
    text = field("text")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RepromptResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RepromptResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryTransformationConfiguration:
    boto3_raw_data: "type_defs.QueryTransformationConfigurationTypeDef" = (
        dataclasses.field()
    )

    type = field("type")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.QueryTransformationConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QueryTransformationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RawResponse:
    boto3_raw_data: "type_defs.RawResponseTypeDef" = dataclasses.field()

    content = field("content")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RawResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RawResponseTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Rationale:
    boto3_raw_data: "type_defs.RationaleTypeDef" = dataclasses.field()

    text = field("text")
    traceId = field("traceId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RationaleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RationaleTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PostProcessingParsedResponse:
    boto3_raw_data: "type_defs.PostProcessingParsedResponseTypeDef" = (
        dataclasses.field()
    )

    text = field("text")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PostProcessingParsedResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PostProcessingParsedResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PreProcessingParsedResponse:
    boto3_raw_data: "type_defs.PreProcessingParsedResponseTypeDef" = dataclasses.field()

    isValid = field("isValid")
    rationale = field("rationale")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PreProcessingParsedResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PreProcessingParsedResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReasoningTextBlock:
    boto3_raw_data: "type_defs.ReasoningTextBlockTypeDef" = dataclasses.field()

    text = field("text")
    signature = field("signature")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReasoningTextBlockTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReasoningTextBlockTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RerankTextDocument:
    boto3_raw_data: "type_defs.RerankTextDocumentTypeDef" = dataclasses.field()

    text = field("text")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RerankTextDocumentTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RerankTextDocumentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RetrievalResultConfluenceLocation:
    boto3_raw_data: "type_defs.RetrievalResultConfluenceLocationTypeDef" = (
        dataclasses.field()
    )

    url = field("url")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RetrievalResultConfluenceLocationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RetrievalResultConfluenceLocationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RetrievalResultContentColumn:
    boto3_raw_data: "type_defs.RetrievalResultContentColumnTypeDef" = (
        dataclasses.field()
    )

    columnName = field("columnName")
    columnValue = field("columnValue")
    type = field("type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RetrievalResultContentColumnTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RetrievalResultContentColumnTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RetrievalResultCustomDocumentLocation:
    boto3_raw_data: "type_defs.RetrievalResultCustomDocumentLocationTypeDef" = (
        dataclasses.field()
    )

    id = field("id")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RetrievalResultCustomDocumentLocationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RetrievalResultCustomDocumentLocationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RetrievalResultKendraDocumentLocation:
    boto3_raw_data: "type_defs.RetrievalResultKendraDocumentLocationTypeDef" = (
        dataclasses.field()
    )

    uri = field("uri")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RetrievalResultKendraDocumentLocationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RetrievalResultKendraDocumentLocationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RetrievalResultS3Location:
    boto3_raw_data: "type_defs.RetrievalResultS3LocationTypeDef" = dataclasses.field()

    uri = field("uri")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RetrievalResultS3LocationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RetrievalResultS3LocationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RetrievalResultSalesforceLocation:
    boto3_raw_data: "type_defs.RetrievalResultSalesforceLocationTypeDef" = (
        dataclasses.field()
    )

    url = field("url")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RetrievalResultSalesforceLocationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RetrievalResultSalesforceLocationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RetrievalResultSharePointLocation:
    boto3_raw_data: "type_defs.RetrievalResultSharePointLocationTypeDef" = (
        dataclasses.field()
    )

    url = field("url")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RetrievalResultSharePointLocationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RetrievalResultSharePointLocationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RetrievalResultSqlLocation:
    boto3_raw_data: "type_defs.RetrievalResultSqlLocationTypeDef" = dataclasses.field()

    query = field("query")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RetrievalResultSqlLocationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RetrievalResultSqlLocationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RetrievalResultWebLocation:
    boto3_raw_data: "type_defs.RetrievalResultWebLocationTypeDef" = dataclasses.field()

    url = field("url")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RetrievalResultWebLocationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RetrievalResultWebLocationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RetrieveAndGenerateInput:
    boto3_raw_data: "type_defs.RetrieveAndGenerateInputTypeDef" = dataclasses.field()

    text = field("text")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RetrieveAndGenerateInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RetrieveAndGenerateInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RetrieveAndGenerateOutputEvent:
    boto3_raw_data: "type_defs.RetrieveAndGenerateOutputEventTypeDef" = (
        dataclasses.field()
    )

    text = field("text")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RetrieveAndGenerateOutputEventTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RetrieveAndGenerateOutputEventTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RetrieveAndGenerateOutput:
    boto3_raw_data: "type_defs.RetrieveAndGenerateOutputTypeDef" = dataclasses.field()

    text = field("text")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RetrieveAndGenerateOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RetrieveAndGenerateOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RetrieveAndGenerateSessionConfiguration:
    boto3_raw_data: "type_defs.RetrieveAndGenerateSessionConfigurationTypeDef" = (
        dataclasses.field()
    )

    kmsKeyArn = field("kmsKeyArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RetrieveAndGenerateSessionConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RetrieveAndGenerateSessionConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Span:
    boto3_raw_data: "type_defs.SpanTypeDef" = dataclasses.field()

    end = field("end")
    start = field("start")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SpanTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SpanTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopFlowExecutionRequest:
    boto3_raw_data: "type_defs.StopFlowExecutionRequestTypeDef" = dataclasses.field()

    executionIdentifier = field("executionIdentifier")
    flowAliasIdentifier = field("flowAliasIdentifier")
    flowIdentifier = field("flowIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopFlowExecutionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopFlowExecutionRequestTypeDef"]
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

    resourceArn = field("resourceArn")
    tags = field("tags")

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
class TextToSqlKnowledgeBaseConfiguration:
    boto3_raw_data: "type_defs.TextToSqlKnowledgeBaseConfigurationTypeDef" = (
        dataclasses.field()
    )

    knowledgeBaseArn = field("knowledgeBaseArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.TextToSqlKnowledgeBaseConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TextToSqlKnowledgeBaseConfigurationTypeDef"]
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

    resourceArn = field("resourceArn")
    tagKeys = field("tagKeys")

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
class UpdateSessionRequest:
    boto3_raw_data: "type_defs.UpdateSessionRequestTypeDef" = dataclasses.field()

    sessionIdentifier = field("sessionIdentifier")
    sessionMetadata = field("sessionMetadata")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateSessionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSessionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VectorSearchBedrockRerankingModelConfiguration:
    boto3_raw_data: (
        "type_defs.VectorSearchBedrockRerankingModelConfigurationTypeDef"
    ) = dataclasses.field()

    modelArn = field("modelArn")
    additionalModelRequestFields = field("additionalModelRequestFields")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.VectorSearchBedrockRerankingModelConfigurationTypeDef"
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
                "type_defs.VectorSearchBedrockRerankingModelConfigurationTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class APISchema:
    boto3_raw_data: "type_defs.APISchemaTypeDef" = dataclasses.field()

    payload = field("payload")

    @cached_property
    def s3(self):  # pragma: no cover
        return S3Identifier.make_one(self.boto3_raw_data["s3"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.APISchemaTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.APISchemaTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PropertyParameters:
    boto3_raw_data: "type_defs.PropertyParametersTypeDef" = dataclasses.field()

    @cached_property
    def properties(self):  # pragma: no cover
        return Parameter.make_many(self.boto3_raw_data["properties"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PropertyParametersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PropertyParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RequestBody:
    boto3_raw_data: "type_defs.RequestBodyTypeDef" = dataclasses.field()

    content = field("content")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RequestBodyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RequestBodyTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BedrockModelConfigurations:
    boto3_raw_data: "type_defs.BedrockModelConfigurationsTypeDef" = dataclasses.field()

    @cached_property
    def performanceConfig(self):  # pragma: no cover
        return PerformanceConfiguration.make_one(
            self.boto3_raw_data["performanceConfig"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BedrockModelConfigurationsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BedrockModelConfigurationsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InlineBedrockModelConfigurations:
    boto3_raw_data: "type_defs.InlineBedrockModelConfigurationsTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def performanceConfig(self):  # pragma: no cover
        return PerformanceConfiguration.make_one(
            self.boto3_raw_data["performanceConfig"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.InlineBedrockModelConfigurationsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InlineBedrockModelConfigurationsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModelPerformanceConfiguration:
    boto3_raw_data: "type_defs.ModelPerformanceConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def performanceConfig(self):  # pragma: no cover
        return PerformanceConfiguration.make_one(
            self.boto3_raw_data["performanceConfig"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ModelPerformanceConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModelPerformanceConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BedrockRerankingConfiguration:
    boto3_raw_data: "type_defs.BedrockRerankingConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def modelConfiguration(self):  # pragma: no cover
        return BedrockRerankingModelConfiguration.make_one(
            self.boto3_raw_data["modelConfiguration"]
        )

    numberOfResults = field("numberOfResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BedrockRerankingConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BedrockRerankingConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ByteContentDoc:
    boto3_raw_data: "type_defs.ByteContentDocTypeDef" = dataclasses.field()

    contentType = field("contentType")
    data = field("data")
    identifier = field("identifier")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ByteContentDocTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ByteContentDocTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ByteContentFile:
    boto3_raw_data: "type_defs.ByteContentFileTypeDef" = dataclasses.field()

    data = field("data")
    mediaType = field("mediaType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ByteContentFileTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ByteContentFileTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImageInputSource:
    boto3_raw_data: "type_defs.ImageInputSourceTypeDef" = dataclasses.field()

    bytes = field("bytes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImageInputSourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImageInputSourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConditionResultEvent:
    boto3_raw_data: "type_defs.ConditionResultEventTypeDef" = dataclasses.field()

    nodeName = field("nodeName")

    @cached_property
    def satisfiedConditions(self):  # pragma: no cover
        return SatisfiedCondition.make_many(self.boto3_raw_data["satisfiedConditions"])

    timestamp = field("timestamp")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConditionResultEventTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConditionResultEventTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Message:
    boto3_raw_data: "type_defs.MessageTypeDef" = dataclasses.field()

    @cached_property
    def content(self):  # pragma: no cover
        return ContentBlock.make_many(self.boto3_raw_data["content"])

    role = field("role")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MessageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MessageTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateInvocationResponse:
    boto3_raw_data: "type_defs.CreateInvocationResponseTypeDef" = dataclasses.field()

    createdAt = field("createdAt")
    invocationId = field("invocationId")
    sessionId = field("sessionId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateInvocationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateInvocationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSessionResponse:
    boto3_raw_data: "type_defs.CreateSessionResponseTypeDef" = dataclasses.field()

    createdAt = field("createdAt")
    sessionArn = field("sessionArn")
    sessionId = field("sessionId")
    sessionStatus = field("sessionStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSessionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSessionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EndSessionResponse:
    boto3_raw_data: "type_defs.EndSessionResponseTypeDef" = dataclasses.field()

    sessionArn = field("sessionArn")
    sessionId = field("sessionId")
    sessionStatus = field("sessionStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EndSessionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EndSessionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetExecutionFlowSnapshotResponse:
    boto3_raw_data: "type_defs.GetExecutionFlowSnapshotResponseTypeDef" = (
        dataclasses.field()
    )

    customerEncryptionKeyArn = field("customerEncryptionKeyArn")
    definition = field("definition")
    executionRoleArn = field("executionRoleArn")
    flowAliasIdentifier = field("flowAliasIdentifier")
    flowIdentifier = field("flowIdentifier")
    flowVersion = field("flowVersion")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetExecutionFlowSnapshotResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetExecutionFlowSnapshotResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSessionResponse:
    boto3_raw_data: "type_defs.GetSessionResponseTypeDef" = dataclasses.field()

    createdAt = field("createdAt")
    encryptionKeyArn = field("encryptionKeyArn")
    lastUpdatedAt = field("lastUpdatedAt")
    sessionArn = field("sessionArn")
    sessionId = field("sessionId")
    sessionMetadata = field("sessionMetadata")
    sessionStatus = field("sessionStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSessionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSessionResponseTypeDef"]
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

    tags = field("tags")

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
class PutInvocationStepResponse:
    boto3_raw_data: "type_defs.PutInvocationStepResponseTypeDef" = dataclasses.field()

    invocationStepId = field("invocationStepId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutInvocationStepResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutInvocationStepResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartFlowExecutionResponse:
    boto3_raw_data: "type_defs.StartFlowExecutionResponseTypeDef" = dataclasses.field()

    executionArn = field("executionArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartFlowExecutionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartFlowExecutionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopFlowExecutionResponse:
    boto3_raw_data: "type_defs.StopFlowExecutionResponseTypeDef" = dataclasses.field()

    executionArn = field("executionArn")
    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopFlowExecutionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopFlowExecutionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSessionResponse:
    boto3_raw_data: "type_defs.UpdateSessionResponseTypeDef" = dataclasses.field()

    createdAt = field("createdAt")
    lastUpdatedAt = field("lastUpdatedAt")
    sessionArn = field("sessionArn")
    sessionId = field("sessionId")
    sessionStatus = field("sessionStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateSessionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSessionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomOrchestrationTrace:
    boto3_raw_data: "type_defs.CustomOrchestrationTraceTypeDef" = dataclasses.field()

    @cached_property
    def event(self):  # pragma: no cover
        return CustomOrchestrationTraceEvent.make_one(self.boto3_raw_data["event"])

    traceId = field("traceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CustomOrchestrationTraceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomOrchestrationTraceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomOrchestration:
    boto3_raw_data: "type_defs.CustomOrchestrationTypeDef" = dataclasses.field()

    @cached_property
    def executor(self):  # pragma: no cover
        return OrchestrationExecutor.make_one(self.boto3_raw_data["executor"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CustomOrchestrationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomOrchestrationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RerankingMetadataSelectiveModeConfiguration:
    boto3_raw_data: "type_defs.RerankingMetadataSelectiveModeConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def fieldsToExclude(self):  # pragma: no cover
        return FieldForReranking.make_many(self.boto3_raw_data["fieldsToExclude"])

    @cached_property
    def fieldsToInclude(self):  # pragma: no cover
        return FieldForReranking.make_many(self.boto3_raw_data["fieldsToInclude"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RerankingMetadataSelectiveModeConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RerankingMetadataSelectiveModeConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FilePart:
    boto3_raw_data: "type_defs.FilePartTypeDef" = dataclasses.field()

    @cached_property
    def files(self):  # pragma: no cover
        return OutputFile.make_many(self.boto3_raw_data["files"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FilePartTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FilePartTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InlineAgentFilePart:
    boto3_raw_data: "type_defs.InlineAgentFilePartTypeDef" = dataclasses.field()

    @cached_property
    def files(self):  # pragma: no cover
        return OutputFile.make_many(self.boto3_raw_data["files"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InlineAgentFilePartTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InlineAgentFilePartTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RetrievalFilterPaginator:
    boto3_raw_data: "type_defs.RetrievalFilterPaginatorTypeDef" = dataclasses.field()

    andAll = field("andAll")

    @cached_property
    def equals(self):  # pragma: no cover
        return FilterAttribute.make_one(self.boto3_raw_data["equals"])

    @cached_property
    def greaterThan(self):  # pragma: no cover
        return FilterAttribute.make_one(self.boto3_raw_data["greaterThan"])

    @cached_property
    def greaterThanOrEquals(self):  # pragma: no cover
        return FilterAttribute.make_one(self.boto3_raw_data["greaterThanOrEquals"])

    @cached_property
    def in_(self):  # pragma: no cover
        return FilterAttribute.make_one(self.boto3_raw_data["in"])

    @cached_property
    def lessThan(self):  # pragma: no cover
        return FilterAttribute.make_one(self.boto3_raw_data["lessThan"])

    @cached_property
    def lessThanOrEquals(self):  # pragma: no cover
        return FilterAttribute.make_one(self.boto3_raw_data["lessThanOrEquals"])

    @cached_property
    def listContains(self):  # pragma: no cover
        return FilterAttribute.make_one(self.boto3_raw_data["listContains"])

    @cached_property
    def notEquals(self):  # pragma: no cover
        return FilterAttribute.make_one(self.boto3_raw_data["notEquals"])

    @cached_property
    def notIn(self):  # pragma: no cover
        return FilterAttribute.make_one(self.boto3_raw_data["notIn"])

    orAll = field("orAll")

    @cached_property
    def startsWith(self):  # pragma: no cover
        return FilterAttribute.make_one(self.boto3_raw_data["startsWith"])

    @cached_property
    def stringContains(self):  # pragma: no cover
        return FilterAttribute.make_one(self.boto3_raw_data["stringContains"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RetrievalFilterPaginatorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RetrievalFilterPaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RetrievalFilter:
    boto3_raw_data: "type_defs.RetrievalFilterTypeDef" = dataclasses.field()

    andAll = field("andAll")

    @cached_property
    def equals(self):  # pragma: no cover
        return FilterAttribute.make_one(self.boto3_raw_data["equals"])

    @cached_property
    def greaterThan(self):  # pragma: no cover
        return FilterAttribute.make_one(self.boto3_raw_data["greaterThan"])

    @cached_property
    def greaterThanOrEquals(self):  # pragma: no cover
        return FilterAttribute.make_one(self.boto3_raw_data["greaterThanOrEquals"])

    @cached_property
    def in_(self):  # pragma: no cover
        return FilterAttribute.make_one(self.boto3_raw_data["in"])

    @cached_property
    def lessThan(self):  # pragma: no cover
        return FilterAttribute.make_one(self.boto3_raw_data["lessThan"])

    @cached_property
    def lessThanOrEquals(self):  # pragma: no cover
        return FilterAttribute.make_one(self.boto3_raw_data["lessThanOrEquals"])

    @cached_property
    def listContains(self):  # pragma: no cover
        return FilterAttribute.make_one(self.boto3_raw_data["listContains"])

    @cached_property
    def notEquals(self):  # pragma: no cover
        return FilterAttribute.make_one(self.boto3_raw_data["notEquals"])

    @cached_property
    def notIn(self):  # pragma: no cover
        return FilterAttribute.make_one(self.boto3_raw_data["notIn"])

    orAll = field("orAll")

    @cached_property
    def startsWith(self):  # pragma: no cover
        return FilterAttribute.make_one(self.boto3_raw_data["startsWith"])

    @cached_property
    def stringContains(self):  # pragma: no cover
        return FilterAttribute.make_one(self.boto3_raw_data["stringContains"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RetrievalFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RetrievalFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FlowInputField:
    boto3_raw_data: "type_defs.FlowInputFieldTypeDef" = dataclasses.field()

    @cached_property
    def content(self):  # pragma: no cover
        return FlowExecutionContent.make_one(self.boto3_raw_data["content"])

    name = field("name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FlowInputFieldTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FlowInputFieldTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FlowOutputField:
    boto3_raw_data: "type_defs.FlowOutputFieldTypeDef" = dataclasses.field()

    @cached_property
    def content(self):  # pragma: no cover
        return FlowExecutionContent.make_one(self.boto3_raw_data["content"])

    name = field("name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FlowOutputFieldTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FlowOutputFieldTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFlowExecutionResponse:
    boto3_raw_data: "type_defs.GetFlowExecutionResponseTypeDef" = dataclasses.field()

    endedAt = field("endedAt")

    @cached_property
    def errors(self):  # pragma: no cover
        return FlowExecutionError.make_many(self.boto3_raw_data["errors"])

    executionArn = field("executionArn")
    flowAliasIdentifier = field("flowAliasIdentifier")
    flowIdentifier = field("flowIdentifier")
    flowVersion = field("flowVersion")
    startedAt = field("startedAt")
    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetFlowExecutionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFlowExecutionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFlowExecutionsResponse:
    boto3_raw_data: "type_defs.ListFlowExecutionsResponseTypeDef" = dataclasses.field()

    @cached_property
    def flowExecutionSummaries(self):  # pragma: no cover
        return FlowExecutionSummary.make_many(
            self.boto3_raw_data["flowExecutionSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFlowExecutionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFlowExecutionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FlowInput:
    boto3_raw_data: "type_defs.FlowInputTypeDef" = dataclasses.field()

    @cached_property
    def content(self):  # pragma: no cover
        return FlowInputContent.make_one(self.boto3_raw_data["content"])

    nodeName = field("nodeName")
    nodeInputName = field("nodeInputName")
    nodeOutputName = field("nodeOutputName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FlowInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FlowInputTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FlowMultiTurnInputRequestEvent:
    boto3_raw_data: "type_defs.FlowMultiTurnInputRequestEventTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def content(self):  # pragma: no cover
        return FlowMultiTurnInputContent.make_one(self.boto3_raw_data["content"])

    nodeName = field("nodeName")
    nodeType = field("nodeType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.FlowMultiTurnInputRequestEventTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FlowMultiTurnInputRequestEventTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FlowOutputEvent:
    boto3_raw_data: "type_defs.FlowOutputEventTypeDef" = dataclasses.field()

    @cached_property
    def content(self):  # pragma: no cover
        return FlowOutputContent.make_one(self.boto3_raw_data["content"])

    nodeName = field("nodeName")
    nodeType = field("nodeType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FlowOutputEventTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FlowOutputEventTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FlowTraceConditionNodeResultEvent:
    boto3_raw_data: "type_defs.FlowTraceConditionNodeResultEventTypeDef" = (
        dataclasses.field()
    )

    nodeName = field("nodeName")

    @cached_property
    def satisfiedConditions(self):  # pragma: no cover
        return FlowTraceCondition.make_many(self.boto3_raw_data["satisfiedConditions"])

    timestamp = field("timestamp")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.FlowTraceConditionNodeResultEventTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FlowTraceConditionNodeResultEventTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FlowTraceNodeInputField:
    boto3_raw_data: "type_defs.FlowTraceNodeInputFieldTypeDef" = dataclasses.field()

    @cached_property
    def content(self):  # pragma: no cover
        return FlowTraceNodeInputContent.make_one(self.boto3_raw_data["content"])

    nodeInputName = field("nodeInputName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FlowTraceNodeInputFieldTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FlowTraceNodeInputFieldTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FlowTraceNodeOutputField:
    boto3_raw_data: "type_defs.FlowTraceNodeOutputFieldTypeDef" = dataclasses.field()

    @cached_property
    def content(self):  # pragma: no cover
        return FlowTraceNodeOutputContent.make_one(self.boto3_raw_data["content"])

    nodeOutputName = field("nodeOutputName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FlowTraceNodeOutputFieldTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FlowTraceNodeOutputFieldTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FunctionDefinition:
    boto3_raw_data: "type_defs.FunctionDefinitionTypeDef" = dataclasses.field()

    name = field("name")
    description = field("description")
    parameters = field("parameters")
    requireConfirmation = field("requireConfirmation")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FunctionDefinitionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FunctionDefinitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FunctionInvocationInput:
    boto3_raw_data: "type_defs.FunctionInvocationInputTypeDef" = dataclasses.field()

    actionGroup = field("actionGroup")
    actionInvocationType = field("actionInvocationType")
    agentId = field("agentId")
    collaboratorName = field("collaboratorName")
    function = field("function")

    @cached_property
    def parameters(self):  # pragma: no cover
        return FunctionParameter.make_many(self.boto3_raw_data["parameters"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FunctionInvocationInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FunctionInvocationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GenerateQueryResponse:
    boto3_raw_data: "type_defs.GenerateQueryResponseTypeDef" = dataclasses.field()

    @cached_property
    def queries(self):  # pragma: no cover
        return GeneratedQuery.make_many(self.boto3_raw_data["queries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GenerateQueryResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GenerateQueryResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAgentMemoryRequestPaginate:
    boto3_raw_data: "type_defs.GetAgentMemoryRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    agentAliasId = field("agentAliasId")
    agentId = field("agentId")
    memoryId = field("memoryId")
    memoryType = field("memoryType")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetAgentMemoryRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAgentMemoryRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFlowExecutionEventsRequestPaginate:
    boto3_raw_data: "type_defs.ListFlowExecutionEventsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    eventType = field("eventType")
    executionIdentifier = field("executionIdentifier")
    flowAliasIdentifier = field("flowAliasIdentifier")
    flowIdentifier = field("flowIdentifier")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListFlowExecutionEventsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFlowExecutionEventsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFlowExecutionsRequestPaginate:
    boto3_raw_data: "type_defs.ListFlowExecutionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    flowIdentifier = field("flowIdentifier")
    flowAliasIdentifier = field("flowAliasIdentifier")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListFlowExecutionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFlowExecutionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInvocationStepsRequestPaginate:
    boto3_raw_data: "type_defs.ListInvocationStepsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    sessionIdentifier = field("sessionIdentifier")
    invocationIdentifier = field("invocationIdentifier")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListInvocationStepsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInvocationStepsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInvocationsRequestPaginate:
    boto3_raw_data: "type_defs.ListInvocationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    sessionIdentifier = field("sessionIdentifier")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListInvocationsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInvocationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSessionsRequestPaginate:
    boto3_raw_data: "type_defs.ListSessionsRequestPaginateTypeDef" = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSessionsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSessionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailContentPolicyAssessment:
    boto3_raw_data: "type_defs.GuardrailContentPolicyAssessmentTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def filters(self):  # pragma: no cover
        return GuardrailContentFilter.make_many(self.boto3_raw_data["filters"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GuardrailContentPolicyAssessmentTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GuardrailContentPolicyAssessmentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailWordPolicyAssessment:
    boto3_raw_data: "type_defs.GuardrailWordPolicyAssessmentTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def customWords(self):  # pragma: no cover
        return GuardrailCustomWord.make_many(self.boto3_raw_data["customWords"])

    @cached_property
    def managedWordLists(self):  # pragma: no cover
        return GuardrailManagedWord.make_many(self.boto3_raw_data["managedWordLists"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GuardrailWordPolicyAssessmentTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GuardrailWordPolicyAssessmentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailSensitiveInformationPolicyAssessment:
    boto3_raw_data: "type_defs.GuardrailSensitiveInformationPolicyAssessmentTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def piiEntities(self):  # pragma: no cover
        return GuardrailPiiEntityFilter.make_many(self.boto3_raw_data["piiEntities"])

    @cached_property
    def regexes(self):  # pragma: no cover
        return GuardrailRegexFilter.make_many(self.boto3_raw_data["regexes"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GuardrailSensitiveInformationPolicyAssessmentTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GuardrailSensitiveInformationPolicyAssessmentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailTopicPolicyAssessment:
    boto3_raw_data: "type_defs.GuardrailTopicPolicyAssessmentTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def topics(self):  # pragma: no cover
        return GuardrailTopic.make_many(self.boto3_raw_data["topics"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GuardrailTopicPolicyAssessmentTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GuardrailTopicPolicyAssessmentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImageInputOutput:
    boto3_raw_data: "type_defs.ImageInputOutputTypeDef" = dataclasses.field()

    format = field("format")

    @cached_property
    def source(self):  # pragma: no cover
        return ImageInputSourceOutput.make_one(self.boto3_raw_data["source"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImageInputOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImageInputOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImageSourceOutput:
    boto3_raw_data: "type_defs.ImageSourceOutputTypeDef" = dataclasses.field()

    bytes = field("bytes")

    @cached_property
    def s3Location(self):  # pragma: no cover
        return S3Location.make_one(self.boto3_raw_data["s3Location"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImageSourceOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImageSourceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImageSource:
    boto3_raw_data: "type_defs.ImageSourceTypeDef" = dataclasses.field()

    bytes = field("bytes")

    @cached_property
    def s3Location(self):  # pragma: no cover
        return S3Location.make_one(self.boto3_raw_data["s3Location"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImageSourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ImageSourceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImplicitFilterConfiguration:
    boto3_raw_data: "type_defs.ImplicitFilterConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def metadataAttributes(self):  # pragma: no cover
        return MetadataAttributeSchema.make_many(
            self.boto3_raw_data["metadataAttributes"]
        )

    modelArn = field("modelArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImplicitFilterConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImplicitFilterConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InferenceConfig:
    boto3_raw_data: "type_defs.InferenceConfigTypeDef" = dataclasses.field()

    @cached_property
    def textInferenceConfig(self):  # pragma: no cover
        return TextInferenceConfig.make_one(self.boto3_raw_data["textInferenceConfig"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InferenceConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InferenceConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModelInvocationInput:
    boto3_raw_data: "type_defs.ModelInvocationInputTypeDef" = dataclasses.field()

    foundationModel = field("foundationModel")

    @cached_property
    def inferenceConfiguration(self):  # pragma: no cover
        return InferenceConfigurationOutput.make_one(
            self.boto3_raw_data["inferenceConfiguration"]
        )

    overrideLambda = field("overrideLambda")
    parserMode = field("parserMode")
    promptCreationMode = field("promptCreationMode")
    text = field("text")
    traceId = field("traceId")
    type = field("type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModelInvocationInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModelInvocationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputPrompt:
    boto3_raw_data: "type_defs.InputPromptTypeDef" = dataclasses.field()

    @cached_property
    def textPrompt(self):  # pragma: no cover
        return TextPrompt.make_one(self.boto3_raw_data["textPrompt"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InputPromptTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InputPromptTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OptimizedPrompt:
    boto3_raw_data: "type_defs.OptimizedPromptTypeDef" = dataclasses.field()

    @cached_property
    def textPrompt(self):  # pragma: no cover
        return TextPrompt.make_one(self.boto3_raw_data["textPrompt"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OptimizedPromptTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OptimizedPromptTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInvocationStepsResponse:
    boto3_raw_data: "type_defs.ListInvocationStepsResponseTypeDef" = dataclasses.field()

    @cached_property
    def invocationStepSummaries(self):  # pragma: no cover
        return InvocationStepSummary.make_many(
            self.boto3_raw_data["invocationStepSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListInvocationStepsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInvocationStepsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInvocationsResponse:
    boto3_raw_data: "type_defs.ListInvocationsResponseTypeDef" = dataclasses.field()

    @cached_property
    def invocationSummaries(self):  # pragma: no cover
        return InvocationSummary.make_many(self.boto3_raw_data["invocationSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListInvocationsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInvocationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSessionsResponse:
    boto3_raw_data: "type_defs.ListSessionsResponseTypeDef" = dataclasses.field()

    @cached_property
    def sessionSummaries(self):  # pragma: no cover
        return SessionSummary.make_many(self.boto3_raw_data["sessionSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSessionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSessionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Memory:
    boto3_raw_data: "type_defs.MemoryTypeDef" = dataclasses.field()

    @cached_property
    def sessionSummary(self):  # pragma: no cover
        return MemorySessionSummary.make_one(self.boto3_raw_data["sessionSummary"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MemoryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MemoryTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Metadata:
    boto3_raw_data: "type_defs.MetadataTypeDef" = dataclasses.field()

    clientRequestId = field("clientRequestId")
    endTime = field("endTime")
    operationTotalTimeMs = field("operationTotalTimeMs")
    startTime = field("startTime")
    totalTimeMs = field("totalTimeMs")

    @cached_property
    def usage(self):  # pragma: no cover
        return Usage.make_one(self.boto3_raw_data["usage"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MetadataTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NodeInputField:
    boto3_raw_data: "type_defs.NodeInputFieldTypeDef" = dataclasses.field()

    @cached_property
    def content(self):  # pragma: no cover
        return NodeExecutionContent.make_one(self.boto3_raw_data["content"])

    name = field("name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NodeInputFieldTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.NodeInputFieldTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NodeOutputField:
    boto3_raw_data: "type_defs.NodeOutputFieldTypeDef" = dataclasses.field()

    @cached_property
    def content(self):  # pragma: no cover
        return NodeExecutionContent.make_one(self.boto3_raw_data["content"])

    name = field("name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NodeOutputFieldTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.NodeOutputFieldTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReasoningContentBlock:
    boto3_raw_data: "type_defs.ReasoningContentBlockTypeDef" = dataclasses.field()

    @cached_property
    def reasoningText(self):  # pragma: no cover
        return ReasoningTextBlock.make_one(self.boto3_raw_data["reasoningText"])

    redactedContent = field("redactedContent")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReasoningContentBlockTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReasoningContentBlockTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RerankDocumentOutput:
    boto3_raw_data: "type_defs.RerankDocumentOutputTypeDef" = dataclasses.field()

    type = field("type")
    jsonDocument = field("jsonDocument")

    @cached_property
    def textDocument(self):  # pragma: no cover
        return RerankTextDocument.make_one(self.boto3_raw_data["textDocument"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RerankDocumentOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RerankDocumentOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RerankDocument:
    boto3_raw_data: "type_defs.RerankDocumentTypeDef" = dataclasses.field()

    type = field("type")
    jsonDocument = field("jsonDocument")

    @cached_property
    def textDocument(self):  # pragma: no cover
        return RerankTextDocument.make_one(self.boto3_raw_data["textDocument"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RerankDocumentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RerankDocumentTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RerankQuery:
    boto3_raw_data: "type_defs.RerankQueryTypeDef" = dataclasses.field()

    @cached_property
    def textQuery(self):  # pragma: no cover
        return RerankTextDocument.make_one(self.boto3_raw_data["textQuery"])

    type = field("type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RerankQueryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RerankQueryTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RetrievalResultContent:
    boto3_raw_data: "type_defs.RetrievalResultContentTypeDef" = dataclasses.field()

    byteContent = field("byteContent")

    @cached_property
    def row(self):  # pragma: no cover
        return RetrievalResultContentColumn.make_many(self.boto3_raw_data["row"])

    text = field("text")
    type = field("type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RetrievalResultContentTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RetrievalResultContentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RetrievalResultLocation:
    boto3_raw_data: "type_defs.RetrievalResultLocationTypeDef" = dataclasses.field()

    type = field("type")

    @cached_property
    def confluenceLocation(self):  # pragma: no cover
        return RetrievalResultConfluenceLocation.make_one(
            self.boto3_raw_data["confluenceLocation"]
        )

    @cached_property
    def customDocumentLocation(self):  # pragma: no cover
        return RetrievalResultCustomDocumentLocation.make_one(
            self.boto3_raw_data["customDocumentLocation"]
        )

    @cached_property
    def kendraDocumentLocation(self):  # pragma: no cover
        return RetrievalResultKendraDocumentLocation.make_one(
            self.boto3_raw_data["kendraDocumentLocation"]
        )

    @cached_property
    def s3Location(self):  # pragma: no cover
        return RetrievalResultS3Location.make_one(self.boto3_raw_data["s3Location"])

    @cached_property
    def salesforceLocation(self):  # pragma: no cover
        return RetrievalResultSalesforceLocation.make_one(
            self.boto3_raw_data["salesforceLocation"]
        )

    @cached_property
    def sharePointLocation(self):  # pragma: no cover
        return RetrievalResultSharePointLocation.make_one(
            self.boto3_raw_data["sharePointLocation"]
        )

    @cached_property
    def sqlLocation(self):  # pragma: no cover
        return RetrievalResultSqlLocation.make_one(self.boto3_raw_data["sqlLocation"])

    @cached_property
    def webLocation(self):  # pragma: no cover
        return RetrievalResultWebLocation.make_one(self.boto3_raw_data["webLocation"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RetrievalResultLocationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RetrievalResultLocationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TextResponsePart:
    boto3_raw_data: "type_defs.TextResponsePartTypeDef" = dataclasses.field()

    @cached_property
    def span(self):  # pragma: no cover
        return Span.make_one(self.boto3_raw_data["span"])

    text = field("text")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TextResponsePartTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TextResponsePartTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TextToSqlConfiguration:
    boto3_raw_data: "type_defs.TextToSqlConfigurationTypeDef" = dataclasses.field()

    type = field("type")

    @cached_property
    def knowledgeBaseConfiguration(self):  # pragma: no cover
        return TextToSqlKnowledgeBaseConfiguration.make_one(
            self.boto3_raw_data["knowledgeBaseConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TextToSqlConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TextToSqlConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApiRequestBody:
    boto3_raw_data: "type_defs.ApiRequestBodyTypeDef" = dataclasses.field()

    content = field("content")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ApiRequestBodyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ApiRequestBodyTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActionGroupInvocationInput:
    boto3_raw_data: "type_defs.ActionGroupInvocationInputTypeDef" = dataclasses.field()

    actionGroupName = field("actionGroupName")
    apiPath = field("apiPath")
    executionType = field("executionType")
    function = field("function")
    invocationId = field("invocationId")

    @cached_property
    def parameters(self):  # pragma: no cover
        return Parameter.make_many(self.boto3_raw_data["parameters"])

    @cached_property
    def requestBody(self):  # pragma: no cover
        return RequestBody.make_one(self.boto3_raw_data["requestBody"])

    verb = field("verb")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ActionGroupInvocationInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActionGroupInvocationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RerankingConfiguration:
    boto3_raw_data: "type_defs.RerankingConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def bedrockRerankingConfiguration(self):  # pragma: no cover
        return BedrockRerankingConfiguration.make_one(
            self.boto3_raw_data["bedrockRerankingConfiguration"]
        )

    type = field("type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RerankingConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RerankingConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExternalSource:
    boto3_raw_data: "type_defs.ExternalSourceTypeDef" = dataclasses.field()

    sourceType = field("sourceType")

    @cached_property
    def byteContent(self):  # pragma: no cover
        return ByteContentDoc.make_one(self.boto3_raw_data["byteContent"])

    @cached_property
    def s3Location(self):  # pragma: no cover
        return S3ObjectDoc.make_one(self.boto3_raw_data["s3Location"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExternalSourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ExternalSourceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FileSource:
    boto3_raw_data: "type_defs.FileSourceTypeDef" = dataclasses.field()

    sourceType = field("sourceType")

    @cached_property
    def byteContent(self):  # pragma: no cover
        return ByteContentFile.make_one(self.boto3_raw_data["byteContent"])

    @cached_property
    def s3Location(self):  # pragma: no cover
        return S3ObjectFile.make_one(self.boto3_raw_data["s3Location"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FileSourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FileSourceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConversationHistory:
    boto3_raw_data: "type_defs.ConversationHistoryTypeDef" = dataclasses.field()

    @cached_property
    def messages(self):  # pragma: no cover
        return Message.make_many(self.boto3_raw_data["messages"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConversationHistoryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConversationHistoryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetadataConfigurationForReranking:
    boto3_raw_data: "type_defs.MetadataConfigurationForRerankingTypeDef" = (
        dataclasses.field()
    )

    selectionMode = field("selectionMode")

    @cached_property
    def selectiveModeConfiguration(self):  # pragma: no cover
        return RerankingMetadataSelectiveModeConfiguration.make_one(
            self.boto3_raw_data["selectiveModeConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MetadataConfigurationForRerankingTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MetadataConfigurationForRerankingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FlowExecutionInputEvent:
    boto3_raw_data: "type_defs.FlowExecutionInputEventTypeDef" = dataclasses.field()

    @cached_property
    def fields(self):  # pragma: no cover
        return FlowInputField.make_many(self.boto3_raw_data["fields"])

    nodeName = field("nodeName")
    timestamp = field("timestamp")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FlowExecutionInputEventTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FlowExecutionInputEventTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FlowExecutionOutputEvent:
    boto3_raw_data: "type_defs.FlowExecutionOutputEventTypeDef" = dataclasses.field()

    @cached_property
    def fields(self):  # pragma: no cover
        return FlowOutputField.make_many(self.boto3_raw_data["fields"])

    nodeName = field("nodeName")
    timestamp = field("timestamp")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FlowExecutionOutputEventTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FlowExecutionOutputEventTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InvokeFlowRequest:
    boto3_raw_data: "type_defs.InvokeFlowRequestTypeDef" = dataclasses.field()

    flowAliasIdentifier = field("flowAliasIdentifier")
    flowIdentifier = field("flowIdentifier")

    @cached_property
    def inputs(self):  # pragma: no cover
        return FlowInput.make_many(self.boto3_raw_data["inputs"])

    enableTrace = field("enableTrace")
    executionId = field("executionId")

    @cached_property
    def modelPerformanceConfiguration(self):  # pragma: no cover
        return ModelPerformanceConfiguration.make_one(
            self.boto3_raw_data["modelPerformanceConfiguration"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InvokeFlowRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InvokeFlowRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartFlowExecutionRequest:
    boto3_raw_data: "type_defs.StartFlowExecutionRequestTypeDef" = dataclasses.field()

    flowAliasIdentifier = field("flowAliasIdentifier")
    flowIdentifier = field("flowIdentifier")

    @cached_property
    def inputs(self):  # pragma: no cover
        return FlowInput.make_many(self.boto3_raw_data["inputs"])

    flowExecutionName = field("flowExecutionName")

    @cached_property
    def modelPerformanceConfiguration(self):  # pragma: no cover
        return ModelPerformanceConfiguration.make_one(
            self.boto3_raw_data["modelPerformanceConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartFlowExecutionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartFlowExecutionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FlowTraceNodeInputEvent:
    boto3_raw_data: "type_defs.FlowTraceNodeInputEventTypeDef" = dataclasses.field()

    @cached_property
    def fields(self):  # pragma: no cover
        return FlowTraceNodeInputField.make_many(self.boto3_raw_data["fields"])

    nodeName = field("nodeName")
    timestamp = field("timestamp")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FlowTraceNodeInputEventTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FlowTraceNodeInputEventTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FlowTraceNodeOutputEvent:
    boto3_raw_data: "type_defs.FlowTraceNodeOutputEventTypeDef" = dataclasses.field()

    @cached_property
    def fields(self):  # pragma: no cover
        return FlowTraceNodeOutputField.make_many(self.boto3_raw_data["fields"])

    nodeName = field("nodeName")
    timestamp = field("timestamp")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FlowTraceNodeOutputEventTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FlowTraceNodeOutputEventTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FunctionSchema:
    boto3_raw_data: "type_defs.FunctionSchemaTypeDef" = dataclasses.field()

    @cached_property
    def functions(self):  # pragma: no cover
        return FunctionDefinition.make_many(self.boto3_raw_data["functions"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FunctionSchemaTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FunctionSchemaTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailAssessment:
    boto3_raw_data: "type_defs.GuardrailAssessmentTypeDef" = dataclasses.field()

    @cached_property
    def contentPolicy(self):  # pragma: no cover
        return GuardrailContentPolicyAssessment.make_one(
            self.boto3_raw_data["contentPolicy"]
        )

    @cached_property
    def sensitiveInformationPolicy(self):  # pragma: no cover
        return GuardrailSensitiveInformationPolicyAssessment.make_one(
            self.boto3_raw_data["sensitiveInformationPolicy"]
        )

    @cached_property
    def topicPolicy(self):  # pragma: no cover
        return GuardrailTopicPolicyAssessment.make_one(
            self.boto3_raw_data["topicPolicy"]
        )

    @cached_property
    def wordPolicy(self):  # pragma: no cover
        return GuardrailWordPolicyAssessment.make_one(self.boto3_raw_data["wordPolicy"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GuardrailAssessmentTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GuardrailAssessmentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContentBodyOutput:
    boto3_raw_data: "type_defs.ContentBodyOutputTypeDef" = dataclasses.field()

    body = field("body")

    @cached_property
    def images(self):  # pragma: no cover
        return ImageInputOutput.make_many(self.boto3_raw_data["images"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ContentBodyOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContentBodyOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImageBlockOutput:
    boto3_raw_data: "type_defs.ImageBlockOutputTypeDef" = dataclasses.field()

    format = field("format")

    @cached_property
    def source(self):  # pragma: no cover
        return ImageSourceOutput.make_one(self.boto3_raw_data["source"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImageBlockOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImageBlockOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImageBlock:
    boto3_raw_data: "type_defs.ImageBlockTypeDef" = dataclasses.field()

    format = field("format")

    @cached_property
    def source(self):  # pragma: no cover
        return ImageSource.make_one(self.boto3_raw_data["source"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImageBlockTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ImageBlockTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExternalSourcesGenerationConfiguration:
    boto3_raw_data: "type_defs.ExternalSourcesGenerationConfigurationTypeDef" = (
        dataclasses.field()
    )

    additionalModelRequestFields = field("additionalModelRequestFields")

    @cached_property
    def guardrailConfiguration(self):  # pragma: no cover
        return GuardrailConfiguration.make_one(
            self.boto3_raw_data["guardrailConfiguration"]
        )

    @cached_property
    def inferenceConfig(self):  # pragma: no cover
        return InferenceConfig.make_one(self.boto3_raw_data["inferenceConfig"])

    @cached_property
    def performanceConfig(self):  # pragma: no cover
        return PerformanceConfiguration.make_one(
            self.boto3_raw_data["performanceConfig"]
        )

    @cached_property
    def promptTemplate(self):  # pragma: no cover
        return PromptTemplate.make_one(self.boto3_raw_data["promptTemplate"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ExternalSourcesGenerationConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExternalSourcesGenerationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GenerationConfiguration:
    boto3_raw_data: "type_defs.GenerationConfigurationTypeDef" = dataclasses.field()

    additionalModelRequestFields = field("additionalModelRequestFields")

    @cached_property
    def guardrailConfiguration(self):  # pragma: no cover
        return GuardrailConfiguration.make_one(
            self.boto3_raw_data["guardrailConfiguration"]
        )

    @cached_property
    def inferenceConfig(self):  # pragma: no cover
        return InferenceConfig.make_one(self.boto3_raw_data["inferenceConfig"])

    @cached_property
    def performanceConfig(self):  # pragma: no cover
        return PerformanceConfiguration.make_one(
            self.boto3_raw_data["performanceConfig"]
        )

    @cached_property
    def promptTemplate(self):  # pragma: no cover
        return PromptTemplate.make_one(self.boto3_raw_data["promptTemplate"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GenerationConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GenerationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OrchestrationConfiguration:
    boto3_raw_data: "type_defs.OrchestrationConfigurationTypeDef" = dataclasses.field()

    additionalModelRequestFields = field("additionalModelRequestFields")

    @cached_property
    def inferenceConfig(self):  # pragma: no cover
        return InferenceConfig.make_one(self.boto3_raw_data["inferenceConfig"])

    @cached_property
    def performanceConfig(self):  # pragma: no cover
        return PerformanceConfiguration.make_one(
            self.boto3_raw_data["performanceConfig"]
        )

    @cached_property
    def promptTemplate(self):  # pragma: no cover
        return PromptTemplate.make_one(self.boto3_raw_data["promptTemplate"])

    @cached_property
    def queryTransformationConfiguration(self):  # pragma: no cover
        return QueryTransformationConfiguration.make_one(
            self.boto3_raw_data["queryTransformationConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OrchestrationConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OrchestrationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PromptConfiguration:
    boto3_raw_data: "type_defs.PromptConfigurationTypeDef" = dataclasses.field()

    additionalModelRequestFields = field("additionalModelRequestFields")
    basePromptTemplate = field("basePromptTemplate")
    foundationModel = field("foundationModel")
    inferenceConfiguration = field("inferenceConfiguration")
    parserMode = field("parserMode")
    promptCreationMode = field("promptCreationMode")
    promptState = field("promptState")
    promptType = field("promptType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PromptConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PromptConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OptimizePromptRequest:
    boto3_raw_data: "type_defs.OptimizePromptRequestTypeDef" = dataclasses.field()

    @cached_property
    def input(self):  # pragma: no cover
        return InputPrompt.make_one(self.boto3_raw_data["input"])

    targetModelId = field("targetModelId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OptimizePromptRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OptimizePromptRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OptimizedPromptEvent:
    boto3_raw_data: "type_defs.OptimizedPromptEventTypeDef" = dataclasses.field()

    @cached_property
    def optimizedPrompt(self):  # pragma: no cover
        return OptimizedPrompt.make_one(self.boto3_raw_data["optimizedPrompt"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OptimizedPromptEventTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OptimizedPromptEventTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAgentMemoryResponse:
    boto3_raw_data: "type_defs.GetAgentMemoryResponseTypeDef" = dataclasses.field()

    @cached_property
    def memoryContents(self):  # pragma: no cover
        return Memory.make_many(self.boto3_raw_data["memoryContents"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAgentMemoryResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAgentMemoryResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActionGroupInvocationOutput:
    boto3_raw_data: "type_defs.ActionGroupInvocationOutputTypeDef" = dataclasses.field()

    @cached_property
    def metadata(self):  # pragma: no cover
        return Metadata.make_one(self.boto3_raw_data["metadata"])

    text = field("text")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ActionGroupInvocationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActionGroupInvocationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CodeInterpreterInvocationOutput:
    boto3_raw_data: "type_defs.CodeInterpreterInvocationOutputTypeDef" = (
        dataclasses.field()
    )

    executionError = field("executionError")
    executionOutput = field("executionOutput")
    executionTimeout = field("executionTimeout")
    files = field("files")

    @cached_property
    def metadata(self):  # pragma: no cover
        return Metadata.make_one(self.boto3_raw_data["metadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CodeInterpreterInvocationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CodeInterpreterInvocationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FailureTrace:
    boto3_raw_data: "type_defs.FailureTraceTypeDef" = dataclasses.field()

    failureCode = field("failureCode")
    failureReason = field("failureReason")

    @cached_property
    def metadata(self):  # pragma: no cover
        return Metadata.make_one(self.boto3_raw_data["metadata"])

    traceId = field("traceId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FailureTraceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FailureTraceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FinalResponse:
    boto3_raw_data: "type_defs.FinalResponseTypeDef" = dataclasses.field()

    @cached_property
    def metadata(self):  # pragma: no cover
        return Metadata.make_one(self.boto3_raw_data["metadata"])

    text = field("text")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FinalResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FinalResponseTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RoutingClassifierModelInvocationOutput:
    boto3_raw_data: "type_defs.RoutingClassifierModelInvocationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def metadata(self):  # pragma: no cover
        return Metadata.make_one(self.boto3_raw_data["metadata"])

    @cached_property
    def rawResponse(self):  # pragma: no cover
        return RawResponse.make_one(self.boto3_raw_data["rawResponse"])

    traceId = field("traceId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RoutingClassifierModelInvocationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RoutingClassifierModelInvocationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NodeInputEvent:
    boto3_raw_data: "type_defs.NodeInputEventTypeDef" = dataclasses.field()

    @cached_property
    def fields(self):  # pragma: no cover
        return NodeInputField.make_many(self.boto3_raw_data["fields"])

    nodeName = field("nodeName")
    timestamp = field("timestamp")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NodeInputEventTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.NodeInputEventTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NodeOutputEvent:
    boto3_raw_data: "type_defs.NodeOutputEventTypeDef" = dataclasses.field()

    @cached_property
    def fields(self):  # pragma: no cover
        return NodeOutputField.make_many(self.boto3_raw_data["fields"])

    nodeName = field("nodeName")
    timestamp = field("timestamp")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NodeOutputEventTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.NodeOutputEventTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OrchestrationModelInvocationOutput:
    boto3_raw_data: "type_defs.OrchestrationModelInvocationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def metadata(self):  # pragma: no cover
        return Metadata.make_one(self.boto3_raw_data["metadata"])

    @cached_property
    def rawResponse(self):  # pragma: no cover
        return RawResponse.make_one(self.boto3_raw_data["rawResponse"])

    @cached_property
    def reasoningContent(self):  # pragma: no cover
        return ReasoningContentBlock.make_one(self.boto3_raw_data["reasoningContent"])

    traceId = field("traceId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.OrchestrationModelInvocationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OrchestrationModelInvocationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PostProcessingModelInvocationOutput:
    boto3_raw_data: "type_defs.PostProcessingModelInvocationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def metadata(self):  # pragma: no cover
        return Metadata.make_one(self.boto3_raw_data["metadata"])

    @cached_property
    def parsedResponse(self):  # pragma: no cover
        return PostProcessingParsedResponse.make_one(
            self.boto3_raw_data["parsedResponse"]
        )

    @cached_property
    def rawResponse(self):  # pragma: no cover
        return RawResponse.make_one(self.boto3_raw_data["rawResponse"])

    @cached_property
    def reasoningContent(self):  # pragma: no cover
        return ReasoningContentBlock.make_one(self.boto3_raw_data["reasoningContent"])

    traceId = field("traceId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PostProcessingModelInvocationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PostProcessingModelInvocationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PreProcessingModelInvocationOutput:
    boto3_raw_data: "type_defs.PreProcessingModelInvocationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def metadata(self):  # pragma: no cover
        return Metadata.make_one(self.boto3_raw_data["metadata"])

    @cached_property
    def parsedResponse(self):  # pragma: no cover
        return PreProcessingParsedResponse.make_one(
            self.boto3_raw_data["parsedResponse"]
        )

    @cached_property
    def rawResponse(self):  # pragma: no cover
        return RawResponse.make_one(self.boto3_raw_data["rawResponse"])

    @cached_property
    def reasoningContent(self):  # pragma: no cover
        return ReasoningContentBlock.make_one(self.boto3_raw_data["reasoningContent"])

    traceId = field("traceId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PreProcessingModelInvocationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PreProcessingModelInvocationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RerankResult:
    boto3_raw_data: "type_defs.RerankResultTypeDef" = dataclasses.field()

    index = field("index")
    relevanceScore = field("relevanceScore")

    @cached_property
    def document(self):  # pragma: no cover
        return RerankDocumentOutput.make_one(self.boto3_raw_data["document"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RerankResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RerankResultTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KnowledgeBaseRetrievalResult:
    boto3_raw_data: "type_defs.KnowledgeBaseRetrievalResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def content(self):  # pragma: no cover
        return RetrievalResultContent.make_one(self.boto3_raw_data["content"])

    @cached_property
    def location(self):  # pragma: no cover
        return RetrievalResultLocation.make_one(self.boto3_raw_data["location"])

    metadata = field("metadata")
    score = field("score")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KnowledgeBaseRetrievalResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KnowledgeBaseRetrievalResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RetrievedReference:
    boto3_raw_data: "type_defs.RetrievedReferenceTypeDef" = dataclasses.field()

    @cached_property
    def content(self):  # pragma: no cover
        return RetrievalResultContent.make_one(self.boto3_raw_data["content"])

    @cached_property
    def location(self):  # pragma: no cover
        return RetrievalResultLocation.make_one(self.boto3_raw_data["location"])

    metadata = field("metadata")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RetrievedReferenceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RetrievedReferenceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GeneratedResponsePart:
    boto3_raw_data: "type_defs.GeneratedResponsePartTypeDef" = dataclasses.field()

    @cached_property
    def textResponsePart(self):  # pragma: no cover
        return TextResponsePart.make_one(self.boto3_raw_data["textResponsePart"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GeneratedResponsePartTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GeneratedResponsePartTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TransformationConfiguration:
    boto3_raw_data: "type_defs.TransformationConfigurationTypeDef" = dataclasses.field()

    mode = field("mode")

    @cached_property
    def textToSqlConfiguration(self):  # pragma: no cover
        return TextToSqlConfiguration.make_one(
            self.boto3_raw_data["textToSqlConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TransformationConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TransformationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApiInvocationInput:
    boto3_raw_data: "type_defs.ApiInvocationInputTypeDef" = dataclasses.field()

    actionGroup = field("actionGroup")
    actionInvocationType = field("actionInvocationType")
    agentId = field("agentId")
    apiPath = field("apiPath")
    collaboratorName = field("collaboratorName")
    httpMethod = field("httpMethod")

    @cached_property
    def parameters(self):  # pragma: no cover
        return ApiParameter.make_many(self.boto3_raw_data["parameters"])

    @cached_property
    def requestBody(self):  # pragma: no cover
        return ApiRequestBody.make_one(self.boto3_raw_data["requestBody"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ApiInvocationInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApiInvocationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputFile:
    boto3_raw_data: "type_defs.InputFileTypeDef" = dataclasses.field()

    name = field("name")

    @cached_property
    def source(self):  # pragma: no cover
        return FileSource.make_one(self.boto3_raw_data["source"])

    useCase = field("useCase")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InputFileTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InputFileTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImageInput:
    boto3_raw_data: "type_defs.ImageInputTypeDef" = dataclasses.field()

    format = field("format")
    source = field("source")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImageInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ImageInputTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VectorSearchBedrockRerankingConfiguration:
    boto3_raw_data: "type_defs.VectorSearchBedrockRerankingConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def modelConfiguration(self):  # pragma: no cover
        return VectorSearchBedrockRerankingModelConfiguration.make_one(
            self.boto3_raw_data["modelConfiguration"]
        )

    @cached_property
    def metadataConfiguration(self):  # pragma: no cover
        return MetadataConfigurationForReranking.make_one(
            self.boto3_raw_data["metadataConfiguration"]
        )

    numberOfRerankedResults = field("numberOfRerankedResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.VectorSearchBedrockRerankingConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VectorSearchBedrockRerankingConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FlowTrace:
    boto3_raw_data: "type_defs.FlowTraceTypeDef" = dataclasses.field()

    @cached_property
    def conditionNodeResultTrace(self):  # pragma: no cover
        return FlowTraceConditionNodeResultEvent.make_one(
            self.boto3_raw_data["conditionNodeResultTrace"]
        )

    @cached_property
    def nodeActionTrace(self):  # pragma: no cover
        return FlowTraceNodeActionEvent.make_one(self.boto3_raw_data["nodeActionTrace"])

    @cached_property
    def nodeInputTrace(self):  # pragma: no cover
        return FlowTraceNodeInputEvent.make_one(self.boto3_raw_data["nodeInputTrace"])

    @cached_property
    def nodeOutputTrace(self):  # pragma: no cover
        return FlowTraceNodeOutputEvent.make_one(self.boto3_raw_data["nodeOutputTrace"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FlowTraceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FlowTraceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AgentActionGroup:
    boto3_raw_data: "type_defs.AgentActionGroupTypeDef" = dataclasses.field()

    actionGroupName = field("actionGroupName")

    @cached_property
    def actionGroupExecutor(self):  # pragma: no cover
        return ActionGroupExecutor.make_one(self.boto3_raw_data["actionGroupExecutor"])

    @cached_property
    def apiSchema(self):  # pragma: no cover
        return APISchema.make_one(self.boto3_raw_data["apiSchema"])

    description = field("description")

    @cached_property
    def functionSchema(self):  # pragma: no cover
        return FunctionSchema.make_one(self.boto3_raw_data["functionSchema"])

    parentActionGroupSignature = field("parentActionGroupSignature")
    parentActionGroupSignatureParams = field("parentActionGroupSignatureParams")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AgentActionGroupTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AgentActionGroupTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailTrace:
    boto3_raw_data: "type_defs.GuardrailTraceTypeDef" = dataclasses.field()

    action = field("action")

    @cached_property
    def inputAssessments(self):  # pragma: no cover
        return GuardrailAssessment.make_many(self.boto3_raw_data["inputAssessments"])

    @cached_property
    def metadata(self):  # pragma: no cover
        return Metadata.make_one(self.boto3_raw_data["metadata"])

    @cached_property
    def outputAssessments(self):  # pragma: no cover
        return GuardrailAssessment.make_many(self.boto3_raw_data["outputAssessments"])

    traceId = field("traceId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GuardrailTraceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GuardrailTraceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApiResultOutput:
    boto3_raw_data: "type_defs.ApiResultOutputTypeDef" = dataclasses.field()

    actionGroup = field("actionGroup")
    agentId = field("agentId")
    apiPath = field("apiPath")
    confirmationState = field("confirmationState")
    httpMethod = field("httpMethod")
    httpStatusCode = field("httpStatusCode")
    responseBody = field("responseBody")
    responseState = field("responseState")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ApiResultOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ApiResultOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FunctionResultOutput:
    boto3_raw_data: "type_defs.FunctionResultOutputTypeDef" = dataclasses.field()

    actionGroup = field("actionGroup")
    agentId = field("agentId")
    confirmationState = field("confirmationState")
    function = field("function")
    responseBody = field("responseBody")
    responseState = field("responseState")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FunctionResultOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FunctionResultOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BedrockSessionContentBlockOutput:
    boto3_raw_data: "type_defs.BedrockSessionContentBlockOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def image(self):  # pragma: no cover
        return ImageBlockOutput.make_one(self.boto3_raw_data["image"])

    text = field("text")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BedrockSessionContentBlockOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BedrockSessionContentBlockOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BedrockSessionContentBlock:
    boto3_raw_data: "type_defs.BedrockSessionContentBlockTypeDef" = dataclasses.field()

    @cached_property
    def image(self):  # pragma: no cover
        return ImageBlock.make_one(self.boto3_raw_data["image"])

    text = field("text")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BedrockSessionContentBlockTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BedrockSessionContentBlockTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExternalSourcesRetrieveAndGenerateConfiguration:
    boto3_raw_data: (
        "type_defs.ExternalSourcesRetrieveAndGenerateConfigurationTypeDef"
    ) = dataclasses.field()

    modelArn = field("modelArn")

    @cached_property
    def sources(self):  # pragma: no cover
        return ExternalSource.make_many(self.boto3_raw_data["sources"])

    @cached_property
    def generationConfiguration(self):  # pragma: no cover
        return ExternalSourcesGenerationConfiguration.make_one(
            self.boto3_raw_data["generationConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ExternalSourcesRetrieveAndGenerateConfigurationTypeDef"
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
                "type_defs.ExternalSourcesRetrieveAndGenerateConfigurationTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PromptOverrideConfiguration:
    boto3_raw_data: "type_defs.PromptOverrideConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def promptConfigurations(self):  # pragma: no cover
        return PromptConfiguration.make_many(
            self.boto3_raw_data["promptConfigurations"]
        )

    overrideLambda = field("overrideLambda")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PromptOverrideConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PromptOverrideConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OptimizedPromptStream:
    boto3_raw_data: "type_defs.OptimizedPromptStreamTypeDef" = dataclasses.field()

    @cached_property
    def accessDeniedException(self):  # pragma: no cover
        return AccessDeniedException.make_one(
            self.boto3_raw_data["accessDeniedException"]
        )

    @cached_property
    def analyzePromptEvent(self):  # pragma: no cover
        return AnalyzePromptEvent.make_one(self.boto3_raw_data["analyzePromptEvent"])

    @cached_property
    def badGatewayException(self):  # pragma: no cover
        return BadGatewayException.make_one(self.boto3_raw_data["badGatewayException"])

    @cached_property
    def dependencyFailedException(self):  # pragma: no cover
        return DependencyFailedException.make_one(
            self.boto3_raw_data["dependencyFailedException"]
        )

    @cached_property
    def internalServerException(self):  # pragma: no cover
        return InternalServerException.make_one(
            self.boto3_raw_data["internalServerException"]
        )

    @cached_property
    def optimizedPromptEvent(self):  # pragma: no cover
        return OptimizedPromptEvent.make_one(
            self.boto3_raw_data["optimizedPromptEvent"]
        )

    @cached_property
    def throttlingException(self):  # pragma: no cover
        return ThrottlingException.make_one(self.boto3_raw_data["throttlingException"])

    @cached_property
    def validationException(self):  # pragma: no cover
        return ValidationException.make_one(self.boto3_raw_data["validationException"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OptimizedPromptStreamTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OptimizedPromptStreamTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FlowExecutionEvent:
    boto3_raw_data: "type_defs.FlowExecutionEventTypeDef" = dataclasses.field()

    @cached_property
    def conditionResultEvent(self):  # pragma: no cover
        return ConditionResultEvent.make_one(
            self.boto3_raw_data["conditionResultEvent"]
        )

    @cached_property
    def flowFailureEvent(self):  # pragma: no cover
        return FlowFailureEvent.make_one(self.boto3_raw_data["flowFailureEvent"])

    @cached_property
    def flowInputEvent(self):  # pragma: no cover
        return FlowExecutionInputEvent.make_one(self.boto3_raw_data["flowInputEvent"])

    @cached_property
    def flowOutputEvent(self):  # pragma: no cover
        return FlowExecutionOutputEvent.make_one(self.boto3_raw_data["flowOutputEvent"])

    @cached_property
    def nodeFailureEvent(self):  # pragma: no cover
        return NodeFailureEvent.make_one(self.boto3_raw_data["nodeFailureEvent"])

    @cached_property
    def nodeInputEvent(self):  # pragma: no cover
        return NodeInputEvent.make_one(self.boto3_raw_data["nodeInputEvent"])

    @cached_property
    def nodeOutputEvent(self):  # pragma: no cover
        return NodeOutputEvent.make_one(self.boto3_raw_data["nodeOutputEvent"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FlowExecutionEventTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FlowExecutionEventTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PostProcessingTrace:
    boto3_raw_data: "type_defs.PostProcessingTraceTypeDef" = dataclasses.field()

    @cached_property
    def modelInvocationInput(self):  # pragma: no cover
        return ModelInvocationInput.make_one(
            self.boto3_raw_data["modelInvocationInput"]
        )

    @cached_property
    def modelInvocationOutput(self):  # pragma: no cover
        return PostProcessingModelInvocationOutput.make_one(
            self.boto3_raw_data["modelInvocationOutput"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PostProcessingTraceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PostProcessingTraceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PreProcessingTrace:
    boto3_raw_data: "type_defs.PreProcessingTraceTypeDef" = dataclasses.field()

    @cached_property
    def modelInvocationInput(self):  # pragma: no cover
        return ModelInvocationInput.make_one(
            self.boto3_raw_data["modelInvocationInput"]
        )

    @cached_property
    def modelInvocationOutput(self):  # pragma: no cover
        return PreProcessingModelInvocationOutput.make_one(
            self.boto3_raw_data["modelInvocationOutput"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PreProcessingTraceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PreProcessingTraceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RerankResponse:
    boto3_raw_data: "type_defs.RerankResponseTypeDef" = dataclasses.field()

    @cached_property
    def results(self):  # pragma: no cover
        return RerankResult.make_many(self.boto3_raw_data["results"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RerankResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RerankResponseTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RerankSource:
    boto3_raw_data: "type_defs.RerankSourceTypeDef" = dataclasses.field()

    inlineDocumentSource = field("inlineDocumentSource")
    type = field("type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RerankSourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RerankSourceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RetrieveResponse:
    boto3_raw_data: "type_defs.RetrieveResponseTypeDef" = dataclasses.field()

    guardrailAction = field("guardrailAction")

    @cached_property
    def retrievalResults(self):  # pragma: no cover
        return KnowledgeBaseRetrievalResult.make_many(
            self.boto3_raw_data["retrievalResults"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RetrieveResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RetrieveResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KnowledgeBaseLookupOutput:
    boto3_raw_data: "type_defs.KnowledgeBaseLookupOutputTypeDef" = dataclasses.field()

    @cached_property
    def metadata(self):  # pragma: no cover
        return Metadata.make_one(self.boto3_raw_data["metadata"])

    @cached_property
    def retrievedReferences(self):  # pragma: no cover
        return RetrievedReference.make_many(self.boto3_raw_data["retrievedReferences"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KnowledgeBaseLookupOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KnowledgeBaseLookupOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Citation:
    boto3_raw_data: "type_defs.CitationTypeDef" = dataclasses.field()

    @cached_property
    def generatedResponsePart(self):  # pragma: no cover
        return GeneratedResponsePart.make_one(
            self.boto3_raw_data["generatedResponsePart"]
        )

    @cached_property
    def retrievedReferences(self):  # pragma: no cover
        return RetrievedReference.make_many(self.boto3_raw_data["retrievedReferences"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CitationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CitationTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GenerateQueryRequest:
    boto3_raw_data: "type_defs.GenerateQueryRequestTypeDef" = dataclasses.field()

    @cached_property
    def queryGenerationInput(self):  # pragma: no cover
        return QueryGenerationInput.make_one(
            self.boto3_raw_data["queryGenerationInput"]
        )

    @cached_property
    def transformationConfiguration(self):  # pragma: no cover
        return TransformationConfiguration.make_one(
            self.boto3_raw_data["transformationConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GenerateQueryRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GenerateQueryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InvocationInputMember:
    boto3_raw_data: "type_defs.InvocationInputMemberTypeDef" = dataclasses.field()

    @cached_property
    def apiInvocationInput(self):  # pragma: no cover
        return ApiInvocationInput.make_one(self.boto3_raw_data["apiInvocationInput"])

    @cached_property
    def functionInvocationInput(self):  # pragma: no cover
        return FunctionInvocationInput.make_one(
            self.boto3_raw_data["functionInvocationInput"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InvocationInputMemberTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InvocationInputMemberTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VectorSearchRerankingConfiguration:
    boto3_raw_data: "type_defs.VectorSearchRerankingConfigurationTypeDef" = (
        dataclasses.field()
    )

    type = field("type")

    @cached_property
    def bedrockRerankingConfiguration(self):  # pragma: no cover
        return VectorSearchBedrockRerankingConfiguration.make_one(
            self.boto3_raw_data["bedrockRerankingConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.VectorSearchRerankingConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VectorSearchRerankingConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FlowTraceEvent:
    boto3_raw_data: "type_defs.FlowTraceEventTypeDef" = dataclasses.field()

    @cached_property
    def trace(self):  # pragma: no cover
        return FlowTrace.make_one(self.boto3_raw_data["trace"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FlowTraceEventTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FlowTraceEventTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InvocationResultMemberOutput:
    boto3_raw_data: "type_defs.InvocationResultMemberOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def apiResult(self):  # pragma: no cover
        return ApiResultOutput.make_one(self.boto3_raw_data["apiResult"])

    @cached_property
    def functionResult(self):  # pragma: no cover
        return FunctionResultOutput.make_one(self.boto3_raw_data["functionResult"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InvocationResultMemberOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InvocationResultMemberOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InvocationStepPayloadOutput:
    boto3_raw_data: "type_defs.InvocationStepPayloadOutputTypeDef" = dataclasses.field()

    @cached_property
    def contentBlocks(self):  # pragma: no cover
        return BedrockSessionContentBlockOutput.make_many(
            self.boto3_raw_data["contentBlocks"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InvocationStepPayloadOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InvocationStepPayloadOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InvocationStepPayload:
    boto3_raw_data: "type_defs.InvocationStepPayloadTypeDef" = dataclasses.field()

    @cached_property
    def contentBlocks(self):  # pragma: no cover
        return BedrockSessionContentBlock.make_many(
            self.boto3_raw_data["contentBlocks"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InvocationStepPayloadTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InvocationStepPayloadTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OptimizePromptResponse:
    boto3_raw_data: "type_defs.OptimizePromptResponseTypeDef" = dataclasses.field()

    optimizedPrompt = field("optimizedPrompt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OptimizePromptResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OptimizePromptResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFlowExecutionEventsResponse:
    boto3_raw_data: "type_defs.ListFlowExecutionEventsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def flowExecutionEvents(self):  # pragma: no cover
        return FlowExecutionEvent.make_many(self.boto3_raw_data["flowExecutionEvents"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListFlowExecutionEventsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFlowExecutionEventsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RerankRequestPaginate:
    boto3_raw_data: "type_defs.RerankRequestPaginateTypeDef" = dataclasses.field()

    @cached_property
    def queries(self):  # pragma: no cover
        return RerankQuery.make_many(self.boto3_raw_data["queries"])

    @cached_property
    def rerankingConfiguration(self):  # pragma: no cover
        return RerankingConfiguration.make_one(
            self.boto3_raw_data["rerankingConfiguration"]
        )

    @cached_property
    def sources(self):  # pragma: no cover
        return RerankSource.make_many(self.boto3_raw_data["sources"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RerankRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RerankRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RerankRequest:
    boto3_raw_data: "type_defs.RerankRequestTypeDef" = dataclasses.field()

    @cached_property
    def queries(self):  # pragma: no cover
        return RerankQuery.make_many(self.boto3_raw_data["queries"])

    @cached_property
    def rerankingConfiguration(self):  # pragma: no cover
        return RerankingConfiguration.make_one(
            self.boto3_raw_data["rerankingConfiguration"]
        )

    @cached_property
    def sources(self):  # pragma: no cover
        return RerankSource.make_many(self.boto3_raw_data["sources"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RerankRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RerankRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Attribution:
    boto3_raw_data: "type_defs.AttributionTypeDef" = dataclasses.field()

    @cached_property
    def citations(self):  # pragma: no cover
        return Citation.make_many(self.boto3_raw_data["citations"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AttributionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AttributionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CitationEvent:
    boto3_raw_data: "type_defs.CitationEventTypeDef" = dataclasses.field()

    @cached_property
    def citation(self):  # pragma: no cover
        return Citation.make_one(self.boto3_raw_data["citation"])

    @cached_property
    def generatedResponsePart(self):  # pragma: no cover
        return GeneratedResponsePart.make_one(
            self.boto3_raw_data["generatedResponsePart"]
        )

    @cached_property
    def retrievedReferences(self):  # pragma: no cover
        return RetrievedReference.make_many(self.boto3_raw_data["retrievedReferences"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CitationEventTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CitationEventTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RetrieveAndGenerateResponse:
    boto3_raw_data: "type_defs.RetrieveAndGenerateResponseTypeDef" = dataclasses.field()

    @cached_property
    def citations(self):  # pragma: no cover
        return Citation.make_many(self.boto3_raw_data["citations"])

    guardrailAction = field("guardrailAction")

    @cached_property
    def output(self):  # pragma: no cover
        return RetrieveAndGenerateOutput.make_one(self.boto3_raw_data["output"])

    sessionId = field("sessionId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RetrieveAndGenerateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RetrieveAndGenerateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InlineAgentReturnControlPayload:
    boto3_raw_data: "type_defs.InlineAgentReturnControlPayloadTypeDef" = (
        dataclasses.field()
    )

    invocationId = field("invocationId")

    @cached_property
    def invocationInputs(self):  # pragma: no cover
        return InvocationInputMember.make_many(self.boto3_raw_data["invocationInputs"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.InlineAgentReturnControlPayloadTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InlineAgentReturnControlPayloadTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReturnControlPayload:
    boto3_raw_data: "type_defs.ReturnControlPayloadTypeDef" = dataclasses.field()

    invocationId = field("invocationId")

    @cached_property
    def invocationInputs(self):  # pragma: no cover
        return InvocationInputMember.make_many(self.boto3_raw_data["invocationInputs"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReturnControlPayloadTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReturnControlPayloadTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContentBody:
    boto3_raw_data: "type_defs.ContentBodyTypeDef" = dataclasses.field()

    body = field("body")
    images = field("images")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ContentBodyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ContentBodyTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KnowledgeBaseVectorSearchConfigurationPaginator:
    boto3_raw_data: (
        "type_defs.KnowledgeBaseVectorSearchConfigurationPaginatorTypeDef"
    ) = dataclasses.field()

    @cached_property
    def filter(self):  # pragma: no cover
        return RetrievalFilterPaginator.make_one(self.boto3_raw_data["filter"])

    @cached_property
    def implicitFilterConfiguration(self):  # pragma: no cover
        return ImplicitFilterConfiguration.make_one(
            self.boto3_raw_data["implicitFilterConfiguration"]
        )

    numberOfResults = field("numberOfResults")
    overrideSearchType = field("overrideSearchType")

    @cached_property
    def rerankingConfiguration(self):  # pragma: no cover
        return VectorSearchRerankingConfiguration.make_one(
            self.boto3_raw_data["rerankingConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.KnowledgeBaseVectorSearchConfigurationPaginatorTypeDef"
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
                "type_defs.KnowledgeBaseVectorSearchConfigurationPaginatorTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KnowledgeBaseVectorSearchConfiguration:
    boto3_raw_data: "type_defs.KnowledgeBaseVectorSearchConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def filter(self):  # pragma: no cover
        return RetrievalFilter.make_one(self.boto3_raw_data["filter"])

    @cached_property
    def implicitFilterConfiguration(self):  # pragma: no cover
        return ImplicitFilterConfiguration.make_one(
            self.boto3_raw_data["implicitFilterConfiguration"]
        )

    numberOfResults = field("numberOfResults")
    overrideSearchType = field("overrideSearchType")

    @cached_property
    def rerankingConfiguration(self):  # pragma: no cover
        return VectorSearchRerankingConfiguration.make_one(
            self.boto3_raw_data["rerankingConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.KnowledgeBaseVectorSearchConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KnowledgeBaseVectorSearchConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FlowResponseStream:
    boto3_raw_data: "type_defs.FlowResponseStreamTypeDef" = dataclasses.field()

    @cached_property
    def accessDeniedException(self):  # pragma: no cover
        return AccessDeniedException.make_one(
            self.boto3_raw_data["accessDeniedException"]
        )

    @cached_property
    def badGatewayException(self):  # pragma: no cover
        return BadGatewayException.make_one(self.boto3_raw_data["badGatewayException"])

    @cached_property
    def conflictException(self):  # pragma: no cover
        return ConflictException.make_one(self.boto3_raw_data["conflictException"])

    @cached_property
    def dependencyFailedException(self):  # pragma: no cover
        return DependencyFailedException.make_one(
            self.boto3_raw_data["dependencyFailedException"]
        )

    @cached_property
    def flowCompletionEvent(self):  # pragma: no cover
        return FlowCompletionEvent.make_one(self.boto3_raw_data["flowCompletionEvent"])

    @cached_property
    def flowMultiTurnInputRequestEvent(self):  # pragma: no cover
        return FlowMultiTurnInputRequestEvent.make_one(
            self.boto3_raw_data["flowMultiTurnInputRequestEvent"]
        )

    @cached_property
    def flowOutputEvent(self):  # pragma: no cover
        return FlowOutputEvent.make_one(self.boto3_raw_data["flowOutputEvent"])

    @cached_property
    def flowTraceEvent(self):  # pragma: no cover
        return FlowTraceEvent.make_one(self.boto3_raw_data["flowTraceEvent"])

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
        cls, boto3_raw_data: T.Optional["type_defs.FlowResponseStreamTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FlowResponseStreamTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReturnControlResults:
    boto3_raw_data: "type_defs.ReturnControlResultsTypeDef" = dataclasses.field()

    invocationId = field("invocationId")

    @cached_property
    def returnControlInvocationResults(self):  # pragma: no cover
        return InvocationResultMemberOutput.make_many(
            self.boto3_raw_data["returnControlInvocationResults"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReturnControlResultsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReturnControlResultsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InvocationStep:
    boto3_raw_data: "type_defs.InvocationStepTypeDef" = dataclasses.field()

    invocationId = field("invocationId")
    invocationStepId = field("invocationStepId")
    invocationStepTime = field("invocationStepTime")

    @cached_property
    def payload(self):  # pragma: no cover
        return InvocationStepPayloadOutput.make_one(self.boto3_raw_data["payload"])

    sessionId = field("sessionId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InvocationStepTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InvocationStepTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InlineAgentPayloadPart:
    boto3_raw_data: "type_defs.InlineAgentPayloadPartTypeDef" = dataclasses.field()

    @cached_property
    def attribution(self):  # pragma: no cover
        return Attribution.make_one(self.boto3_raw_data["attribution"])

    bytes = field("bytes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InlineAgentPayloadPartTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InlineAgentPayloadPartTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PayloadPart:
    boto3_raw_data: "type_defs.PayloadPartTypeDef" = dataclasses.field()

    @cached_property
    def attribution(self):  # pragma: no cover
        return Attribution.make_one(self.boto3_raw_data["attribution"])

    bytes = field("bytes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PayloadPartTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PayloadPartTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RetrieveAndGenerateStreamResponseOutput:
    boto3_raw_data: "type_defs.RetrieveAndGenerateStreamResponseOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def accessDeniedException(self):  # pragma: no cover
        return AccessDeniedException.make_one(
            self.boto3_raw_data["accessDeniedException"]
        )

    @cached_property
    def badGatewayException(self):  # pragma: no cover
        return BadGatewayException.make_one(self.boto3_raw_data["badGatewayException"])

    @cached_property
    def citation(self):  # pragma: no cover
        return CitationEvent.make_one(self.boto3_raw_data["citation"])

    @cached_property
    def conflictException(self):  # pragma: no cover
        return ConflictException.make_one(self.boto3_raw_data["conflictException"])

    @cached_property
    def dependencyFailedException(self):  # pragma: no cover
        return DependencyFailedException.make_one(
            self.boto3_raw_data["dependencyFailedException"]
        )

    @cached_property
    def guardrail(self):  # pragma: no cover
        return GuardrailEvent.make_one(self.boto3_raw_data["guardrail"])

    @cached_property
    def internalServerException(self):  # pragma: no cover
        return InternalServerException.make_one(
            self.boto3_raw_data["internalServerException"]
        )

    @cached_property
    def output(self):  # pragma: no cover
        return RetrieveAndGenerateOutputEvent.make_one(self.boto3_raw_data["output"])

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
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RetrieveAndGenerateStreamResponseOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RetrieveAndGenerateStreamResponseOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AgentCollaboratorOutputPayload:
    boto3_raw_data: "type_defs.AgentCollaboratorOutputPayloadTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def returnControlPayload(self):  # pragma: no cover
        return ReturnControlPayload.make_one(
            self.boto3_raw_data["returnControlPayload"]
        )

    text = field("text")
    type = field("type")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AgentCollaboratorOutputPayloadTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AgentCollaboratorOutputPayloadTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KnowledgeBaseRetrievalConfigurationPaginator:
    boto3_raw_data: "type_defs.KnowledgeBaseRetrievalConfigurationPaginatorTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def vectorSearchConfiguration(self):  # pragma: no cover
        return KnowledgeBaseVectorSearchConfigurationPaginator.make_one(
            self.boto3_raw_data["vectorSearchConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.KnowledgeBaseRetrievalConfigurationPaginatorTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KnowledgeBaseRetrievalConfigurationPaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KnowledgeBaseRetrievalConfiguration:
    boto3_raw_data: "type_defs.KnowledgeBaseRetrievalConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def vectorSearchConfiguration(self):  # pragma: no cover
        return KnowledgeBaseVectorSearchConfiguration.make_one(
            self.boto3_raw_data["vectorSearchConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.KnowledgeBaseRetrievalConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KnowledgeBaseRetrievalConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InvokeFlowResponse:
    boto3_raw_data: "type_defs.InvokeFlowResponseTypeDef" = dataclasses.field()

    executionId = field("executionId")
    responseStream = field("responseStream")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InvokeFlowResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InvokeFlowResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AgentCollaboratorInputPayload:
    boto3_raw_data: "type_defs.AgentCollaboratorInputPayloadTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def returnControlResults(self):  # pragma: no cover
        return ReturnControlResults.make_one(
            self.boto3_raw_data["returnControlResults"]
        )

    text = field("text")
    type = field("type")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AgentCollaboratorInputPayloadTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AgentCollaboratorInputPayloadTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetInvocationStepResponse:
    boto3_raw_data: "type_defs.GetInvocationStepResponseTypeDef" = dataclasses.field()

    @cached_property
    def invocationStep(self):  # pragma: no cover
        return InvocationStep.make_one(self.boto3_raw_data["invocationStep"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetInvocationStepResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetInvocationStepResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutInvocationStepRequest:
    boto3_raw_data: "type_defs.PutInvocationStepRequestTypeDef" = dataclasses.field()

    invocationIdentifier = field("invocationIdentifier")
    invocationStepTime = field("invocationStepTime")
    payload = field("payload")
    sessionIdentifier = field("sessionIdentifier")
    invocationStepId = field("invocationStepId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutInvocationStepRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutInvocationStepRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RetrieveAndGenerateStreamResponse:
    boto3_raw_data: "type_defs.RetrieveAndGenerateStreamResponseTypeDef" = (
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
        boto3_raw_data: T.Optional[
            "type_defs.RetrieveAndGenerateStreamResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RetrieveAndGenerateStreamResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AgentCollaboratorInvocationOutput:
    boto3_raw_data: "type_defs.AgentCollaboratorInvocationOutputTypeDef" = (
        dataclasses.field()
    )

    agentCollaboratorAliasArn = field("agentCollaboratorAliasArn")
    agentCollaboratorName = field("agentCollaboratorName")

    @cached_property
    def metadata(self):  # pragma: no cover
        return Metadata.make_one(self.boto3_raw_data["metadata"])

    @cached_property
    def output(self):  # pragma: no cover
        return AgentCollaboratorOutputPayload.make_one(self.boto3_raw_data["output"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AgentCollaboratorInvocationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AgentCollaboratorInvocationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApiResult:
    boto3_raw_data: "type_defs.ApiResultTypeDef" = dataclasses.field()

    actionGroup = field("actionGroup")
    agentId = field("agentId")
    apiPath = field("apiPath")
    confirmationState = field("confirmationState")
    httpMethod = field("httpMethod")
    httpStatusCode = field("httpStatusCode")
    responseBody = field("responseBody")
    responseState = field("responseState")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ApiResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ApiResultTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FunctionResult:
    boto3_raw_data: "type_defs.FunctionResultTypeDef" = dataclasses.field()

    actionGroup = field("actionGroup")
    agentId = field("agentId")
    confirmationState = field("confirmationState")
    function = field("function")
    responseBody = field("responseBody")
    responseState = field("responseState")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FunctionResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FunctionResultTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RetrieveRequestPaginate:
    boto3_raw_data: "type_defs.RetrieveRequestPaginateTypeDef" = dataclasses.field()

    knowledgeBaseId = field("knowledgeBaseId")

    @cached_property
    def retrievalQuery(self):  # pragma: no cover
        return KnowledgeBaseQuery.make_one(self.boto3_raw_data["retrievalQuery"])

    @cached_property
    def guardrailConfiguration(self):  # pragma: no cover
        return GuardrailConfiguration.make_one(
            self.boto3_raw_data["guardrailConfiguration"]
        )

    @cached_property
    def retrievalConfiguration(self):  # pragma: no cover
        return KnowledgeBaseRetrievalConfigurationPaginator.make_one(
            self.boto3_raw_data["retrievalConfiguration"]
        )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RetrieveRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RetrieveRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KnowledgeBaseConfiguration:
    boto3_raw_data: "type_defs.KnowledgeBaseConfigurationTypeDef" = dataclasses.field()

    knowledgeBaseId = field("knowledgeBaseId")

    @cached_property
    def retrievalConfiguration(self):  # pragma: no cover
        return KnowledgeBaseRetrievalConfiguration.make_one(
            self.boto3_raw_data["retrievalConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KnowledgeBaseConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KnowledgeBaseConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KnowledgeBaseRetrieveAndGenerateConfiguration:
    boto3_raw_data: "type_defs.KnowledgeBaseRetrieveAndGenerateConfigurationTypeDef" = (
        dataclasses.field()
    )

    knowledgeBaseId = field("knowledgeBaseId")
    modelArn = field("modelArn")

    @cached_property
    def generationConfiguration(self):  # pragma: no cover
        return GenerationConfiguration.make_one(
            self.boto3_raw_data["generationConfiguration"]
        )

    @cached_property
    def orchestrationConfiguration(self):  # pragma: no cover
        return OrchestrationConfiguration.make_one(
            self.boto3_raw_data["orchestrationConfiguration"]
        )

    @cached_property
    def retrievalConfiguration(self):  # pragma: no cover
        return KnowledgeBaseRetrievalConfiguration.make_one(
            self.boto3_raw_data["retrievalConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.KnowledgeBaseRetrieveAndGenerateConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KnowledgeBaseRetrieveAndGenerateConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KnowledgeBase:
    boto3_raw_data: "type_defs.KnowledgeBaseTypeDef" = dataclasses.field()

    description = field("description")
    knowledgeBaseId = field("knowledgeBaseId")

    @cached_property
    def retrievalConfiguration(self):  # pragma: no cover
        return KnowledgeBaseRetrievalConfiguration.make_one(
            self.boto3_raw_data["retrievalConfiguration"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.KnowledgeBaseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.KnowledgeBaseTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RetrieveRequest:
    boto3_raw_data: "type_defs.RetrieveRequestTypeDef" = dataclasses.field()

    knowledgeBaseId = field("knowledgeBaseId")

    @cached_property
    def retrievalQuery(self):  # pragma: no cover
        return KnowledgeBaseQuery.make_one(self.boto3_raw_data["retrievalQuery"])

    @cached_property
    def guardrailConfiguration(self):  # pragma: no cover
        return GuardrailConfiguration.make_one(
            self.boto3_raw_data["guardrailConfiguration"]
        )

    nextToken = field("nextToken")

    @cached_property
    def retrievalConfiguration(self):  # pragma: no cover
        return KnowledgeBaseRetrievalConfiguration.make_one(
            self.boto3_raw_data["retrievalConfiguration"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RetrieveRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RetrieveRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AgentCollaboratorInvocationInput:
    boto3_raw_data: "type_defs.AgentCollaboratorInvocationInputTypeDef" = (
        dataclasses.field()
    )

    agentCollaboratorAliasArn = field("agentCollaboratorAliasArn")
    agentCollaboratorName = field("agentCollaboratorName")

    @cached_property
    def input(self):  # pragma: no cover
        return AgentCollaboratorInputPayload.make_one(self.boto3_raw_data["input"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AgentCollaboratorInvocationInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AgentCollaboratorInvocationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Observation:
    boto3_raw_data: "type_defs.ObservationTypeDef" = dataclasses.field()

    @cached_property
    def actionGroupInvocationOutput(self):  # pragma: no cover
        return ActionGroupInvocationOutput.make_one(
            self.boto3_raw_data["actionGroupInvocationOutput"]
        )

    @cached_property
    def agentCollaboratorInvocationOutput(self):  # pragma: no cover
        return AgentCollaboratorInvocationOutput.make_one(
            self.boto3_raw_data["agentCollaboratorInvocationOutput"]
        )

    @cached_property
    def codeInterpreterInvocationOutput(self):  # pragma: no cover
        return CodeInterpreterInvocationOutput.make_one(
            self.boto3_raw_data["codeInterpreterInvocationOutput"]
        )

    @cached_property
    def finalResponse(self):  # pragma: no cover
        return FinalResponse.make_one(self.boto3_raw_data["finalResponse"])

    @cached_property
    def knowledgeBaseLookupOutput(self):  # pragma: no cover
        return KnowledgeBaseLookupOutput.make_one(
            self.boto3_raw_data["knowledgeBaseLookupOutput"]
        )

    @cached_property
    def repromptResponse(self):  # pragma: no cover
        return RepromptResponse.make_one(self.boto3_raw_data["repromptResponse"])

    traceId = field("traceId")
    type = field("type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ObservationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ObservationTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RetrieveAndGenerateConfiguration:
    boto3_raw_data: "type_defs.RetrieveAndGenerateConfigurationTypeDef" = (
        dataclasses.field()
    )

    type = field("type")

    @cached_property
    def externalSourcesConfiguration(self):  # pragma: no cover
        return ExternalSourcesRetrieveAndGenerateConfiguration.make_one(
            self.boto3_raw_data["externalSourcesConfiguration"]
        )

    @cached_property
    def knowledgeBaseConfiguration(self):  # pragma: no cover
        return KnowledgeBaseRetrieveAndGenerateConfiguration.make_one(
            self.boto3_raw_data["knowledgeBaseConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RetrieveAndGenerateConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RetrieveAndGenerateConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Collaborator:
    boto3_raw_data: "type_defs.CollaboratorTypeDef" = dataclasses.field()

    foundationModel = field("foundationModel")
    instruction = field("instruction")

    @cached_property
    def actionGroups(self):  # pragma: no cover
        return AgentActionGroup.make_many(self.boto3_raw_data["actionGroups"])

    agentCollaboration = field("agentCollaboration")
    agentName = field("agentName")

    @cached_property
    def collaboratorConfigurations(self):  # pragma: no cover
        return CollaboratorConfiguration.make_many(
            self.boto3_raw_data["collaboratorConfigurations"]
        )

    customerEncryptionKeyArn = field("customerEncryptionKeyArn")

    @cached_property
    def guardrailConfiguration(self):  # pragma: no cover
        return GuardrailConfigurationWithArn.make_one(
            self.boto3_raw_data["guardrailConfiguration"]
        )

    idleSessionTTLInSeconds = field("idleSessionTTLInSeconds")

    @cached_property
    def knowledgeBases(self):  # pragma: no cover
        return KnowledgeBase.make_many(self.boto3_raw_data["knowledgeBases"])

    @cached_property
    def promptOverrideConfiguration(self):  # pragma: no cover
        return PromptOverrideConfiguration.make_one(
            self.boto3_raw_data["promptOverrideConfiguration"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CollaboratorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CollaboratorTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InvocationInput:
    boto3_raw_data: "type_defs.InvocationInputTypeDef" = dataclasses.field()

    @cached_property
    def actionGroupInvocationInput(self):  # pragma: no cover
        return ActionGroupInvocationInput.make_one(
            self.boto3_raw_data["actionGroupInvocationInput"]
        )

    @cached_property
    def agentCollaboratorInvocationInput(self):  # pragma: no cover
        return AgentCollaboratorInvocationInput.make_one(
            self.boto3_raw_data["agentCollaboratorInvocationInput"]
        )

    @cached_property
    def codeInterpreterInvocationInput(self):  # pragma: no cover
        return CodeInterpreterInvocationInput.make_one(
            self.boto3_raw_data["codeInterpreterInvocationInput"]
        )

    invocationType = field("invocationType")

    @cached_property
    def knowledgeBaseLookupInput(self):  # pragma: no cover
        return KnowledgeBaseLookupInput.make_one(
            self.boto3_raw_data["knowledgeBaseLookupInput"]
        )

    traceId = field("traceId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InvocationInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InvocationInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InvocationResultMember:
    boto3_raw_data: "type_defs.InvocationResultMemberTypeDef" = dataclasses.field()

    apiResult = field("apiResult")
    functionResult = field("functionResult")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InvocationResultMemberTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InvocationResultMemberTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RetrieveAndGenerateRequest:
    boto3_raw_data: "type_defs.RetrieveAndGenerateRequestTypeDef" = dataclasses.field()

    @cached_property
    def input(self):  # pragma: no cover
        return RetrieveAndGenerateInput.make_one(self.boto3_raw_data["input"])

    @cached_property
    def retrieveAndGenerateConfiguration(self):  # pragma: no cover
        return RetrieveAndGenerateConfiguration.make_one(
            self.boto3_raw_data["retrieveAndGenerateConfiguration"]
        )

    @cached_property
    def sessionConfiguration(self):  # pragma: no cover
        return RetrieveAndGenerateSessionConfiguration.make_one(
            self.boto3_raw_data["sessionConfiguration"]
        )

    sessionId = field("sessionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RetrieveAndGenerateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RetrieveAndGenerateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RetrieveAndGenerateStreamRequest:
    boto3_raw_data: "type_defs.RetrieveAndGenerateStreamRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def input(self):  # pragma: no cover
        return RetrieveAndGenerateInput.make_one(self.boto3_raw_data["input"])

    @cached_property
    def retrieveAndGenerateConfiguration(self):  # pragma: no cover
        return RetrieveAndGenerateConfiguration.make_one(
            self.boto3_raw_data["retrieveAndGenerateConfiguration"]
        )

    @cached_property
    def sessionConfiguration(self):  # pragma: no cover
        return RetrieveAndGenerateSessionConfiguration.make_one(
            self.boto3_raw_data["sessionConfiguration"]
        )

    sessionId = field("sessionId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RetrieveAndGenerateStreamRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RetrieveAndGenerateStreamRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OrchestrationTrace:
    boto3_raw_data: "type_defs.OrchestrationTraceTypeDef" = dataclasses.field()

    @cached_property
    def invocationInput(self):  # pragma: no cover
        return InvocationInput.make_one(self.boto3_raw_data["invocationInput"])

    @cached_property
    def modelInvocationInput(self):  # pragma: no cover
        return ModelInvocationInput.make_one(
            self.boto3_raw_data["modelInvocationInput"]
        )

    @cached_property
    def modelInvocationOutput(self):  # pragma: no cover
        return OrchestrationModelInvocationOutput.make_one(
            self.boto3_raw_data["modelInvocationOutput"]
        )

    @cached_property
    def observation(self):  # pragma: no cover
        return Observation.make_one(self.boto3_raw_data["observation"])

    @cached_property
    def rationale(self):  # pragma: no cover
        return Rationale.make_one(self.boto3_raw_data["rationale"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OrchestrationTraceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OrchestrationTraceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RoutingClassifierTrace:
    boto3_raw_data: "type_defs.RoutingClassifierTraceTypeDef" = dataclasses.field()

    @cached_property
    def invocationInput(self):  # pragma: no cover
        return InvocationInput.make_one(self.boto3_raw_data["invocationInput"])

    @cached_property
    def modelInvocationInput(self):  # pragma: no cover
        return ModelInvocationInput.make_one(
            self.boto3_raw_data["modelInvocationInput"]
        )

    @cached_property
    def modelInvocationOutput(self):  # pragma: no cover
        return RoutingClassifierModelInvocationOutput.make_one(
            self.boto3_raw_data["modelInvocationOutput"]
        )

    @cached_property
    def observation(self):  # pragma: no cover
        return Observation.make_one(self.boto3_raw_data["observation"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RoutingClassifierTraceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RoutingClassifierTraceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Trace:
    boto3_raw_data: "type_defs.TraceTypeDef" = dataclasses.field()

    @cached_property
    def customOrchestrationTrace(self):  # pragma: no cover
        return CustomOrchestrationTrace.make_one(
            self.boto3_raw_data["customOrchestrationTrace"]
        )

    @cached_property
    def failureTrace(self):  # pragma: no cover
        return FailureTrace.make_one(self.boto3_raw_data["failureTrace"])

    @cached_property
    def guardrailTrace(self):  # pragma: no cover
        return GuardrailTrace.make_one(self.boto3_raw_data["guardrailTrace"])

    @cached_property
    def orchestrationTrace(self):  # pragma: no cover
        return OrchestrationTrace.make_one(self.boto3_raw_data["orchestrationTrace"])

    @cached_property
    def postProcessingTrace(self):  # pragma: no cover
        return PostProcessingTrace.make_one(self.boto3_raw_data["postProcessingTrace"])

    @cached_property
    def preProcessingTrace(self):  # pragma: no cover
        return PreProcessingTrace.make_one(self.boto3_raw_data["preProcessingTrace"])

    @cached_property
    def routingClassifierTrace(self):  # pragma: no cover
        return RoutingClassifierTrace.make_one(
            self.boto3_raw_data["routingClassifierTrace"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TraceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TraceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InlineSessionState:
    boto3_raw_data: "type_defs.InlineSessionStateTypeDef" = dataclasses.field()

    @cached_property
    def conversationHistory(self):  # pragma: no cover
        return ConversationHistory.make_one(self.boto3_raw_data["conversationHistory"])

    @cached_property
    def files(self):  # pragma: no cover
        return InputFile.make_many(self.boto3_raw_data["files"])

    invocationId = field("invocationId")
    promptSessionAttributes = field("promptSessionAttributes")
    returnControlInvocationResults = field("returnControlInvocationResults")
    sessionAttributes = field("sessionAttributes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InlineSessionStateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InlineSessionStateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SessionState:
    boto3_raw_data: "type_defs.SessionStateTypeDef" = dataclasses.field()

    @cached_property
    def conversationHistory(self):  # pragma: no cover
        return ConversationHistory.make_one(self.boto3_raw_data["conversationHistory"])

    @cached_property
    def files(self):  # pragma: no cover
        return InputFile.make_many(self.boto3_raw_data["files"])

    invocationId = field("invocationId")

    @cached_property
    def knowledgeBaseConfigurations(self):  # pragma: no cover
        return KnowledgeBaseConfiguration.make_many(
            self.boto3_raw_data["knowledgeBaseConfigurations"]
        )

    promptSessionAttributes = field("promptSessionAttributes")
    returnControlInvocationResults = field("returnControlInvocationResults")
    sessionAttributes = field("sessionAttributes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SessionStateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SessionStateTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InlineAgentTracePart:
    boto3_raw_data: "type_defs.InlineAgentTracePartTypeDef" = dataclasses.field()

    @cached_property
    def callerChain(self):  # pragma: no cover
        return Caller.make_many(self.boto3_raw_data["callerChain"])

    collaboratorName = field("collaboratorName")
    eventTime = field("eventTime")
    sessionId = field("sessionId")

    @cached_property
    def trace(self):  # pragma: no cover
        return Trace.make_one(self.boto3_raw_data["trace"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InlineAgentTracePartTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InlineAgentTracePartTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TracePart:
    boto3_raw_data: "type_defs.TracePartTypeDef" = dataclasses.field()

    agentAliasId = field("agentAliasId")
    agentId = field("agentId")
    agentVersion = field("agentVersion")

    @cached_property
    def callerChain(self):  # pragma: no cover
        return Caller.make_many(self.boto3_raw_data["callerChain"])

    collaboratorName = field("collaboratorName")
    eventTime = field("eventTime")
    sessionId = field("sessionId")

    @cached_property
    def trace(self):  # pragma: no cover
        return Trace.make_one(self.boto3_raw_data["trace"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TracePartTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TracePartTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InvokeInlineAgentRequest:
    boto3_raw_data: "type_defs.InvokeInlineAgentRequestTypeDef" = dataclasses.field()

    foundationModel = field("foundationModel")
    instruction = field("instruction")
    sessionId = field("sessionId")

    @cached_property
    def actionGroups(self):  # pragma: no cover
        return AgentActionGroup.make_many(self.boto3_raw_data["actionGroups"])

    agentCollaboration = field("agentCollaboration")
    agentName = field("agentName")

    @cached_property
    def bedrockModelConfigurations(self):  # pragma: no cover
        return InlineBedrockModelConfigurations.make_one(
            self.boto3_raw_data["bedrockModelConfigurations"]
        )

    @cached_property
    def collaboratorConfigurations(self):  # pragma: no cover
        return CollaboratorConfiguration.make_many(
            self.boto3_raw_data["collaboratorConfigurations"]
        )

    @cached_property
    def collaborators(self):  # pragma: no cover
        return Collaborator.make_many(self.boto3_raw_data["collaborators"])

    @cached_property
    def customOrchestration(self):  # pragma: no cover
        return CustomOrchestration.make_one(self.boto3_raw_data["customOrchestration"])

    customerEncryptionKeyArn = field("customerEncryptionKeyArn")
    enableTrace = field("enableTrace")
    endSession = field("endSession")

    @cached_property
    def guardrailConfiguration(self):  # pragma: no cover
        return GuardrailConfigurationWithArn.make_one(
            self.boto3_raw_data["guardrailConfiguration"]
        )

    idleSessionTTLInSeconds = field("idleSessionTTLInSeconds")

    @cached_property
    def inlineSessionState(self):  # pragma: no cover
        return InlineSessionState.make_one(self.boto3_raw_data["inlineSessionState"])

    inputText = field("inputText")

    @cached_property
    def knowledgeBases(self):  # pragma: no cover
        return KnowledgeBase.make_many(self.boto3_raw_data["knowledgeBases"])

    orchestrationType = field("orchestrationType")

    @cached_property
    def promptCreationConfigurations(self):  # pragma: no cover
        return PromptCreationConfigurations.make_one(
            self.boto3_raw_data["promptCreationConfigurations"]
        )

    @cached_property
    def promptOverrideConfiguration(self):  # pragma: no cover
        return PromptOverrideConfiguration.make_one(
            self.boto3_raw_data["promptOverrideConfiguration"]
        )

    @cached_property
    def streamingConfigurations(self):  # pragma: no cover
        return StreamingConfigurations.make_one(
            self.boto3_raw_data["streamingConfigurations"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InvokeInlineAgentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InvokeInlineAgentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InvokeAgentRequest:
    boto3_raw_data: "type_defs.InvokeAgentRequestTypeDef" = dataclasses.field()

    agentAliasId = field("agentAliasId")
    agentId = field("agentId")
    sessionId = field("sessionId")

    @cached_property
    def bedrockModelConfigurations(self):  # pragma: no cover
        return BedrockModelConfigurations.make_one(
            self.boto3_raw_data["bedrockModelConfigurations"]
        )

    enableTrace = field("enableTrace")
    endSession = field("endSession")
    inputText = field("inputText")
    memoryId = field("memoryId")

    @cached_property
    def promptCreationConfigurations(self):  # pragma: no cover
        return PromptCreationConfigurations.make_one(
            self.boto3_raw_data["promptCreationConfigurations"]
        )

    @cached_property
    def sessionState(self):  # pragma: no cover
        return SessionState.make_one(self.boto3_raw_data["sessionState"])

    sourceArn = field("sourceArn")

    @cached_property
    def streamingConfigurations(self):  # pragma: no cover
        return StreamingConfigurations.make_one(
            self.boto3_raw_data["streamingConfigurations"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InvokeAgentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InvokeAgentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InlineAgentResponseStream:
    boto3_raw_data: "type_defs.InlineAgentResponseStreamTypeDef" = dataclasses.field()

    @cached_property
    def accessDeniedException(self):  # pragma: no cover
        return AccessDeniedException.make_one(
            self.boto3_raw_data["accessDeniedException"]
        )

    @cached_property
    def badGatewayException(self):  # pragma: no cover
        return BadGatewayException.make_one(self.boto3_raw_data["badGatewayException"])

    @cached_property
    def chunk(self):  # pragma: no cover
        return InlineAgentPayloadPart.make_one(self.boto3_raw_data["chunk"])

    @cached_property
    def conflictException(self):  # pragma: no cover
        return ConflictException.make_one(self.boto3_raw_data["conflictException"])

    @cached_property
    def dependencyFailedException(self):  # pragma: no cover
        return DependencyFailedException.make_one(
            self.boto3_raw_data["dependencyFailedException"]
        )

    @cached_property
    def files(self):  # pragma: no cover
        return InlineAgentFilePart.make_one(self.boto3_raw_data["files"])

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
    def returnControl(self):  # pragma: no cover
        return InlineAgentReturnControlPayload.make_one(
            self.boto3_raw_data["returnControl"]
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
    def trace(self):  # pragma: no cover
        return InlineAgentTracePart.make_one(self.boto3_raw_data["trace"])

    @cached_property
    def validationException(self):  # pragma: no cover
        return ValidationException.make_one(self.boto3_raw_data["validationException"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InlineAgentResponseStreamTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InlineAgentResponseStreamTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResponseStream:
    boto3_raw_data: "type_defs.ResponseStreamTypeDef" = dataclasses.field()

    @cached_property
    def accessDeniedException(self):  # pragma: no cover
        return AccessDeniedException.make_one(
            self.boto3_raw_data["accessDeniedException"]
        )

    @cached_property
    def badGatewayException(self):  # pragma: no cover
        return BadGatewayException.make_one(self.boto3_raw_data["badGatewayException"])

    @cached_property
    def chunk(self):  # pragma: no cover
        return PayloadPart.make_one(self.boto3_raw_data["chunk"])

    @cached_property
    def conflictException(self):  # pragma: no cover
        return ConflictException.make_one(self.boto3_raw_data["conflictException"])

    @cached_property
    def dependencyFailedException(self):  # pragma: no cover
        return DependencyFailedException.make_one(
            self.boto3_raw_data["dependencyFailedException"]
        )

    @cached_property
    def files(self):  # pragma: no cover
        return FilePart.make_one(self.boto3_raw_data["files"])

    @cached_property
    def internalServerException(self):  # pragma: no cover
        return InternalServerException.make_one(
            self.boto3_raw_data["internalServerException"]
        )

    @cached_property
    def modelNotReadyException(self):  # pragma: no cover
        return ModelNotReadyException.make_one(
            self.boto3_raw_data["modelNotReadyException"]
        )

    @cached_property
    def resourceNotFoundException(self):  # pragma: no cover
        return ResourceNotFoundException.make_one(
            self.boto3_raw_data["resourceNotFoundException"]
        )

    @cached_property
    def returnControl(self):  # pragma: no cover
        return ReturnControlPayload.make_one(self.boto3_raw_data["returnControl"])

    @cached_property
    def serviceQuotaExceededException(self):  # pragma: no cover
        return ServiceQuotaExceededException.make_one(
            self.boto3_raw_data["serviceQuotaExceededException"]
        )

    @cached_property
    def throttlingException(self):  # pragma: no cover
        return ThrottlingException.make_one(self.boto3_raw_data["throttlingException"])

    @cached_property
    def trace(self):  # pragma: no cover
        return TracePart.make_one(self.boto3_raw_data["trace"])

    @cached_property
    def validationException(self):  # pragma: no cover
        return ValidationException.make_one(self.boto3_raw_data["validationException"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResponseStreamTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResponseStreamTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InvokeInlineAgentResponse:
    boto3_raw_data: "type_defs.InvokeInlineAgentResponseTypeDef" = dataclasses.field()

    completion = field("completion")
    contentType = field("contentType")
    sessionId = field("sessionId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InvokeInlineAgentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InvokeInlineAgentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InvokeAgentResponse:
    boto3_raw_data: "type_defs.InvokeAgentResponseTypeDef" = dataclasses.field()

    completion = field("completion")
    contentType = field("contentType")
    memoryId = field("memoryId")
    sessionId = field("sessionId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InvokeAgentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InvokeAgentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
