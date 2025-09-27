# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_bedrock_runtime import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class GuardrailOutputContent:
    boto3_raw_data: "type_defs.GuardrailOutputContentTypeDef" = dataclasses.field()

    text = field("text")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GuardrailOutputContentTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GuardrailOutputContentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailUsage:
    boto3_raw_data: "type_defs.GuardrailUsageTypeDef" = dataclasses.field()

    topicPolicyUnits = field("topicPolicyUnits")
    contentPolicyUnits = field("contentPolicyUnits")
    wordPolicyUnits = field("wordPolicyUnits")
    sensitiveInformationPolicyUnits = field("sensitiveInformationPolicyUnits")
    sensitiveInformationPolicyFreeUnits = field("sensitiveInformationPolicyFreeUnits")
    contextualGroundingPolicyUnits = field("contextualGroundingPolicyUnits")
    contentPolicyImageUnits = field("contentPolicyImageUnits")
    automatedReasoningPolicyUnits = field("automatedReasoningPolicyUnits")
    automatedReasoningPolicies = field("automatedReasoningPolicies")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GuardrailUsageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GuardrailUsageTypeDef"]],
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
class AsyncInvokeS3OutputDataConfig:
    boto3_raw_data: "type_defs.AsyncInvokeS3OutputDataConfigTypeDef" = (
        dataclasses.field()
    )

    s3Uri = field("s3Uri")
    kmsKeyId = field("kmsKeyId")
    bucketOwner = field("bucketOwner")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AsyncInvokeS3OutputDataConfigTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AsyncInvokeS3OutputDataConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BidirectionalOutputPayloadPart:
    boto3_raw_data: "type_defs.BidirectionalOutputPayloadPartTypeDef" = (
        dataclasses.field()
    )

    bytes = field("bytes")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BidirectionalOutputPayloadPartTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BidirectionalOutputPayloadPartTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CachePointBlock:
    boto3_raw_data: "type_defs.CachePointBlockTypeDef" = dataclasses.field()

    type = field("type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CachePointBlockTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CachePointBlockTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CitationGeneratedContent:
    boto3_raw_data: "type_defs.CitationGeneratedContentTypeDef" = dataclasses.field()

    text = field("text")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CitationGeneratedContentTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CitationGeneratedContentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentCharLocation:
    boto3_raw_data: "type_defs.DocumentCharLocationTypeDef" = dataclasses.field()

    documentIndex = field("documentIndex")
    start = field("start")
    end = field("end")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DocumentCharLocationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentCharLocationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentChunkLocation:
    boto3_raw_data: "type_defs.DocumentChunkLocationTypeDef" = dataclasses.field()

    documentIndex = field("documentIndex")
    start = field("start")
    end = field("end")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DocumentChunkLocationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentChunkLocationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentPageLocation:
    boto3_raw_data: "type_defs.DocumentPageLocationTypeDef" = dataclasses.field()

    documentIndex = field("documentIndex")
    start = field("start")
    end = field("end")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DocumentPageLocationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentPageLocationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CitationSourceContent:
    boto3_raw_data: "type_defs.CitationSourceContentTypeDef" = dataclasses.field()

    text = field("text")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CitationSourceContentTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CitationSourceContentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CitationSourceContentDelta:
    boto3_raw_data: "type_defs.CitationSourceContentDeltaTypeDef" = dataclasses.field()

    text = field("text")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CitationSourceContentDeltaTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CitationSourceContentDeltaTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CitationsConfig:
    boto3_raw_data: "type_defs.CitationsConfigTypeDef" = dataclasses.field()

    enabled = field("enabled")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CitationsConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CitationsConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReasoningContentBlockDelta:
    boto3_raw_data: "type_defs.ReasoningContentBlockDeltaTypeDef" = dataclasses.field()

    text = field("text")
    redactedContent = field("redactedContent")
    signature = field("signature")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReasoningContentBlockDeltaTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReasoningContentBlockDeltaTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ToolUseBlockDelta:
    boto3_raw_data: "type_defs.ToolUseBlockDeltaTypeDef" = dataclasses.field()

    input = field("input")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ToolUseBlockDeltaTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ToolUseBlockDeltaTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ToolUseBlockOutput:
    boto3_raw_data: "type_defs.ToolUseBlockOutputTypeDef" = dataclasses.field()

    toolUseId = field("toolUseId")
    name = field("name")
    input = field("input")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ToolUseBlockOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ToolUseBlockOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ToolUseBlockStart:
    boto3_raw_data: "type_defs.ToolUseBlockStartTypeDef" = dataclasses.field()

    toolUseId = field("toolUseId")
    name = field("name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ToolUseBlockStartTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ToolUseBlockStartTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContentBlockStopEvent:
    boto3_raw_data: "type_defs.ContentBlockStopEventTypeDef" = dataclasses.field()

    contentBlockIndex = field("contentBlockIndex")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContentBlockStopEventTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContentBlockStopEventTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConverseMetrics:
    boto3_raw_data: "type_defs.ConverseMetricsTypeDef" = dataclasses.field()

    latencyMs = field("latencyMs")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConverseMetricsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ConverseMetricsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailConfiguration:
    boto3_raw_data: "type_defs.GuardrailConfigurationTypeDef" = dataclasses.field()

    guardrailIdentifier = field("guardrailIdentifier")
    guardrailVersion = field("guardrailVersion")
    trace = field("trace")

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
class InferenceConfiguration:
    boto3_raw_data: "type_defs.InferenceConfigurationTypeDef" = dataclasses.field()

    maxTokens = field("maxTokens")
    temperature = field("temperature")
    topP = field("topP")
    stopSequences = field("stopSequences")

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
class PromptVariableValues:
    boto3_raw_data: "type_defs.PromptVariableValuesTypeDef" = dataclasses.field()

    text = field("text")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PromptVariableValuesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PromptVariableValuesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TokenUsage:
    boto3_raw_data: "type_defs.TokenUsageTypeDef" = dataclasses.field()

    inputTokens = field("inputTokens")
    outputTokens = field("outputTokens")
    totalTokens = field("totalTokens")
    cacheReadInputTokens = field("cacheReadInputTokens")
    cacheWriteInputTokens = field("cacheWriteInputTokens")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TokenUsageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TokenUsageTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConverseStreamMetrics:
    boto3_raw_data: "type_defs.ConverseStreamMetricsTypeDef" = dataclasses.field()

    latencyMs = field("latencyMs")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConverseStreamMetricsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConverseStreamMetricsTypeDef"]
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
class MessageStartEvent:
    boto3_raw_data: "type_defs.MessageStartEventTypeDef" = dataclasses.field()

    role = field("role")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MessageStartEventTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MessageStartEventTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MessageStopEvent:
    boto3_raw_data: "type_defs.MessageStopEventTypeDef" = dataclasses.field()

    stopReason = field("stopReason")
    additionalModelResponseFields = field("additionalModelResponseFields")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MessageStopEventTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MessageStopEventTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModelStreamErrorException:
    boto3_raw_data: "type_defs.ModelStreamErrorExceptionTypeDef" = dataclasses.field()

    message = field("message")
    originalStatusCode = field("originalStatusCode")
    originalMessage = field("originalMessage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModelStreamErrorExceptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModelStreamErrorExceptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceUnavailableException:
    boto3_raw_data: "type_defs.ServiceUnavailableExceptionTypeDef" = dataclasses.field()

    message = field("message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ServiceUnavailableExceptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceUnavailableExceptionTypeDef"]
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
class GuardrailStreamConfiguration:
    boto3_raw_data: "type_defs.GuardrailStreamConfigurationTypeDef" = (
        dataclasses.field()
    )

    guardrailIdentifier = field("guardrailIdentifier")
    guardrailVersion = field("guardrailVersion")
    trace = field("trace")
    streamProcessingMode = field("streamProcessingMode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GuardrailStreamConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GuardrailStreamConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PromptRouterTrace:
    boto3_raw_data: "type_defs.PromptRouterTraceTypeDef" = dataclasses.field()

    invokedModelId = field("invokedModelId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PromptRouterTraceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PromptRouterTraceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentContentBlock:
    boto3_raw_data: "type_defs.DocumentContentBlockTypeDef" = dataclasses.field()

    text = field("text")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DocumentContentBlockTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentContentBlockTypeDef"]
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
    bucketOwner = field("bucketOwner")

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
class GetAsyncInvokeRequest:
    boto3_raw_data: "type_defs.GetAsyncInvokeRequestTypeDef" = dataclasses.field()

    invocationArn = field("invocationArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAsyncInvokeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAsyncInvokeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailAutomatedReasoningRule:
    boto3_raw_data: "type_defs.GuardrailAutomatedReasoningRuleTypeDef" = (
        dataclasses.field()
    )

    identifier = field("identifier")
    policyVersionArn = field("policyVersionArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GuardrailAutomatedReasoningRuleTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GuardrailAutomatedReasoningRuleTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailAutomatedReasoningInputTextReference:
    boto3_raw_data: "type_defs.GuardrailAutomatedReasoningInputTextReferenceTypeDef" = (
        dataclasses.field()
    )

    text = field("text")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GuardrailAutomatedReasoningInputTextReferenceTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GuardrailAutomatedReasoningInputTextReferenceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailAutomatedReasoningStatement:
    boto3_raw_data: "type_defs.GuardrailAutomatedReasoningStatementTypeDef" = (
        dataclasses.field()
    )

    logic = field("logic")
    naturalLanguage = field("naturalLanguage")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GuardrailAutomatedReasoningStatementTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GuardrailAutomatedReasoningStatementTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailTextBlock:
    boto3_raw_data: "type_defs.GuardrailTextBlockTypeDef" = dataclasses.field()

    text = field("text")
    qualifiers = field("qualifiers")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GuardrailTextBlockTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GuardrailTextBlockTypeDef"]
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

    type = field("type")
    confidence = field("confidence")
    action = field("action")
    filterStrength = field("filterStrength")
    detected = field("detected")

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
class GuardrailContextualGroundingFilter:
    boto3_raw_data: "type_defs.GuardrailContextualGroundingFilterTypeDef" = (
        dataclasses.field()
    )

    type = field("type")
    threshold = field("threshold")
    score = field("score")
    action = field("action")
    detected = field("detected")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GuardrailContextualGroundingFilterTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GuardrailContextualGroundingFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailConverseTextBlockOutput:
    boto3_raw_data: "type_defs.GuardrailConverseTextBlockOutputTypeDef" = (
        dataclasses.field()
    )

    text = field("text")
    qualifiers = field("qualifiers")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GuardrailConverseTextBlockOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GuardrailConverseTextBlockOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailConverseImageSourceOutput:
    boto3_raw_data: "type_defs.GuardrailConverseImageSourceOutputTypeDef" = (
        dataclasses.field()
    )

    bytes = field("bytes")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GuardrailConverseImageSourceOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GuardrailConverseImageSourceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailConverseTextBlock:
    boto3_raw_data: "type_defs.GuardrailConverseTextBlockTypeDef" = dataclasses.field()

    text = field("text")
    qualifiers = field("qualifiers")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GuardrailConverseTextBlockTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GuardrailConverseTextBlockTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailImageCoverage:
    boto3_raw_data: "type_defs.GuardrailImageCoverageTypeDef" = dataclasses.field()

    guarded = field("guarded")
    total = field("total")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GuardrailImageCoverageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GuardrailImageCoverageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailTextCharactersCoverage:
    boto3_raw_data: "type_defs.GuardrailTextCharactersCoverageTypeDef" = (
        dataclasses.field()
    )

    guarded = field("guarded")
    total = field("total")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GuardrailTextCharactersCoverageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GuardrailTextCharactersCoverageTypeDef"]
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

    match = field("match")
    action = field("action")
    detected = field("detected")

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
class GuardrailManagedWord:
    boto3_raw_data: "type_defs.GuardrailManagedWordTypeDef" = dataclasses.field()

    match = field("match")
    type = field("type")
    action = field("action")
    detected = field("detected")

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

    match = field("match")
    type = field("type")
    action = field("action")
    detected = field("detected")

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
    name = field("name")
    match = field("match")
    regex = field("regex")
    detected = field("detected")

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

    name = field("name")
    type = field("type")
    action = field("action")
    detected = field("detected")

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
class ModelTimeoutException:
    boto3_raw_data: "type_defs.ModelTimeoutExceptionTypeDef" = dataclasses.field()

    message = field("message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModelTimeoutExceptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModelTimeoutExceptionTypeDef"]
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
class PayloadPart:
    boto3_raw_data: "type_defs.PayloadPartTypeDef" = dataclasses.field()

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
class SpecificToolChoice:
    boto3_raw_data: "type_defs.SpecificToolChoiceTypeDef" = dataclasses.field()

    name = field("name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SpecificToolChoiceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SpecificToolChoiceTypeDef"]
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

    key = field("key")
    value = field("value")

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
class ToolInputSchema:
    boto3_raw_data: "type_defs.ToolInputSchemaTypeDef" = dataclasses.field()

    json = field("json")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ToolInputSchemaTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ToolInputSchemaTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ToolUseBlock:
    boto3_raw_data: "type_defs.ToolUseBlockTypeDef" = dataclasses.field()

    toolUseId = field("toolUseId")
    name = field("name")
    input = field("input")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ToolUseBlockTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ToolUseBlockTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CountTokensResponse:
    boto3_raw_data: "type_defs.CountTokensResponseTypeDef" = dataclasses.field()

    inputTokens = field("inputTokens")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CountTokensResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CountTokensResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InvokeModelResponse:
    boto3_raw_data: "type_defs.InvokeModelResponseTypeDef" = dataclasses.field()

    body = field("body")
    contentType = field("contentType")
    performanceConfigLatency = field("performanceConfigLatency")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InvokeModelResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InvokeModelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartAsyncInvokeResponse:
    boto3_raw_data: "type_defs.StartAsyncInvokeResponseTypeDef" = dataclasses.field()

    invocationArn = field("invocationArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartAsyncInvokeResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartAsyncInvokeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AsyncInvokeOutputDataConfig:
    boto3_raw_data: "type_defs.AsyncInvokeOutputDataConfigTypeDef" = dataclasses.field()

    @cached_property
    def s3OutputDataConfig(self):  # pragma: no cover
        return AsyncInvokeS3OutputDataConfig.make_one(
            self.boto3_raw_data["s3OutputDataConfig"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AsyncInvokeOutputDataConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AsyncInvokeOutputDataConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BidirectionalInputPayloadPart:
    boto3_raw_data: "type_defs.BidirectionalInputPayloadPartTypeDef" = (
        dataclasses.field()
    )

    bytes = field("bytes")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BidirectionalInputPayloadPartTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BidirectionalInputPayloadPartTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailConverseImageSource:
    boto3_raw_data: "type_defs.GuardrailConverseImageSourceTypeDef" = (
        dataclasses.field()
    )

    bytes = field("bytes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GuardrailConverseImageSourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GuardrailConverseImageSourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailImageSource:
    boto3_raw_data: "type_defs.GuardrailImageSourceTypeDef" = dataclasses.field()

    bytes = field("bytes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GuardrailImageSourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GuardrailImageSourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InvokeModelRequest:
    boto3_raw_data: "type_defs.InvokeModelRequestTypeDef" = dataclasses.field()

    modelId = field("modelId")
    body = field("body")
    contentType = field("contentType")
    accept = field("accept")
    trace = field("trace")
    guardrailIdentifier = field("guardrailIdentifier")
    guardrailVersion = field("guardrailVersion")
    performanceConfigLatency = field("performanceConfigLatency")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InvokeModelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InvokeModelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InvokeModelTokensRequest:
    boto3_raw_data: "type_defs.InvokeModelTokensRequestTypeDef" = dataclasses.field()

    body = field("body")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InvokeModelTokensRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InvokeModelTokensRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InvokeModelWithResponseStreamRequest:
    boto3_raw_data: "type_defs.InvokeModelWithResponseStreamRequestTypeDef" = (
        dataclasses.field()
    )

    modelId = field("modelId")
    body = field("body")
    contentType = field("contentType")
    accept = field("accept")
    trace = field("trace")
    guardrailIdentifier = field("guardrailIdentifier")
    guardrailVersion = field("guardrailVersion")
    performanceConfigLatency = field("performanceConfigLatency")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.InvokeModelWithResponseStreamRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InvokeModelWithResponseStreamRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CitationLocation:
    boto3_raw_data: "type_defs.CitationLocationTypeDef" = dataclasses.field()

    @cached_property
    def documentChar(self):  # pragma: no cover
        return DocumentCharLocation.make_one(self.boto3_raw_data["documentChar"])

    @cached_property
    def documentPage(self):  # pragma: no cover
        return DocumentPageLocation.make_one(self.boto3_raw_data["documentPage"])

    @cached_property
    def documentChunk(self):  # pragma: no cover
        return DocumentChunkLocation.make_one(self.boto3_raw_data["documentChunk"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CitationLocationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CitationLocationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContentBlockStart:
    boto3_raw_data: "type_defs.ContentBlockStartTypeDef" = dataclasses.field()

    @cached_property
    def toolUse(self):  # pragma: no cover
        return ToolUseBlockStart.make_one(self.boto3_raw_data["toolUse"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ContentBlockStartTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContentBlockStartTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentSourceOutput:
    boto3_raw_data: "type_defs.DocumentSourceOutputTypeDef" = dataclasses.field()

    bytes = field("bytes")

    @cached_property
    def s3Location(self):  # pragma: no cover
        return S3Location.make_one(self.boto3_raw_data["s3Location"])

    text = field("text")

    @cached_property
    def content(self):  # pragma: no cover
        return DocumentContentBlock.make_many(self.boto3_raw_data["content"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DocumentSourceOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentSourceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentSource:
    boto3_raw_data: "type_defs.DocumentSourceTypeDef" = dataclasses.field()

    bytes = field("bytes")

    @cached_property
    def s3Location(self):  # pragma: no cover
        return S3Location.make_one(self.boto3_raw_data["s3Location"])

    text = field("text")

    @cached_property
    def content(self):  # pragma: no cover
        return DocumentContentBlock.make_many(self.boto3_raw_data["content"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DocumentSourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DocumentSourceTypeDef"]],
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
class VideoSourceOutput:
    boto3_raw_data: "type_defs.VideoSourceOutputTypeDef" = dataclasses.field()

    bytes = field("bytes")

    @cached_property
    def s3Location(self):  # pragma: no cover
        return S3Location.make_one(self.boto3_raw_data["s3Location"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VideoSourceOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VideoSourceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VideoSource:
    boto3_raw_data: "type_defs.VideoSourceTypeDef" = dataclasses.field()

    bytes = field("bytes")

    @cached_property
    def s3Location(self):  # pragma: no cover
        return S3Location.make_one(self.boto3_raw_data["s3Location"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VideoSourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VideoSourceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailAutomatedReasoningLogicWarning:
    boto3_raw_data: "type_defs.GuardrailAutomatedReasoningLogicWarningTypeDef" = (
        dataclasses.field()
    )

    type = field("type")

    @cached_property
    def premises(self):  # pragma: no cover
        return GuardrailAutomatedReasoningStatement.make_many(
            self.boto3_raw_data["premises"]
        )

    @cached_property
    def claims(self):  # pragma: no cover
        return GuardrailAutomatedReasoningStatement.make_many(
            self.boto3_raw_data["claims"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GuardrailAutomatedReasoningLogicWarningTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GuardrailAutomatedReasoningLogicWarningTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailAutomatedReasoningScenario:
    boto3_raw_data: "type_defs.GuardrailAutomatedReasoningScenarioTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def statements(self):  # pragma: no cover
        return GuardrailAutomatedReasoningStatement.make_many(
            self.boto3_raw_data["statements"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GuardrailAutomatedReasoningScenarioTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GuardrailAutomatedReasoningScenarioTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailAutomatedReasoningTranslation:
    boto3_raw_data: "type_defs.GuardrailAutomatedReasoningTranslationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def premises(self):  # pragma: no cover
        return GuardrailAutomatedReasoningStatement.make_many(
            self.boto3_raw_data["premises"]
        )

    @cached_property
    def claims(self):  # pragma: no cover
        return GuardrailAutomatedReasoningStatement.make_many(
            self.boto3_raw_data["claims"]
        )

    @cached_property
    def untranslatedPremises(self):  # pragma: no cover
        return GuardrailAutomatedReasoningInputTextReference.make_many(
            self.boto3_raw_data["untranslatedPremises"]
        )

    @cached_property
    def untranslatedClaims(self):  # pragma: no cover
        return GuardrailAutomatedReasoningInputTextReference.make_many(
            self.boto3_raw_data["untranslatedClaims"]
        )

    confidence = field("confidence")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GuardrailAutomatedReasoningTranslationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GuardrailAutomatedReasoningTranslationTypeDef"]
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
class GuardrailContextualGroundingPolicyAssessment:
    boto3_raw_data: "type_defs.GuardrailContextualGroundingPolicyAssessmentTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def filters(self):  # pragma: no cover
        return GuardrailContextualGroundingFilter.make_many(
            self.boto3_raw_data["filters"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GuardrailContextualGroundingPolicyAssessmentTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GuardrailContextualGroundingPolicyAssessmentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailConverseImageBlockOutput:
    boto3_raw_data: "type_defs.GuardrailConverseImageBlockOutputTypeDef" = (
        dataclasses.field()
    )

    format = field("format")

    @cached_property
    def source(self):  # pragma: no cover
        return GuardrailConverseImageSourceOutput.make_one(
            self.boto3_raw_data["source"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GuardrailConverseImageBlockOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GuardrailConverseImageBlockOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailCoverage:
    boto3_raw_data: "type_defs.GuardrailCoverageTypeDef" = dataclasses.field()

    @cached_property
    def textCharacters(self):  # pragma: no cover
        return GuardrailTextCharactersCoverage.make_one(
            self.boto3_raw_data["textCharacters"]
        )

    @cached_property
    def images(self):  # pragma: no cover
        return GuardrailImageCoverage.make_one(self.boto3_raw_data["images"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GuardrailCoverageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GuardrailCoverageTypeDef"]
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
class InvokeModelWithBidirectionalStreamOutput:
    boto3_raw_data: "type_defs.InvokeModelWithBidirectionalStreamOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def chunk(self):  # pragma: no cover
        return BidirectionalOutputPayloadPart.make_one(self.boto3_raw_data["chunk"])

    @cached_property
    def internalServerException(self):  # pragma: no cover
        return InternalServerException.make_one(
            self.boto3_raw_data["internalServerException"]
        )

    @cached_property
    def modelStreamErrorException(self):  # pragma: no cover
        return ModelStreamErrorException.make_one(
            self.boto3_raw_data["modelStreamErrorException"]
        )

    @cached_property
    def validationException(self):  # pragma: no cover
        return ValidationException.make_one(self.boto3_raw_data["validationException"])

    @cached_property
    def throttlingException(self):  # pragma: no cover
        return ThrottlingException.make_one(self.boto3_raw_data["throttlingException"])

    @cached_property
    def modelTimeoutException(self):  # pragma: no cover
        return ModelTimeoutException.make_one(
            self.boto3_raw_data["modelTimeoutException"]
        )

    @cached_property
    def serviceUnavailableException(self):  # pragma: no cover
        return ServiceUnavailableException.make_one(
            self.boto3_raw_data["serviceUnavailableException"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.InvokeModelWithBidirectionalStreamOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InvokeModelWithBidirectionalStreamOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAsyncInvokesRequestPaginate:
    boto3_raw_data: "type_defs.ListAsyncInvokesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    submitTimeAfter = field("submitTimeAfter")
    submitTimeBefore = field("submitTimeBefore")
    statusEquals = field("statusEquals")
    sortBy = field("sortBy")
    sortOrder = field("sortOrder")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAsyncInvokesRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAsyncInvokesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAsyncInvokesRequest:
    boto3_raw_data: "type_defs.ListAsyncInvokesRequestTypeDef" = dataclasses.field()

    submitTimeAfter = field("submitTimeAfter")
    submitTimeBefore = field("submitTimeBefore")
    statusEquals = field("statusEquals")
    maxResults = field("maxResults")
    nextToken = field("nextToken")
    sortBy = field("sortBy")
    sortOrder = field("sortOrder")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAsyncInvokesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAsyncInvokesRequestTypeDef"]
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
    def chunk(self):  # pragma: no cover
        return PayloadPart.make_one(self.boto3_raw_data["chunk"])

    @cached_property
    def internalServerException(self):  # pragma: no cover
        return InternalServerException.make_one(
            self.boto3_raw_data["internalServerException"]
        )

    @cached_property
    def modelStreamErrorException(self):  # pragma: no cover
        return ModelStreamErrorException.make_one(
            self.boto3_raw_data["modelStreamErrorException"]
        )

    @cached_property
    def validationException(self):  # pragma: no cover
        return ValidationException.make_one(self.boto3_raw_data["validationException"])

    @cached_property
    def throttlingException(self):  # pragma: no cover
        return ThrottlingException.make_one(self.boto3_raw_data["throttlingException"])

    @cached_property
    def modelTimeoutException(self):  # pragma: no cover
        return ModelTimeoutException.make_one(
            self.boto3_raw_data["modelTimeoutException"]
        )

    @cached_property
    def serviceUnavailableException(self):  # pragma: no cover
        return ServiceUnavailableException.make_one(
            self.boto3_raw_data["serviceUnavailableException"]
        )

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
class ReasoningContentBlockOutput:
    boto3_raw_data: "type_defs.ReasoningContentBlockOutputTypeDef" = dataclasses.field()

    @cached_property
    def reasoningText(self):  # pragma: no cover
        return ReasoningTextBlock.make_one(self.boto3_raw_data["reasoningText"])

    redactedContent = field("redactedContent")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReasoningContentBlockOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReasoningContentBlockOutputTypeDef"]
        ],
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
class ToolChoice:
    boto3_raw_data: "type_defs.ToolChoiceTypeDef" = dataclasses.field()

    auto = field("auto")
    any = field("any")

    @cached_property
    def tool(self):  # pragma: no cover
        return SpecificToolChoice.make_one(self.boto3_raw_data["tool"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ToolChoiceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ToolChoiceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ToolSpecification:
    boto3_raw_data: "type_defs.ToolSpecificationTypeDef" = dataclasses.field()

    name = field("name")

    @cached_property
    def inputSchema(self):  # pragma: no cover
        return ToolInputSchema.make_one(self.boto3_raw_data["inputSchema"])

    description = field("description")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ToolSpecificationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ToolSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AsyncInvokeSummary:
    boto3_raw_data: "type_defs.AsyncInvokeSummaryTypeDef" = dataclasses.field()

    invocationArn = field("invocationArn")
    modelArn = field("modelArn")
    submitTime = field("submitTime")

    @cached_property
    def outputDataConfig(self):  # pragma: no cover
        return AsyncInvokeOutputDataConfig.make_one(
            self.boto3_raw_data["outputDataConfig"]
        )

    clientRequestToken = field("clientRequestToken")
    status = field("status")
    failureMessage = field("failureMessage")
    lastModifiedTime = field("lastModifiedTime")
    endTime = field("endTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AsyncInvokeSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AsyncInvokeSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAsyncInvokeResponse:
    boto3_raw_data: "type_defs.GetAsyncInvokeResponseTypeDef" = dataclasses.field()

    invocationArn = field("invocationArn")
    modelArn = field("modelArn")
    clientRequestToken = field("clientRequestToken")
    status = field("status")
    failureMessage = field("failureMessage")
    submitTime = field("submitTime")
    lastModifiedTime = field("lastModifiedTime")
    endTime = field("endTime")

    @cached_property
    def outputDataConfig(self):  # pragma: no cover
        return AsyncInvokeOutputDataConfig.make_one(
            self.boto3_raw_data["outputDataConfig"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAsyncInvokeResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAsyncInvokeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartAsyncInvokeRequest:
    boto3_raw_data: "type_defs.StartAsyncInvokeRequestTypeDef" = dataclasses.field()

    modelId = field("modelId")
    modelInput = field("modelInput")

    @cached_property
    def outputDataConfig(self):  # pragma: no cover
        return AsyncInvokeOutputDataConfig.make_one(
            self.boto3_raw_data["outputDataConfig"]
        )

    clientRequestToken = field("clientRequestToken")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartAsyncInvokeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartAsyncInvokeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InvokeModelWithBidirectionalStreamInput:
    boto3_raw_data: "type_defs.InvokeModelWithBidirectionalStreamInputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def chunk(self):  # pragma: no cover
        return BidirectionalInputPayloadPart.make_one(self.boto3_raw_data["chunk"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.InvokeModelWithBidirectionalStreamInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InvokeModelWithBidirectionalStreamInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailImageBlock:
    boto3_raw_data: "type_defs.GuardrailImageBlockTypeDef" = dataclasses.field()

    format = field("format")

    @cached_property
    def source(self):  # pragma: no cover
        return GuardrailImageSource.make_one(self.boto3_raw_data["source"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GuardrailImageBlockTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GuardrailImageBlockTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CitationOutput:
    boto3_raw_data: "type_defs.CitationOutputTypeDef" = dataclasses.field()

    title = field("title")

    @cached_property
    def sourceContent(self):  # pragma: no cover
        return CitationSourceContent.make_many(self.boto3_raw_data["sourceContent"])

    @cached_property
    def location(self):  # pragma: no cover
        return CitationLocation.make_one(self.boto3_raw_data["location"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CitationOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CitationOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Citation:
    boto3_raw_data: "type_defs.CitationTypeDef" = dataclasses.field()

    title = field("title")

    @cached_property
    def sourceContent(self):  # pragma: no cover
        return CitationSourceContent.make_many(self.boto3_raw_data["sourceContent"])

    @cached_property
    def location(self):  # pragma: no cover
        return CitationLocation.make_one(self.boto3_raw_data["location"])

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
class CitationsDelta:
    boto3_raw_data: "type_defs.CitationsDeltaTypeDef" = dataclasses.field()

    title = field("title")

    @cached_property
    def sourceContent(self):  # pragma: no cover
        return CitationSourceContentDelta.make_many(
            self.boto3_raw_data["sourceContent"]
        )

    @cached_property
    def location(self):  # pragma: no cover
        return CitationLocation.make_one(self.boto3_raw_data["location"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CitationsDeltaTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CitationsDeltaTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContentBlockStartEvent:
    boto3_raw_data: "type_defs.ContentBlockStartEventTypeDef" = dataclasses.field()

    @cached_property
    def start(self):  # pragma: no cover
        return ContentBlockStart.make_one(self.boto3_raw_data["start"])

    contentBlockIndex = field("contentBlockIndex")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContentBlockStartEventTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContentBlockStartEventTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentBlockOutput:
    boto3_raw_data: "type_defs.DocumentBlockOutputTypeDef" = dataclasses.field()

    name = field("name")

    @cached_property
    def source(self):  # pragma: no cover
        return DocumentSourceOutput.make_one(self.boto3_raw_data["source"])

    format = field("format")
    context = field("context")

    @cached_property
    def citations(self):  # pragma: no cover
        return CitationsConfig.make_one(self.boto3_raw_data["citations"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DocumentBlockOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentBlockOutputTypeDef"]
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
class VideoBlockOutput:
    boto3_raw_data: "type_defs.VideoBlockOutputTypeDef" = dataclasses.field()

    format = field("format")

    @cached_property
    def source(self):  # pragma: no cover
        return VideoSourceOutput.make_one(self.boto3_raw_data["source"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VideoBlockOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VideoBlockOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailAutomatedReasoningImpossibleFinding:
    boto3_raw_data: "type_defs.GuardrailAutomatedReasoningImpossibleFindingTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def translation(self):  # pragma: no cover
        return GuardrailAutomatedReasoningTranslation.make_one(
            self.boto3_raw_data["translation"]
        )

    @cached_property
    def contradictingRules(self):  # pragma: no cover
        return GuardrailAutomatedReasoningRule.make_many(
            self.boto3_raw_data["contradictingRules"]
        )

    @cached_property
    def logicWarning(self):  # pragma: no cover
        return GuardrailAutomatedReasoningLogicWarning.make_one(
            self.boto3_raw_data["logicWarning"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GuardrailAutomatedReasoningImpossibleFindingTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GuardrailAutomatedReasoningImpossibleFindingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailAutomatedReasoningInvalidFinding:
    boto3_raw_data: "type_defs.GuardrailAutomatedReasoningInvalidFindingTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def translation(self):  # pragma: no cover
        return GuardrailAutomatedReasoningTranslation.make_one(
            self.boto3_raw_data["translation"]
        )

    @cached_property
    def contradictingRules(self):  # pragma: no cover
        return GuardrailAutomatedReasoningRule.make_many(
            self.boto3_raw_data["contradictingRules"]
        )

    @cached_property
    def logicWarning(self):  # pragma: no cover
        return GuardrailAutomatedReasoningLogicWarning.make_one(
            self.boto3_raw_data["logicWarning"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GuardrailAutomatedReasoningInvalidFindingTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GuardrailAutomatedReasoningInvalidFindingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailAutomatedReasoningSatisfiableFinding:
    boto3_raw_data: "type_defs.GuardrailAutomatedReasoningSatisfiableFindingTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def translation(self):  # pragma: no cover
        return GuardrailAutomatedReasoningTranslation.make_one(
            self.boto3_raw_data["translation"]
        )

    @cached_property
    def claimsTrueScenario(self):  # pragma: no cover
        return GuardrailAutomatedReasoningScenario.make_one(
            self.boto3_raw_data["claimsTrueScenario"]
        )

    @cached_property
    def claimsFalseScenario(self):  # pragma: no cover
        return GuardrailAutomatedReasoningScenario.make_one(
            self.boto3_raw_data["claimsFalseScenario"]
        )

    @cached_property
    def logicWarning(self):  # pragma: no cover
        return GuardrailAutomatedReasoningLogicWarning.make_one(
            self.boto3_raw_data["logicWarning"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GuardrailAutomatedReasoningSatisfiableFindingTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GuardrailAutomatedReasoningSatisfiableFindingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailAutomatedReasoningTranslationOption:
    boto3_raw_data: "type_defs.GuardrailAutomatedReasoningTranslationOptionTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def translations(self):  # pragma: no cover
        return GuardrailAutomatedReasoningTranslation.make_many(
            self.boto3_raw_data["translations"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GuardrailAutomatedReasoningTranslationOptionTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GuardrailAutomatedReasoningTranslationOptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailAutomatedReasoningValidFinding:
    boto3_raw_data: "type_defs.GuardrailAutomatedReasoningValidFindingTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def translation(self):  # pragma: no cover
        return GuardrailAutomatedReasoningTranslation.make_one(
            self.boto3_raw_data["translation"]
        )

    @cached_property
    def claimsTrueScenario(self):  # pragma: no cover
        return GuardrailAutomatedReasoningScenario.make_one(
            self.boto3_raw_data["claimsTrueScenario"]
        )

    @cached_property
    def supportingRules(self):  # pragma: no cover
        return GuardrailAutomatedReasoningRule.make_many(
            self.boto3_raw_data["supportingRules"]
        )

    @cached_property
    def logicWarning(self):  # pragma: no cover
        return GuardrailAutomatedReasoningLogicWarning.make_one(
            self.boto3_raw_data["logicWarning"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GuardrailAutomatedReasoningValidFindingTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GuardrailAutomatedReasoningValidFindingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailConverseContentBlockOutput:
    boto3_raw_data: "type_defs.GuardrailConverseContentBlockOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def text(self):  # pragma: no cover
        return GuardrailConverseTextBlockOutput.make_one(self.boto3_raw_data["text"])

    @cached_property
    def image(self):  # pragma: no cover
        return GuardrailConverseImageBlockOutput.make_one(self.boto3_raw_data["image"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GuardrailConverseContentBlockOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GuardrailConverseContentBlockOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailInvocationMetrics:
    boto3_raw_data: "type_defs.GuardrailInvocationMetricsTypeDef" = dataclasses.field()

    guardrailProcessingLatency = field("guardrailProcessingLatency")

    @cached_property
    def usage(self):  # pragma: no cover
        return GuardrailUsage.make_one(self.boto3_raw_data["usage"])

    @cached_property
    def guardrailCoverage(self):  # pragma: no cover
        return GuardrailCoverage.make_one(self.boto3_raw_data["guardrailCoverage"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GuardrailInvocationMetricsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GuardrailInvocationMetricsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InvokeModelWithBidirectionalStreamResponse:
    boto3_raw_data: "type_defs.InvokeModelWithBidirectionalStreamResponseTypeDef" = (
        dataclasses.field()
    )

    body = field("body")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.InvokeModelWithBidirectionalStreamResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InvokeModelWithBidirectionalStreamResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InvokeModelWithResponseStreamResponse:
    boto3_raw_data: "type_defs.InvokeModelWithResponseStreamResponseTypeDef" = (
        dataclasses.field()
    )

    body = field("body")
    contentType = field("contentType")
    performanceConfigLatency = field("performanceConfigLatency")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.InvokeModelWithResponseStreamResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InvokeModelWithResponseStreamResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Tool:
    boto3_raw_data: "type_defs.ToolTypeDef" = dataclasses.field()

    @cached_property
    def toolSpec(self):  # pragma: no cover
        return ToolSpecification.make_one(self.boto3_raw_data["toolSpec"])

    @cached_property
    def cachePoint(self):  # pragma: no cover
        return CachePointBlock.make_one(self.boto3_raw_data["cachePoint"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ToolTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ToolTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAsyncInvokesResponse:
    boto3_raw_data: "type_defs.ListAsyncInvokesResponseTypeDef" = dataclasses.field()

    @cached_property
    def asyncInvokeSummaries(self):  # pragma: no cover
        return AsyncInvokeSummary.make_many(self.boto3_raw_data["asyncInvokeSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAsyncInvokesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAsyncInvokesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InvokeModelWithBidirectionalStreamRequest:
    boto3_raw_data: "type_defs.InvokeModelWithBidirectionalStreamRequestTypeDef" = (
        dataclasses.field()
    )

    modelId = field("modelId")
    body = field("body")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.InvokeModelWithBidirectionalStreamRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InvokeModelWithBidirectionalStreamRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailConverseImageBlock:
    boto3_raw_data: "type_defs.GuardrailConverseImageBlockTypeDef" = dataclasses.field()

    format = field("format")
    source = field("source")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GuardrailConverseImageBlockTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GuardrailConverseImageBlockTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailContentBlock:
    boto3_raw_data: "type_defs.GuardrailContentBlockTypeDef" = dataclasses.field()

    @cached_property
    def text(self):  # pragma: no cover
        return GuardrailTextBlock.make_one(self.boto3_raw_data["text"])

    @cached_property
    def image(self):  # pragma: no cover
        return GuardrailImageBlock.make_one(self.boto3_raw_data["image"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GuardrailContentBlockTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GuardrailContentBlockTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CitationsContentBlockOutput:
    boto3_raw_data: "type_defs.CitationsContentBlockOutputTypeDef" = dataclasses.field()

    @cached_property
    def content(self):  # pragma: no cover
        return CitationGeneratedContent.make_many(self.boto3_raw_data["content"])

    @cached_property
    def citations(self):  # pragma: no cover
        return CitationOutput.make_many(self.boto3_raw_data["citations"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CitationsContentBlockOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CitationsContentBlockOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContentBlockDelta:
    boto3_raw_data: "type_defs.ContentBlockDeltaTypeDef" = dataclasses.field()

    text = field("text")

    @cached_property
    def toolUse(self):  # pragma: no cover
        return ToolUseBlockDelta.make_one(self.boto3_raw_data["toolUse"])

    @cached_property
    def reasoningContent(self):  # pragma: no cover
        return ReasoningContentBlockDelta.make_one(
            self.boto3_raw_data["reasoningContent"]
        )

    @cached_property
    def citation(self):  # pragma: no cover
        return CitationsDelta.make_one(self.boto3_raw_data["citation"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ContentBlockDeltaTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContentBlockDeltaTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentBlock:
    boto3_raw_data: "type_defs.DocumentBlockTypeDef" = dataclasses.field()

    name = field("name")
    source = field("source")
    format = field("format")
    context = field("context")

    @cached_property
    def citations(self):  # pragma: no cover
        return CitationsConfig.make_one(self.boto3_raw_data["citations"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DocumentBlockTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DocumentBlockTypeDef"]],
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
    source = field("source")

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
class ToolResultContentBlockOutput:
    boto3_raw_data: "type_defs.ToolResultContentBlockOutputTypeDef" = (
        dataclasses.field()
    )

    json = field("json")
    text = field("text")

    @cached_property
    def image(self):  # pragma: no cover
        return ImageBlockOutput.make_one(self.boto3_raw_data["image"])

    @cached_property
    def document(self):  # pragma: no cover
        return DocumentBlockOutput.make_one(self.boto3_raw_data["document"])

    @cached_property
    def video(self):  # pragma: no cover
        return VideoBlockOutput.make_one(self.boto3_raw_data["video"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ToolResultContentBlockOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ToolResultContentBlockOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VideoBlock:
    boto3_raw_data: "type_defs.VideoBlockTypeDef" = dataclasses.field()

    format = field("format")
    source = field("source")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VideoBlockTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VideoBlockTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailAutomatedReasoningTranslationAmbiguousFinding:
    boto3_raw_data: (
        "type_defs.GuardrailAutomatedReasoningTranslationAmbiguousFindingTypeDef"
    ) = dataclasses.field()

    @cached_property
    def options(self):  # pragma: no cover
        return GuardrailAutomatedReasoningTranslationOption.make_many(
            self.boto3_raw_data["options"]
        )

    @cached_property
    def differenceScenarios(self):  # pragma: no cover
        return GuardrailAutomatedReasoningScenario.make_many(
            self.boto3_raw_data["differenceScenarios"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GuardrailAutomatedReasoningTranslationAmbiguousFindingTypeDef"
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
                "type_defs.GuardrailAutomatedReasoningTranslationAmbiguousFindingTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ToolConfiguration:
    boto3_raw_data: "type_defs.ToolConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def tools(self):  # pragma: no cover
        return Tool.make_many(self.boto3_raw_data["tools"])

    @cached_property
    def toolChoice(self):  # pragma: no cover
        return ToolChoice.make_one(self.boto3_raw_data["toolChoice"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ToolConfigurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ToolConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplyGuardrailRequest:
    boto3_raw_data: "type_defs.ApplyGuardrailRequestTypeDef" = dataclasses.field()

    guardrailIdentifier = field("guardrailIdentifier")
    guardrailVersion = field("guardrailVersion")
    source = field("source")

    @cached_property
    def content(self):  # pragma: no cover
        return GuardrailContentBlock.make_many(self.boto3_raw_data["content"])

    outputScope = field("outputScope")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ApplyGuardrailRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplyGuardrailRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CitationsContentBlock:
    boto3_raw_data: "type_defs.CitationsContentBlockTypeDef" = dataclasses.field()

    @cached_property
    def content(self):  # pragma: no cover
        return CitationGeneratedContent.make_many(self.boto3_raw_data["content"])

    citations = field("citations")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CitationsContentBlockTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CitationsContentBlockTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContentBlockDeltaEvent:
    boto3_raw_data: "type_defs.ContentBlockDeltaEventTypeDef" = dataclasses.field()

    @cached_property
    def delta(self):  # pragma: no cover
        return ContentBlockDelta.make_one(self.boto3_raw_data["delta"])

    contentBlockIndex = field("contentBlockIndex")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContentBlockDeltaEventTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContentBlockDeltaEventTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ToolResultBlockOutput:
    boto3_raw_data: "type_defs.ToolResultBlockOutputTypeDef" = dataclasses.field()

    toolUseId = field("toolUseId")

    @cached_property
    def content(self):  # pragma: no cover
        return ToolResultContentBlockOutput.make_many(self.boto3_raw_data["content"])

    status = field("status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ToolResultBlockOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ToolResultBlockOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailAutomatedReasoningFinding:
    boto3_raw_data: "type_defs.GuardrailAutomatedReasoningFindingTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def valid(self):  # pragma: no cover
        return GuardrailAutomatedReasoningValidFinding.make_one(
            self.boto3_raw_data["valid"]
        )

    @cached_property
    def invalid(self):  # pragma: no cover
        return GuardrailAutomatedReasoningInvalidFinding.make_one(
            self.boto3_raw_data["invalid"]
        )

    @cached_property
    def satisfiable(self):  # pragma: no cover
        return GuardrailAutomatedReasoningSatisfiableFinding.make_one(
            self.boto3_raw_data["satisfiable"]
        )

    @cached_property
    def impossible(self):  # pragma: no cover
        return GuardrailAutomatedReasoningImpossibleFinding.make_one(
            self.boto3_raw_data["impossible"]
        )

    @cached_property
    def translationAmbiguous(self):  # pragma: no cover
        return GuardrailAutomatedReasoningTranslationAmbiguousFinding.make_one(
            self.boto3_raw_data["translationAmbiguous"]
        )

    tooComplex = field("tooComplex")
    noTranslations = field("noTranslations")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GuardrailAutomatedReasoningFindingTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GuardrailAutomatedReasoningFindingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailConverseContentBlock:
    boto3_raw_data: "type_defs.GuardrailConverseContentBlockTypeDef" = (
        dataclasses.field()
    )

    text = field("text")
    image = field("image")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GuardrailConverseContentBlockTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GuardrailConverseContentBlockTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContentBlockOutput:
    boto3_raw_data: "type_defs.ContentBlockOutputTypeDef" = dataclasses.field()

    text = field("text")

    @cached_property
    def image(self):  # pragma: no cover
        return ImageBlockOutput.make_one(self.boto3_raw_data["image"])

    @cached_property
    def document(self):  # pragma: no cover
        return DocumentBlockOutput.make_one(self.boto3_raw_data["document"])

    @cached_property
    def video(self):  # pragma: no cover
        return VideoBlockOutput.make_one(self.boto3_raw_data["video"])

    @cached_property
    def toolUse(self):  # pragma: no cover
        return ToolUseBlockOutput.make_one(self.boto3_raw_data["toolUse"])

    @cached_property
    def toolResult(self):  # pragma: no cover
        return ToolResultBlockOutput.make_one(self.boto3_raw_data["toolResult"])

    @cached_property
    def guardContent(self):  # pragma: no cover
        return GuardrailConverseContentBlockOutput.make_one(
            self.boto3_raw_data["guardContent"]
        )

    @cached_property
    def cachePoint(self):  # pragma: no cover
        return CachePointBlock.make_one(self.boto3_raw_data["cachePoint"])

    @cached_property
    def reasoningContent(self):  # pragma: no cover
        return ReasoningContentBlockOutput.make_one(
            self.boto3_raw_data["reasoningContent"]
        )

    @cached_property
    def citationsContent(self):  # pragma: no cover
        return CitationsContentBlockOutput.make_one(
            self.boto3_raw_data["citationsContent"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContentBlockOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContentBlockOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ToolResultContentBlock:
    boto3_raw_data: "type_defs.ToolResultContentBlockTypeDef" = dataclasses.field()

    json = field("json")
    text = field("text")
    image = field("image")
    document = field("document")
    video = field("video")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ToolResultContentBlockTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ToolResultContentBlockTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailAutomatedReasoningPolicyAssessment:
    boto3_raw_data: "type_defs.GuardrailAutomatedReasoningPolicyAssessmentTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def findings(self):  # pragma: no cover
        return GuardrailAutomatedReasoningFinding.make_many(
            self.boto3_raw_data["findings"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GuardrailAutomatedReasoningPolicyAssessmentTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GuardrailAutomatedReasoningPolicyAssessmentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MessageOutput:
    boto3_raw_data: "type_defs.MessageOutputTypeDef" = dataclasses.field()

    role = field("role")

    @cached_property
    def content(self):  # pragma: no cover
        return ContentBlockOutput.make_many(self.boto3_raw_data["content"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MessageOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MessageOutputTypeDef"]],
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
    def topicPolicy(self):  # pragma: no cover
        return GuardrailTopicPolicyAssessment.make_one(
            self.boto3_raw_data["topicPolicy"]
        )

    @cached_property
    def contentPolicy(self):  # pragma: no cover
        return GuardrailContentPolicyAssessment.make_one(
            self.boto3_raw_data["contentPolicy"]
        )

    @cached_property
    def wordPolicy(self):  # pragma: no cover
        return GuardrailWordPolicyAssessment.make_one(self.boto3_raw_data["wordPolicy"])

    @cached_property
    def sensitiveInformationPolicy(self):  # pragma: no cover
        return GuardrailSensitiveInformationPolicyAssessment.make_one(
            self.boto3_raw_data["sensitiveInformationPolicy"]
        )

    @cached_property
    def contextualGroundingPolicy(self):  # pragma: no cover
        return GuardrailContextualGroundingPolicyAssessment.make_one(
            self.boto3_raw_data["contextualGroundingPolicy"]
        )

    @cached_property
    def automatedReasoningPolicy(self):  # pragma: no cover
        return GuardrailAutomatedReasoningPolicyAssessment.make_one(
            self.boto3_raw_data["automatedReasoningPolicy"]
        )

    @cached_property
    def invocationMetrics(self):  # pragma: no cover
        return GuardrailInvocationMetrics.make_one(
            self.boto3_raw_data["invocationMetrics"]
        )

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
class SystemContentBlock:
    boto3_raw_data: "type_defs.SystemContentBlockTypeDef" = dataclasses.field()

    text = field("text")
    guardContent = field("guardContent")

    @cached_property
    def cachePoint(self):  # pragma: no cover
        return CachePointBlock.make_one(self.boto3_raw_data["cachePoint"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SystemContentBlockTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SystemContentBlockTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConverseOutput:
    boto3_raw_data: "type_defs.ConverseOutputTypeDef" = dataclasses.field()

    @cached_property
    def message(self):  # pragma: no cover
        return MessageOutput.make_one(self.boto3_raw_data["message"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConverseOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ConverseOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ToolResultBlock:
    boto3_raw_data: "type_defs.ToolResultBlockTypeDef" = dataclasses.field()

    toolUseId = field("toolUseId")
    content = field("content")
    status = field("status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ToolResultBlockTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ToolResultBlockTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplyGuardrailResponse:
    boto3_raw_data: "type_defs.ApplyGuardrailResponseTypeDef" = dataclasses.field()

    @cached_property
    def usage(self):  # pragma: no cover
        return GuardrailUsage.make_one(self.boto3_raw_data["usage"])

    action = field("action")
    actionReason = field("actionReason")

    @cached_property
    def outputs(self):  # pragma: no cover
        return GuardrailOutputContent.make_many(self.boto3_raw_data["outputs"])

    @cached_property
    def assessments(self):  # pragma: no cover
        return GuardrailAssessment.make_many(self.boto3_raw_data["assessments"])

    @cached_property
    def guardrailCoverage(self):  # pragma: no cover
        return GuardrailCoverage.make_one(self.boto3_raw_data["guardrailCoverage"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ApplyGuardrailResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplyGuardrailResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailTraceAssessment:
    boto3_raw_data: "type_defs.GuardrailTraceAssessmentTypeDef" = dataclasses.field()

    modelOutput = field("modelOutput")
    inputAssessment = field("inputAssessment")
    outputAssessments = field("outputAssessments")
    actionReason = field("actionReason")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GuardrailTraceAssessmentTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GuardrailTraceAssessmentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConverseStreamTrace:
    boto3_raw_data: "type_defs.ConverseStreamTraceTypeDef" = dataclasses.field()

    @cached_property
    def guardrail(self):  # pragma: no cover
        return GuardrailTraceAssessment.make_one(self.boto3_raw_data["guardrail"])

    @cached_property
    def promptRouter(self):  # pragma: no cover
        return PromptRouterTrace.make_one(self.boto3_raw_data["promptRouter"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConverseStreamTraceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConverseStreamTraceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConverseTrace:
    boto3_raw_data: "type_defs.ConverseTraceTypeDef" = dataclasses.field()

    @cached_property
    def guardrail(self):  # pragma: no cover
        return GuardrailTraceAssessment.make_one(self.boto3_raw_data["guardrail"])

    @cached_property
    def promptRouter(self):  # pragma: no cover
        return PromptRouterTrace.make_one(self.boto3_raw_data["promptRouter"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConverseTraceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ConverseTraceTypeDef"]],
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
    image = field("image")
    document = field("document")
    video = field("video")
    toolUse = field("toolUse")
    toolResult = field("toolResult")
    guardContent = field("guardContent")

    @cached_property
    def cachePoint(self):  # pragma: no cover
        return CachePointBlock.make_one(self.boto3_raw_data["cachePoint"])

    reasoningContent = field("reasoningContent")
    citationsContent = field("citationsContent")

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
class ConverseStreamMetadataEvent:
    boto3_raw_data: "type_defs.ConverseStreamMetadataEventTypeDef" = dataclasses.field()

    @cached_property
    def usage(self):  # pragma: no cover
        return TokenUsage.make_one(self.boto3_raw_data["usage"])

    @cached_property
    def metrics(self):  # pragma: no cover
        return ConverseStreamMetrics.make_one(self.boto3_raw_data["metrics"])

    @cached_property
    def trace(self):  # pragma: no cover
        return ConverseStreamTrace.make_one(self.boto3_raw_data["trace"])

    @cached_property
    def performanceConfig(self):  # pragma: no cover
        return PerformanceConfiguration.make_one(
            self.boto3_raw_data["performanceConfig"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConverseStreamMetadataEventTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConverseStreamMetadataEventTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConverseResponse:
    boto3_raw_data: "type_defs.ConverseResponseTypeDef" = dataclasses.field()

    @cached_property
    def output(self):  # pragma: no cover
        return ConverseOutput.make_one(self.boto3_raw_data["output"])

    stopReason = field("stopReason")

    @cached_property
    def usage(self):  # pragma: no cover
        return TokenUsage.make_one(self.boto3_raw_data["usage"])

    @cached_property
    def metrics(self):  # pragma: no cover
        return ConverseMetrics.make_one(self.boto3_raw_data["metrics"])

    additionalModelResponseFields = field("additionalModelResponseFields")

    @cached_property
    def trace(self):  # pragma: no cover
        return ConverseTrace.make_one(self.boto3_raw_data["trace"])

    @cached_property
    def performanceConfig(self):  # pragma: no cover
        return PerformanceConfiguration.make_one(
            self.boto3_raw_data["performanceConfig"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConverseResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConverseResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConverseStreamOutput:
    boto3_raw_data: "type_defs.ConverseStreamOutputTypeDef" = dataclasses.field()

    @cached_property
    def messageStart(self):  # pragma: no cover
        return MessageStartEvent.make_one(self.boto3_raw_data["messageStart"])

    @cached_property
    def contentBlockStart(self):  # pragma: no cover
        return ContentBlockStartEvent.make_one(self.boto3_raw_data["contentBlockStart"])

    @cached_property
    def contentBlockDelta(self):  # pragma: no cover
        return ContentBlockDeltaEvent.make_one(self.boto3_raw_data["contentBlockDelta"])

    @cached_property
    def contentBlockStop(self):  # pragma: no cover
        return ContentBlockStopEvent.make_one(self.boto3_raw_data["contentBlockStop"])

    @cached_property
    def messageStop(self):  # pragma: no cover
        return MessageStopEvent.make_one(self.boto3_raw_data["messageStop"])

    @cached_property
    def metadata(self):  # pragma: no cover
        return ConverseStreamMetadataEvent.make_one(self.boto3_raw_data["metadata"])

    @cached_property
    def internalServerException(self):  # pragma: no cover
        return InternalServerException.make_one(
            self.boto3_raw_data["internalServerException"]
        )

    @cached_property
    def modelStreamErrorException(self):  # pragma: no cover
        return ModelStreamErrorException.make_one(
            self.boto3_raw_data["modelStreamErrorException"]
        )

    @cached_property
    def validationException(self):  # pragma: no cover
        return ValidationException.make_one(self.boto3_raw_data["validationException"])

    @cached_property
    def throttlingException(self):  # pragma: no cover
        return ThrottlingException.make_one(self.boto3_raw_data["throttlingException"])

    @cached_property
    def serviceUnavailableException(self):  # pragma: no cover
        return ServiceUnavailableException.make_one(
            self.boto3_raw_data["serviceUnavailableException"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConverseStreamOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConverseStreamOutputTypeDef"]
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

    role = field("role")
    content = field("content")

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
class ConverseStreamResponse:
    boto3_raw_data: "type_defs.ConverseStreamResponseTypeDef" = dataclasses.field()

    stream = field("stream")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConverseStreamResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConverseStreamResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConverseRequest:
    boto3_raw_data: "type_defs.ConverseRequestTypeDef" = dataclasses.field()

    modelId = field("modelId")
    messages = field("messages")

    @cached_property
    def system(self):  # pragma: no cover
        return SystemContentBlock.make_many(self.boto3_raw_data["system"])

    @cached_property
    def inferenceConfig(self):  # pragma: no cover
        return InferenceConfiguration.make_one(self.boto3_raw_data["inferenceConfig"])

    @cached_property
    def toolConfig(self):  # pragma: no cover
        return ToolConfiguration.make_one(self.boto3_raw_data["toolConfig"])

    @cached_property
    def guardrailConfig(self):  # pragma: no cover
        return GuardrailConfiguration.make_one(self.boto3_raw_data["guardrailConfig"])

    additionalModelRequestFields = field("additionalModelRequestFields")
    promptVariables = field("promptVariables")
    additionalModelResponseFieldPaths = field("additionalModelResponseFieldPaths")
    requestMetadata = field("requestMetadata")

    @cached_property
    def performanceConfig(self):  # pragma: no cover
        return PerformanceConfiguration.make_one(
            self.boto3_raw_data["performanceConfig"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConverseRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ConverseRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConverseStreamRequest:
    boto3_raw_data: "type_defs.ConverseStreamRequestTypeDef" = dataclasses.field()

    modelId = field("modelId")
    messages = field("messages")

    @cached_property
    def system(self):  # pragma: no cover
        return SystemContentBlock.make_many(self.boto3_raw_data["system"])

    @cached_property
    def inferenceConfig(self):  # pragma: no cover
        return InferenceConfiguration.make_one(self.boto3_raw_data["inferenceConfig"])

    @cached_property
    def toolConfig(self):  # pragma: no cover
        return ToolConfiguration.make_one(self.boto3_raw_data["toolConfig"])

    @cached_property
    def guardrailConfig(self):  # pragma: no cover
        return GuardrailStreamConfiguration.make_one(
            self.boto3_raw_data["guardrailConfig"]
        )

    additionalModelRequestFields = field("additionalModelRequestFields")
    promptVariables = field("promptVariables")
    additionalModelResponseFieldPaths = field("additionalModelResponseFieldPaths")
    requestMetadata = field("requestMetadata")

    @cached_property
    def performanceConfig(self):  # pragma: no cover
        return PerformanceConfiguration.make_one(
            self.boto3_raw_data["performanceConfig"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConverseStreamRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConverseStreamRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConverseTokensRequest:
    boto3_raw_data: "type_defs.ConverseTokensRequestTypeDef" = dataclasses.field()

    messages = field("messages")

    @cached_property
    def system(self):  # pragma: no cover
        return SystemContentBlock.make_many(self.boto3_raw_data["system"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConverseTokensRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConverseTokensRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CountTokensInput:
    boto3_raw_data: "type_defs.CountTokensInputTypeDef" = dataclasses.field()

    @cached_property
    def invokeModel(self):  # pragma: no cover
        return InvokeModelTokensRequest.make_one(self.boto3_raw_data["invokeModel"])

    @cached_property
    def converse(self):  # pragma: no cover
        return ConverseTokensRequest.make_one(self.boto3_raw_data["converse"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CountTokensInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CountTokensInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CountTokensRequest:
    boto3_raw_data: "type_defs.CountTokensRequestTypeDef" = dataclasses.field()

    modelId = field("modelId")

    @cached_property
    def input(self):  # pragma: no cover
        return CountTokensInput.make_one(self.boto3_raw_data["input"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CountTokensRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CountTokensRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
