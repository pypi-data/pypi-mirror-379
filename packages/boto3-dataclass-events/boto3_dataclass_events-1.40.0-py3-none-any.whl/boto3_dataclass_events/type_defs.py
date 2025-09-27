# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_events import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class ActivateEventSourceRequest:
    boto3_raw_data: "type_defs.ActivateEventSourceRequestTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ActivateEventSourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActivateEventSourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApiDestination:
    boto3_raw_data: "type_defs.ApiDestinationTypeDef" = dataclasses.field()

    ApiDestinationArn = field("ApiDestinationArn")
    Name = field("Name")
    ApiDestinationState = field("ApiDestinationState")
    ConnectionArn = field("ConnectionArn")
    InvocationEndpoint = field("InvocationEndpoint")
    HttpMethod = field("HttpMethod")
    InvocationRateLimitPerSecond = field("InvocationRateLimitPerSecond")
    CreationTime = field("CreationTime")
    LastModifiedTime = field("LastModifiedTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ApiDestinationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ApiDestinationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AppSyncParameters:
    boto3_raw_data: "type_defs.AppSyncParametersTypeDef" = dataclasses.field()

    GraphQLOperation = field("GraphQLOperation")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AppSyncParametersTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AppSyncParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Archive:
    boto3_raw_data: "type_defs.ArchiveTypeDef" = dataclasses.field()

    ArchiveName = field("ArchiveName")
    EventSourceArn = field("EventSourceArn")
    State = field("State")
    StateReason = field("StateReason")
    RetentionDays = field("RetentionDays")
    SizeBytes = field("SizeBytes")
    EventCount = field("EventCount")
    CreationTime = field("CreationTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ArchiveTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ArchiveTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AwsVpcConfigurationOutput:
    boto3_raw_data: "type_defs.AwsVpcConfigurationOutputTypeDef" = dataclasses.field()

    Subnets = field("Subnets")
    SecurityGroups = field("SecurityGroups")
    AssignPublicIp = field("AssignPublicIp")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AwsVpcConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AwsVpcConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AwsVpcConfiguration:
    boto3_raw_data: "type_defs.AwsVpcConfigurationTypeDef" = dataclasses.field()

    Subnets = field("Subnets")
    SecurityGroups = field("SecurityGroups")
    AssignPublicIp = field("AssignPublicIp")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AwsVpcConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AwsVpcConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchArrayProperties:
    boto3_raw_data: "type_defs.BatchArrayPropertiesTypeDef" = dataclasses.field()

    Size = field("Size")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchArrayPropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchArrayPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchRetryStrategy:
    boto3_raw_data: "type_defs.BatchRetryStrategyTypeDef" = dataclasses.field()

    Attempts = field("Attempts")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchRetryStrategyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchRetryStrategyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelReplayRequest:
    boto3_raw_data: "type_defs.CancelReplayRequestTypeDef" = dataclasses.field()

    ReplayName = field("ReplayName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CancelReplayRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelReplayRequestTypeDef"]
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
class CapacityProviderStrategyItem:
    boto3_raw_data: "type_defs.CapacityProviderStrategyItemTypeDef" = (
        dataclasses.field()
    )

    capacityProvider = field("capacityProvider")
    weight = field("weight")
    base = field("base")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CapacityProviderStrategyItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CapacityProviderStrategyItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Condition:
    boto3_raw_data: "type_defs.ConditionTypeDef" = dataclasses.field()

    Type = field("Type")
    Key = field("Key")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConditionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ConditionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConnectionApiKeyAuthResponseParameters:
    boto3_raw_data: "type_defs.ConnectionApiKeyAuthResponseParametersTypeDef" = (
        dataclasses.field()
    )

    ApiKeyName = field("ApiKeyName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ConnectionApiKeyAuthResponseParametersTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConnectionApiKeyAuthResponseParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConnectionBasicAuthResponseParameters:
    boto3_raw_data: "type_defs.ConnectionBasicAuthResponseParametersTypeDef" = (
        dataclasses.field()
    )

    Username = field("Username")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ConnectionBasicAuthResponseParametersTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConnectionBasicAuthResponseParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConnectionBodyParameter:
    boto3_raw_data: "type_defs.ConnectionBodyParameterTypeDef" = dataclasses.field()

    Key = field("Key")
    Value = field("Value")
    IsValueSecret = field("IsValueSecret")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConnectionBodyParameterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConnectionBodyParameterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConnectionHeaderParameter:
    boto3_raw_data: "type_defs.ConnectionHeaderParameterTypeDef" = dataclasses.field()

    Key = field("Key")
    Value = field("Value")
    IsValueSecret = field("IsValueSecret")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConnectionHeaderParameterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConnectionHeaderParameterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConnectionQueryStringParameter:
    boto3_raw_data: "type_defs.ConnectionQueryStringParameterTypeDef" = (
        dataclasses.field()
    )

    Key = field("Key")
    Value = field("Value")
    IsValueSecret = field("IsValueSecret")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ConnectionQueryStringParameterTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConnectionQueryStringParameterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConnectionOAuthClientResponseParameters:
    boto3_raw_data: "type_defs.ConnectionOAuthClientResponseParametersTypeDef" = (
        dataclasses.field()
    )

    ClientID = field("ClientID")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ConnectionOAuthClientResponseParametersTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConnectionOAuthClientResponseParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Connection:
    boto3_raw_data: "type_defs.ConnectionTypeDef" = dataclasses.field()

    ConnectionArn = field("ConnectionArn")
    Name = field("Name")
    ConnectionState = field("ConnectionState")
    StateReason = field("StateReason")
    AuthorizationType = field("AuthorizationType")
    CreationTime = field("CreationTime")
    LastModifiedTime = field("LastModifiedTime")
    LastAuthorizedTime = field("LastAuthorizedTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConnectionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ConnectionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConnectivityResourceConfigurationArn:
    boto3_raw_data: "type_defs.ConnectivityResourceConfigurationArnTypeDef" = (
        dataclasses.field()
    )

    ResourceConfigurationArn = field("ResourceConfigurationArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ConnectivityResourceConfigurationArnTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConnectivityResourceConfigurationArnTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateApiDestinationRequest:
    boto3_raw_data: "type_defs.CreateApiDestinationRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    ConnectionArn = field("ConnectionArn")
    InvocationEndpoint = field("InvocationEndpoint")
    HttpMethod = field("HttpMethod")
    Description = field("Description")
    InvocationRateLimitPerSecond = field("InvocationRateLimitPerSecond")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateApiDestinationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateApiDestinationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateArchiveRequest:
    boto3_raw_data: "type_defs.CreateArchiveRequestTypeDef" = dataclasses.field()

    ArchiveName = field("ArchiveName")
    EventSourceArn = field("EventSourceArn")
    Description = field("Description")
    EventPattern = field("EventPattern")
    RetentionDays = field("RetentionDays")
    KmsKeyIdentifier = field("KmsKeyIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateArchiveRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateArchiveRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateConnectionApiKeyAuthRequestParameters:
    boto3_raw_data: "type_defs.CreateConnectionApiKeyAuthRequestParametersTypeDef" = (
        dataclasses.field()
    )

    ApiKeyName = field("ApiKeyName")
    ApiKeyValue = field("ApiKeyValue")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateConnectionApiKeyAuthRequestParametersTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateConnectionApiKeyAuthRequestParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateConnectionBasicAuthRequestParameters:
    boto3_raw_data: "type_defs.CreateConnectionBasicAuthRequestParametersTypeDef" = (
        dataclasses.field()
    )

    Username = field("Username")
    Password = field("Password")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateConnectionBasicAuthRequestParametersTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateConnectionBasicAuthRequestParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateConnectionOAuthClientRequestParameters:
    boto3_raw_data: "type_defs.CreateConnectionOAuthClientRequestParametersTypeDef" = (
        dataclasses.field()
    )

    ClientID = field("ClientID")
    ClientSecret = field("ClientSecret")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateConnectionOAuthClientRequestParametersTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateConnectionOAuthClientRequestParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EndpointEventBus:
    boto3_raw_data: "type_defs.EndpointEventBusTypeDef" = dataclasses.field()

    EventBusArn = field("EventBusArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EndpointEventBusTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EndpointEventBusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicationConfig:
    boto3_raw_data: "type_defs.ReplicationConfigTypeDef" = dataclasses.field()

    State = field("State")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReplicationConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplicationConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeadLetterConfig:
    boto3_raw_data: "type_defs.DeadLetterConfigTypeDef" = dataclasses.field()

    Arn = field("Arn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeadLetterConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeadLetterConfigTypeDef"]
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

    IncludeDetail = field("IncludeDetail")
    Level = field("Level")

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
class CreatePartnerEventSourceRequest:
    boto3_raw_data: "type_defs.CreatePartnerEventSourceRequestTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    Account = field("Account")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreatePartnerEventSourceRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePartnerEventSourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeactivateEventSourceRequest:
    boto3_raw_data: "type_defs.DeactivateEventSourceRequestTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeactivateEventSourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeactivateEventSourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeauthorizeConnectionRequest:
    boto3_raw_data: "type_defs.DeauthorizeConnectionRequestTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeauthorizeConnectionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeauthorizeConnectionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteApiDestinationRequest:
    boto3_raw_data: "type_defs.DeleteApiDestinationRequestTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteApiDestinationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteApiDestinationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteArchiveRequest:
    boto3_raw_data: "type_defs.DeleteArchiveRequestTypeDef" = dataclasses.field()

    ArchiveName = field("ArchiveName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteArchiveRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteArchiveRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteConnectionRequest:
    boto3_raw_data: "type_defs.DeleteConnectionRequestTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteConnectionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteConnectionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteEndpointRequest:
    boto3_raw_data: "type_defs.DeleteEndpointRequestTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteEndpointRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteEndpointRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteEventBusRequest:
    boto3_raw_data: "type_defs.DeleteEventBusRequestTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteEventBusRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteEventBusRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePartnerEventSourceRequest:
    boto3_raw_data: "type_defs.DeletePartnerEventSourceRequestTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    Account = field("Account")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeletePartnerEventSourceRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePartnerEventSourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRuleRequest:
    boto3_raw_data: "type_defs.DeleteRuleRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    EventBusName = field("EventBusName")
    Force = field("Force")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteRuleRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRuleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeApiDestinationRequest:
    boto3_raw_data: "type_defs.DescribeApiDestinationRequestTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeApiDestinationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeApiDestinationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeArchiveRequest:
    boto3_raw_data: "type_defs.DescribeArchiveRequestTypeDef" = dataclasses.field()

    ArchiveName = field("ArchiveName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeArchiveRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeArchiveRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeConnectionResourceParameters:
    boto3_raw_data: "type_defs.DescribeConnectionResourceParametersTypeDef" = (
        dataclasses.field()
    )

    ResourceConfigurationArn = field("ResourceConfigurationArn")
    ResourceAssociationArn = field("ResourceAssociationArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeConnectionResourceParametersTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeConnectionResourceParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeConnectionRequest:
    boto3_raw_data: "type_defs.DescribeConnectionRequestTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeConnectionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeConnectionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEndpointRequest:
    boto3_raw_data: "type_defs.DescribeEndpointRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    HomeRegion = field("HomeRegion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeEndpointRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEndpointRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEventBusRequest:
    boto3_raw_data: "type_defs.DescribeEventBusRequestTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeEventBusRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEventBusRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEventSourceRequest:
    boto3_raw_data: "type_defs.DescribeEventSourceRequestTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeEventSourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEventSourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePartnerEventSourceRequest:
    boto3_raw_data: "type_defs.DescribePartnerEventSourceRequestTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribePartnerEventSourceRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePartnerEventSourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReplayRequest:
    boto3_raw_data: "type_defs.DescribeReplayRequestTypeDef" = dataclasses.field()

    ReplayName = field("ReplayName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeReplayRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeReplayRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplayDestinationOutput:
    boto3_raw_data: "type_defs.ReplayDestinationOutputTypeDef" = dataclasses.field()

    Arn = field("Arn")
    FilterArns = field("FilterArns")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReplayDestinationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplayDestinationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRuleRequest:
    boto3_raw_data: "type_defs.DescribeRuleRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    EventBusName = field("EventBusName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeRuleRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRuleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisableRuleRequest:
    boto3_raw_data: "type_defs.DisableRuleRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    EventBusName = field("EventBusName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DisableRuleRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisableRuleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PlacementConstraint:
    boto3_raw_data: "type_defs.PlacementConstraintTypeDef" = dataclasses.field()

    type = field("type")
    expression = field("expression")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PlacementConstraintTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PlacementConstraintTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PlacementStrategy:
    boto3_raw_data: "type_defs.PlacementStrategyTypeDef" = dataclasses.field()

    type = field("type")
    field = field("field")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PlacementStrategyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PlacementStrategyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnableRuleRequest:
    boto3_raw_data: "type_defs.EnableRuleRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    EventBusName = field("EventBusName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EnableRuleRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnableRuleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventBus:
    boto3_raw_data: "type_defs.EventBusTypeDef" = dataclasses.field()

    Name = field("Name")
    Arn = field("Arn")
    Description = field("Description")
    Policy = field("Policy")
    CreationTime = field("CreationTime")
    LastModifiedTime = field("LastModifiedTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EventBusTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EventBusTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventSource:
    boto3_raw_data: "type_defs.EventSourceTypeDef" = dataclasses.field()

    Arn = field("Arn")
    CreatedBy = field("CreatedBy")
    CreationTime = field("CreationTime")
    ExpirationTime = field("ExpirationTime")
    Name = field("Name")
    State = field("State")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EventSourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EventSourceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Primary:
    boto3_raw_data: "type_defs.PrimaryTypeDef" = dataclasses.field()

    HealthCheck = field("HealthCheck")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PrimaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PrimaryTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Secondary:
    boto3_raw_data: "type_defs.SecondaryTypeDef" = dataclasses.field()

    Route = field("Route")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SecondaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SecondaryTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HttpParametersOutput:
    boto3_raw_data: "type_defs.HttpParametersOutputTypeDef" = dataclasses.field()

    PathParameterValues = field("PathParameterValues")
    HeaderParameters = field("HeaderParameters")
    QueryStringParameters = field("QueryStringParameters")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HttpParametersOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HttpParametersOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HttpParameters:
    boto3_raw_data: "type_defs.HttpParametersTypeDef" = dataclasses.field()

    PathParameterValues = field("PathParameterValues")
    HeaderParameters = field("HeaderParameters")
    QueryStringParameters = field("QueryStringParameters")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HttpParametersTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.HttpParametersTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputTransformerOutput:
    boto3_raw_data: "type_defs.InputTransformerOutputTypeDef" = dataclasses.field()

    InputTemplate = field("InputTemplate")
    InputPathsMap = field("InputPathsMap")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InputTransformerOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InputTransformerOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputTransformer:
    boto3_raw_data: "type_defs.InputTransformerTypeDef" = dataclasses.field()

    InputTemplate = field("InputTemplate")
    InputPathsMap = field("InputPathsMap")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InputTransformerTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InputTransformerTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KinesisParameters:
    boto3_raw_data: "type_defs.KinesisParametersTypeDef" = dataclasses.field()

    PartitionKeyPath = field("PartitionKeyPath")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.KinesisParametersTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KinesisParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListApiDestinationsRequest:
    boto3_raw_data: "type_defs.ListApiDestinationsRequestTypeDef" = dataclasses.field()

    NamePrefix = field("NamePrefix")
    ConnectionArn = field("ConnectionArn")
    NextToken = field("NextToken")
    Limit = field("Limit")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListApiDestinationsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApiDestinationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListArchivesRequest:
    boto3_raw_data: "type_defs.ListArchivesRequestTypeDef" = dataclasses.field()

    NamePrefix = field("NamePrefix")
    EventSourceArn = field("EventSourceArn")
    State = field("State")
    NextToken = field("NextToken")
    Limit = field("Limit")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListArchivesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListArchivesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConnectionsRequest:
    boto3_raw_data: "type_defs.ListConnectionsRequestTypeDef" = dataclasses.field()

    NamePrefix = field("NamePrefix")
    ConnectionState = field("ConnectionState")
    NextToken = field("NextToken")
    Limit = field("Limit")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListConnectionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConnectionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEndpointsRequest:
    boto3_raw_data: "type_defs.ListEndpointsRequestTypeDef" = dataclasses.field()

    NamePrefix = field("NamePrefix")
    HomeRegion = field("HomeRegion")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEndpointsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEndpointsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEventBusesRequest:
    boto3_raw_data: "type_defs.ListEventBusesRequestTypeDef" = dataclasses.field()

    NamePrefix = field("NamePrefix")
    NextToken = field("NextToken")
    Limit = field("Limit")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEventBusesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEventBusesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEventSourcesRequest:
    boto3_raw_data: "type_defs.ListEventSourcesRequestTypeDef" = dataclasses.field()

    NamePrefix = field("NamePrefix")
    NextToken = field("NextToken")
    Limit = field("Limit")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEventSourcesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEventSourcesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPartnerEventSourceAccountsRequest:
    boto3_raw_data: "type_defs.ListPartnerEventSourceAccountsRequestTypeDef" = (
        dataclasses.field()
    )

    EventSourceName = field("EventSourceName")
    NextToken = field("NextToken")
    Limit = field("Limit")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListPartnerEventSourceAccountsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPartnerEventSourceAccountsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PartnerEventSourceAccount:
    boto3_raw_data: "type_defs.PartnerEventSourceAccountTypeDef" = dataclasses.field()

    Account = field("Account")
    CreationTime = field("CreationTime")
    ExpirationTime = field("ExpirationTime")
    State = field("State")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PartnerEventSourceAccountTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PartnerEventSourceAccountTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPartnerEventSourcesRequest:
    boto3_raw_data: "type_defs.ListPartnerEventSourcesRequestTypeDef" = (
        dataclasses.field()
    )

    NamePrefix = field("NamePrefix")
    NextToken = field("NextToken")
    Limit = field("Limit")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListPartnerEventSourcesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPartnerEventSourcesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PartnerEventSource:
    boto3_raw_data: "type_defs.PartnerEventSourceTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PartnerEventSourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PartnerEventSourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListReplaysRequest:
    boto3_raw_data: "type_defs.ListReplaysRequestTypeDef" = dataclasses.field()

    NamePrefix = field("NamePrefix")
    State = field("State")
    EventSourceArn = field("EventSourceArn")
    NextToken = field("NextToken")
    Limit = field("Limit")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListReplaysRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListReplaysRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Replay:
    boto3_raw_data: "type_defs.ReplayTypeDef" = dataclasses.field()

    ReplayName = field("ReplayName")
    EventSourceArn = field("EventSourceArn")
    State = field("State")
    StateReason = field("StateReason")
    EventStartTime = field("EventStartTime")
    EventEndTime = field("EventEndTime")
    EventLastReplayedTime = field("EventLastReplayedTime")
    ReplayStartTime = field("ReplayStartTime")
    ReplayEndTime = field("ReplayEndTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReplayTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ReplayTypeDef"]]
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
class ListRuleNamesByTargetRequest:
    boto3_raw_data: "type_defs.ListRuleNamesByTargetRequestTypeDef" = (
        dataclasses.field()
    )

    TargetArn = field("TargetArn")
    EventBusName = field("EventBusName")
    NextToken = field("NextToken")
    Limit = field("Limit")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRuleNamesByTargetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRuleNamesByTargetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRulesRequest:
    boto3_raw_data: "type_defs.ListRulesRequestTypeDef" = dataclasses.field()

    NamePrefix = field("NamePrefix")
    EventBusName = field("EventBusName")
    NextToken = field("NextToken")
    Limit = field("Limit")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListRulesRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRulesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Rule:
    boto3_raw_data: "type_defs.RuleTypeDef" = dataclasses.field()

    Name = field("Name")
    Arn = field("Arn")
    EventPattern = field("EventPattern")
    State = field("State")
    Description = field("Description")
    ScheduleExpression = field("ScheduleExpression")
    RoleArn = field("RoleArn")
    ManagedBy = field("ManagedBy")
    EventBusName = field("EventBusName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RuleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RuleTypeDef"]]
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
class ListTargetsByRuleRequest:
    boto3_raw_data: "type_defs.ListTargetsByRuleRequestTypeDef" = dataclasses.field()

    Rule = field("Rule")
    EventBusName = field("EventBusName")
    NextToken = field("NextToken")
    Limit = field("Limit")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTargetsByRuleRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTargetsByRuleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutEventsResultEntry:
    boto3_raw_data: "type_defs.PutEventsResultEntryTypeDef" = dataclasses.field()

    EventId = field("EventId")
    ErrorCode = field("ErrorCode")
    ErrorMessage = field("ErrorMessage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutEventsResultEntryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutEventsResultEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutPartnerEventsResultEntry:
    boto3_raw_data: "type_defs.PutPartnerEventsResultEntryTypeDef" = dataclasses.field()

    EventId = field("EventId")
    ErrorCode = field("ErrorCode")
    ErrorMessage = field("ErrorMessage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutPartnerEventsResultEntryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutPartnerEventsResultEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutTargetsResultEntry:
    boto3_raw_data: "type_defs.PutTargetsResultEntryTypeDef" = dataclasses.field()

    TargetId = field("TargetId")
    ErrorCode = field("ErrorCode")
    ErrorMessage = field("ErrorMessage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutTargetsResultEntryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutTargetsResultEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RedshiftDataParametersOutput:
    boto3_raw_data: "type_defs.RedshiftDataParametersOutputTypeDef" = (
        dataclasses.field()
    )

    Database = field("Database")
    SecretManagerArn = field("SecretManagerArn")
    DbUser = field("DbUser")
    Sql = field("Sql")
    StatementName = field("StatementName")
    WithEvent = field("WithEvent")
    Sqls = field("Sqls")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RedshiftDataParametersOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RedshiftDataParametersOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RedshiftDataParameters:
    boto3_raw_data: "type_defs.RedshiftDataParametersTypeDef" = dataclasses.field()

    Database = field("Database")
    SecretManagerArn = field("SecretManagerArn")
    DbUser = field("DbUser")
    Sql = field("Sql")
    StatementName = field("StatementName")
    WithEvent = field("WithEvent")
    Sqls = field("Sqls")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RedshiftDataParametersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RedshiftDataParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemovePermissionRequest:
    boto3_raw_data: "type_defs.RemovePermissionRequestTypeDef" = dataclasses.field()

    StatementId = field("StatementId")
    RemoveAllPermissions = field("RemoveAllPermissions")
    EventBusName = field("EventBusName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RemovePermissionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemovePermissionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveTargetsRequest:
    boto3_raw_data: "type_defs.RemoveTargetsRequestTypeDef" = dataclasses.field()

    Rule = field("Rule")
    Ids = field("Ids")
    EventBusName = field("EventBusName")
    Force = field("Force")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RemoveTargetsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveTargetsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveTargetsResultEntry:
    boto3_raw_data: "type_defs.RemoveTargetsResultEntryTypeDef" = dataclasses.field()

    TargetId = field("TargetId")
    ErrorCode = field("ErrorCode")
    ErrorMessage = field("ErrorMessage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RemoveTargetsResultEntryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveTargetsResultEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplayDestination:
    boto3_raw_data: "type_defs.ReplayDestinationTypeDef" = dataclasses.field()

    Arn = field("Arn")
    FilterArns = field("FilterArns")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReplayDestinationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplayDestinationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RetryPolicy:
    boto3_raw_data: "type_defs.RetryPolicyTypeDef" = dataclasses.field()

    MaximumRetryAttempts = field("MaximumRetryAttempts")
    MaximumEventAgeInSeconds = field("MaximumEventAgeInSeconds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RetryPolicyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RetryPolicyTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RunCommandTargetOutput:
    boto3_raw_data: "type_defs.RunCommandTargetOutputTypeDef" = dataclasses.field()

    Key = field("Key")
    Values = field("Values")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RunCommandTargetOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RunCommandTargetOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RunCommandTarget:
    boto3_raw_data: "type_defs.RunCommandTargetTypeDef" = dataclasses.field()

    Key = field("Key")
    Values = field("Values")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RunCommandTargetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RunCommandTargetTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SageMakerPipelineParameter:
    boto3_raw_data: "type_defs.SageMakerPipelineParameterTypeDef" = dataclasses.field()

    Name = field("Name")
    Value = field("Value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SageMakerPipelineParameterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SageMakerPipelineParameterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SqsParameters:
    boto3_raw_data: "type_defs.SqsParametersTypeDef" = dataclasses.field()

    MessageGroupId = field("MessageGroupId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SqsParametersTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SqsParametersTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestEventPatternRequest:
    boto3_raw_data: "type_defs.TestEventPatternRequestTypeDef" = dataclasses.field()

    EventPattern = field("EventPattern")
    Event = field("Event")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TestEventPatternRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TestEventPatternRequestTypeDef"]
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
class UpdateApiDestinationRequest:
    boto3_raw_data: "type_defs.UpdateApiDestinationRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    Description = field("Description")
    ConnectionArn = field("ConnectionArn")
    InvocationEndpoint = field("InvocationEndpoint")
    HttpMethod = field("HttpMethod")
    InvocationRateLimitPerSecond = field("InvocationRateLimitPerSecond")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateApiDestinationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateApiDestinationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateArchiveRequest:
    boto3_raw_data: "type_defs.UpdateArchiveRequestTypeDef" = dataclasses.field()

    ArchiveName = field("ArchiveName")
    Description = field("Description")
    EventPattern = field("EventPattern")
    RetentionDays = field("RetentionDays")
    KmsKeyIdentifier = field("KmsKeyIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateArchiveRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateArchiveRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateConnectionApiKeyAuthRequestParameters:
    boto3_raw_data: "type_defs.UpdateConnectionApiKeyAuthRequestParametersTypeDef" = (
        dataclasses.field()
    )

    ApiKeyName = field("ApiKeyName")
    ApiKeyValue = field("ApiKeyValue")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateConnectionApiKeyAuthRequestParametersTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateConnectionApiKeyAuthRequestParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateConnectionBasicAuthRequestParameters:
    boto3_raw_data: "type_defs.UpdateConnectionBasicAuthRequestParametersTypeDef" = (
        dataclasses.field()
    )

    Username = field("Username")
    Password = field("Password")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateConnectionBasicAuthRequestParametersTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateConnectionBasicAuthRequestParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateConnectionOAuthClientRequestParameters:
    boto3_raw_data: "type_defs.UpdateConnectionOAuthClientRequestParametersTypeDef" = (
        dataclasses.field()
    )

    ClientID = field("ClientID")
    ClientSecret = field("ClientSecret")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateConnectionOAuthClientRequestParametersTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateConnectionOAuthClientRequestParametersTypeDef"]
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

    @cached_property
    def awsvpcConfiguration(self):  # pragma: no cover
        return AwsVpcConfigurationOutput.make_one(
            self.boto3_raw_data["awsvpcConfiguration"]
        )

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
class BatchParameters:
    boto3_raw_data: "type_defs.BatchParametersTypeDef" = dataclasses.field()

    JobDefinition = field("JobDefinition")
    JobName = field("JobName")

    @cached_property
    def ArrayProperties(self):  # pragma: no cover
        return BatchArrayProperties.make_one(self.boto3_raw_data["ArrayProperties"])

    @cached_property
    def RetryStrategy(self):  # pragma: no cover
        return BatchRetryStrategy.make_one(self.boto3_raw_data["RetryStrategy"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BatchParametersTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BatchParametersTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelReplayResponse:
    boto3_raw_data: "type_defs.CancelReplayResponseTypeDef" = dataclasses.field()

    ReplayArn = field("ReplayArn")
    State = field("State")
    StateReason = field("StateReason")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CancelReplayResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelReplayResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateApiDestinationResponse:
    boto3_raw_data: "type_defs.CreateApiDestinationResponseTypeDef" = (
        dataclasses.field()
    )

    ApiDestinationArn = field("ApiDestinationArn")
    ApiDestinationState = field("ApiDestinationState")
    CreationTime = field("CreationTime")
    LastModifiedTime = field("LastModifiedTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateApiDestinationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateApiDestinationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateArchiveResponse:
    boto3_raw_data: "type_defs.CreateArchiveResponseTypeDef" = dataclasses.field()

    ArchiveArn = field("ArchiveArn")
    State = field("State")
    StateReason = field("StateReason")
    CreationTime = field("CreationTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateArchiveResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateArchiveResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateConnectionResponse:
    boto3_raw_data: "type_defs.CreateConnectionResponseTypeDef" = dataclasses.field()

    ConnectionArn = field("ConnectionArn")
    ConnectionState = field("ConnectionState")
    CreationTime = field("CreationTime")
    LastModifiedTime = field("LastModifiedTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateConnectionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateConnectionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePartnerEventSourceResponse:
    boto3_raw_data: "type_defs.CreatePartnerEventSourceResponseTypeDef" = (
        dataclasses.field()
    )

    EventSourceArn = field("EventSourceArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreatePartnerEventSourceResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePartnerEventSourceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeauthorizeConnectionResponse:
    boto3_raw_data: "type_defs.DeauthorizeConnectionResponseTypeDef" = (
        dataclasses.field()
    )

    ConnectionArn = field("ConnectionArn")
    ConnectionState = field("ConnectionState")
    CreationTime = field("CreationTime")
    LastModifiedTime = field("LastModifiedTime")
    LastAuthorizedTime = field("LastAuthorizedTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeauthorizeConnectionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeauthorizeConnectionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteConnectionResponse:
    boto3_raw_data: "type_defs.DeleteConnectionResponseTypeDef" = dataclasses.field()

    ConnectionArn = field("ConnectionArn")
    ConnectionState = field("ConnectionState")
    CreationTime = field("CreationTime")
    LastModifiedTime = field("LastModifiedTime")
    LastAuthorizedTime = field("LastAuthorizedTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteConnectionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteConnectionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeApiDestinationResponse:
    boto3_raw_data: "type_defs.DescribeApiDestinationResponseTypeDef" = (
        dataclasses.field()
    )

    ApiDestinationArn = field("ApiDestinationArn")
    Name = field("Name")
    Description = field("Description")
    ApiDestinationState = field("ApiDestinationState")
    ConnectionArn = field("ConnectionArn")
    InvocationEndpoint = field("InvocationEndpoint")
    HttpMethod = field("HttpMethod")
    InvocationRateLimitPerSecond = field("InvocationRateLimitPerSecond")
    CreationTime = field("CreationTime")
    LastModifiedTime = field("LastModifiedTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeApiDestinationResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeApiDestinationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeArchiveResponse:
    boto3_raw_data: "type_defs.DescribeArchiveResponseTypeDef" = dataclasses.field()

    ArchiveArn = field("ArchiveArn")
    ArchiveName = field("ArchiveName")
    EventSourceArn = field("EventSourceArn")
    Description = field("Description")
    EventPattern = field("EventPattern")
    State = field("State")
    StateReason = field("StateReason")
    KmsKeyIdentifier = field("KmsKeyIdentifier")
    RetentionDays = field("RetentionDays")
    SizeBytes = field("SizeBytes")
    EventCount = field("EventCount")
    CreationTime = field("CreationTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeArchiveResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeArchiveResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEventSourceResponse:
    boto3_raw_data: "type_defs.DescribeEventSourceResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    CreatedBy = field("CreatedBy")
    CreationTime = field("CreationTime")
    ExpirationTime = field("ExpirationTime")
    Name = field("Name")
    State = field("State")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeEventSourceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEventSourceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePartnerEventSourceResponse:
    boto3_raw_data: "type_defs.DescribePartnerEventSourceResponseTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    Name = field("Name")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribePartnerEventSourceResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePartnerEventSourceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRuleResponse:
    boto3_raw_data: "type_defs.DescribeRuleResponseTypeDef" = dataclasses.field()

    Name = field("Name")
    Arn = field("Arn")
    EventPattern = field("EventPattern")
    ScheduleExpression = field("ScheduleExpression")
    State = field("State")
    Description = field("Description")
    RoleArn = field("RoleArn")
    ManagedBy = field("ManagedBy")
    EventBusName = field("EventBusName")
    CreatedBy = field("CreatedBy")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeRuleResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRuleResponseTypeDef"]
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
class ListApiDestinationsResponse:
    boto3_raw_data: "type_defs.ListApiDestinationsResponseTypeDef" = dataclasses.field()

    @cached_property
    def ApiDestinations(self):  # pragma: no cover
        return ApiDestination.make_many(self.boto3_raw_data["ApiDestinations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListApiDestinationsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApiDestinationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListArchivesResponse:
    boto3_raw_data: "type_defs.ListArchivesResponseTypeDef" = dataclasses.field()

    @cached_property
    def Archives(self):  # pragma: no cover
        return Archive.make_many(self.boto3_raw_data["Archives"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListArchivesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListArchivesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRuleNamesByTargetResponse:
    boto3_raw_data: "type_defs.ListRuleNamesByTargetResponseTypeDef" = (
        dataclasses.field()
    )

    RuleNames = field("RuleNames")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListRuleNamesByTargetResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRuleNamesByTargetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutRuleResponse:
    boto3_raw_data: "type_defs.PutRuleResponseTypeDef" = dataclasses.field()

    RuleArn = field("RuleArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PutRuleResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PutRuleResponseTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartReplayResponse:
    boto3_raw_data: "type_defs.StartReplayResponseTypeDef" = dataclasses.field()

    ReplayArn = field("ReplayArn")
    State = field("State")
    StateReason = field("StateReason")
    ReplayStartTime = field("ReplayStartTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartReplayResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartReplayResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestEventPatternResponse:
    boto3_raw_data: "type_defs.TestEventPatternResponseTypeDef" = dataclasses.field()

    Result = field("Result")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TestEventPatternResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TestEventPatternResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateApiDestinationResponse:
    boto3_raw_data: "type_defs.UpdateApiDestinationResponseTypeDef" = (
        dataclasses.field()
    )

    ApiDestinationArn = field("ApiDestinationArn")
    ApiDestinationState = field("ApiDestinationState")
    CreationTime = field("CreationTime")
    LastModifiedTime = field("LastModifiedTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateApiDestinationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateApiDestinationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateArchiveResponse:
    boto3_raw_data: "type_defs.UpdateArchiveResponseTypeDef" = dataclasses.field()

    ArchiveArn = field("ArchiveArn")
    State = field("State")
    StateReason = field("StateReason")
    CreationTime = field("CreationTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateArchiveResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateArchiveResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateConnectionResponse:
    boto3_raw_data: "type_defs.UpdateConnectionResponseTypeDef" = dataclasses.field()

    ConnectionArn = field("ConnectionArn")
    ConnectionState = field("ConnectionState")
    CreationTime = field("CreationTime")
    LastModifiedTime = field("LastModifiedTime")
    LastAuthorizedTime = field("LastAuthorizedTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateConnectionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateConnectionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutPermissionRequest:
    boto3_raw_data: "type_defs.PutPermissionRequestTypeDef" = dataclasses.field()

    EventBusName = field("EventBusName")
    Action = field("Action")
    Principal = field("Principal")
    StatementId = field("StatementId")

    @cached_property
    def Condition(self):  # pragma: no cover
        return Condition.make_one(self.boto3_raw_data["Condition"])

    Policy = field("Policy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutPermissionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutPermissionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConnectionHttpParametersOutput:
    boto3_raw_data: "type_defs.ConnectionHttpParametersOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def HeaderParameters(self):  # pragma: no cover
        return ConnectionHeaderParameter.make_many(
            self.boto3_raw_data["HeaderParameters"]
        )

    @cached_property
    def QueryStringParameters(self):  # pragma: no cover
        return ConnectionQueryStringParameter.make_many(
            self.boto3_raw_data["QueryStringParameters"]
        )

    @cached_property
    def BodyParameters(self):  # pragma: no cover
        return ConnectionBodyParameter.make_many(self.boto3_raw_data["BodyParameters"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ConnectionHttpParametersOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConnectionHttpParametersOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConnectionHttpParameters:
    boto3_raw_data: "type_defs.ConnectionHttpParametersTypeDef" = dataclasses.field()

    @cached_property
    def HeaderParameters(self):  # pragma: no cover
        return ConnectionHeaderParameter.make_many(
            self.boto3_raw_data["HeaderParameters"]
        )

    @cached_property
    def QueryStringParameters(self):  # pragma: no cover
        return ConnectionQueryStringParameter.make_many(
            self.boto3_raw_data["QueryStringParameters"]
        )

    @cached_property
    def BodyParameters(self):  # pragma: no cover
        return ConnectionBodyParameter.make_many(self.boto3_raw_data["BodyParameters"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConnectionHttpParametersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConnectionHttpParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConnectionsResponse:
    boto3_raw_data: "type_defs.ListConnectionsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Connections(self):  # pragma: no cover
        return Connection.make_many(self.boto3_raw_data["Connections"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListConnectionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConnectionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConnectivityResourceParameters:
    boto3_raw_data: "type_defs.ConnectivityResourceParametersTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ResourceParameters(self):  # pragma: no cover
        return ConnectivityResourceConfigurationArn.make_one(
            self.boto3_raw_data["ResourceParameters"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ConnectivityResourceParametersTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConnectivityResourceParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEventBusResponse:
    boto3_raw_data: "type_defs.CreateEventBusResponseTypeDef" = dataclasses.field()

    EventBusArn = field("EventBusArn")
    Description = field("Description")
    KmsKeyIdentifier = field("KmsKeyIdentifier")

    @cached_property
    def DeadLetterConfig(self):  # pragma: no cover
        return DeadLetterConfig.make_one(self.boto3_raw_data["DeadLetterConfig"])

    @cached_property
    def LogConfig(self):  # pragma: no cover
        return LogConfig.make_one(self.boto3_raw_data["LogConfig"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateEventBusResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEventBusResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEventBusResponse:
    boto3_raw_data: "type_defs.DescribeEventBusResponseTypeDef" = dataclasses.field()

    Name = field("Name")
    Arn = field("Arn")
    Description = field("Description")
    KmsKeyIdentifier = field("KmsKeyIdentifier")

    @cached_property
    def DeadLetterConfig(self):  # pragma: no cover
        return DeadLetterConfig.make_one(self.boto3_raw_data["DeadLetterConfig"])

    Policy = field("Policy")

    @cached_property
    def LogConfig(self):  # pragma: no cover
        return LogConfig.make_one(self.boto3_raw_data["LogConfig"])

    CreationTime = field("CreationTime")
    LastModifiedTime = field("LastModifiedTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeEventBusResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEventBusResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateEventBusRequest:
    boto3_raw_data: "type_defs.UpdateEventBusRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    KmsKeyIdentifier = field("KmsKeyIdentifier")
    Description = field("Description")

    @cached_property
    def DeadLetterConfig(self):  # pragma: no cover
        return DeadLetterConfig.make_one(self.boto3_raw_data["DeadLetterConfig"])

    @cached_property
    def LogConfig(self):  # pragma: no cover
        return LogConfig.make_one(self.boto3_raw_data["LogConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateEventBusRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateEventBusRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateEventBusResponse:
    boto3_raw_data: "type_defs.UpdateEventBusResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Name = field("Name")
    KmsKeyIdentifier = field("KmsKeyIdentifier")
    Description = field("Description")

    @cached_property
    def DeadLetterConfig(self):  # pragma: no cover
        return DeadLetterConfig.make_one(self.boto3_raw_data["DeadLetterConfig"])

    @cached_property
    def LogConfig(self):  # pragma: no cover
        return LogConfig.make_one(self.boto3_raw_data["LogConfig"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateEventBusResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateEventBusResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEventBusRequest:
    boto3_raw_data: "type_defs.CreateEventBusRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    EventSourceName = field("EventSourceName")
    Description = field("Description")
    KmsKeyIdentifier = field("KmsKeyIdentifier")

    @cached_property
    def DeadLetterConfig(self):  # pragma: no cover
        return DeadLetterConfig.make_one(self.boto3_raw_data["DeadLetterConfig"])

    @cached_property
    def LogConfig(self):  # pragma: no cover
        return LogConfig.make_one(self.boto3_raw_data["LogConfig"])

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateEventBusRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEventBusRequestTypeDef"]
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
class PutRuleRequest:
    boto3_raw_data: "type_defs.PutRuleRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    ScheduleExpression = field("ScheduleExpression")
    EventPattern = field("EventPattern")
    State = field("State")
    Description = field("Description")
    RoleArn = field("RoleArn")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    EventBusName = field("EventBusName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PutRuleRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PutRuleRequestTypeDef"]],
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
class DescribeConnectionConnectivityParameters:
    boto3_raw_data: "type_defs.DescribeConnectionConnectivityParametersTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ResourceParameters(self):  # pragma: no cover
        return DescribeConnectionResourceParameters.make_one(
            self.boto3_raw_data["ResourceParameters"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeConnectionConnectivityParametersTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeConnectionConnectivityParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReplayResponse:
    boto3_raw_data: "type_defs.DescribeReplayResponseTypeDef" = dataclasses.field()

    ReplayName = field("ReplayName")
    ReplayArn = field("ReplayArn")
    Description = field("Description")
    State = field("State")
    StateReason = field("StateReason")
    EventSourceArn = field("EventSourceArn")

    @cached_property
    def Destination(self):  # pragma: no cover
        return ReplayDestinationOutput.make_one(self.boto3_raw_data["Destination"])

    EventStartTime = field("EventStartTime")
    EventEndTime = field("EventEndTime")
    EventLastReplayedTime = field("EventLastReplayedTime")
    ReplayStartTime = field("ReplayStartTime")
    ReplayEndTime = field("ReplayEndTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeReplayResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeReplayResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEventBusesResponse:
    boto3_raw_data: "type_defs.ListEventBusesResponseTypeDef" = dataclasses.field()

    @cached_property
    def EventBuses(self):  # pragma: no cover
        return EventBus.make_many(self.boto3_raw_data["EventBuses"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEventBusesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEventBusesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEventSourcesResponse:
    boto3_raw_data: "type_defs.ListEventSourcesResponseTypeDef" = dataclasses.field()

    @cached_property
    def EventSources(self):  # pragma: no cover
        return EventSource.make_many(self.boto3_raw_data["EventSources"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEventSourcesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEventSourcesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FailoverConfig:
    boto3_raw_data: "type_defs.FailoverConfigTypeDef" = dataclasses.field()

    @cached_property
    def Primary(self):  # pragma: no cover
        return Primary.make_one(self.boto3_raw_data["Primary"])

    @cached_property
    def Secondary(self):  # pragma: no cover
        return Secondary.make_one(self.boto3_raw_data["Secondary"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FailoverConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FailoverConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPartnerEventSourceAccountsResponse:
    boto3_raw_data: "type_defs.ListPartnerEventSourceAccountsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PartnerEventSourceAccounts(self):  # pragma: no cover
        return PartnerEventSourceAccount.make_many(
            self.boto3_raw_data["PartnerEventSourceAccounts"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListPartnerEventSourceAccountsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPartnerEventSourceAccountsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPartnerEventSourcesResponse:
    boto3_raw_data: "type_defs.ListPartnerEventSourcesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PartnerEventSources(self):  # pragma: no cover
        return PartnerEventSource.make_many(self.boto3_raw_data["PartnerEventSources"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListPartnerEventSourcesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPartnerEventSourcesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListReplaysResponse:
    boto3_raw_data: "type_defs.ListReplaysResponseTypeDef" = dataclasses.field()

    @cached_property
    def Replays(self):  # pragma: no cover
        return Replay.make_many(self.boto3_raw_data["Replays"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListReplaysResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListReplaysResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRuleNamesByTargetRequestPaginate:
    boto3_raw_data: "type_defs.ListRuleNamesByTargetRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    TargetArn = field("TargetArn")
    EventBusName = field("EventBusName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListRuleNamesByTargetRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRuleNamesByTargetRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRulesRequestPaginate:
    boto3_raw_data: "type_defs.ListRulesRequestPaginateTypeDef" = dataclasses.field()

    NamePrefix = field("NamePrefix")
    EventBusName = field("EventBusName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRulesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRulesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTargetsByRuleRequestPaginate:
    boto3_raw_data: "type_defs.ListTargetsByRuleRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    Rule = field("Rule")
    EventBusName = field("EventBusName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListTargetsByRuleRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTargetsByRuleRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRulesResponse:
    boto3_raw_data: "type_defs.ListRulesResponseTypeDef" = dataclasses.field()

    @cached_property
    def Rules(self):  # pragma: no cover
        return Rule.make_many(self.boto3_raw_data["Rules"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListRulesResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRulesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutEventsRequestEntry:
    boto3_raw_data: "type_defs.PutEventsRequestEntryTypeDef" = dataclasses.field()

    Time = field("Time")
    Source = field("Source")
    Resources = field("Resources")
    DetailType = field("DetailType")
    Detail = field("Detail")
    EventBusName = field("EventBusName")
    TraceHeader = field("TraceHeader")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutEventsRequestEntryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutEventsRequestEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutPartnerEventsRequestEntry:
    boto3_raw_data: "type_defs.PutPartnerEventsRequestEntryTypeDef" = (
        dataclasses.field()
    )

    Time = field("Time")
    Source = field("Source")
    Resources = field("Resources")
    DetailType = field("DetailType")
    Detail = field("Detail")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutPartnerEventsRequestEntryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutPartnerEventsRequestEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutEventsResponse:
    boto3_raw_data: "type_defs.PutEventsResponseTypeDef" = dataclasses.field()

    FailedEntryCount = field("FailedEntryCount")

    @cached_property
    def Entries(self):  # pragma: no cover
        return PutEventsResultEntry.make_many(self.boto3_raw_data["Entries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PutEventsResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutEventsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutPartnerEventsResponse:
    boto3_raw_data: "type_defs.PutPartnerEventsResponseTypeDef" = dataclasses.field()

    FailedEntryCount = field("FailedEntryCount")

    @cached_property
    def Entries(self):  # pragma: no cover
        return PutPartnerEventsResultEntry.make_many(self.boto3_raw_data["Entries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutPartnerEventsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutPartnerEventsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutTargetsResponse:
    boto3_raw_data: "type_defs.PutTargetsResponseTypeDef" = dataclasses.field()

    FailedEntryCount = field("FailedEntryCount")

    @cached_property
    def FailedEntries(self):  # pragma: no cover
        return PutTargetsResultEntry.make_many(self.boto3_raw_data["FailedEntries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutTargetsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutTargetsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveTargetsResponse:
    boto3_raw_data: "type_defs.RemoveTargetsResponseTypeDef" = dataclasses.field()

    FailedEntryCount = field("FailedEntryCount")

    @cached_property
    def FailedEntries(self):  # pragma: no cover
        return RemoveTargetsResultEntry.make_many(self.boto3_raw_data["FailedEntries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RemoveTargetsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveTargetsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RunCommandParametersOutput:
    boto3_raw_data: "type_defs.RunCommandParametersOutputTypeDef" = dataclasses.field()

    @cached_property
    def RunCommandTargets(self):  # pragma: no cover
        return RunCommandTargetOutput.make_many(
            self.boto3_raw_data["RunCommandTargets"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RunCommandParametersOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RunCommandParametersOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SageMakerPipelineParametersOutput:
    boto3_raw_data: "type_defs.SageMakerPipelineParametersOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PipelineParameterList(self):  # pragma: no cover
        return SageMakerPipelineParameter.make_many(
            self.boto3_raw_data["PipelineParameterList"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SageMakerPipelineParametersOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SageMakerPipelineParametersOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SageMakerPipelineParameters:
    boto3_raw_data: "type_defs.SageMakerPipelineParametersTypeDef" = dataclasses.field()

    @cached_property
    def PipelineParameterList(self):  # pragma: no cover
        return SageMakerPipelineParameter.make_many(
            self.boto3_raw_data["PipelineParameterList"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SageMakerPipelineParametersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SageMakerPipelineParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EcsParametersOutput:
    boto3_raw_data: "type_defs.EcsParametersOutputTypeDef" = dataclasses.field()

    TaskDefinitionArn = field("TaskDefinitionArn")
    TaskCount = field("TaskCount")
    LaunchType = field("LaunchType")

    @cached_property
    def NetworkConfiguration(self):  # pragma: no cover
        return NetworkConfigurationOutput.make_one(
            self.boto3_raw_data["NetworkConfiguration"]
        )

    PlatformVersion = field("PlatformVersion")
    Group = field("Group")

    @cached_property
    def CapacityProviderStrategy(self):  # pragma: no cover
        return CapacityProviderStrategyItem.make_many(
            self.boto3_raw_data["CapacityProviderStrategy"]
        )

    EnableECSManagedTags = field("EnableECSManagedTags")
    EnableExecuteCommand = field("EnableExecuteCommand")

    @cached_property
    def PlacementConstraints(self):  # pragma: no cover
        return PlacementConstraint.make_many(
            self.boto3_raw_data["PlacementConstraints"]
        )

    @cached_property
    def PlacementStrategy(self):  # pragma: no cover
        return PlacementStrategy.make_many(self.boto3_raw_data["PlacementStrategy"])

    PropagateTags = field("PropagateTags")
    ReferenceId = field("ReferenceId")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EcsParametersOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EcsParametersOutputTypeDef"]
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

    awsvpcConfiguration = field("awsvpcConfiguration")

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
class ConnectionOAuthResponseParameters:
    boto3_raw_data: "type_defs.ConnectionOAuthResponseParametersTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ClientParameters(self):  # pragma: no cover
        return ConnectionOAuthClientResponseParameters.make_one(
            self.boto3_raw_data["ClientParameters"]
        )

    AuthorizationEndpoint = field("AuthorizationEndpoint")
    HttpMethod = field("HttpMethod")

    @cached_property
    def OAuthHttpParameters(self):  # pragma: no cover
        return ConnectionHttpParametersOutput.make_one(
            self.boto3_raw_data["OAuthHttpParameters"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ConnectionOAuthResponseParametersTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConnectionOAuthResponseParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RoutingConfig:
    boto3_raw_data: "type_defs.RoutingConfigTypeDef" = dataclasses.field()

    @cached_property
    def FailoverConfig(self):  # pragma: no cover
        return FailoverConfig.make_one(self.boto3_raw_data["FailoverConfig"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RoutingConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RoutingConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutEventsRequest:
    boto3_raw_data: "type_defs.PutEventsRequestTypeDef" = dataclasses.field()

    @cached_property
    def Entries(self):  # pragma: no cover
        return PutEventsRequestEntry.make_many(self.boto3_raw_data["Entries"])

    EndpointId = field("EndpointId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PutEventsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutEventsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutPartnerEventsRequest:
    boto3_raw_data: "type_defs.PutPartnerEventsRequestTypeDef" = dataclasses.field()

    @cached_property
    def Entries(self):  # pragma: no cover
        return PutPartnerEventsRequestEntry.make_many(self.boto3_raw_data["Entries"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutPartnerEventsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutPartnerEventsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartReplayRequest:
    boto3_raw_data: "type_defs.StartReplayRequestTypeDef" = dataclasses.field()

    ReplayName = field("ReplayName")
    EventSourceArn = field("EventSourceArn")
    EventStartTime = field("EventStartTime")
    EventEndTime = field("EventEndTime")
    Destination = field("Destination")
    Description = field("Description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartReplayRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartReplayRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RunCommandParameters:
    boto3_raw_data: "type_defs.RunCommandParametersTypeDef" = dataclasses.field()

    RunCommandTargets = field("RunCommandTargets")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RunCommandParametersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RunCommandParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TargetOutput:
    boto3_raw_data: "type_defs.TargetOutputTypeDef" = dataclasses.field()

    Id = field("Id")
    Arn = field("Arn")
    RoleArn = field("RoleArn")
    Input = field("Input")
    InputPath = field("InputPath")

    @cached_property
    def InputTransformer(self):  # pragma: no cover
        return InputTransformerOutput.make_one(self.boto3_raw_data["InputTransformer"])

    @cached_property
    def KinesisParameters(self):  # pragma: no cover
        return KinesisParameters.make_one(self.boto3_raw_data["KinesisParameters"])

    @cached_property
    def RunCommandParameters(self):  # pragma: no cover
        return RunCommandParametersOutput.make_one(
            self.boto3_raw_data["RunCommandParameters"]
        )

    @cached_property
    def EcsParameters(self):  # pragma: no cover
        return EcsParametersOutput.make_one(self.boto3_raw_data["EcsParameters"])

    @cached_property
    def BatchParameters(self):  # pragma: no cover
        return BatchParameters.make_one(self.boto3_raw_data["BatchParameters"])

    @cached_property
    def SqsParameters(self):  # pragma: no cover
        return SqsParameters.make_one(self.boto3_raw_data["SqsParameters"])

    @cached_property
    def HttpParameters(self):  # pragma: no cover
        return HttpParametersOutput.make_one(self.boto3_raw_data["HttpParameters"])

    @cached_property
    def RedshiftDataParameters(self):  # pragma: no cover
        return RedshiftDataParametersOutput.make_one(
            self.boto3_raw_data["RedshiftDataParameters"]
        )

    @cached_property
    def SageMakerPipelineParameters(self):  # pragma: no cover
        return SageMakerPipelineParametersOutput.make_one(
            self.boto3_raw_data["SageMakerPipelineParameters"]
        )

    @cached_property
    def DeadLetterConfig(self):  # pragma: no cover
        return DeadLetterConfig.make_one(self.boto3_raw_data["DeadLetterConfig"])

    @cached_property
    def RetryPolicy(self):  # pragma: no cover
        return RetryPolicy.make_one(self.boto3_raw_data["RetryPolicy"])

    @cached_property
    def AppSyncParameters(self):  # pragma: no cover
        return AppSyncParameters.make_one(self.boto3_raw_data["AppSyncParameters"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TargetOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TargetOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConnectionAuthResponseParameters:
    boto3_raw_data: "type_defs.ConnectionAuthResponseParametersTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def BasicAuthParameters(self):  # pragma: no cover
        return ConnectionBasicAuthResponseParameters.make_one(
            self.boto3_raw_data["BasicAuthParameters"]
        )

    @cached_property
    def OAuthParameters(self):  # pragma: no cover
        return ConnectionOAuthResponseParameters.make_one(
            self.boto3_raw_data["OAuthParameters"]
        )

    @cached_property
    def ApiKeyAuthParameters(self):  # pragma: no cover
        return ConnectionApiKeyAuthResponseParameters.make_one(
            self.boto3_raw_data["ApiKeyAuthParameters"]
        )

    @cached_property
    def InvocationHttpParameters(self):  # pragma: no cover
        return ConnectionHttpParametersOutput.make_one(
            self.boto3_raw_data["InvocationHttpParameters"]
        )

    @cached_property
    def ConnectivityParameters(self):  # pragma: no cover
        return DescribeConnectionConnectivityParameters.make_one(
            self.boto3_raw_data["ConnectivityParameters"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ConnectionAuthResponseParametersTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConnectionAuthResponseParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateConnectionOAuthRequestParameters:
    boto3_raw_data: "type_defs.CreateConnectionOAuthRequestParametersTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ClientParameters(self):  # pragma: no cover
        return CreateConnectionOAuthClientRequestParameters.make_one(
            self.boto3_raw_data["ClientParameters"]
        )

    AuthorizationEndpoint = field("AuthorizationEndpoint")
    HttpMethod = field("HttpMethod")
    OAuthHttpParameters = field("OAuthHttpParameters")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateConnectionOAuthRequestParametersTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateConnectionOAuthRequestParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateConnectionOAuthRequestParameters:
    boto3_raw_data: "type_defs.UpdateConnectionOAuthRequestParametersTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ClientParameters(self):  # pragma: no cover
        return UpdateConnectionOAuthClientRequestParameters.make_one(
            self.boto3_raw_data["ClientParameters"]
        )

    AuthorizationEndpoint = field("AuthorizationEndpoint")
    HttpMethod = field("HttpMethod")
    OAuthHttpParameters = field("OAuthHttpParameters")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateConnectionOAuthRequestParametersTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateConnectionOAuthRequestParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEndpointRequest:
    boto3_raw_data: "type_defs.CreateEndpointRequestTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def RoutingConfig(self):  # pragma: no cover
        return RoutingConfig.make_one(self.boto3_raw_data["RoutingConfig"])

    @cached_property
    def EventBuses(self):  # pragma: no cover
        return EndpointEventBus.make_many(self.boto3_raw_data["EventBuses"])

    Description = field("Description")

    @cached_property
    def ReplicationConfig(self):  # pragma: no cover
        return ReplicationConfig.make_one(self.boto3_raw_data["ReplicationConfig"])

    RoleArn = field("RoleArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateEndpointRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEndpointRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEndpointResponse:
    boto3_raw_data: "type_defs.CreateEndpointResponseTypeDef" = dataclasses.field()

    Name = field("Name")
    Arn = field("Arn")

    @cached_property
    def RoutingConfig(self):  # pragma: no cover
        return RoutingConfig.make_one(self.boto3_raw_data["RoutingConfig"])

    @cached_property
    def ReplicationConfig(self):  # pragma: no cover
        return ReplicationConfig.make_one(self.boto3_raw_data["ReplicationConfig"])

    @cached_property
    def EventBuses(self):  # pragma: no cover
        return EndpointEventBus.make_many(self.boto3_raw_data["EventBuses"])

    RoleArn = field("RoleArn")
    State = field("State")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateEndpointResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEndpointResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEndpointResponse:
    boto3_raw_data: "type_defs.DescribeEndpointResponseTypeDef" = dataclasses.field()

    Name = field("Name")
    Description = field("Description")
    Arn = field("Arn")

    @cached_property
    def RoutingConfig(self):  # pragma: no cover
        return RoutingConfig.make_one(self.boto3_raw_data["RoutingConfig"])

    @cached_property
    def ReplicationConfig(self):  # pragma: no cover
        return ReplicationConfig.make_one(self.boto3_raw_data["ReplicationConfig"])

    @cached_property
    def EventBuses(self):  # pragma: no cover
        return EndpointEventBus.make_many(self.boto3_raw_data["EventBuses"])

    RoleArn = field("RoleArn")
    EndpointId = field("EndpointId")
    EndpointUrl = field("EndpointUrl")
    State = field("State")
    StateReason = field("StateReason")
    CreationTime = field("CreationTime")
    LastModifiedTime = field("LastModifiedTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeEndpointResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEndpointResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Endpoint:
    boto3_raw_data: "type_defs.EndpointTypeDef" = dataclasses.field()

    Name = field("Name")
    Description = field("Description")
    Arn = field("Arn")

    @cached_property
    def RoutingConfig(self):  # pragma: no cover
        return RoutingConfig.make_one(self.boto3_raw_data["RoutingConfig"])

    @cached_property
    def ReplicationConfig(self):  # pragma: no cover
        return ReplicationConfig.make_one(self.boto3_raw_data["ReplicationConfig"])

    @cached_property
    def EventBuses(self):  # pragma: no cover
        return EndpointEventBus.make_many(self.boto3_raw_data["EventBuses"])

    RoleArn = field("RoleArn")
    EndpointId = field("EndpointId")
    EndpointUrl = field("EndpointUrl")
    State = field("State")
    StateReason = field("StateReason")
    CreationTime = field("CreationTime")
    LastModifiedTime = field("LastModifiedTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EndpointTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EndpointTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateEndpointRequest:
    boto3_raw_data: "type_defs.UpdateEndpointRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    Description = field("Description")

    @cached_property
    def RoutingConfig(self):  # pragma: no cover
        return RoutingConfig.make_one(self.boto3_raw_data["RoutingConfig"])

    @cached_property
    def ReplicationConfig(self):  # pragma: no cover
        return ReplicationConfig.make_one(self.boto3_raw_data["ReplicationConfig"])

    @cached_property
    def EventBuses(self):  # pragma: no cover
        return EndpointEventBus.make_many(self.boto3_raw_data["EventBuses"])

    RoleArn = field("RoleArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateEndpointRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateEndpointRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateEndpointResponse:
    boto3_raw_data: "type_defs.UpdateEndpointResponseTypeDef" = dataclasses.field()

    Name = field("Name")
    Arn = field("Arn")

    @cached_property
    def RoutingConfig(self):  # pragma: no cover
        return RoutingConfig.make_one(self.boto3_raw_data["RoutingConfig"])

    @cached_property
    def ReplicationConfig(self):  # pragma: no cover
        return ReplicationConfig.make_one(self.boto3_raw_data["ReplicationConfig"])

    @cached_property
    def EventBuses(self):  # pragma: no cover
        return EndpointEventBus.make_many(self.boto3_raw_data["EventBuses"])

    RoleArn = field("RoleArn")
    EndpointId = field("EndpointId")
    EndpointUrl = field("EndpointUrl")
    State = field("State")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateEndpointResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateEndpointResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTargetsByRuleResponse:
    boto3_raw_data: "type_defs.ListTargetsByRuleResponseTypeDef" = dataclasses.field()

    @cached_property
    def Targets(self):  # pragma: no cover
        return TargetOutput.make_many(self.boto3_raw_data["Targets"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTargetsByRuleResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTargetsByRuleResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EcsParameters:
    boto3_raw_data: "type_defs.EcsParametersTypeDef" = dataclasses.field()

    TaskDefinitionArn = field("TaskDefinitionArn")
    TaskCount = field("TaskCount")
    LaunchType = field("LaunchType")
    NetworkConfiguration = field("NetworkConfiguration")
    PlatformVersion = field("PlatformVersion")
    Group = field("Group")

    @cached_property
    def CapacityProviderStrategy(self):  # pragma: no cover
        return CapacityProviderStrategyItem.make_many(
            self.boto3_raw_data["CapacityProviderStrategy"]
        )

    EnableECSManagedTags = field("EnableECSManagedTags")
    EnableExecuteCommand = field("EnableExecuteCommand")

    @cached_property
    def PlacementConstraints(self):  # pragma: no cover
        return PlacementConstraint.make_many(
            self.boto3_raw_data["PlacementConstraints"]
        )

    @cached_property
    def PlacementStrategy(self):  # pragma: no cover
        return PlacementStrategy.make_many(self.boto3_raw_data["PlacementStrategy"])

    PropagateTags = field("PropagateTags")
    ReferenceId = field("ReferenceId")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EcsParametersTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EcsParametersTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeConnectionResponse:
    boto3_raw_data: "type_defs.DescribeConnectionResponseTypeDef" = dataclasses.field()

    ConnectionArn = field("ConnectionArn")
    Name = field("Name")
    Description = field("Description")

    @cached_property
    def InvocationConnectivityParameters(self):  # pragma: no cover
        return DescribeConnectionConnectivityParameters.make_one(
            self.boto3_raw_data["InvocationConnectivityParameters"]
        )

    ConnectionState = field("ConnectionState")
    StateReason = field("StateReason")
    AuthorizationType = field("AuthorizationType")
    SecretArn = field("SecretArn")
    KmsKeyIdentifier = field("KmsKeyIdentifier")

    @cached_property
    def AuthParameters(self):  # pragma: no cover
        return ConnectionAuthResponseParameters.make_one(
            self.boto3_raw_data["AuthParameters"]
        )

    CreationTime = field("CreationTime")
    LastModifiedTime = field("LastModifiedTime")
    LastAuthorizedTime = field("LastAuthorizedTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeConnectionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeConnectionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateConnectionAuthRequestParameters:
    boto3_raw_data: "type_defs.CreateConnectionAuthRequestParametersTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def BasicAuthParameters(self):  # pragma: no cover
        return CreateConnectionBasicAuthRequestParameters.make_one(
            self.boto3_raw_data["BasicAuthParameters"]
        )

    @cached_property
    def OAuthParameters(self):  # pragma: no cover
        return CreateConnectionOAuthRequestParameters.make_one(
            self.boto3_raw_data["OAuthParameters"]
        )

    @cached_property
    def ApiKeyAuthParameters(self):  # pragma: no cover
        return CreateConnectionApiKeyAuthRequestParameters.make_one(
            self.boto3_raw_data["ApiKeyAuthParameters"]
        )

    InvocationHttpParameters = field("InvocationHttpParameters")

    @cached_property
    def ConnectivityParameters(self):  # pragma: no cover
        return ConnectivityResourceParameters.make_one(
            self.boto3_raw_data["ConnectivityParameters"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateConnectionAuthRequestParametersTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateConnectionAuthRequestParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateConnectionAuthRequestParameters:
    boto3_raw_data: "type_defs.UpdateConnectionAuthRequestParametersTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def BasicAuthParameters(self):  # pragma: no cover
        return UpdateConnectionBasicAuthRequestParameters.make_one(
            self.boto3_raw_data["BasicAuthParameters"]
        )

    @cached_property
    def OAuthParameters(self):  # pragma: no cover
        return UpdateConnectionOAuthRequestParameters.make_one(
            self.boto3_raw_data["OAuthParameters"]
        )

    @cached_property
    def ApiKeyAuthParameters(self):  # pragma: no cover
        return UpdateConnectionApiKeyAuthRequestParameters.make_one(
            self.boto3_raw_data["ApiKeyAuthParameters"]
        )

    InvocationHttpParameters = field("InvocationHttpParameters")

    @cached_property
    def ConnectivityParameters(self):  # pragma: no cover
        return ConnectivityResourceParameters.make_one(
            self.boto3_raw_data["ConnectivityParameters"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateConnectionAuthRequestParametersTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateConnectionAuthRequestParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEndpointsResponse:
    boto3_raw_data: "type_defs.ListEndpointsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Endpoints(self):  # pragma: no cover
        return Endpoint.make_many(self.boto3_raw_data["Endpoints"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEndpointsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEndpointsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateConnectionRequest:
    boto3_raw_data: "type_defs.CreateConnectionRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    AuthorizationType = field("AuthorizationType")

    @cached_property
    def AuthParameters(self):  # pragma: no cover
        return CreateConnectionAuthRequestParameters.make_one(
            self.boto3_raw_data["AuthParameters"]
        )

    Description = field("Description")

    @cached_property
    def InvocationConnectivityParameters(self):  # pragma: no cover
        return ConnectivityResourceParameters.make_one(
            self.boto3_raw_data["InvocationConnectivityParameters"]
        )

    KmsKeyIdentifier = field("KmsKeyIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateConnectionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateConnectionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateConnectionRequest:
    boto3_raw_data: "type_defs.UpdateConnectionRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    Description = field("Description")
    AuthorizationType = field("AuthorizationType")

    @cached_property
    def AuthParameters(self):  # pragma: no cover
        return UpdateConnectionAuthRequestParameters.make_one(
            self.boto3_raw_data["AuthParameters"]
        )

    @cached_property
    def InvocationConnectivityParameters(self):  # pragma: no cover
        return ConnectivityResourceParameters.make_one(
            self.boto3_raw_data["InvocationConnectivityParameters"]
        )

    KmsKeyIdentifier = field("KmsKeyIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateConnectionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateConnectionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Target:
    boto3_raw_data: "type_defs.TargetTypeDef" = dataclasses.field()

    Id = field("Id")
    Arn = field("Arn")
    RoleArn = field("RoleArn")
    Input = field("Input")
    InputPath = field("InputPath")
    InputTransformer = field("InputTransformer")

    @cached_property
    def KinesisParameters(self):  # pragma: no cover
        return KinesisParameters.make_one(self.boto3_raw_data["KinesisParameters"])

    RunCommandParameters = field("RunCommandParameters")
    EcsParameters = field("EcsParameters")

    @cached_property
    def BatchParameters(self):  # pragma: no cover
        return BatchParameters.make_one(self.boto3_raw_data["BatchParameters"])

    @cached_property
    def SqsParameters(self):  # pragma: no cover
        return SqsParameters.make_one(self.boto3_raw_data["SqsParameters"])

    HttpParameters = field("HttpParameters")
    RedshiftDataParameters = field("RedshiftDataParameters")
    SageMakerPipelineParameters = field("SageMakerPipelineParameters")

    @cached_property
    def DeadLetterConfig(self):  # pragma: no cover
        return DeadLetterConfig.make_one(self.boto3_raw_data["DeadLetterConfig"])

    @cached_property
    def RetryPolicy(self):  # pragma: no cover
        return RetryPolicy.make_one(self.boto3_raw_data["RetryPolicy"])

    @cached_property
    def AppSyncParameters(self):  # pragma: no cover
        return AppSyncParameters.make_one(self.boto3_raw_data["AppSyncParameters"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TargetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TargetTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutTargetsRequest:
    boto3_raw_data: "type_defs.PutTargetsRequestTypeDef" = dataclasses.field()

    Rule = field("Rule")
    Targets = field("Targets")
    EventBusName = field("EventBusName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PutTargetsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutTargetsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
