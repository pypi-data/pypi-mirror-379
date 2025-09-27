# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_appsync import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class CognitoUserPoolConfig:
    boto3_raw_data: "type_defs.CognitoUserPoolConfigTypeDef" = dataclasses.field()

    userPoolId = field("userPoolId")
    awsRegion = field("awsRegion")
    appIdClientRegex = field("appIdClientRegex")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CognitoUserPoolConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CognitoUserPoolConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LambdaAuthorizerConfig:
    boto3_raw_data: "type_defs.LambdaAuthorizerConfigTypeDef" = dataclasses.field()

    authorizerUri = field("authorizerUri")
    authorizerResultTtlInSeconds = field("authorizerResultTtlInSeconds")
    identityValidationExpression = field("identityValidationExpression")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LambdaAuthorizerConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LambdaAuthorizerConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpenIDConnectConfig:
    boto3_raw_data: "type_defs.OpenIDConnectConfigTypeDef" = dataclasses.field()

    issuer = field("issuer")
    clientId = field("clientId")
    iatTTL = field("iatTTL")
    authTTL = field("authTTL")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OpenIDConnectConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OpenIDConnectConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApiAssociation:
    boto3_raw_data: "type_defs.ApiAssociationTypeDef" = dataclasses.field()

    domainName = field("domainName")
    apiId = field("apiId")
    associationStatus = field("associationStatus")
    deploymentDetail = field("deploymentDetail")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ApiAssociationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ApiAssociationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApiCache:
    boto3_raw_data: "type_defs.ApiCacheTypeDef" = dataclasses.field()

    ttl = field("ttl")
    apiCachingBehavior = field("apiCachingBehavior")
    transitEncryptionEnabled = field("transitEncryptionEnabled")
    atRestEncryptionEnabled = field("atRestEncryptionEnabled")
    type = field("type")
    status = field("status")
    healthMetricsConfig = field("healthMetricsConfig")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ApiCacheTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ApiCacheTypeDef"]]
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
    description = field("description")
    expires = field("expires")
    deletes = field("deletes")

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
class AppSyncRuntime:
    boto3_raw_data: "type_defs.AppSyncRuntimeTypeDef" = dataclasses.field()

    name = field("name")
    runtimeVersion = field("runtimeVersion")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AppSyncRuntimeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AppSyncRuntimeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateApiRequest:
    boto3_raw_data: "type_defs.AssociateApiRequestTypeDef" = dataclasses.field()

    domainName = field("domainName")
    apiId = field("apiId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociateApiRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateApiRequestTypeDef"]
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
class SourceApiAssociationConfig:
    boto3_raw_data: "type_defs.SourceApiAssociationConfigTypeDef" = dataclasses.field()

    mergeType = field("mergeType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SourceApiAssociationConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SourceApiAssociationConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AuthMode:
    boto3_raw_data: "type_defs.AuthModeTypeDef" = dataclasses.field()

    authType = field("authType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AuthModeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AuthModeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CognitoConfig:
    boto3_raw_data: "type_defs.CognitoConfigTypeDef" = dataclasses.field()

    userPoolId = field("userPoolId")
    awsRegion = field("awsRegion")
    appIdClientRegex = field("appIdClientRegex")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CognitoConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CognitoConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AwsIamConfig:
    boto3_raw_data: "type_defs.AwsIamConfigTypeDef" = dataclasses.field()

    signingRegion = field("signingRegion")
    signingServiceName = field("signingServiceName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AwsIamConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AwsIamConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CachingConfigOutput:
    boto3_raw_data: "type_defs.CachingConfigOutputTypeDef" = dataclasses.field()

    ttl = field("ttl")
    cachingKeys = field("cachingKeys")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CachingConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CachingConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CachingConfig:
    boto3_raw_data: "type_defs.CachingConfigTypeDef" = dataclasses.field()

    ttl = field("ttl")
    cachingKeys = field("cachingKeys")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CachingConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CachingConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CodeErrorLocation:
    boto3_raw_data: "type_defs.CodeErrorLocationTypeDef" = dataclasses.field()

    line = field("line")
    column = field("column")
    span = field("span")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CodeErrorLocationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CodeErrorLocationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateApiCacheRequest:
    boto3_raw_data: "type_defs.CreateApiCacheRequestTypeDef" = dataclasses.field()

    apiId = field("apiId")
    ttl = field("ttl")
    apiCachingBehavior = field("apiCachingBehavior")
    type = field("type")
    transitEncryptionEnabled = field("transitEncryptionEnabled")
    atRestEncryptionEnabled = field("atRestEncryptionEnabled")
    healthMetricsConfig = field("healthMetricsConfig")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateApiCacheRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateApiCacheRequestTypeDef"]
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

    apiId = field("apiId")
    description = field("description")
    expires = field("expires")

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
class ElasticsearchDataSourceConfig:
    boto3_raw_data: "type_defs.ElasticsearchDataSourceConfigTypeDef" = (
        dataclasses.field()
    )

    endpoint = field("endpoint")
    awsRegion = field("awsRegion")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ElasticsearchDataSourceConfigTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ElasticsearchDataSourceConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventBridgeDataSourceConfig:
    boto3_raw_data: "type_defs.EventBridgeDataSourceConfigTypeDef" = dataclasses.field()

    eventBusArn = field("eventBusArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EventBridgeDataSourceConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EventBridgeDataSourceConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LambdaDataSourceConfig:
    boto3_raw_data: "type_defs.LambdaDataSourceConfigTypeDef" = dataclasses.field()

    lambdaFunctionArn = field("lambdaFunctionArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LambdaDataSourceConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LambdaDataSourceConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpenSearchServiceDataSourceConfig:
    boto3_raw_data: "type_defs.OpenSearchServiceDataSourceConfigTypeDef" = (
        dataclasses.field()
    )

    endpoint = field("endpoint")
    awsRegion = field("awsRegion")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.OpenSearchServiceDataSourceConfigTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OpenSearchServiceDataSourceConfigTypeDef"]
        ],
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
    certificateArn = field("certificateArn")
    description = field("description")
    tags = field("tags")

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
class DomainNameConfig:
    boto3_raw_data: "type_defs.DomainNameConfigTypeDef" = dataclasses.field()

    domainName = field("domainName")
    description = field("description")
    certificateArn = field("certificateArn")
    appsyncDomainName = field("appsyncDomainName")
    hostedZoneId = field("hostedZoneId")
    tags = field("tags")
    domainNameArn = field("domainNameArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DomainNameConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DomainNameConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnhancedMetricsConfig:
    boto3_raw_data: "type_defs.EnhancedMetricsConfigTypeDef" = dataclasses.field()

    resolverLevelMetricsBehavior = field("resolverLevelMetricsBehavior")
    dataSourceLevelMetricsBehavior = field("dataSourceLevelMetricsBehavior")
    operationLevelMetricsConfig = field("operationLevelMetricsConfig")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EnhancedMetricsConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnhancedMetricsConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LogConfig:
    boto3_raw_data: "type_defs.LogConfigTypeDef" = dataclasses.field()

    fieldLogLevel = field("fieldLogLevel")
    cloudWatchLogsRoleArn = field("cloudWatchLogsRoleArn")
    excludeVerboseContent = field("excludeVerboseContent")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LogConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LogConfigTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserPoolConfig:
    boto3_raw_data: "type_defs.UserPoolConfigTypeDef" = dataclasses.field()

    userPoolId = field("userPoolId")
    awsRegion = field("awsRegion")
    defaultAction = field("defaultAction")
    appIdClientRegex = field("appIdClientRegex")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UserPoolConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UserPoolConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTypeRequest:
    boto3_raw_data: "type_defs.CreateTypeRequestTypeDef" = dataclasses.field()

    apiId = field("apiId")
    definition = field("definition")
    format = field("format")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateTypeRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTypeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Type:
    boto3_raw_data: "type_defs.TypeTypeDef" = dataclasses.field()

    name = field("name")
    description = field("description")
    arn = field("arn")
    definition = field("definition")
    format = field("format")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TypeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TypeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataSourceIntrospectionModelFieldType:
    boto3_raw_data: "type_defs.DataSourceIntrospectionModelFieldTypeTypeDef" = (
        dataclasses.field()
    )

    kind = field("kind")
    name = field("name")
    type = field("type")
    values = field("values")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DataSourceIntrospectionModelFieldTypeTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataSourceIntrospectionModelFieldTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataSourceIntrospectionModelIndex:
    boto3_raw_data: "type_defs.DataSourceIntrospectionModelIndexTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    fields = field("fields")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DataSourceIntrospectionModelIndexTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataSourceIntrospectionModelIndexTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteApiCacheRequest:
    boto3_raw_data: "type_defs.DeleteApiCacheRequestTypeDef" = dataclasses.field()

    apiId = field("apiId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteApiCacheRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteApiCacheRequestTypeDef"]
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

    apiId = field("apiId")
    id = field("id")

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
class DeleteApiRequest:
    boto3_raw_data: "type_defs.DeleteApiRequestTypeDef" = dataclasses.field()

    apiId = field("apiId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteApiRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteApiRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteChannelNamespaceRequest:
    boto3_raw_data: "type_defs.DeleteChannelNamespaceRequestTypeDef" = (
        dataclasses.field()
    )

    apiId = field("apiId")
    name = field("name")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteChannelNamespaceRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteChannelNamespaceRequestTypeDef"]
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

    apiId = field("apiId")
    name = field("name")

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
class DeleteDomainNameRequest:
    boto3_raw_data: "type_defs.DeleteDomainNameRequestTypeDef" = dataclasses.field()

    domainName = field("domainName")

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
class DeleteFunctionRequest:
    boto3_raw_data: "type_defs.DeleteFunctionRequestTypeDef" = dataclasses.field()

    apiId = field("apiId")
    functionId = field("functionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteFunctionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteFunctionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteGraphqlApiRequest:
    boto3_raw_data: "type_defs.DeleteGraphqlApiRequestTypeDef" = dataclasses.field()

    apiId = field("apiId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteGraphqlApiRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteGraphqlApiRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteResolverRequest:
    boto3_raw_data: "type_defs.DeleteResolverRequestTypeDef" = dataclasses.field()

    apiId = field("apiId")
    typeName = field("typeName")
    fieldName = field("fieldName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteResolverRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteResolverRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteTypeRequest:
    boto3_raw_data: "type_defs.DeleteTypeRequestTypeDef" = dataclasses.field()

    apiId = field("apiId")
    typeName = field("typeName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteTypeRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteTypeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeltaSyncConfig:
    boto3_raw_data: "type_defs.DeltaSyncConfigTypeDef" = dataclasses.field()

    baseTableTTL = field("baseTableTTL")
    deltaSyncTableName = field("deltaSyncTableName")
    deltaSyncTableTTL = field("deltaSyncTableTTL")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeltaSyncConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DeltaSyncConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateApiRequest:
    boto3_raw_data: "type_defs.DisassociateApiRequestTypeDef" = dataclasses.field()

    domainName = field("domainName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DisassociateApiRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateApiRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateMergedGraphqlApiRequest:
    boto3_raw_data: "type_defs.DisassociateMergedGraphqlApiRequestTypeDef" = (
        dataclasses.field()
    )

    sourceApiIdentifier = field("sourceApiIdentifier")
    associationId = field("associationId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateMergedGraphqlApiRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateMergedGraphqlApiRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateSourceGraphqlApiRequest:
    boto3_raw_data: "type_defs.DisassociateSourceGraphqlApiRequestTypeDef" = (
        dataclasses.field()
    )

    mergedApiIdentifier = field("mergedApiIdentifier")
    associationId = field("associationId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateSourceGraphqlApiRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateSourceGraphqlApiRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ErrorDetail:
    boto3_raw_data: "type_defs.ErrorDetailTypeDef" = dataclasses.field()

    message = field("message")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ErrorDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ErrorDetailTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvaluateMappingTemplateRequest:
    boto3_raw_data: "type_defs.EvaluateMappingTemplateRequestTypeDef" = (
        dataclasses.field()
    )

    template = field("template")
    context = field("context")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.EvaluateMappingTemplateRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EvaluateMappingTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventLogConfig:
    boto3_raw_data: "type_defs.EventLogConfigTypeDef" = dataclasses.field()

    logLevel = field("logLevel")
    cloudWatchLogsRoleArn = field("cloudWatchLogsRoleArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EventLogConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EventLogConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FlushApiCacheRequest:
    boto3_raw_data: "type_defs.FlushApiCacheRequestTypeDef" = dataclasses.field()

    apiId = field("apiId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FlushApiCacheRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FlushApiCacheRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetApiAssociationRequest:
    boto3_raw_data: "type_defs.GetApiAssociationRequestTypeDef" = dataclasses.field()

    domainName = field("domainName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetApiAssociationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetApiAssociationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetApiCacheRequest:
    boto3_raw_data: "type_defs.GetApiCacheRequestTypeDef" = dataclasses.field()

    apiId = field("apiId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetApiCacheRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetApiCacheRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetApiRequest:
    boto3_raw_data: "type_defs.GetApiRequestTypeDef" = dataclasses.field()

    apiId = field("apiId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetApiRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetApiRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetChannelNamespaceRequest:
    boto3_raw_data: "type_defs.GetChannelNamespaceRequestTypeDef" = dataclasses.field()

    apiId = field("apiId")
    name = field("name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetChannelNamespaceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetChannelNamespaceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDataSourceIntrospectionRequest:
    boto3_raw_data: "type_defs.GetDataSourceIntrospectionRequestTypeDef" = (
        dataclasses.field()
    )

    introspectionId = field("introspectionId")
    includeModelsSDL = field("includeModelsSDL")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetDataSourceIntrospectionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDataSourceIntrospectionRequestTypeDef"]
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

    apiId = field("apiId")
    name = field("name")

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
class GetDomainNameRequest:
    boto3_raw_data: "type_defs.GetDomainNameRequestTypeDef" = dataclasses.field()

    domainName = field("domainName")

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
class GetFunctionRequest:
    boto3_raw_data: "type_defs.GetFunctionRequestTypeDef" = dataclasses.field()

    apiId = field("apiId")
    functionId = field("functionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetFunctionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFunctionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetGraphqlApiEnvironmentVariablesRequest:
    boto3_raw_data: "type_defs.GetGraphqlApiEnvironmentVariablesRequestTypeDef" = (
        dataclasses.field()
    )

    apiId = field("apiId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetGraphqlApiEnvironmentVariablesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetGraphqlApiEnvironmentVariablesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetGraphqlApiRequest:
    boto3_raw_data: "type_defs.GetGraphqlApiRequestTypeDef" = dataclasses.field()

    apiId = field("apiId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetGraphqlApiRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetGraphqlApiRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetIntrospectionSchemaRequest:
    boto3_raw_data: "type_defs.GetIntrospectionSchemaRequestTypeDef" = (
        dataclasses.field()
    )

    apiId = field("apiId")
    format = field("format")
    includeDirectives = field("includeDirectives")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetIntrospectionSchemaRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetIntrospectionSchemaRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResolverRequest:
    boto3_raw_data: "type_defs.GetResolverRequestTypeDef" = dataclasses.field()

    apiId = field("apiId")
    typeName = field("typeName")
    fieldName = field("fieldName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetResolverRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResolverRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSchemaCreationStatusRequest:
    boto3_raw_data: "type_defs.GetSchemaCreationStatusRequestTypeDef" = (
        dataclasses.field()
    )

    apiId = field("apiId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetSchemaCreationStatusRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSchemaCreationStatusRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSourceApiAssociationRequest:
    boto3_raw_data: "type_defs.GetSourceApiAssociationRequestTypeDef" = (
        dataclasses.field()
    )

    mergedApiIdentifier = field("mergedApiIdentifier")
    associationId = field("associationId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetSourceApiAssociationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSourceApiAssociationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTypeRequest:
    boto3_raw_data: "type_defs.GetTypeRequestTypeDef" = dataclasses.field()

    apiId = field("apiId")
    typeName = field("typeName")
    format = field("format")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetTypeRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetTypeRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LambdaConfig:
    boto3_raw_data: "type_defs.LambdaConfigTypeDef" = dataclasses.field()

    invokeType = field("invokeType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LambdaConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LambdaConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LambdaConflictHandlerConfig:
    boto3_raw_data: "type_defs.LambdaConflictHandlerConfigTypeDef" = dataclasses.field()

    lambdaConflictHandlerArn = field("lambdaConflictHandlerArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LambdaConflictHandlerConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LambdaConflictHandlerConfigTypeDef"]
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
class ListApiKeysRequest:
    boto3_raw_data: "type_defs.ListApiKeysRequestTypeDef" = dataclasses.field()

    apiId = field("apiId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListApiKeysRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApiKeysRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListApisRequest:
    boto3_raw_data: "type_defs.ListApisRequestTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListApisRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListApisRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListChannelNamespacesRequest:
    boto3_raw_data: "type_defs.ListChannelNamespacesRequestTypeDef" = (
        dataclasses.field()
    )

    apiId = field("apiId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListChannelNamespacesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListChannelNamespacesRequestTypeDef"]
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

    apiId = field("apiId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

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
class ListDomainNamesRequest:
    boto3_raw_data: "type_defs.ListDomainNamesRequestTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDomainNamesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDomainNamesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFunctionsRequest:
    boto3_raw_data: "type_defs.ListFunctionsRequestTypeDef" = dataclasses.field()

    apiId = field("apiId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFunctionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFunctionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGraphqlApisRequest:
    boto3_raw_data: "type_defs.ListGraphqlApisRequestTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")
    apiType = field("apiType")
    owner = field("owner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListGraphqlApisRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGraphqlApisRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResolversByFunctionRequest:
    boto3_raw_data: "type_defs.ListResolversByFunctionRequestTypeDef" = (
        dataclasses.field()
    )

    apiId = field("apiId")
    functionId = field("functionId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListResolversByFunctionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResolversByFunctionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResolversRequest:
    boto3_raw_data: "type_defs.ListResolversRequestTypeDef" = dataclasses.field()

    apiId = field("apiId")
    typeName = field("typeName")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListResolversRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResolversRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSourceApiAssociationsRequest:
    boto3_raw_data: "type_defs.ListSourceApiAssociationsRequestTypeDef" = (
        dataclasses.field()
    )

    apiId = field("apiId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListSourceApiAssociationsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSourceApiAssociationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SourceApiAssociationSummary:
    boto3_raw_data: "type_defs.SourceApiAssociationSummaryTypeDef" = dataclasses.field()

    associationId = field("associationId")
    associationArn = field("associationArn")
    sourceApiId = field("sourceApiId")
    sourceApiArn = field("sourceApiArn")
    mergedApiId = field("mergedApiId")
    mergedApiArn = field("mergedApiArn")
    description = field("description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SourceApiAssociationSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SourceApiAssociationSummaryTypeDef"]
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
class ListTypesByAssociationRequest:
    boto3_raw_data: "type_defs.ListTypesByAssociationRequestTypeDef" = (
        dataclasses.field()
    )

    mergedApiIdentifier = field("mergedApiIdentifier")
    associationId = field("associationId")
    format = field("format")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListTypesByAssociationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTypesByAssociationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTypesRequest:
    boto3_raw_data: "type_defs.ListTypesRequestTypeDef" = dataclasses.field()

    apiId = field("apiId")
    format = field("format")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListTypesRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTypesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PipelineConfigOutput:
    boto3_raw_data: "type_defs.PipelineConfigOutputTypeDef" = dataclasses.field()

    functions = field("functions")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PipelineConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PipelineConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PipelineConfig:
    boto3_raw_data: "type_defs.PipelineConfigTypeDef" = dataclasses.field()

    functions = field("functions")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PipelineConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PipelineConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutGraphqlApiEnvironmentVariablesRequest:
    boto3_raw_data: "type_defs.PutGraphqlApiEnvironmentVariablesRequestTypeDef" = (
        dataclasses.field()
    )

    apiId = field("apiId")
    environmentVariables = field("environmentVariables")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutGraphqlApiEnvironmentVariablesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutGraphqlApiEnvironmentVariablesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RdsDataApiConfig:
    boto3_raw_data: "type_defs.RdsDataApiConfigTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")
    secretArn = field("secretArn")
    databaseName = field("databaseName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RdsDataApiConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RdsDataApiConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RdsHttpEndpointConfig:
    boto3_raw_data: "type_defs.RdsHttpEndpointConfigTypeDef" = dataclasses.field()

    awsRegion = field("awsRegion")
    dbClusterIdentifier = field("dbClusterIdentifier")
    databaseName = field("databaseName")
    schema = field("schema")
    awsSecretStoreArn = field("awsSecretStoreArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RdsHttpEndpointConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RdsHttpEndpointConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartSchemaMergeRequest:
    boto3_raw_data: "type_defs.StartSchemaMergeRequestTypeDef" = dataclasses.field()

    associationId = field("associationId")
    mergedApiIdentifier = field("mergedApiIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartSchemaMergeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartSchemaMergeRequestTypeDef"]
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
class UpdateApiCacheRequest:
    boto3_raw_data: "type_defs.UpdateApiCacheRequestTypeDef" = dataclasses.field()

    apiId = field("apiId")
    ttl = field("ttl")
    apiCachingBehavior = field("apiCachingBehavior")
    type = field("type")
    healthMetricsConfig = field("healthMetricsConfig")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateApiCacheRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateApiCacheRequestTypeDef"]
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

    apiId = field("apiId")
    id = field("id")
    description = field("description")
    expires = field("expires")

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
class UpdateDomainNameRequest:
    boto3_raw_data: "type_defs.UpdateDomainNameRequestTypeDef" = dataclasses.field()

    domainName = field("domainName")
    description = field("description")

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
class UpdateTypeRequest:
    boto3_raw_data: "type_defs.UpdateTypeRequestTypeDef" = dataclasses.field()

    apiId = field("apiId")
    typeName = field("typeName")
    format = field("format")
    definition = field("definition")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateTypeRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTypeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AdditionalAuthenticationProvider:
    boto3_raw_data: "type_defs.AdditionalAuthenticationProviderTypeDef" = (
        dataclasses.field()
    )

    authenticationType = field("authenticationType")

    @cached_property
    def openIDConnectConfig(self):  # pragma: no cover
        return OpenIDConnectConfig.make_one(self.boto3_raw_data["openIDConnectConfig"])

    @cached_property
    def userPoolConfig(self):  # pragma: no cover
        return CognitoUserPoolConfig.make_one(self.boto3_raw_data["userPoolConfig"])

    @cached_property
    def lambdaAuthorizerConfig(self):  # pragma: no cover
        return LambdaAuthorizerConfig.make_one(
            self.boto3_raw_data["lambdaAuthorizerConfig"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AdditionalAuthenticationProviderTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AdditionalAuthenticationProviderTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvaluateCodeRequest:
    boto3_raw_data: "type_defs.EvaluateCodeRequestTypeDef" = dataclasses.field()

    @cached_property
    def runtime(self):  # pragma: no cover
        return AppSyncRuntime.make_one(self.boto3_raw_data["runtime"])

    code = field("code")
    context = field("context")
    function = field("function")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EvaluateCodeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EvaluateCodeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateApiResponse:
    boto3_raw_data: "type_defs.AssociateApiResponseTypeDef" = dataclasses.field()

    @cached_property
    def apiAssociation(self):  # pragma: no cover
        return ApiAssociation.make_one(self.boto3_raw_data["apiAssociation"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociateApiResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateApiResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateApiCacheResponse:
    boto3_raw_data: "type_defs.CreateApiCacheResponseTypeDef" = dataclasses.field()

    @cached_property
    def apiCache(self):  # pragma: no cover
        return ApiCache.make_one(self.boto3_raw_data["apiCache"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateApiCacheResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateApiCacheResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateApiKeyResponse:
    boto3_raw_data: "type_defs.CreateApiKeyResponseTypeDef" = dataclasses.field()

    @cached_property
    def apiKey(self):  # pragma: no cover
        return ApiKey.make_one(self.boto3_raw_data["apiKey"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateApiKeyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateApiKeyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateMergedGraphqlApiResponse:
    boto3_raw_data: "type_defs.DisassociateMergedGraphqlApiResponseTypeDef" = (
        dataclasses.field()
    )

    sourceApiAssociationStatus = field("sourceApiAssociationStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateMergedGraphqlApiResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateMergedGraphqlApiResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateSourceGraphqlApiResponse:
    boto3_raw_data: "type_defs.DisassociateSourceGraphqlApiResponseTypeDef" = (
        dataclasses.field()
    )

    sourceApiAssociationStatus = field("sourceApiAssociationStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateSourceGraphqlApiResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateSourceGraphqlApiResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetApiAssociationResponse:
    boto3_raw_data: "type_defs.GetApiAssociationResponseTypeDef" = dataclasses.field()

    @cached_property
    def apiAssociation(self):  # pragma: no cover
        return ApiAssociation.make_one(self.boto3_raw_data["apiAssociation"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetApiAssociationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetApiAssociationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetApiCacheResponse:
    boto3_raw_data: "type_defs.GetApiCacheResponseTypeDef" = dataclasses.field()

    @cached_property
    def apiCache(self):  # pragma: no cover
        return ApiCache.make_one(self.boto3_raw_data["apiCache"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetApiCacheResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetApiCacheResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetGraphqlApiEnvironmentVariablesResponse:
    boto3_raw_data: "type_defs.GetGraphqlApiEnvironmentVariablesResponseTypeDef" = (
        dataclasses.field()
    )

    environmentVariables = field("environmentVariables")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetGraphqlApiEnvironmentVariablesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetGraphqlApiEnvironmentVariablesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetIntrospectionSchemaResponse:
    boto3_raw_data: "type_defs.GetIntrospectionSchemaResponseTypeDef" = (
        dataclasses.field()
    )

    schema = field("schema")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetIntrospectionSchemaResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetIntrospectionSchemaResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSchemaCreationStatusResponse:
    boto3_raw_data: "type_defs.GetSchemaCreationStatusResponseTypeDef" = (
        dataclasses.field()
    )

    status = field("status")
    details = field("details")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetSchemaCreationStatusResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSchemaCreationStatusResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListApiKeysResponse:
    boto3_raw_data: "type_defs.ListApiKeysResponseTypeDef" = dataclasses.field()

    @cached_property
    def apiKeys(self):  # pragma: no cover
        return ApiKey.make_many(self.boto3_raw_data["apiKeys"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListApiKeysResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApiKeysResponseTypeDef"]
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
class PutGraphqlApiEnvironmentVariablesResponse:
    boto3_raw_data: "type_defs.PutGraphqlApiEnvironmentVariablesResponseTypeDef" = (
        dataclasses.field()
    )

    environmentVariables = field("environmentVariables")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutGraphqlApiEnvironmentVariablesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutGraphqlApiEnvironmentVariablesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartDataSourceIntrospectionResponse:
    boto3_raw_data: "type_defs.StartDataSourceIntrospectionResponseTypeDef" = (
        dataclasses.field()
    )

    introspectionId = field("introspectionId")
    introspectionStatus = field("introspectionStatus")
    introspectionStatusDetail = field("introspectionStatusDetail")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartDataSourceIntrospectionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartDataSourceIntrospectionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartSchemaCreationResponse:
    boto3_raw_data: "type_defs.StartSchemaCreationResponseTypeDef" = dataclasses.field()

    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartSchemaCreationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartSchemaCreationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartSchemaMergeResponse:
    boto3_raw_data: "type_defs.StartSchemaMergeResponseTypeDef" = dataclasses.field()

    sourceApiAssociationStatus = field("sourceApiAssociationStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartSchemaMergeResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartSchemaMergeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateApiCacheResponse:
    boto3_raw_data: "type_defs.UpdateApiCacheResponseTypeDef" = dataclasses.field()

    @cached_property
    def apiCache(self):  # pragma: no cover
        return ApiCache.make_one(self.boto3_raw_data["apiCache"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateApiCacheResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateApiCacheResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateApiKeyResponse:
    boto3_raw_data: "type_defs.UpdateApiKeyResponseTypeDef" = dataclasses.field()

    @cached_property
    def apiKey(self):  # pragma: no cover
        return ApiKey.make_one(self.boto3_raw_data["apiKey"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateApiKeyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateApiKeyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateMergedGraphqlApiRequest:
    boto3_raw_data: "type_defs.AssociateMergedGraphqlApiRequestTypeDef" = (
        dataclasses.field()
    )

    sourceApiIdentifier = field("sourceApiIdentifier")
    mergedApiIdentifier = field("mergedApiIdentifier")
    description = field("description")

    @cached_property
    def sourceApiAssociationConfig(self):  # pragma: no cover
        return SourceApiAssociationConfig.make_one(
            self.boto3_raw_data["sourceApiAssociationConfig"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AssociateMergedGraphqlApiRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateMergedGraphqlApiRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateSourceGraphqlApiRequest:
    boto3_raw_data: "type_defs.AssociateSourceGraphqlApiRequestTypeDef" = (
        dataclasses.field()
    )

    mergedApiIdentifier = field("mergedApiIdentifier")
    sourceApiIdentifier = field("sourceApiIdentifier")
    description = field("description")

    @cached_property
    def sourceApiAssociationConfig(self):  # pragma: no cover
        return SourceApiAssociationConfig.make_one(
            self.boto3_raw_data["sourceApiAssociationConfig"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AssociateSourceGraphqlApiRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateSourceGraphqlApiRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SourceApiAssociation:
    boto3_raw_data: "type_defs.SourceApiAssociationTypeDef" = dataclasses.field()

    associationId = field("associationId")
    associationArn = field("associationArn")
    sourceApiId = field("sourceApiId")
    sourceApiArn = field("sourceApiArn")
    mergedApiArn = field("mergedApiArn")
    mergedApiId = field("mergedApiId")
    description = field("description")

    @cached_property
    def sourceApiAssociationConfig(self):  # pragma: no cover
        return SourceApiAssociationConfig.make_one(
            self.boto3_raw_data["sourceApiAssociationConfig"]
        )

    sourceApiAssociationStatus = field("sourceApiAssociationStatus")
    sourceApiAssociationStatusDetail = field("sourceApiAssociationStatusDetail")
    lastSuccessfulMergeDate = field("lastSuccessfulMergeDate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SourceApiAssociationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SourceApiAssociationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSourceApiAssociationRequest:
    boto3_raw_data: "type_defs.UpdateSourceApiAssociationRequestTypeDef" = (
        dataclasses.field()
    )

    associationId = field("associationId")
    mergedApiIdentifier = field("mergedApiIdentifier")
    description = field("description")

    @cached_property
    def sourceApiAssociationConfig(self):  # pragma: no cover
        return SourceApiAssociationConfig.make_one(
            self.boto3_raw_data["sourceApiAssociationConfig"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateSourceApiAssociationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSourceApiAssociationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AuthProvider:
    boto3_raw_data: "type_defs.AuthProviderTypeDef" = dataclasses.field()

    authType = field("authType")

    @cached_property
    def cognitoConfig(self):  # pragma: no cover
        return CognitoConfig.make_one(self.boto3_raw_data["cognitoConfig"])

    @cached_property
    def openIDConnectConfig(self):  # pragma: no cover
        return OpenIDConnectConfig.make_one(self.boto3_raw_data["openIDConnectConfig"])

    @cached_property
    def lambdaAuthorizerConfig(self):  # pragma: no cover
        return LambdaAuthorizerConfig.make_one(
            self.boto3_raw_data["lambdaAuthorizerConfig"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AuthProviderTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AuthProviderTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AuthorizationConfig:
    boto3_raw_data: "type_defs.AuthorizationConfigTypeDef" = dataclasses.field()

    authorizationType = field("authorizationType")

    @cached_property
    def awsIamConfig(self):  # pragma: no cover
        return AwsIamConfig.make_one(self.boto3_raw_data["awsIamConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AuthorizationConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AuthorizationConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartSchemaCreationRequest:
    boto3_raw_data: "type_defs.StartSchemaCreationRequestTypeDef" = dataclasses.field()

    apiId = field("apiId")
    definition = field("definition")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartSchemaCreationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartSchemaCreationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CodeError:
    boto3_raw_data: "type_defs.CodeErrorTypeDef" = dataclasses.field()

    errorType = field("errorType")
    value = field("value")

    @cached_property
    def location(self):  # pragma: no cover
        return CodeErrorLocation.make_one(self.boto3_raw_data["location"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CodeErrorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CodeErrorTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDomainNameResponse:
    boto3_raw_data: "type_defs.CreateDomainNameResponseTypeDef" = dataclasses.field()

    @cached_property
    def domainNameConfig(self):  # pragma: no cover
        return DomainNameConfig.make_one(self.boto3_raw_data["domainNameConfig"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDomainNameResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDomainNameResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDomainNameResponse:
    boto3_raw_data: "type_defs.GetDomainNameResponseTypeDef" = dataclasses.field()

    @cached_property
    def domainNameConfig(self):  # pragma: no cover
        return DomainNameConfig.make_one(self.boto3_raw_data["domainNameConfig"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDomainNameResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDomainNameResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDomainNamesResponse:
    boto3_raw_data: "type_defs.ListDomainNamesResponseTypeDef" = dataclasses.field()

    @cached_property
    def domainNameConfigs(self):  # pragma: no cover
        return DomainNameConfig.make_many(self.boto3_raw_data["domainNameConfigs"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDomainNamesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDomainNamesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDomainNameResponse:
    boto3_raw_data: "type_defs.UpdateDomainNameResponseTypeDef" = dataclasses.field()

    @cached_property
    def domainNameConfig(self):  # pragma: no cover
        return DomainNameConfig.make_one(self.boto3_raw_data["domainNameConfig"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDomainNameResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDomainNameResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTypeResponse:
    boto3_raw_data: "type_defs.CreateTypeResponseTypeDef" = dataclasses.field()

    @cached_property
    def type(self):  # pragma: no cover
        return Type.make_one(self.boto3_raw_data["type"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateTypeResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTypeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTypeResponse:
    boto3_raw_data: "type_defs.GetTypeResponseTypeDef" = dataclasses.field()

    @cached_property
    def type(self):  # pragma: no cover
        return Type.make_one(self.boto3_raw_data["type"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetTypeResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetTypeResponseTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTypesByAssociationResponse:
    boto3_raw_data: "type_defs.ListTypesByAssociationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def types(self):  # pragma: no cover
        return Type.make_many(self.boto3_raw_data["types"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListTypesByAssociationResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTypesByAssociationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTypesResponse:
    boto3_raw_data: "type_defs.ListTypesResponseTypeDef" = dataclasses.field()

    @cached_property
    def types(self):  # pragma: no cover
        return Type.make_many(self.boto3_raw_data["types"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListTypesResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTypesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateTypeResponse:
    boto3_raw_data: "type_defs.UpdateTypeResponseTypeDef" = dataclasses.field()

    @cached_property
    def type(self):  # pragma: no cover
        return Type.make_one(self.boto3_raw_data["type"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateTypeResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTypeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataSourceIntrospectionModelField:
    boto3_raw_data: "type_defs.DataSourceIntrospectionModelFieldTypeDef" = (
        dataclasses.field()
    )

    name = field("name")

    @cached_property
    def type(self):  # pragma: no cover
        return DataSourceIntrospectionModelFieldType.make_one(
            self.boto3_raw_data["type"]
        )

    length = field("length")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DataSourceIntrospectionModelFieldTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataSourceIntrospectionModelFieldTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DynamodbDataSourceConfig:
    boto3_raw_data: "type_defs.DynamodbDataSourceConfigTypeDef" = dataclasses.field()

    tableName = field("tableName")
    awsRegion = field("awsRegion")
    useCallerCredentials = field("useCallerCredentials")

    @cached_property
    def deltaSyncConfig(self):  # pragma: no cover
        return DeltaSyncConfig.make_one(self.boto3_raw_data["deltaSyncConfig"])

    versioned = field("versioned")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DynamodbDataSourceConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DynamodbDataSourceConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvaluateMappingTemplateResponse:
    boto3_raw_data: "type_defs.EvaluateMappingTemplateResponseTypeDef" = (
        dataclasses.field()
    )

    evaluationResult = field("evaluationResult")

    @cached_property
    def error(self):  # pragma: no cover
        return ErrorDetail.make_one(self.boto3_raw_data["error"])

    logs = field("logs")
    stash = field("stash")
    outErrors = field("outErrors")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.EvaluateMappingTemplateResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EvaluateMappingTemplateResponseTypeDef"]
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

    dataSourceName = field("dataSourceName")

    @cached_property
    def lambdaConfig(self):  # pragma: no cover
        return LambdaConfig.make_one(self.boto3_raw_data["lambdaConfig"])

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
class SyncConfig:
    boto3_raw_data: "type_defs.SyncConfigTypeDef" = dataclasses.field()

    conflictHandler = field("conflictHandler")
    conflictDetection = field("conflictDetection")

    @cached_property
    def lambdaConflictHandlerConfig(self):  # pragma: no cover
        return LambdaConflictHandlerConfig.make_one(
            self.boto3_raw_data["lambdaConflictHandlerConfig"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SyncConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SyncConfigTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListApiKeysRequestPaginate:
    boto3_raw_data: "type_defs.ListApiKeysRequestPaginateTypeDef" = dataclasses.field()

    apiId = field("apiId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListApiKeysRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApiKeysRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListApisRequestPaginate:
    boto3_raw_data: "type_defs.ListApisRequestPaginateTypeDef" = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListApisRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApisRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListChannelNamespacesRequestPaginate:
    boto3_raw_data: "type_defs.ListChannelNamespacesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    apiId = field("apiId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListChannelNamespacesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListChannelNamespacesRequestPaginateTypeDef"]
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

    apiId = field("apiId")

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
class ListDomainNamesRequestPaginate:
    boto3_raw_data: "type_defs.ListDomainNamesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListDomainNamesRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDomainNamesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFunctionsRequestPaginate:
    boto3_raw_data: "type_defs.ListFunctionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    apiId = field("apiId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFunctionsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFunctionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGraphqlApisRequestPaginate:
    boto3_raw_data: "type_defs.ListGraphqlApisRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    apiType = field("apiType")
    owner = field("owner")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListGraphqlApisRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGraphqlApisRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResolversByFunctionRequestPaginate:
    boto3_raw_data: "type_defs.ListResolversByFunctionRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    apiId = field("apiId")
    functionId = field("functionId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListResolversByFunctionRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResolversByFunctionRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResolversRequestPaginate:
    boto3_raw_data: "type_defs.ListResolversRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    apiId = field("apiId")
    typeName = field("typeName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListResolversRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResolversRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSourceApiAssociationsRequestPaginate:
    boto3_raw_data: "type_defs.ListSourceApiAssociationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    apiId = field("apiId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSourceApiAssociationsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSourceApiAssociationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTypesByAssociationRequestPaginate:
    boto3_raw_data: "type_defs.ListTypesByAssociationRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    mergedApiIdentifier = field("mergedApiIdentifier")
    associationId = field("associationId")
    format = field("format")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListTypesByAssociationRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTypesByAssociationRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTypesRequestPaginate:
    boto3_raw_data: "type_defs.ListTypesRequestPaginateTypeDef" = dataclasses.field()

    apiId = field("apiId")
    format = field("format")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTypesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTypesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSourceApiAssociationsResponse:
    boto3_raw_data: "type_defs.ListSourceApiAssociationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def sourceApiAssociationSummaries(self):  # pragma: no cover
        return SourceApiAssociationSummary.make_many(
            self.boto3_raw_data["sourceApiAssociationSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSourceApiAssociationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSourceApiAssociationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartDataSourceIntrospectionRequest:
    boto3_raw_data: "type_defs.StartDataSourceIntrospectionRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def rdsDataApiConfig(self):  # pragma: no cover
        return RdsDataApiConfig.make_one(self.boto3_raw_data["rdsDataApiConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartDataSourceIntrospectionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartDataSourceIntrospectionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RelationalDatabaseDataSourceConfig:
    boto3_raw_data: "type_defs.RelationalDatabaseDataSourceConfigTypeDef" = (
        dataclasses.field()
    )

    relationalDatabaseSourceType = field("relationalDatabaseSourceType")

    @cached_property
    def rdsHttpEndpointConfig(self):  # pragma: no cover
        return RdsHttpEndpointConfig.make_one(
            self.boto3_raw_data["rdsHttpEndpointConfig"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RelationalDatabaseDataSourceConfigTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RelationalDatabaseDataSourceConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateGraphqlApiRequest:
    boto3_raw_data: "type_defs.CreateGraphqlApiRequestTypeDef" = dataclasses.field()

    name = field("name")
    authenticationType = field("authenticationType")

    @cached_property
    def logConfig(self):  # pragma: no cover
        return LogConfig.make_one(self.boto3_raw_data["logConfig"])

    @cached_property
    def userPoolConfig(self):  # pragma: no cover
        return UserPoolConfig.make_one(self.boto3_raw_data["userPoolConfig"])

    @cached_property
    def openIDConnectConfig(self):  # pragma: no cover
        return OpenIDConnectConfig.make_one(self.boto3_raw_data["openIDConnectConfig"])

    tags = field("tags")

    @cached_property
    def additionalAuthenticationProviders(self):  # pragma: no cover
        return AdditionalAuthenticationProvider.make_many(
            self.boto3_raw_data["additionalAuthenticationProviders"]
        )

    xrayEnabled = field("xrayEnabled")

    @cached_property
    def lambdaAuthorizerConfig(self):  # pragma: no cover
        return LambdaAuthorizerConfig.make_one(
            self.boto3_raw_data["lambdaAuthorizerConfig"]
        )

    apiType = field("apiType")
    mergedApiExecutionRoleArn = field("mergedApiExecutionRoleArn")
    visibility = field("visibility")
    ownerContact = field("ownerContact")
    introspectionConfig = field("introspectionConfig")
    queryDepthLimit = field("queryDepthLimit")
    resolverCountLimit = field("resolverCountLimit")

    @cached_property
    def enhancedMetricsConfig(self):  # pragma: no cover
        return EnhancedMetricsConfig.make_one(
            self.boto3_raw_data["enhancedMetricsConfig"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateGraphqlApiRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateGraphqlApiRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GraphqlApi:
    boto3_raw_data: "type_defs.GraphqlApiTypeDef" = dataclasses.field()

    name = field("name")
    apiId = field("apiId")
    authenticationType = field("authenticationType")

    @cached_property
    def logConfig(self):  # pragma: no cover
        return LogConfig.make_one(self.boto3_raw_data["logConfig"])

    @cached_property
    def userPoolConfig(self):  # pragma: no cover
        return UserPoolConfig.make_one(self.boto3_raw_data["userPoolConfig"])

    @cached_property
    def openIDConnectConfig(self):  # pragma: no cover
        return OpenIDConnectConfig.make_one(self.boto3_raw_data["openIDConnectConfig"])

    arn = field("arn")
    uris = field("uris")
    tags = field("tags")

    @cached_property
    def additionalAuthenticationProviders(self):  # pragma: no cover
        return AdditionalAuthenticationProvider.make_many(
            self.boto3_raw_data["additionalAuthenticationProviders"]
        )

    xrayEnabled = field("xrayEnabled")
    wafWebAclArn = field("wafWebAclArn")

    @cached_property
    def lambdaAuthorizerConfig(self):  # pragma: no cover
        return LambdaAuthorizerConfig.make_one(
            self.boto3_raw_data["lambdaAuthorizerConfig"]
        )

    dns = field("dns")
    visibility = field("visibility")
    apiType = field("apiType")
    mergedApiExecutionRoleArn = field("mergedApiExecutionRoleArn")
    owner = field("owner")
    ownerContact = field("ownerContact")
    introspectionConfig = field("introspectionConfig")
    queryDepthLimit = field("queryDepthLimit")
    resolverCountLimit = field("resolverCountLimit")

    @cached_property
    def enhancedMetricsConfig(self):  # pragma: no cover
        return EnhancedMetricsConfig.make_one(
            self.boto3_raw_data["enhancedMetricsConfig"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GraphqlApiTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GraphqlApiTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateGraphqlApiRequest:
    boto3_raw_data: "type_defs.UpdateGraphqlApiRequestTypeDef" = dataclasses.field()

    apiId = field("apiId")
    name = field("name")
    authenticationType = field("authenticationType")

    @cached_property
    def logConfig(self):  # pragma: no cover
        return LogConfig.make_one(self.boto3_raw_data["logConfig"])

    @cached_property
    def userPoolConfig(self):  # pragma: no cover
        return UserPoolConfig.make_one(self.boto3_raw_data["userPoolConfig"])

    @cached_property
    def openIDConnectConfig(self):  # pragma: no cover
        return OpenIDConnectConfig.make_one(self.boto3_raw_data["openIDConnectConfig"])

    @cached_property
    def additionalAuthenticationProviders(self):  # pragma: no cover
        return AdditionalAuthenticationProvider.make_many(
            self.boto3_raw_data["additionalAuthenticationProviders"]
        )

    xrayEnabled = field("xrayEnabled")

    @cached_property
    def lambdaAuthorizerConfig(self):  # pragma: no cover
        return LambdaAuthorizerConfig.make_one(
            self.boto3_raw_data["lambdaAuthorizerConfig"]
        )

    mergedApiExecutionRoleArn = field("mergedApiExecutionRoleArn")
    ownerContact = field("ownerContact")
    introspectionConfig = field("introspectionConfig")
    queryDepthLimit = field("queryDepthLimit")
    resolverCountLimit = field("resolverCountLimit")

    @cached_property
    def enhancedMetricsConfig(self):  # pragma: no cover
        return EnhancedMetricsConfig.make_one(
            self.boto3_raw_data["enhancedMetricsConfig"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateGraphqlApiRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateGraphqlApiRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateMergedGraphqlApiResponse:
    boto3_raw_data: "type_defs.AssociateMergedGraphqlApiResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def sourceApiAssociation(self):  # pragma: no cover
        return SourceApiAssociation.make_one(
            self.boto3_raw_data["sourceApiAssociation"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateMergedGraphqlApiResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateMergedGraphqlApiResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateSourceGraphqlApiResponse:
    boto3_raw_data: "type_defs.AssociateSourceGraphqlApiResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def sourceApiAssociation(self):  # pragma: no cover
        return SourceApiAssociation.make_one(
            self.boto3_raw_data["sourceApiAssociation"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateSourceGraphqlApiResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateSourceGraphqlApiResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSourceApiAssociationResponse:
    boto3_raw_data: "type_defs.GetSourceApiAssociationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def sourceApiAssociation(self):  # pragma: no cover
        return SourceApiAssociation.make_one(
            self.boto3_raw_data["sourceApiAssociation"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetSourceApiAssociationResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSourceApiAssociationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSourceApiAssociationResponse:
    boto3_raw_data: "type_defs.UpdateSourceApiAssociationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def sourceApiAssociation(self):  # pragma: no cover
        return SourceApiAssociation.make_one(
            self.boto3_raw_data["sourceApiAssociation"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateSourceApiAssociationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSourceApiAssociationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventConfigOutput:
    boto3_raw_data: "type_defs.EventConfigOutputTypeDef" = dataclasses.field()

    @cached_property
    def authProviders(self):  # pragma: no cover
        return AuthProvider.make_many(self.boto3_raw_data["authProviders"])

    @cached_property
    def connectionAuthModes(self):  # pragma: no cover
        return AuthMode.make_many(self.boto3_raw_data["connectionAuthModes"])

    @cached_property
    def defaultPublishAuthModes(self):  # pragma: no cover
        return AuthMode.make_many(self.boto3_raw_data["defaultPublishAuthModes"])

    @cached_property
    def defaultSubscribeAuthModes(self):  # pragma: no cover
        return AuthMode.make_many(self.boto3_raw_data["defaultSubscribeAuthModes"])

    @cached_property
    def logConfig(self):  # pragma: no cover
        return EventLogConfig.make_one(self.boto3_raw_data["logConfig"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EventConfigOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EventConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventConfig:
    boto3_raw_data: "type_defs.EventConfigTypeDef" = dataclasses.field()

    @cached_property
    def authProviders(self):  # pragma: no cover
        return AuthProvider.make_many(self.boto3_raw_data["authProviders"])

    @cached_property
    def connectionAuthModes(self):  # pragma: no cover
        return AuthMode.make_many(self.boto3_raw_data["connectionAuthModes"])

    @cached_property
    def defaultPublishAuthModes(self):  # pragma: no cover
        return AuthMode.make_many(self.boto3_raw_data["defaultPublishAuthModes"])

    @cached_property
    def defaultSubscribeAuthModes(self):  # pragma: no cover
        return AuthMode.make_many(self.boto3_raw_data["defaultSubscribeAuthModes"])

    @cached_property
    def logConfig(self):  # pragma: no cover
        return EventLogConfig.make_one(self.boto3_raw_data["logConfig"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EventConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EventConfigTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HttpDataSourceConfig:
    boto3_raw_data: "type_defs.HttpDataSourceConfigTypeDef" = dataclasses.field()

    endpoint = field("endpoint")

    @cached_property
    def authorizationConfig(self):  # pragma: no cover
        return AuthorizationConfig.make_one(self.boto3_raw_data["authorizationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HttpDataSourceConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HttpDataSourceConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvaluateCodeErrorDetail:
    boto3_raw_data: "type_defs.EvaluateCodeErrorDetailTypeDef" = dataclasses.field()

    message = field("message")

    @cached_property
    def codeErrors(self):  # pragma: no cover
        return CodeError.make_many(self.boto3_raw_data["codeErrors"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EvaluateCodeErrorDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EvaluateCodeErrorDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataSourceIntrospectionModel:
    boto3_raw_data: "type_defs.DataSourceIntrospectionModelTypeDef" = (
        dataclasses.field()
    )

    name = field("name")

    @cached_property
    def fields(self):  # pragma: no cover
        return DataSourceIntrospectionModelField.make_many(
            self.boto3_raw_data["fields"]
        )

    @cached_property
    def primaryKey(self):  # pragma: no cover
        return DataSourceIntrospectionModelIndex.make_one(
            self.boto3_raw_data["primaryKey"]
        )

    @cached_property
    def indexes(self):  # pragma: no cover
        return DataSourceIntrospectionModelIndex.make_many(
            self.boto3_raw_data["indexes"]
        )

    sdl = field("sdl")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataSourceIntrospectionModelTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataSourceIntrospectionModelTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HandlerConfig:
    boto3_raw_data: "type_defs.HandlerConfigTypeDef" = dataclasses.field()

    behavior = field("behavior")

    @cached_property
    def integration(self):  # pragma: no cover
        return Integration.make_one(self.boto3_raw_data["integration"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HandlerConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.HandlerConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFunctionRequest:
    boto3_raw_data: "type_defs.CreateFunctionRequestTypeDef" = dataclasses.field()

    apiId = field("apiId")
    name = field("name")
    dataSourceName = field("dataSourceName")
    description = field("description")
    requestMappingTemplate = field("requestMappingTemplate")
    responseMappingTemplate = field("responseMappingTemplate")
    functionVersion = field("functionVersion")

    @cached_property
    def syncConfig(self):  # pragma: no cover
        return SyncConfig.make_one(self.boto3_raw_data["syncConfig"])

    maxBatchSize = field("maxBatchSize")

    @cached_property
    def runtime(self):  # pragma: no cover
        return AppSyncRuntime.make_one(self.boto3_raw_data["runtime"])

    code = field("code")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateFunctionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFunctionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FunctionConfiguration:
    boto3_raw_data: "type_defs.FunctionConfigurationTypeDef" = dataclasses.field()

    functionId = field("functionId")
    functionArn = field("functionArn")
    name = field("name")
    description = field("description")
    dataSourceName = field("dataSourceName")
    requestMappingTemplate = field("requestMappingTemplate")
    responseMappingTemplate = field("responseMappingTemplate")
    functionVersion = field("functionVersion")

    @cached_property
    def syncConfig(self):  # pragma: no cover
        return SyncConfig.make_one(self.boto3_raw_data["syncConfig"])

    maxBatchSize = field("maxBatchSize")

    @cached_property
    def runtime(self):  # pragma: no cover
        return AppSyncRuntime.make_one(self.boto3_raw_data["runtime"])

    code = field("code")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FunctionConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FunctionConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Resolver:
    boto3_raw_data: "type_defs.ResolverTypeDef" = dataclasses.field()

    typeName = field("typeName")
    fieldName = field("fieldName")
    dataSourceName = field("dataSourceName")
    resolverArn = field("resolverArn")
    requestMappingTemplate = field("requestMappingTemplate")
    responseMappingTemplate = field("responseMappingTemplate")
    kind = field("kind")

    @cached_property
    def pipelineConfig(self):  # pragma: no cover
        return PipelineConfigOutput.make_one(self.boto3_raw_data["pipelineConfig"])

    @cached_property
    def syncConfig(self):  # pragma: no cover
        return SyncConfig.make_one(self.boto3_raw_data["syncConfig"])

    @cached_property
    def cachingConfig(self):  # pragma: no cover
        return CachingConfigOutput.make_one(self.boto3_raw_data["cachingConfig"])

    maxBatchSize = field("maxBatchSize")

    @cached_property
    def runtime(self):  # pragma: no cover
        return AppSyncRuntime.make_one(self.boto3_raw_data["runtime"])

    code = field("code")
    metricsConfig = field("metricsConfig")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResolverTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResolverTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFunctionRequest:
    boto3_raw_data: "type_defs.UpdateFunctionRequestTypeDef" = dataclasses.field()

    apiId = field("apiId")
    name = field("name")
    functionId = field("functionId")
    dataSourceName = field("dataSourceName")
    description = field("description")
    requestMappingTemplate = field("requestMappingTemplate")
    responseMappingTemplate = field("responseMappingTemplate")
    functionVersion = field("functionVersion")

    @cached_property
    def syncConfig(self):  # pragma: no cover
        return SyncConfig.make_one(self.boto3_raw_data["syncConfig"])

    maxBatchSize = field("maxBatchSize")

    @cached_property
    def runtime(self):  # pragma: no cover
        return AppSyncRuntime.make_one(self.boto3_raw_data["runtime"])

    code = field("code")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateFunctionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFunctionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateResolverRequest:
    boto3_raw_data: "type_defs.CreateResolverRequestTypeDef" = dataclasses.field()

    apiId = field("apiId")
    typeName = field("typeName")
    fieldName = field("fieldName")
    dataSourceName = field("dataSourceName")
    requestMappingTemplate = field("requestMappingTemplate")
    responseMappingTemplate = field("responseMappingTemplate")
    kind = field("kind")
    pipelineConfig = field("pipelineConfig")

    @cached_property
    def syncConfig(self):  # pragma: no cover
        return SyncConfig.make_one(self.boto3_raw_data["syncConfig"])

    cachingConfig = field("cachingConfig")
    maxBatchSize = field("maxBatchSize")

    @cached_property
    def runtime(self):  # pragma: no cover
        return AppSyncRuntime.make_one(self.boto3_raw_data["runtime"])

    code = field("code")
    metricsConfig = field("metricsConfig")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateResolverRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateResolverRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateResolverRequest:
    boto3_raw_data: "type_defs.UpdateResolverRequestTypeDef" = dataclasses.field()

    apiId = field("apiId")
    typeName = field("typeName")
    fieldName = field("fieldName")
    dataSourceName = field("dataSourceName")
    requestMappingTemplate = field("requestMappingTemplate")
    responseMappingTemplate = field("responseMappingTemplate")
    kind = field("kind")
    pipelineConfig = field("pipelineConfig")

    @cached_property
    def syncConfig(self):  # pragma: no cover
        return SyncConfig.make_one(self.boto3_raw_data["syncConfig"])

    cachingConfig = field("cachingConfig")
    maxBatchSize = field("maxBatchSize")

    @cached_property
    def runtime(self):  # pragma: no cover
        return AppSyncRuntime.make_one(self.boto3_raw_data["runtime"])

    code = field("code")
    metricsConfig = field("metricsConfig")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateResolverRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateResolverRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateGraphqlApiResponse:
    boto3_raw_data: "type_defs.CreateGraphqlApiResponseTypeDef" = dataclasses.field()

    @cached_property
    def graphqlApi(self):  # pragma: no cover
        return GraphqlApi.make_one(self.boto3_raw_data["graphqlApi"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateGraphqlApiResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateGraphqlApiResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetGraphqlApiResponse:
    boto3_raw_data: "type_defs.GetGraphqlApiResponseTypeDef" = dataclasses.field()

    @cached_property
    def graphqlApi(self):  # pragma: no cover
        return GraphqlApi.make_one(self.boto3_raw_data["graphqlApi"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetGraphqlApiResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetGraphqlApiResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGraphqlApisResponse:
    boto3_raw_data: "type_defs.ListGraphqlApisResponseTypeDef" = dataclasses.field()

    @cached_property
    def graphqlApis(self):  # pragma: no cover
        return GraphqlApi.make_many(self.boto3_raw_data["graphqlApis"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListGraphqlApisResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGraphqlApisResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateGraphqlApiResponse:
    boto3_raw_data: "type_defs.UpdateGraphqlApiResponseTypeDef" = dataclasses.field()

    @cached_property
    def graphqlApi(self):  # pragma: no cover
        return GraphqlApi.make_one(self.boto3_raw_data["graphqlApi"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateGraphqlApiResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateGraphqlApiResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Api:
    boto3_raw_data: "type_defs.ApiTypeDef" = dataclasses.field()

    apiId = field("apiId")
    name = field("name")
    ownerContact = field("ownerContact")
    tags = field("tags")
    dns = field("dns")
    apiArn = field("apiArn")
    created = field("created")
    xrayEnabled = field("xrayEnabled")
    wafWebAclArn = field("wafWebAclArn")

    @cached_property
    def eventConfig(self):  # pragma: no cover
        return EventConfigOutput.make_one(self.boto3_raw_data["eventConfig"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ApiTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ApiTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDataSourceRequest:
    boto3_raw_data: "type_defs.CreateDataSourceRequestTypeDef" = dataclasses.field()

    apiId = field("apiId")
    name = field("name")
    type = field("type")
    description = field("description")
    serviceRoleArn = field("serviceRoleArn")

    @cached_property
    def dynamodbConfig(self):  # pragma: no cover
        return DynamodbDataSourceConfig.make_one(self.boto3_raw_data["dynamodbConfig"])

    @cached_property
    def lambdaConfig(self):  # pragma: no cover
        return LambdaDataSourceConfig.make_one(self.boto3_raw_data["lambdaConfig"])

    @cached_property
    def elasticsearchConfig(self):  # pragma: no cover
        return ElasticsearchDataSourceConfig.make_one(
            self.boto3_raw_data["elasticsearchConfig"]
        )

    @cached_property
    def openSearchServiceConfig(self):  # pragma: no cover
        return OpenSearchServiceDataSourceConfig.make_one(
            self.boto3_raw_data["openSearchServiceConfig"]
        )

    @cached_property
    def httpConfig(self):  # pragma: no cover
        return HttpDataSourceConfig.make_one(self.boto3_raw_data["httpConfig"])

    @cached_property
    def relationalDatabaseConfig(self):  # pragma: no cover
        return RelationalDatabaseDataSourceConfig.make_one(
            self.boto3_raw_data["relationalDatabaseConfig"]
        )

    @cached_property
    def eventBridgeConfig(self):  # pragma: no cover
        return EventBridgeDataSourceConfig.make_one(
            self.boto3_raw_data["eventBridgeConfig"]
        )

    metricsConfig = field("metricsConfig")

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
class DataSource:
    boto3_raw_data: "type_defs.DataSourceTypeDef" = dataclasses.field()

    dataSourceArn = field("dataSourceArn")
    name = field("name")
    description = field("description")
    type = field("type")
    serviceRoleArn = field("serviceRoleArn")

    @cached_property
    def dynamodbConfig(self):  # pragma: no cover
        return DynamodbDataSourceConfig.make_one(self.boto3_raw_data["dynamodbConfig"])

    @cached_property
    def lambdaConfig(self):  # pragma: no cover
        return LambdaDataSourceConfig.make_one(self.boto3_raw_data["lambdaConfig"])

    @cached_property
    def elasticsearchConfig(self):  # pragma: no cover
        return ElasticsearchDataSourceConfig.make_one(
            self.boto3_raw_data["elasticsearchConfig"]
        )

    @cached_property
    def openSearchServiceConfig(self):  # pragma: no cover
        return OpenSearchServiceDataSourceConfig.make_one(
            self.boto3_raw_data["openSearchServiceConfig"]
        )

    @cached_property
    def httpConfig(self):  # pragma: no cover
        return HttpDataSourceConfig.make_one(self.boto3_raw_data["httpConfig"])

    @cached_property
    def relationalDatabaseConfig(self):  # pragma: no cover
        return RelationalDatabaseDataSourceConfig.make_one(
            self.boto3_raw_data["relationalDatabaseConfig"]
        )

    @cached_property
    def eventBridgeConfig(self):  # pragma: no cover
        return EventBridgeDataSourceConfig.make_one(
            self.boto3_raw_data["eventBridgeConfig"]
        )

    metricsConfig = field("metricsConfig")

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
class UpdateDataSourceRequest:
    boto3_raw_data: "type_defs.UpdateDataSourceRequestTypeDef" = dataclasses.field()

    apiId = field("apiId")
    name = field("name")
    type = field("type")
    description = field("description")
    serviceRoleArn = field("serviceRoleArn")

    @cached_property
    def dynamodbConfig(self):  # pragma: no cover
        return DynamodbDataSourceConfig.make_one(self.boto3_raw_data["dynamodbConfig"])

    @cached_property
    def lambdaConfig(self):  # pragma: no cover
        return LambdaDataSourceConfig.make_one(self.boto3_raw_data["lambdaConfig"])

    @cached_property
    def elasticsearchConfig(self):  # pragma: no cover
        return ElasticsearchDataSourceConfig.make_one(
            self.boto3_raw_data["elasticsearchConfig"]
        )

    @cached_property
    def openSearchServiceConfig(self):  # pragma: no cover
        return OpenSearchServiceDataSourceConfig.make_one(
            self.boto3_raw_data["openSearchServiceConfig"]
        )

    @cached_property
    def httpConfig(self):  # pragma: no cover
        return HttpDataSourceConfig.make_one(self.boto3_raw_data["httpConfig"])

    @cached_property
    def relationalDatabaseConfig(self):  # pragma: no cover
        return RelationalDatabaseDataSourceConfig.make_one(
            self.boto3_raw_data["relationalDatabaseConfig"]
        )

    @cached_property
    def eventBridgeConfig(self):  # pragma: no cover
        return EventBridgeDataSourceConfig.make_one(
            self.boto3_raw_data["eventBridgeConfig"]
        )

    metricsConfig = field("metricsConfig")

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
class EvaluateCodeResponse:
    boto3_raw_data: "type_defs.EvaluateCodeResponseTypeDef" = dataclasses.field()

    evaluationResult = field("evaluationResult")

    @cached_property
    def error(self):  # pragma: no cover
        return EvaluateCodeErrorDetail.make_one(self.boto3_raw_data["error"])

    logs = field("logs")
    stash = field("stash")
    outErrors = field("outErrors")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EvaluateCodeResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EvaluateCodeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataSourceIntrospectionResult:
    boto3_raw_data: "type_defs.DataSourceIntrospectionResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def models(self):  # pragma: no cover
        return DataSourceIntrospectionModel.make_many(self.boto3_raw_data["models"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DataSourceIntrospectionResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataSourceIntrospectionResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HandlerConfigs:
    boto3_raw_data: "type_defs.HandlerConfigsTypeDef" = dataclasses.field()

    @cached_property
    def onPublish(self):  # pragma: no cover
        return HandlerConfig.make_one(self.boto3_raw_data["onPublish"])

    @cached_property
    def onSubscribe(self):  # pragma: no cover
        return HandlerConfig.make_one(self.boto3_raw_data["onSubscribe"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HandlerConfigsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.HandlerConfigsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFunctionResponse:
    boto3_raw_data: "type_defs.CreateFunctionResponseTypeDef" = dataclasses.field()

    @cached_property
    def functionConfiguration(self):  # pragma: no cover
        return FunctionConfiguration.make_one(
            self.boto3_raw_data["functionConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateFunctionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFunctionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFunctionResponse:
    boto3_raw_data: "type_defs.GetFunctionResponseTypeDef" = dataclasses.field()

    @cached_property
    def functionConfiguration(self):  # pragma: no cover
        return FunctionConfiguration.make_one(
            self.boto3_raw_data["functionConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetFunctionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFunctionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFunctionsResponse:
    boto3_raw_data: "type_defs.ListFunctionsResponseTypeDef" = dataclasses.field()

    @cached_property
    def functions(self):  # pragma: no cover
        return FunctionConfiguration.make_many(self.boto3_raw_data["functions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFunctionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFunctionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFunctionResponse:
    boto3_raw_data: "type_defs.UpdateFunctionResponseTypeDef" = dataclasses.field()

    @cached_property
    def functionConfiguration(self):  # pragma: no cover
        return FunctionConfiguration.make_one(
            self.boto3_raw_data["functionConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateFunctionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFunctionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateResolverResponse:
    boto3_raw_data: "type_defs.CreateResolverResponseTypeDef" = dataclasses.field()

    @cached_property
    def resolver(self):  # pragma: no cover
        return Resolver.make_one(self.boto3_raw_data["resolver"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateResolverResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateResolverResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResolverResponse:
    boto3_raw_data: "type_defs.GetResolverResponseTypeDef" = dataclasses.field()

    @cached_property
    def resolver(self):  # pragma: no cover
        return Resolver.make_one(self.boto3_raw_data["resolver"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetResolverResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResolverResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResolversByFunctionResponse:
    boto3_raw_data: "type_defs.ListResolversByFunctionResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def resolvers(self):  # pragma: no cover
        return Resolver.make_many(self.boto3_raw_data["resolvers"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListResolversByFunctionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResolversByFunctionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResolversResponse:
    boto3_raw_data: "type_defs.ListResolversResponseTypeDef" = dataclasses.field()

    @cached_property
    def resolvers(self):  # pragma: no cover
        return Resolver.make_many(self.boto3_raw_data["resolvers"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListResolversResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResolversResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateResolverResponse:
    boto3_raw_data: "type_defs.UpdateResolverResponseTypeDef" = dataclasses.field()

    @cached_property
    def resolver(self):  # pragma: no cover
        return Resolver.make_one(self.boto3_raw_data["resolver"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateResolverResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateResolverResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateApiResponse:
    boto3_raw_data: "type_defs.CreateApiResponseTypeDef" = dataclasses.field()

    @cached_property
    def api(self):  # pragma: no cover
        return Api.make_one(self.boto3_raw_data["api"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateApiResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateApiResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetApiResponse:
    boto3_raw_data: "type_defs.GetApiResponseTypeDef" = dataclasses.field()

    @cached_property
    def api(self):  # pragma: no cover
        return Api.make_one(self.boto3_raw_data["api"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetApiResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetApiResponseTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListApisResponse:
    boto3_raw_data: "type_defs.ListApisResponseTypeDef" = dataclasses.field()

    @cached_property
    def apis(self):  # pragma: no cover
        return Api.make_many(self.boto3_raw_data["apis"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListApisResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApisResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateApiResponse:
    boto3_raw_data: "type_defs.UpdateApiResponseTypeDef" = dataclasses.field()

    @cached_property
    def api(self):  # pragma: no cover
        return Api.make_one(self.boto3_raw_data["api"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateApiResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateApiResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateApiRequest:
    boto3_raw_data: "type_defs.CreateApiRequestTypeDef" = dataclasses.field()

    name = field("name")
    ownerContact = field("ownerContact")
    tags = field("tags")
    eventConfig = field("eventConfig")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateApiRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateApiRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateApiRequest:
    boto3_raw_data: "type_defs.UpdateApiRequestTypeDef" = dataclasses.field()

    apiId = field("apiId")
    name = field("name")
    ownerContact = field("ownerContact")
    eventConfig = field("eventConfig")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateApiRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateApiRequestTypeDef"]
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
class ListDataSourcesResponse:
    boto3_raw_data: "type_defs.ListDataSourcesResponseTypeDef" = dataclasses.field()

    @cached_property
    def dataSources(self):  # pragma: no cover
        return DataSource.make_many(self.boto3_raw_data["dataSources"])

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
class GetDataSourceIntrospectionResponse:
    boto3_raw_data: "type_defs.GetDataSourceIntrospectionResponseTypeDef" = (
        dataclasses.field()
    )

    introspectionId = field("introspectionId")
    introspectionStatus = field("introspectionStatus")
    introspectionStatusDetail = field("introspectionStatusDetail")

    @cached_property
    def introspectionResult(self):  # pragma: no cover
        return DataSourceIntrospectionResult.make_one(
            self.boto3_raw_data["introspectionResult"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetDataSourceIntrospectionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDataSourceIntrospectionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChannelNamespace:
    boto3_raw_data: "type_defs.ChannelNamespaceTypeDef" = dataclasses.field()

    apiId = field("apiId")
    name = field("name")

    @cached_property
    def subscribeAuthModes(self):  # pragma: no cover
        return AuthMode.make_many(self.boto3_raw_data["subscribeAuthModes"])

    @cached_property
    def publishAuthModes(self):  # pragma: no cover
        return AuthMode.make_many(self.boto3_raw_data["publishAuthModes"])

    codeHandlers = field("codeHandlers")
    tags = field("tags")
    channelNamespaceArn = field("channelNamespaceArn")
    created = field("created")
    lastModified = field("lastModified")

    @cached_property
    def handlerConfigs(self):  # pragma: no cover
        return HandlerConfigs.make_one(self.boto3_raw_data["handlerConfigs"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ChannelNamespaceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ChannelNamespaceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateChannelNamespaceRequest:
    boto3_raw_data: "type_defs.CreateChannelNamespaceRequestTypeDef" = (
        dataclasses.field()
    )

    apiId = field("apiId")
    name = field("name")

    @cached_property
    def subscribeAuthModes(self):  # pragma: no cover
        return AuthMode.make_many(self.boto3_raw_data["subscribeAuthModes"])

    @cached_property
    def publishAuthModes(self):  # pragma: no cover
        return AuthMode.make_many(self.boto3_raw_data["publishAuthModes"])

    codeHandlers = field("codeHandlers")
    tags = field("tags")

    @cached_property
    def handlerConfigs(self):  # pragma: no cover
        return HandlerConfigs.make_one(self.boto3_raw_data["handlerConfigs"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateChannelNamespaceRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateChannelNamespaceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateChannelNamespaceRequest:
    boto3_raw_data: "type_defs.UpdateChannelNamespaceRequestTypeDef" = (
        dataclasses.field()
    )

    apiId = field("apiId")
    name = field("name")

    @cached_property
    def subscribeAuthModes(self):  # pragma: no cover
        return AuthMode.make_many(self.boto3_raw_data["subscribeAuthModes"])

    @cached_property
    def publishAuthModes(self):  # pragma: no cover
        return AuthMode.make_many(self.boto3_raw_data["publishAuthModes"])

    codeHandlers = field("codeHandlers")

    @cached_property
    def handlerConfigs(self):  # pragma: no cover
        return HandlerConfigs.make_one(self.boto3_raw_data["handlerConfigs"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateChannelNamespaceRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateChannelNamespaceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateChannelNamespaceResponse:
    boto3_raw_data: "type_defs.CreateChannelNamespaceResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def channelNamespace(self):  # pragma: no cover
        return ChannelNamespace.make_one(self.boto3_raw_data["channelNamespace"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateChannelNamespaceResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateChannelNamespaceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetChannelNamespaceResponse:
    boto3_raw_data: "type_defs.GetChannelNamespaceResponseTypeDef" = dataclasses.field()

    @cached_property
    def channelNamespace(self):  # pragma: no cover
        return ChannelNamespace.make_one(self.boto3_raw_data["channelNamespace"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetChannelNamespaceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetChannelNamespaceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListChannelNamespacesResponse:
    boto3_raw_data: "type_defs.ListChannelNamespacesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def channelNamespaces(self):  # pragma: no cover
        return ChannelNamespace.make_many(self.boto3_raw_data["channelNamespaces"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListChannelNamespacesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListChannelNamespacesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateChannelNamespaceResponse:
    boto3_raw_data: "type_defs.UpdateChannelNamespaceResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def channelNamespace(self):  # pragma: no cover
        return ChannelNamespace.make_one(self.boto3_raw_data["channelNamespace"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateChannelNamespaceResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateChannelNamespaceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
