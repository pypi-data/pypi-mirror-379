# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_bedrock_agent import type_defs


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
class ActionGroupExecutor:
    boto3_raw_data: "type_defs.ActionGroupExecutorTypeDef" = dataclasses.field()

    lambda_ = field("lambda")
    customControl = field("customControl")

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
class ActionGroupSummary:
    boto3_raw_data: "type_defs.ActionGroupSummaryTypeDef" = dataclasses.field()

    actionGroupId = field("actionGroupId")
    actionGroupName = field("actionGroupName")
    actionGroupState = field("actionGroupState")
    updatedAt = field("updatedAt")
    description = field("description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ActionGroupSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActionGroupSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AgentAliasRoutingConfigurationListItem:
    boto3_raw_data: "type_defs.AgentAliasRoutingConfigurationListItemTypeDef" = (
        dataclasses.field()
    )

    agentVersion = field("agentVersion")
    provisionedThroughput = field("provisionedThroughput")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AgentAliasRoutingConfigurationListItemTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AgentAliasRoutingConfigurationListItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AgentDescriptor:
    boto3_raw_data: "type_defs.AgentDescriptorTypeDef" = dataclasses.field()

    aliasArn = field("aliasArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AgentDescriptorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AgentDescriptorTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AgentFlowNodeConfiguration:
    boto3_raw_data: "type_defs.AgentFlowNodeConfigurationTypeDef" = dataclasses.field()

    agentAliasArn = field("agentAliasArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AgentFlowNodeConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AgentFlowNodeConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AgentKnowledgeBaseSummary:
    boto3_raw_data: "type_defs.AgentKnowledgeBaseSummaryTypeDef" = dataclasses.field()

    knowledgeBaseId = field("knowledgeBaseId")
    knowledgeBaseState = field("knowledgeBaseState")
    updatedAt = field("updatedAt")
    description = field("description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AgentKnowledgeBaseSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AgentKnowledgeBaseSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AgentKnowledgeBase:
    boto3_raw_data: "type_defs.AgentKnowledgeBaseTypeDef" = dataclasses.field()

    agentId = field("agentId")
    agentVersion = field("agentVersion")
    knowledgeBaseId = field("knowledgeBaseId")
    description = field("description")
    createdAt = field("createdAt")
    updatedAt = field("updatedAt")
    knowledgeBaseState = field("knowledgeBaseState")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AgentKnowledgeBaseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AgentKnowledgeBaseTypeDef"]
        ],
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
class AssociateAgentKnowledgeBaseRequest:
    boto3_raw_data: "type_defs.AssociateAgentKnowledgeBaseRequestTypeDef" = (
        dataclasses.field()
    )

    agentId = field("agentId")
    agentVersion = field("agentVersion")
    knowledgeBaseId = field("knowledgeBaseId")
    description = field("description")
    knowledgeBaseState = field("knowledgeBaseState")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateAgentKnowledgeBaseRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateAgentKnowledgeBaseRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BedrockDataAutomationConfiguration:
    boto3_raw_data: "type_defs.BedrockDataAutomationConfigurationTypeDef" = (
        dataclasses.field()
    )

    parsingModality = field("parsingModality")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BedrockDataAutomationConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BedrockDataAutomationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BedrockEmbeddingModelConfiguration:
    boto3_raw_data: "type_defs.BedrockEmbeddingModelConfigurationTypeDef" = (
        dataclasses.field()
    )

    dimensions = field("dimensions")
    embeddingDataType = field("embeddingDataType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BedrockEmbeddingModelConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BedrockEmbeddingModelConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ParsingPrompt:
    boto3_raw_data: "type_defs.ParsingPromptTypeDef" = dataclasses.field()

    parsingPromptText = field("parsingPromptText")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ParsingPromptTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ParsingPromptTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnrichmentStrategyConfiguration:
    boto3_raw_data: "type_defs.EnrichmentStrategyConfigurationTypeDef" = (
        dataclasses.field()
    )

    method = field("method")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.EnrichmentStrategyConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnrichmentStrategyConfigurationTypeDef"]
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
class PromptInputVariable:
    boto3_raw_data: "type_defs.PromptInputVariableTypeDef" = dataclasses.field()

    name = field("name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PromptInputVariableTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PromptInputVariableTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FixedSizeChunkingConfiguration:
    boto3_raw_data: "type_defs.FixedSizeChunkingConfigurationTypeDef" = (
        dataclasses.field()
    )

    maxTokens = field("maxTokens")
    overlapPercentage = field("overlapPercentage")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.FixedSizeChunkingConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FixedSizeChunkingConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SemanticChunkingConfiguration:
    boto3_raw_data: "type_defs.SemanticChunkingConfigurationTypeDef" = (
        dataclasses.field()
    )

    maxTokens = field("maxTokens")
    bufferSize = field("bufferSize")
    breakpointPercentileThreshold = field("breakpointPercentileThreshold")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SemanticChunkingConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SemanticChunkingConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FlowCondition:
    boto3_raw_data: "type_defs.FlowConditionTypeDef" = dataclasses.field()

    name = field("name")
    expression = field("expression")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FlowConditionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FlowConditionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfluenceSourceConfiguration:
    boto3_raw_data: "type_defs.ConfluenceSourceConfigurationTypeDef" = (
        dataclasses.field()
    )

    hostUrl = field("hostUrl")
    hostType = field("hostType")
    authType = field("authType")
    credentialsSecretArn = field("credentialsSecretArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ConfluenceSourceConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfluenceSourceConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServerSideEncryptionConfiguration:
    boto3_raw_data: "type_defs.ServerSideEncryptionConfigurationTypeDef" = (
        dataclasses.field()
    )

    kmsKeyArn = field("kmsKeyArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ServerSideEncryptionConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServerSideEncryptionConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FlowAliasConcurrencyConfiguration:
    boto3_raw_data: "type_defs.FlowAliasConcurrencyConfigurationTypeDef" = (
        dataclasses.field()
    )

    type = field("type")
    maxConcurrency = field("maxConcurrency")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.FlowAliasConcurrencyConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FlowAliasConcurrencyConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FlowAliasRoutingConfigurationListItem:
    boto3_raw_data: "type_defs.FlowAliasRoutingConfigurationListItemTypeDef" = (
        dataclasses.field()
    )

    flowVersion = field("flowVersion")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.FlowAliasRoutingConfigurationListItemTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FlowAliasRoutingConfigurationListItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFlowVersionRequest:
    boto3_raw_data: "type_defs.CreateFlowVersionRequestTypeDef" = dataclasses.field()

    flowIdentifier = field("flowIdentifier")
    description = field("description")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateFlowVersionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFlowVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePromptVersionRequest:
    boto3_raw_data: "type_defs.CreatePromptVersionRequestTypeDef" = dataclasses.field()

    promptIdentifier = field("promptIdentifier")
    description = field("description")
    clientToken = field("clientToken")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePromptVersionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePromptVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CuratedQuery:
    boto3_raw_data: "type_defs.CuratedQueryTypeDef" = dataclasses.field()

    naturalLanguage = field("naturalLanguage")
    sql = field("sql")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CuratedQueryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CuratedQueryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomDocumentIdentifier:
    boto3_raw_data: "type_defs.CustomDocumentIdentifierTypeDef" = dataclasses.field()

    id = field("id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CustomDocumentIdentifierTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomDocumentIdentifierTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomS3Location:
    boto3_raw_data: "type_defs.CustomS3LocationTypeDef" = dataclasses.field()

    uri = field("uri")
    bucketOwnerAccountId = field("bucketOwnerAccountId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CustomS3LocationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomS3LocationTypeDef"]
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
class CyclicConnectionFlowValidationDetails:
    boto3_raw_data: "type_defs.CyclicConnectionFlowValidationDetailsTypeDef" = (
        dataclasses.field()
    )

    connection = field("connection")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CyclicConnectionFlowValidationDetailsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CyclicConnectionFlowValidationDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3DataSourceConfigurationOutput:
    boto3_raw_data: "type_defs.S3DataSourceConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    bucketArn = field("bucketArn")
    inclusionPrefixes = field("inclusionPrefixes")
    bucketOwnerAccountId = field("bucketOwnerAccountId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.S3DataSourceConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3DataSourceConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3DataSourceConfiguration:
    boto3_raw_data: "type_defs.S3DataSourceConfigurationTypeDef" = dataclasses.field()

    bucketArn = field("bucketArn")
    inclusionPrefixes = field("inclusionPrefixes")
    bucketOwnerAccountId = field("bucketOwnerAccountId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3DataSourceConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3DataSourceConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataSourceSummary:
    boto3_raw_data: "type_defs.DataSourceSummaryTypeDef" = dataclasses.field()

    knowledgeBaseId = field("knowledgeBaseId")
    dataSourceId = field("dataSourceId")
    name = field("name")
    status = field("status")
    updatedAt = field("updatedAt")
    description = field("description")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DataSourceSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataSourceSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAgentActionGroupRequest:
    boto3_raw_data: "type_defs.DeleteAgentActionGroupRequestTypeDef" = (
        dataclasses.field()
    )

    agentId = field("agentId")
    agentVersion = field("agentVersion")
    actionGroupId = field("actionGroupId")
    skipResourceInUseCheck = field("skipResourceInUseCheck")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteAgentActionGroupRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAgentActionGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAgentAliasRequest:
    boto3_raw_data: "type_defs.DeleteAgentAliasRequestTypeDef" = dataclasses.field()

    agentId = field("agentId")
    agentAliasId = field("agentAliasId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAgentAliasRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAgentAliasRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAgentRequest:
    boto3_raw_data: "type_defs.DeleteAgentRequestTypeDef" = dataclasses.field()

    agentId = field("agentId")
    skipResourceInUseCheck = field("skipResourceInUseCheck")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAgentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAgentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAgentVersionRequest:
    boto3_raw_data: "type_defs.DeleteAgentVersionRequestTypeDef" = dataclasses.field()

    agentId = field("agentId")
    agentVersion = field("agentVersion")
    skipResourceInUseCheck = field("skipResourceInUseCheck")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAgentVersionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAgentVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDataSourceRequest:
    boto3_raw_data: "type_defs.DeleteDataSourceRequestTypeDef" = dataclasses.field()

    knowledgeBaseId = field("knowledgeBaseId")
    dataSourceId = field("dataSourceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDataSourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDataSourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteFlowAliasRequest:
    boto3_raw_data: "type_defs.DeleteFlowAliasRequestTypeDef" = dataclasses.field()

    flowIdentifier = field("flowIdentifier")
    aliasIdentifier = field("aliasIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteFlowAliasRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteFlowAliasRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteFlowRequest:
    boto3_raw_data: "type_defs.DeleteFlowRequestTypeDef" = dataclasses.field()

    flowIdentifier = field("flowIdentifier")
    skipResourceInUseCheck = field("skipResourceInUseCheck")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteFlowRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteFlowRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteFlowVersionRequest:
    boto3_raw_data: "type_defs.DeleteFlowVersionRequestTypeDef" = dataclasses.field()

    flowIdentifier = field("flowIdentifier")
    flowVersion = field("flowVersion")
    skipResourceInUseCheck = field("skipResourceInUseCheck")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteFlowVersionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteFlowVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteKnowledgeBaseRequest:
    boto3_raw_data: "type_defs.DeleteKnowledgeBaseRequestTypeDef" = dataclasses.field()

    knowledgeBaseId = field("knowledgeBaseId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteKnowledgeBaseRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteKnowledgeBaseRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePromptRequest:
    boto3_raw_data: "type_defs.DeletePromptRequestTypeDef" = dataclasses.field()

    promptIdentifier = field("promptIdentifier")
    promptVersion = field("promptVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeletePromptRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePromptRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateAgentCollaboratorRequest:
    boto3_raw_data: "type_defs.DisassociateAgentCollaboratorRequestTypeDef" = (
        dataclasses.field()
    )

    agentId = field("agentId")
    agentVersion = field("agentVersion")
    collaboratorId = field("collaboratorId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateAgentCollaboratorRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateAgentCollaboratorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateAgentKnowledgeBaseRequest:
    boto3_raw_data: "type_defs.DisassociateAgentKnowledgeBaseRequestTypeDef" = (
        dataclasses.field()
    )

    agentId = field("agentId")
    agentVersion = field("agentVersion")
    knowledgeBaseId = field("knowledgeBaseId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateAgentKnowledgeBaseRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateAgentKnowledgeBaseRequestTypeDef"]
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
class DuplicateConditionExpressionFlowValidationDetails:
    boto3_raw_data: (
        "type_defs.DuplicateConditionExpressionFlowValidationDetailsTypeDef"
    ) = dataclasses.field()

    node = field("node")
    expression = field("expression")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DuplicateConditionExpressionFlowValidationDetailsTypeDef"
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
                "type_defs.DuplicateConditionExpressionFlowValidationDetailsTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DuplicateConnectionsFlowValidationDetails:
    boto3_raw_data: "type_defs.DuplicateConnectionsFlowValidationDetailsTypeDef" = (
        dataclasses.field()
    )

    source = field("source")
    target = field("target")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DuplicateConnectionsFlowValidationDetailsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DuplicateConnectionsFlowValidationDetailsTypeDef"]
        ],
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
class FlowConditionalConnectionConfiguration:
    boto3_raw_data: "type_defs.FlowConditionalConnectionConfigurationTypeDef" = (
        dataclasses.field()
    )

    condition = field("condition")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.FlowConditionalConnectionConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FlowConditionalConnectionConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FlowDataConnectionConfiguration:
    boto3_raw_data: "type_defs.FlowDataConnectionConfigurationTypeDef" = (
        dataclasses.field()
    )

    sourceOutput = field("sourceOutput")
    targetInput = field("targetInput")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.FlowDataConnectionConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FlowDataConnectionConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InlineCodeFlowNodeConfiguration:
    boto3_raw_data: "type_defs.InlineCodeFlowNodeConfigurationTypeDef" = (
        dataclasses.field()
    )

    code = field("code")
    language = field("language")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.InlineCodeFlowNodeConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InlineCodeFlowNodeConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LambdaFunctionFlowNodeConfiguration:
    boto3_raw_data: "type_defs.LambdaFunctionFlowNodeConfigurationTypeDef" = (
        dataclasses.field()
    )

    lambdaArn = field("lambdaArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.LambdaFunctionFlowNodeConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LambdaFunctionFlowNodeConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LexFlowNodeConfiguration:
    boto3_raw_data: "type_defs.LexFlowNodeConfigurationTypeDef" = dataclasses.field()

    botAliasArn = field("botAliasArn")
    localeId = field("localeId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LexFlowNodeConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LexFlowNodeConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoopFlowNodeConfigurationOutput:
    boto3_raw_data: "type_defs.LoopFlowNodeConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    definition = field("definition")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.LoopFlowNodeConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LoopFlowNodeConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoopFlowNodeConfiguration:
    boto3_raw_data: "type_defs.LoopFlowNodeConfigurationTypeDef" = dataclasses.field()

    definition = field("definition")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LoopFlowNodeConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LoopFlowNodeConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FlowNodeInput:
    boto3_raw_data: "type_defs.FlowNodeInputTypeDef" = dataclasses.field()

    name = field("name")
    type = field("type")
    expression = field("expression")
    category = field("category")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FlowNodeInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FlowNodeInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FlowNodeOutput:
    boto3_raw_data: "type_defs.FlowNodeOutputTypeDef" = dataclasses.field()

    name = field("name")
    type = field("type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FlowNodeOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FlowNodeOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FlowSummary:
    boto3_raw_data: "type_defs.FlowSummaryTypeDef" = dataclasses.field()

    name = field("name")
    id = field("id")
    arn = field("arn")
    status = field("status")
    createdAt = field("createdAt")
    updatedAt = field("updatedAt")
    version = field("version")
    description = field("description")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FlowSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FlowSummaryTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IncompatibleConnectionDataTypeFlowValidationDetails:
    boto3_raw_data: (
        "type_defs.IncompatibleConnectionDataTypeFlowValidationDetailsTypeDef"
    ) = dataclasses.field()

    connection = field("connection")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.IncompatibleConnectionDataTypeFlowValidationDetailsTypeDef"
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
                "type_defs.IncompatibleConnectionDataTypeFlowValidationDetailsTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InvalidLoopBoundaryFlowValidationDetails:
    boto3_raw_data: "type_defs.InvalidLoopBoundaryFlowValidationDetailsTypeDef" = (
        dataclasses.field()
    )

    connection = field("connection")
    source = field("source")
    target = field("target")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.InvalidLoopBoundaryFlowValidationDetailsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InvalidLoopBoundaryFlowValidationDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoopIncompatibleNodeTypeFlowValidationDetails:
    boto3_raw_data: "type_defs.LoopIncompatibleNodeTypeFlowValidationDetailsTypeDef" = (
        dataclasses.field()
    )

    node = field("node")
    incompatibleNodeType = field("incompatibleNodeType")
    incompatibleNodeName = field("incompatibleNodeName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.LoopIncompatibleNodeTypeFlowValidationDetailsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LoopIncompatibleNodeTypeFlowValidationDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MalformedConditionExpressionFlowValidationDetails:
    boto3_raw_data: (
        "type_defs.MalformedConditionExpressionFlowValidationDetailsTypeDef"
    ) = dataclasses.field()

    node = field("node")
    condition = field("condition")
    cause = field("cause")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MalformedConditionExpressionFlowValidationDetailsTypeDef"
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
                "type_defs.MalformedConditionExpressionFlowValidationDetailsTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MalformedNodeInputExpressionFlowValidationDetails:
    boto3_raw_data: (
        "type_defs.MalformedNodeInputExpressionFlowValidationDetailsTypeDef"
    ) = dataclasses.field()

    node = field("node")
    input = field("input")
    cause = field("cause")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MalformedNodeInputExpressionFlowValidationDetailsTypeDef"
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
                "type_defs.MalformedNodeInputExpressionFlowValidationDetailsTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MismatchedNodeInputTypeFlowValidationDetails:
    boto3_raw_data: "type_defs.MismatchedNodeInputTypeFlowValidationDetailsTypeDef" = (
        dataclasses.field()
    )

    node = field("node")
    input = field("input")
    expectedType = field("expectedType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MismatchedNodeInputTypeFlowValidationDetailsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MismatchedNodeInputTypeFlowValidationDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MismatchedNodeOutputTypeFlowValidationDetails:
    boto3_raw_data: "type_defs.MismatchedNodeOutputTypeFlowValidationDetailsTypeDef" = (
        dataclasses.field()
    )

    node = field("node")
    output = field("output")
    expectedType = field("expectedType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MismatchedNodeOutputTypeFlowValidationDetailsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MismatchedNodeOutputTypeFlowValidationDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MissingConnectionConfigurationFlowValidationDetails:
    boto3_raw_data: (
        "type_defs.MissingConnectionConfigurationFlowValidationDetailsTypeDef"
    ) = dataclasses.field()

    connection = field("connection")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MissingConnectionConfigurationFlowValidationDetailsTypeDef"
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
                "type_defs.MissingConnectionConfigurationFlowValidationDetailsTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MissingDefaultConditionFlowValidationDetails:
    boto3_raw_data: "type_defs.MissingDefaultConditionFlowValidationDetailsTypeDef" = (
        dataclasses.field()
    )

    node = field("node")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MissingDefaultConditionFlowValidationDetailsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MissingDefaultConditionFlowValidationDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MissingLoopControllerNodeFlowValidationDetails:
    boto3_raw_data: (
        "type_defs.MissingLoopControllerNodeFlowValidationDetailsTypeDef"
    ) = dataclasses.field()

    loopNode = field("loopNode")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MissingLoopControllerNodeFlowValidationDetailsTypeDef"
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
                "type_defs.MissingLoopControllerNodeFlowValidationDetailsTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MissingLoopInputNodeFlowValidationDetails:
    boto3_raw_data: "type_defs.MissingLoopInputNodeFlowValidationDetailsTypeDef" = (
        dataclasses.field()
    )

    loopNode = field("loopNode")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MissingLoopInputNodeFlowValidationDetailsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MissingLoopInputNodeFlowValidationDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MissingNodeConfigurationFlowValidationDetails:
    boto3_raw_data: "type_defs.MissingNodeConfigurationFlowValidationDetailsTypeDef" = (
        dataclasses.field()
    )

    node = field("node")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MissingNodeConfigurationFlowValidationDetailsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MissingNodeConfigurationFlowValidationDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MissingNodeInputFlowValidationDetails:
    boto3_raw_data: "type_defs.MissingNodeInputFlowValidationDetailsTypeDef" = (
        dataclasses.field()
    )

    node = field("node")
    input = field("input")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MissingNodeInputFlowValidationDetailsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MissingNodeInputFlowValidationDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MissingNodeOutputFlowValidationDetails:
    boto3_raw_data: "type_defs.MissingNodeOutputFlowValidationDetailsTypeDef" = (
        dataclasses.field()
    )

    node = field("node")
    output = field("output")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MissingNodeOutputFlowValidationDetailsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MissingNodeOutputFlowValidationDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MultipleLoopControllerNodesFlowValidationDetails:
    boto3_raw_data: (
        "type_defs.MultipleLoopControllerNodesFlowValidationDetailsTypeDef"
    ) = dataclasses.field()

    loopNode = field("loopNode")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MultipleLoopControllerNodesFlowValidationDetailsTypeDef"
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
                "type_defs.MultipleLoopControllerNodesFlowValidationDetailsTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MultipleLoopInputNodesFlowValidationDetails:
    boto3_raw_data: "type_defs.MultipleLoopInputNodesFlowValidationDetailsTypeDef" = (
        dataclasses.field()
    )

    loopNode = field("loopNode")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MultipleLoopInputNodesFlowValidationDetailsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MultipleLoopInputNodesFlowValidationDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MultipleNodeInputConnectionsFlowValidationDetails:
    boto3_raw_data: (
        "type_defs.MultipleNodeInputConnectionsFlowValidationDetailsTypeDef"
    ) = dataclasses.field()

    node = field("node")
    input = field("input")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MultipleNodeInputConnectionsFlowValidationDetailsTypeDef"
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
                "type_defs.MultipleNodeInputConnectionsFlowValidationDetailsTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UnfulfilledNodeInputFlowValidationDetails:
    boto3_raw_data: "type_defs.UnfulfilledNodeInputFlowValidationDetailsTypeDef" = (
        dataclasses.field()
    )

    node = field("node")
    input = field("input")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UnfulfilledNodeInputFlowValidationDetailsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UnfulfilledNodeInputFlowValidationDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UnknownConnectionConditionFlowValidationDetails:
    boto3_raw_data: (
        "type_defs.UnknownConnectionConditionFlowValidationDetailsTypeDef"
    ) = dataclasses.field()

    connection = field("connection")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UnknownConnectionConditionFlowValidationDetailsTypeDef"
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
                "type_defs.UnknownConnectionConditionFlowValidationDetailsTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UnknownConnectionSourceFlowValidationDetails:
    boto3_raw_data: "type_defs.UnknownConnectionSourceFlowValidationDetailsTypeDef" = (
        dataclasses.field()
    )

    connection = field("connection")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UnknownConnectionSourceFlowValidationDetailsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UnknownConnectionSourceFlowValidationDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UnknownConnectionSourceOutputFlowValidationDetails:
    boto3_raw_data: (
        "type_defs.UnknownConnectionSourceOutputFlowValidationDetailsTypeDef"
    ) = dataclasses.field()

    connection = field("connection")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UnknownConnectionSourceOutputFlowValidationDetailsTypeDef"
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
                "type_defs.UnknownConnectionSourceOutputFlowValidationDetailsTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UnknownConnectionTargetFlowValidationDetails:
    boto3_raw_data: "type_defs.UnknownConnectionTargetFlowValidationDetailsTypeDef" = (
        dataclasses.field()
    )

    connection = field("connection")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UnknownConnectionTargetFlowValidationDetailsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UnknownConnectionTargetFlowValidationDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UnknownConnectionTargetInputFlowValidationDetails:
    boto3_raw_data: (
        "type_defs.UnknownConnectionTargetInputFlowValidationDetailsTypeDef"
    ) = dataclasses.field()

    connection = field("connection")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UnknownConnectionTargetInputFlowValidationDetailsTypeDef"
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
                "type_defs.UnknownConnectionTargetInputFlowValidationDetailsTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UnknownNodeInputFlowValidationDetails:
    boto3_raw_data: "type_defs.UnknownNodeInputFlowValidationDetailsTypeDef" = (
        dataclasses.field()
    )

    node = field("node")
    input = field("input")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UnknownNodeInputFlowValidationDetailsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UnknownNodeInputFlowValidationDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UnknownNodeOutputFlowValidationDetails:
    boto3_raw_data: "type_defs.UnknownNodeOutputFlowValidationDetailsTypeDef" = (
        dataclasses.field()
    )

    node = field("node")
    output = field("output")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UnknownNodeOutputFlowValidationDetailsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UnknownNodeOutputFlowValidationDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UnreachableNodeFlowValidationDetails:
    boto3_raw_data: "type_defs.UnreachableNodeFlowValidationDetailsTypeDef" = (
        dataclasses.field()
    )

    node = field("node")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UnreachableNodeFlowValidationDetailsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UnreachableNodeFlowValidationDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UnsatisfiedConnectionConditionsFlowValidationDetails:
    boto3_raw_data: (
        "type_defs.UnsatisfiedConnectionConditionsFlowValidationDetailsTypeDef"
    ) = dataclasses.field()

    connection = field("connection")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UnsatisfiedConnectionConditionsFlowValidationDetailsTypeDef"
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
                "type_defs.UnsatisfiedConnectionConditionsFlowValidationDetailsTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FlowVersionSummary:
    boto3_raw_data: "type_defs.FlowVersionSummaryTypeDef" = dataclasses.field()

    id = field("id")
    arn = field("arn")
    status = field("status")
    createdAt = field("createdAt")
    version = field("version")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FlowVersionSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FlowVersionSummaryTypeDef"]
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
class GetAgentActionGroupRequest:
    boto3_raw_data: "type_defs.GetAgentActionGroupRequestTypeDef" = dataclasses.field()

    agentId = field("agentId")
    agentVersion = field("agentVersion")
    actionGroupId = field("actionGroupId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAgentActionGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAgentActionGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAgentAliasRequest:
    boto3_raw_data: "type_defs.GetAgentAliasRequestTypeDef" = dataclasses.field()

    agentId = field("agentId")
    agentAliasId = field("agentAliasId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAgentAliasRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAgentAliasRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAgentCollaboratorRequest:
    boto3_raw_data: "type_defs.GetAgentCollaboratorRequestTypeDef" = dataclasses.field()

    agentId = field("agentId")
    agentVersion = field("agentVersion")
    collaboratorId = field("collaboratorId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAgentCollaboratorRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAgentCollaboratorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAgentKnowledgeBaseRequest:
    boto3_raw_data: "type_defs.GetAgentKnowledgeBaseRequestTypeDef" = (
        dataclasses.field()
    )

    agentId = field("agentId")
    agentVersion = field("agentVersion")
    knowledgeBaseId = field("knowledgeBaseId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAgentKnowledgeBaseRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAgentKnowledgeBaseRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAgentRequest:
    boto3_raw_data: "type_defs.GetAgentRequestTypeDef" = dataclasses.field()

    agentId = field("agentId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetAgentRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetAgentRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAgentVersionRequest:
    boto3_raw_data: "type_defs.GetAgentVersionRequestTypeDef" = dataclasses.field()

    agentId = field("agentId")
    agentVersion = field("agentVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAgentVersionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAgentVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDataSourceRequest:
    boto3_raw_data: "type_defs.GetDataSourceRequestTypeDef" = dataclasses.field()

    knowledgeBaseId = field("knowledgeBaseId")
    dataSourceId = field("dataSourceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDataSourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDataSourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFlowAliasRequest:
    boto3_raw_data: "type_defs.GetFlowAliasRequestTypeDef" = dataclasses.field()

    flowIdentifier = field("flowIdentifier")
    aliasIdentifier = field("aliasIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetFlowAliasRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFlowAliasRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFlowRequest:
    boto3_raw_data: "type_defs.GetFlowRequestTypeDef" = dataclasses.field()

    flowIdentifier = field("flowIdentifier")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetFlowRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetFlowRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFlowVersionRequest:
    boto3_raw_data: "type_defs.GetFlowVersionRequestTypeDef" = dataclasses.field()

    flowIdentifier = field("flowIdentifier")
    flowVersion = field("flowVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetFlowVersionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFlowVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetIngestionJobRequest:
    boto3_raw_data: "type_defs.GetIngestionJobRequestTypeDef" = dataclasses.field()

    knowledgeBaseId = field("knowledgeBaseId")
    dataSourceId = field("dataSourceId")
    ingestionJobId = field("ingestionJobId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetIngestionJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetIngestionJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetKnowledgeBaseRequest:
    boto3_raw_data: "type_defs.GetKnowledgeBaseRequestTypeDef" = dataclasses.field()

    knowledgeBaseId = field("knowledgeBaseId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetKnowledgeBaseRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetKnowledgeBaseRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPromptRequest:
    boto3_raw_data: "type_defs.GetPromptRequestTypeDef" = dataclasses.field()

    promptIdentifier = field("promptIdentifier")
    promptVersion = field("promptVersion")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetPromptRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPromptRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HierarchicalChunkingLevelConfiguration:
    boto3_raw_data: "type_defs.HierarchicalChunkingLevelConfigurationTypeDef" = (
        dataclasses.field()
    )

    maxTokens = field("maxTokens")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.HierarchicalChunkingLevelConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HierarchicalChunkingLevelConfigurationTypeDef"]
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

    temperature = field("temperature")
    topP = field("topP")
    topK = field("topK")
    maximumLength = field("maximumLength")
    stopSequences = field("stopSequences")

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

    temperature = field("temperature")
    topP = field("topP")
    topK = field("topK")
    maximumLength = field("maximumLength")
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
class IngestionJobFilter:
    boto3_raw_data: "type_defs.IngestionJobFilterTypeDef" = dataclasses.field()

    attribute = field("attribute")
    operator = field("operator")
    values = field("values")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IngestionJobFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IngestionJobFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IngestionJobSortBy:
    boto3_raw_data: "type_defs.IngestionJobSortByTypeDef" = dataclasses.field()

    attribute = field("attribute")
    order = field("order")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IngestionJobSortByTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IngestionJobSortByTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IngestionJobStatistics:
    boto3_raw_data: "type_defs.IngestionJobStatisticsTypeDef" = dataclasses.field()

    numberOfDocumentsScanned = field("numberOfDocumentsScanned")
    numberOfMetadataDocumentsScanned = field("numberOfMetadataDocumentsScanned")
    numberOfNewDocumentsIndexed = field("numberOfNewDocumentsIndexed")
    numberOfModifiedDocumentsIndexed = field("numberOfModifiedDocumentsIndexed")
    numberOfMetadataDocumentsModified = field("numberOfMetadataDocumentsModified")
    numberOfDocumentsDeleted = field("numberOfDocumentsDeleted")
    numberOfDocumentsFailed = field("numberOfDocumentsFailed")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IngestionJobStatisticsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IngestionJobStatisticsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TextContentDoc:
    boto3_raw_data: "type_defs.TextContentDocTypeDef" = dataclasses.field()

    data = field("data")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TextContentDocTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TextContentDocTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KendraKnowledgeBaseConfiguration:
    boto3_raw_data: "type_defs.KendraKnowledgeBaseConfigurationTypeDef" = (
        dataclasses.field()
    )

    kendraIndexArn = field("kendraIndexArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.KendraKnowledgeBaseConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KendraKnowledgeBaseConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KnowledgeBasePromptTemplate:
    boto3_raw_data: "type_defs.KnowledgeBasePromptTemplateTypeDef" = dataclasses.field()

    textPromptTemplate = field("textPromptTemplate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KnowledgeBasePromptTemplateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KnowledgeBasePromptTemplateTypeDef"]
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
class KnowledgeBaseSummary:
    boto3_raw_data: "type_defs.KnowledgeBaseSummaryTypeDef" = dataclasses.field()

    knowledgeBaseId = field("knowledgeBaseId")
    name = field("name")
    status = field("status")
    updatedAt = field("updatedAt")
    description = field("description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KnowledgeBaseSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KnowledgeBaseSummaryTypeDef"]
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
class ListAgentActionGroupsRequest:
    boto3_raw_data: "type_defs.ListAgentActionGroupsRequestTypeDef" = (
        dataclasses.field()
    )

    agentId = field("agentId")
    agentVersion = field("agentVersion")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAgentActionGroupsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAgentActionGroupsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAgentAliasesRequest:
    boto3_raw_data: "type_defs.ListAgentAliasesRequestTypeDef" = dataclasses.field()

    agentId = field("agentId")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAgentAliasesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAgentAliasesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAgentCollaboratorsRequest:
    boto3_raw_data: "type_defs.ListAgentCollaboratorsRequestTypeDef" = (
        dataclasses.field()
    )

    agentId = field("agentId")
    agentVersion = field("agentVersion")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAgentCollaboratorsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAgentCollaboratorsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAgentKnowledgeBasesRequest:
    boto3_raw_data: "type_defs.ListAgentKnowledgeBasesRequestTypeDef" = (
        dataclasses.field()
    )

    agentId = field("agentId")
    agentVersion = field("agentVersion")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAgentKnowledgeBasesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAgentKnowledgeBasesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAgentVersionsRequest:
    boto3_raw_data: "type_defs.ListAgentVersionsRequestTypeDef" = dataclasses.field()

    agentId = field("agentId")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAgentVersionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAgentVersionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAgentsRequest:
    boto3_raw_data: "type_defs.ListAgentsRequestTypeDef" = dataclasses.field()

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListAgentsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAgentsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDataSourcesRequest:
    boto3_raw_data: "type_defs.ListDataSourcesRequestTypeDef" = dataclasses.field()

    knowledgeBaseId = field("knowledgeBaseId")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDataSourcesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDataSourcesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFlowAliasesRequest:
    boto3_raw_data: "type_defs.ListFlowAliasesRequestTypeDef" = dataclasses.field()

    flowIdentifier = field("flowIdentifier")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFlowAliasesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFlowAliasesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFlowVersionsRequest:
    boto3_raw_data: "type_defs.ListFlowVersionsRequestTypeDef" = dataclasses.field()

    flowIdentifier = field("flowIdentifier")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFlowVersionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFlowVersionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFlowsRequest:
    boto3_raw_data: "type_defs.ListFlowsRequestTypeDef" = dataclasses.field()

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListFlowsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFlowsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListKnowledgeBaseDocumentsRequest:
    boto3_raw_data: "type_defs.ListKnowledgeBaseDocumentsRequestTypeDef" = (
        dataclasses.field()
    )

    knowledgeBaseId = field("knowledgeBaseId")
    dataSourceId = field("dataSourceId")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListKnowledgeBaseDocumentsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListKnowledgeBaseDocumentsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListKnowledgeBasesRequest:
    boto3_raw_data: "type_defs.ListKnowledgeBasesRequestTypeDef" = dataclasses.field()

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListKnowledgeBasesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListKnowledgeBasesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPromptsRequest:
    boto3_raw_data: "type_defs.ListPromptsRequestTypeDef" = dataclasses.field()

    promptIdentifier = field("promptIdentifier")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPromptsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPromptsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PromptSummary:
    boto3_raw_data: "type_defs.PromptSummaryTypeDef" = dataclasses.field()

    name = field("name")
    id = field("id")
    arn = field("arn")
    version = field("version")
    createdAt = field("createdAt")
    updatedAt = field("updatedAt")
    description = field("description")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PromptSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PromptSummaryTypeDef"]],
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
class SessionSummaryConfiguration:
    boto3_raw_data: "type_defs.SessionSummaryConfigurationTypeDef" = dataclasses.field()

    maxRecentSessions = field("maxRecentSessions")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SessionSummaryConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SessionSummaryConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetadataAttributeValue:
    boto3_raw_data: "type_defs.MetadataAttributeValueTypeDef" = dataclasses.field()

    type = field("type")
    numberValue = field("numberValue")
    booleanValue = field("booleanValue")
    stringValue = field("stringValue")
    stringListValue = field("stringListValue")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MetadataAttributeValueTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MetadataAttributeValueTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MongoDbAtlasFieldMapping:
    boto3_raw_data: "type_defs.MongoDbAtlasFieldMappingTypeDef" = dataclasses.field()

    vectorField = field("vectorField")
    textField = field("textField")
    metadataField = field("metadataField")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MongoDbAtlasFieldMappingTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MongoDbAtlasFieldMappingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NeptuneAnalyticsFieldMapping:
    boto3_raw_data: "type_defs.NeptuneAnalyticsFieldMappingTypeDef" = (
        dataclasses.field()
    )

    textField = field("textField")
    metadataField = field("metadataField")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NeptuneAnalyticsFieldMappingTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NeptuneAnalyticsFieldMappingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpenSearchManagedClusterFieldMapping:
    boto3_raw_data: "type_defs.OpenSearchManagedClusterFieldMappingTypeDef" = (
        dataclasses.field()
    )

    vectorField = field("vectorField")
    textField = field("textField")
    metadataField = field("metadataField")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.OpenSearchManagedClusterFieldMappingTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OpenSearchManagedClusterFieldMappingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpenSearchServerlessFieldMapping:
    boto3_raw_data: "type_defs.OpenSearchServerlessFieldMappingTypeDef" = (
        dataclasses.field()
    )

    vectorField = field("vectorField")
    textField = field("textField")
    metadataField = field("metadataField")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.OpenSearchServerlessFieldMappingTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OpenSearchServerlessFieldMappingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PatternObjectFilterOutput:
    boto3_raw_data: "type_defs.PatternObjectFilterOutputTypeDef" = dataclasses.field()

    objectType = field("objectType")
    inclusionFilters = field("inclusionFilters")
    exclusionFilters = field("exclusionFilters")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PatternObjectFilterOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PatternObjectFilterOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PatternObjectFilter:
    boto3_raw_data: "type_defs.PatternObjectFilterTypeDef" = dataclasses.field()

    objectType = field("objectType")
    inclusionFilters = field("inclusionFilters")
    exclusionFilters = field("exclusionFilters")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PatternObjectFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PatternObjectFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PineconeFieldMapping:
    boto3_raw_data: "type_defs.PineconeFieldMappingTypeDef" = dataclasses.field()

    textField = field("textField")
    metadataField = field("metadataField")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PineconeFieldMappingTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PineconeFieldMappingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PrepareAgentRequest:
    boto3_raw_data: "type_defs.PrepareAgentRequestTypeDef" = dataclasses.field()

    agentId = field("agentId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PrepareAgentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PrepareAgentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PrepareFlowRequest:
    boto3_raw_data: "type_defs.PrepareFlowRequestTypeDef" = dataclasses.field()

    flowIdentifier = field("flowIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PrepareFlowRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PrepareFlowRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PromptAgentResource:
    boto3_raw_data: "type_defs.PromptAgentResourceTypeDef" = dataclasses.field()

    agentIdentifier = field("agentIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PromptAgentResourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PromptAgentResourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PromptFlowNodeResourceConfiguration:
    boto3_raw_data: "type_defs.PromptFlowNodeResourceConfigurationTypeDef" = (
        dataclasses.field()
    )

    promptArn = field("promptArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PromptFlowNodeResourceConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PromptFlowNodeResourceConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PromptModelInferenceConfigurationOutput:
    boto3_raw_data: "type_defs.PromptModelInferenceConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    temperature = field("temperature")
    topP = field("topP")
    maxTokens = field("maxTokens")
    stopSequences = field("stopSequences")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PromptModelInferenceConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PromptModelInferenceConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PromptMetadataEntry:
    boto3_raw_data: "type_defs.PromptMetadataEntryTypeDef" = dataclasses.field()

    key = field("key")
    value = field("value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PromptMetadataEntryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PromptMetadataEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PromptModelInferenceConfiguration:
    boto3_raw_data: "type_defs.PromptModelInferenceConfigurationTypeDef" = (
        dataclasses.field()
    )

    temperature = field("temperature")
    topP = field("topP")
    maxTokens = field("maxTokens")
    stopSequences = field("stopSequences")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PromptModelInferenceConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PromptModelInferenceConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryGenerationColumn:
    boto3_raw_data: "type_defs.QueryGenerationColumnTypeDef" = dataclasses.field()

    name = field("name")
    description = field("description")
    inclusion = field("inclusion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.QueryGenerationColumnTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QueryGenerationColumnTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RdsFieldMapping:
    boto3_raw_data: "type_defs.RdsFieldMappingTypeDef" = dataclasses.field()

    primaryKeyField = field("primaryKeyField")
    vectorField = field("vectorField")
    textField = field("textField")
    metadataField = field("metadataField")
    customMetadataField = field("customMetadataField")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RdsFieldMappingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RdsFieldMappingTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RedisEnterpriseCloudFieldMapping:
    boto3_raw_data: "type_defs.RedisEnterpriseCloudFieldMappingTypeDef" = (
        dataclasses.field()
    )

    vectorField = field("vectorField")
    textField = field("textField")
    metadataField = field("metadataField")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RedisEnterpriseCloudFieldMappingTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RedisEnterpriseCloudFieldMappingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RedshiftProvisionedAuthConfiguration:
    boto3_raw_data: "type_defs.RedshiftProvisionedAuthConfigurationTypeDef" = (
        dataclasses.field()
    )

    type = field("type")
    databaseUser = field("databaseUser")
    usernamePasswordSecretArn = field("usernamePasswordSecretArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RedshiftProvisionedAuthConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RedshiftProvisionedAuthConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RedshiftQueryEngineAwsDataCatalogStorageConfigurationOutput:
    boto3_raw_data: (
        "type_defs.RedshiftQueryEngineAwsDataCatalogStorageConfigurationOutputTypeDef"
    ) = dataclasses.field()

    tableNames = field("tableNames")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RedshiftQueryEngineAwsDataCatalogStorageConfigurationOutputTypeDef"
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
                "type_defs.RedshiftQueryEngineAwsDataCatalogStorageConfigurationOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RedshiftQueryEngineAwsDataCatalogStorageConfiguration:
    boto3_raw_data: (
        "type_defs.RedshiftQueryEngineAwsDataCatalogStorageConfigurationTypeDef"
    ) = dataclasses.field()

    tableNames = field("tableNames")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RedshiftQueryEngineAwsDataCatalogStorageConfigurationTypeDef"
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
                "type_defs.RedshiftQueryEngineAwsDataCatalogStorageConfigurationTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RedshiftQueryEngineRedshiftStorageConfiguration:
    boto3_raw_data: (
        "type_defs.RedshiftQueryEngineRedshiftStorageConfigurationTypeDef"
    ) = dataclasses.field()

    databaseName = field("databaseName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RedshiftQueryEngineRedshiftStorageConfigurationTypeDef"
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
                "type_defs.RedshiftQueryEngineRedshiftStorageConfigurationTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RedshiftServerlessAuthConfiguration:
    boto3_raw_data: "type_defs.RedshiftServerlessAuthConfigurationTypeDef" = (
        dataclasses.field()
    )

    type = field("type")
    usernamePasswordSecretArn = field("usernamePasswordSecretArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RedshiftServerlessAuthConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RedshiftServerlessAuthConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RetrievalFlowNodeS3Configuration:
    boto3_raw_data: "type_defs.RetrievalFlowNodeS3ConfigurationTypeDef" = (
        dataclasses.field()
    )

    bucketName = field("bucketName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RetrievalFlowNodeS3ConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RetrievalFlowNodeS3ConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3VectorsConfiguration:
    boto3_raw_data: "type_defs.S3VectorsConfigurationTypeDef" = dataclasses.field()

    vectorBucketArn = field("vectorBucketArn")
    indexArn = field("indexArn")
    indexName = field("indexName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3VectorsConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3VectorsConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SalesforceSourceConfiguration:
    boto3_raw_data: "type_defs.SalesforceSourceConfigurationTypeDef" = (
        dataclasses.field()
    )

    hostUrl = field("hostUrl")
    authType = field("authType")
    credentialsSecretArn = field("credentialsSecretArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SalesforceSourceConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SalesforceSourceConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SeedUrl:
    boto3_raw_data: "type_defs.SeedUrlTypeDef" = dataclasses.field()

    url = field("url")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SeedUrlTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SeedUrlTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SharePointSourceConfigurationOutput:
    boto3_raw_data: "type_defs.SharePointSourceConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    domain = field("domain")
    siteUrls = field("siteUrls")
    hostType = field("hostType")
    authType = field("authType")
    credentialsSecretArn = field("credentialsSecretArn")
    tenantId = field("tenantId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SharePointSourceConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SharePointSourceConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SharePointSourceConfiguration:
    boto3_raw_data: "type_defs.SharePointSourceConfigurationTypeDef" = (
        dataclasses.field()
    )

    domain = field("domain")
    siteUrls = field("siteUrls")
    hostType = field("hostType")
    authType = field("authType")
    credentialsSecretArn = field("credentialsSecretArn")
    tenantId = field("tenantId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SharePointSourceConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SharePointSourceConfigurationTypeDef"]
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
class StartIngestionJobRequest:
    boto3_raw_data: "type_defs.StartIngestionJobRequestTypeDef" = dataclasses.field()

    knowledgeBaseId = field("knowledgeBaseId")
    dataSourceId = field("dataSourceId")
    clientToken = field("clientToken")
    description = field("description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartIngestionJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartIngestionJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopIngestionJobRequest:
    boto3_raw_data: "type_defs.StopIngestionJobRequestTypeDef" = dataclasses.field()

    knowledgeBaseId = field("knowledgeBaseId")
    dataSourceId = field("dataSourceId")
    ingestionJobId = field("ingestionJobId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopIngestionJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopIngestionJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StorageFlowNodeS3Configuration:
    boto3_raw_data: "type_defs.StorageFlowNodeS3ConfigurationTypeDef" = (
        dataclasses.field()
    )

    bucketName = field("bucketName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StorageFlowNodeS3ConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StorageFlowNodeS3ConfigurationTypeDef"]
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
class ToolInputSchemaOutput:
    boto3_raw_data: "type_defs.ToolInputSchemaOutputTypeDef" = dataclasses.field()

    json = field("json")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ToolInputSchemaOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ToolInputSchemaOutputTypeDef"]
        ],
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
class TransformationLambdaConfiguration:
    boto3_raw_data: "type_defs.TransformationLambdaConfigurationTypeDef" = (
        dataclasses.field()
    )

    lambdaArn = field("lambdaArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.TransformationLambdaConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TransformationLambdaConfigurationTypeDef"]
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
class UpdateAgentKnowledgeBaseRequest:
    boto3_raw_data: "type_defs.UpdateAgentKnowledgeBaseRequestTypeDef" = (
        dataclasses.field()
    )

    agentId = field("agentId")
    agentVersion = field("agentVersion")
    knowledgeBaseId = field("knowledgeBaseId")
    description = field("description")
    knowledgeBaseState = field("knowledgeBaseState")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateAgentKnowledgeBaseRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAgentKnowledgeBaseRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VectorSearchBedrockRerankingModelConfigurationOutput:
    boto3_raw_data: (
        "type_defs.VectorSearchBedrockRerankingModelConfigurationOutputTypeDef"
    ) = dataclasses.field()

    modelArn = field("modelArn")
    additionalModelRequestFields = field("additionalModelRequestFields")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.VectorSearchBedrockRerankingModelConfigurationOutputTypeDef"
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
                "type_defs.VectorSearchBedrockRerankingModelConfigurationOutputTypeDef"
            ]
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
class WebCrawlerLimits:
    boto3_raw_data: "type_defs.WebCrawlerLimitsTypeDef" = dataclasses.field()

    rateLimit = field("rateLimit")
    maxPages = field("maxPages")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WebCrawlerLimitsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WebCrawlerLimitsTypeDef"]
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

    @cached_property
    def s3(self):  # pragma: no cover
        return S3Identifier.make_one(self.boto3_raw_data["s3"])

    payload = field("payload")

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
class AgentAliasHistoryEvent:
    boto3_raw_data: "type_defs.AgentAliasHistoryEventTypeDef" = dataclasses.field()

    @cached_property
    def routingConfiguration(self):  # pragma: no cover
        return AgentAliasRoutingConfigurationListItem.make_many(
            self.boto3_raw_data["routingConfiguration"]
        )

    endDate = field("endDate")
    startDate = field("startDate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AgentAliasHistoryEventTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AgentAliasHistoryEventTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AgentAliasSummary:
    boto3_raw_data: "type_defs.AgentAliasSummaryTypeDef" = dataclasses.field()

    agentAliasId = field("agentAliasId")
    agentAliasName = field("agentAliasName")
    agentAliasStatus = field("agentAliasStatus")
    createdAt = field("createdAt")
    updatedAt = field("updatedAt")
    description = field("description")

    @cached_property
    def routingConfiguration(self):  # pragma: no cover
        return AgentAliasRoutingConfigurationListItem.make_many(
            self.boto3_raw_data["routingConfiguration"]
        )

    aliasInvocationState = field("aliasInvocationState")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AgentAliasSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AgentAliasSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAgentAliasRequest:
    boto3_raw_data: "type_defs.CreateAgentAliasRequestTypeDef" = dataclasses.field()

    agentId = field("agentId")
    agentAliasName = field("agentAliasName")
    clientToken = field("clientToken")
    description = field("description")

    @cached_property
    def routingConfiguration(self):  # pragma: no cover
        return AgentAliasRoutingConfigurationListItem.make_many(
            self.boto3_raw_data["routingConfiguration"]
        )

    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAgentAliasRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAgentAliasRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAgentAliasRequest:
    boto3_raw_data: "type_defs.UpdateAgentAliasRequestTypeDef" = dataclasses.field()

    agentId = field("agentId")
    agentAliasId = field("agentAliasId")
    agentAliasName = field("agentAliasName")
    description = field("description")

    @cached_property
    def routingConfiguration(self):  # pragma: no cover
        return AgentAliasRoutingConfigurationListItem.make_many(
            self.boto3_raw_data["routingConfiguration"]
        )

    aliasInvocationState = field("aliasInvocationState")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAgentAliasRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAgentAliasRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AgentCollaboratorSummary:
    boto3_raw_data: "type_defs.AgentCollaboratorSummaryTypeDef" = dataclasses.field()

    agentId = field("agentId")
    agentVersion = field("agentVersion")
    collaboratorId = field("collaboratorId")

    @cached_property
    def agentDescriptor(self):  # pragma: no cover
        return AgentDescriptor.make_one(self.boto3_raw_data["agentDescriptor"])

    collaborationInstruction = field("collaborationInstruction")
    relayConversationHistory = field("relayConversationHistory")
    collaboratorName = field("collaboratorName")
    createdAt = field("createdAt")
    lastUpdatedAt = field("lastUpdatedAt")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AgentCollaboratorSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AgentCollaboratorSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AgentCollaborator:
    boto3_raw_data: "type_defs.AgentCollaboratorTypeDef" = dataclasses.field()

    agentId = field("agentId")
    agentVersion = field("agentVersion")

    @cached_property
    def agentDescriptor(self):  # pragma: no cover
        return AgentDescriptor.make_one(self.boto3_raw_data["agentDescriptor"])

    collaboratorId = field("collaboratorId")
    collaborationInstruction = field("collaborationInstruction")
    collaboratorName = field("collaboratorName")
    createdAt = field("createdAt")
    lastUpdatedAt = field("lastUpdatedAt")
    relayConversationHistory = field("relayConversationHistory")
    clientToken = field("clientToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AgentCollaboratorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AgentCollaboratorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateAgentCollaboratorRequest:
    boto3_raw_data: "type_defs.AssociateAgentCollaboratorRequestTypeDef" = (
        dataclasses.field()
    )

    agentId = field("agentId")
    agentVersion = field("agentVersion")

    @cached_property
    def agentDescriptor(self):  # pragma: no cover
        return AgentDescriptor.make_one(self.boto3_raw_data["agentDescriptor"])

    collaboratorName = field("collaboratorName")
    collaborationInstruction = field("collaborationInstruction")
    relayConversationHistory = field("relayConversationHistory")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateAgentCollaboratorRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateAgentCollaboratorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAgentCollaboratorRequest:
    boto3_raw_data: "type_defs.UpdateAgentCollaboratorRequestTypeDef" = (
        dataclasses.field()
    )

    agentId = field("agentId")
    agentVersion = field("agentVersion")
    collaboratorId = field("collaboratorId")

    @cached_property
    def agentDescriptor(self):  # pragma: no cover
        return AgentDescriptor.make_one(self.boto3_raw_data["agentDescriptor"])

    collaboratorName = field("collaboratorName")
    collaborationInstruction = field("collaborationInstruction")
    relayConversationHistory = field("relayConversationHistory")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateAgentCollaboratorRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAgentCollaboratorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AgentSummary:
    boto3_raw_data: "type_defs.AgentSummaryTypeDef" = dataclasses.field()

    agentId = field("agentId")
    agentName = field("agentName")
    agentStatus = field("agentStatus")
    updatedAt = field("updatedAt")
    description = field("description")
    latestAgentVersion = field("latestAgentVersion")

    @cached_property
    def guardrailConfiguration(self):  # pragma: no cover
        return GuardrailConfiguration.make_one(
            self.boto3_raw_data["guardrailConfiguration"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AgentSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AgentSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AgentVersionSummary:
    boto3_raw_data: "type_defs.AgentVersionSummaryTypeDef" = dataclasses.field()

    agentName = field("agentName")
    agentStatus = field("agentStatus")
    agentVersion = field("agentVersion")
    createdAt = field("createdAt")
    updatedAt = field("updatedAt")
    description = field("description")

    @cached_property
    def guardrailConfiguration(self):  # pragma: no cover
        return GuardrailConfiguration.make_one(
            self.boto3_raw_data["guardrailConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AgentVersionSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AgentVersionSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateAgentKnowledgeBaseResponse:
    boto3_raw_data: "type_defs.AssociateAgentKnowledgeBaseResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def agentKnowledgeBase(self):  # pragma: no cover
        return AgentKnowledgeBase.make_one(self.boto3_raw_data["agentKnowledgeBase"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateAgentKnowledgeBaseResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateAgentKnowledgeBaseResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAgentAliasResponse:
    boto3_raw_data: "type_defs.DeleteAgentAliasResponseTypeDef" = dataclasses.field()

    agentId = field("agentId")
    agentAliasId = field("agentAliasId")
    agentAliasStatus = field("agentAliasStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAgentAliasResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAgentAliasResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAgentResponse:
    boto3_raw_data: "type_defs.DeleteAgentResponseTypeDef" = dataclasses.field()

    agentId = field("agentId")
    agentStatus = field("agentStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAgentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAgentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAgentVersionResponse:
    boto3_raw_data: "type_defs.DeleteAgentVersionResponseTypeDef" = dataclasses.field()

    agentId = field("agentId")
    agentVersion = field("agentVersion")
    agentStatus = field("agentStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAgentVersionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAgentVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDataSourceResponse:
    boto3_raw_data: "type_defs.DeleteDataSourceResponseTypeDef" = dataclasses.field()

    knowledgeBaseId = field("knowledgeBaseId")
    dataSourceId = field("dataSourceId")
    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDataSourceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDataSourceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteFlowAliasResponse:
    boto3_raw_data: "type_defs.DeleteFlowAliasResponseTypeDef" = dataclasses.field()

    flowId = field("flowId")
    id = field("id")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteFlowAliasResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteFlowAliasResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteFlowResponse:
    boto3_raw_data: "type_defs.DeleteFlowResponseTypeDef" = dataclasses.field()

    id = field("id")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteFlowResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteFlowResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteFlowVersionResponse:
    boto3_raw_data: "type_defs.DeleteFlowVersionResponseTypeDef" = dataclasses.field()

    id = field("id")
    version = field("version")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteFlowVersionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteFlowVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteKnowledgeBaseResponse:
    boto3_raw_data: "type_defs.DeleteKnowledgeBaseResponseTypeDef" = dataclasses.field()

    knowledgeBaseId = field("knowledgeBaseId")
    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteKnowledgeBaseResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteKnowledgeBaseResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePromptResponse:
    boto3_raw_data: "type_defs.DeletePromptResponseTypeDef" = dataclasses.field()

    id = field("id")
    version = field("version")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeletePromptResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePromptResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAgentKnowledgeBaseResponse:
    boto3_raw_data: "type_defs.GetAgentKnowledgeBaseResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def agentKnowledgeBase(self):  # pragma: no cover
        return AgentKnowledgeBase.make_one(self.boto3_raw_data["agentKnowledgeBase"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetAgentKnowledgeBaseResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAgentKnowledgeBaseResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAgentActionGroupsResponse:
    boto3_raw_data: "type_defs.ListAgentActionGroupsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def actionGroupSummaries(self):  # pragma: no cover
        return ActionGroupSummary.make_many(self.boto3_raw_data["actionGroupSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAgentActionGroupsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAgentActionGroupsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAgentKnowledgeBasesResponse:
    boto3_raw_data: "type_defs.ListAgentKnowledgeBasesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def agentKnowledgeBaseSummaries(self):  # pragma: no cover
        return AgentKnowledgeBaseSummary.make_many(
            self.boto3_raw_data["agentKnowledgeBaseSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAgentKnowledgeBasesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAgentKnowledgeBasesResponseTypeDef"]
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
class PrepareAgentResponse:
    boto3_raw_data: "type_defs.PrepareAgentResponseTypeDef" = dataclasses.field()

    agentId = field("agentId")
    agentStatus = field("agentStatus")
    agentVersion = field("agentVersion")
    preparedAt = field("preparedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PrepareAgentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PrepareAgentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PrepareFlowResponse:
    boto3_raw_data: "type_defs.PrepareFlowResponseTypeDef" = dataclasses.field()

    id = field("id")
    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PrepareFlowResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PrepareFlowResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAgentKnowledgeBaseResponse:
    boto3_raw_data: "type_defs.UpdateAgentKnowledgeBaseResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def agentKnowledgeBase(self):  # pragma: no cover
        return AgentKnowledgeBase.make_one(self.boto3_raw_data["agentKnowledgeBase"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateAgentKnowledgeBaseResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAgentKnowledgeBaseResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EmbeddingModelConfiguration:
    boto3_raw_data: "type_defs.EmbeddingModelConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def bedrockEmbeddingModelConfiguration(self):  # pragma: no cover
        return BedrockEmbeddingModelConfiguration.make_one(
            self.boto3_raw_data["bedrockEmbeddingModelConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EmbeddingModelConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EmbeddingModelConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BedrockFoundationModelConfiguration:
    boto3_raw_data: "type_defs.BedrockFoundationModelConfigurationTypeDef" = (
        dataclasses.field()
    )

    modelArn = field("modelArn")

    @cached_property
    def parsingPrompt(self):  # pragma: no cover
        return ParsingPrompt.make_one(self.boto3_raw_data["parsingPrompt"])

    parsingModality = field("parsingModality")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BedrockFoundationModelConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BedrockFoundationModelConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BedrockFoundationModelContextEnrichmentConfiguration:
    boto3_raw_data: (
        "type_defs.BedrockFoundationModelContextEnrichmentConfigurationTypeDef"
    ) = dataclasses.field()

    @cached_property
    def enrichmentStrategyConfiguration(self):  # pragma: no cover
        return EnrichmentStrategyConfiguration.make_one(
            self.boto3_raw_data["enrichmentStrategyConfiguration"]
        )

    modelArn = field("modelArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BedrockFoundationModelContextEnrichmentConfigurationTypeDef"
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
                "type_defs.BedrockFoundationModelContextEnrichmentConfigurationTypeDef"
            ]
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

    mimeType = field("mimeType")
    data = field("data")

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
class ContentBlock:
    boto3_raw_data: "type_defs.ContentBlockTypeDef" = dataclasses.field()

    text = field("text")

    @cached_property
    def cachePoint(self):  # pragma: no cover
        return CachePointBlock.make_one(self.boto3_raw_data["cachePoint"])

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
class SystemContentBlock:
    boto3_raw_data: "type_defs.SystemContentBlockTypeDef" = dataclasses.field()

    text = field("text")

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
class TextPromptTemplateConfigurationOutput:
    boto3_raw_data: "type_defs.TextPromptTemplateConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    text = field("text")

    @cached_property
    def cachePoint(self):  # pragma: no cover
        return CachePointBlock.make_one(self.boto3_raw_data["cachePoint"])

    @cached_property
    def inputVariables(self):  # pragma: no cover
        return PromptInputVariable.make_many(self.boto3_raw_data["inputVariables"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.TextPromptTemplateConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TextPromptTemplateConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TextPromptTemplateConfiguration:
    boto3_raw_data: "type_defs.TextPromptTemplateConfigurationTypeDef" = (
        dataclasses.field()
    )

    text = field("text")

    @cached_property
    def cachePoint(self):  # pragma: no cover
        return CachePointBlock.make_one(self.boto3_raw_data["cachePoint"])

    @cached_property
    def inputVariables(self):  # pragma: no cover
        return PromptInputVariable.make_many(self.boto3_raw_data["inputVariables"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.TextPromptTemplateConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TextPromptTemplateConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConditionFlowNodeConfigurationOutput:
    boto3_raw_data: "type_defs.ConditionFlowNodeConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def conditions(self):  # pragma: no cover
        return FlowCondition.make_many(self.boto3_raw_data["conditions"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ConditionFlowNodeConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConditionFlowNodeConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConditionFlowNodeConfiguration:
    boto3_raw_data: "type_defs.ConditionFlowNodeConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def conditions(self):  # pragma: no cover
        return FlowCondition.make_many(self.boto3_raw_data["conditions"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ConditionFlowNodeConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConditionFlowNodeConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoopControllerFlowNodeConfiguration:
    boto3_raw_data: "type_defs.LoopControllerFlowNodeConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def continueCondition(self):  # pragma: no cover
        return FlowCondition.make_one(self.boto3_raw_data["continueCondition"])

    maxIterations = field("maxIterations")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.LoopControllerFlowNodeConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LoopControllerFlowNodeConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFlowAliasRequest:
    boto3_raw_data: "type_defs.CreateFlowAliasRequestTypeDef" = dataclasses.field()

    name = field("name")

    @cached_property
    def routingConfiguration(self):  # pragma: no cover
        return FlowAliasRoutingConfigurationListItem.make_many(
            self.boto3_raw_data["routingConfiguration"]
        )

    flowIdentifier = field("flowIdentifier")
    description = field("description")

    @cached_property
    def concurrencyConfiguration(self):  # pragma: no cover
        return FlowAliasConcurrencyConfiguration.make_one(
            self.boto3_raw_data["concurrencyConfiguration"]
        )

    clientToken = field("clientToken")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateFlowAliasRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFlowAliasRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFlowAliasResponse:
    boto3_raw_data: "type_defs.CreateFlowAliasResponseTypeDef" = dataclasses.field()

    name = field("name")
    description = field("description")

    @cached_property
    def routingConfiguration(self):  # pragma: no cover
        return FlowAliasRoutingConfigurationListItem.make_many(
            self.boto3_raw_data["routingConfiguration"]
        )

    @cached_property
    def concurrencyConfiguration(self):  # pragma: no cover
        return FlowAliasConcurrencyConfiguration.make_one(
            self.boto3_raw_data["concurrencyConfiguration"]
        )

    flowId = field("flowId")
    id = field("id")
    arn = field("arn")
    createdAt = field("createdAt")
    updatedAt = field("updatedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateFlowAliasResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFlowAliasResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FlowAliasSummary:
    boto3_raw_data: "type_defs.FlowAliasSummaryTypeDef" = dataclasses.field()

    name = field("name")

    @cached_property
    def routingConfiguration(self):  # pragma: no cover
        return FlowAliasRoutingConfigurationListItem.make_many(
            self.boto3_raw_data["routingConfiguration"]
        )

    flowId = field("flowId")
    id = field("id")
    arn = field("arn")
    createdAt = field("createdAt")
    updatedAt = field("updatedAt")
    description = field("description")

    @cached_property
    def concurrencyConfiguration(self):  # pragma: no cover
        return FlowAliasConcurrencyConfiguration.make_one(
            self.boto3_raw_data["concurrencyConfiguration"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FlowAliasSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FlowAliasSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFlowAliasResponse:
    boto3_raw_data: "type_defs.GetFlowAliasResponseTypeDef" = dataclasses.field()

    name = field("name")
    description = field("description")

    @cached_property
    def routingConfiguration(self):  # pragma: no cover
        return FlowAliasRoutingConfigurationListItem.make_many(
            self.boto3_raw_data["routingConfiguration"]
        )

    @cached_property
    def concurrencyConfiguration(self):  # pragma: no cover
        return FlowAliasConcurrencyConfiguration.make_one(
            self.boto3_raw_data["concurrencyConfiguration"]
        )

    flowId = field("flowId")
    id = field("id")
    arn = field("arn")
    createdAt = field("createdAt")
    updatedAt = field("updatedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetFlowAliasResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFlowAliasResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFlowAliasRequest:
    boto3_raw_data: "type_defs.UpdateFlowAliasRequestTypeDef" = dataclasses.field()

    name = field("name")

    @cached_property
    def routingConfiguration(self):  # pragma: no cover
        return FlowAliasRoutingConfigurationListItem.make_many(
            self.boto3_raw_data["routingConfiguration"]
        )

    flowIdentifier = field("flowIdentifier")
    aliasIdentifier = field("aliasIdentifier")
    description = field("description")

    @cached_property
    def concurrencyConfiguration(self):  # pragma: no cover
        return FlowAliasConcurrencyConfiguration.make_one(
            self.boto3_raw_data["concurrencyConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateFlowAliasRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFlowAliasRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFlowAliasResponse:
    boto3_raw_data: "type_defs.UpdateFlowAliasResponseTypeDef" = dataclasses.field()

    name = field("name")
    description = field("description")

    @cached_property
    def routingConfiguration(self):  # pragma: no cover
        return FlowAliasRoutingConfigurationListItem.make_many(
            self.boto3_raw_data["routingConfiguration"]
        )

    @cached_property
    def concurrencyConfiguration(self):  # pragma: no cover
        return FlowAliasConcurrencyConfiguration.make_one(
            self.boto3_raw_data["concurrencyConfiguration"]
        )

    flowId = field("flowId")
    id = field("id")
    arn = field("arn")
    createdAt = field("createdAt")
    updatedAt = field("updatedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateFlowAliasResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFlowAliasResponseTypeDef"]
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
class ListDataSourcesResponse:
    boto3_raw_data: "type_defs.ListDataSourcesResponseTypeDef" = dataclasses.field()

    @cached_property
    def dataSourceSummaries(self):  # pragma: no cover
        return DataSourceSummary.make_many(self.boto3_raw_data["dataSourceSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDataSourcesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDataSourcesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentIdentifier:
    boto3_raw_data: "type_defs.DocumentIdentifierTypeDef" = dataclasses.field()

    dataSourceType = field("dataSourceType")

    @cached_property
    def s3(self):  # pragma: no cover
        return S3Location.make_one(self.boto3_raw_data["s3"])

    @cached_property
    def custom(self):  # pragma: no cover
        return CustomDocumentIdentifier.make_one(self.boto3_raw_data["custom"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DocumentIdentifierTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentIdentifierTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IntermediateStorage:
    boto3_raw_data: "type_defs.IntermediateStorageTypeDef" = dataclasses.field()

    @cached_property
    def s3Location(self):  # pragma: no cover
        return S3Location.make_one(self.boto3_raw_data["s3Location"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IntermediateStorageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IntermediateStorageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3Content:
    boto3_raw_data: "type_defs.S3ContentTypeDef" = dataclasses.field()

    @cached_property
    def s3Location(self):  # pragma: no cover
        return S3Location.make_one(self.boto3_raw_data["s3Location"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3ContentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3ContentTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SupplementalDataStorageLocation:
    boto3_raw_data: "type_defs.SupplementalDataStorageLocationTypeDef" = (
        dataclasses.field()
    )

    type = field("type")

    @cached_property
    def s3Location(self):  # pragma: no cover
        return S3Location.make_one(self.boto3_raw_data["s3Location"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SupplementalDataStorageLocationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SupplementalDataStorageLocationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RerankingMetadataSelectiveModeConfigurationOutput:
    boto3_raw_data: (
        "type_defs.RerankingMetadataSelectiveModeConfigurationOutputTypeDef"
    ) = dataclasses.field()

    @cached_property
    def fieldsToInclude(self):  # pragma: no cover
        return FieldForReranking.make_many(self.boto3_raw_data["fieldsToInclude"])

    @cached_property
    def fieldsToExclude(self):  # pragma: no cover
        return FieldForReranking.make_many(self.boto3_raw_data["fieldsToExclude"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RerankingMetadataSelectiveModeConfigurationOutputTypeDef"
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
                "type_defs.RerankingMetadataSelectiveModeConfigurationOutputTypeDef"
            ]
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
    def fieldsToInclude(self):  # pragma: no cover
        return FieldForReranking.make_many(self.boto3_raw_data["fieldsToInclude"])

    @cached_property
    def fieldsToExclude(self):  # pragma: no cover
        return FieldForReranking.make_many(self.boto3_raw_data["fieldsToExclude"])

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
class FlowConnectionConfiguration:
    boto3_raw_data: "type_defs.FlowConnectionConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def data(self):  # pragma: no cover
        return FlowDataConnectionConfiguration.make_one(self.boto3_raw_data["data"])

    @cached_property
    def conditional(self):  # pragma: no cover
        return FlowConditionalConnectionConfiguration.make_one(
            self.boto3_raw_data["conditional"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FlowConnectionConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FlowConnectionConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFlowsResponse:
    boto3_raw_data: "type_defs.ListFlowsResponseTypeDef" = dataclasses.field()

    @cached_property
    def flowSummaries(self):  # pragma: no cover
        return FlowSummary.make_many(self.boto3_raw_data["flowSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListFlowsResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFlowsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FlowValidationDetails:
    boto3_raw_data: "type_defs.FlowValidationDetailsTypeDef" = dataclasses.field()

    @cached_property
    def cyclicConnection(self):  # pragma: no cover
        return CyclicConnectionFlowValidationDetails.make_one(
            self.boto3_raw_data["cyclicConnection"]
        )

    @cached_property
    def duplicateConnections(self):  # pragma: no cover
        return DuplicateConnectionsFlowValidationDetails.make_one(
            self.boto3_raw_data["duplicateConnections"]
        )

    @cached_property
    def duplicateConditionExpression(self):  # pragma: no cover
        return DuplicateConditionExpressionFlowValidationDetails.make_one(
            self.boto3_raw_data["duplicateConditionExpression"]
        )

    @cached_property
    def unreachableNode(self):  # pragma: no cover
        return UnreachableNodeFlowValidationDetails.make_one(
            self.boto3_raw_data["unreachableNode"]
        )

    @cached_property
    def unknownConnectionSource(self):  # pragma: no cover
        return UnknownConnectionSourceFlowValidationDetails.make_one(
            self.boto3_raw_data["unknownConnectionSource"]
        )

    @cached_property
    def unknownConnectionSourceOutput(self):  # pragma: no cover
        return UnknownConnectionSourceOutputFlowValidationDetails.make_one(
            self.boto3_raw_data["unknownConnectionSourceOutput"]
        )

    @cached_property
    def unknownConnectionTarget(self):  # pragma: no cover
        return UnknownConnectionTargetFlowValidationDetails.make_one(
            self.boto3_raw_data["unknownConnectionTarget"]
        )

    @cached_property
    def unknownConnectionTargetInput(self):  # pragma: no cover
        return UnknownConnectionTargetInputFlowValidationDetails.make_one(
            self.boto3_raw_data["unknownConnectionTargetInput"]
        )

    @cached_property
    def unknownConnectionCondition(self):  # pragma: no cover
        return UnknownConnectionConditionFlowValidationDetails.make_one(
            self.boto3_raw_data["unknownConnectionCondition"]
        )

    @cached_property
    def malformedConditionExpression(self):  # pragma: no cover
        return MalformedConditionExpressionFlowValidationDetails.make_one(
            self.boto3_raw_data["malformedConditionExpression"]
        )

    @cached_property
    def malformedNodeInputExpression(self):  # pragma: no cover
        return MalformedNodeInputExpressionFlowValidationDetails.make_one(
            self.boto3_raw_data["malformedNodeInputExpression"]
        )

    @cached_property
    def mismatchedNodeInputType(self):  # pragma: no cover
        return MismatchedNodeInputTypeFlowValidationDetails.make_one(
            self.boto3_raw_data["mismatchedNodeInputType"]
        )

    @cached_property
    def mismatchedNodeOutputType(self):  # pragma: no cover
        return MismatchedNodeOutputTypeFlowValidationDetails.make_one(
            self.boto3_raw_data["mismatchedNodeOutputType"]
        )

    @cached_property
    def incompatibleConnectionDataType(self):  # pragma: no cover
        return IncompatibleConnectionDataTypeFlowValidationDetails.make_one(
            self.boto3_raw_data["incompatibleConnectionDataType"]
        )

    @cached_property
    def missingConnectionConfiguration(self):  # pragma: no cover
        return MissingConnectionConfigurationFlowValidationDetails.make_one(
            self.boto3_raw_data["missingConnectionConfiguration"]
        )

    @cached_property
    def missingDefaultCondition(self):  # pragma: no cover
        return MissingDefaultConditionFlowValidationDetails.make_one(
            self.boto3_raw_data["missingDefaultCondition"]
        )

    missingEndingNodes = field("missingEndingNodes")

    @cached_property
    def missingNodeConfiguration(self):  # pragma: no cover
        return MissingNodeConfigurationFlowValidationDetails.make_one(
            self.boto3_raw_data["missingNodeConfiguration"]
        )

    @cached_property
    def missingNodeInput(self):  # pragma: no cover
        return MissingNodeInputFlowValidationDetails.make_one(
            self.boto3_raw_data["missingNodeInput"]
        )

    @cached_property
    def missingNodeOutput(self):  # pragma: no cover
        return MissingNodeOutputFlowValidationDetails.make_one(
            self.boto3_raw_data["missingNodeOutput"]
        )

    missingStartingNodes = field("missingStartingNodes")

    @cached_property
    def multipleNodeInputConnections(self):  # pragma: no cover
        return MultipleNodeInputConnectionsFlowValidationDetails.make_one(
            self.boto3_raw_data["multipleNodeInputConnections"]
        )

    @cached_property
    def unfulfilledNodeInput(self):  # pragma: no cover
        return UnfulfilledNodeInputFlowValidationDetails.make_one(
            self.boto3_raw_data["unfulfilledNodeInput"]
        )

    @cached_property
    def unsatisfiedConnectionConditions(self):  # pragma: no cover
        return UnsatisfiedConnectionConditionsFlowValidationDetails.make_one(
            self.boto3_raw_data["unsatisfiedConnectionConditions"]
        )

    unspecified = field("unspecified")

    @cached_property
    def unknownNodeInput(self):  # pragma: no cover
        return UnknownNodeInputFlowValidationDetails.make_one(
            self.boto3_raw_data["unknownNodeInput"]
        )

    @cached_property
    def unknownNodeOutput(self):  # pragma: no cover
        return UnknownNodeOutputFlowValidationDetails.make_one(
            self.boto3_raw_data["unknownNodeOutput"]
        )

    @cached_property
    def missingLoopInputNode(self):  # pragma: no cover
        return MissingLoopInputNodeFlowValidationDetails.make_one(
            self.boto3_raw_data["missingLoopInputNode"]
        )

    @cached_property
    def missingLoopControllerNode(self):  # pragma: no cover
        return MissingLoopControllerNodeFlowValidationDetails.make_one(
            self.boto3_raw_data["missingLoopControllerNode"]
        )

    @cached_property
    def multipleLoopInputNodes(self):  # pragma: no cover
        return MultipleLoopInputNodesFlowValidationDetails.make_one(
            self.boto3_raw_data["multipleLoopInputNodes"]
        )

    @cached_property
    def multipleLoopControllerNodes(self):  # pragma: no cover
        return MultipleLoopControllerNodesFlowValidationDetails.make_one(
            self.boto3_raw_data["multipleLoopControllerNodes"]
        )

    @cached_property
    def loopIncompatibleNodeType(self):  # pragma: no cover
        return LoopIncompatibleNodeTypeFlowValidationDetails.make_one(
            self.boto3_raw_data["loopIncompatibleNodeType"]
        )

    @cached_property
    def invalidLoopBoundary(self):  # pragma: no cover
        return InvalidLoopBoundaryFlowValidationDetails.make_one(
            self.boto3_raw_data["invalidLoopBoundary"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FlowValidationDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FlowValidationDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFlowVersionsResponse:
    boto3_raw_data: "type_defs.ListFlowVersionsResponseTypeDef" = dataclasses.field()

    @cached_property
    def flowVersionSummaries(self):  # pragma: no cover
        return FlowVersionSummary.make_many(self.boto3_raw_data["flowVersionSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFlowVersionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFlowVersionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FunctionOutput:
    boto3_raw_data: "type_defs.FunctionOutputTypeDef" = dataclasses.field()

    name = field("name")
    description = field("description")
    parameters = field("parameters")
    requireConfirmation = field("requireConfirmation")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FunctionOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FunctionOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Function:
    boto3_raw_data: "type_defs.FunctionTypeDef" = dataclasses.field()

    name = field("name")
    description = field("description")
    parameters = field("parameters")
    requireConfirmation = field("requireConfirmation")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FunctionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FunctionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HierarchicalChunkingConfigurationOutput:
    boto3_raw_data: "type_defs.HierarchicalChunkingConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def levelConfigurations(self):  # pragma: no cover
        return HierarchicalChunkingLevelConfiguration.make_many(
            self.boto3_raw_data["levelConfigurations"]
        )

    overlapTokens = field("overlapTokens")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.HierarchicalChunkingConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HierarchicalChunkingConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HierarchicalChunkingConfiguration:
    boto3_raw_data: "type_defs.HierarchicalChunkingConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def levelConfigurations(self):  # pragma: no cover
        return HierarchicalChunkingLevelConfiguration.make_many(
            self.boto3_raw_data["levelConfigurations"]
        )

    overlapTokens = field("overlapTokens")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.HierarchicalChunkingConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HierarchicalChunkingConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PromptConfigurationOutput:
    boto3_raw_data: "type_defs.PromptConfigurationOutputTypeDef" = dataclasses.field()

    promptType = field("promptType")
    promptCreationMode = field("promptCreationMode")
    promptState = field("promptState")
    basePromptTemplate = field("basePromptTemplate")

    @cached_property
    def inferenceConfiguration(self):  # pragma: no cover
        return InferenceConfigurationOutput.make_one(
            self.boto3_raw_data["inferenceConfiguration"]
        )

    parserMode = field("parserMode")
    foundationModel = field("foundationModel")
    additionalModelRequestFields = field("additionalModelRequestFields")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PromptConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PromptConfigurationOutputTypeDef"]
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

    promptType = field("promptType")
    promptCreationMode = field("promptCreationMode")
    promptState = field("promptState")
    basePromptTemplate = field("basePromptTemplate")

    @cached_property
    def inferenceConfiguration(self):  # pragma: no cover
        return InferenceConfiguration.make_one(
            self.boto3_raw_data["inferenceConfiguration"]
        )

    parserMode = field("parserMode")
    foundationModel = field("foundationModel")
    additionalModelRequestFields = field("additionalModelRequestFields")

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
class ListIngestionJobsRequest:
    boto3_raw_data: "type_defs.ListIngestionJobsRequestTypeDef" = dataclasses.field()

    knowledgeBaseId = field("knowledgeBaseId")
    dataSourceId = field("dataSourceId")

    @cached_property
    def filters(self):  # pragma: no cover
        return IngestionJobFilter.make_many(self.boto3_raw_data["filters"])

    @cached_property
    def sortBy(self):  # pragma: no cover
        return IngestionJobSortBy.make_one(self.boto3_raw_data["sortBy"])

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListIngestionJobsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIngestionJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IngestionJobSummary:
    boto3_raw_data: "type_defs.IngestionJobSummaryTypeDef" = dataclasses.field()

    knowledgeBaseId = field("knowledgeBaseId")
    dataSourceId = field("dataSourceId")
    ingestionJobId = field("ingestionJobId")
    status = field("status")
    startedAt = field("startedAt")
    updatedAt = field("updatedAt")
    description = field("description")

    @cached_property
    def statistics(self):  # pragma: no cover
        return IngestionJobStatistics.make_one(self.boto3_raw_data["statistics"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IngestionJobSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IngestionJobSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IngestionJob:
    boto3_raw_data: "type_defs.IngestionJobTypeDef" = dataclasses.field()

    knowledgeBaseId = field("knowledgeBaseId")
    dataSourceId = field("dataSourceId")
    ingestionJobId = field("ingestionJobId")
    status = field("status")
    startedAt = field("startedAt")
    updatedAt = field("updatedAt")
    description = field("description")

    @cached_property
    def statistics(self):  # pragma: no cover
        return IngestionJobStatistics.make_one(self.boto3_raw_data["statistics"])

    failureReasons = field("failureReasons")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IngestionJobTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IngestionJobTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListKnowledgeBasesResponse:
    boto3_raw_data: "type_defs.ListKnowledgeBasesResponseTypeDef" = dataclasses.field()

    @cached_property
    def knowledgeBaseSummaries(self):  # pragma: no cover
        return KnowledgeBaseSummary.make_many(
            self.boto3_raw_data["knowledgeBaseSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListKnowledgeBasesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListKnowledgeBasesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAgentActionGroupsRequestPaginate:
    boto3_raw_data: "type_defs.ListAgentActionGroupsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    agentId = field("agentId")
    agentVersion = field("agentVersion")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAgentActionGroupsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAgentActionGroupsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAgentAliasesRequestPaginate:
    boto3_raw_data: "type_defs.ListAgentAliasesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    agentId = field("agentId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAgentAliasesRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAgentAliasesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAgentCollaboratorsRequestPaginate:
    boto3_raw_data: "type_defs.ListAgentCollaboratorsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    agentId = field("agentId")
    agentVersion = field("agentVersion")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAgentCollaboratorsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAgentCollaboratorsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAgentKnowledgeBasesRequestPaginate:
    boto3_raw_data: "type_defs.ListAgentKnowledgeBasesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    agentId = field("agentId")
    agentVersion = field("agentVersion")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAgentKnowledgeBasesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAgentKnowledgeBasesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAgentVersionsRequestPaginate:
    boto3_raw_data: "type_defs.ListAgentVersionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    agentId = field("agentId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAgentVersionsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAgentVersionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAgentsRequestPaginate:
    boto3_raw_data: "type_defs.ListAgentsRequestPaginateTypeDef" = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAgentsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAgentsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDataSourcesRequestPaginate:
    boto3_raw_data: "type_defs.ListDataSourcesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    knowledgeBaseId = field("knowledgeBaseId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListDataSourcesRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDataSourcesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFlowAliasesRequestPaginate:
    boto3_raw_data: "type_defs.ListFlowAliasesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    flowIdentifier = field("flowIdentifier")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListFlowAliasesRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFlowAliasesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFlowVersionsRequestPaginate:
    boto3_raw_data: "type_defs.ListFlowVersionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    flowIdentifier = field("flowIdentifier")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListFlowVersionsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFlowVersionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFlowsRequestPaginate:
    boto3_raw_data: "type_defs.ListFlowsRequestPaginateTypeDef" = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFlowsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFlowsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIngestionJobsRequestPaginate:
    boto3_raw_data: "type_defs.ListIngestionJobsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    knowledgeBaseId = field("knowledgeBaseId")
    dataSourceId = field("dataSourceId")

    @cached_property
    def filters(self):  # pragma: no cover
        return IngestionJobFilter.make_many(self.boto3_raw_data["filters"])

    @cached_property
    def sortBy(self):  # pragma: no cover
        return IngestionJobSortBy.make_one(self.boto3_raw_data["sortBy"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListIngestionJobsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIngestionJobsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListKnowledgeBaseDocumentsRequestPaginate:
    boto3_raw_data: "type_defs.ListKnowledgeBaseDocumentsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    knowledgeBaseId = field("knowledgeBaseId")
    dataSourceId = field("dataSourceId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListKnowledgeBaseDocumentsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListKnowledgeBaseDocumentsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListKnowledgeBasesRequestPaginate:
    boto3_raw_data: "type_defs.ListKnowledgeBasesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListKnowledgeBasesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListKnowledgeBasesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPromptsRequestPaginate:
    boto3_raw_data: "type_defs.ListPromptsRequestPaginateTypeDef" = dataclasses.field()

    promptIdentifier = field("promptIdentifier")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPromptsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPromptsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPromptsResponse:
    boto3_raw_data: "type_defs.ListPromptsResponseTypeDef" = dataclasses.field()

    @cached_property
    def promptSummaries(self):  # pragma: no cover
        return PromptSummary.make_many(self.boto3_raw_data["promptSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPromptsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPromptsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MemoryConfigurationOutput:
    boto3_raw_data: "type_defs.MemoryConfigurationOutputTypeDef" = dataclasses.field()

    enabledMemoryTypes = field("enabledMemoryTypes")
    storageDays = field("storageDays")

    @cached_property
    def sessionSummaryConfiguration(self):  # pragma: no cover
        return SessionSummaryConfiguration.make_one(
            self.boto3_raw_data["sessionSummaryConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MemoryConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MemoryConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MemoryConfiguration:
    boto3_raw_data: "type_defs.MemoryConfigurationTypeDef" = dataclasses.field()

    enabledMemoryTypes = field("enabledMemoryTypes")
    storageDays = field("storageDays")

    @cached_property
    def sessionSummaryConfiguration(self):  # pragma: no cover
        return SessionSummaryConfiguration.make_one(
            self.boto3_raw_data["sessionSummaryConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MemoryConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MemoryConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetadataAttribute:
    boto3_raw_data: "type_defs.MetadataAttributeTypeDef" = dataclasses.field()

    key = field("key")

    @cached_property
    def value(self):  # pragma: no cover
        return MetadataAttributeValue.make_one(self.boto3_raw_data["value"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MetadataAttributeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MetadataAttributeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MongoDbAtlasConfiguration:
    boto3_raw_data: "type_defs.MongoDbAtlasConfigurationTypeDef" = dataclasses.field()

    endpoint = field("endpoint")
    databaseName = field("databaseName")
    collectionName = field("collectionName")
    vectorIndexName = field("vectorIndexName")
    credentialsSecretArn = field("credentialsSecretArn")

    @cached_property
    def fieldMapping(self):  # pragma: no cover
        return MongoDbAtlasFieldMapping.make_one(self.boto3_raw_data["fieldMapping"])

    endpointServiceName = field("endpointServiceName")
    textIndexName = field("textIndexName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MongoDbAtlasConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MongoDbAtlasConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NeptuneAnalyticsConfiguration:
    boto3_raw_data: "type_defs.NeptuneAnalyticsConfigurationTypeDef" = (
        dataclasses.field()
    )

    graphArn = field("graphArn")

    @cached_property
    def fieldMapping(self):  # pragma: no cover
        return NeptuneAnalyticsFieldMapping.make_one(
            self.boto3_raw_data["fieldMapping"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.NeptuneAnalyticsConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NeptuneAnalyticsConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpenSearchManagedClusterConfiguration:
    boto3_raw_data: "type_defs.OpenSearchManagedClusterConfigurationTypeDef" = (
        dataclasses.field()
    )

    domainEndpoint = field("domainEndpoint")
    domainArn = field("domainArn")
    vectorIndexName = field("vectorIndexName")

    @cached_property
    def fieldMapping(self):  # pragma: no cover
        return OpenSearchManagedClusterFieldMapping.make_one(
            self.boto3_raw_data["fieldMapping"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.OpenSearchManagedClusterConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OpenSearchManagedClusterConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpenSearchServerlessConfiguration:
    boto3_raw_data: "type_defs.OpenSearchServerlessConfigurationTypeDef" = (
        dataclasses.field()
    )

    collectionArn = field("collectionArn")
    vectorIndexName = field("vectorIndexName")

    @cached_property
    def fieldMapping(self):  # pragma: no cover
        return OpenSearchServerlessFieldMapping.make_one(
            self.boto3_raw_data["fieldMapping"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.OpenSearchServerlessConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OpenSearchServerlessConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PatternObjectFilterConfigurationOutput:
    boto3_raw_data: "type_defs.PatternObjectFilterConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def filters(self):  # pragma: no cover
        return PatternObjectFilterOutput.make_many(self.boto3_raw_data["filters"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PatternObjectFilterConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PatternObjectFilterConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PatternObjectFilterConfiguration:
    boto3_raw_data: "type_defs.PatternObjectFilterConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def filters(self):  # pragma: no cover
        return PatternObjectFilter.make_many(self.boto3_raw_data["filters"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PatternObjectFilterConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PatternObjectFilterConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PineconeConfiguration:
    boto3_raw_data: "type_defs.PineconeConfigurationTypeDef" = dataclasses.field()

    connectionString = field("connectionString")
    credentialsSecretArn = field("credentialsSecretArn")

    @cached_property
    def fieldMapping(self):  # pragma: no cover
        return PineconeFieldMapping.make_one(self.boto3_raw_data["fieldMapping"])

    namespace = field("namespace")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PineconeConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PineconeConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PromptGenAiResource:
    boto3_raw_data: "type_defs.PromptGenAiResourceTypeDef" = dataclasses.field()

    @cached_property
    def agent(self):  # pragma: no cover
        return PromptAgentResource.make_one(self.boto3_raw_data["agent"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PromptGenAiResourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PromptGenAiResourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PromptInferenceConfigurationOutput:
    boto3_raw_data: "type_defs.PromptInferenceConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def text(self):  # pragma: no cover
        return PromptModelInferenceConfigurationOutput.make_one(
            self.boto3_raw_data["text"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PromptInferenceConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PromptInferenceConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryGenerationTableOutput:
    boto3_raw_data: "type_defs.QueryGenerationTableOutputTypeDef" = dataclasses.field()

    name = field("name")
    description = field("description")
    inclusion = field("inclusion")

    @cached_property
    def columns(self):  # pragma: no cover
        return QueryGenerationColumn.make_many(self.boto3_raw_data["columns"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.QueryGenerationTableOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QueryGenerationTableOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryGenerationTable:
    boto3_raw_data: "type_defs.QueryGenerationTableTypeDef" = dataclasses.field()

    name = field("name")
    description = field("description")
    inclusion = field("inclusion")

    @cached_property
    def columns(self):  # pragma: no cover
        return QueryGenerationColumn.make_many(self.boto3_raw_data["columns"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.QueryGenerationTableTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QueryGenerationTableTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RdsConfiguration:
    boto3_raw_data: "type_defs.RdsConfigurationTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")
    credentialsSecretArn = field("credentialsSecretArn")
    databaseName = field("databaseName")
    tableName = field("tableName")

    @cached_property
    def fieldMapping(self):  # pragma: no cover
        return RdsFieldMapping.make_one(self.boto3_raw_data["fieldMapping"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RdsConfigurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RdsConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RedisEnterpriseCloudConfiguration:
    boto3_raw_data: "type_defs.RedisEnterpriseCloudConfigurationTypeDef" = (
        dataclasses.field()
    )

    endpoint = field("endpoint")
    vectorIndexName = field("vectorIndexName")
    credentialsSecretArn = field("credentialsSecretArn")

    @cached_property
    def fieldMapping(self):  # pragma: no cover
        return RedisEnterpriseCloudFieldMapping.make_one(
            self.boto3_raw_data["fieldMapping"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RedisEnterpriseCloudConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RedisEnterpriseCloudConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RedshiftProvisionedConfiguration:
    boto3_raw_data: "type_defs.RedshiftProvisionedConfigurationTypeDef" = (
        dataclasses.field()
    )

    clusterIdentifier = field("clusterIdentifier")

    @cached_property
    def authConfiguration(self):  # pragma: no cover
        return RedshiftProvisionedAuthConfiguration.make_one(
            self.boto3_raw_data["authConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RedshiftProvisionedConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RedshiftProvisionedConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RedshiftQueryEngineStorageConfigurationOutput:
    boto3_raw_data: "type_defs.RedshiftQueryEngineStorageConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    type = field("type")

    @cached_property
    def awsDataCatalogConfiguration(self):  # pragma: no cover
        return RedshiftQueryEngineAwsDataCatalogStorageConfigurationOutput.make_one(
            self.boto3_raw_data["awsDataCatalogConfiguration"]
        )

    @cached_property
    def redshiftConfiguration(self):  # pragma: no cover
        return RedshiftQueryEngineRedshiftStorageConfiguration.make_one(
            self.boto3_raw_data["redshiftConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RedshiftQueryEngineStorageConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RedshiftQueryEngineStorageConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RedshiftQueryEngineStorageConfiguration:
    boto3_raw_data: "type_defs.RedshiftQueryEngineStorageConfigurationTypeDef" = (
        dataclasses.field()
    )

    type = field("type")

    @cached_property
    def awsDataCatalogConfiguration(self):  # pragma: no cover
        return RedshiftQueryEngineAwsDataCatalogStorageConfiguration.make_one(
            self.boto3_raw_data["awsDataCatalogConfiguration"]
        )

    @cached_property
    def redshiftConfiguration(self):  # pragma: no cover
        return RedshiftQueryEngineRedshiftStorageConfiguration.make_one(
            self.boto3_raw_data["redshiftConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RedshiftQueryEngineStorageConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RedshiftQueryEngineStorageConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RedshiftServerlessConfiguration:
    boto3_raw_data: "type_defs.RedshiftServerlessConfigurationTypeDef" = (
        dataclasses.field()
    )

    workgroupArn = field("workgroupArn")

    @cached_property
    def authConfiguration(self):  # pragma: no cover
        return RedshiftServerlessAuthConfiguration.make_one(
            self.boto3_raw_data["authConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RedshiftServerlessConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RedshiftServerlessConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RetrievalFlowNodeServiceConfiguration:
    boto3_raw_data: "type_defs.RetrievalFlowNodeServiceConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def s3(self):  # pragma: no cover
        return RetrievalFlowNodeS3Configuration.make_one(self.boto3_raw_data["s3"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RetrievalFlowNodeServiceConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RetrievalFlowNodeServiceConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UrlConfigurationOutput:
    boto3_raw_data: "type_defs.UrlConfigurationOutputTypeDef" = dataclasses.field()

    @cached_property
    def seedUrls(self):  # pragma: no cover
        return SeedUrl.make_many(self.boto3_raw_data["seedUrls"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UrlConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UrlConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UrlConfiguration:
    boto3_raw_data: "type_defs.UrlConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def seedUrls(self):  # pragma: no cover
        return SeedUrl.make_many(self.boto3_raw_data["seedUrls"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UrlConfigurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UrlConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ToolChoiceOutput:
    boto3_raw_data: "type_defs.ToolChoiceOutputTypeDef" = dataclasses.field()

    auto = field("auto")
    any = field("any")

    @cached_property
    def tool(self):  # pragma: no cover
        return SpecificToolChoice.make_one(self.boto3_raw_data["tool"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ToolChoiceOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ToolChoiceOutputTypeDef"]
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
class StorageFlowNodeServiceConfiguration:
    boto3_raw_data: "type_defs.StorageFlowNodeServiceConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def s3(self):  # pragma: no cover
        return StorageFlowNodeS3Configuration.make_one(self.boto3_raw_data["s3"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StorageFlowNodeServiceConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StorageFlowNodeServiceConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ToolSpecificationOutput:
    boto3_raw_data: "type_defs.ToolSpecificationOutputTypeDef" = dataclasses.field()

    name = field("name")

    @cached_property
    def inputSchema(self):  # pragma: no cover
        return ToolInputSchemaOutput.make_one(self.boto3_raw_data["inputSchema"])

    description = field("description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ToolSpecificationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ToolSpecificationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TransformationFunction:
    boto3_raw_data: "type_defs.TransformationFunctionTypeDef" = dataclasses.field()

    @cached_property
    def transformationLambdaConfiguration(self):  # pragma: no cover
        return TransformationLambdaConfiguration.make_one(
            self.boto3_raw_data["transformationLambdaConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TransformationFunctionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TransformationFunctionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WebCrawlerConfigurationOutput:
    boto3_raw_data: "type_defs.WebCrawlerConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def crawlerLimits(self):  # pragma: no cover
        return WebCrawlerLimits.make_one(self.boto3_raw_data["crawlerLimits"])

    inclusionFilters = field("inclusionFilters")
    exclusionFilters = field("exclusionFilters")
    scope = field("scope")
    userAgent = field("userAgent")
    userAgentHeader = field("userAgentHeader")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.WebCrawlerConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WebCrawlerConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WebCrawlerConfiguration:
    boto3_raw_data: "type_defs.WebCrawlerConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def crawlerLimits(self):  # pragma: no cover
        return WebCrawlerLimits.make_one(self.boto3_raw_data["crawlerLimits"])

    inclusionFilters = field("inclusionFilters")
    exclusionFilters = field("exclusionFilters")
    scope = field("scope")
    userAgent = field("userAgent")
    userAgentHeader = field("userAgentHeader")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WebCrawlerConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WebCrawlerConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AgentAlias:
    boto3_raw_data: "type_defs.AgentAliasTypeDef" = dataclasses.field()

    agentId = field("agentId")
    agentAliasId = field("agentAliasId")
    agentAliasName = field("agentAliasName")
    agentAliasArn = field("agentAliasArn")

    @cached_property
    def routingConfiguration(self):  # pragma: no cover
        return AgentAliasRoutingConfigurationListItem.make_many(
            self.boto3_raw_data["routingConfiguration"]
        )

    createdAt = field("createdAt")
    updatedAt = field("updatedAt")
    agentAliasStatus = field("agentAliasStatus")
    clientToken = field("clientToken")
    description = field("description")

    @cached_property
    def agentAliasHistoryEvents(self):  # pragma: no cover
        return AgentAliasHistoryEvent.make_many(
            self.boto3_raw_data["agentAliasHistoryEvents"]
        )

    failureReasons = field("failureReasons")
    aliasInvocationState = field("aliasInvocationState")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AgentAliasTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AgentAliasTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAgentAliasesResponse:
    boto3_raw_data: "type_defs.ListAgentAliasesResponseTypeDef" = dataclasses.field()

    @cached_property
    def agentAliasSummaries(self):  # pragma: no cover
        return AgentAliasSummary.make_many(self.boto3_raw_data["agentAliasSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAgentAliasesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAgentAliasesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAgentCollaboratorsResponse:
    boto3_raw_data: "type_defs.ListAgentCollaboratorsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def agentCollaboratorSummaries(self):  # pragma: no cover
        return AgentCollaboratorSummary.make_many(
            self.boto3_raw_data["agentCollaboratorSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAgentCollaboratorsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAgentCollaboratorsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateAgentCollaboratorResponse:
    boto3_raw_data: "type_defs.AssociateAgentCollaboratorResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def agentCollaborator(self):  # pragma: no cover
        return AgentCollaborator.make_one(self.boto3_raw_data["agentCollaborator"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateAgentCollaboratorResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateAgentCollaboratorResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAgentCollaboratorResponse:
    boto3_raw_data: "type_defs.GetAgentCollaboratorResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def agentCollaborator(self):  # pragma: no cover
        return AgentCollaborator.make_one(self.boto3_raw_data["agentCollaborator"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAgentCollaboratorResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAgentCollaboratorResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAgentCollaboratorResponse:
    boto3_raw_data: "type_defs.UpdateAgentCollaboratorResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def agentCollaborator(self):  # pragma: no cover
        return AgentCollaborator.make_one(self.boto3_raw_data["agentCollaborator"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateAgentCollaboratorResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAgentCollaboratorResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAgentsResponse:
    boto3_raw_data: "type_defs.ListAgentsResponseTypeDef" = dataclasses.field()

    @cached_property
    def agentSummaries(self):  # pragma: no cover
        return AgentSummary.make_many(self.boto3_raw_data["agentSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAgentsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAgentsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAgentVersionsResponse:
    boto3_raw_data: "type_defs.ListAgentVersionsResponseTypeDef" = dataclasses.field()

    @cached_property
    def agentVersionSummaries(self):  # pragma: no cover
        return AgentVersionSummary.make_many(
            self.boto3_raw_data["agentVersionSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAgentVersionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAgentVersionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ParsingConfiguration:
    boto3_raw_data: "type_defs.ParsingConfigurationTypeDef" = dataclasses.field()

    parsingStrategy = field("parsingStrategy")

    @cached_property
    def bedrockFoundationModelConfiguration(self):  # pragma: no cover
        return BedrockFoundationModelConfiguration.make_one(
            self.boto3_raw_data["bedrockFoundationModelConfiguration"]
        )

    @cached_property
    def bedrockDataAutomationConfiguration(self):  # pragma: no cover
        return BedrockDataAutomationConfiguration.make_one(
            self.boto3_raw_data["bedrockDataAutomationConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ParsingConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ParsingConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContextEnrichmentConfiguration:
    boto3_raw_data: "type_defs.ContextEnrichmentConfigurationTypeDef" = (
        dataclasses.field()
    )

    type = field("type")

    @cached_property
    def bedrockFoundationModelConfiguration(self):  # pragma: no cover
        return BedrockFoundationModelContextEnrichmentConfiguration.make_one(
            self.boto3_raw_data["bedrockFoundationModelConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ContextEnrichmentConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContextEnrichmentConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InlineContent:
    boto3_raw_data: "type_defs.InlineContentTypeDef" = dataclasses.field()

    type = field("type")

    @cached_property
    def byteContent(self):  # pragma: no cover
        return ByteContentDoc.make_one(self.boto3_raw_data["byteContent"])

    @cached_property
    def textContent(self):  # pragma: no cover
        return TextContentDoc.make_one(self.boto3_raw_data["textContent"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InlineContentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InlineContentTypeDef"]],
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
        return ContentBlock.make_many(self.boto3_raw_data["content"])

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
class Message:
    boto3_raw_data: "type_defs.MessageTypeDef" = dataclasses.field()

    role = field("role")

    @cached_property
    def content(self):  # pragma: no cover
        return ContentBlock.make_many(self.boto3_raw_data["content"])

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
class ListFlowAliasesResponse:
    boto3_raw_data: "type_defs.ListFlowAliasesResponseTypeDef" = dataclasses.field()

    @cached_property
    def flowAliasSummaries(self):  # pragma: no cover
        return FlowAliasSummary.make_many(self.boto3_raw_data["flowAliasSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFlowAliasesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFlowAliasesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteKnowledgeBaseDocumentsRequest:
    boto3_raw_data: "type_defs.DeleteKnowledgeBaseDocumentsRequestTypeDef" = (
        dataclasses.field()
    )

    knowledgeBaseId = field("knowledgeBaseId")
    dataSourceId = field("dataSourceId")

    @cached_property
    def documentIdentifiers(self):  # pragma: no cover
        return DocumentIdentifier.make_many(self.boto3_raw_data["documentIdentifiers"])

    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteKnowledgeBaseDocumentsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteKnowledgeBaseDocumentsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetKnowledgeBaseDocumentsRequest:
    boto3_raw_data: "type_defs.GetKnowledgeBaseDocumentsRequestTypeDef" = (
        dataclasses.field()
    )

    knowledgeBaseId = field("knowledgeBaseId")
    dataSourceId = field("dataSourceId")

    @cached_property
    def documentIdentifiers(self):  # pragma: no cover
        return DocumentIdentifier.make_many(self.boto3_raw_data["documentIdentifiers"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetKnowledgeBaseDocumentsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetKnowledgeBaseDocumentsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KnowledgeBaseDocumentDetail:
    boto3_raw_data: "type_defs.KnowledgeBaseDocumentDetailTypeDef" = dataclasses.field()

    knowledgeBaseId = field("knowledgeBaseId")
    dataSourceId = field("dataSourceId")
    status = field("status")

    @cached_property
    def identifier(self):  # pragma: no cover
        return DocumentIdentifier.make_one(self.boto3_raw_data["identifier"])

    statusReason = field("statusReason")
    updatedAt = field("updatedAt")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KnowledgeBaseDocumentDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KnowledgeBaseDocumentDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SupplementalDataStorageConfigurationOutput:
    boto3_raw_data: "type_defs.SupplementalDataStorageConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def storageLocations(self):  # pragma: no cover
        return SupplementalDataStorageLocation.make_many(
            self.boto3_raw_data["storageLocations"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SupplementalDataStorageConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SupplementalDataStorageConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SupplementalDataStorageConfiguration:
    boto3_raw_data: "type_defs.SupplementalDataStorageConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def storageLocations(self):  # pragma: no cover
        return SupplementalDataStorageLocation.make_many(
            self.boto3_raw_data["storageLocations"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SupplementalDataStorageConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SupplementalDataStorageConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetadataConfigurationForRerankingOutput:
    boto3_raw_data: "type_defs.MetadataConfigurationForRerankingOutputTypeDef" = (
        dataclasses.field()
    )

    selectionMode = field("selectionMode")

    @cached_property
    def selectiveModeConfiguration(self):  # pragma: no cover
        return RerankingMetadataSelectiveModeConfigurationOutput.make_one(
            self.boto3_raw_data["selectiveModeConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MetadataConfigurationForRerankingOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MetadataConfigurationForRerankingOutputTypeDef"]
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
class FlowConnection:
    boto3_raw_data: "type_defs.FlowConnectionTypeDef" = dataclasses.field()

    type = field("type")
    name = field("name")
    source = field("source")
    target = field("target")

    @cached_property
    def configuration(self):  # pragma: no cover
        return FlowConnectionConfiguration.make_one(
            self.boto3_raw_data["configuration"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FlowConnectionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FlowConnectionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FlowValidation:
    boto3_raw_data: "type_defs.FlowValidationTypeDef" = dataclasses.field()

    message = field("message")
    severity = field("severity")

    @cached_property
    def details(self):  # pragma: no cover
        return FlowValidationDetails.make_one(self.boto3_raw_data["details"])

    type = field("type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FlowValidationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FlowValidationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FunctionSchemaOutput:
    boto3_raw_data: "type_defs.FunctionSchemaOutputTypeDef" = dataclasses.field()

    @cached_property
    def functions(self):  # pragma: no cover
        return FunctionOutput.make_many(self.boto3_raw_data["functions"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FunctionSchemaOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FunctionSchemaOutputTypeDef"]
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
        return Function.make_many(self.boto3_raw_data["functions"])

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
class ChunkingConfigurationOutput:
    boto3_raw_data: "type_defs.ChunkingConfigurationOutputTypeDef" = dataclasses.field()

    chunkingStrategy = field("chunkingStrategy")

    @cached_property
    def fixedSizeChunkingConfiguration(self):  # pragma: no cover
        return FixedSizeChunkingConfiguration.make_one(
            self.boto3_raw_data["fixedSizeChunkingConfiguration"]
        )

    @cached_property
    def hierarchicalChunkingConfiguration(self):  # pragma: no cover
        return HierarchicalChunkingConfigurationOutput.make_one(
            self.boto3_raw_data["hierarchicalChunkingConfiguration"]
        )

    @cached_property
    def semanticChunkingConfiguration(self):  # pragma: no cover
        return SemanticChunkingConfiguration.make_one(
            self.boto3_raw_data["semanticChunkingConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ChunkingConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ChunkingConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChunkingConfiguration:
    boto3_raw_data: "type_defs.ChunkingConfigurationTypeDef" = dataclasses.field()

    chunkingStrategy = field("chunkingStrategy")

    @cached_property
    def fixedSizeChunkingConfiguration(self):  # pragma: no cover
        return FixedSizeChunkingConfiguration.make_one(
            self.boto3_raw_data["fixedSizeChunkingConfiguration"]
        )

    @cached_property
    def hierarchicalChunkingConfiguration(self):  # pragma: no cover
        return HierarchicalChunkingConfiguration.make_one(
            self.boto3_raw_data["hierarchicalChunkingConfiguration"]
        )

    @cached_property
    def semanticChunkingConfiguration(self):  # pragma: no cover
        return SemanticChunkingConfiguration.make_one(
            self.boto3_raw_data["semanticChunkingConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ChunkingConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ChunkingConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PromptOverrideConfigurationOutput:
    boto3_raw_data: "type_defs.PromptOverrideConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def promptConfigurations(self):  # pragma: no cover
        return PromptConfigurationOutput.make_many(
            self.boto3_raw_data["promptConfigurations"]
        )

    overrideLambda = field("overrideLambda")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PromptOverrideConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PromptOverrideConfigurationOutputTypeDef"]
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
class ListIngestionJobsResponse:
    boto3_raw_data: "type_defs.ListIngestionJobsResponseTypeDef" = dataclasses.field()

    @cached_property
    def ingestionJobSummaries(self):  # pragma: no cover
        return IngestionJobSummary.make_many(
            self.boto3_raw_data["ingestionJobSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListIngestionJobsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIngestionJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetIngestionJobResponse:
    boto3_raw_data: "type_defs.GetIngestionJobResponseTypeDef" = dataclasses.field()

    @cached_property
    def ingestionJob(self):  # pragma: no cover
        return IngestionJob.make_one(self.boto3_raw_data["ingestionJob"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetIngestionJobResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetIngestionJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartIngestionJobResponse:
    boto3_raw_data: "type_defs.StartIngestionJobResponseTypeDef" = dataclasses.field()

    @cached_property
    def ingestionJob(self):  # pragma: no cover
        return IngestionJob.make_one(self.boto3_raw_data["ingestionJob"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartIngestionJobResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartIngestionJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopIngestionJobResponse:
    boto3_raw_data: "type_defs.StopIngestionJobResponseTypeDef" = dataclasses.field()

    @cached_property
    def ingestionJob(self):  # pragma: no cover
        return IngestionJob.make_one(self.boto3_raw_data["ingestionJob"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopIngestionJobResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopIngestionJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentMetadata:
    boto3_raw_data: "type_defs.DocumentMetadataTypeDef" = dataclasses.field()

    type = field("type")

    @cached_property
    def inlineAttributes(self):  # pragma: no cover
        return MetadataAttribute.make_many(self.boto3_raw_data["inlineAttributes"])

    @cached_property
    def s3Location(self):  # pragma: no cover
        return CustomS3Location.make_one(self.boto3_raw_data["s3Location"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DocumentMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CrawlFilterConfigurationOutput:
    boto3_raw_data: "type_defs.CrawlFilterConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    type = field("type")

    @cached_property
    def patternObjectFilter(self):  # pragma: no cover
        return PatternObjectFilterConfigurationOutput.make_one(
            self.boto3_raw_data["patternObjectFilter"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CrawlFilterConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CrawlFilterConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CrawlFilterConfiguration:
    boto3_raw_data: "type_defs.CrawlFilterConfigurationTypeDef" = dataclasses.field()

    type = field("type")

    @cached_property
    def patternObjectFilter(self):  # pragma: no cover
        return PatternObjectFilterConfiguration.make_one(
            self.boto3_raw_data["patternObjectFilter"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CrawlFilterConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CrawlFilterConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KnowledgeBaseOrchestrationConfigurationOutput:
    boto3_raw_data: "type_defs.KnowledgeBaseOrchestrationConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def promptTemplate(self):  # pragma: no cover
        return KnowledgeBasePromptTemplate.make_one(
            self.boto3_raw_data["promptTemplate"]
        )

    @cached_property
    def inferenceConfig(self):  # pragma: no cover
        return PromptInferenceConfigurationOutput.make_one(
            self.boto3_raw_data["inferenceConfig"]
        )

    additionalModelRequestFields = field("additionalModelRequestFields")

    @cached_property
    def performanceConfig(self):  # pragma: no cover
        return PerformanceConfiguration.make_one(
            self.boto3_raw_data["performanceConfig"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.KnowledgeBaseOrchestrationConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KnowledgeBaseOrchestrationConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PromptInferenceConfiguration:
    boto3_raw_data: "type_defs.PromptInferenceConfigurationTypeDef" = (
        dataclasses.field()
    )

    text = field("text")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PromptInferenceConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PromptInferenceConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryGenerationContextOutput:
    boto3_raw_data: "type_defs.QueryGenerationContextOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def tables(self):  # pragma: no cover
        return QueryGenerationTableOutput.make_many(self.boto3_raw_data["tables"])

    @cached_property
    def curatedQueries(self):  # pragma: no cover
        return CuratedQuery.make_many(self.boto3_raw_data["curatedQueries"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.QueryGenerationContextOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QueryGenerationContextOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryGenerationContext:
    boto3_raw_data: "type_defs.QueryGenerationContextTypeDef" = dataclasses.field()

    @cached_property
    def tables(self):  # pragma: no cover
        return QueryGenerationTable.make_many(self.boto3_raw_data["tables"])

    @cached_property
    def curatedQueries(self):  # pragma: no cover
        return CuratedQuery.make_many(self.boto3_raw_data["curatedQueries"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.QueryGenerationContextTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QueryGenerationContextTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StorageConfiguration:
    boto3_raw_data: "type_defs.StorageConfigurationTypeDef" = dataclasses.field()

    type = field("type")

    @cached_property
    def opensearchServerlessConfiguration(self):  # pragma: no cover
        return OpenSearchServerlessConfiguration.make_one(
            self.boto3_raw_data["opensearchServerlessConfiguration"]
        )

    @cached_property
    def opensearchManagedClusterConfiguration(self):  # pragma: no cover
        return OpenSearchManagedClusterConfiguration.make_one(
            self.boto3_raw_data["opensearchManagedClusterConfiguration"]
        )

    @cached_property
    def pineconeConfiguration(self):  # pragma: no cover
        return PineconeConfiguration.make_one(
            self.boto3_raw_data["pineconeConfiguration"]
        )

    @cached_property
    def redisEnterpriseCloudConfiguration(self):  # pragma: no cover
        return RedisEnterpriseCloudConfiguration.make_one(
            self.boto3_raw_data["redisEnterpriseCloudConfiguration"]
        )

    @cached_property
    def rdsConfiguration(self):  # pragma: no cover
        return RdsConfiguration.make_one(self.boto3_raw_data["rdsConfiguration"])

    @cached_property
    def mongoDbAtlasConfiguration(self):  # pragma: no cover
        return MongoDbAtlasConfiguration.make_one(
            self.boto3_raw_data["mongoDbAtlasConfiguration"]
        )

    @cached_property
    def neptuneAnalyticsConfiguration(self):  # pragma: no cover
        return NeptuneAnalyticsConfiguration.make_one(
            self.boto3_raw_data["neptuneAnalyticsConfiguration"]
        )

    @cached_property
    def s3VectorsConfiguration(self):  # pragma: no cover
        return S3VectorsConfiguration.make_one(
            self.boto3_raw_data["s3VectorsConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StorageConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StorageConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RedshiftQueryEngineConfiguration:
    boto3_raw_data: "type_defs.RedshiftQueryEngineConfigurationTypeDef" = (
        dataclasses.field()
    )

    type = field("type")

    @cached_property
    def serverlessConfiguration(self):  # pragma: no cover
        return RedshiftServerlessConfiguration.make_one(
            self.boto3_raw_data["serverlessConfiguration"]
        )

    @cached_property
    def provisionedConfiguration(self):  # pragma: no cover
        return RedshiftProvisionedConfiguration.make_one(
            self.boto3_raw_data["provisionedConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RedshiftQueryEngineConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RedshiftQueryEngineConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RetrievalFlowNodeConfiguration:
    boto3_raw_data: "type_defs.RetrievalFlowNodeConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def serviceConfiguration(self):  # pragma: no cover
        return RetrievalFlowNodeServiceConfiguration.make_one(
            self.boto3_raw_data["serviceConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RetrievalFlowNodeConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RetrievalFlowNodeConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WebSourceConfigurationOutput:
    boto3_raw_data: "type_defs.WebSourceConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def urlConfiguration(self):  # pragma: no cover
        return UrlConfigurationOutput.make_one(self.boto3_raw_data["urlConfiguration"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WebSourceConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WebSourceConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WebSourceConfiguration:
    boto3_raw_data: "type_defs.WebSourceConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def urlConfiguration(self):  # pragma: no cover
        return UrlConfiguration.make_one(self.boto3_raw_data["urlConfiguration"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WebSourceConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WebSourceConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StorageFlowNodeConfiguration:
    boto3_raw_data: "type_defs.StorageFlowNodeConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def serviceConfiguration(self):  # pragma: no cover
        return StorageFlowNodeServiceConfiguration.make_one(
            self.boto3_raw_data["serviceConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StorageFlowNodeConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StorageFlowNodeConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ToolOutput:
    boto3_raw_data: "type_defs.ToolOutputTypeDef" = dataclasses.field()

    @cached_property
    def toolSpec(self):  # pragma: no cover
        return ToolSpecificationOutput.make_one(self.boto3_raw_data["toolSpec"])

    @cached_property
    def cachePoint(self):  # pragma: no cover
        return CachePointBlock.make_one(self.boto3_raw_data["cachePoint"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ToolOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ToolOutputTypeDef"]]
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
    inputSchema = field("inputSchema")
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
class Transformation:
    boto3_raw_data: "type_defs.TransformationTypeDef" = dataclasses.field()

    @cached_property
    def transformationFunction(self):  # pragma: no cover
        return TransformationFunction.make_one(
            self.boto3_raw_data["transformationFunction"]
        )

    stepToApply = field("stepToApply")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TransformationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TransformationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAgentAliasResponse:
    boto3_raw_data: "type_defs.CreateAgentAliasResponseTypeDef" = dataclasses.field()

    @cached_property
    def agentAlias(self):  # pragma: no cover
        return AgentAlias.make_one(self.boto3_raw_data["agentAlias"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAgentAliasResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAgentAliasResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAgentAliasResponse:
    boto3_raw_data: "type_defs.GetAgentAliasResponseTypeDef" = dataclasses.field()

    @cached_property
    def agentAlias(self):  # pragma: no cover
        return AgentAlias.make_one(self.boto3_raw_data["agentAlias"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAgentAliasResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAgentAliasResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAgentAliasResponse:
    boto3_raw_data: "type_defs.UpdateAgentAliasResponseTypeDef" = dataclasses.field()

    @cached_property
    def agentAlias(self):  # pragma: no cover
        return AgentAlias.make_one(self.boto3_raw_data["agentAlias"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAgentAliasResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAgentAliasResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomContent:
    boto3_raw_data: "type_defs.CustomContentTypeDef" = dataclasses.field()

    @cached_property
    def customDocumentIdentifier(self):  # pragma: no cover
        return CustomDocumentIdentifier.make_one(
            self.boto3_raw_data["customDocumentIdentifier"]
        )

    sourceType = field("sourceType")

    @cached_property
    def s3Location(self):  # pragma: no cover
        return CustomS3Location.make_one(self.boto3_raw_data["s3Location"])

    @cached_property
    def inlineContent(self):  # pragma: no cover
        return InlineContent.make_one(self.boto3_raw_data["inlineContent"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CustomContentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CustomContentTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteKnowledgeBaseDocumentsResponse:
    boto3_raw_data: "type_defs.DeleteKnowledgeBaseDocumentsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def documentDetails(self):  # pragma: no cover
        return KnowledgeBaseDocumentDetail.make_many(
            self.boto3_raw_data["documentDetails"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteKnowledgeBaseDocumentsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteKnowledgeBaseDocumentsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetKnowledgeBaseDocumentsResponse:
    boto3_raw_data: "type_defs.GetKnowledgeBaseDocumentsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def documentDetails(self):  # pragma: no cover
        return KnowledgeBaseDocumentDetail.make_many(
            self.boto3_raw_data["documentDetails"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetKnowledgeBaseDocumentsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetKnowledgeBaseDocumentsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IngestKnowledgeBaseDocumentsResponse:
    boto3_raw_data: "type_defs.IngestKnowledgeBaseDocumentsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def documentDetails(self):  # pragma: no cover
        return KnowledgeBaseDocumentDetail.make_many(
            self.boto3_raw_data["documentDetails"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.IngestKnowledgeBaseDocumentsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IngestKnowledgeBaseDocumentsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListKnowledgeBaseDocumentsResponse:
    boto3_raw_data: "type_defs.ListKnowledgeBaseDocumentsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def documentDetails(self):  # pragma: no cover
        return KnowledgeBaseDocumentDetail.make_many(
            self.boto3_raw_data["documentDetails"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListKnowledgeBaseDocumentsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListKnowledgeBaseDocumentsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VectorKnowledgeBaseConfigurationOutput:
    boto3_raw_data: "type_defs.VectorKnowledgeBaseConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    embeddingModelArn = field("embeddingModelArn")

    @cached_property
    def embeddingModelConfiguration(self):  # pragma: no cover
        return EmbeddingModelConfiguration.make_one(
            self.boto3_raw_data["embeddingModelConfiguration"]
        )

    @cached_property
    def supplementalDataStorageConfiguration(self):  # pragma: no cover
        return SupplementalDataStorageConfigurationOutput.make_one(
            self.boto3_raw_data["supplementalDataStorageConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.VectorKnowledgeBaseConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VectorKnowledgeBaseConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VectorKnowledgeBaseConfiguration:
    boto3_raw_data: "type_defs.VectorKnowledgeBaseConfigurationTypeDef" = (
        dataclasses.field()
    )

    embeddingModelArn = field("embeddingModelArn")

    @cached_property
    def embeddingModelConfiguration(self):  # pragma: no cover
        return EmbeddingModelConfiguration.make_one(
            self.boto3_raw_data["embeddingModelConfiguration"]
        )

    @cached_property
    def supplementalDataStorageConfiguration(self):  # pragma: no cover
        return SupplementalDataStorageConfiguration.make_one(
            self.boto3_raw_data["supplementalDataStorageConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.VectorKnowledgeBaseConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VectorKnowledgeBaseConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VectorSearchBedrockRerankingConfigurationOutput:
    boto3_raw_data: (
        "type_defs.VectorSearchBedrockRerankingConfigurationOutputTypeDef"
    ) = dataclasses.field()

    @cached_property
    def modelConfiguration(self):  # pragma: no cover
        return VectorSearchBedrockRerankingModelConfigurationOutput.make_one(
            self.boto3_raw_data["modelConfiguration"]
        )

    numberOfRerankedResults = field("numberOfRerankedResults")

    @cached_property
    def metadataConfiguration(self):  # pragma: no cover
        return MetadataConfigurationForRerankingOutput.make_one(
            self.boto3_raw_data["metadataConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.VectorSearchBedrockRerankingConfigurationOutputTypeDef"
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
                "type_defs.VectorSearchBedrockRerankingConfigurationOutputTypeDef"
            ]
        ],
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

    numberOfRerankedResults = field("numberOfRerankedResults")

    @cached_property
    def metadataConfiguration(self):  # pragma: no cover
        return MetadataConfigurationForReranking.make_one(
            self.boto3_raw_data["metadataConfiguration"]
        )

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
class ValidateFlowDefinitionResponse:
    boto3_raw_data: "type_defs.ValidateFlowDefinitionResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def validations(self):  # pragma: no cover
        return FlowValidation.make_many(self.boto3_raw_data["validations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ValidateFlowDefinitionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ValidateFlowDefinitionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AgentActionGroup:
    boto3_raw_data: "type_defs.AgentActionGroupTypeDef" = dataclasses.field()

    agentId = field("agentId")
    agentVersion = field("agentVersion")
    actionGroupId = field("actionGroupId")
    actionGroupName = field("actionGroupName")
    createdAt = field("createdAt")
    updatedAt = field("updatedAt")
    actionGroupState = field("actionGroupState")
    clientToken = field("clientToken")
    description = field("description")
    parentActionSignature = field("parentActionSignature")
    parentActionGroupSignatureParams = field("parentActionGroupSignatureParams")

    @cached_property
    def actionGroupExecutor(self):  # pragma: no cover
        return ActionGroupExecutor.make_one(self.boto3_raw_data["actionGroupExecutor"])

    @cached_property
    def apiSchema(self):  # pragma: no cover
        return APISchema.make_one(self.boto3_raw_data["apiSchema"])

    @cached_property
    def functionSchema(self):  # pragma: no cover
        return FunctionSchemaOutput.make_one(self.boto3_raw_data["functionSchema"])

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
class Agent:
    boto3_raw_data: "type_defs.AgentTypeDef" = dataclasses.field()

    agentId = field("agentId")
    agentName = field("agentName")
    agentArn = field("agentArn")
    agentVersion = field("agentVersion")
    agentStatus = field("agentStatus")
    idleSessionTTLInSeconds = field("idleSessionTTLInSeconds")
    agentResourceRoleArn = field("agentResourceRoleArn")
    createdAt = field("createdAt")
    updatedAt = field("updatedAt")
    clientToken = field("clientToken")
    instruction = field("instruction")
    foundationModel = field("foundationModel")
    description = field("description")
    orchestrationType = field("orchestrationType")

    @cached_property
    def customOrchestration(self):  # pragma: no cover
        return CustomOrchestration.make_one(self.boto3_raw_data["customOrchestration"])

    customerEncryptionKeyArn = field("customerEncryptionKeyArn")
    preparedAt = field("preparedAt")
    failureReasons = field("failureReasons")
    recommendedActions = field("recommendedActions")

    @cached_property
    def promptOverrideConfiguration(self):  # pragma: no cover
        return PromptOverrideConfigurationOutput.make_one(
            self.boto3_raw_data["promptOverrideConfiguration"]
        )

    @cached_property
    def guardrailConfiguration(self):  # pragma: no cover
        return GuardrailConfiguration.make_one(
            self.boto3_raw_data["guardrailConfiguration"]
        )

    @cached_property
    def memoryConfiguration(self):  # pragma: no cover
        return MemoryConfigurationOutput.make_one(
            self.boto3_raw_data["memoryConfiguration"]
        )

    agentCollaboration = field("agentCollaboration")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AgentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AgentTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AgentVersion:
    boto3_raw_data: "type_defs.AgentVersionTypeDef" = dataclasses.field()

    agentId = field("agentId")
    agentName = field("agentName")
    agentArn = field("agentArn")
    version = field("version")
    agentStatus = field("agentStatus")
    idleSessionTTLInSeconds = field("idleSessionTTLInSeconds")
    agentResourceRoleArn = field("agentResourceRoleArn")
    createdAt = field("createdAt")
    updatedAt = field("updatedAt")
    instruction = field("instruction")
    foundationModel = field("foundationModel")
    description = field("description")
    customerEncryptionKeyArn = field("customerEncryptionKeyArn")
    failureReasons = field("failureReasons")
    recommendedActions = field("recommendedActions")

    @cached_property
    def promptOverrideConfiguration(self):  # pragma: no cover
        return PromptOverrideConfigurationOutput.make_one(
            self.boto3_raw_data["promptOverrideConfiguration"]
        )

    @cached_property
    def guardrailConfiguration(self):  # pragma: no cover
        return GuardrailConfiguration.make_one(
            self.boto3_raw_data["guardrailConfiguration"]
        )

    @cached_property
    def memoryConfiguration(self):  # pragma: no cover
        return MemoryConfigurationOutput.make_one(
            self.boto3_raw_data["memoryConfiguration"]
        )

    agentCollaboration = field("agentCollaboration")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AgentVersionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AgentVersionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfluenceCrawlerConfigurationOutput:
    boto3_raw_data: "type_defs.ConfluenceCrawlerConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def filterConfiguration(self):  # pragma: no cover
        return CrawlFilterConfigurationOutput.make_one(
            self.boto3_raw_data["filterConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ConfluenceCrawlerConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfluenceCrawlerConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SalesforceCrawlerConfigurationOutput:
    boto3_raw_data: "type_defs.SalesforceCrawlerConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def filterConfiguration(self):  # pragma: no cover
        return CrawlFilterConfigurationOutput.make_one(
            self.boto3_raw_data["filterConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SalesforceCrawlerConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SalesforceCrawlerConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SharePointCrawlerConfigurationOutput:
    boto3_raw_data: "type_defs.SharePointCrawlerConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def filterConfiguration(self):  # pragma: no cover
        return CrawlFilterConfigurationOutput.make_one(
            self.boto3_raw_data["filterConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SharePointCrawlerConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SharePointCrawlerConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfluenceCrawlerConfiguration:
    boto3_raw_data: "type_defs.ConfluenceCrawlerConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def filterConfiguration(self):  # pragma: no cover
        return CrawlFilterConfiguration.make_one(
            self.boto3_raw_data["filterConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ConfluenceCrawlerConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfluenceCrawlerConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SalesforceCrawlerConfiguration:
    boto3_raw_data: "type_defs.SalesforceCrawlerConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def filterConfiguration(self):  # pragma: no cover
        return CrawlFilterConfiguration.make_one(
            self.boto3_raw_data["filterConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SalesforceCrawlerConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SalesforceCrawlerConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SharePointCrawlerConfiguration:
    boto3_raw_data: "type_defs.SharePointCrawlerConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def filterConfiguration(self):  # pragma: no cover
        return CrawlFilterConfiguration.make_one(
            self.boto3_raw_data["filterConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SharePointCrawlerConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SharePointCrawlerConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KnowledgeBaseOrchestrationConfiguration:
    boto3_raw_data: "type_defs.KnowledgeBaseOrchestrationConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def promptTemplate(self):  # pragma: no cover
        return KnowledgeBasePromptTemplate.make_one(
            self.boto3_raw_data["promptTemplate"]
        )

    @cached_property
    def inferenceConfig(self):  # pragma: no cover
        return PromptInferenceConfiguration.make_one(
            self.boto3_raw_data["inferenceConfig"]
        )

    additionalModelRequestFields = field("additionalModelRequestFields")

    @cached_property
    def performanceConfig(self):  # pragma: no cover
        return PerformanceConfiguration.make_one(
            self.boto3_raw_data["performanceConfig"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.KnowledgeBaseOrchestrationConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KnowledgeBaseOrchestrationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryGenerationConfigurationOutput:
    boto3_raw_data: "type_defs.QueryGenerationConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    executionTimeoutSeconds = field("executionTimeoutSeconds")

    @cached_property
    def generationContext(self):  # pragma: no cover
        return QueryGenerationContextOutput.make_one(
            self.boto3_raw_data["generationContext"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.QueryGenerationConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QueryGenerationConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryGenerationConfiguration:
    boto3_raw_data: "type_defs.QueryGenerationConfigurationTypeDef" = (
        dataclasses.field()
    )

    executionTimeoutSeconds = field("executionTimeoutSeconds")

    @cached_property
    def generationContext(self):  # pragma: no cover
        return QueryGenerationContext.make_one(self.boto3_raw_data["generationContext"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.QueryGenerationConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QueryGenerationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WebDataSourceConfigurationOutput:
    boto3_raw_data: "type_defs.WebDataSourceConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def sourceConfiguration(self):  # pragma: no cover
        return WebSourceConfigurationOutput.make_one(
            self.boto3_raw_data["sourceConfiguration"]
        )

    @cached_property
    def crawlerConfiguration(self):  # pragma: no cover
        return WebCrawlerConfigurationOutput.make_one(
            self.boto3_raw_data["crawlerConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.WebDataSourceConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WebDataSourceConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WebDataSourceConfiguration:
    boto3_raw_data: "type_defs.WebDataSourceConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def sourceConfiguration(self):  # pragma: no cover
        return WebSourceConfiguration.make_one(
            self.boto3_raw_data["sourceConfiguration"]
        )

    @cached_property
    def crawlerConfiguration(self):  # pragma: no cover
        return WebCrawlerConfiguration.make_one(
            self.boto3_raw_data["crawlerConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WebDataSourceConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WebDataSourceConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ToolConfigurationOutput:
    boto3_raw_data: "type_defs.ToolConfigurationOutputTypeDef" = dataclasses.field()

    @cached_property
    def tools(self):  # pragma: no cover
        return ToolOutput.make_many(self.boto3_raw_data["tools"])

    @cached_property
    def toolChoice(self):  # pragma: no cover
        return ToolChoiceOutput.make_one(self.boto3_raw_data["toolChoice"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ToolConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ToolConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomTransformationConfigurationOutput:
    boto3_raw_data: "type_defs.CustomTransformationConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def intermediateStorage(self):  # pragma: no cover
        return IntermediateStorage.make_one(self.boto3_raw_data["intermediateStorage"])

    @cached_property
    def transformations(self):  # pragma: no cover
        return Transformation.make_many(self.boto3_raw_data["transformations"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CustomTransformationConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomTransformationConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomTransformationConfiguration:
    boto3_raw_data: "type_defs.CustomTransformationConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def intermediateStorage(self):  # pragma: no cover
        return IntermediateStorage.make_one(self.boto3_raw_data["intermediateStorage"])

    @cached_property
    def transformations(self):  # pragma: no cover
        return Transformation.make_many(self.boto3_raw_data["transformations"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CustomTransformationConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomTransformationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentContent:
    boto3_raw_data: "type_defs.DocumentContentTypeDef" = dataclasses.field()

    dataSourceType = field("dataSourceType")

    @cached_property
    def custom(self):  # pragma: no cover
        return CustomContent.make_one(self.boto3_raw_data["custom"])

    @cached_property
    def s3(self):  # pragma: no cover
        return S3Content.make_one(self.boto3_raw_data["s3"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DocumentContentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DocumentContentTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VectorSearchRerankingConfigurationOutput:
    boto3_raw_data: "type_defs.VectorSearchRerankingConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    type = field("type")

    @cached_property
    def bedrockRerankingConfiguration(self):  # pragma: no cover
        return VectorSearchBedrockRerankingConfigurationOutput.make_one(
            self.boto3_raw_data["bedrockRerankingConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.VectorSearchRerankingConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VectorSearchRerankingConfigurationOutputTypeDef"]
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
class CreateAgentActionGroupResponse:
    boto3_raw_data: "type_defs.CreateAgentActionGroupResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def agentActionGroup(self):  # pragma: no cover
        return AgentActionGroup.make_one(self.boto3_raw_data["agentActionGroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateAgentActionGroupResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAgentActionGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAgentActionGroupResponse:
    boto3_raw_data: "type_defs.GetAgentActionGroupResponseTypeDef" = dataclasses.field()

    @cached_property
    def agentActionGroup(self):  # pragma: no cover
        return AgentActionGroup.make_one(self.boto3_raw_data["agentActionGroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAgentActionGroupResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAgentActionGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAgentActionGroupResponse:
    boto3_raw_data: "type_defs.UpdateAgentActionGroupResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def agentActionGroup(self):  # pragma: no cover
        return AgentActionGroup.make_one(self.boto3_raw_data["agentActionGroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateAgentActionGroupResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAgentActionGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAgentActionGroupRequest:
    boto3_raw_data: "type_defs.CreateAgentActionGroupRequestTypeDef" = (
        dataclasses.field()
    )

    agentId = field("agentId")
    agentVersion = field("agentVersion")
    actionGroupName = field("actionGroupName")
    clientToken = field("clientToken")
    description = field("description")
    parentActionGroupSignature = field("parentActionGroupSignature")
    parentActionGroupSignatureParams = field("parentActionGroupSignatureParams")

    @cached_property
    def actionGroupExecutor(self):  # pragma: no cover
        return ActionGroupExecutor.make_one(self.boto3_raw_data["actionGroupExecutor"])

    @cached_property
    def apiSchema(self):  # pragma: no cover
        return APISchema.make_one(self.boto3_raw_data["apiSchema"])

    actionGroupState = field("actionGroupState")
    functionSchema = field("functionSchema")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateAgentActionGroupRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAgentActionGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAgentActionGroupRequest:
    boto3_raw_data: "type_defs.UpdateAgentActionGroupRequestTypeDef" = (
        dataclasses.field()
    )

    agentId = field("agentId")
    agentVersion = field("agentVersion")
    actionGroupId = field("actionGroupId")
    actionGroupName = field("actionGroupName")
    description = field("description")
    parentActionGroupSignature = field("parentActionGroupSignature")
    parentActionGroupSignatureParams = field("parentActionGroupSignatureParams")

    @cached_property
    def actionGroupExecutor(self):  # pragma: no cover
        return ActionGroupExecutor.make_one(self.boto3_raw_data["actionGroupExecutor"])

    actionGroupState = field("actionGroupState")

    @cached_property
    def apiSchema(self):  # pragma: no cover
        return APISchema.make_one(self.boto3_raw_data["apiSchema"])

    functionSchema = field("functionSchema")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateAgentActionGroupRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAgentActionGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAgentResponse:
    boto3_raw_data: "type_defs.CreateAgentResponseTypeDef" = dataclasses.field()

    @cached_property
    def agent(self):  # pragma: no cover
        return Agent.make_one(self.boto3_raw_data["agent"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAgentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAgentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAgentResponse:
    boto3_raw_data: "type_defs.GetAgentResponseTypeDef" = dataclasses.field()

    @cached_property
    def agent(self):  # pragma: no cover
        return Agent.make_one(self.boto3_raw_data["agent"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetAgentResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAgentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAgentResponse:
    boto3_raw_data: "type_defs.UpdateAgentResponseTypeDef" = dataclasses.field()

    @cached_property
    def agent(self):  # pragma: no cover
        return Agent.make_one(self.boto3_raw_data["agent"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAgentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAgentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAgentVersionResponse:
    boto3_raw_data: "type_defs.GetAgentVersionResponseTypeDef" = dataclasses.field()

    @cached_property
    def agentVersion(self):  # pragma: no cover
        return AgentVersion.make_one(self.boto3_raw_data["agentVersion"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAgentVersionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAgentVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAgentRequest:
    boto3_raw_data: "type_defs.CreateAgentRequestTypeDef" = dataclasses.field()

    agentName = field("agentName")
    clientToken = field("clientToken")
    instruction = field("instruction")
    foundationModel = field("foundationModel")
    description = field("description")
    orchestrationType = field("orchestrationType")

    @cached_property
    def customOrchestration(self):  # pragma: no cover
        return CustomOrchestration.make_one(self.boto3_raw_data["customOrchestration"])

    idleSessionTTLInSeconds = field("idleSessionTTLInSeconds")
    agentResourceRoleArn = field("agentResourceRoleArn")
    customerEncryptionKeyArn = field("customerEncryptionKeyArn")
    tags = field("tags")
    promptOverrideConfiguration = field("promptOverrideConfiguration")

    @cached_property
    def guardrailConfiguration(self):  # pragma: no cover
        return GuardrailConfiguration.make_one(
            self.boto3_raw_data["guardrailConfiguration"]
        )

    memoryConfiguration = field("memoryConfiguration")
    agentCollaboration = field("agentCollaboration")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAgentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAgentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAgentRequest:
    boto3_raw_data: "type_defs.UpdateAgentRequestTypeDef" = dataclasses.field()

    agentId = field("agentId")
    agentName = field("agentName")
    foundationModel = field("foundationModel")
    agentResourceRoleArn = field("agentResourceRoleArn")
    instruction = field("instruction")
    description = field("description")
    orchestrationType = field("orchestrationType")

    @cached_property
    def customOrchestration(self):  # pragma: no cover
        return CustomOrchestration.make_one(self.boto3_raw_data["customOrchestration"])

    idleSessionTTLInSeconds = field("idleSessionTTLInSeconds")
    customerEncryptionKeyArn = field("customerEncryptionKeyArn")
    promptOverrideConfiguration = field("promptOverrideConfiguration")

    @cached_property
    def guardrailConfiguration(self):  # pragma: no cover
        return GuardrailConfiguration.make_one(
            self.boto3_raw_data["guardrailConfiguration"]
        )

    memoryConfiguration = field("memoryConfiguration")
    agentCollaboration = field("agentCollaboration")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAgentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAgentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfluenceDataSourceConfigurationOutput:
    boto3_raw_data: "type_defs.ConfluenceDataSourceConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def sourceConfiguration(self):  # pragma: no cover
        return ConfluenceSourceConfiguration.make_one(
            self.boto3_raw_data["sourceConfiguration"]
        )

    @cached_property
    def crawlerConfiguration(self):  # pragma: no cover
        return ConfluenceCrawlerConfigurationOutput.make_one(
            self.boto3_raw_data["crawlerConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ConfluenceDataSourceConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfluenceDataSourceConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SalesforceDataSourceConfigurationOutput:
    boto3_raw_data: "type_defs.SalesforceDataSourceConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def sourceConfiguration(self):  # pragma: no cover
        return SalesforceSourceConfiguration.make_one(
            self.boto3_raw_data["sourceConfiguration"]
        )

    @cached_property
    def crawlerConfiguration(self):  # pragma: no cover
        return SalesforceCrawlerConfigurationOutput.make_one(
            self.boto3_raw_data["crawlerConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SalesforceDataSourceConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SalesforceDataSourceConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SharePointDataSourceConfigurationOutput:
    boto3_raw_data: "type_defs.SharePointDataSourceConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def sourceConfiguration(self):  # pragma: no cover
        return SharePointSourceConfigurationOutput.make_one(
            self.boto3_raw_data["sourceConfiguration"]
        )

    @cached_property
    def crawlerConfiguration(self):  # pragma: no cover
        return SharePointCrawlerConfigurationOutput.make_one(
            self.boto3_raw_data["crawlerConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SharePointDataSourceConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SharePointDataSourceConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfluenceDataSourceConfiguration:
    boto3_raw_data: "type_defs.ConfluenceDataSourceConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def sourceConfiguration(self):  # pragma: no cover
        return ConfluenceSourceConfiguration.make_one(
            self.boto3_raw_data["sourceConfiguration"]
        )

    @cached_property
    def crawlerConfiguration(self):  # pragma: no cover
        return ConfluenceCrawlerConfiguration.make_one(
            self.boto3_raw_data["crawlerConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ConfluenceDataSourceConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfluenceDataSourceConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SalesforceDataSourceConfiguration:
    boto3_raw_data: "type_defs.SalesforceDataSourceConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def sourceConfiguration(self):  # pragma: no cover
        return SalesforceSourceConfiguration.make_one(
            self.boto3_raw_data["sourceConfiguration"]
        )

    @cached_property
    def crawlerConfiguration(self):  # pragma: no cover
        return SalesforceCrawlerConfiguration.make_one(
            self.boto3_raw_data["crawlerConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SalesforceDataSourceConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SalesforceDataSourceConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SharePointDataSourceConfiguration:
    boto3_raw_data: "type_defs.SharePointDataSourceConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def sourceConfiguration(self):  # pragma: no cover
        return SharePointSourceConfiguration.make_one(
            self.boto3_raw_data["sourceConfiguration"]
        )

    @cached_property
    def crawlerConfiguration(self):  # pragma: no cover
        return SharePointCrawlerConfiguration.make_one(
            self.boto3_raw_data["crawlerConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SharePointDataSourceConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SharePointDataSourceConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RedshiftConfigurationOutput:
    boto3_raw_data: "type_defs.RedshiftConfigurationOutputTypeDef" = dataclasses.field()

    @cached_property
    def storageConfigurations(self):  # pragma: no cover
        return RedshiftQueryEngineStorageConfigurationOutput.make_many(
            self.boto3_raw_data["storageConfigurations"]
        )

    @cached_property
    def queryEngineConfiguration(self):  # pragma: no cover
        return RedshiftQueryEngineConfiguration.make_one(
            self.boto3_raw_data["queryEngineConfiguration"]
        )

    @cached_property
    def queryGenerationConfiguration(self):  # pragma: no cover
        return QueryGenerationConfigurationOutput.make_one(
            self.boto3_raw_data["queryGenerationConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RedshiftConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RedshiftConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RedshiftConfiguration:
    boto3_raw_data: "type_defs.RedshiftConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def storageConfigurations(self):  # pragma: no cover
        return RedshiftQueryEngineStorageConfiguration.make_many(
            self.boto3_raw_data["storageConfigurations"]
        )

    @cached_property
    def queryEngineConfiguration(self):  # pragma: no cover
        return RedshiftQueryEngineConfiguration.make_one(
            self.boto3_raw_data["queryEngineConfiguration"]
        )

    @cached_property
    def queryGenerationConfiguration(self):  # pragma: no cover
        return QueryGenerationConfiguration.make_one(
            self.boto3_raw_data["queryGenerationConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RedshiftConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RedshiftConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChatPromptTemplateConfigurationOutput:
    boto3_raw_data: "type_defs.ChatPromptTemplateConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def messages(self):  # pragma: no cover
        return MessageOutput.make_many(self.boto3_raw_data["messages"])

    @cached_property
    def system(self):  # pragma: no cover
        return SystemContentBlock.make_many(self.boto3_raw_data["system"])

    @cached_property
    def inputVariables(self):  # pragma: no cover
        return PromptInputVariable.make_many(self.boto3_raw_data["inputVariables"])

    @cached_property
    def toolConfiguration(self):  # pragma: no cover
        return ToolConfigurationOutput.make_one(
            self.boto3_raw_data["toolConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ChatPromptTemplateConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ChatPromptTemplateConfigurationOutputTypeDef"]
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

    toolSpec = field("toolSpec")

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
class VectorIngestionConfigurationOutput:
    boto3_raw_data: "type_defs.VectorIngestionConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def chunkingConfiguration(self):  # pragma: no cover
        return ChunkingConfigurationOutput.make_one(
            self.boto3_raw_data["chunkingConfiguration"]
        )

    @cached_property
    def customTransformationConfiguration(self):  # pragma: no cover
        return CustomTransformationConfigurationOutput.make_one(
            self.boto3_raw_data["customTransformationConfiguration"]
        )

    @cached_property
    def parsingConfiguration(self):  # pragma: no cover
        return ParsingConfiguration.make_one(
            self.boto3_raw_data["parsingConfiguration"]
        )

    @cached_property
    def contextEnrichmentConfiguration(self):  # pragma: no cover
        return ContextEnrichmentConfiguration.make_one(
            self.boto3_raw_data["contextEnrichmentConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.VectorIngestionConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VectorIngestionConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VectorIngestionConfiguration:
    boto3_raw_data: "type_defs.VectorIngestionConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def chunkingConfiguration(self):  # pragma: no cover
        return ChunkingConfiguration.make_one(
            self.boto3_raw_data["chunkingConfiguration"]
        )

    @cached_property
    def customTransformationConfiguration(self):  # pragma: no cover
        return CustomTransformationConfiguration.make_one(
            self.boto3_raw_data["customTransformationConfiguration"]
        )

    @cached_property
    def parsingConfiguration(self):  # pragma: no cover
        return ParsingConfiguration.make_one(
            self.boto3_raw_data["parsingConfiguration"]
        )

    @cached_property
    def contextEnrichmentConfiguration(self):  # pragma: no cover
        return ContextEnrichmentConfiguration.make_one(
            self.boto3_raw_data["contextEnrichmentConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VectorIngestionConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VectorIngestionConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KnowledgeBaseDocument:
    boto3_raw_data: "type_defs.KnowledgeBaseDocumentTypeDef" = dataclasses.field()

    @cached_property
    def content(self):  # pragma: no cover
        return DocumentContent.make_one(self.boto3_raw_data["content"])

    @cached_property
    def metadata(self):  # pragma: no cover
        return DocumentMetadata.make_one(self.boto3_raw_data["metadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KnowledgeBaseDocumentTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KnowledgeBaseDocumentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KnowledgeBaseFlowNodeConfigurationOutput:
    boto3_raw_data: "type_defs.KnowledgeBaseFlowNodeConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    knowledgeBaseId = field("knowledgeBaseId")
    modelId = field("modelId")

    @cached_property
    def guardrailConfiguration(self):  # pragma: no cover
        return GuardrailConfiguration.make_one(
            self.boto3_raw_data["guardrailConfiguration"]
        )

    numberOfResults = field("numberOfResults")

    @cached_property
    def promptTemplate(self):  # pragma: no cover
        return KnowledgeBasePromptTemplate.make_one(
            self.boto3_raw_data["promptTemplate"]
        )

    @cached_property
    def inferenceConfiguration(self):  # pragma: no cover
        return PromptInferenceConfigurationOutput.make_one(
            self.boto3_raw_data["inferenceConfiguration"]
        )

    @cached_property
    def rerankingConfiguration(self):  # pragma: no cover
        return VectorSearchRerankingConfigurationOutput.make_one(
            self.boto3_raw_data["rerankingConfiguration"]
        )

    @cached_property
    def orchestrationConfiguration(self):  # pragma: no cover
        return KnowledgeBaseOrchestrationConfigurationOutput.make_one(
            self.boto3_raw_data["orchestrationConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.KnowledgeBaseFlowNodeConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KnowledgeBaseFlowNodeConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KnowledgeBaseFlowNodeConfiguration:
    boto3_raw_data: "type_defs.KnowledgeBaseFlowNodeConfigurationTypeDef" = (
        dataclasses.field()
    )

    knowledgeBaseId = field("knowledgeBaseId")
    modelId = field("modelId")

    @cached_property
    def guardrailConfiguration(self):  # pragma: no cover
        return GuardrailConfiguration.make_one(
            self.boto3_raw_data["guardrailConfiguration"]
        )

    numberOfResults = field("numberOfResults")

    @cached_property
    def promptTemplate(self):  # pragma: no cover
        return KnowledgeBasePromptTemplate.make_one(
            self.boto3_raw_data["promptTemplate"]
        )

    @cached_property
    def inferenceConfiguration(self):  # pragma: no cover
        return PromptInferenceConfiguration.make_one(
            self.boto3_raw_data["inferenceConfiguration"]
        )

    @cached_property
    def rerankingConfiguration(self):  # pragma: no cover
        return VectorSearchRerankingConfiguration.make_one(
            self.boto3_raw_data["rerankingConfiguration"]
        )

    @cached_property
    def orchestrationConfiguration(self):  # pragma: no cover
        return KnowledgeBaseOrchestrationConfiguration.make_one(
            self.boto3_raw_data["orchestrationConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.KnowledgeBaseFlowNodeConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KnowledgeBaseFlowNodeConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataSourceConfigurationOutput:
    boto3_raw_data: "type_defs.DataSourceConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    type = field("type")

    @cached_property
    def s3Configuration(self):  # pragma: no cover
        return S3DataSourceConfigurationOutput.make_one(
            self.boto3_raw_data["s3Configuration"]
        )

    @cached_property
    def webConfiguration(self):  # pragma: no cover
        return WebDataSourceConfigurationOutput.make_one(
            self.boto3_raw_data["webConfiguration"]
        )

    @cached_property
    def confluenceConfiguration(self):  # pragma: no cover
        return ConfluenceDataSourceConfigurationOutput.make_one(
            self.boto3_raw_data["confluenceConfiguration"]
        )

    @cached_property
    def salesforceConfiguration(self):  # pragma: no cover
        return SalesforceDataSourceConfigurationOutput.make_one(
            self.boto3_raw_data["salesforceConfiguration"]
        )

    @cached_property
    def sharePointConfiguration(self):  # pragma: no cover
        return SharePointDataSourceConfigurationOutput.make_one(
            self.boto3_raw_data["sharePointConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DataSourceConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataSourceConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataSourceConfiguration:
    boto3_raw_data: "type_defs.DataSourceConfigurationTypeDef" = dataclasses.field()

    type = field("type")

    @cached_property
    def s3Configuration(self):  # pragma: no cover
        return S3DataSourceConfiguration.make_one(
            self.boto3_raw_data["s3Configuration"]
        )

    @cached_property
    def webConfiguration(self):  # pragma: no cover
        return WebDataSourceConfiguration.make_one(
            self.boto3_raw_data["webConfiguration"]
        )

    @cached_property
    def confluenceConfiguration(self):  # pragma: no cover
        return ConfluenceDataSourceConfiguration.make_one(
            self.boto3_raw_data["confluenceConfiguration"]
        )

    @cached_property
    def salesforceConfiguration(self):  # pragma: no cover
        return SalesforceDataSourceConfiguration.make_one(
            self.boto3_raw_data["salesforceConfiguration"]
        )

    @cached_property
    def sharePointConfiguration(self):  # pragma: no cover
        return SharePointDataSourceConfiguration.make_one(
            self.boto3_raw_data["sharePointConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataSourceConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataSourceConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SqlKnowledgeBaseConfigurationOutput:
    boto3_raw_data: "type_defs.SqlKnowledgeBaseConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    type = field("type")

    @cached_property
    def redshiftConfiguration(self):  # pragma: no cover
        return RedshiftConfigurationOutput.make_one(
            self.boto3_raw_data["redshiftConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SqlKnowledgeBaseConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SqlKnowledgeBaseConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SqlKnowledgeBaseConfiguration:
    boto3_raw_data: "type_defs.SqlKnowledgeBaseConfigurationTypeDef" = (
        dataclasses.field()
    )

    type = field("type")

    @cached_property
    def redshiftConfiguration(self):  # pragma: no cover
        return RedshiftConfiguration.make_one(
            self.boto3_raw_data["redshiftConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SqlKnowledgeBaseConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SqlKnowledgeBaseConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PromptTemplateConfigurationOutput:
    boto3_raw_data: "type_defs.PromptTemplateConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def text(self):  # pragma: no cover
        return TextPromptTemplateConfigurationOutput.make_one(
            self.boto3_raw_data["text"]
        )

    @cached_property
    def chat(self):  # pragma: no cover
        return ChatPromptTemplateConfigurationOutput.make_one(
            self.boto3_raw_data["chat"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PromptTemplateConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PromptTemplateConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IngestKnowledgeBaseDocumentsRequest:
    boto3_raw_data: "type_defs.IngestKnowledgeBaseDocumentsRequestTypeDef" = (
        dataclasses.field()
    )

    knowledgeBaseId = field("knowledgeBaseId")
    dataSourceId = field("dataSourceId")

    @cached_property
    def documents(self):  # pragma: no cover
        return KnowledgeBaseDocument.make_many(self.boto3_raw_data["documents"])

    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.IngestKnowledgeBaseDocumentsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IngestKnowledgeBaseDocumentsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataSource:
    boto3_raw_data: "type_defs.DataSourceTypeDef" = dataclasses.field()

    knowledgeBaseId = field("knowledgeBaseId")
    dataSourceId = field("dataSourceId")
    name = field("name")
    status = field("status")

    @cached_property
    def dataSourceConfiguration(self):  # pragma: no cover
        return DataSourceConfigurationOutput.make_one(
            self.boto3_raw_data["dataSourceConfiguration"]
        )

    createdAt = field("createdAt")
    updatedAt = field("updatedAt")
    description = field("description")

    @cached_property
    def serverSideEncryptionConfiguration(self):  # pragma: no cover
        return ServerSideEncryptionConfiguration.make_one(
            self.boto3_raw_data["serverSideEncryptionConfiguration"]
        )

    @cached_property
    def vectorIngestionConfiguration(self):  # pragma: no cover
        return VectorIngestionConfigurationOutput.make_one(
            self.boto3_raw_data["vectorIngestionConfiguration"]
        )

    dataDeletionPolicy = field("dataDeletionPolicy")
    failureReasons = field("failureReasons")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DataSourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DataSourceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KnowledgeBaseConfigurationOutput:
    boto3_raw_data: "type_defs.KnowledgeBaseConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    type = field("type")

    @cached_property
    def vectorKnowledgeBaseConfiguration(self):  # pragma: no cover
        return VectorKnowledgeBaseConfigurationOutput.make_one(
            self.boto3_raw_data["vectorKnowledgeBaseConfiguration"]
        )

    @cached_property
    def kendraKnowledgeBaseConfiguration(self):  # pragma: no cover
        return KendraKnowledgeBaseConfiguration.make_one(
            self.boto3_raw_data["kendraKnowledgeBaseConfiguration"]
        )

    @cached_property
    def sqlKnowledgeBaseConfiguration(self):  # pragma: no cover
        return SqlKnowledgeBaseConfigurationOutput.make_one(
            self.boto3_raw_data["sqlKnowledgeBaseConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.KnowledgeBaseConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KnowledgeBaseConfigurationOutputTypeDef"]
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

    type = field("type")

    @cached_property
    def vectorKnowledgeBaseConfiguration(self):  # pragma: no cover
        return VectorKnowledgeBaseConfiguration.make_one(
            self.boto3_raw_data["vectorKnowledgeBaseConfiguration"]
        )

    @cached_property
    def kendraKnowledgeBaseConfiguration(self):  # pragma: no cover
        return KendraKnowledgeBaseConfiguration.make_one(
            self.boto3_raw_data["kendraKnowledgeBaseConfiguration"]
        )

    @cached_property
    def sqlKnowledgeBaseConfiguration(self):  # pragma: no cover
        return SqlKnowledgeBaseConfiguration.make_one(
            self.boto3_raw_data["sqlKnowledgeBaseConfiguration"]
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
class PromptFlowNodeInlineConfigurationOutput:
    boto3_raw_data: "type_defs.PromptFlowNodeInlineConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    templateType = field("templateType")

    @cached_property
    def templateConfiguration(self):  # pragma: no cover
        return PromptTemplateConfigurationOutput.make_one(
            self.boto3_raw_data["templateConfiguration"]
        )

    modelId = field("modelId")

    @cached_property
    def inferenceConfiguration(self):  # pragma: no cover
        return PromptInferenceConfigurationOutput.make_one(
            self.boto3_raw_data["inferenceConfiguration"]
        )

    additionalModelRequestFields = field("additionalModelRequestFields")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PromptFlowNodeInlineConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PromptFlowNodeInlineConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PromptVariantOutput:
    boto3_raw_data: "type_defs.PromptVariantOutputTypeDef" = dataclasses.field()

    name = field("name")
    templateType = field("templateType")

    @cached_property
    def templateConfiguration(self):  # pragma: no cover
        return PromptTemplateConfigurationOutput.make_one(
            self.boto3_raw_data["templateConfiguration"]
        )

    modelId = field("modelId")

    @cached_property
    def inferenceConfiguration(self):  # pragma: no cover
        return PromptInferenceConfigurationOutput.make_one(
            self.boto3_raw_data["inferenceConfiguration"]
        )

    @cached_property
    def metadata(self):  # pragma: no cover
        return PromptMetadataEntry.make_many(self.boto3_raw_data["metadata"])

    additionalModelRequestFields = field("additionalModelRequestFields")

    @cached_property
    def genAiResource(self):  # pragma: no cover
        return PromptGenAiResource.make_one(self.boto3_raw_data["genAiResource"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PromptVariantOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PromptVariantOutputTypeDef"]
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

    tools = field("tools")
    toolChoice = field("toolChoice")

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
class CreateDataSourceResponse:
    boto3_raw_data: "type_defs.CreateDataSourceResponseTypeDef" = dataclasses.field()

    @cached_property
    def dataSource(self):  # pragma: no cover
        return DataSource.make_one(self.boto3_raw_data["dataSource"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDataSourceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDataSourceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDataSourceResponse:
    boto3_raw_data: "type_defs.GetDataSourceResponseTypeDef" = dataclasses.field()

    @cached_property
    def dataSource(self):  # pragma: no cover
        return DataSource.make_one(self.boto3_raw_data["dataSource"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDataSourceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDataSourceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDataSourceResponse:
    boto3_raw_data: "type_defs.UpdateDataSourceResponseTypeDef" = dataclasses.field()

    @cached_property
    def dataSource(self):  # pragma: no cover
        return DataSource.make_one(self.boto3_raw_data["dataSource"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDataSourceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDataSourceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDataSourceRequest:
    boto3_raw_data: "type_defs.CreateDataSourceRequestTypeDef" = dataclasses.field()

    knowledgeBaseId = field("knowledgeBaseId")
    name = field("name")
    dataSourceConfiguration = field("dataSourceConfiguration")
    clientToken = field("clientToken")
    description = field("description")
    dataDeletionPolicy = field("dataDeletionPolicy")

    @cached_property
    def serverSideEncryptionConfiguration(self):  # pragma: no cover
        return ServerSideEncryptionConfiguration.make_one(
            self.boto3_raw_data["serverSideEncryptionConfiguration"]
        )

    vectorIngestionConfiguration = field("vectorIngestionConfiguration")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDataSourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDataSourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDataSourceRequest:
    boto3_raw_data: "type_defs.UpdateDataSourceRequestTypeDef" = dataclasses.field()

    knowledgeBaseId = field("knowledgeBaseId")
    dataSourceId = field("dataSourceId")
    name = field("name")
    dataSourceConfiguration = field("dataSourceConfiguration")
    description = field("description")
    dataDeletionPolicy = field("dataDeletionPolicy")

    @cached_property
    def serverSideEncryptionConfiguration(self):  # pragma: no cover
        return ServerSideEncryptionConfiguration.make_one(
            self.boto3_raw_data["serverSideEncryptionConfiguration"]
        )

    vectorIngestionConfiguration = field("vectorIngestionConfiguration")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDataSourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDataSourceRequestTypeDef"]
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

    knowledgeBaseId = field("knowledgeBaseId")
    name = field("name")
    knowledgeBaseArn = field("knowledgeBaseArn")
    roleArn = field("roleArn")

    @cached_property
    def knowledgeBaseConfiguration(self):  # pragma: no cover
        return KnowledgeBaseConfigurationOutput.make_one(
            self.boto3_raw_data["knowledgeBaseConfiguration"]
        )

    status = field("status")
    createdAt = field("createdAt")
    updatedAt = field("updatedAt")
    description = field("description")

    @cached_property
    def storageConfiguration(self):  # pragma: no cover
        return StorageConfiguration.make_one(
            self.boto3_raw_data["storageConfiguration"]
        )

    failureReasons = field("failureReasons")

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
class PromptFlowNodeSourceConfigurationOutput:
    boto3_raw_data: "type_defs.PromptFlowNodeSourceConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def resource(self):  # pragma: no cover
        return PromptFlowNodeResourceConfiguration.make_one(
            self.boto3_raw_data["resource"]
        )

    @cached_property
    def inline(self):  # pragma: no cover
        return PromptFlowNodeInlineConfigurationOutput.make_one(
            self.boto3_raw_data["inline"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PromptFlowNodeSourceConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PromptFlowNodeSourceConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePromptResponse:
    boto3_raw_data: "type_defs.CreatePromptResponseTypeDef" = dataclasses.field()

    name = field("name")
    description = field("description")
    customerEncryptionKeyArn = field("customerEncryptionKeyArn")
    defaultVariant = field("defaultVariant")

    @cached_property
    def variants(self):  # pragma: no cover
        return PromptVariantOutput.make_many(self.boto3_raw_data["variants"])

    id = field("id")
    arn = field("arn")
    version = field("version")
    createdAt = field("createdAt")
    updatedAt = field("updatedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePromptResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePromptResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePromptVersionResponse:
    boto3_raw_data: "type_defs.CreatePromptVersionResponseTypeDef" = dataclasses.field()

    name = field("name")
    description = field("description")
    customerEncryptionKeyArn = field("customerEncryptionKeyArn")
    defaultVariant = field("defaultVariant")

    @cached_property
    def variants(self):  # pragma: no cover
        return PromptVariantOutput.make_many(self.boto3_raw_data["variants"])

    id = field("id")
    arn = field("arn")
    version = field("version")
    createdAt = field("createdAt")
    updatedAt = field("updatedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePromptVersionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePromptVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPromptResponse:
    boto3_raw_data: "type_defs.GetPromptResponseTypeDef" = dataclasses.field()

    name = field("name")
    description = field("description")
    customerEncryptionKeyArn = field("customerEncryptionKeyArn")
    defaultVariant = field("defaultVariant")

    @cached_property
    def variants(self):  # pragma: no cover
        return PromptVariantOutput.make_many(self.boto3_raw_data["variants"])

    id = field("id")
    arn = field("arn")
    version = field("version")
    createdAt = field("createdAt")
    updatedAt = field("updatedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetPromptResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPromptResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePromptResponse:
    boto3_raw_data: "type_defs.UpdatePromptResponseTypeDef" = dataclasses.field()

    name = field("name")
    description = field("description")
    customerEncryptionKeyArn = field("customerEncryptionKeyArn")
    defaultVariant = field("defaultVariant")

    @cached_property
    def variants(self):  # pragma: no cover
        return PromptVariantOutput.make_many(self.boto3_raw_data["variants"])

    id = field("id")
    arn = field("arn")
    version = field("version")
    createdAt = field("createdAt")
    updatedAt = field("updatedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdatePromptResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePromptResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateKnowledgeBaseResponse:
    boto3_raw_data: "type_defs.CreateKnowledgeBaseResponseTypeDef" = dataclasses.field()

    @cached_property
    def knowledgeBase(self):  # pragma: no cover
        return KnowledgeBase.make_one(self.boto3_raw_data["knowledgeBase"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateKnowledgeBaseResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateKnowledgeBaseResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetKnowledgeBaseResponse:
    boto3_raw_data: "type_defs.GetKnowledgeBaseResponseTypeDef" = dataclasses.field()

    @cached_property
    def knowledgeBase(self):  # pragma: no cover
        return KnowledgeBase.make_one(self.boto3_raw_data["knowledgeBase"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetKnowledgeBaseResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetKnowledgeBaseResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateKnowledgeBaseResponse:
    boto3_raw_data: "type_defs.UpdateKnowledgeBaseResponseTypeDef" = dataclasses.field()

    @cached_property
    def knowledgeBase(self):  # pragma: no cover
        return KnowledgeBase.make_one(self.boto3_raw_data["knowledgeBase"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateKnowledgeBaseResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateKnowledgeBaseResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateKnowledgeBaseRequest:
    boto3_raw_data: "type_defs.CreateKnowledgeBaseRequestTypeDef" = dataclasses.field()

    name = field("name")
    roleArn = field("roleArn")
    knowledgeBaseConfiguration = field("knowledgeBaseConfiguration")
    clientToken = field("clientToken")
    description = field("description")

    @cached_property
    def storageConfiguration(self):  # pragma: no cover
        return StorageConfiguration.make_one(
            self.boto3_raw_data["storageConfiguration"]
        )

    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateKnowledgeBaseRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateKnowledgeBaseRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateKnowledgeBaseRequest:
    boto3_raw_data: "type_defs.UpdateKnowledgeBaseRequestTypeDef" = dataclasses.field()

    knowledgeBaseId = field("knowledgeBaseId")
    name = field("name")
    roleArn = field("roleArn")
    knowledgeBaseConfiguration = field("knowledgeBaseConfiguration")
    description = field("description")

    @cached_property
    def storageConfiguration(self):  # pragma: no cover
        return StorageConfiguration.make_one(
            self.boto3_raw_data["storageConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateKnowledgeBaseRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateKnowledgeBaseRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PromptFlowNodeConfigurationOutput:
    boto3_raw_data: "type_defs.PromptFlowNodeConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def sourceConfiguration(self):  # pragma: no cover
        return PromptFlowNodeSourceConfigurationOutput.make_one(
            self.boto3_raw_data["sourceConfiguration"]
        )

    @cached_property
    def guardrailConfiguration(self):  # pragma: no cover
        return GuardrailConfiguration.make_one(
            self.boto3_raw_data["guardrailConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PromptFlowNodeConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PromptFlowNodeConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChatPromptTemplateConfiguration:
    boto3_raw_data: "type_defs.ChatPromptTemplateConfigurationTypeDef" = (
        dataclasses.field()
    )

    messages = field("messages")

    @cached_property
    def system(self):  # pragma: no cover
        return SystemContentBlock.make_many(self.boto3_raw_data["system"])

    @cached_property
    def inputVariables(self):  # pragma: no cover
        return PromptInputVariable.make_many(self.boto3_raw_data["inputVariables"])

    toolConfiguration = field("toolConfiguration")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ChatPromptTemplateConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ChatPromptTemplateConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FlowNodeConfigurationOutput:
    boto3_raw_data: "type_defs.FlowNodeConfigurationOutputTypeDef" = dataclasses.field()

    input = field("input")
    output = field("output")

    @cached_property
    def knowledgeBase(self):  # pragma: no cover
        return KnowledgeBaseFlowNodeConfigurationOutput.make_one(
            self.boto3_raw_data["knowledgeBase"]
        )

    @cached_property
    def condition(self):  # pragma: no cover
        return ConditionFlowNodeConfigurationOutput.make_one(
            self.boto3_raw_data["condition"]
        )

    @cached_property
    def lex(self):  # pragma: no cover
        return LexFlowNodeConfiguration.make_one(self.boto3_raw_data["lex"])

    @cached_property
    def prompt(self):  # pragma: no cover
        return PromptFlowNodeConfigurationOutput.make_one(self.boto3_raw_data["prompt"])

    @cached_property
    def lambdaFunction(self):  # pragma: no cover
        return LambdaFunctionFlowNodeConfiguration.make_one(
            self.boto3_raw_data["lambdaFunction"]
        )

    @cached_property
    def storage(self):  # pragma: no cover
        return StorageFlowNodeConfiguration.make_one(self.boto3_raw_data["storage"])

    @cached_property
    def agent(self):  # pragma: no cover
        return AgentFlowNodeConfiguration.make_one(self.boto3_raw_data["agent"])

    @cached_property
    def retrieval(self):  # pragma: no cover
        return RetrievalFlowNodeConfiguration.make_one(self.boto3_raw_data["retrieval"])

    iterator = field("iterator")
    collector = field("collector")

    @cached_property
    def inlineCode(self):  # pragma: no cover
        return InlineCodeFlowNodeConfiguration.make_one(
            self.boto3_raw_data["inlineCode"]
        )

    @cached_property
    def loop(self):  # pragma: no cover
        return LoopFlowNodeConfigurationOutput.make_one(self.boto3_raw_data["loop"])

    loopInput = field("loopInput")

    @cached_property
    def loopController(self):  # pragma: no cover
        return LoopControllerFlowNodeConfiguration.make_one(
            self.boto3_raw_data["loopController"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FlowNodeConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FlowNodeConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FlowNodeExtra:
    boto3_raw_data: "type_defs.FlowNodeExtraTypeDef" = dataclasses.field()

    name = field("name")
    type = field("type")

    @cached_property
    def configuration(self):  # pragma: no cover
        return FlowNodeConfigurationOutput.make_one(
            self.boto3_raw_data["configuration"]
        )

    @cached_property
    def inputs(self):  # pragma: no cover
        return FlowNodeInput.make_many(self.boto3_raw_data["inputs"])

    @cached_property
    def outputs(self):  # pragma: no cover
        return FlowNodeOutput.make_many(self.boto3_raw_data["outputs"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FlowNodeExtraTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FlowNodeExtraTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PromptTemplateConfiguration:
    boto3_raw_data: "type_defs.PromptTemplateConfigurationTypeDef" = dataclasses.field()

    text = field("text")
    chat = field("chat")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PromptTemplateConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PromptTemplateConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FlowDefinitionOutput:
    boto3_raw_data: "type_defs.FlowDefinitionOutputTypeDef" = dataclasses.field()

    @cached_property
    def nodes(self):  # pragma: no cover
        return FlowNodeExtra.make_many(self.boto3_raw_data["nodes"])

    @cached_property
    def connections(self):  # pragma: no cover
        return FlowConnection.make_many(self.boto3_raw_data["connections"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FlowDefinitionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FlowDefinitionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PromptFlowNodeInlineConfiguration:
    boto3_raw_data: "type_defs.PromptFlowNodeInlineConfigurationTypeDef" = (
        dataclasses.field()
    )

    templateType = field("templateType")

    @cached_property
    def templateConfiguration(self):  # pragma: no cover
        return PromptTemplateConfiguration.make_one(
            self.boto3_raw_data["templateConfiguration"]
        )

    modelId = field("modelId")

    @cached_property
    def inferenceConfiguration(self):  # pragma: no cover
        return PromptInferenceConfiguration.make_one(
            self.boto3_raw_data["inferenceConfiguration"]
        )

    additionalModelRequestFields = field("additionalModelRequestFields")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PromptFlowNodeInlineConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PromptFlowNodeInlineConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFlowResponse:
    boto3_raw_data: "type_defs.CreateFlowResponseTypeDef" = dataclasses.field()

    name = field("name")
    description = field("description")
    executionRoleArn = field("executionRoleArn")
    customerEncryptionKeyArn = field("customerEncryptionKeyArn")
    id = field("id")
    arn = field("arn")
    status = field("status")
    createdAt = field("createdAt")
    updatedAt = field("updatedAt")
    version = field("version")

    @cached_property
    def definition(self):  # pragma: no cover
        return FlowDefinitionOutput.make_one(self.boto3_raw_data["definition"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateFlowResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFlowResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFlowVersionResponse:
    boto3_raw_data: "type_defs.CreateFlowVersionResponseTypeDef" = dataclasses.field()

    name = field("name")
    description = field("description")
    executionRoleArn = field("executionRoleArn")
    customerEncryptionKeyArn = field("customerEncryptionKeyArn")
    id = field("id")
    arn = field("arn")
    status = field("status")
    createdAt = field("createdAt")
    version = field("version")

    @cached_property
    def definition(self):  # pragma: no cover
        return FlowDefinitionOutput.make_one(self.boto3_raw_data["definition"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateFlowVersionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFlowVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFlowResponse:
    boto3_raw_data: "type_defs.GetFlowResponseTypeDef" = dataclasses.field()

    name = field("name")
    description = field("description")
    executionRoleArn = field("executionRoleArn")
    customerEncryptionKeyArn = field("customerEncryptionKeyArn")
    id = field("id")
    arn = field("arn")
    status = field("status")
    createdAt = field("createdAt")
    updatedAt = field("updatedAt")
    version = field("version")

    @cached_property
    def definition(self):  # pragma: no cover
        return FlowDefinitionOutput.make_one(self.boto3_raw_data["definition"])

    @cached_property
    def validations(self):  # pragma: no cover
        return FlowValidation.make_many(self.boto3_raw_data["validations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetFlowResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetFlowResponseTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFlowVersionResponse:
    boto3_raw_data: "type_defs.GetFlowVersionResponseTypeDef" = dataclasses.field()

    name = field("name")
    description = field("description")
    executionRoleArn = field("executionRoleArn")
    customerEncryptionKeyArn = field("customerEncryptionKeyArn")
    id = field("id")
    arn = field("arn")
    status = field("status")
    createdAt = field("createdAt")
    version = field("version")

    @cached_property
    def definition(self):  # pragma: no cover
        return FlowDefinitionOutput.make_one(self.boto3_raw_data["definition"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetFlowVersionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFlowVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFlowResponse:
    boto3_raw_data: "type_defs.UpdateFlowResponseTypeDef" = dataclasses.field()

    name = field("name")
    description = field("description")
    executionRoleArn = field("executionRoleArn")
    customerEncryptionKeyArn = field("customerEncryptionKeyArn")
    id = field("id")
    arn = field("arn")
    status = field("status")
    createdAt = field("createdAt")
    updatedAt = field("updatedAt")
    version = field("version")

    @cached_property
    def definition(self):  # pragma: no cover
        return FlowDefinitionOutput.make_one(self.boto3_raw_data["definition"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateFlowResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFlowResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PromptFlowNodeSourceConfiguration:
    boto3_raw_data: "type_defs.PromptFlowNodeSourceConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def resource(self):  # pragma: no cover
        return PromptFlowNodeResourceConfiguration.make_one(
            self.boto3_raw_data["resource"]
        )

    @cached_property
    def inline(self):  # pragma: no cover
        return PromptFlowNodeInlineConfiguration.make_one(self.boto3_raw_data["inline"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PromptFlowNodeSourceConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PromptFlowNodeSourceConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PromptVariant:
    boto3_raw_data: "type_defs.PromptVariantTypeDef" = dataclasses.field()

    name = field("name")
    templateType = field("templateType")
    templateConfiguration = field("templateConfiguration")
    modelId = field("modelId")
    inferenceConfiguration = field("inferenceConfiguration")

    @cached_property
    def metadata(self):  # pragma: no cover
        return PromptMetadataEntry.make_many(self.boto3_raw_data["metadata"])

    additionalModelRequestFields = field("additionalModelRequestFields")

    @cached_property
    def genAiResource(self):  # pragma: no cover
        return PromptGenAiResource.make_one(self.boto3_raw_data["genAiResource"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PromptVariantTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PromptVariantTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PromptFlowNodeConfiguration:
    boto3_raw_data: "type_defs.PromptFlowNodeConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def sourceConfiguration(self):  # pragma: no cover
        return PromptFlowNodeSourceConfiguration.make_one(
            self.boto3_raw_data["sourceConfiguration"]
        )

    @cached_property
    def guardrailConfiguration(self):  # pragma: no cover
        return GuardrailConfiguration.make_one(
            self.boto3_raw_data["guardrailConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PromptFlowNodeConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PromptFlowNodeConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FlowNodeConfiguration:
    boto3_raw_data: "type_defs.FlowNodeConfigurationTypeDef" = dataclasses.field()

    input = field("input")
    output = field("output")

    @cached_property
    def knowledgeBase(self):  # pragma: no cover
        return KnowledgeBaseFlowNodeConfiguration.make_one(
            self.boto3_raw_data["knowledgeBase"]
        )

    @cached_property
    def condition(self):  # pragma: no cover
        return ConditionFlowNodeConfiguration.make_one(self.boto3_raw_data["condition"])

    @cached_property
    def lex(self):  # pragma: no cover
        return LexFlowNodeConfiguration.make_one(self.boto3_raw_data["lex"])

    @cached_property
    def prompt(self):  # pragma: no cover
        return PromptFlowNodeConfiguration.make_one(self.boto3_raw_data["prompt"])

    @cached_property
    def lambdaFunction(self):  # pragma: no cover
        return LambdaFunctionFlowNodeConfiguration.make_one(
            self.boto3_raw_data["lambdaFunction"]
        )

    @cached_property
    def storage(self):  # pragma: no cover
        return StorageFlowNodeConfiguration.make_one(self.boto3_raw_data["storage"])

    @cached_property
    def agent(self):  # pragma: no cover
        return AgentFlowNodeConfiguration.make_one(self.boto3_raw_data["agent"])

    @cached_property
    def retrieval(self):  # pragma: no cover
        return RetrievalFlowNodeConfiguration.make_one(self.boto3_raw_data["retrieval"])

    iterator = field("iterator")
    collector = field("collector")

    @cached_property
    def inlineCode(self):  # pragma: no cover
        return InlineCodeFlowNodeConfiguration.make_one(
            self.boto3_raw_data["inlineCode"]
        )

    @cached_property
    def loop(self):  # pragma: no cover
        return LoopFlowNodeConfiguration.make_one(self.boto3_raw_data["loop"])

    loopInput = field("loopInput")

    @cached_property
    def loopController(self):  # pragma: no cover
        return LoopControllerFlowNodeConfiguration.make_one(
            self.boto3_raw_data["loopController"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FlowNodeConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FlowNodeConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePromptRequest:
    boto3_raw_data: "type_defs.CreatePromptRequestTypeDef" = dataclasses.field()

    name = field("name")
    description = field("description")
    customerEncryptionKeyArn = field("customerEncryptionKeyArn")
    defaultVariant = field("defaultVariant")
    variants = field("variants")
    clientToken = field("clientToken")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePromptRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePromptRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePromptRequest:
    boto3_raw_data: "type_defs.UpdatePromptRequestTypeDef" = dataclasses.field()

    name = field("name")
    promptIdentifier = field("promptIdentifier")
    description = field("description")
    customerEncryptionKeyArn = field("customerEncryptionKeyArn")
    defaultVariant = field("defaultVariant")
    variants = field("variants")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdatePromptRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePromptRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FlowNode:
    boto3_raw_data: "type_defs.FlowNodeTypeDef" = dataclasses.field()

    name = field("name")
    type = field("type")

    @cached_property
    def configuration(self):  # pragma: no cover
        return FlowNodeConfiguration.make_one(self.boto3_raw_data["configuration"])

    @cached_property
    def inputs(self):  # pragma: no cover
        return FlowNodeInput.make_many(self.boto3_raw_data["inputs"])

    @cached_property
    def outputs(self):  # pragma: no cover
        return FlowNodeOutput.make_many(self.boto3_raw_data["outputs"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FlowNodeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FlowNodeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FlowDefinition:
    boto3_raw_data: "type_defs.FlowDefinitionTypeDef" = dataclasses.field()

    @cached_property
    def nodes(self):  # pragma: no cover
        return FlowNode.make_many(self.boto3_raw_data["nodes"])

    @cached_property
    def connections(self):  # pragma: no cover
        return FlowConnection.make_many(self.boto3_raw_data["connections"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FlowDefinitionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FlowDefinitionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFlowRequest:
    boto3_raw_data: "type_defs.CreateFlowRequestTypeDef" = dataclasses.field()

    name = field("name")
    executionRoleArn = field("executionRoleArn")
    description = field("description")
    customerEncryptionKeyArn = field("customerEncryptionKeyArn")
    definition = field("definition")
    clientToken = field("clientToken")
    tags = field("tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateFlowRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFlowRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFlowRequest:
    boto3_raw_data: "type_defs.UpdateFlowRequestTypeDef" = dataclasses.field()

    name = field("name")
    executionRoleArn = field("executionRoleArn")
    flowIdentifier = field("flowIdentifier")
    description = field("description")
    customerEncryptionKeyArn = field("customerEncryptionKeyArn")
    definition = field("definition")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateFlowRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFlowRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ValidateFlowDefinitionRequest:
    boto3_raw_data: "type_defs.ValidateFlowDefinitionRequestTypeDef" = (
        dataclasses.field()
    )

    definition = field("definition")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ValidateFlowDefinitionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ValidateFlowDefinitionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
