# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_apigateway import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AccessLogSettings:
    boto3_raw_data: "type_defs.AccessLogSettingsTypeDef" = dataclasses.field()

    format = field("format")
    destinationArn = field("destinationArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AccessLogSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccessLogSettingsTypeDef"]
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
class ThrottleSettings:
    boto3_raw_data: "type_defs.ThrottleSettingsTypeDef" = dataclasses.field()

    burstLimit = field("burstLimit")
    rateLimit = field("rateLimit")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ThrottleSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ThrottleSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApiKey:
    boto3_raw_data: "type_defs.ApiKeyTypeDef" = dataclasses.field()

    id = field("id")
    value = field("value")
    name = field("name")
    customerId = field("customerId")
    description = field("description")
    enabled = field("enabled")
    createdDate = field("createdDate")
    lastUpdatedDate = field("lastUpdatedDate")
    stageKeys = field("stageKeys")
    tags = field("tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ApiKeyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ApiKeyTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Authorizer:
    boto3_raw_data: "type_defs.AuthorizerTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")
    type = field("type")
    providerARNs = field("providerARNs")
    authType = field("authType")
    authorizerUri = field("authorizerUri")
    authorizerCredentials = field("authorizerCredentials")
    identitySource = field("identitySource")
    identityValidationExpression = field("identityValidationExpression")
    authorizerResultTtlInSeconds = field("authorizerResultTtlInSeconds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AuthorizerTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AuthorizerTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BasePathMapping:
    boto3_raw_data: "type_defs.BasePathMappingTypeDef" = dataclasses.field()

    basePath = field("basePath")
    restApiId = field("restApiId")
    stage = field("stage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BasePathMappingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BasePathMappingTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CanarySettingsOutput:
    boto3_raw_data: "type_defs.CanarySettingsOutputTypeDef" = dataclasses.field()

    percentTraffic = field("percentTraffic")
    deploymentId = field("deploymentId")
    stageVariableOverrides = field("stageVariableOverrides")
    useStageCache = field("useStageCache")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CanarySettingsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CanarySettingsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CanarySettings:
    boto3_raw_data: "type_defs.CanarySettingsTypeDef" = dataclasses.field()

    percentTraffic = field("percentTraffic")
    deploymentId = field("deploymentId")
    stageVariableOverrides = field("stageVariableOverrides")
    useStageCache = field("useStageCache")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CanarySettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CanarySettingsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClientCertificate:
    boto3_raw_data: "type_defs.ClientCertificateTypeDef" = dataclasses.field()

    clientCertificateId = field("clientCertificateId")
    description = field("description")
    pemEncodedCertificate = field("pemEncodedCertificate")
    createdDate = field("createdDate")
    expirationDate = field("expirationDate")
    tags = field("tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ClientCertificateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClientCertificateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StageKey:
    boto3_raw_data: "type_defs.StageKeyTypeDef" = dataclasses.field()

    restApiId = field("restApiId")
    stageName = field("stageName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StageKeyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StageKeyTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAuthorizerRequest:
    boto3_raw_data: "type_defs.CreateAuthorizerRequestTypeDef" = dataclasses.field()

    restApiId = field("restApiId")
    name = field("name")
    type = field("type")
    providerARNs = field("providerARNs")
    authType = field("authType")
    authorizerUri = field("authorizerUri")
    authorizerCredentials = field("authorizerCredentials")
    identitySource = field("identitySource")
    identityValidationExpression = field("identityValidationExpression")
    authorizerResultTtlInSeconds = field("authorizerResultTtlInSeconds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAuthorizerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAuthorizerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBasePathMappingRequest:
    boto3_raw_data: "type_defs.CreateBasePathMappingRequestTypeDef" = (
        dataclasses.field()
    )

    domainName = field("domainName")
    restApiId = field("restApiId")
    domainNameId = field("domainNameId")
    basePath = field("basePath")
    stage = field("stage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateBasePathMappingRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBasePathMappingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeploymentCanarySettings:
    boto3_raw_data: "type_defs.DeploymentCanarySettingsTypeDef" = dataclasses.field()

    percentTraffic = field("percentTraffic")
    stageVariableOverrides = field("stageVariableOverrides")
    useStageCache = field("useStageCache")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeploymentCanarySettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeploymentCanarySettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentationPartLocation:
    boto3_raw_data: "type_defs.DocumentationPartLocationTypeDef" = dataclasses.field()

    type = field("type")
    path = field("path")
    method = field("method")
    statusCode = field("statusCode")
    name = field("name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DocumentationPartLocationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentationPartLocationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDocumentationVersionRequest:
    boto3_raw_data: "type_defs.CreateDocumentationVersionRequestTypeDef" = (
        dataclasses.field()
    )

    restApiId = field("restApiId")
    documentationVersion = field("documentationVersion")
    stageName = field("stageName")
    description = field("description")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateDocumentationVersionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDocumentationVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDomainNameAccessAssociationRequest:
    boto3_raw_data: "type_defs.CreateDomainNameAccessAssociationRequestTypeDef" = (
        dataclasses.field()
    )

    domainNameArn = field("domainNameArn")
    accessAssociationSourceType = field("accessAssociationSourceType")
    accessAssociationSource = field("accessAssociationSource")
    tags = field("tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateDomainNameAccessAssociationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDomainNameAccessAssociationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MutualTlsAuthenticationInput:
    boto3_raw_data: "type_defs.MutualTlsAuthenticationInputTypeDef" = (
        dataclasses.field()
    )

    truststoreUri = field("truststoreUri")
    truststoreVersion = field("truststoreVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MutualTlsAuthenticationInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MutualTlsAuthenticationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateModelRequest:
    boto3_raw_data: "type_defs.CreateModelRequestTypeDef" = dataclasses.field()

    restApiId = field("restApiId")
    name = field("name")
    contentType = field("contentType")
    description = field("description")
    schema = field("schema")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateModelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateModelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRequestValidatorRequest:
    boto3_raw_data: "type_defs.CreateRequestValidatorRequestTypeDef" = (
        dataclasses.field()
    )

    restApiId = field("restApiId")
    name = field("name")
    validateRequestBody = field("validateRequestBody")
    validateRequestParameters = field("validateRequestParameters")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateRequestValidatorRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRequestValidatorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateResourceRequest:
    boto3_raw_data: "type_defs.CreateResourceRequestTypeDef" = dataclasses.field()

    restApiId = field("restApiId")
    parentId = field("parentId")
    pathPart = field("pathPart")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateResourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateUsagePlanKeyRequest:
    boto3_raw_data: "type_defs.CreateUsagePlanKeyRequestTypeDef" = dataclasses.field()

    usagePlanId = field("usagePlanId")
    keyId = field("keyId")
    keyType = field("keyType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateUsagePlanKeyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateUsagePlanKeyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QuotaSettings:
    boto3_raw_data: "type_defs.QuotaSettingsTypeDef" = dataclasses.field()

    limit = field("limit")
    offset = field("offset")
    period = field("period")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.QuotaSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.QuotaSettingsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateVpcLinkRequest:
    boto3_raw_data: "type_defs.CreateVpcLinkRequestTypeDef" = dataclasses.field()

    name = field("name")
    targetArns = field("targetArns")
    description = field("description")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateVpcLinkRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateVpcLinkRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteApiKeyRequest:
    boto3_raw_data: "type_defs.DeleteApiKeyRequestTypeDef" = dataclasses.field()

    apiKey = field("apiKey")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteApiKeyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteApiKeyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAuthorizerRequest:
    boto3_raw_data: "type_defs.DeleteAuthorizerRequestTypeDef" = dataclasses.field()

    restApiId = field("restApiId")
    authorizerId = field("authorizerId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAuthorizerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAuthorizerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBasePathMappingRequest:
    boto3_raw_data: "type_defs.DeleteBasePathMappingRequestTypeDef" = (
        dataclasses.field()
    )

    domainName = field("domainName")
    basePath = field("basePath")
    domainNameId = field("domainNameId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteBasePathMappingRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBasePathMappingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteClientCertificateRequest:
    boto3_raw_data: "type_defs.DeleteClientCertificateRequestTypeDef" = (
        dataclasses.field()
    )

    clientCertificateId = field("clientCertificateId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteClientCertificateRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteClientCertificateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDeploymentRequest:
    boto3_raw_data: "type_defs.DeleteDeploymentRequestTypeDef" = dataclasses.field()

    restApiId = field("restApiId")
    deploymentId = field("deploymentId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDeploymentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDeploymentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDocumentationPartRequest:
    boto3_raw_data: "type_defs.DeleteDocumentationPartRequestTypeDef" = (
        dataclasses.field()
    )

    restApiId = field("restApiId")
    documentationPartId = field("documentationPartId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteDocumentationPartRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDocumentationPartRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDocumentationVersionRequest:
    boto3_raw_data: "type_defs.DeleteDocumentationVersionRequestTypeDef" = (
        dataclasses.field()
    )

    restApiId = field("restApiId")
    documentationVersion = field("documentationVersion")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteDocumentationVersionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDocumentationVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDomainNameAccessAssociationRequest:
    boto3_raw_data: "type_defs.DeleteDomainNameAccessAssociationRequestTypeDef" = (
        dataclasses.field()
    )

    domainNameAccessAssociationArn = field("domainNameAccessAssociationArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteDomainNameAccessAssociationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDomainNameAccessAssociationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDomainNameRequest:
    boto3_raw_data: "type_defs.DeleteDomainNameRequestTypeDef" = dataclasses.field()

    domainName = field("domainName")
    domainNameId = field("domainNameId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDomainNameRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDomainNameRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteGatewayResponseRequest:
    boto3_raw_data: "type_defs.DeleteGatewayResponseRequestTypeDef" = (
        dataclasses.field()
    )

    restApiId = field("restApiId")
    responseType = field("responseType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteGatewayResponseRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteGatewayResponseRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteIntegrationRequest:
    boto3_raw_data: "type_defs.DeleteIntegrationRequestTypeDef" = dataclasses.field()

    restApiId = field("restApiId")
    resourceId = field("resourceId")
    httpMethod = field("httpMethod")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteIntegrationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteIntegrationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteIntegrationResponseRequest:
    boto3_raw_data: "type_defs.DeleteIntegrationResponseRequestTypeDef" = (
        dataclasses.field()
    )

    restApiId = field("restApiId")
    resourceId = field("resourceId")
    httpMethod = field("httpMethod")
    statusCode = field("statusCode")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteIntegrationResponseRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteIntegrationResponseRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteMethodRequest:
    boto3_raw_data: "type_defs.DeleteMethodRequestTypeDef" = dataclasses.field()

    restApiId = field("restApiId")
    resourceId = field("resourceId")
    httpMethod = field("httpMethod")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteMethodRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteMethodRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteMethodResponseRequest:
    boto3_raw_data: "type_defs.DeleteMethodResponseRequestTypeDef" = dataclasses.field()

    restApiId = field("restApiId")
    resourceId = field("resourceId")
    httpMethod = field("httpMethod")
    statusCode = field("statusCode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteMethodResponseRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteMethodResponseRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteModelRequest:
    boto3_raw_data: "type_defs.DeleteModelRequestTypeDef" = dataclasses.field()

    restApiId = field("restApiId")
    modelName = field("modelName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteModelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteModelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRequestValidatorRequest:
    boto3_raw_data: "type_defs.DeleteRequestValidatorRequestTypeDef" = (
        dataclasses.field()
    )

    restApiId = field("restApiId")
    requestValidatorId = field("requestValidatorId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteRequestValidatorRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRequestValidatorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteResourceRequest:
    boto3_raw_data: "type_defs.DeleteResourceRequestTypeDef" = dataclasses.field()

    restApiId = field("restApiId")
    resourceId = field("resourceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteResourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRestApiRequest:
    boto3_raw_data: "type_defs.DeleteRestApiRequestTypeDef" = dataclasses.field()

    restApiId = field("restApiId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteRestApiRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRestApiRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteStageRequest:
    boto3_raw_data: "type_defs.DeleteStageRequestTypeDef" = dataclasses.field()

    restApiId = field("restApiId")
    stageName = field("stageName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteStageRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteStageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteUsagePlanKeyRequest:
    boto3_raw_data: "type_defs.DeleteUsagePlanKeyRequestTypeDef" = dataclasses.field()

    usagePlanId = field("usagePlanId")
    keyId = field("keyId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteUsagePlanKeyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteUsagePlanKeyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteUsagePlanRequest:
    boto3_raw_data: "type_defs.DeleteUsagePlanRequestTypeDef" = dataclasses.field()

    usagePlanId = field("usagePlanId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteUsagePlanRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteUsagePlanRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteVpcLinkRequest:
    boto3_raw_data: "type_defs.DeleteVpcLinkRequestTypeDef" = dataclasses.field()

    vpcLinkId = field("vpcLinkId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteVpcLinkRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteVpcLinkRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MethodSnapshot:
    boto3_raw_data: "type_defs.MethodSnapshotTypeDef" = dataclasses.field()

    authorizationType = field("authorizationType")
    apiKeyRequired = field("apiKeyRequired")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MethodSnapshotTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MethodSnapshotTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentationVersion:
    boto3_raw_data: "type_defs.DocumentationVersionTypeDef" = dataclasses.field()

    version = field("version")
    createdDate = field("createdDate")
    description = field("description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DocumentationVersionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentationVersionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DomainNameAccessAssociation:
    boto3_raw_data: "type_defs.DomainNameAccessAssociationTypeDef" = dataclasses.field()

    domainNameAccessAssociationArn = field("domainNameAccessAssociationArn")
    domainNameArn = field("domainNameArn")
    accessAssociationSourceType = field("accessAssociationSourceType")
    accessAssociationSource = field("accessAssociationSource")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DomainNameAccessAssociationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DomainNameAccessAssociationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EndpointConfigurationOutput:
    boto3_raw_data: "type_defs.EndpointConfigurationOutputTypeDef" = dataclasses.field()

    types = field("types")
    ipAddressType = field("ipAddressType")
    vpcEndpointIds = field("vpcEndpointIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EndpointConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EndpointConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MutualTlsAuthentication:
    boto3_raw_data: "type_defs.MutualTlsAuthenticationTypeDef" = dataclasses.field()

    truststoreUri = field("truststoreUri")
    truststoreVersion = field("truststoreVersion")
    truststoreWarnings = field("truststoreWarnings")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MutualTlsAuthenticationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MutualTlsAuthenticationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EndpointConfiguration:
    boto3_raw_data: "type_defs.EndpointConfigurationTypeDef" = dataclasses.field()

    types = field("types")
    ipAddressType = field("ipAddressType")
    vpcEndpointIds = field("vpcEndpointIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EndpointConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EndpointConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FlushStageAuthorizersCacheRequest:
    boto3_raw_data: "type_defs.FlushStageAuthorizersCacheRequestTypeDef" = (
        dataclasses.field()
    )

    restApiId = field("restApiId")
    stageName = field("stageName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.FlushStageAuthorizersCacheRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FlushStageAuthorizersCacheRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FlushStageCacheRequest:
    boto3_raw_data: "type_defs.FlushStageCacheRequestTypeDef" = dataclasses.field()

    restApiId = field("restApiId")
    stageName = field("stageName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FlushStageCacheRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FlushStageCacheRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GatewayResponse:
    boto3_raw_data: "type_defs.GatewayResponseTypeDef" = dataclasses.field()

    responseType = field("responseType")
    statusCode = field("statusCode")
    responseParameters = field("responseParameters")
    responseTemplates = field("responseTemplates")
    defaultResponse = field("defaultResponse")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GatewayResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GatewayResponseTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GenerateClientCertificateRequest:
    boto3_raw_data: "type_defs.GenerateClientCertificateRequestTypeDef" = (
        dataclasses.field()
    )

    description = field("description")
    tags = field("tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GenerateClientCertificateRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GenerateClientCertificateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetApiKeyRequest:
    boto3_raw_data: "type_defs.GetApiKeyRequestTypeDef" = dataclasses.field()

    apiKey = field("apiKey")
    includeValue = field("includeValue")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetApiKeyRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetApiKeyRequestTypeDef"]
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
class GetApiKeysRequest:
    boto3_raw_data: "type_defs.GetApiKeysRequestTypeDef" = dataclasses.field()

    position = field("position")
    limit = field("limit")
    nameQuery = field("nameQuery")
    customerId = field("customerId")
    includeValues = field("includeValues")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetApiKeysRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetApiKeysRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAuthorizerRequest:
    boto3_raw_data: "type_defs.GetAuthorizerRequestTypeDef" = dataclasses.field()

    restApiId = field("restApiId")
    authorizerId = field("authorizerId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAuthorizerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAuthorizerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAuthorizersRequest:
    boto3_raw_data: "type_defs.GetAuthorizersRequestTypeDef" = dataclasses.field()

    restApiId = field("restApiId")
    position = field("position")
    limit = field("limit")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAuthorizersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAuthorizersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBasePathMappingRequest:
    boto3_raw_data: "type_defs.GetBasePathMappingRequestTypeDef" = dataclasses.field()

    domainName = field("domainName")
    basePath = field("basePath")
    domainNameId = field("domainNameId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBasePathMappingRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBasePathMappingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBasePathMappingsRequest:
    boto3_raw_data: "type_defs.GetBasePathMappingsRequestTypeDef" = dataclasses.field()

    domainName = field("domainName")
    domainNameId = field("domainNameId")
    position = field("position")
    limit = field("limit")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBasePathMappingsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBasePathMappingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetClientCertificateRequest:
    boto3_raw_data: "type_defs.GetClientCertificateRequestTypeDef" = dataclasses.field()

    clientCertificateId = field("clientCertificateId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetClientCertificateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetClientCertificateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetClientCertificatesRequest:
    boto3_raw_data: "type_defs.GetClientCertificatesRequestTypeDef" = (
        dataclasses.field()
    )

    position = field("position")
    limit = field("limit")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetClientCertificatesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetClientCertificatesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDeploymentRequest:
    boto3_raw_data: "type_defs.GetDeploymentRequestTypeDef" = dataclasses.field()

    restApiId = field("restApiId")
    deploymentId = field("deploymentId")
    embed = field("embed")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDeploymentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDeploymentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDeploymentsRequest:
    boto3_raw_data: "type_defs.GetDeploymentsRequestTypeDef" = dataclasses.field()

    restApiId = field("restApiId")
    position = field("position")
    limit = field("limit")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDeploymentsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDeploymentsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDocumentationPartRequest:
    boto3_raw_data: "type_defs.GetDocumentationPartRequestTypeDef" = dataclasses.field()

    restApiId = field("restApiId")
    documentationPartId = field("documentationPartId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDocumentationPartRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDocumentationPartRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDocumentationPartsRequest:
    boto3_raw_data: "type_defs.GetDocumentationPartsRequestTypeDef" = (
        dataclasses.field()
    )

    restApiId = field("restApiId")
    type = field("type")
    nameQuery = field("nameQuery")
    path = field("path")
    position = field("position")
    limit = field("limit")
    locationStatus = field("locationStatus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDocumentationPartsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDocumentationPartsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDocumentationVersionRequest:
    boto3_raw_data: "type_defs.GetDocumentationVersionRequestTypeDef" = (
        dataclasses.field()
    )

    restApiId = field("restApiId")
    documentationVersion = field("documentationVersion")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetDocumentationVersionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDocumentationVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDocumentationVersionsRequest:
    boto3_raw_data: "type_defs.GetDocumentationVersionsRequestTypeDef" = (
        dataclasses.field()
    )

    restApiId = field("restApiId")
    position = field("position")
    limit = field("limit")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetDocumentationVersionsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDocumentationVersionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDomainNameAccessAssociationsRequest:
    boto3_raw_data: "type_defs.GetDomainNameAccessAssociationsRequestTypeDef" = (
        dataclasses.field()
    )

    position = field("position")
    limit = field("limit")
    resourceOwner = field("resourceOwner")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetDomainNameAccessAssociationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDomainNameAccessAssociationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDomainNameRequest:
    boto3_raw_data: "type_defs.GetDomainNameRequestTypeDef" = dataclasses.field()

    domainName = field("domainName")
    domainNameId = field("domainNameId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDomainNameRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDomainNameRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDomainNamesRequest:
    boto3_raw_data: "type_defs.GetDomainNamesRequestTypeDef" = dataclasses.field()

    position = field("position")
    limit = field("limit")
    resourceOwner = field("resourceOwner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDomainNamesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDomainNamesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetExportRequest:
    boto3_raw_data: "type_defs.GetExportRequestTypeDef" = dataclasses.field()

    restApiId = field("restApiId")
    stageName = field("stageName")
    exportType = field("exportType")
    parameters = field("parameters")
    accepts = field("accepts")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetExportRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetExportRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetGatewayResponseRequest:
    boto3_raw_data: "type_defs.GetGatewayResponseRequestTypeDef" = dataclasses.field()

    restApiId = field("restApiId")
    responseType = field("responseType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetGatewayResponseRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetGatewayResponseRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetGatewayResponsesRequest:
    boto3_raw_data: "type_defs.GetGatewayResponsesRequestTypeDef" = dataclasses.field()

    restApiId = field("restApiId")
    position = field("position")
    limit = field("limit")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetGatewayResponsesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetGatewayResponsesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetIntegrationRequest:
    boto3_raw_data: "type_defs.GetIntegrationRequestTypeDef" = dataclasses.field()

    restApiId = field("restApiId")
    resourceId = field("resourceId")
    httpMethod = field("httpMethod")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetIntegrationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetIntegrationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetIntegrationResponseRequest:
    boto3_raw_data: "type_defs.GetIntegrationResponseRequestTypeDef" = (
        dataclasses.field()
    )

    restApiId = field("restApiId")
    resourceId = field("resourceId")
    httpMethod = field("httpMethod")
    statusCode = field("statusCode")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetIntegrationResponseRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetIntegrationResponseRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMethodRequest:
    boto3_raw_data: "type_defs.GetMethodRequestTypeDef" = dataclasses.field()

    restApiId = field("restApiId")
    resourceId = field("resourceId")
    httpMethod = field("httpMethod")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetMethodRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMethodRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMethodResponseRequest:
    boto3_raw_data: "type_defs.GetMethodResponseRequestTypeDef" = dataclasses.field()

    restApiId = field("restApiId")
    resourceId = field("resourceId")
    httpMethod = field("httpMethod")
    statusCode = field("statusCode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMethodResponseRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMethodResponseRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetModelRequest:
    boto3_raw_data: "type_defs.GetModelRequestTypeDef" = dataclasses.field()

    restApiId = field("restApiId")
    modelName = field("modelName")
    flatten = field("flatten")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetModelRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetModelRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetModelTemplateRequest:
    boto3_raw_data: "type_defs.GetModelTemplateRequestTypeDef" = dataclasses.field()

    restApiId = field("restApiId")
    modelName = field("modelName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetModelTemplateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetModelTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetModelsRequest:
    boto3_raw_data: "type_defs.GetModelsRequestTypeDef" = dataclasses.field()

    restApiId = field("restApiId")
    position = field("position")
    limit = field("limit")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetModelsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetModelsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRequestValidatorRequest:
    boto3_raw_data: "type_defs.GetRequestValidatorRequestTypeDef" = dataclasses.field()

    restApiId = field("restApiId")
    requestValidatorId = field("requestValidatorId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetRequestValidatorRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRequestValidatorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRequestValidatorsRequest:
    boto3_raw_data: "type_defs.GetRequestValidatorsRequestTypeDef" = dataclasses.field()

    restApiId = field("restApiId")
    position = field("position")
    limit = field("limit")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetRequestValidatorsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRequestValidatorsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResourceRequest:
    boto3_raw_data: "type_defs.GetResourceRequestTypeDef" = dataclasses.field()

    restApiId = field("restApiId")
    resourceId = field("resourceId")
    embed = field("embed")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetResourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResourcesRequest:
    boto3_raw_data: "type_defs.GetResourcesRequestTypeDef" = dataclasses.field()

    restApiId = field("restApiId")
    position = field("position")
    limit = field("limit")
    embed = field("embed")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetResourcesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResourcesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRestApiRequest:
    boto3_raw_data: "type_defs.GetRestApiRequestTypeDef" = dataclasses.field()

    restApiId = field("restApiId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetRestApiRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRestApiRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRestApisRequest:
    boto3_raw_data: "type_defs.GetRestApisRequestTypeDef" = dataclasses.field()

    position = field("position")
    limit = field("limit")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetRestApisRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRestApisRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSdkRequest:
    boto3_raw_data: "type_defs.GetSdkRequestTypeDef" = dataclasses.field()

    restApiId = field("restApiId")
    stageName = field("stageName")
    sdkType = field("sdkType")
    parameters = field("parameters")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetSdkRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetSdkRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSdkTypeRequest:
    boto3_raw_data: "type_defs.GetSdkTypeRequestTypeDef" = dataclasses.field()

    id = field("id")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetSdkTypeRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSdkTypeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSdkTypesRequest:
    boto3_raw_data: "type_defs.GetSdkTypesRequestTypeDef" = dataclasses.field()

    position = field("position")
    limit = field("limit")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSdkTypesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSdkTypesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetStageRequest:
    boto3_raw_data: "type_defs.GetStageRequestTypeDef" = dataclasses.field()

    restApiId = field("restApiId")
    stageName = field("stageName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetStageRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetStageRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetStagesRequest:
    boto3_raw_data: "type_defs.GetStagesRequestTypeDef" = dataclasses.field()

    restApiId = field("restApiId")
    deploymentId = field("deploymentId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetStagesRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetStagesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTagsRequest:
    boto3_raw_data: "type_defs.GetTagsRequestTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")
    position = field("position")
    limit = field("limit")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetTagsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetTagsRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetUsagePlanKeyRequest:
    boto3_raw_data: "type_defs.GetUsagePlanKeyRequestTypeDef" = dataclasses.field()

    usagePlanId = field("usagePlanId")
    keyId = field("keyId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetUsagePlanKeyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetUsagePlanKeyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetUsagePlanKeysRequest:
    boto3_raw_data: "type_defs.GetUsagePlanKeysRequestTypeDef" = dataclasses.field()

    usagePlanId = field("usagePlanId")
    position = field("position")
    limit = field("limit")
    nameQuery = field("nameQuery")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetUsagePlanKeysRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetUsagePlanKeysRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetUsagePlanRequest:
    boto3_raw_data: "type_defs.GetUsagePlanRequestTypeDef" = dataclasses.field()

    usagePlanId = field("usagePlanId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetUsagePlanRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetUsagePlanRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetUsagePlansRequest:
    boto3_raw_data: "type_defs.GetUsagePlansRequestTypeDef" = dataclasses.field()

    position = field("position")
    keyId = field("keyId")
    limit = field("limit")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetUsagePlansRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetUsagePlansRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetUsageRequest:
    boto3_raw_data: "type_defs.GetUsageRequestTypeDef" = dataclasses.field()

    usagePlanId = field("usagePlanId")
    startDate = field("startDate")
    endDate = field("endDate")
    keyId = field("keyId")
    position = field("position")
    limit = field("limit")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetUsageRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetUsageRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetVpcLinkRequest:
    boto3_raw_data: "type_defs.GetVpcLinkRequestTypeDef" = dataclasses.field()

    vpcLinkId = field("vpcLinkId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetVpcLinkRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetVpcLinkRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetVpcLinksRequest:
    boto3_raw_data: "type_defs.GetVpcLinksRequestTypeDef" = dataclasses.field()

    position = field("position")
    limit = field("limit")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetVpcLinksRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetVpcLinksRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IntegrationResponse:
    boto3_raw_data: "type_defs.IntegrationResponseTypeDef" = dataclasses.field()

    statusCode = field("statusCode")
    selectionPattern = field("selectionPattern")
    responseParameters = field("responseParameters")
    responseTemplates = field("responseTemplates")
    contentHandling = field("contentHandling")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IntegrationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IntegrationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TlsConfig:
    boto3_raw_data: "type_defs.TlsConfigTypeDef" = dataclasses.field()

    insecureSkipVerification = field("insecureSkipVerification")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TlsConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TlsConfigTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MethodResponse:
    boto3_raw_data: "type_defs.MethodResponseTypeDef" = dataclasses.field()

    statusCode = field("statusCode")
    responseParameters = field("responseParameters")
    responseModels = field("responseModels")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MethodResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MethodResponseTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MethodSetting:
    boto3_raw_data: "type_defs.MethodSettingTypeDef" = dataclasses.field()

    metricsEnabled = field("metricsEnabled")
    loggingLevel = field("loggingLevel")
    dataTraceEnabled = field("dataTraceEnabled")
    throttlingBurstLimit = field("throttlingBurstLimit")
    throttlingRateLimit = field("throttlingRateLimit")
    cachingEnabled = field("cachingEnabled")
    cacheTtlInSeconds = field("cacheTtlInSeconds")
    cacheDataEncrypted = field("cacheDataEncrypted")
    requireAuthorizationForCacheControl = field("requireAuthorizationForCacheControl")
    unauthorizedCacheControlHeaderStrategy = field(
        "unauthorizedCacheControlHeaderStrategy"
    )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MethodSettingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MethodSettingTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Model:
    boto3_raw_data: "type_defs.ModelTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")
    description = field("description")
    schema = field("schema")
    contentType = field("contentType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ModelTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ModelTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PatchOperation:
    boto3_raw_data: "type_defs.PatchOperationTypeDef" = dataclasses.field()

    op = field("op")
    path = field("path")
    value = field("value")
    from_ = field("from")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PatchOperationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PatchOperationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutGatewayResponseRequest:
    boto3_raw_data: "type_defs.PutGatewayResponseRequestTypeDef" = dataclasses.field()

    restApiId = field("restApiId")
    responseType = field("responseType")
    statusCode = field("statusCode")
    responseParameters = field("responseParameters")
    responseTemplates = field("responseTemplates")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutGatewayResponseRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutGatewayResponseRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutIntegrationResponseRequest:
    boto3_raw_data: "type_defs.PutIntegrationResponseRequestTypeDef" = (
        dataclasses.field()
    )

    restApiId = field("restApiId")
    resourceId = field("resourceId")
    httpMethod = field("httpMethod")
    statusCode = field("statusCode")
    selectionPattern = field("selectionPattern")
    responseParameters = field("responseParameters")
    responseTemplates = field("responseTemplates")
    contentHandling = field("contentHandling")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PutIntegrationResponseRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutIntegrationResponseRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutMethodRequest:
    boto3_raw_data: "type_defs.PutMethodRequestTypeDef" = dataclasses.field()

    restApiId = field("restApiId")
    resourceId = field("resourceId")
    httpMethod = field("httpMethod")
    authorizationType = field("authorizationType")
    authorizerId = field("authorizerId")
    apiKeyRequired = field("apiKeyRequired")
    operationName = field("operationName")
    requestParameters = field("requestParameters")
    requestModels = field("requestModels")
    requestValidatorId = field("requestValidatorId")
    authorizationScopes = field("authorizationScopes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PutMethodRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutMethodRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutMethodResponseRequest:
    boto3_raw_data: "type_defs.PutMethodResponseRequestTypeDef" = dataclasses.field()

    restApiId = field("restApiId")
    resourceId = field("resourceId")
    httpMethod = field("httpMethod")
    statusCode = field("statusCode")
    responseParameters = field("responseParameters")
    responseModels = field("responseModels")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutMethodResponseRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutMethodResponseRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RejectDomainNameAccessAssociationRequest:
    boto3_raw_data: "type_defs.RejectDomainNameAccessAssociationRequestTypeDef" = (
        dataclasses.field()
    )

    domainNameAccessAssociationArn = field("domainNameAccessAssociationArn")
    domainNameArn = field("domainNameArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RejectDomainNameAccessAssociationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RejectDomainNameAccessAssociationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RequestValidator:
    boto3_raw_data: "type_defs.RequestValidatorTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")
    validateRequestBody = field("validateRequestBody")
    validateRequestParameters = field("validateRequestParameters")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RequestValidatorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RequestValidatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SdkConfigurationProperty:
    boto3_raw_data: "type_defs.SdkConfigurationPropertyTypeDef" = dataclasses.field()

    name = field("name")
    friendlyName = field("friendlyName")
    description = field("description")
    required = field("required")
    defaultValue = field("defaultValue")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SdkConfigurationPropertyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SdkConfigurationPropertyTypeDef"]
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
class TestInvokeAuthorizerRequest:
    boto3_raw_data: "type_defs.TestInvokeAuthorizerRequestTypeDef" = dataclasses.field()

    restApiId = field("restApiId")
    authorizerId = field("authorizerId")
    headers = field("headers")
    multiValueHeaders = field("multiValueHeaders")
    pathWithQueryString = field("pathWithQueryString")
    body = field("body")
    stageVariables = field("stageVariables")
    additionalContext = field("additionalContext")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TestInvokeAuthorizerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TestInvokeAuthorizerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestInvokeMethodRequest:
    boto3_raw_data: "type_defs.TestInvokeMethodRequestTypeDef" = dataclasses.field()

    restApiId = field("restApiId")
    resourceId = field("resourceId")
    httpMethod = field("httpMethod")
    pathWithQueryString = field("pathWithQueryString")
    body = field("body")
    headers = field("headers")
    multiValueHeaders = field("multiValueHeaders")
    clientCertificateId = field("clientCertificateId")
    stageVariables = field("stageVariables")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TestInvokeMethodRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TestInvokeMethodRequestTypeDef"]
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
class UsagePlanKey:
    boto3_raw_data: "type_defs.UsagePlanKeyTypeDef" = dataclasses.field()

    id = field("id")
    type = field("type")
    value = field("value")
    name = field("name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UsagePlanKeyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UsagePlanKeyTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VpcLink:
    boto3_raw_data: "type_defs.VpcLinkTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")
    description = field("description")
    targetArns = field("targetArns")
    status = field("status")
    statusMessage = field("statusMessage")
    tags = field("tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VpcLinkTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VpcLinkTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApiKeyIds:
    boto3_raw_data: "type_defs.ApiKeyIdsTypeDef" = dataclasses.field()

    ids = field("ids")
    warnings = field("warnings")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ApiKeyIdsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ApiKeyIdsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApiKeyResponse:
    boto3_raw_data: "type_defs.ApiKeyResponseTypeDef" = dataclasses.field()

    id = field("id")
    value = field("value")
    name = field("name")
    customerId = field("customerId")
    description = field("description")
    enabled = field("enabled")
    createdDate = field("createdDate")
    lastUpdatedDate = field("lastUpdatedDate")
    stageKeys = field("stageKeys")
    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ApiKeyResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ApiKeyResponseTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AuthorizerResponse:
    boto3_raw_data: "type_defs.AuthorizerResponseTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")
    type = field("type")
    providerARNs = field("providerARNs")
    authType = field("authType")
    authorizerUri = field("authorizerUri")
    authorizerCredentials = field("authorizerCredentials")
    identitySource = field("identitySource")
    identityValidationExpression = field("identityValidationExpression")
    authorizerResultTtlInSeconds = field("authorizerResultTtlInSeconds")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AuthorizerResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AuthorizerResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BasePathMappingResponse:
    boto3_raw_data: "type_defs.BasePathMappingResponseTypeDef" = dataclasses.field()

    basePath = field("basePath")
    restApiId = field("restApiId")
    stage = field("stage")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BasePathMappingResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BasePathMappingResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClientCertificateResponse:
    boto3_raw_data: "type_defs.ClientCertificateResponseTypeDef" = dataclasses.field()

    clientCertificateId = field("clientCertificateId")
    description = field("description")
    pemEncodedCertificate = field("pemEncodedCertificate")
    createdDate = field("createdDate")
    expirationDate = field("expirationDate")
    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ClientCertificateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClientCertificateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentationPartIds:
    boto3_raw_data: "type_defs.DocumentationPartIdsTypeDef" = dataclasses.field()

    ids = field("ids")
    warnings = field("warnings")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DocumentationPartIdsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentationPartIdsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentationVersionResponse:
    boto3_raw_data: "type_defs.DocumentationVersionResponseTypeDef" = (
        dataclasses.field()
    )

    version = field("version")
    createdDate = field("createdDate")
    description = field("description")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DocumentationVersionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentationVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DomainNameAccessAssociationResponse:
    boto3_raw_data: "type_defs.DomainNameAccessAssociationResponseTypeDef" = (
        dataclasses.field()
    )

    domainNameAccessAssociationArn = field("domainNameAccessAssociationArn")
    domainNameArn = field("domainNameArn")
    accessAssociationSourceType = field("accessAssociationSourceType")
    accessAssociationSource = field("accessAssociationSource")
    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DomainNameAccessAssociationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DomainNameAccessAssociationResponseTypeDef"]
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
class ExportResponse:
    boto3_raw_data: "type_defs.ExportResponseTypeDef" = dataclasses.field()

    contentType = field("contentType")
    contentDisposition = field("contentDisposition")
    body = field("body")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExportResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ExportResponseTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GatewayResponseResponse:
    boto3_raw_data: "type_defs.GatewayResponseResponseTypeDef" = dataclasses.field()

    responseType = field("responseType")
    statusCode = field("statusCode")
    responseParameters = field("responseParameters")
    responseTemplates = field("responseTemplates")
    defaultResponse = field("defaultResponse")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GatewayResponseResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GatewayResponseResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IntegrationResponseResponse:
    boto3_raw_data: "type_defs.IntegrationResponseResponseTypeDef" = dataclasses.field()

    statusCode = field("statusCode")
    selectionPattern = field("selectionPattern")
    responseParameters = field("responseParameters")
    responseTemplates = field("responseTemplates")
    contentHandling = field("contentHandling")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IntegrationResponseResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IntegrationResponseResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MethodResponseResponse:
    boto3_raw_data: "type_defs.MethodResponseResponseTypeDef" = dataclasses.field()

    statusCode = field("statusCode")
    responseParameters = field("responseParameters")
    responseModels = field("responseModels")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MethodResponseResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MethodResponseResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModelResponse:
    boto3_raw_data: "type_defs.ModelResponseTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")
    description = field("description")
    schema = field("schema")
    contentType = field("contentType")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ModelResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ModelResponseTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RequestValidatorResponse:
    boto3_raw_data: "type_defs.RequestValidatorResponseTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")
    validateRequestBody = field("validateRequestBody")
    validateRequestParameters = field("validateRequestParameters")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RequestValidatorResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RequestValidatorResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SdkResponse:
    boto3_raw_data: "type_defs.SdkResponseTypeDef" = dataclasses.field()

    contentType = field("contentType")
    contentDisposition = field("contentDisposition")
    body = field("body")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SdkResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SdkResponseTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Tags:
    boto3_raw_data: "type_defs.TagsTypeDef" = dataclasses.field()

    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TagsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TagsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Template:
    boto3_raw_data: "type_defs.TemplateTypeDef" = dataclasses.field()

    value = field("value")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TemplateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TemplateTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestInvokeAuthorizerResponse:
    boto3_raw_data: "type_defs.TestInvokeAuthorizerResponseTypeDef" = (
        dataclasses.field()
    )

    clientStatus = field("clientStatus")
    log = field("log")
    latency = field("latency")
    principalId = field("principalId")
    policy = field("policy")
    authorization = field("authorization")
    claims = field("claims")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TestInvokeAuthorizerResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TestInvokeAuthorizerResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestInvokeMethodResponse:
    boto3_raw_data: "type_defs.TestInvokeMethodResponseTypeDef" = dataclasses.field()

    status = field("status")
    body = field("body")
    headers = field("headers")
    multiValueHeaders = field("multiValueHeaders")
    log = field("log")
    latency = field("latency")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TestInvokeMethodResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TestInvokeMethodResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UsagePlanKeyResponse:
    boto3_raw_data: "type_defs.UsagePlanKeyResponseTypeDef" = dataclasses.field()

    id = field("id")
    type = field("type")
    value = field("value")
    name = field("name")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UsagePlanKeyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UsagePlanKeyResponseTypeDef"]
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

    usagePlanId = field("usagePlanId")
    startDate = field("startDate")
    endDate = field("endDate")
    position = field("position")
    items = field("items")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

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
class VpcLinkResponse:
    boto3_raw_data: "type_defs.VpcLinkResponseTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")
    description = field("description")
    targetArns = field("targetArns")
    status = field("status")
    statusMessage = field("statusMessage")
    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VpcLinkResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VpcLinkResponseTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Account:
    boto3_raw_data: "type_defs.AccountTypeDef" = dataclasses.field()

    cloudwatchRoleArn = field("cloudwatchRoleArn")

    @cached_property
    def throttleSettings(self):  # pragma: no cover
        return ThrottleSettings.make_one(self.boto3_raw_data["throttleSettings"])

    features = field("features")
    apiKeyVersion = field("apiKeyVersion")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AccountTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AccountTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApiStageOutput:
    boto3_raw_data: "type_defs.ApiStageOutputTypeDef" = dataclasses.field()

    apiId = field("apiId")
    stage = field("stage")
    throttle = field("throttle")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ApiStageOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ApiStageOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApiStage:
    boto3_raw_data: "type_defs.ApiStageTypeDef" = dataclasses.field()

    apiId = field("apiId")
    stage = field("stage")
    throttle = field("throttle")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ApiStageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ApiStageTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApiKeys:
    boto3_raw_data: "type_defs.ApiKeysTypeDef" = dataclasses.field()

    warnings = field("warnings")
    position = field("position")

    @cached_property
    def items(self):  # pragma: no cover
        return ApiKey.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ApiKeysTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ApiKeysTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Authorizers:
    boto3_raw_data: "type_defs.AuthorizersTypeDef" = dataclasses.field()

    position = field("position")

    @cached_property
    def items(self):  # pragma: no cover
        return Authorizer.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AuthorizersTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AuthorizersTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BasePathMappings:
    boto3_raw_data: "type_defs.BasePathMappingsTypeDef" = dataclasses.field()

    position = field("position")

    @cached_property
    def items(self):  # pragma: no cover
        return BasePathMapping.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BasePathMappingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BasePathMappingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportApiKeysRequest:
    boto3_raw_data: "type_defs.ImportApiKeysRequestTypeDef" = dataclasses.field()

    body = field("body")
    format = field("format")
    failOnWarnings = field("failOnWarnings")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImportApiKeysRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportApiKeysRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportDocumentationPartsRequest:
    boto3_raw_data: "type_defs.ImportDocumentationPartsRequestTypeDef" = (
        dataclasses.field()
    )

    restApiId = field("restApiId")
    body = field("body")
    mode = field("mode")
    failOnWarnings = field("failOnWarnings")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ImportDocumentationPartsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportDocumentationPartsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportRestApiRequest:
    boto3_raw_data: "type_defs.ImportRestApiRequestTypeDef" = dataclasses.field()

    body = field("body")
    failOnWarnings = field("failOnWarnings")
    parameters = field("parameters")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImportRestApiRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportRestApiRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutRestApiRequest:
    boto3_raw_data: "type_defs.PutRestApiRequestTypeDef" = dataclasses.field()

    restApiId = field("restApiId")
    body = field("body")
    mode = field("mode")
    failOnWarnings = field("failOnWarnings")
    parameters = field("parameters")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PutRestApiRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutRestApiRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClientCertificates:
    boto3_raw_data: "type_defs.ClientCertificatesTypeDef" = dataclasses.field()

    position = field("position")

    @cached_property
    def items(self):  # pragma: no cover
        return ClientCertificate.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ClientCertificatesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClientCertificatesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateApiKeyRequest:
    boto3_raw_data: "type_defs.CreateApiKeyRequestTypeDef" = dataclasses.field()

    name = field("name")
    description = field("description")
    enabled = field("enabled")
    generateDistinctId = field("generateDistinctId")
    value = field("value")

    @cached_property
    def stageKeys(self):  # pragma: no cover
        return StageKey.make_many(self.boto3_raw_data["stageKeys"])

    customerId = field("customerId")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateApiKeyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateApiKeyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDeploymentRequest:
    boto3_raw_data: "type_defs.CreateDeploymentRequestTypeDef" = dataclasses.field()

    restApiId = field("restApiId")
    stageName = field("stageName")
    stageDescription = field("stageDescription")
    description = field("description")
    cacheClusterEnabled = field("cacheClusterEnabled")
    cacheClusterSize = field("cacheClusterSize")
    variables = field("variables")

    @cached_property
    def canarySettings(self):  # pragma: no cover
        return DeploymentCanarySettings.make_one(self.boto3_raw_data["canarySettings"])

    tracingEnabled = field("tracingEnabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDeploymentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDeploymentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDocumentationPartRequest:
    boto3_raw_data: "type_defs.CreateDocumentationPartRequestTypeDef" = (
        dataclasses.field()
    )

    restApiId = field("restApiId")

    @cached_property
    def location(self):  # pragma: no cover
        return DocumentationPartLocation.make_one(self.boto3_raw_data["location"])

    properties = field("properties")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateDocumentationPartRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDocumentationPartRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentationPartResponse:
    boto3_raw_data: "type_defs.DocumentationPartResponseTypeDef" = dataclasses.field()

    id = field("id")

    @cached_property
    def location(self):  # pragma: no cover
        return DocumentationPartLocation.make_one(self.boto3_raw_data["location"])

    properties = field("properties")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DocumentationPartResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentationPartResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentationPart:
    boto3_raw_data: "type_defs.DocumentationPartTypeDef" = dataclasses.field()

    id = field("id")

    @cached_property
    def location(self):  # pragma: no cover
        return DocumentationPartLocation.make_one(self.boto3_raw_data["location"])

    properties = field("properties")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DocumentationPartTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentationPartTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeploymentResponse:
    boto3_raw_data: "type_defs.DeploymentResponseTypeDef" = dataclasses.field()

    id = field("id")
    description = field("description")
    createdDate = field("createdDate")
    apiSummary = field("apiSummary")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeploymentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeploymentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Deployment:
    boto3_raw_data: "type_defs.DeploymentTypeDef" = dataclasses.field()

    id = field("id")
    description = field("description")
    createdDate = field("createdDate")
    apiSummary = field("apiSummary")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeploymentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DeploymentTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentationVersions:
    boto3_raw_data: "type_defs.DocumentationVersionsTypeDef" = dataclasses.field()

    position = field("position")

    @cached_property
    def items(self):  # pragma: no cover
        return DocumentationVersion.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DocumentationVersionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentationVersionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DomainNameAccessAssociations:
    boto3_raw_data: "type_defs.DomainNameAccessAssociationsTypeDef" = (
        dataclasses.field()
    )

    position = field("position")

    @cached_property
    def items(self):  # pragma: no cover
        return DomainNameAccessAssociation.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DomainNameAccessAssociationsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DomainNameAccessAssociationsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RestApiResponse:
    boto3_raw_data: "type_defs.RestApiResponseTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")
    description = field("description")
    createdDate = field("createdDate")
    version = field("version")
    warnings = field("warnings")
    binaryMediaTypes = field("binaryMediaTypes")
    minimumCompressionSize = field("minimumCompressionSize")
    apiKeySource = field("apiKeySource")

    @cached_property
    def endpointConfiguration(self):  # pragma: no cover
        return EndpointConfigurationOutput.make_one(
            self.boto3_raw_data["endpointConfiguration"]
        )

    policy = field("policy")
    tags = field("tags")
    disableExecuteApiEndpoint = field("disableExecuteApiEndpoint")
    rootResourceId = field("rootResourceId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RestApiResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RestApiResponseTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RestApi:
    boto3_raw_data: "type_defs.RestApiTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")
    description = field("description")
    createdDate = field("createdDate")
    version = field("version")
    warnings = field("warnings")
    binaryMediaTypes = field("binaryMediaTypes")
    minimumCompressionSize = field("minimumCompressionSize")
    apiKeySource = field("apiKeySource")

    @cached_property
    def endpointConfiguration(self):  # pragma: no cover
        return EndpointConfigurationOutput.make_one(
            self.boto3_raw_data["endpointConfiguration"]
        )

    policy = field("policy")
    tags = field("tags")
    disableExecuteApiEndpoint = field("disableExecuteApiEndpoint")
    rootResourceId = field("rootResourceId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RestApiTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RestApiTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DomainNameResponse:
    boto3_raw_data: "type_defs.DomainNameResponseTypeDef" = dataclasses.field()

    domainName = field("domainName")
    domainNameId = field("domainNameId")
    domainNameArn = field("domainNameArn")
    certificateName = field("certificateName")
    certificateArn = field("certificateArn")
    certificateUploadDate = field("certificateUploadDate")
    regionalDomainName = field("regionalDomainName")
    regionalHostedZoneId = field("regionalHostedZoneId")
    regionalCertificateName = field("regionalCertificateName")
    regionalCertificateArn = field("regionalCertificateArn")
    distributionDomainName = field("distributionDomainName")
    distributionHostedZoneId = field("distributionHostedZoneId")

    @cached_property
    def endpointConfiguration(self):  # pragma: no cover
        return EndpointConfigurationOutput.make_one(
            self.boto3_raw_data["endpointConfiguration"]
        )

    domainNameStatus = field("domainNameStatus")
    domainNameStatusMessage = field("domainNameStatusMessage")
    securityPolicy = field("securityPolicy")
    tags = field("tags")

    @cached_property
    def mutualTlsAuthentication(self):  # pragma: no cover
        return MutualTlsAuthentication.make_one(
            self.boto3_raw_data["mutualTlsAuthentication"]
        )

    ownershipVerificationCertificateArn = field("ownershipVerificationCertificateArn")
    managementPolicy = field("managementPolicy")
    policy = field("policy")
    routingMode = field("routingMode")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DomainNameResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DomainNameResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DomainName:
    boto3_raw_data: "type_defs.DomainNameTypeDef" = dataclasses.field()

    domainName = field("domainName")
    domainNameId = field("domainNameId")
    domainNameArn = field("domainNameArn")
    certificateName = field("certificateName")
    certificateArn = field("certificateArn")
    certificateUploadDate = field("certificateUploadDate")
    regionalDomainName = field("regionalDomainName")
    regionalHostedZoneId = field("regionalHostedZoneId")
    regionalCertificateName = field("regionalCertificateName")
    regionalCertificateArn = field("regionalCertificateArn")
    distributionDomainName = field("distributionDomainName")
    distributionHostedZoneId = field("distributionHostedZoneId")

    @cached_property
    def endpointConfiguration(self):  # pragma: no cover
        return EndpointConfigurationOutput.make_one(
            self.boto3_raw_data["endpointConfiguration"]
        )

    domainNameStatus = field("domainNameStatus")
    domainNameStatusMessage = field("domainNameStatusMessage")
    securityPolicy = field("securityPolicy")
    tags = field("tags")

    @cached_property
    def mutualTlsAuthentication(self):  # pragma: no cover
        return MutualTlsAuthentication.make_one(
            self.boto3_raw_data["mutualTlsAuthentication"]
        )

    ownershipVerificationCertificateArn = field("ownershipVerificationCertificateArn")
    managementPolicy = field("managementPolicy")
    policy = field("policy")
    routingMode = field("routingMode")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DomainNameTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DomainNameTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GatewayResponses:
    boto3_raw_data: "type_defs.GatewayResponsesTypeDef" = dataclasses.field()

    position = field("position")

    @cached_property
    def items(self):  # pragma: no cover
        return GatewayResponse.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GatewayResponsesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GatewayResponsesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetApiKeysRequestPaginate:
    boto3_raw_data: "type_defs.GetApiKeysRequestPaginateTypeDef" = dataclasses.field()

    nameQuery = field("nameQuery")
    customerId = field("customerId")
    includeValues = field("includeValues")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetApiKeysRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetApiKeysRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAuthorizersRequestPaginate:
    boto3_raw_data: "type_defs.GetAuthorizersRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    restApiId = field("restApiId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetAuthorizersRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAuthorizersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBasePathMappingsRequestPaginate:
    boto3_raw_data: "type_defs.GetBasePathMappingsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    domainName = field("domainName")
    domainNameId = field("domainNameId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetBasePathMappingsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBasePathMappingsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetClientCertificatesRequestPaginate:
    boto3_raw_data: "type_defs.GetClientCertificatesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetClientCertificatesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetClientCertificatesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDeploymentsRequestPaginate:
    boto3_raw_data: "type_defs.GetDeploymentsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    restApiId = field("restApiId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetDeploymentsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDeploymentsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDocumentationPartsRequestPaginate:
    boto3_raw_data: "type_defs.GetDocumentationPartsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    restApiId = field("restApiId")
    type = field("type")
    nameQuery = field("nameQuery")
    path = field("path")
    locationStatus = field("locationStatus")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetDocumentationPartsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDocumentationPartsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDocumentationVersionsRequestPaginate:
    boto3_raw_data: "type_defs.GetDocumentationVersionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    restApiId = field("restApiId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetDocumentationVersionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDocumentationVersionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDomainNamesRequestPaginate:
    boto3_raw_data: "type_defs.GetDomainNamesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    resourceOwner = field("resourceOwner")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetDomainNamesRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDomainNamesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetGatewayResponsesRequestPaginate:
    boto3_raw_data: "type_defs.GetGatewayResponsesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    restApiId = field("restApiId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetGatewayResponsesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetGatewayResponsesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetModelsRequestPaginate:
    boto3_raw_data: "type_defs.GetModelsRequestPaginateTypeDef" = dataclasses.field()

    restApiId = field("restApiId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetModelsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetModelsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRequestValidatorsRequestPaginate:
    boto3_raw_data: "type_defs.GetRequestValidatorsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    restApiId = field("restApiId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetRequestValidatorsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRequestValidatorsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResourcesRequestPaginate:
    boto3_raw_data: "type_defs.GetResourcesRequestPaginateTypeDef" = dataclasses.field()

    restApiId = field("restApiId")
    embed = field("embed")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetResourcesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResourcesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRestApisRequestPaginate:
    boto3_raw_data: "type_defs.GetRestApisRequestPaginateTypeDef" = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetRestApisRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRestApisRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSdkTypesRequestPaginate:
    boto3_raw_data: "type_defs.GetSdkTypesRequestPaginateTypeDef" = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSdkTypesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSdkTypesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetUsagePlanKeysRequestPaginate:
    boto3_raw_data: "type_defs.GetUsagePlanKeysRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    usagePlanId = field("usagePlanId")
    nameQuery = field("nameQuery")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetUsagePlanKeysRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetUsagePlanKeysRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetUsagePlansRequestPaginate:
    boto3_raw_data: "type_defs.GetUsagePlansRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    keyId = field("keyId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetUsagePlansRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetUsagePlansRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetUsageRequestPaginate:
    boto3_raw_data: "type_defs.GetUsageRequestPaginateTypeDef" = dataclasses.field()

    usagePlanId = field("usagePlanId")
    startDate = field("startDate")
    endDate = field("endDate")
    keyId = field("keyId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetUsageRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetUsageRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetVpcLinksRequestPaginate:
    boto3_raw_data: "type_defs.GetVpcLinksRequestPaginateTypeDef" = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetVpcLinksRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetVpcLinksRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IntegrationResponseExtra:
    boto3_raw_data: "type_defs.IntegrationResponseExtraTypeDef" = dataclasses.field()

    type = field("type")
    httpMethod = field("httpMethod")
    uri = field("uri")
    connectionType = field("connectionType")
    connectionId = field("connectionId")
    credentials = field("credentials")
    requestParameters = field("requestParameters")
    requestTemplates = field("requestTemplates")
    passthroughBehavior = field("passthroughBehavior")
    contentHandling = field("contentHandling")
    timeoutInMillis = field("timeoutInMillis")
    cacheNamespace = field("cacheNamespace")
    cacheKeyParameters = field("cacheKeyParameters")
    integrationResponses = field("integrationResponses")

    @cached_property
    def tlsConfig(self):  # pragma: no cover
        return TlsConfig.make_one(self.boto3_raw_data["tlsConfig"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IntegrationResponseExtraTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IntegrationResponseExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Integration:
    boto3_raw_data: "type_defs.IntegrationTypeDef" = dataclasses.field()

    type = field("type")
    httpMethod = field("httpMethod")
    uri = field("uri")
    connectionType = field("connectionType")
    connectionId = field("connectionId")
    credentials = field("credentials")
    requestParameters = field("requestParameters")
    requestTemplates = field("requestTemplates")
    passthroughBehavior = field("passthroughBehavior")
    contentHandling = field("contentHandling")
    timeoutInMillis = field("timeoutInMillis")
    cacheNamespace = field("cacheNamespace")
    cacheKeyParameters = field("cacheKeyParameters")
    integrationResponses = field("integrationResponses")

    @cached_property
    def tlsConfig(self):  # pragma: no cover
        return TlsConfig.make_one(self.boto3_raw_data["tlsConfig"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IntegrationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IntegrationTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutIntegrationRequest:
    boto3_raw_data: "type_defs.PutIntegrationRequestTypeDef" = dataclasses.field()

    restApiId = field("restApiId")
    resourceId = field("resourceId")
    httpMethod = field("httpMethod")
    type = field("type")
    integrationHttpMethod = field("integrationHttpMethod")
    uri = field("uri")
    connectionType = field("connectionType")
    connectionId = field("connectionId")
    credentials = field("credentials")
    requestParameters = field("requestParameters")
    requestTemplates = field("requestTemplates")
    passthroughBehavior = field("passthroughBehavior")
    cacheNamespace = field("cacheNamespace")
    cacheKeyParameters = field("cacheKeyParameters")
    contentHandling = field("contentHandling")
    timeoutInMillis = field("timeoutInMillis")

    @cached_property
    def tlsConfig(self):  # pragma: no cover
        return TlsConfig.make_one(self.boto3_raw_data["tlsConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutIntegrationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutIntegrationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StageResponse:
    boto3_raw_data: "type_defs.StageResponseTypeDef" = dataclasses.field()

    deploymentId = field("deploymentId")
    clientCertificateId = field("clientCertificateId")
    stageName = field("stageName")
    description = field("description")
    cacheClusterEnabled = field("cacheClusterEnabled")
    cacheClusterSize = field("cacheClusterSize")
    cacheClusterStatus = field("cacheClusterStatus")
    methodSettings = field("methodSettings")
    variables = field("variables")
    documentationVersion = field("documentationVersion")

    @cached_property
    def accessLogSettings(self):  # pragma: no cover
        return AccessLogSettings.make_one(self.boto3_raw_data["accessLogSettings"])

    @cached_property
    def canarySettings(self):  # pragma: no cover
        return CanarySettingsOutput.make_one(self.boto3_raw_data["canarySettings"])

    tracingEnabled = field("tracingEnabled")
    webAclArn = field("webAclArn")
    tags = field("tags")
    createdDate = field("createdDate")
    lastUpdatedDate = field("lastUpdatedDate")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StageResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StageResponseTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Stage:
    boto3_raw_data: "type_defs.StageTypeDef" = dataclasses.field()

    deploymentId = field("deploymentId")
    clientCertificateId = field("clientCertificateId")
    stageName = field("stageName")
    description = field("description")
    cacheClusterEnabled = field("cacheClusterEnabled")
    cacheClusterSize = field("cacheClusterSize")
    cacheClusterStatus = field("cacheClusterStatus")
    methodSettings = field("methodSettings")
    variables = field("variables")
    documentationVersion = field("documentationVersion")

    @cached_property
    def accessLogSettings(self):  # pragma: no cover
        return AccessLogSettings.make_one(self.boto3_raw_data["accessLogSettings"])

    @cached_property
    def canarySettings(self):  # pragma: no cover
        return CanarySettingsOutput.make_one(self.boto3_raw_data["canarySettings"])

    tracingEnabled = field("tracingEnabled")
    webAclArn = field("webAclArn")
    tags = field("tags")
    createdDate = field("createdDate")
    lastUpdatedDate = field("lastUpdatedDate")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StageTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Models:
    boto3_raw_data: "type_defs.ModelsTypeDef" = dataclasses.field()

    position = field("position")

    @cached_property
    def items(self):  # pragma: no cover
        return Model.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ModelsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ModelsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAccountRequest:
    boto3_raw_data: "type_defs.UpdateAccountRequestTypeDef" = dataclasses.field()

    @cached_property
    def patchOperations(self):  # pragma: no cover
        return PatchOperation.make_many(self.boto3_raw_data["patchOperations"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAccountRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAccountRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateApiKeyRequest:
    boto3_raw_data: "type_defs.UpdateApiKeyRequestTypeDef" = dataclasses.field()

    apiKey = field("apiKey")

    @cached_property
    def patchOperations(self):  # pragma: no cover
        return PatchOperation.make_many(self.boto3_raw_data["patchOperations"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateApiKeyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateApiKeyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAuthorizerRequest:
    boto3_raw_data: "type_defs.UpdateAuthorizerRequestTypeDef" = dataclasses.field()

    restApiId = field("restApiId")
    authorizerId = field("authorizerId")

    @cached_property
    def patchOperations(self):  # pragma: no cover
        return PatchOperation.make_many(self.boto3_raw_data["patchOperations"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAuthorizerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAuthorizerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateBasePathMappingRequest:
    boto3_raw_data: "type_defs.UpdateBasePathMappingRequestTypeDef" = (
        dataclasses.field()
    )

    domainName = field("domainName")
    basePath = field("basePath")
    domainNameId = field("domainNameId")

    @cached_property
    def patchOperations(self):  # pragma: no cover
        return PatchOperation.make_many(self.boto3_raw_data["patchOperations"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateBasePathMappingRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateBasePathMappingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateClientCertificateRequest:
    boto3_raw_data: "type_defs.UpdateClientCertificateRequestTypeDef" = (
        dataclasses.field()
    )

    clientCertificateId = field("clientCertificateId")

    @cached_property
    def patchOperations(self):  # pragma: no cover
        return PatchOperation.make_many(self.boto3_raw_data["patchOperations"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateClientCertificateRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateClientCertificateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDeploymentRequest:
    boto3_raw_data: "type_defs.UpdateDeploymentRequestTypeDef" = dataclasses.field()

    restApiId = field("restApiId")
    deploymentId = field("deploymentId")

    @cached_property
    def patchOperations(self):  # pragma: no cover
        return PatchOperation.make_many(self.boto3_raw_data["patchOperations"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDeploymentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDeploymentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDocumentationPartRequest:
    boto3_raw_data: "type_defs.UpdateDocumentationPartRequestTypeDef" = (
        dataclasses.field()
    )

    restApiId = field("restApiId")
    documentationPartId = field("documentationPartId")

    @cached_property
    def patchOperations(self):  # pragma: no cover
        return PatchOperation.make_many(self.boto3_raw_data["patchOperations"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateDocumentationPartRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDocumentationPartRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDocumentationVersionRequest:
    boto3_raw_data: "type_defs.UpdateDocumentationVersionRequestTypeDef" = (
        dataclasses.field()
    )

    restApiId = field("restApiId")
    documentationVersion = field("documentationVersion")

    @cached_property
    def patchOperations(self):  # pragma: no cover
        return PatchOperation.make_many(self.boto3_raw_data["patchOperations"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateDocumentationVersionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDocumentationVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDomainNameRequest:
    boto3_raw_data: "type_defs.UpdateDomainNameRequestTypeDef" = dataclasses.field()

    domainName = field("domainName")
    domainNameId = field("domainNameId")

    @cached_property
    def patchOperations(self):  # pragma: no cover
        return PatchOperation.make_many(self.boto3_raw_data["patchOperations"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDomainNameRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDomainNameRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateGatewayResponseRequest:
    boto3_raw_data: "type_defs.UpdateGatewayResponseRequestTypeDef" = (
        dataclasses.field()
    )

    restApiId = field("restApiId")
    responseType = field("responseType")

    @cached_property
    def patchOperations(self):  # pragma: no cover
        return PatchOperation.make_many(self.boto3_raw_data["patchOperations"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateGatewayResponseRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateGatewayResponseRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateIntegrationRequest:
    boto3_raw_data: "type_defs.UpdateIntegrationRequestTypeDef" = dataclasses.field()

    restApiId = field("restApiId")
    resourceId = field("resourceId")
    httpMethod = field("httpMethod")

    @cached_property
    def patchOperations(self):  # pragma: no cover
        return PatchOperation.make_many(self.boto3_raw_data["patchOperations"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateIntegrationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateIntegrationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateIntegrationResponseRequest:
    boto3_raw_data: "type_defs.UpdateIntegrationResponseRequestTypeDef" = (
        dataclasses.field()
    )

    restApiId = field("restApiId")
    resourceId = field("resourceId")
    httpMethod = field("httpMethod")
    statusCode = field("statusCode")

    @cached_property
    def patchOperations(self):  # pragma: no cover
        return PatchOperation.make_many(self.boto3_raw_data["patchOperations"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateIntegrationResponseRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateIntegrationResponseRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateMethodRequest:
    boto3_raw_data: "type_defs.UpdateMethodRequestTypeDef" = dataclasses.field()

    restApiId = field("restApiId")
    resourceId = field("resourceId")
    httpMethod = field("httpMethod")

    @cached_property
    def patchOperations(self):  # pragma: no cover
        return PatchOperation.make_many(self.boto3_raw_data["patchOperations"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateMethodRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateMethodRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateMethodResponseRequest:
    boto3_raw_data: "type_defs.UpdateMethodResponseRequestTypeDef" = dataclasses.field()

    restApiId = field("restApiId")
    resourceId = field("resourceId")
    httpMethod = field("httpMethod")
    statusCode = field("statusCode")

    @cached_property
    def patchOperations(self):  # pragma: no cover
        return PatchOperation.make_many(self.boto3_raw_data["patchOperations"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateMethodResponseRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateMethodResponseRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateModelRequest:
    boto3_raw_data: "type_defs.UpdateModelRequestTypeDef" = dataclasses.field()

    restApiId = field("restApiId")
    modelName = field("modelName")

    @cached_property
    def patchOperations(self):  # pragma: no cover
        return PatchOperation.make_many(self.boto3_raw_data["patchOperations"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateModelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateModelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRequestValidatorRequest:
    boto3_raw_data: "type_defs.UpdateRequestValidatorRequestTypeDef" = (
        dataclasses.field()
    )

    restApiId = field("restApiId")
    requestValidatorId = field("requestValidatorId")

    @cached_property
    def patchOperations(self):  # pragma: no cover
        return PatchOperation.make_many(self.boto3_raw_data["patchOperations"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateRequestValidatorRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRequestValidatorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateResourceRequest:
    boto3_raw_data: "type_defs.UpdateResourceRequestTypeDef" = dataclasses.field()

    restApiId = field("restApiId")
    resourceId = field("resourceId")

    @cached_property
    def patchOperations(self):  # pragma: no cover
        return PatchOperation.make_many(self.boto3_raw_data["patchOperations"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateResourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRestApiRequest:
    boto3_raw_data: "type_defs.UpdateRestApiRequestTypeDef" = dataclasses.field()

    restApiId = field("restApiId")

    @cached_property
    def patchOperations(self):  # pragma: no cover
        return PatchOperation.make_many(self.boto3_raw_data["patchOperations"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateRestApiRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRestApiRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateStageRequest:
    boto3_raw_data: "type_defs.UpdateStageRequestTypeDef" = dataclasses.field()

    restApiId = field("restApiId")
    stageName = field("stageName")

    @cached_property
    def patchOperations(self):  # pragma: no cover
        return PatchOperation.make_many(self.boto3_raw_data["patchOperations"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateStageRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateStageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateUsagePlanRequest:
    boto3_raw_data: "type_defs.UpdateUsagePlanRequestTypeDef" = dataclasses.field()

    usagePlanId = field("usagePlanId")

    @cached_property
    def patchOperations(self):  # pragma: no cover
        return PatchOperation.make_many(self.boto3_raw_data["patchOperations"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateUsagePlanRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateUsagePlanRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateUsageRequest:
    boto3_raw_data: "type_defs.UpdateUsageRequestTypeDef" = dataclasses.field()

    usagePlanId = field("usagePlanId")
    keyId = field("keyId")

    @cached_property
    def patchOperations(self):  # pragma: no cover
        return PatchOperation.make_many(self.boto3_raw_data["patchOperations"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateUsageRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateUsageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateVpcLinkRequest:
    boto3_raw_data: "type_defs.UpdateVpcLinkRequestTypeDef" = dataclasses.field()

    vpcLinkId = field("vpcLinkId")

    @cached_property
    def patchOperations(self):  # pragma: no cover
        return PatchOperation.make_many(self.boto3_raw_data["patchOperations"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateVpcLinkRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateVpcLinkRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RequestValidators:
    boto3_raw_data: "type_defs.RequestValidatorsTypeDef" = dataclasses.field()

    position = field("position")

    @cached_property
    def items(self):  # pragma: no cover
        return RequestValidator.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RequestValidatorsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RequestValidatorsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SdkTypeResponse:
    boto3_raw_data: "type_defs.SdkTypeResponseTypeDef" = dataclasses.field()

    id = field("id")
    friendlyName = field("friendlyName")
    description = field("description")

    @cached_property
    def configurationProperties(self):  # pragma: no cover
        return SdkConfigurationProperty.make_many(
            self.boto3_raw_data["configurationProperties"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SdkTypeResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SdkTypeResponseTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SdkType:
    boto3_raw_data: "type_defs.SdkTypeTypeDef" = dataclasses.field()

    id = field("id")
    friendlyName = field("friendlyName")
    description = field("description")

    @cached_property
    def configurationProperties(self):  # pragma: no cover
        return SdkConfigurationProperty.make_many(
            self.boto3_raw_data["configurationProperties"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SdkTypeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SdkTypeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UsagePlanKeys:
    boto3_raw_data: "type_defs.UsagePlanKeysTypeDef" = dataclasses.field()

    position = field("position")

    @cached_property
    def items(self):  # pragma: no cover
        return UsagePlanKey.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UsagePlanKeysTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UsagePlanKeysTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VpcLinks:
    boto3_raw_data: "type_defs.VpcLinksTypeDef" = dataclasses.field()

    position = field("position")

    @cached_property
    def items(self):  # pragma: no cover
        return VpcLink.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VpcLinksTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VpcLinksTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UsagePlanResponse:
    boto3_raw_data: "type_defs.UsagePlanResponseTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")
    description = field("description")

    @cached_property
    def apiStages(self):  # pragma: no cover
        return ApiStageOutput.make_many(self.boto3_raw_data["apiStages"])

    @cached_property
    def throttle(self):  # pragma: no cover
        return ThrottleSettings.make_one(self.boto3_raw_data["throttle"])

    @cached_property
    def quota(self):  # pragma: no cover
        return QuotaSettings.make_one(self.boto3_raw_data["quota"])

    productCode = field("productCode")
    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UsagePlanResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UsagePlanResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UsagePlan:
    boto3_raw_data: "type_defs.UsagePlanTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")
    description = field("description")

    @cached_property
    def apiStages(self):  # pragma: no cover
        return ApiStageOutput.make_many(self.boto3_raw_data["apiStages"])

    @cached_property
    def throttle(self):  # pragma: no cover
        return ThrottleSettings.make_one(self.boto3_raw_data["throttle"])

    @cached_property
    def quota(self):  # pragma: no cover
        return QuotaSettings.make_one(self.boto3_raw_data["quota"])

    productCode = field("productCode")
    tags = field("tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UsagePlanTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UsagePlanTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateStageRequest:
    boto3_raw_data: "type_defs.CreateStageRequestTypeDef" = dataclasses.field()

    restApiId = field("restApiId")
    stageName = field("stageName")
    deploymentId = field("deploymentId")
    description = field("description")
    cacheClusterEnabled = field("cacheClusterEnabled")
    cacheClusterSize = field("cacheClusterSize")
    variables = field("variables")
    documentationVersion = field("documentationVersion")
    canarySettings = field("canarySettings")
    tracingEnabled = field("tracingEnabled")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateStageRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateStageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentationParts:
    boto3_raw_data: "type_defs.DocumentationPartsTypeDef" = dataclasses.field()

    position = field("position")

    @cached_property
    def items(self):  # pragma: no cover
        return DocumentationPart.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DocumentationPartsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentationPartsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Deployments:
    boto3_raw_data: "type_defs.DeploymentsTypeDef" = dataclasses.field()

    position = field("position")

    @cached_property
    def items(self):  # pragma: no cover
        return Deployment.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeploymentsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DeploymentsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RestApis:
    boto3_raw_data: "type_defs.RestApisTypeDef" = dataclasses.field()

    position = field("position")

    @cached_property
    def items(self):  # pragma: no cover
        return RestApi.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RestApisTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RestApisTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DomainNames:
    boto3_raw_data: "type_defs.DomainNamesTypeDef" = dataclasses.field()

    position = field("position")

    @cached_property
    def items(self):  # pragma: no cover
        return DomainName.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DomainNamesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DomainNamesTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDomainNameRequest:
    boto3_raw_data: "type_defs.CreateDomainNameRequestTypeDef" = dataclasses.field()

    domainName = field("domainName")
    certificateName = field("certificateName")
    certificateBody = field("certificateBody")
    certificatePrivateKey = field("certificatePrivateKey")
    certificateChain = field("certificateChain")
    certificateArn = field("certificateArn")
    regionalCertificateName = field("regionalCertificateName")
    regionalCertificateArn = field("regionalCertificateArn")
    endpointConfiguration = field("endpointConfiguration")
    tags = field("tags")
    securityPolicy = field("securityPolicy")

    @cached_property
    def mutualTlsAuthentication(self):  # pragma: no cover
        return MutualTlsAuthenticationInput.make_one(
            self.boto3_raw_data["mutualTlsAuthentication"]
        )

    ownershipVerificationCertificateArn = field("ownershipVerificationCertificateArn")
    policy = field("policy")
    routingMode = field("routingMode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDomainNameRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDomainNameRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRestApiRequest:
    boto3_raw_data: "type_defs.CreateRestApiRequestTypeDef" = dataclasses.field()

    name = field("name")
    description = field("description")
    version = field("version")
    cloneFrom = field("cloneFrom")
    binaryMediaTypes = field("binaryMediaTypes")
    minimumCompressionSize = field("minimumCompressionSize")
    apiKeySource = field("apiKeySource")
    endpointConfiguration = field("endpointConfiguration")
    policy = field("policy")
    tags = field("tags")
    disableExecuteApiEndpoint = field("disableExecuteApiEndpoint")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateRestApiRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRestApiRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MethodResponseExtra:
    boto3_raw_data: "type_defs.MethodResponseExtraTypeDef" = dataclasses.field()

    httpMethod = field("httpMethod")
    authorizationType = field("authorizationType")
    authorizerId = field("authorizerId")
    apiKeyRequired = field("apiKeyRequired")
    requestValidatorId = field("requestValidatorId")
    operationName = field("operationName")
    requestParameters = field("requestParameters")
    requestModels = field("requestModels")
    methodResponses = field("methodResponses")

    @cached_property
    def methodIntegration(self):  # pragma: no cover
        return Integration.make_one(self.boto3_raw_data["methodIntegration"])

    authorizationScopes = field("authorizationScopes")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MethodResponseExtraTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MethodResponseExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Method:
    boto3_raw_data: "type_defs.MethodTypeDef" = dataclasses.field()

    httpMethod = field("httpMethod")
    authorizationType = field("authorizationType")
    authorizerId = field("authorizerId")
    apiKeyRequired = field("apiKeyRequired")
    requestValidatorId = field("requestValidatorId")
    operationName = field("operationName")
    requestParameters = field("requestParameters")
    requestModels = field("requestModels")
    methodResponses = field("methodResponses")

    @cached_property
    def methodIntegration(self):  # pragma: no cover
        return Integration.make_one(self.boto3_raw_data["methodIntegration"])

    authorizationScopes = field("authorizationScopes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MethodTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MethodTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Stages:
    boto3_raw_data: "type_defs.StagesTypeDef" = dataclasses.field()

    @cached_property
    def item(self):  # pragma: no cover
        return Stage.make_many(self.boto3_raw_data["item"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StagesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StagesTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SdkTypes:
    boto3_raw_data: "type_defs.SdkTypesTypeDef" = dataclasses.field()

    position = field("position")

    @cached_property
    def items(self):  # pragma: no cover
        return SdkType.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SdkTypesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SdkTypesTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UsagePlans:
    boto3_raw_data: "type_defs.UsagePlansTypeDef" = dataclasses.field()

    position = field("position")

    @cached_property
    def items(self):  # pragma: no cover
        return UsagePlan.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UsagePlansTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UsagePlansTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateUsagePlanRequest:
    boto3_raw_data: "type_defs.CreateUsagePlanRequestTypeDef" = dataclasses.field()

    name = field("name")
    description = field("description")
    apiStages = field("apiStages")

    @cached_property
    def throttle(self):  # pragma: no cover
        return ThrottleSettings.make_one(self.boto3_raw_data["throttle"])

    @cached_property
    def quota(self):  # pragma: no cover
        return QuotaSettings.make_one(self.boto3_raw_data["quota"])

    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateUsagePlanRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateUsagePlanRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceResponse:
    boto3_raw_data: "type_defs.ResourceResponseTypeDef" = dataclasses.field()

    id = field("id")
    parentId = field("parentId")
    pathPart = field("pathPart")
    path = field("path")
    resourceMethods = field("resourceMethods")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResourceResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Resource:
    boto3_raw_data: "type_defs.ResourceTypeDef" = dataclasses.field()

    id = field("id")
    parentId = field("parentId")
    pathPart = field("pathPart")
    path = field("path")
    resourceMethods = field("resourceMethods")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResourceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Resources:
    boto3_raw_data: "type_defs.ResourcesTypeDef" = dataclasses.field()

    position = field("position")

    @cached_property
    def items(self):  # pragma: no cover
        return Resource.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResourcesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResourcesTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
