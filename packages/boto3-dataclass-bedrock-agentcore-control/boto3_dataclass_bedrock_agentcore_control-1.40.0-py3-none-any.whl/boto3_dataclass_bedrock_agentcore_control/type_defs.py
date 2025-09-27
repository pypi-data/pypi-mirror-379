# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_bedrock_agentcore_control import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class ContainerConfiguration:
    boto3_raw_data: "type_defs.ContainerConfigurationTypeDef" = dataclasses.field()

    containerUri = field("containerUri")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContainerConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContainerConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AgentRuntimeEndpoint:
    boto3_raw_data: "type_defs.AgentRuntimeEndpointTypeDef" = dataclasses.field()

    name = field("name")
    agentRuntimeEndpointArn = field("agentRuntimeEndpointArn")
    agentRuntimeArn = field("agentRuntimeArn")
    status = field("status")
    id = field("id")
    createdAt = field("createdAt")
    lastUpdatedAt = field("lastUpdatedAt")
    liveVersion = field("liveVersion")
    targetVersion = field("targetVersion")
    description = field("description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AgentRuntimeEndpointTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AgentRuntimeEndpointTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AgentRuntime:
    boto3_raw_data: "type_defs.AgentRuntimeTypeDef" = dataclasses.field()

    agentRuntimeArn = field("agentRuntimeArn")
    agentRuntimeId = field("agentRuntimeId")
    agentRuntimeVersion = field("agentRuntimeVersion")
    agentRuntimeName = field("agentRuntimeName")
    description = field("description")
    lastUpdatedAt = field("lastUpdatedAt")
    status = field("status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AgentRuntimeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AgentRuntimeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApiKeyCredentialProviderItem:
    boto3_raw_data: "type_defs.ApiKeyCredentialProviderItemTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    credentialProviderArn = field("credentialProviderArn")
    createdTime = field("createdTime")
    lastUpdatedTime = field("lastUpdatedTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ApiKeyCredentialProviderItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApiKeyCredentialProviderItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApiKeyCredentialProvider:
    boto3_raw_data: "type_defs.ApiKeyCredentialProviderTypeDef" = dataclasses.field()

    providerArn = field("providerArn")
    credentialParameterName = field("credentialParameterName")
    credentialPrefix = field("credentialPrefix")
    credentialLocation = field("credentialLocation")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ApiKeyCredentialProviderTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApiKeyCredentialProviderTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3Configuration:
    boto3_raw_data: "type_defs.S3ConfigurationTypeDef" = dataclasses.field()

    uri = field("uri")
    bucketOwnerAccountId = field("bucketOwnerAccountId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3ConfigurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3ConfigurationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomJWTAuthorizerConfigurationOutput:
    boto3_raw_data: "type_defs.CustomJWTAuthorizerConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    discoveryUrl = field("discoveryUrl")
    allowedAudience = field("allowedAudience")
    allowedClients = field("allowedClients")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CustomJWTAuthorizerConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomJWTAuthorizerConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomJWTAuthorizerConfiguration:
    boto3_raw_data: "type_defs.CustomJWTAuthorizerConfigurationTypeDef" = (
        dataclasses.field()
    )

    discoveryUrl = field("discoveryUrl")
    allowedAudience = field("allowedAudience")
    allowedClients = field("allowedClients")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CustomJWTAuthorizerConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomJWTAuthorizerConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VpcConfigOutput:
    boto3_raw_data: "type_defs.VpcConfigOutputTypeDef" = dataclasses.field()

    securityGroups = field("securityGroups")
    subnets = field("subnets")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VpcConfigOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VpcConfigOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VpcConfig:
    boto3_raw_data: "type_defs.VpcConfigTypeDef" = dataclasses.field()

    securityGroups = field("securityGroups")
    subnets = field("subnets")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VpcConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VpcConfigTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BrowserSummary:
    boto3_raw_data: "type_defs.BrowserSummaryTypeDef" = dataclasses.field()

    browserId = field("browserId")
    browserArn = field("browserArn")
    status = field("status")
    createdAt = field("createdAt")
    name = field("name")
    description = field("description")
    lastUpdatedAt = field("lastUpdatedAt")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BrowserSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BrowserSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CodeInterpreterSummary:
    boto3_raw_data: "type_defs.CodeInterpreterSummaryTypeDef" = dataclasses.field()

    codeInterpreterId = field("codeInterpreterId")
    codeInterpreterArn = field("codeInterpreterArn")
    status = field("status")
    createdAt = field("createdAt")
    name = field("name")
    description = field("description")
    lastUpdatedAt = field("lastUpdatedAt")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CodeInterpreterSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CodeInterpreterSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAgentRuntimeEndpointRequest:
    boto3_raw_data: "type_defs.CreateAgentRuntimeEndpointRequestTypeDef" = (
        dataclasses.field()
    )

    agentRuntimeId = field("agentRuntimeId")
    name = field("name")
    agentRuntimeVersion = field("agentRuntimeVersion")
    description = field("description")
    clientToken = field("clientToken")
    tags = field("tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateAgentRuntimeEndpointRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAgentRuntimeEndpointRequestTypeDef"]
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
class ProtocolConfiguration:
    boto3_raw_data: "type_defs.ProtocolConfigurationTypeDef" = dataclasses.field()

    serverProtocol = field("serverProtocol")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProtocolConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProtocolConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkloadIdentityDetails:
    boto3_raw_data: "type_defs.WorkloadIdentityDetailsTypeDef" = dataclasses.field()

    workloadIdentityArn = field("workloadIdentityArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WorkloadIdentityDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkloadIdentityDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateApiKeyCredentialProviderRequest:
    boto3_raw_data: "type_defs.CreateApiKeyCredentialProviderRequestTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    apiKey = field("apiKey")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateApiKeyCredentialProviderRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateApiKeyCredentialProviderRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Secret:
    boto3_raw_data: "type_defs.SecretTypeDef" = dataclasses.field()

    secretArn = field("secretArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SecretTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SecretTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateWorkloadIdentityRequest:
    boto3_raw_data: "type_defs.CreateWorkloadIdentityRequestTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    allowedResourceOauth2ReturnUrls = field("allowedResourceOauth2ReturnUrls")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateWorkloadIdentityRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateWorkloadIdentityRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OAuthCredentialProviderOutput:
    boto3_raw_data: "type_defs.OAuthCredentialProviderOutputTypeDef" = (
        dataclasses.field()
    )

    providerArn = field("providerArn")
    scopes = field("scopes")
    customParameters = field("customParameters")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.OAuthCredentialProviderOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OAuthCredentialProviderOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SemanticOverrideConsolidationConfigurationInput:
    boto3_raw_data: (
        "type_defs.SemanticOverrideConsolidationConfigurationInputTypeDef"
    ) = dataclasses.field()

    appendToPrompt = field("appendToPrompt")
    modelId = field("modelId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SemanticOverrideConsolidationConfigurationInputTypeDef"
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
                "type_defs.SemanticOverrideConsolidationConfigurationInputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SummaryOverrideConsolidationConfigurationInput:
    boto3_raw_data: (
        "type_defs.SummaryOverrideConsolidationConfigurationInputTypeDef"
    ) = dataclasses.field()

    appendToPrompt = field("appendToPrompt")
    modelId = field("modelId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SummaryOverrideConsolidationConfigurationInputTypeDef"
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
                "type_defs.SummaryOverrideConsolidationConfigurationInputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserPreferenceOverrideConsolidationConfigurationInput:
    boto3_raw_data: (
        "type_defs.UserPreferenceOverrideConsolidationConfigurationInputTypeDef"
    ) = dataclasses.field()

    appendToPrompt = field("appendToPrompt")
    modelId = field("modelId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UserPreferenceOverrideConsolidationConfigurationInputTypeDef"
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
                "type_defs.UserPreferenceOverrideConsolidationConfigurationInputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SemanticConsolidationOverride:
    boto3_raw_data: "type_defs.SemanticConsolidationOverrideTypeDef" = (
        dataclasses.field()
    )

    appendToPrompt = field("appendToPrompt")
    modelId = field("modelId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SemanticConsolidationOverrideTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SemanticConsolidationOverrideTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SummaryConsolidationOverride:
    boto3_raw_data: "type_defs.SummaryConsolidationOverrideTypeDef" = (
        dataclasses.field()
    )

    appendToPrompt = field("appendToPrompt")
    modelId = field("modelId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SummaryConsolidationOverrideTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SummaryConsolidationOverrideTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserPreferenceConsolidationOverride:
    boto3_raw_data: "type_defs.UserPreferenceConsolidationOverrideTypeDef" = (
        dataclasses.field()
    )

    appendToPrompt = field("appendToPrompt")
    modelId = field("modelId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UserPreferenceConsolidationOverrideTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UserPreferenceConsolidationOverrideTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SemanticOverrideExtractionConfigurationInput:
    boto3_raw_data: "type_defs.SemanticOverrideExtractionConfigurationInputTypeDef" = (
        dataclasses.field()
    )

    appendToPrompt = field("appendToPrompt")
    modelId = field("modelId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SemanticOverrideExtractionConfigurationInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SemanticOverrideExtractionConfigurationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserPreferenceOverrideExtractionConfigurationInput:
    boto3_raw_data: (
        "type_defs.UserPreferenceOverrideExtractionConfigurationInputTypeDef"
    ) = dataclasses.field()

    appendToPrompt = field("appendToPrompt")
    modelId = field("modelId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UserPreferenceOverrideExtractionConfigurationInputTypeDef"
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
                "type_defs.UserPreferenceOverrideExtractionConfigurationInputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SemanticExtractionOverride:
    boto3_raw_data: "type_defs.SemanticExtractionOverrideTypeDef" = dataclasses.field()

    appendToPrompt = field("appendToPrompt")
    modelId = field("modelId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SemanticExtractionOverrideTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SemanticExtractionOverrideTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserPreferenceExtractionOverride:
    boto3_raw_data: "type_defs.UserPreferenceExtractionOverrideTypeDef" = (
        dataclasses.field()
    )

    appendToPrompt = field("appendToPrompt")
    modelId = field("modelId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UserPreferenceExtractionOverrideTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UserPreferenceExtractionOverrideTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAgentRuntimeEndpointRequest:
    boto3_raw_data: "type_defs.DeleteAgentRuntimeEndpointRequestTypeDef" = (
        dataclasses.field()
    )

    agentRuntimeId = field("agentRuntimeId")
    endpointName = field("endpointName")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteAgentRuntimeEndpointRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAgentRuntimeEndpointRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAgentRuntimeRequest:
    boto3_raw_data: "type_defs.DeleteAgentRuntimeRequestTypeDef" = dataclasses.field()

    agentRuntimeId = field("agentRuntimeId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAgentRuntimeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAgentRuntimeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteApiKeyCredentialProviderRequest:
    boto3_raw_data: "type_defs.DeleteApiKeyCredentialProviderRequestTypeDef" = (
        dataclasses.field()
    )

    name = field("name")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteApiKeyCredentialProviderRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteApiKeyCredentialProviderRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBrowserRequest:
    boto3_raw_data: "type_defs.DeleteBrowserRequestTypeDef" = dataclasses.field()

    browserId = field("browserId")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteBrowserRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBrowserRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCodeInterpreterRequest:
    boto3_raw_data: "type_defs.DeleteCodeInterpreterRequestTypeDef" = (
        dataclasses.field()
    )

    codeInterpreterId = field("codeInterpreterId")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteCodeInterpreterRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCodeInterpreterRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteGatewayRequest:
    boto3_raw_data: "type_defs.DeleteGatewayRequestTypeDef" = dataclasses.field()

    gatewayIdentifier = field("gatewayIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteGatewayRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteGatewayRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteGatewayTargetRequest:
    boto3_raw_data: "type_defs.DeleteGatewayTargetRequestTypeDef" = dataclasses.field()

    gatewayIdentifier = field("gatewayIdentifier")
    targetId = field("targetId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteGatewayTargetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteGatewayTargetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteMemoryInput:
    boto3_raw_data: "type_defs.DeleteMemoryInputTypeDef" = dataclasses.field()

    memoryId = field("memoryId")
    clientToken = field("clientToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteMemoryInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteMemoryInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteMemoryStrategyInput:
    boto3_raw_data: "type_defs.DeleteMemoryStrategyInputTypeDef" = dataclasses.field()

    memoryStrategyId = field("memoryStrategyId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteMemoryStrategyInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteMemoryStrategyInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteOauth2CredentialProviderRequest:
    boto3_raw_data: "type_defs.DeleteOauth2CredentialProviderRequestTypeDef" = (
        dataclasses.field()
    )

    name = field("name")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteOauth2CredentialProviderRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteOauth2CredentialProviderRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteWorkloadIdentityRequest:
    boto3_raw_data: "type_defs.DeleteWorkloadIdentityRequestTypeDef" = (
        dataclasses.field()
    )

    name = field("name")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteWorkloadIdentityRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteWorkloadIdentityRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MCPGatewayConfigurationOutput:
    boto3_raw_data: "type_defs.MCPGatewayConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    supportedVersions = field("supportedVersions")
    instructions = field("instructions")
    searchType = field("searchType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.MCPGatewayConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MCPGatewayConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MCPGatewayConfiguration:
    boto3_raw_data: "type_defs.MCPGatewayConfigurationTypeDef" = dataclasses.field()

    supportedVersions = field("supportedVersions")
    instructions = field("instructions")
    searchType = field("searchType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MCPGatewayConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MCPGatewayConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GatewaySummary:
    boto3_raw_data: "type_defs.GatewaySummaryTypeDef" = dataclasses.field()

    gatewayId = field("gatewayId")
    name = field("name")
    status = field("status")
    createdAt = field("createdAt")
    updatedAt = field("updatedAt")
    authorizerType = field("authorizerType")
    protocolType = field("protocolType")
    description = field("description")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GatewaySummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GatewaySummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAgentRuntimeEndpointRequest:
    boto3_raw_data: "type_defs.GetAgentRuntimeEndpointRequestTypeDef" = (
        dataclasses.field()
    )

    agentRuntimeId = field("agentRuntimeId")
    endpointName = field("endpointName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetAgentRuntimeEndpointRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAgentRuntimeEndpointRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAgentRuntimeRequest:
    boto3_raw_data: "type_defs.GetAgentRuntimeRequestTypeDef" = dataclasses.field()

    agentRuntimeId = field("agentRuntimeId")
    agentRuntimeVersion = field("agentRuntimeVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAgentRuntimeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAgentRuntimeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RequestHeaderConfigurationOutput:
    boto3_raw_data: "type_defs.RequestHeaderConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    requestHeaderAllowlist = field("requestHeaderAllowlist")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RequestHeaderConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RequestHeaderConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetApiKeyCredentialProviderRequest:
    boto3_raw_data: "type_defs.GetApiKeyCredentialProviderRequestTypeDef" = (
        dataclasses.field()
    )

    name = field("name")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetApiKeyCredentialProviderRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetApiKeyCredentialProviderRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBrowserRequest:
    boto3_raw_data: "type_defs.GetBrowserRequestTypeDef" = dataclasses.field()

    browserId = field("browserId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetBrowserRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBrowserRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCodeInterpreterRequest:
    boto3_raw_data: "type_defs.GetCodeInterpreterRequestTypeDef" = dataclasses.field()

    codeInterpreterId = field("codeInterpreterId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCodeInterpreterRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCodeInterpreterRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetGatewayRequest:
    boto3_raw_data: "type_defs.GetGatewayRequestTypeDef" = dataclasses.field()

    gatewayIdentifier = field("gatewayIdentifier")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetGatewayRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetGatewayRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetGatewayTargetRequest:
    boto3_raw_data: "type_defs.GetGatewayTargetRequestTypeDef" = dataclasses.field()

    gatewayIdentifier = field("gatewayIdentifier")
    targetId = field("targetId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetGatewayTargetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetGatewayTargetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMemoryInput:
    boto3_raw_data: "type_defs.GetMemoryInputTypeDef" = dataclasses.field()

    memoryId = field("memoryId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetMemoryInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetMemoryInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WaiterConfig:
    boto3_raw_data: "type_defs.WaiterConfigTypeDef" = dataclasses.field()

    Delay = field("Delay")
    MaxAttempts = field("MaxAttempts")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WaiterConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WaiterConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetOauth2CredentialProviderRequest:
    boto3_raw_data: "type_defs.GetOauth2CredentialProviderRequestTypeDef" = (
        dataclasses.field()
    )

    name = field("name")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetOauth2CredentialProviderRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetOauth2CredentialProviderRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTokenVaultRequest:
    boto3_raw_data: "type_defs.GetTokenVaultRequestTypeDef" = dataclasses.field()

    tokenVaultId = field("tokenVaultId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTokenVaultRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTokenVaultRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KmsConfiguration:
    boto3_raw_data: "type_defs.KmsConfigurationTypeDef" = dataclasses.field()

    keyType = field("keyType")
    kmsKeyArn = field("kmsKeyArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.KmsConfigurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KmsConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetWorkloadIdentityRequest:
    boto3_raw_data: "type_defs.GetWorkloadIdentityRequestTypeDef" = dataclasses.field()

    name = field("name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetWorkloadIdentityRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetWorkloadIdentityRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GithubOauth2ProviderConfigInput:
    boto3_raw_data: "type_defs.GithubOauth2ProviderConfigInputTypeDef" = (
        dataclasses.field()
    )

    clientId = field("clientId")
    clientSecret = field("clientSecret")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GithubOauth2ProviderConfigInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GithubOauth2ProviderConfigInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GoogleOauth2ProviderConfigInput:
    boto3_raw_data: "type_defs.GoogleOauth2ProviderConfigInputTypeDef" = (
        dataclasses.field()
    )

    clientId = field("clientId")
    clientSecret = field("clientSecret")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GoogleOauth2ProviderConfigInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GoogleOauth2ProviderConfigInputTypeDef"]
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
class ListAgentRuntimeEndpointsRequest:
    boto3_raw_data: "type_defs.ListAgentRuntimeEndpointsRequestTypeDef" = (
        dataclasses.field()
    )

    agentRuntimeId = field("agentRuntimeId")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAgentRuntimeEndpointsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAgentRuntimeEndpointsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAgentRuntimeVersionsRequest:
    boto3_raw_data: "type_defs.ListAgentRuntimeVersionsRequestTypeDef" = (
        dataclasses.field()
    )

    agentRuntimeId = field("agentRuntimeId")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAgentRuntimeVersionsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAgentRuntimeVersionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAgentRuntimesRequest:
    boto3_raw_data: "type_defs.ListAgentRuntimesRequestTypeDef" = dataclasses.field()

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAgentRuntimesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAgentRuntimesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListApiKeyCredentialProvidersRequest:
    boto3_raw_data: "type_defs.ListApiKeyCredentialProvidersRequestTypeDef" = (
        dataclasses.field()
    )

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListApiKeyCredentialProvidersRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApiKeyCredentialProvidersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBrowsersRequest:
    boto3_raw_data: "type_defs.ListBrowsersRequestTypeDef" = dataclasses.field()

    maxResults = field("maxResults")
    nextToken = field("nextToken")
    type = field("type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBrowsersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBrowsersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCodeInterpretersRequest:
    boto3_raw_data: "type_defs.ListCodeInterpretersRequestTypeDef" = dataclasses.field()

    maxResults = field("maxResults")
    nextToken = field("nextToken")
    type = field("type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCodeInterpretersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCodeInterpretersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGatewayTargetsRequest:
    boto3_raw_data: "type_defs.ListGatewayTargetsRequestTypeDef" = dataclasses.field()

    gatewayIdentifier = field("gatewayIdentifier")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListGatewayTargetsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGatewayTargetsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TargetSummary:
    boto3_raw_data: "type_defs.TargetSummaryTypeDef" = dataclasses.field()

    targetId = field("targetId")
    name = field("name")
    status = field("status")
    createdAt = field("createdAt")
    updatedAt = field("updatedAt")
    description = field("description")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TargetSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TargetSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGatewaysRequest:
    boto3_raw_data: "type_defs.ListGatewaysRequestTypeDef" = dataclasses.field()

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListGatewaysRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGatewaysRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMemoriesInput:
    boto3_raw_data: "type_defs.ListMemoriesInputTypeDef" = dataclasses.field()

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListMemoriesInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMemoriesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MemorySummary:
    boto3_raw_data: "type_defs.MemorySummaryTypeDef" = dataclasses.field()

    createdAt = field("createdAt")
    updatedAt = field("updatedAt")
    arn = field("arn")
    id = field("id")
    status = field("status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MemorySummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MemorySummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOauth2CredentialProvidersRequest:
    boto3_raw_data: "type_defs.ListOauth2CredentialProvidersRequestTypeDef" = (
        dataclasses.field()
    )

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListOauth2CredentialProvidersRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOauth2CredentialProvidersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Oauth2CredentialProviderItem:
    boto3_raw_data: "type_defs.Oauth2CredentialProviderItemTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    credentialProviderVendor = field("credentialProviderVendor")
    credentialProviderArn = field("credentialProviderArn")
    createdTime = field("createdTime")
    lastUpdatedTime = field("lastUpdatedTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.Oauth2CredentialProviderItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.Oauth2CredentialProviderItemTypeDef"]
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
class ListWorkloadIdentitiesRequest:
    boto3_raw_data: "type_defs.ListWorkloadIdentitiesRequestTypeDef" = (
        dataclasses.field()
    )

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListWorkloadIdentitiesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorkloadIdentitiesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkloadIdentityType:
    boto3_raw_data: "type_defs.WorkloadIdentityTypeTypeDef" = dataclasses.field()

    name = field("name")
    workloadIdentityArn = field("workloadIdentityArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WorkloadIdentityTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkloadIdentityTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SemanticMemoryStrategyInput:
    boto3_raw_data: "type_defs.SemanticMemoryStrategyInputTypeDef" = dataclasses.field()

    name = field("name")
    description = field("description")
    namespaces = field("namespaces")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SemanticMemoryStrategyInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SemanticMemoryStrategyInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SummaryMemoryStrategyInput:
    boto3_raw_data: "type_defs.SummaryMemoryStrategyInputTypeDef" = dataclasses.field()

    name = field("name")
    description = field("description")
    namespaces = field("namespaces")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SummaryMemoryStrategyInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SummaryMemoryStrategyInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserPreferenceMemoryStrategyInput:
    boto3_raw_data: "type_defs.UserPreferenceMemoryStrategyInputTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    description = field("description")
    namespaces = field("namespaces")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UserPreferenceMemoryStrategyInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UserPreferenceMemoryStrategyInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MicrosoftOauth2ProviderConfigInput:
    boto3_raw_data: "type_defs.MicrosoftOauth2ProviderConfigInputTypeDef" = (
        dataclasses.field()
    )

    clientId = field("clientId")
    clientSecret = field("clientSecret")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MicrosoftOauth2ProviderConfigInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MicrosoftOauth2ProviderConfigInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OAuthCredentialProvider:
    boto3_raw_data: "type_defs.OAuthCredentialProviderTypeDef" = dataclasses.field()

    providerArn = field("providerArn")
    scopes = field("scopes")
    customParameters = field("customParameters")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OAuthCredentialProviderTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OAuthCredentialProviderTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Oauth2AuthorizationServerMetadataOutput:
    boto3_raw_data: "type_defs.Oauth2AuthorizationServerMetadataOutputTypeDef" = (
        dataclasses.field()
    )

    issuer = field("issuer")
    authorizationEndpoint = field("authorizationEndpoint")
    tokenEndpoint = field("tokenEndpoint")
    responseTypes = field("responseTypes")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.Oauth2AuthorizationServerMetadataOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.Oauth2AuthorizationServerMetadataOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Oauth2AuthorizationServerMetadata:
    boto3_raw_data: "type_defs.Oauth2AuthorizationServerMetadataTypeDef" = (
        dataclasses.field()
    )

    issuer = field("issuer")
    authorizationEndpoint = field("authorizationEndpoint")
    tokenEndpoint = field("tokenEndpoint")
    responseTypes = field("responseTypes")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.Oauth2AuthorizationServerMetadataTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.Oauth2AuthorizationServerMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SalesforceOauth2ProviderConfigInput:
    boto3_raw_data: "type_defs.SalesforceOauth2ProviderConfigInputTypeDef" = (
        dataclasses.field()
    )

    clientId = field("clientId")
    clientSecret = field("clientSecret")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SalesforceOauth2ProviderConfigInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SalesforceOauth2ProviderConfigInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SlackOauth2ProviderConfigInput:
    boto3_raw_data: "type_defs.SlackOauth2ProviderConfigInputTypeDef" = (
        dataclasses.field()
    )

    clientId = field("clientId")
    clientSecret = field("clientSecret")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SlackOauth2ProviderConfigInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SlackOauth2ProviderConfigInputTypeDef"]
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

    bucket = field("bucket")
    prefix = field("prefix")

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
class RequestHeaderConfiguration:
    boto3_raw_data: "type_defs.RequestHeaderConfigurationTypeDef" = dataclasses.field()

    requestHeaderAllowlist = field("requestHeaderAllowlist")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RequestHeaderConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RequestHeaderConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SchemaDefinitionOutput:
    boto3_raw_data: "type_defs.SchemaDefinitionOutputTypeDef" = dataclasses.field()

    type = field("type")
    properties = field("properties")
    required = field("required")
    items = field("items")
    description = field("description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SchemaDefinitionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SchemaDefinitionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SchemaDefinition:
    boto3_raw_data: "type_defs.SchemaDefinitionTypeDef" = dataclasses.field()

    type = field("type")
    properties = field("properties")
    required = field("required")
    items = field("items")
    description = field("description")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SchemaDefinitionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SchemaDefinitionTypeDef"]
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
class UpdateAgentRuntimeEndpointRequest:
    boto3_raw_data: "type_defs.UpdateAgentRuntimeEndpointRequestTypeDef" = (
        dataclasses.field()
    )

    agentRuntimeId = field("agentRuntimeId")
    endpointName = field("endpointName")
    agentRuntimeVersion = field("agentRuntimeVersion")
    description = field("description")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateAgentRuntimeEndpointRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAgentRuntimeEndpointRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateApiKeyCredentialProviderRequest:
    boto3_raw_data: "type_defs.UpdateApiKeyCredentialProviderRequestTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    apiKey = field("apiKey")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateApiKeyCredentialProviderRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateApiKeyCredentialProviderRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateWorkloadIdentityRequest:
    boto3_raw_data: "type_defs.UpdateWorkloadIdentityRequestTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    allowedResourceOauth2ReturnUrls = field("allowedResourceOauth2ReturnUrls")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateWorkloadIdentityRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateWorkloadIdentityRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AgentRuntimeArtifact:
    boto3_raw_data: "type_defs.AgentRuntimeArtifactTypeDef" = dataclasses.field()

    @cached_property
    def containerConfiguration(self):  # pragma: no cover
        return ContainerConfiguration.make_one(
            self.boto3_raw_data["containerConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AgentRuntimeArtifactTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AgentRuntimeArtifactTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApiSchemaConfiguration:
    boto3_raw_data: "type_defs.ApiSchemaConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def s3(self):  # pragma: no cover
        return S3Configuration.make_one(self.boto3_raw_data["s3"])

    inlinePayload = field("inlinePayload")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ApiSchemaConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApiSchemaConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AuthorizerConfigurationOutput:
    boto3_raw_data: "type_defs.AuthorizerConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def customJWTAuthorizer(self):  # pragma: no cover
        return CustomJWTAuthorizerConfigurationOutput.make_one(
            self.boto3_raw_data["customJWTAuthorizer"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AuthorizerConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AuthorizerConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AuthorizerConfiguration:
    boto3_raw_data: "type_defs.AuthorizerConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def customJWTAuthorizer(self):  # pragma: no cover
        return CustomJWTAuthorizerConfiguration.make_one(
            self.boto3_raw_data["customJWTAuthorizer"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AuthorizerConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AuthorizerConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BrowserNetworkConfigurationOutput:
    boto3_raw_data: "type_defs.BrowserNetworkConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    networkMode = field("networkMode")

    @cached_property
    def vpcConfig(self):  # pragma: no cover
        return VpcConfigOutput.make_one(self.boto3_raw_data["vpcConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BrowserNetworkConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BrowserNetworkConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CodeInterpreterNetworkConfigurationOutput:
    boto3_raw_data: "type_defs.CodeInterpreterNetworkConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    networkMode = field("networkMode")

    @cached_property
    def vpcConfig(self):  # pragma: no cover
        return VpcConfigOutput.make_one(self.boto3_raw_data["vpcConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CodeInterpreterNetworkConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CodeInterpreterNetworkConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NetworkConfigurationOutput:
    boto3_raw_data: "type_defs.NetworkConfigurationOutputTypeDef" = dataclasses.field()

    networkMode = field("networkMode")

    @cached_property
    def networkModeConfig(self):  # pragma: no cover
        return VpcConfigOutput.make_one(self.boto3_raw_data["networkModeConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NetworkConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NetworkConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BrowserNetworkConfiguration:
    boto3_raw_data: "type_defs.BrowserNetworkConfigurationTypeDef" = dataclasses.field()

    networkMode = field("networkMode")

    @cached_property
    def vpcConfig(self):  # pragma: no cover
        return VpcConfig.make_one(self.boto3_raw_data["vpcConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BrowserNetworkConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BrowserNetworkConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CodeInterpreterNetworkConfiguration:
    boto3_raw_data: "type_defs.CodeInterpreterNetworkConfigurationTypeDef" = (
        dataclasses.field()
    )

    networkMode = field("networkMode")

    @cached_property
    def vpcConfig(self):  # pragma: no cover
        return VpcConfig.make_one(self.boto3_raw_data["vpcConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CodeInterpreterNetworkConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CodeInterpreterNetworkConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NetworkConfiguration:
    boto3_raw_data: "type_defs.NetworkConfigurationTypeDef" = dataclasses.field()

    networkMode = field("networkMode")

    @cached_property
    def networkModeConfig(self):  # pragma: no cover
        return VpcConfig.make_one(self.boto3_raw_data["networkModeConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NetworkConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NetworkConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAgentRuntimeEndpointResponse:
    boto3_raw_data: "type_defs.CreateAgentRuntimeEndpointResponseTypeDef" = (
        dataclasses.field()
    )

    targetVersion = field("targetVersion")
    agentRuntimeEndpointArn = field("agentRuntimeEndpointArn")
    agentRuntimeArn = field("agentRuntimeArn")
    status = field("status")
    createdAt = field("createdAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateAgentRuntimeEndpointResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAgentRuntimeEndpointResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBrowserResponse:
    boto3_raw_data: "type_defs.CreateBrowserResponseTypeDef" = dataclasses.field()

    browserId = field("browserId")
    browserArn = field("browserArn")
    createdAt = field("createdAt")
    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateBrowserResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBrowserResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCodeInterpreterResponse:
    boto3_raw_data: "type_defs.CreateCodeInterpreterResponseTypeDef" = (
        dataclasses.field()
    )

    codeInterpreterId = field("codeInterpreterId")
    codeInterpreterArn = field("codeInterpreterArn")
    createdAt = field("createdAt")
    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateCodeInterpreterResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCodeInterpreterResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateWorkloadIdentityResponse:
    boto3_raw_data: "type_defs.CreateWorkloadIdentityResponseTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    workloadIdentityArn = field("workloadIdentityArn")
    allowedResourceOauth2ReturnUrls = field("allowedResourceOauth2ReturnUrls")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateWorkloadIdentityResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateWorkloadIdentityResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAgentRuntimeEndpointResponse:
    boto3_raw_data: "type_defs.DeleteAgentRuntimeEndpointResponseTypeDef" = (
        dataclasses.field()
    )

    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteAgentRuntimeEndpointResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAgentRuntimeEndpointResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAgentRuntimeResponse:
    boto3_raw_data: "type_defs.DeleteAgentRuntimeResponseTypeDef" = dataclasses.field()

    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAgentRuntimeResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAgentRuntimeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBrowserResponse:
    boto3_raw_data: "type_defs.DeleteBrowserResponseTypeDef" = dataclasses.field()

    browserId = field("browserId")
    status = field("status")
    lastUpdatedAt = field("lastUpdatedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteBrowserResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBrowserResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCodeInterpreterResponse:
    boto3_raw_data: "type_defs.DeleteCodeInterpreterResponseTypeDef" = (
        dataclasses.field()
    )

    codeInterpreterId = field("codeInterpreterId")
    status = field("status")
    lastUpdatedAt = field("lastUpdatedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteCodeInterpreterResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCodeInterpreterResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteGatewayResponse:
    boto3_raw_data: "type_defs.DeleteGatewayResponseTypeDef" = dataclasses.field()

    gatewayId = field("gatewayId")
    status = field("status")
    statusReasons = field("statusReasons")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteGatewayResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteGatewayResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteGatewayTargetResponse:
    boto3_raw_data: "type_defs.DeleteGatewayTargetResponseTypeDef" = dataclasses.field()

    gatewayArn = field("gatewayArn")
    targetId = field("targetId")
    status = field("status")
    statusReasons = field("statusReasons")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteGatewayTargetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteGatewayTargetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteMemoryOutput:
    boto3_raw_data: "type_defs.DeleteMemoryOutputTypeDef" = dataclasses.field()

    memoryId = field("memoryId")
    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteMemoryOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteMemoryOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAgentRuntimeEndpointResponse:
    boto3_raw_data: "type_defs.GetAgentRuntimeEndpointResponseTypeDef" = (
        dataclasses.field()
    )

    liveVersion = field("liveVersion")
    targetVersion = field("targetVersion")
    agentRuntimeEndpointArn = field("agentRuntimeEndpointArn")
    agentRuntimeArn = field("agentRuntimeArn")
    description = field("description")
    status = field("status")
    createdAt = field("createdAt")
    lastUpdatedAt = field("lastUpdatedAt")
    failureReason = field("failureReason")
    name = field("name")
    id = field("id")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetAgentRuntimeEndpointResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAgentRuntimeEndpointResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetWorkloadIdentityResponse:
    boto3_raw_data: "type_defs.GetWorkloadIdentityResponseTypeDef" = dataclasses.field()

    name = field("name")
    workloadIdentityArn = field("workloadIdentityArn")
    allowedResourceOauth2ReturnUrls = field("allowedResourceOauth2ReturnUrls")
    createdTime = field("createdTime")
    lastUpdatedTime = field("lastUpdatedTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetWorkloadIdentityResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetWorkloadIdentityResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAgentRuntimeEndpointsResponse:
    boto3_raw_data: "type_defs.ListAgentRuntimeEndpointsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def runtimeEndpoints(self):  # pragma: no cover
        return AgentRuntimeEndpoint.make_many(self.boto3_raw_data["runtimeEndpoints"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAgentRuntimeEndpointsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAgentRuntimeEndpointsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAgentRuntimeVersionsResponse:
    boto3_raw_data: "type_defs.ListAgentRuntimeVersionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def agentRuntimes(self):  # pragma: no cover
        return AgentRuntime.make_many(self.boto3_raw_data["agentRuntimes"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAgentRuntimeVersionsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAgentRuntimeVersionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAgentRuntimesResponse:
    boto3_raw_data: "type_defs.ListAgentRuntimesResponseTypeDef" = dataclasses.field()

    @cached_property
    def agentRuntimes(self):  # pragma: no cover
        return AgentRuntime.make_many(self.boto3_raw_data["agentRuntimes"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAgentRuntimesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAgentRuntimesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListApiKeyCredentialProvidersResponse:
    boto3_raw_data: "type_defs.ListApiKeyCredentialProvidersResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def credentialProviders(self):  # pragma: no cover
        return ApiKeyCredentialProviderItem.make_many(
            self.boto3_raw_data["credentialProviders"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListApiKeyCredentialProvidersResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApiKeyCredentialProvidersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBrowsersResponse:
    boto3_raw_data: "type_defs.ListBrowsersResponseTypeDef" = dataclasses.field()

    @cached_property
    def browserSummaries(self):  # pragma: no cover
        return BrowserSummary.make_many(self.boto3_raw_data["browserSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBrowsersResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBrowsersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCodeInterpretersResponse:
    boto3_raw_data: "type_defs.ListCodeInterpretersResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def codeInterpreterSummaries(self):  # pragma: no cover
        return CodeInterpreterSummary.make_many(
            self.boto3_raw_data["codeInterpreterSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCodeInterpretersResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCodeInterpretersResponseTypeDef"]
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
class UpdateAgentRuntimeEndpointResponse:
    boto3_raw_data: "type_defs.UpdateAgentRuntimeEndpointResponseTypeDef" = (
        dataclasses.field()
    )

    liveVersion = field("liveVersion")
    targetVersion = field("targetVersion")
    agentRuntimeEndpointArn = field("agentRuntimeEndpointArn")
    agentRuntimeArn = field("agentRuntimeArn")
    status = field("status")
    createdAt = field("createdAt")
    lastUpdatedAt = field("lastUpdatedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateAgentRuntimeEndpointResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAgentRuntimeEndpointResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateWorkloadIdentityResponse:
    boto3_raw_data: "type_defs.UpdateWorkloadIdentityResponseTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    workloadIdentityArn = field("workloadIdentityArn")
    allowedResourceOauth2ReturnUrls = field("allowedResourceOauth2ReturnUrls")
    createdTime = field("createdTime")
    lastUpdatedTime = field("lastUpdatedTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateWorkloadIdentityResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateWorkloadIdentityResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAgentRuntimeResponse:
    boto3_raw_data: "type_defs.CreateAgentRuntimeResponseTypeDef" = dataclasses.field()

    agentRuntimeArn = field("agentRuntimeArn")

    @cached_property
    def workloadIdentityDetails(self):  # pragma: no cover
        return WorkloadIdentityDetails.make_one(
            self.boto3_raw_data["workloadIdentityDetails"]
        )

    agentRuntimeId = field("agentRuntimeId")
    agentRuntimeVersion = field("agentRuntimeVersion")
    createdAt = field("createdAt")
    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAgentRuntimeResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAgentRuntimeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAgentRuntimeResponse:
    boto3_raw_data: "type_defs.UpdateAgentRuntimeResponseTypeDef" = dataclasses.field()

    agentRuntimeArn = field("agentRuntimeArn")
    agentRuntimeId = field("agentRuntimeId")

    @cached_property
    def workloadIdentityDetails(self):  # pragma: no cover
        return WorkloadIdentityDetails.make_one(
            self.boto3_raw_data["workloadIdentityDetails"]
        )

    agentRuntimeVersion = field("agentRuntimeVersion")
    createdAt = field("createdAt")
    lastUpdatedAt = field("lastUpdatedAt")
    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAgentRuntimeResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAgentRuntimeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateApiKeyCredentialProviderResponse:
    boto3_raw_data: "type_defs.CreateApiKeyCredentialProviderResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def apiKeySecretArn(self):  # pragma: no cover
        return Secret.make_one(self.boto3_raw_data["apiKeySecretArn"])

    name = field("name")
    credentialProviderArn = field("credentialProviderArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateApiKeyCredentialProviderResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateApiKeyCredentialProviderResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateOauth2CredentialProviderResponse:
    boto3_raw_data: "type_defs.CreateOauth2CredentialProviderResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def clientSecretArn(self):  # pragma: no cover
        return Secret.make_one(self.boto3_raw_data["clientSecretArn"])

    name = field("name")
    credentialProviderArn = field("credentialProviderArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateOauth2CredentialProviderResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateOauth2CredentialProviderResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetApiKeyCredentialProviderResponse:
    boto3_raw_data: "type_defs.GetApiKeyCredentialProviderResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def apiKeySecretArn(self):  # pragma: no cover
        return Secret.make_one(self.boto3_raw_data["apiKeySecretArn"])

    name = field("name")
    credentialProviderArn = field("credentialProviderArn")
    createdTime = field("createdTime")
    lastUpdatedTime = field("lastUpdatedTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetApiKeyCredentialProviderResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetApiKeyCredentialProviderResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateApiKeyCredentialProviderResponse:
    boto3_raw_data: "type_defs.UpdateApiKeyCredentialProviderResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def apiKeySecretArn(self):  # pragma: no cover
        return Secret.make_one(self.boto3_raw_data["apiKeySecretArn"])

    name = field("name")
    credentialProviderArn = field("credentialProviderArn")
    createdTime = field("createdTime")
    lastUpdatedTime = field("lastUpdatedTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateApiKeyCredentialProviderResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateApiKeyCredentialProviderResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CredentialProviderOutput:
    boto3_raw_data: "type_defs.CredentialProviderOutputTypeDef" = dataclasses.field()

    @cached_property
    def oauthCredentialProvider(self):  # pragma: no cover
        return OAuthCredentialProviderOutput.make_one(
            self.boto3_raw_data["oauthCredentialProvider"]
        )

    @cached_property
    def apiKeyCredentialProvider(self):  # pragma: no cover
        return ApiKeyCredentialProvider.make_one(
            self.boto3_raw_data["apiKeyCredentialProvider"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CredentialProviderOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CredentialProviderOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SummaryOverrideConfigurationInput:
    boto3_raw_data: "type_defs.SummaryOverrideConfigurationInputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def consolidation(self):  # pragma: no cover
        return SummaryOverrideConsolidationConfigurationInput.make_one(
            self.boto3_raw_data["consolidation"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SummaryOverrideConfigurationInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SummaryOverrideConfigurationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomConsolidationConfigurationInput:
    boto3_raw_data: "type_defs.CustomConsolidationConfigurationInputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def semanticConsolidationOverride(self):  # pragma: no cover
        return SemanticOverrideConsolidationConfigurationInput.make_one(
            self.boto3_raw_data["semanticConsolidationOverride"]
        )

    @cached_property
    def summaryConsolidationOverride(self):  # pragma: no cover
        return SummaryOverrideConsolidationConfigurationInput.make_one(
            self.boto3_raw_data["summaryConsolidationOverride"]
        )

    @cached_property
    def userPreferenceConsolidationOverride(self):  # pragma: no cover
        return UserPreferenceOverrideConsolidationConfigurationInput.make_one(
            self.boto3_raw_data["userPreferenceConsolidationOverride"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CustomConsolidationConfigurationInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomConsolidationConfigurationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomConsolidationConfiguration:
    boto3_raw_data: "type_defs.CustomConsolidationConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def semanticConsolidationOverride(self):  # pragma: no cover
        return SemanticConsolidationOverride.make_one(
            self.boto3_raw_data["semanticConsolidationOverride"]
        )

    @cached_property
    def summaryConsolidationOverride(self):  # pragma: no cover
        return SummaryConsolidationOverride.make_one(
            self.boto3_raw_data["summaryConsolidationOverride"]
        )

    @cached_property
    def userPreferenceConsolidationOverride(self):  # pragma: no cover
        return UserPreferenceConsolidationOverride.make_one(
            self.boto3_raw_data["userPreferenceConsolidationOverride"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CustomConsolidationConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomConsolidationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SemanticOverrideConfigurationInput:
    boto3_raw_data: "type_defs.SemanticOverrideConfigurationInputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def extraction(self):  # pragma: no cover
        return SemanticOverrideExtractionConfigurationInput.make_one(
            self.boto3_raw_data["extraction"]
        )

    @cached_property
    def consolidation(self):  # pragma: no cover
        return SemanticOverrideConsolidationConfigurationInput.make_one(
            self.boto3_raw_data["consolidation"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SemanticOverrideConfigurationInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SemanticOverrideConfigurationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomExtractionConfigurationInput:
    boto3_raw_data: "type_defs.CustomExtractionConfigurationInputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def semanticExtractionOverride(self):  # pragma: no cover
        return SemanticOverrideExtractionConfigurationInput.make_one(
            self.boto3_raw_data["semanticExtractionOverride"]
        )

    @cached_property
    def userPreferenceExtractionOverride(self):  # pragma: no cover
        return UserPreferenceOverrideExtractionConfigurationInput.make_one(
            self.boto3_raw_data["userPreferenceExtractionOverride"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CustomExtractionConfigurationInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomExtractionConfigurationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserPreferenceOverrideConfigurationInput:
    boto3_raw_data: "type_defs.UserPreferenceOverrideConfigurationInputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def extraction(self):  # pragma: no cover
        return UserPreferenceOverrideExtractionConfigurationInput.make_one(
            self.boto3_raw_data["extraction"]
        )

    @cached_property
    def consolidation(self):  # pragma: no cover
        return UserPreferenceOverrideConsolidationConfigurationInput.make_one(
            self.boto3_raw_data["consolidation"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UserPreferenceOverrideConfigurationInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UserPreferenceOverrideConfigurationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomExtractionConfiguration:
    boto3_raw_data: "type_defs.CustomExtractionConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def semanticExtractionOverride(self):  # pragma: no cover
        return SemanticExtractionOverride.make_one(
            self.boto3_raw_data["semanticExtractionOverride"]
        )

    @cached_property
    def userPreferenceExtractionOverride(self):  # pragma: no cover
        return UserPreferenceExtractionOverride.make_one(
            self.boto3_raw_data["userPreferenceExtractionOverride"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CustomExtractionConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomExtractionConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GatewayProtocolConfigurationOutput:
    boto3_raw_data: "type_defs.GatewayProtocolConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def mcp(self):  # pragma: no cover
        return MCPGatewayConfigurationOutput.make_one(self.boto3_raw_data["mcp"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GatewayProtocolConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GatewayProtocolConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GatewayProtocolConfiguration:
    boto3_raw_data: "type_defs.GatewayProtocolConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def mcp(self):  # pragma: no cover
        return MCPGatewayConfiguration.make_one(self.boto3_raw_data["mcp"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GatewayProtocolConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GatewayProtocolConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGatewaysResponse:
    boto3_raw_data: "type_defs.ListGatewaysResponseTypeDef" = dataclasses.field()

    @cached_property
    def items(self):  # pragma: no cover
        return GatewaySummary.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListGatewaysResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGatewaysResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMemoryInputWait:
    boto3_raw_data: "type_defs.GetMemoryInputWaitTypeDef" = dataclasses.field()

    memoryId = field("memoryId")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMemoryInputWaitTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMemoryInputWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTokenVaultResponse:
    boto3_raw_data: "type_defs.GetTokenVaultResponseTypeDef" = dataclasses.field()

    tokenVaultId = field("tokenVaultId")

    @cached_property
    def kmsConfiguration(self):  # pragma: no cover
        return KmsConfiguration.make_one(self.boto3_raw_data["kmsConfiguration"])

    lastModifiedDate = field("lastModifiedDate")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTokenVaultResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTokenVaultResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetTokenVaultCMKRequest:
    boto3_raw_data: "type_defs.SetTokenVaultCMKRequestTypeDef" = dataclasses.field()

    @cached_property
    def kmsConfiguration(self):  # pragma: no cover
        return KmsConfiguration.make_one(self.boto3_raw_data["kmsConfiguration"])

    tokenVaultId = field("tokenVaultId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SetTokenVaultCMKRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetTokenVaultCMKRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetTokenVaultCMKResponse:
    boto3_raw_data: "type_defs.SetTokenVaultCMKResponseTypeDef" = dataclasses.field()

    tokenVaultId = field("tokenVaultId")

    @cached_property
    def kmsConfiguration(self):  # pragma: no cover
        return KmsConfiguration.make_one(self.boto3_raw_data["kmsConfiguration"])

    lastModifiedDate = field("lastModifiedDate")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SetTokenVaultCMKResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetTokenVaultCMKResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAgentRuntimeEndpointsRequestPaginate:
    boto3_raw_data: "type_defs.ListAgentRuntimeEndpointsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    agentRuntimeId = field("agentRuntimeId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAgentRuntimeEndpointsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAgentRuntimeEndpointsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAgentRuntimeVersionsRequestPaginate:
    boto3_raw_data: "type_defs.ListAgentRuntimeVersionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    agentRuntimeId = field("agentRuntimeId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAgentRuntimeVersionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAgentRuntimeVersionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAgentRuntimesRequestPaginate:
    boto3_raw_data: "type_defs.ListAgentRuntimesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAgentRuntimesRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAgentRuntimesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListApiKeyCredentialProvidersRequestPaginate:
    boto3_raw_data: "type_defs.ListApiKeyCredentialProvidersRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListApiKeyCredentialProvidersRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApiKeyCredentialProvidersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBrowsersRequestPaginate:
    boto3_raw_data: "type_defs.ListBrowsersRequestPaginateTypeDef" = dataclasses.field()

    type = field("type")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBrowsersRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBrowsersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCodeInterpretersRequestPaginate:
    boto3_raw_data: "type_defs.ListCodeInterpretersRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    type = field("type")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCodeInterpretersRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCodeInterpretersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGatewayTargetsRequestPaginate:
    boto3_raw_data: "type_defs.ListGatewayTargetsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    gatewayIdentifier = field("gatewayIdentifier")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListGatewayTargetsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGatewayTargetsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGatewaysRequestPaginate:
    boto3_raw_data: "type_defs.ListGatewaysRequestPaginateTypeDef" = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListGatewaysRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGatewaysRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMemoriesInputPaginate:
    boto3_raw_data: "type_defs.ListMemoriesInputPaginateTypeDef" = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMemoriesInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMemoriesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOauth2CredentialProvidersRequestPaginate:
    boto3_raw_data: "type_defs.ListOauth2CredentialProvidersRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListOauth2CredentialProvidersRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOauth2CredentialProvidersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWorkloadIdentitiesRequestPaginate:
    boto3_raw_data: "type_defs.ListWorkloadIdentitiesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListWorkloadIdentitiesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorkloadIdentitiesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGatewayTargetsResponse:
    boto3_raw_data: "type_defs.ListGatewayTargetsResponseTypeDef" = dataclasses.field()

    @cached_property
    def items(self):  # pragma: no cover
        return TargetSummary.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListGatewayTargetsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGatewayTargetsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMemoriesOutput:
    boto3_raw_data: "type_defs.ListMemoriesOutputTypeDef" = dataclasses.field()

    @cached_property
    def memories(self):  # pragma: no cover
        return MemorySummary.make_many(self.boto3_raw_data["memories"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMemoriesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMemoriesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOauth2CredentialProvidersResponse:
    boto3_raw_data: "type_defs.ListOauth2CredentialProvidersResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def credentialProviders(self):  # pragma: no cover
        return Oauth2CredentialProviderItem.make_many(
            self.boto3_raw_data["credentialProviders"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListOauth2CredentialProvidersResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOauth2CredentialProvidersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWorkloadIdentitiesResponse:
    boto3_raw_data: "type_defs.ListWorkloadIdentitiesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def workloadIdentities(self):  # pragma: no cover
        return WorkloadIdentityType.make_many(self.boto3_raw_data["workloadIdentities"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListWorkloadIdentitiesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorkloadIdentitiesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Oauth2DiscoveryOutput:
    boto3_raw_data: "type_defs.Oauth2DiscoveryOutputTypeDef" = dataclasses.field()

    discoveryUrl = field("discoveryUrl")

    @cached_property
    def authorizationServerMetadata(self):  # pragma: no cover
        return Oauth2AuthorizationServerMetadataOutput.make_one(
            self.boto3_raw_data["authorizationServerMetadata"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.Oauth2DiscoveryOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.Oauth2DiscoveryOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecordingConfig:
    boto3_raw_data: "type_defs.RecordingConfigTypeDef" = dataclasses.field()

    enabled = field("enabled")

    @cached_property
    def s3Location(self):  # pragma: no cover
        return S3Location.make_one(self.boto3_raw_data["s3Location"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RecordingConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RecordingConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ToolDefinitionOutput:
    boto3_raw_data: "type_defs.ToolDefinitionOutputTypeDef" = dataclasses.field()

    name = field("name")
    description = field("description")

    @cached_property
    def inputSchema(self):  # pragma: no cover
        return SchemaDefinitionOutput.make_one(self.boto3_raw_data["inputSchema"])

    @cached_property
    def outputSchema(self):  # pragma: no cover
        return SchemaDefinitionOutput.make_one(self.boto3_raw_data["outputSchema"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ToolDefinitionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ToolDefinitionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ToolDefinition:
    boto3_raw_data: "type_defs.ToolDefinitionTypeDef" = dataclasses.field()

    name = field("name")
    description = field("description")

    @cached_property
    def inputSchema(self):  # pragma: no cover
        return SchemaDefinition.make_one(self.boto3_raw_data["inputSchema"])

    @cached_property
    def outputSchema(self):  # pragma: no cover
        return SchemaDefinition.make_one(self.boto3_raw_data["outputSchema"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ToolDefinitionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ToolDefinitionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCodeInterpreterResponse:
    boto3_raw_data: "type_defs.GetCodeInterpreterResponseTypeDef" = dataclasses.field()

    codeInterpreterId = field("codeInterpreterId")
    codeInterpreterArn = field("codeInterpreterArn")
    name = field("name")
    description = field("description")
    executionRoleArn = field("executionRoleArn")

    @cached_property
    def networkConfiguration(self):  # pragma: no cover
        return CodeInterpreterNetworkConfigurationOutput.make_one(
            self.boto3_raw_data["networkConfiguration"]
        )

    status = field("status")
    failureReason = field("failureReason")
    createdAt = field("createdAt")
    lastUpdatedAt = field("lastUpdatedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCodeInterpreterResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCodeInterpreterResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAgentRuntimeResponse:
    boto3_raw_data: "type_defs.GetAgentRuntimeResponseTypeDef" = dataclasses.field()

    agentRuntimeArn = field("agentRuntimeArn")

    @cached_property
    def workloadIdentityDetails(self):  # pragma: no cover
        return WorkloadIdentityDetails.make_one(
            self.boto3_raw_data["workloadIdentityDetails"]
        )

    agentRuntimeName = field("agentRuntimeName")
    description = field("description")
    agentRuntimeId = field("agentRuntimeId")
    agentRuntimeVersion = field("agentRuntimeVersion")
    createdAt = field("createdAt")
    lastUpdatedAt = field("lastUpdatedAt")
    roleArn = field("roleArn")

    @cached_property
    def agentRuntimeArtifact(self):  # pragma: no cover
        return AgentRuntimeArtifact.make_one(
            self.boto3_raw_data["agentRuntimeArtifact"]
        )

    @cached_property
    def networkConfiguration(self):  # pragma: no cover
        return NetworkConfigurationOutput.make_one(
            self.boto3_raw_data["networkConfiguration"]
        )

    @cached_property
    def protocolConfiguration(self):  # pragma: no cover
        return ProtocolConfiguration.make_one(
            self.boto3_raw_data["protocolConfiguration"]
        )

    environmentVariables = field("environmentVariables")

    @cached_property
    def authorizerConfiguration(self):  # pragma: no cover
        return AuthorizerConfigurationOutput.make_one(
            self.boto3_raw_data["authorizerConfiguration"]
        )

    @cached_property
    def requestHeaderConfiguration(self):  # pragma: no cover
        return RequestHeaderConfigurationOutput.make_one(
            self.boto3_raw_data["requestHeaderConfiguration"]
        )

    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAgentRuntimeResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAgentRuntimeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CredentialProviderConfigurationOutput:
    boto3_raw_data: "type_defs.CredentialProviderConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    credentialProviderType = field("credentialProviderType")

    @cached_property
    def credentialProvider(self):  # pragma: no cover
        return CredentialProviderOutput.make_one(
            self.boto3_raw_data["credentialProvider"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CredentialProviderConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CredentialProviderConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyConsolidationConfiguration:
    boto3_raw_data: "type_defs.ModifyConsolidationConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def customConsolidationConfiguration(self):  # pragma: no cover
        return CustomConsolidationConfigurationInput.make_one(
            self.boto3_raw_data["customConsolidationConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ModifyConsolidationConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyConsolidationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConsolidationConfiguration:
    boto3_raw_data: "type_defs.ConsolidationConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def customConsolidationConfiguration(self):  # pragma: no cover
        return CustomConsolidationConfiguration.make_one(
            self.boto3_raw_data["customConsolidationConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConsolidationConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConsolidationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyExtractionConfiguration:
    boto3_raw_data: "type_defs.ModifyExtractionConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def customExtractionConfiguration(self):  # pragma: no cover
        return CustomExtractionConfigurationInput.make_one(
            self.boto3_raw_data["customExtractionConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ModifyExtractionConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyExtractionConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomConfigurationInput:
    boto3_raw_data: "type_defs.CustomConfigurationInputTypeDef" = dataclasses.field()

    @cached_property
    def semanticOverride(self):  # pragma: no cover
        return SemanticOverrideConfigurationInput.make_one(
            self.boto3_raw_data["semanticOverride"]
        )

    @cached_property
    def summaryOverride(self):  # pragma: no cover
        return SummaryOverrideConfigurationInput.make_one(
            self.boto3_raw_data["summaryOverride"]
        )

    @cached_property
    def userPreferenceOverride(self):  # pragma: no cover
        return UserPreferenceOverrideConfigurationInput.make_one(
            self.boto3_raw_data["userPreferenceOverride"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CustomConfigurationInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomConfigurationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExtractionConfiguration:
    boto3_raw_data: "type_defs.ExtractionConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def customExtractionConfiguration(self):  # pragma: no cover
        return CustomExtractionConfiguration.make_one(
            self.boto3_raw_data["customExtractionConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExtractionConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExtractionConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateGatewayResponse:
    boto3_raw_data: "type_defs.CreateGatewayResponseTypeDef" = dataclasses.field()

    gatewayArn = field("gatewayArn")
    gatewayId = field("gatewayId")
    gatewayUrl = field("gatewayUrl")
    createdAt = field("createdAt")
    updatedAt = field("updatedAt")
    status = field("status")
    statusReasons = field("statusReasons")
    name = field("name")
    description = field("description")
    roleArn = field("roleArn")
    protocolType = field("protocolType")

    @cached_property
    def protocolConfiguration(self):  # pragma: no cover
        return GatewayProtocolConfigurationOutput.make_one(
            self.boto3_raw_data["protocolConfiguration"]
        )

    authorizerType = field("authorizerType")

    @cached_property
    def authorizerConfiguration(self):  # pragma: no cover
        return AuthorizerConfigurationOutput.make_one(
            self.boto3_raw_data["authorizerConfiguration"]
        )

    kmsKeyArn = field("kmsKeyArn")

    @cached_property
    def workloadIdentityDetails(self):  # pragma: no cover
        return WorkloadIdentityDetails.make_one(
            self.boto3_raw_data["workloadIdentityDetails"]
        )

    exceptionLevel = field("exceptionLevel")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateGatewayResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateGatewayResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetGatewayResponse:
    boto3_raw_data: "type_defs.GetGatewayResponseTypeDef" = dataclasses.field()

    gatewayArn = field("gatewayArn")
    gatewayId = field("gatewayId")
    gatewayUrl = field("gatewayUrl")
    createdAt = field("createdAt")
    updatedAt = field("updatedAt")
    status = field("status")
    statusReasons = field("statusReasons")
    name = field("name")
    description = field("description")
    roleArn = field("roleArn")
    protocolType = field("protocolType")

    @cached_property
    def protocolConfiguration(self):  # pragma: no cover
        return GatewayProtocolConfigurationOutput.make_one(
            self.boto3_raw_data["protocolConfiguration"]
        )

    authorizerType = field("authorizerType")

    @cached_property
    def authorizerConfiguration(self):  # pragma: no cover
        return AuthorizerConfigurationOutput.make_one(
            self.boto3_raw_data["authorizerConfiguration"]
        )

    kmsKeyArn = field("kmsKeyArn")

    @cached_property
    def workloadIdentityDetails(self):  # pragma: no cover
        return WorkloadIdentityDetails.make_one(
            self.boto3_raw_data["workloadIdentityDetails"]
        )

    exceptionLevel = field("exceptionLevel")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetGatewayResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetGatewayResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateGatewayResponse:
    boto3_raw_data: "type_defs.UpdateGatewayResponseTypeDef" = dataclasses.field()

    gatewayArn = field("gatewayArn")
    gatewayId = field("gatewayId")
    gatewayUrl = field("gatewayUrl")
    createdAt = field("createdAt")
    updatedAt = field("updatedAt")
    status = field("status")
    statusReasons = field("statusReasons")
    name = field("name")
    description = field("description")
    roleArn = field("roleArn")
    protocolType = field("protocolType")

    @cached_property
    def protocolConfiguration(self):  # pragma: no cover
        return GatewayProtocolConfigurationOutput.make_one(
            self.boto3_raw_data["protocolConfiguration"]
        )

    authorizerType = field("authorizerType")

    @cached_property
    def authorizerConfiguration(self):  # pragma: no cover
        return AuthorizerConfigurationOutput.make_one(
            self.boto3_raw_data["authorizerConfiguration"]
        )

    kmsKeyArn = field("kmsKeyArn")

    @cached_property
    def workloadIdentityDetails(self):  # pragma: no cover
        return WorkloadIdentityDetails.make_one(
            self.boto3_raw_data["workloadIdentityDetails"]
        )

    exceptionLevel = field("exceptionLevel")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateGatewayResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateGatewayResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CredentialProvider:
    boto3_raw_data: "type_defs.CredentialProviderTypeDef" = dataclasses.field()

    oauthCredentialProvider = field("oauthCredentialProvider")

    @cached_property
    def apiKeyCredentialProvider(self):  # pragma: no cover
        return ApiKeyCredentialProvider.make_one(
            self.boto3_raw_data["apiKeyCredentialProvider"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CredentialProviderTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CredentialProviderTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomOauth2ProviderConfigOutput:
    boto3_raw_data: "type_defs.CustomOauth2ProviderConfigOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def oauthDiscovery(self):  # pragma: no cover
        return Oauth2DiscoveryOutput.make_one(self.boto3_raw_data["oauthDiscovery"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CustomOauth2ProviderConfigOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomOauth2ProviderConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GithubOauth2ProviderConfigOutput:
    boto3_raw_data: "type_defs.GithubOauth2ProviderConfigOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def oauthDiscovery(self):  # pragma: no cover
        return Oauth2DiscoveryOutput.make_one(self.boto3_raw_data["oauthDiscovery"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GithubOauth2ProviderConfigOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GithubOauth2ProviderConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GoogleOauth2ProviderConfigOutput:
    boto3_raw_data: "type_defs.GoogleOauth2ProviderConfigOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def oauthDiscovery(self):  # pragma: no cover
        return Oauth2DiscoveryOutput.make_one(self.boto3_raw_data["oauthDiscovery"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GoogleOauth2ProviderConfigOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GoogleOauth2ProviderConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MicrosoftOauth2ProviderConfigOutput:
    boto3_raw_data: "type_defs.MicrosoftOauth2ProviderConfigOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def oauthDiscovery(self):  # pragma: no cover
        return Oauth2DiscoveryOutput.make_one(self.boto3_raw_data["oauthDiscovery"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MicrosoftOauth2ProviderConfigOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MicrosoftOauth2ProviderConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SalesforceOauth2ProviderConfigOutput:
    boto3_raw_data: "type_defs.SalesforceOauth2ProviderConfigOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def oauthDiscovery(self):  # pragma: no cover
        return Oauth2DiscoveryOutput.make_one(self.boto3_raw_data["oauthDiscovery"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SalesforceOauth2ProviderConfigOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SalesforceOauth2ProviderConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SlackOauth2ProviderConfigOutput:
    boto3_raw_data: "type_defs.SlackOauth2ProviderConfigOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def oauthDiscovery(self):  # pragma: no cover
        return Oauth2DiscoveryOutput.make_one(self.boto3_raw_data["oauthDiscovery"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SlackOauth2ProviderConfigOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SlackOauth2ProviderConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Oauth2Discovery:
    boto3_raw_data: "type_defs.Oauth2DiscoveryTypeDef" = dataclasses.field()

    discoveryUrl = field("discoveryUrl")
    authorizationServerMetadata = field("authorizationServerMetadata")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.Oauth2DiscoveryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.Oauth2DiscoveryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBrowserResponse:
    boto3_raw_data: "type_defs.GetBrowserResponseTypeDef" = dataclasses.field()

    browserId = field("browserId")
    browserArn = field("browserArn")
    name = field("name")
    description = field("description")
    executionRoleArn = field("executionRoleArn")

    @cached_property
    def networkConfiguration(self):  # pragma: no cover
        return BrowserNetworkConfigurationOutput.make_one(
            self.boto3_raw_data["networkConfiguration"]
        )

    @cached_property
    def recording(self):  # pragma: no cover
        return RecordingConfig.make_one(self.boto3_raw_data["recording"])

    status = field("status")
    failureReason = field("failureReason")
    createdAt = field("createdAt")
    lastUpdatedAt = field("lastUpdatedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBrowserResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBrowserResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ToolSchemaOutput:
    boto3_raw_data: "type_defs.ToolSchemaOutputTypeDef" = dataclasses.field()

    @cached_property
    def s3(self):  # pragma: no cover
        return S3Configuration.make_one(self.boto3_raw_data["s3"])

    @cached_property
    def inlinePayload(self):  # pragma: no cover
        return ToolDefinitionOutput.make_many(self.boto3_raw_data["inlinePayload"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ToolSchemaOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ToolSchemaOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ToolSchema:
    boto3_raw_data: "type_defs.ToolSchemaTypeDef" = dataclasses.field()

    @cached_property
    def s3(self):  # pragma: no cover
        return S3Configuration.make_one(self.boto3_raw_data["s3"])

    @cached_property
    def inlinePayload(self):  # pragma: no cover
        return ToolDefinition.make_many(self.boto3_raw_data["inlinePayload"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ToolSchemaTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ToolSchemaTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBrowserRequest:
    boto3_raw_data: "type_defs.CreateBrowserRequestTypeDef" = dataclasses.field()

    name = field("name")
    networkConfiguration = field("networkConfiguration")
    description = field("description")
    executionRoleArn = field("executionRoleArn")

    @cached_property
    def recording(self):  # pragma: no cover
        return RecordingConfig.make_one(self.boto3_raw_data["recording"])

    clientToken = field("clientToken")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateBrowserRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBrowserRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCodeInterpreterRequest:
    boto3_raw_data: "type_defs.CreateCodeInterpreterRequestTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    networkConfiguration = field("networkConfiguration")
    description = field("description")
    executionRoleArn = field("executionRoleArn")
    clientToken = field("clientToken")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateCodeInterpreterRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCodeInterpreterRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAgentRuntimeRequest:
    boto3_raw_data: "type_defs.CreateAgentRuntimeRequestTypeDef" = dataclasses.field()

    agentRuntimeName = field("agentRuntimeName")

    @cached_property
    def agentRuntimeArtifact(self):  # pragma: no cover
        return AgentRuntimeArtifact.make_one(
            self.boto3_raw_data["agentRuntimeArtifact"]
        )

    roleArn = field("roleArn")
    networkConfiguration = field("networkConfiguration")
    description = field("description")

    @cached_property
    def protocolConfiguration(self):  # pragma: no cover
        return ProtocolConfiguration.make_one(
            self.boto3_raw_data["protocolConfiguration"]
        )

    clientToken = field("clientToken")
    environmentVariables = field("environmentVariables")
    authorizerConfiguration = field("authorizerConfiguration")
    requestHeaderConfiguration = field("requestHeaderConfiguration")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAgentRuntimeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAgentRuntimeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAgentRuntimeRequest:
    boto3_raw_data: "type_defs.UpdateAgentRuntimeRequestTypeDef" = dataclasses.field()

    agentRuntimeId = field("agentRuntimeId")

    @cached_property
    def agentRuntimeArtifact(self):  # pragma: no cover
        return AgentRuntimeArtifact.make_one(
            self.boto3_raw_data["agentRuntimeArtifact"]
        )

    roleArn = field("roleArn")
    networkConfiguration = field("networkConfiguration")
    description = field("description")

    @cached_property
    def protocolConfiguration(self):  # pragma: no cover
        return ProtocolConfiguration.make_one(
            self.boto3_raw_data["protocolConfiguration"]
        )

    clientToken = field("clientToken")
    environmentVariables = field("environmentVariables")
    authorizerConfiguration = field("authorizerConfiguration")
    requestHeaderConfiguration = field("requestHeaderConfiguration")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAgentRuntimeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAgentRuntimeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyStrategyConfiguration:
    boto3_raw_data: "type_defs.ModifyStrategyConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def extraction(self):  # pragma: no cover
        return ModifyExtractionConfiguration.make_one(self.boto3_raw_data["extraction"])

    @cached_property
    def consolidation(self):  # pragma: no cover
        return ModifyConsolidationConfiguration.make_one(
            self.boto3_raw_data["consolidation"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModifyStrategyConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyStrategyConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomMemoryStrategyInput:
    boto3_raw_data: "type_defs.CustomMemoryStrategyInputTypeDef" = dataclasses.field()

    name = field("name")
    description = field("description")
    namespaces = field("namespaces")

    @cached_property
    def configuration(self):  # pragma: no cover
        return CustomConfigurationInput.make_one(self.boto3_raw_data["configuration"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CustomMemoryStrategyInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomMemoryStrategyInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StrategyConfiguration:
    boto3_raw_data: "type_defs.StrategyConfigurationTypeDef" = dataclasses.field()

    type = field("type")

    @cached_property
    def extraction(self):  # pragma: no cover
        return ExtractionConfiguration.make_one(self.boto3_raw_data["extraction"])

    @cached_property
    def consolidation(self):  # pragma: no cover
        return ConsolidationConfiguration.make_one(self.boto3_raw_data["consolidation"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StrategyConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StrategyConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateGatewayRequest:
    boto3_raw_data: "type_defs.CreateGatewayRequestTypeDef" = dataclasses.field()

    name = field("name")
    roleArn = field("roleArn")
    protocolType = field("protocolType")
    authorizerType = field("authorizerType")
    authorizerConfiguration = field("authorizerConfiguration")
    description = field("description")
    clientToken = field("clientToken")
    protocolConfiguration = field("protocolConfiguration")
    kmsKeyArn = field("kmsKeyArn")
    exceptionLevel = field("exceptionLevel")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateGatewayRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateGatewayRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateGatewayRequest:
    boto3_raw_data: "type_defs.UpdateGatewayRequestTypeDef" = dataclasses.field()

    gatewayIdentifier = field("gatewayIdentifier")
    name = field("name")
    roleArn = field("roleArn")
    protocolType = field("protocolType")
    authorizerType = field("authorizerType")
    authorizerConfiguration = field("authorizerConfiguration")
    description = field("description")
    protocolConfiguration = field("protocolConfiguration")
    kmsKeyArn = field("kmsKeyArn")
    exceptionLevel = field("exceptionLevel")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateGatewayRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateGatewayRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Oauth2ProviderConfigOutput:
    boto3_raw_data: "type_defs.Oauth2ProviderConfigOutputTypeDef" = dataclasses.field()

    @cached_property
    def customOauth2ProviderConfig(self):  # pragma: no cover
        return CustomOauth2ProviderConfigOutput.make_one(
            self.boto3_raw_data["customOauth2ProviderConfig"]
        )

    @cached_property
    def googleOauth2ProviderConfig(self):  # pragma: no cover
        return GoogleOauth2ProviderConfigOutput.make_one(
            self.boto3_raw_data["googleOauth2ProviderConfig"]
        )

    @cached_property
    def githubOauth2ProviderConfig(self):  # pragma: no cover
        return GithubOauth2ProviderConfigOutput.make_one(
            self.boto3_raw_data["githubOauth2ProviderConfig"]
        )

    @cached_property
    def slackOauth2ProviderConfig(self):  # pragma: no cover
        return SlackOauth2ProviderConfigOutput.make_one(
            self.boto3_raw_data["slackOauth2ProviderConfig"]
        )

    @cached_property
    def salesforceOauth2ProviderConfig(self):  # pragma: no cover
        return SalesforceOauth2ProviderConfigOutput.make_one(
            self.boto3_raw_data["salesforceOauth2ProviderConfig"]
        )

    @cached_property
    def microsoftOauth2ProviderConfig(self):  # pragma: no cover
        return MicrosoftOauth2ProviderConfigOutput.make_one(
            self.boto3_raw_data["microsoftOauth2ProviderConfig"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.Oauth2ProviderConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.Oauth2ProviderConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class McpLambdaTargetConfigurationOutput:
    boto3_raw_data: "type_defs.McpLambdaTargetConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    lambdaArn = field("lambdaArn")

    @cached_property
    def toolSchema(self):  # pragma: no cover
        return ToolSchemaOutput.make_one(self.boto3_raw_data["toolSchema"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.McpLambdaTargetConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.McpLambdaTargetConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class McpLambdaTargetConfiguration:
    boto3_raw_data: "type_defs.McpLambdaTargetConfigurationTypeDef" = (
        dataclasses.field()
    )

    lambdaArn = field("lambdaArn")

    @cached_property
    def toolSchema(self):  # pragma: no cover
        return ToolSchema.make_one(self.boto3_raw_data["toolSchema"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.McpLambdaTargetConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.McpLambdaTargetConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyMemoryStrategyInput:
    boto3_raw_data: "type_defs.ModifyMemoryStrategyInputTypeDef" = dataclasses.field()

    memoryStrategyId = field("memoryStrategyId")
    description = field("description")
    namespaces = field("namespaces")

    @cached_property
    def configuration(self):  # pragma: no cover
        return ModifyStrategyConfiguration.make_one(
            self.boto3_raw_data["configuration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModifyMemoryStrategyInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyMemoryStrategyInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MemoryStrategyInput:
    boto3_raw_data: "type_defs.MemoryStrategyInputTypeDef" = dataclasses.field()

    @cached_property
    def semanticMemoryStrategy(self):  # pragma: no cover
        return SemanticMemoryStrategyInput.make_one(
            self.boto3_raw_data["semanticMemoryStrategy"]
        )

    @cached_property
    def summaryMemoryStrategy(self):  # pragma: no cover
        return SummaryMemoryStrategyInput.make_one(
            self.boto3_raw_data["summaryMemoryStrategy"]
        )

    @cached_property
    def userPreferenceMemoryStrategy(self):  # pragma: no cover
        return UserPreferenceMemoryStrategyInput.make_one(
            self.boto3_raw_data["userPreferenceMemoryStrategy"]
        )

    @cached_property
    def customMemoryStrategy(self):  # pragma: no cover
        return CustomMemoryStrategyInput.make_one(
            self.boto3_raw_data["customMemoryStrategy"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MemoryStrategyInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MemoryStrategyInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MemoryStrategy:
    boto3_raw_data: "type_defs.MemoryStrategyTypeDef" = dataclasses.field()

    strategyId = field("strategyId")
    name = field("name")
    type = field("type")
    namespaces = field("namespaces")
    description = field("description")

    @cached_property
    def configuration(self):  # pragma: no cover
        return StrategyConfiguration.make_one(self.boto3_raw_data["configuration"])

    createdAt = field("createdAt")
    updatedAt = field("updatedAt")
    status = field("status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MemoryStrategyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MemoryStrategyTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CredentialProviderConfiguration:
    boto3_raw_data: "type_defs.CredentialProviderConfigurationTypeDef" = (
        dataclasses.field()
    )

    credentialProviderType = field("credentialProviderType")
    credentialProvider = field("credentialProvider")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CredentialProviderConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CredentialProviderConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetOauth2CredentialProviderResponse:
    boto3_raw_data: "type_defs.GetOauth2CredentialProviderResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def clientSecretArn(self):  # pragma: no cover
        return Secret.make_one(self.boto3_raw_data["clientSecretArn"])

    name = field("name")
    credentialProviderArn = field("credentialProviderArn")
    credentialProviderVendor = field("credentialProviderVendor")

    @cached_property
    def oauth2ProviderConfigOutput(self):  # pragma: no cover
        return Oauth2ProviderConfigOutput.make_one(
            self.boto3_raw_data["oauth2ProviderConfigOutput"]
        )

    createdTime = field("createdTime")
    lastUpdatedTime = field("lastUpdatedTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetOauth2CredentialProviderResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetOauth2CredentialProviderResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateOauth2CredentialProviderResponse:
    boto3_raw_data: "type_defs.UpdateOauth2CredentialProviderResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def clientSecretArn(self):  # pragma: no cover
        return Secret.make_one(self.boto3_raw_data["clientSecretArn"])

    name = field("name")
    credentialProviderVendor = field("credentialProviderVendor")
    credentialProviderArn = field("credentialProviderArn")

    @cached_property
    def oauth2ProviderConfigOutput(self):  # pragma: no cover
        return Oauth2ProviderConfigOutput.make_one(
            self.boto3_raw_data["oauth2ProviderConfigOutput"]
        )

    createdTime = field("createdTime")
    lastUpdatedTime = field("lastUpdatedTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateOauth2CredentialProviderResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateOauth2CredentialProviderResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomOauth2ProviderConfigInput:
    boto3_raw_data: "type_defs.CustomOauth2ProviderConfigInputTypeDef" = (
        dataclasses.field()
    )

    oauthDiscovery = field("oauthDiscovery")
    clientId = field("clientId")
    clientSecret = field("clientSecret")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CustomOauth2ProviderConfigInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomOauth2ProviderConfigInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class McpTargetConfigurationOutput:
    boto3_raw_data: "type_defs.McpTargetConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def openApiSchema(self):  # pragma: no cover
        return ApiSchemaConfiguration.make_one(self.boto3_raw_data["openApiSchema"])

    @cached_property
    def smithyModel(self):  # pragma: no cover
        return ApiSchemaConfiguration.make_one(self.boto3_raw_data["smithyModel"])

    @cached_property
    def lambda_(self):  # pragma: no cover
        return McpLambdaTargetConfigurationOutput.make_one(
            self.boto3_raw_data["lambda"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.McpTargetConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.McpTargetConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class McpTargetConfiguration:
    boto3_raw_data: "type_defs.McpTargetConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def openApiSchema(self):  # pragma: no cover
        return ApiSchemaConfiguration.make_one(self.boto3_raw_data["openApiSchema"])

    @cached_property
    def smithyModel(self):  # pragma: no cover
        return ApiSchemaConfiguration.make_one(self.boto3_raw_data["smithyModel"])

    @cached_property
    def lambda_(self):  # pragma: no cover
        return McpLambdaTargetConfiguration.make_one(self.boto3_raw_data["lambda"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.McpTargetConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.McpTargetConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMemoryInput:
    boto3_raw_data: "type_defs.CreateMemoryInputTypeDef" = dataclasses.field()

    name = field("name")
    eventExpiryDuration = field("eventExpiryDuration")
    clientToken = field("clientToken")
    description = field("description")
    encryptionKeyArn = field("encryptionKeyArn")
    memoryExecutionRoleArn = field("memoryExecutionRoleArn")

    @cached_property
    def memoryStrategies(self):  # pragma: no cover
        return MemoryStrategyInput.make_many(self.boto3_raw_data["memoryStrategies"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateMemoryInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMemoryInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyMemoryStrategies:
    boto3_raw_data: "type_defs.ModifyMemoryStrategiesTypeDef" = dataclasses.field()

    @cached_property
    def addMemoryStrategies(self):  # pragma: no cover
        return MemoryStrategyInput.make_many(self.boto3_raw_data["addMemoryStrategies"])

    @cached_property
    def modifyMemoryStrategies(self):  # pragma: no cover
        return ModifyMemoryStrategyInput.make_many(
            self.boto3_raw_data["modifyMemoryStrategies"]
        )

    @cached_property
    def deleteMemoryStrategies(self):  # pragma: no cover
        return DeleteMemoryStrategyInput.make_many(
            self.boto3_raw_data["deleteMemoryStrategies"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModifyMemoryStrategiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyMemoryStrategiesTypeDef"]
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

    arn = field("arn")
    id = field("id")
    name = field("name")
    eventExpiryDuration = field("eventExpiryDuration")
    status = field("status")
    createdAt = field("createdAt")
    updatedAt = field("updatedAt")
    description = field("description")
    encryptionKeyArn = field("encryptionKeyArn")
    memoryExecutionRoleArn = field("memoryExecutionRoleArn")
    failureReason = field("failureReason")

    @cached_property
    def strategies(self):  # pragma: no cover
        return MemoryStrategy.make_many(self.boto3_raw_data["strategies"])

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
class Oauth2ProviderConfigInput:
    boto3_raw_data: "type_defs.Oauth2ProviderConfigInputTypeDef" = dataclasses.field()

    @cached_property
    def customOauth2ProviderConfig(self):  # pragma: no cover
        return CustomOauth2ProviderConfigInput.make_one(
            self.boto3_raw_data["customOauth2ProviderConfig"]
        )

    @cached_property
    def googleOauth2ProviderConfig(self):  # pragma: no cover
        return GoogleOauth2ProviderConfigInput.make_one(
            self.boto3_raw_data["googleOauth2ProviderConfig"]
        )

    @cached_property
    def githubOauth2ProviderConfig(self):  # pragma: no cover
        return GithubOauth2ProviderConfigInput.make_one(
            self.boto3_raw_data["githubOauth2ProviderConfig"]
        )

    @cached_property
    def slackOauth2ProviderConfig(self):  # pragma: no cover
        return SlackOauth2ProviderConfigInput.make_one(
            self.boto3_raw_data["slackOauth2ProviderConfig"]
        )

    @cached_property
    def salesforceOauth2ProviderConfig(self):  # pragma: no cover
        return SalesforceOauth2ProviderConfigInput.make_one(
            self.boto3_raw_data["salesforceOauth2ProviderConfig"]
        )

    @cached_property
    def microsoftOauth2ProviderConfig(self):  # pragma: no cover
        return MicrosoftOauth2ProviderConfigInput.make_one(
            self.boto3_raw_data["microsoftOauth2ProviderConfig"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.Oauth2ProviderConfigInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.Oauth2ProviderConfigInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TargetConfigurationOutput:
    boto3_raw_data: "type_defs.TargetConfigurationOutputTypeDef" = dataclasses.field()

    @cached_property
    def mcp(self):  # pragma: no cover
        return McpTargetConfigurationOutput.make_one(self.boto3_raw_data["mcp"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TargetConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TargetConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TargetConfiguration:
    boto3_raw_data: "type_defs.TargetConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def mcp(self):  # pragma: no cover
        return McpTargetConfiguration.make_one(self.boto3_raw_data["mcp"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TargetConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TargetConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateMemoryInput:
    boto3_raw_data: "type_defs.UpdateMemoryInputTypeDef" = dataclasses.field()

    memoryId = field("memoryId")
    clientToken = field("clientToken")
    description = field("description")
    eventExpiryDuration = field("eventExpiryDuration")
    memoryExecutionRoleArn = field("memoryExecutionRoleArn")

    @cached_property
    def memoryStrategies(self):  # pragma: no cover
        return ModifyMemoryStrategies.make_one(self.boto3_raw_data["memoryStrategies"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateMemoryInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateMemoryInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMemoryOutput:
    boto3_raw_data: "type_defs.CreateMemoryOutputTypeDef" = dataclasses.field()

    @cached_property
    def memory(self):  # pragma: no cover
        return Memory.make_one(self.boto3_raw_data["memory"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateMemoryOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMemoryOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMemoryOutput:
    boto3_raw_data: "type_defs.GetMemoryOutputTypeDef" = dataclasses.field()

    @cached_property
    def memory(self):  # pragma: no cover
        return Memory.make_one(self.boto3_raw_data["memory"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetMemoryOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetMemoryOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateMemoryOutput:
    boto3_raw_data: "type_defs.UpdateMemoryOutputTypeDef" = dataclasses.field()

    @cached_property
    def memory(self):  # pragma: no cover
        return Memory.make_one(self.boto3_raw_data["memory"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateMemoryOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateMemoryOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateOauth2CredentialProviderRequest:
    boto3_raw_data: "type_defs.CreateOauth2CredentialProviderRequestTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    credentialProviderVendor = field("credentialProviderVendor")

    @cached_property
    def oauth2ProviderConfigInput(self):  # pragma: no cover
        return Oauth2ProviderConfigInput.make_one(
            self.boto3_raw_data["oauth2ProviderConfigInput"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateOauth2CredentialProviderRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateOauth2CredentialProviderRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateOauth2CredentialProviderRequest:
    boto3_raw_data: "type_defs.UpdateOauth2CredentialProviderRequestTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    credentialProviderVendor = field("credentialProviderVendor")

    @cached_property
    def oauth2ProviderConfigInput(self):  # pragma: no cover
        return Oauth2ProviderConfigInput.make_one(
            self.boto3_raw_data["oauth2ProviderConfigInput"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateOauth2CredentialProviderRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateOauth2CredentialProviderRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateGatewayTargetResponse:
    boto3_raw_data: "type_defs.CreateGatewayTargetResponseTypeDef" = dataclasses.field()

    gatewayArn = field("gatewayArn")
    targetId = field("targetId")
    createdAt = field("createdAt")
    updatedAt = field("updatedAt")
    status = field("status")
    statusReasons = field("statusReasons")
    name = field("name")
    description = field("description")

    @cached_property
    def targetConfiguration(self):  # pragma: no cover
        return TargetConfigurationOutput.make_one(
            self.boto3_raw_data["targetConfiguration"]
        )

    @cached_property
    def credentialProviderConfigurations(self):  # pragma: no cover
        return CredentialProviderConfigurationOutput.make_many(
            self.boto3_raw_data["credentialProviderConfigurations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateGatewayTargetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateGatewayTargetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetGatewayTargetResponse:
    boto3_raw_data: "type_defs.GetGatewayTargetResponseTypeDef" = dataclasses.field()

    gatewayArn = field("gatewayArn")
    targetId = field("targetId")
    createdAt = field("createdAt")
    updatedAt = field("updatedAt")
    status = field("status")
    statusReasons = field("statusReasons")
    name = field("name")
    description = field("description")

    @cached_property
    def targetConfiguration(self):  # pragma: no cover
        return TargetConfigurationOutput.make_one(
            self.boto3_raw_data["targetConfiguration"]
        )

    @cached_property
    def credentialProviderConfigurations(self):  # pragma: no cover
        return CredentialProviderConfigurationOutput.make_many(
            self.boto3_raw_data["credentialProviderConfigurations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetGatewayTargetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetGatewayTargetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateGatewayTargetResponse:
    boto3_raw_data: "type_defs.UpdateGatewayTargetResponseTypeDef" = dataclasses.field()

    gatewayArn = field("gatewayArn")
    targetId = field("targetId")
    createdAt = field("createdAt")
    updatedAt = field("updatedAt")
    status = field("status")
    statusReasons = field("statusReasons")
    name = field("name")
    description = field("description")

    @cached_property
    def targetConfiguration(self):  # pragma: no cover
        return TargetConfigurationOutput.make_one(
            self.boto3_raw_data["targetConfiguration"]
        )

    @cached_property
    def credentialProviderConfigurations(self):  # pragma: no cover
        return CredentialProviderConfigurationOutput.make_many(
            self.boto3_raw_data["credentialProviderConfigurations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateGatewayTargetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateGatewayTargetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateGatewayTargetRequest:
    boto3_raw_data: "type_defs.CreateGatewayTargetRequestTypeDef" = dataclasses.field()

    gatewayIdentifier = field("gatewayIdentifier")
    name = field("name")
    targetConfiguration = field("targetConfiguration")
    credentialProviderConfigurations = field("credentialProviderConfigurations")
    description = field("description")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateGatewayTargetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateGatewayTargetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateGatewayTargetRequest:
    boto3_raw_data: "type_defs.UpdateGatewayTargetRequestTypeDef" = dataclasses.field()

    gatewayIdentifier = field("gatewayIdentifier")
    targetId = field("targetId")
    name = field("name")
    targetConfiguration = field("targetConfiguration")
    credentialProviderConfigurations = field("credentialProviderConfigurations")
    description = field("description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateGatewayTargetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateGatewayTargetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
