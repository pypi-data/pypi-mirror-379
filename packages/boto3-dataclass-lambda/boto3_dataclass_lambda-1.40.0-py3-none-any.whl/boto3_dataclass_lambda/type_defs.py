# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_lambda import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AccountLimit:
    boto3_raw_data: "type_defs.AccountLimitTypeDef" = dataclasses.field()

    TotalCodeSize = field("TotalCodeSize")
    CodeSizeUnzipped = field("CodeSizeUnzipped")
    CodeSizeZipped = field("CodeSizeZipped")
    ConcurrentExecutions = field("ConcurrentExecutions")
    UnreservedConcurrentExecutions = field("UnreservedConcurrentExecutions")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AccountLimitTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AccountLimitTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccountUsage:
    boto3_raw_data: "type_defs.AccountUsageTypeDef" = dataclasses.field()

    TotalCodeSize = field("TotalCodeSize")
    FunctionCount = field("FunctionCount")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AccountUsageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AccountUsageTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddLayerVersionPermissionRequest:
    boto3_raw_data: "type_defs.AddLayerVersionPermissionRequestTypeDef" = (
        dataclasses.field()
    )

    LayerName = field("LayerName")
    VersionNumber = field("VersionNumber")
    StatementId = field("StatementId")
    Action = field("Action")
    Principal = field("Principal")
    OrganizationId = field("OrganizationId")
    RevisionId = field("RevisionId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AddLayerVersionPermissionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddLayerVersionPermissionRequestTypeDef"]
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
class AddPermissionRequest:
    boto3_raw_data: "type_defs.AddPermissionRequestTypeDef" = dataclasses.field()

    FunctionName = field("FunctionName")
    StatementId = field("StatementId")
    Action = field("Action")
    Principal = field("Principal")
    SourceArn = field("SourceArn")
    SourceAccount = field("SourceAccount")
    EventSourceToken = field("EventSourceToken")
    Qualifier = field("Qualifier")
    RevisionId = field("RevisionId")
    PrincipalOrgID = field("PrincipalOrgID")
    FunctionUrlAuthType = field("FunctionUrlAuthType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddPermissionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddPermissionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AliasRoutingConfigurationOutput:
    boto3_raw_data: "type_defs.AliasRoutingConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    AdditionalVersionWeights = field("AdditionalVersionWeights")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AliasRoutingConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AliasRoutingConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AliasRoutingConfiguration:
    boto3_raw_data: "type_defs.AliasRoutingConfigurationTypeDef" = dataclasses.field()

    AdditionalVersionWeights = field("AdditionalVersionWeights")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AliasRoutingConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AliasRoutingConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AllowedPublishersOutput:
    boto3_raw_data: "type_defs.AllowedPublishersOutputTypeDef" = dataclasses.field()

    SigningProfileVersionArns = field("SigningProfileVersionArns")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AllowedPublishersOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AllowedPublishersOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AllowedPublishers:
    boto3_raw_data: "type_defs.AllowedPublishersTypeDef" = dataclasses.field()

    SigningProfileVersionArns = field("SigningProfileVersionArns")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AllowedPublishersTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AllowedPublishersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CodeSigningPolicies:
    boto3_raw_data: "type_defs.CodeSigningPoliciesTypeDef" = dataclasses.field()

    UntrustedArtifactOnDeployment = field("UntrustedArtifactOnDeployment")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CodeSigningPoliciesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CodeSigningPoliciesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Concurrency:
    boto3_raw_data: "type_defs.ConcurrencyTypeDef" = dataclasses.field()

    ReservedConcurrentExecutions = field("ReservedConcurrentExecutions")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConcurrencyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ConcurrencyTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CorsOutput:
    boto3_raw_data: "type_defs.CorsOutputTypeDef" = dataclasses.field()

    AllowCredentials = field("AllowCredentials")
    AllowHeaders = field("AllowHeaders")
    AllowMethods = field("AllowMethods")
    AllowOrigins = field("AllowOrigins")
    ExposeHeaders = field("ExposeHeaders")
    MaxAge = field("MaxAge")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CorsOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CorsOutputTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Cors:
    boto3_raw_data: "type_defs.CorsTypeDef" = dataclasses.field()

    AllowCredentials = field("AllowCredentials")
    AllowHeaders = field("AllowHeaders")
    AllowMethods = field("AllowMethods")
    AllowOrigins = field("AllowOrigins")
    ExposeHeaders = field("ExposeHeaders")
    MaxAge = field("MaxAge")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CorsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CorsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentDBEventSourceConfig:
    boto3_raw_data: "type_defs.DocumentDBEventSourceConfigTypeDef" = dataclasses.field()

    DatabaseName = field("DatabaseName")
    CollectionName = field("CollectionName")
    FullDocument = field("FullDocument")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DocumentDBEventSourceConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentDBEventSourceConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProvisionedPollerConfig:
    boto3_raw_data: "type_defs.ProvisionedPollerConfigTypeDef" = dataclasses.field()

    MinimumPollers = field("MinimumPollers")
    MaximumPollers = field("MaximumPollers")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProvisionedPollerConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProvisionedPollerConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScalingConfig:
    boto3_raw_data: "type_defs.ScalingConfigTypeDef" = dataclasses.field()

    MaximumConcurrency = field("MaximumConcurrency")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ScalingConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ScalingConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SourceAccessConfiguration:
    boto3_raw_data: "type_defs.SourceAccessConfigurationTypeDef" = dataclasses.field()

    Type = field("Type")
    URI = field("URI")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SourceAccessConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SourceAccessConfigurationTypeDef"]
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

    TargetArn = field("TargetArn")

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
class Environment:
    boto3_raw_data: "type_defs.EnvironmentTypeDef" = dataclasses.field()

    Variables = field("Variables")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EnvironmentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EnvironmentTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EphemeralStorage:
    boto3_raw_data: "type_defs.EphemeralStorageTypeDef" = dataclasses.field()

    Size = field("Size")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EphemeralStorageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EphemeralStorageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FileSystemConfig:
    boto3_raw_data: "type_defs.FileSystemConfigTypeDef" = dataclasses.field()

    Arn = field("Arn")
    LocalMountPath = field("LocalMountPath")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FileSystemConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FileSystemConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoggingConfig:
    boto3_raw_data: "type_defs.LoggingConfigTypeDef" = dataclasses.field()

    LogFormat = field("LogFormat")
    ApplicationLogLevel = field("ApplicationLogLevel")
    SystemLogLevel = field("SystemLogLevel")
    LogGroup = field("LogGroup")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LoggingConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LoggingConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SnapStart:
    boto3_raw_data: "type_defs.SnapStartTypeDef" = dataclasses.field()

    ApplyOn = field("ApplyOn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SnapStartTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SnapStartTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TracingConfig:
    boto3_raw_data: "type_defs.TracingConfigTypeDef" = dataclasses.field()

    Mode = field("Mode")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TracingConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TracingConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VpcConfig:
    boto3_raw_data: "type_defs.VpcConfigTypeDef" = dataclasses.field()

    SubnetIds = field("SubnetIds")
    SecurityGroupIds = field("SecurityGroupIds")
    Ipv6AllowedForDualStack = field("Ipv6AllowedForDualStack")

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
class DeleteAliasRequest:
    boto3_raw_data: "type_defs.DeleteAliasRequestTypeDef" = dataclasses.field()

    FunctionName = field("FunctionName")
    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAliasRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAliasRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCodeSigningConfigRequest:
    boto3_raw_data: "type_defs.DeleteCodeSigningConfigRequestTypeDef" = (
        dataclasses.field()
    )

    CodeSigningConfigArn = field("CodeSigningConfigArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteCodeSigningConfigRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCodeSigningConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteEventSourceMappingRequest:
    boto3_raw_data: "type_defs.DeleteEventSourceMappingRequestTypeDef" = (
        dataclasses.field()
    )

    UUID = field("UUID")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteEventSourceMappingRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteEventSourceMappingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteFunctionCodeSigningConfigRequest:
    boto3_raw_data: "type_defs.DeleteFunctionCodeSigningConfigRequestTypeDef" = (
        dataclasses.field()
    )

    FunctionName = field("FunctionName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteFunctionCodeSigningConfigRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteFunctionCodeSigningConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteFunctionConcurrencyRequest:
    boto3_raw_data: "type_defs.DeleteFunctionConcurrencyRequestTypeDef" = (
        dataclasses.field()
    )

    FunctionName = field("FunctionName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteFunctionConcurrencyRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteFunctionConcurrencyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteFunctionEventInvokeConfigRequest:
    boto3_raw_data: "type_defs.DeleteFunctionEventInvokeConfigRequestTypeDef" = (
        dataclasses.field()
    )

    FunctionName = field("FunctionName")
    Qualifier = field("Qualifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteFunctionEventInvokeConfigRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteFunctionEventInvokeConfigRequestTypeDef"]
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

    FunctionName = field("FunctionName")
    Qualifier = field("Qualifier")

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
class DeleteFunctionUrlConfigRequest:
    boto3_raw_data: "type_defs.DeleteFunctionUrlConfigRequestTypeDef" = (
        dataclasses.field()
    )

    FunctionName = field("FunctionName")
    Qualifier = field("Qualifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteFunctionUrlConfigRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteFunctionUrlConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteLayerVersionRequest:
    boto3_raw_data: "type_defs.DeleteLayerVersionRequestTypeDef" = dataclasses.field()

    LayerName = field("LayerName")
    VersionNumber = field("VersionNumber")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteLayerVersionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteLayerVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteProvisionedConcurrencyConfigRequest:
    boto3_raw_data: "type_defs.DeleteProvisionedConcurrencyConfigRequestTypeDef" = (
        dataclasses.field()
    )

    FunctionName = field("FunctionName")
    Qualifier = field("Qualifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteProvisionedConcurrencyConfigRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteProvisionedConcurrencyConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OnFailure:
    boto3_raw_data: "type_defs.OnFailureTypeDef" = dataclasses.field()

    Destination = field("Destination")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OnFailureTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OnFailureTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OnSuccess:
    boto3_raw_data: "type_defs.OnSuccessTypeDef" = dataclasses.field()

    Destination = field("Destination")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OnSuccessTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OnSuccessTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnvironmentError:
    boto3_raw_data: "type_defs.EnvironmentErrorTypeDef" = dataclasses.field()

    ErrorCode = field("ErrorCode")
    Message = field("Message")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EnvironmentErrorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnvironmentErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventSourceMappingMetricsConfigOutput:
    boto3_raw_data: "type_defs.EventSourceMappingMetricsConfigOutputTypeDef" = (
        dataclasses.field()
    )

    Metrics = field("Metrics")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.EventSourceMappingMetricsConfigOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EventSourceMappingMetricsConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FilterCriteriaError:
    boto3_raw_data: "type_defs.FilterCriteriaErrorTypeDef" = dataclasses.field()

    ErrorCode = field("ErrorCode")
    Message = field("Message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FilterCriteriaErrorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FilterCriteriaErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SelfManagedEventSourceOutput:
    boto3_raw_data: "type_defs.SelfManagedEventSourceOutputTypeDef" = (
        dataclasses.field()
    )

    Endpoints = field("Endpoints")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SelfManagedEventSourceOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SelfManagedEventSourceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventSourceMappingMetricsConfig:
    boto3_raw_data: "type_defs.EventSourceMappingMetricsConfigTypeDef" = (
        dataclasses.field()
    )

    Metrics = field("Metrics")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.EventSourceMappingMetricsConfigTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EventSourceMappingMetricsConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Filter:
    boto3_raw_data: "type_defs.FilterTypeDef" = dataclasses.field()

    Pattern = field("Pattern")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FilterTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FunctionCodeLocation:
    boto3_raw_data: "type_defs.FunctionCodeLocationTypeDef" = dataclasses.field()

    RepositoryType = field("RepositoryType")
    Location = field("Location")
    ImageUri = field("ImageUri")
    ResolvedImageUri = field("ResolvedImageUri")
    SourceKMSKeyArn = field("SourceKMSKeyArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FunctionCodeLocationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FunctionCodeLocationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Layer:
    boto3_raw_data: "type_defs.LayerTypeDef" = dataclasses.field()

    Arn = field("Arn")
    CodeSize = field("CodeSize")
    SigningProfileVersionArn = field("SigningProfileVersionArn")
    SigningJobArn = field("SigningJobArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LayerTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LayerTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SnapStartResponse:
    boto3_raw_data: "type_defs.SnapStartResponseTypeDef" = dataclasses.field()

    ApplyOn = field("ApplyOn")
    OptimizationStatus = field("OptimizationStatus")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SnapStartResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SnapStartResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TracingConfigResponse:
    boto3_raw_data: "type_defs.TracingConfigResponseTypeDef" = dataclasses.field()

    Mode = field("Mode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TracingConfigResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TracingConfigResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VpcConfigResponse:
    boto3_raw_data: "type_defs.VpcConfigResponseTypeDef" = dataclasses.field()

    SubnetIds = field("SubnetIds")
    SecurityGroupIds = field("SecurityGroupIds")
    VpcId = field("VpcId")
    Ipv6AllowedForDualStack = field("Ipv6AllowedForDualStack")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VpcConfigResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VpcConfigResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAliasRequest:
    boto3_raw_data: "type_defs.GetAliasRequestTypeDef" = dataclasses.field()

    FunctionName = field("FunctionName")
    Name = field("Name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetAliasRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetAliasRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCodeSigningConfigRequest:
    boto3_raw_data: "type_defs.GetCodeSigningConfigRequestTypeDef" = dataclasses.field()

    CodeSigningConfigArn = field("CodeSigningConfigArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCodeSigningConfigRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCodeSigningConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEventSourceMappingRequest:
    boto3_raw_data: "type_defs.GetEventSourceMappingRequestTypeDef" = (
        dataclasses.field()
    )

    UUID = field("UUID")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetEventSourceMappingRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEventSourceMappingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFunctionCodeSigningConfigRequest:
    boto3_raw_data: "type_defs.GetFunctionCodeSigningConfigRequestTypeDef" = (
        dataclasses.field()
    )

    FunctionName = field("FunctionName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetFunctionCodeSigningConfigRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFunctionCodeSigningConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFunctionConcurrencyRequest:
    boto3_raw_data: "type_defs.GetFunctionConcurrencyRequestTypeDef" = (
        dataclasses.field()
    )

    FunctionName = field("FunctionName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetFunctionConcurrencyRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFunctionConcurrencyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFunctionConfigurationRequest:
    boto3_raw_data: "type_defs.GetFunctionConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    FunctionName = field("FunctionName")
    Qualifier = field("Qualifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetFunctionConfigurationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFunctionConfigurationRequestTypeDef"]
        ],
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
class GetFunctionEventInvokeConfigRequest:
    boto3_raw_data: "type_defs.GetFunctionEventInvokeConfigRequestTypeDef" = (
        dataclasses.field()
    )

    FunctionName = field("FunctionName")
    Qualifier = field("Qualifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetFunctionEventInvokeConfigRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFunctionEventInvokeConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFunctionRecursionConfigRequest:
    boto3_raw_data: "type_defs.GetFunctionRecursionConfigRequestTypeDef" = (
        dataclasses.field()
    )

    FunctionName = field("FunctionName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetFunctionRecursionConfigRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFunctionRecursionConfigRequestTypeDef"]
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

    FunctionName = field("FunctionName")
    Qualifier = field("Qualifier")

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
class TagsError:
    boto3_raw_data: "type_defs.TagsErrorTypeDef" = dataclasses.field()

    ErrorCode = field("ErrorCode")
    Message = field("Message")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TagsErrorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TagsErrorTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFunctionUrlConfigRequest:
    boto3_raw_data: "type_defs.GetFunctionUrlConfigRequestTypeDef" = dataclasses.field()

    FunctionName = field("FunctionName")
    Qualifier = field("Qualifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetFunctionUrlConfigRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFunctionUrlConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLayerVersionByArnRequest:
    boto3_raw_data: "type_defs.GetLayerVersionByArnRequestTypeDef" = dataclasses.field()

    Arn = field("Arn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetLayerVersionByArnRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLayerVersionByArnRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLayerVersionPolicyRequest:
    boto3_raw_data: "type_defs.GetLayerVersionPolicyRequestTypeDef" = (
        dataclasses.field()
    )

    LayerName = field("LayerName")
    VersionNumber = field("VersionNumber")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetLayerVersionPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLayerVersionPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLayerVersionRequest:
    boto3_raw_data: "type_defs.GetLayerVersionRequestTypeDef" = dataclasses.field()

    LayerName = field("LayerName")
    VersionNumber = field("VersionNumber")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetLayerVersionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLayerVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LayerVersionContentOutput:
    boto3_raw_data: "type_defs.LayerVersionContentOutputTypeDef" = dataclasses.field()

    Location = field("Location")
    CodeSha256 = field("CodeSha256")
    CodeSize = field("CodeSize")
    SigningProfileVersionArn = field("SigningProfileVersionArn")
    SigningJobArn = field("SigningJobArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LayerVersionContentOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LayerVersionContentOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPolicyRequest:
    boto3_raw_data: "type_defs.GetPolicyRequestTypeDef" = dataclasses.field()

    FunctionName = field("FunctionName")
    Qualifier = field("Qualifier")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetPolicyRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetProvisionedConcurrencyConfigRequest:
    boto3_raw_data: "type_defs.GetProvisionedConcurrencyConfigRequestTypeDef" = (
        dataclasses.field()
    )

    FunctionName = field("FunctionName")
    Qualifier = field("Qualifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetProvisionedConcurrencyConfigRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetProvisionedConcurrencyConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRuntimeManagementConfigRequest:
    boto3_raw_data: "type_defs.GetRuntimeManagementConfigRequestTypeDef" = (
        dataclasses.field()
    )

    FunctionName = field("FunctionName")
    Qualifier = field("Qualifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetRuntimeManagementConfigRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRuntimeManagementConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImageConfigError:
    boto3_raw_data: "type_defs.ImageConfigErrorTypeDef" = dataclasses.field()

    ErrorCode = field("ErrorCode")
    Message = field("Message")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImageConfigErrorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImageConfigErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImageConfigOutput:
    boto3_raw_data: "type_defs.ImageConfigOutputTypeDef" = dataclasses.field()

    EntryPoint = field("EntryPoint")
    Command = field("Command")
    WorkingDirectory = field("WorkingDirectory")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImageConfigOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImageConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImageConfig:
    boto3_raw_data: "type_defs.ImageConfigTypeDef" = dataclasses.field()

    EntryPoint = field("EntryPoint")
    Command = field("Command")
    WorkingDirectory = field("WorkingDirectory")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImageConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ImageConfigTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InvokeResponseStreamUpdate:
    boto3_raw_data: "type_defs.InvokeResponseStreamUpdateTypeDef" = dataclasses.field()

    Payload = field("Payload")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InvokeResponseStreamUpdateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InvokeResponseStreamUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InvokeWithResponseStreamCompleteEvent:
    boto3_raw_data: "type_defs.InvokeWithResponseStreamCompleteEventTypeDef" = (
        dataclasses.field()
    )

    ErrorCode = field("ErrorCode")
    ErrorDetails = field("ErrorDetails")
    LogResult = field("LogResult")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.InvokeWithResponseStreamCompleteEventTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InvokeWithResponseStreamCompleteEventTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KafkaSchemaRegistryAccessConfig:
    boto3_raw_data: "type_defs.KafkaSchemaRegistryAccessConfigTypeDef" = (
        dataclasses.field()
    )

    Type = field("Type")
    URI = field("URI")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.KafkaSchemaRegistryAccessConfigTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KafkaSchemaRegistryAccessConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KafkaSchemaValidationConfig:
    boto3_raw_data: "type_defs.KafkaSchemaValidationConfigTypeDef" = dataclasses.field()

    Attribute = field("Attribute")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KafkaSchemaValidationConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KafkaSchemaValidationConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LayerVersionsListItem:
    boto3_raw_data: "type_defs.LayerVersionsListItemTypeDef" = dataclasses.field()

    LayerVersionArn = field("LayerVersionArn")
    Version = field("Version")
    Description = field("Description")
    CreatedDate = field("CreatedDate")
    CompatibleRuntimes = field("CompatibleRuntimes")
    LicenseInfo = field("LicenseInfo")
    CompatibleArchitectures = field("CompatibleArchitectures")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LayerVersionsListItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LayerVersionsListItemTypeDef"]
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
class ListAliasesRequest:
    boto3_raw_data: "type_defs.ListAliasesRequestTypeDef" = dataclasses.field()

    FunctionName = field("FunctionName")
    FunctionVersion = field("FunctionVersion")
    Marker = field("Marker")
    MaxItems = field("MaxItems")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAliasesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAliasesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCodeSigningConfigsRequest:
    boto3_raw_data: "type_defs.ListCodeSigningConfigsRequestTypeDef" = (
        dataclasses.field()
    )

    Marker = field("Marker")
    MaxItems = field("MaxItems")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListCodeSigningConfigsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCodeSigningConfigsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEventSourceMappingsRequest:
    boto3_raw_data: "type_defs.ListEventSourceMappingsRequestTypeDef" = (
        dataclasses.field()
    )

    EventSourceArn = field("EventSourceArn")
    FunctionName = field("FunctionName")
    Marker = field("Marker")
    MaxItems = field("MaxItems")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListEventSourceMappingsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEventSourceMappingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFunctionEventInvokeConfigsRequest:
    boto3_raw_data: "type_defs.ListFunctionEventInvokeConfigsRequestTypeDef" = (
        dataclasses.field()
    )

    FunctionName = field("FunctionName")
    Marker = field("Marker")
    MaxItems = field("MaxItems")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListFunctionEventInvokeConfigsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFunctionEventInvokeConfigsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFunctionUrlConfigsRequest:
    boto3_raw_data: "type_defs.ListFunctionUrlConfigsRequestTypeDef" = (
        dataclasses.field()
    )

    FunctionName = field("FunctionName")
    Marker = field("Marker")
    MaxItems = field("MaxItems")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListFunctionUrlConfigsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFunctionUrlConfigsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFunctionsByCodeSigningConfigRequest:
    boto3_raw_data: "type_defs.ListFunctionsByCodeSigningConfigRequestTypeDef" = (
        dataclasses.field()
    )

    CodeSigningConfigArn = field("CodeSigningConfigArn")
    Marker = field("Marker")
    MaxItems = field("MaxItems")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListFunctionsByCodeSigningConfigRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFunctionsByCodeSigningConfigRequestTypeDef"]
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

    MasterRegion = field("MasterRegion")
    FunctionVersion = field("FunctionVersion")
    Marker = field("Marker")
    MaxItems = field("MaxItems")

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
class ListLayerVersionsRequest:
    boto3_raw_data: "type_defs.ListLayerVersionsRequestTypeDef" = dataclasses.field()

    LayerName = field("LayerName")
    CompatibleRuntime = field("CompatibleRuntime")
    Marker = field("Marker")
    MaxItems = field("MaxItems")
    CompatibleArchitecture = field("CompatibleArchitecture")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListLayerVersionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLayerVersionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLayersRequest:
    boto3_raw_data: "type_defs.ListLayersRequestTypeDef" = dataclasses.field()

    CompatibleRuntime = field("CompatibleRuntime")
    Marker = field("Marker")
    MaxItems = field("MaxItems")
    CompatibleArchitecture = field("CompatibleArchitecture")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListLayersRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLayersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProvisionedConcurrencyConfigsRequest:
    boto3_raw_data: "type_defs.ListProvisionedConcurrencyConfigsRequestTypeDef" = (
        dataclasses.field()
    )

    FunctionName = field("FunctionName")
    Marker = field("Marker")
    MaxItems = field("MaxItems")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListProvisionedConcurrencyConfigsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProvisionedConcurrencyConfigsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProvisionedConcurrencyConfigListItem:
    boto3_raw_data: "type_defs.ProvisionedConcurrencyConfigListItemTypeDef" = (
        dataclasses.field()
    )

    FunctionArn = field("FunctionArn")
    RequestedProvisionedConcurrentExecutions = field(
        "RequestedProvisionedConcurrentExecutions"
    )
    AvailableProvisionedConcurrentExecutions = field(
        "AvailableProvisionedConcurrentExecutions"
    )
    AllocatedProvisionedConcurrentExecutions = field(
        "AllocatedProvisionedConcurrentExecutions"
    )
    Status = field("Status")
    StatusReason = field("StatusReason")
    LastModified = field("LastModified")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ProvisionedConcurrencyConfigListItemTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProvisionedConcurrencyConfigListItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsRequest:
    boto3_raw_data: "type_defs.ListTagsRequestTypeDef" = dataclasses.field()

    Resource = field("Resource")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListTagsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListTagsRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVersionsByFunctionRequest:
    boto3_raw_data: "type_defs.ListVersionsByFunctionRequestTypeDef" = (
        dataclasses.field()
    )

    FunctionName = field("FunctionName")
    Marker = field("Marker")
    MaxItems = field("MaxItems")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListVersionsByFunctionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVersionsByFunctionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PublishVersionRequest:
    boto3_raw_data: "type_defs.PublishVersionRequestTypeDef" = dataclasses.field()

    FunctionName = field("FunctionName")
    CodeSha256 = field("CodeSha256")
    Description = field("Description")
    RevisionId = field("RevisionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PublishVersionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PublishVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutFunctionCodeSigningConfigRequest:
    boto3_raw_data: "type_defs.PutFunctionCodeSigningConfigRequestTypeDef" = (
        dataclasses.field()
    )

    CodeSigningConfigArn = field("CodeSigningConfigArn")
    FunctionName = field("FunctionName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutFunctionCodeSigningConfigRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutFunctionCodeSigningConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutFunctionConcurrencyRequest:
    boto3_raw_data: "type_defs.PutFunctionConcurrencyRequestTypeDef" = (
        dataclasses.field()
    )

    FunctionName = field("FunctionName")
    ReservedConcurrentExecutions = field("ReservedConcurrentExecutions")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PutFunctionConcurrencyRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutFunctionConcurrencyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutFunctionRecursionConfigRequest:
    boto3_raw_data: "type_defs.PutFunctionRecursionConfigRequestTypeDef" = (
        dataclasses.field()
    )

    FunctionName = field("FunctionName")
    RecursiveLoop = field("RecursiveLoop")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutFunctionRecursionConfigRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutFunctionRecursionConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutProvisionedConcurrencyConfigRequest:
    boto3_raw_data: "type_defs.PutProvisionedConcurrencyConfigRequestTypeDef" = (
        dataclasses.field()
    )

    FunctionName = field("FunctionName")
    Qualifier = field("Qualifier")
    ProvisionedConcurrentExecutions = field("ProvisionedConcurrentExecutions")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutProvisionedConcurrencyConfigRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutProvisionedConcurrencyConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutRuntimeManagementConfigRequest:
    boto3_raw_data: "type_defs.PutRuntimeManagementConfigRequestTypeDef" = (
        dataclasses.field()
    )

    FunctionName = field("FunctionName")
    UpdateRuntimeOn = field("UpdateRuntimeOn")
    Qualifier = field("Qualifier")
    RuntimeVersionArn = field("RuntimeVersionArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutRuntimeManagementConfigRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutRuntimeManagementConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveLayerVersionPermissionRequest:
    boto3_raw_data: "type_defs.RemoveLayerVersionPermissionRequestTypeDef" = (
        dataclasses.field()
    )

    LayerName = field("LayerName")
    VersionNumber = field("VersionNumber")
    StatementId = field("StatementId")
    RevisionId = field("RevisionId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RemoveLayerVersionPermissionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveLayerVersionPermissionRequestTypeDef"]
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

    FunctionName = field("FunctionName")
    StatementId = field("StatementId")
    Qualifier = field("Qualifier")
    RevisionId = field("RevisionId")

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
class RuntimeVersionError:
    boto3_raw_data: "type_defs.RuntimeVersionErrorTypeDef" = dataclasses.field()

    ErrorCode = field("ErrorCode")
    Message = field("Message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RuntimeVersionErrorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RuntimeVersionErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SelfManagedEventSource:
    boto3_raw_data: "type_defs.SelfManagedEventSourceTypeDef" = dataclasses.field()

    Endpoints = field("Endpoints")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SelfManagedEventSourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SelfManagedEventSourceTypeDef"]
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

    Resource = field("Resource")
    Tags = field("Tags")

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

    Resource = field("Resource")
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
class AddLayerVersionPermissionResponse:
    boto3_raw_data: "type_defs.AddLayerVersionPermissionResponseTypeDef" = (
        dataclasses.field()
    )

    Statement = field("Statement")
    RevisionId = field("RevisionId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AddLayerVersionPermissionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddLayerVersionPermissionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddPermissionResponse:
    boto3_raw_data: "type_defs.AddPermissionResponseTypeDef" = dataclasses.field()

    Statement = field("Statement")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddPermissionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddPermissionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConcurrencyResponse:
    boto3_raw_data: "type_defs.ConcurrencyResponseTypeDef" = dataclasses.field()

    ReservedConcurrentExecutions = field("ReservedConcurrentExecutions")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConcurrencyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConcurrencyResponseTypeDef"]
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
class GetAccountSettingsResponse:
    boto3_raw_data: "type_defs.GetAccountSettingsResponseTypeDef" = dataclasses.field()

    @cached_property
    def AccountLimit(self):  # pragma: no cover
        return AccountLimit.make_one(self.boto3_raw_data["AccountLimit"])

    @cached_property
    def AccountUsage(self):  # pragma: no cover
        return AccountUsage.make_one(self.boto3_raw_data["AccountUsage"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAccountSettingsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAccountSettingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFunctionCodeSigningConfigResponse:
    boto3_raw_data: "type_defs.GetFunctionCodeSigningConfigResponseTypeDef" = (
        dataclasses.field()
    )

    CodeSigningConfigArn = field("CodeSigningConfigArn")
    FunctionName = field("FunctionName")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetFunctionCodeSigningConfigResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFunctionCodeSigningConfigResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFunctionConcurrencyResponse:
    boto3_raw_data: "type_defs.GetFunctionConcurrencyResponseTypeDef" = (
        dataclasses.field()
    )

    ReservedConcurrentExecutions = field("ReservedConcurrentExecutions")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetFunctionConcurrencyResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFunctionConcurrencyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFunctionRecursionConfigResponse:
    boto3_raw_data: "type_defs.GetFunctionRecursionConfigResponseTypeDef" = (
        dataclasses.field()
    )

    RecursiveLoop = field("RecursiveLoop")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetFunctionRecursionConfigResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFunctionRecursionConfigResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLayerVersionPolicyResponse:
    boto3_raw_data: "type_defs.GetLayerVersionPolicyResponseTypeDef" = (
        dataclasses.field()
    )

    Policy = field("Policy")
    RevisionId = field("RevisionId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetLayerVersionPolicyResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLayerVersionPolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPolicyResponse:
    boto3_raw_data: "type_defs.GetPolicyResponseTypeDef" = dataclasses.field()

    Policy = field("Policy")
    RevisionId = field("RevisionId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetPolicyResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetProvisionedConcurrencyConfigResponse:
    boto3_raw_data: "type_defs.GetProvisionedConcurrencyConfigResponseTypeDef" = (
        dataclasses.field()
    )

    RequestedProvisionedConcurrentExecutions = field(
        "RequestedProvisionedConcurrentExecutions"
    )
    AvailableProvisionedConcurrentExecutions = field(
        "AvailableProvisionedConcurrentExecutions"
    )
    AllocatedProvisionedConcurrentExecutions = field(
        "AllocatedProvisionedConcurrentExecutions"
    )
    Status = field("Status")
    StatusReason = field("StatusReason")
    LastModified = field("LastModified")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetProvisionedConcurrencyConfigResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetProvisionedConcurrencyConfigResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRuntimeManagementConfigResponse:
    boto3_raw_data: "type_defs.GetRuntimeManagementConfigResponseTypeDef" = (
        dataclasses.field()
    )

    UpdateRuntimeOn = field("UpdateRuntimeOn")
    RuntimeVersionArn = field("RuntimeVersionArn")
    FunctionArn = field("FunctionArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetRuntimeManagementConfigResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRuntimeManagementConfigResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InvocationResponse:
    boto3_raw_data: "type_defs.InvocationResponseTypeDef" = dataclasses.field()

    StatusCode = field("StatusCode")
    FunctionError = field("FunctionError")
    LogResult = field("LogResult")
    Payload = field("Payload")
    ExecutedVersion = field("ExecutedVersion")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InvocationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InvocationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InvokeAsyncResponse:
    boto3_raw_data: "type_defs.InvokeAsyncResponseTypeDef" = dataclasses.field()

    Status = field("Status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InvokeAsyncResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InvokeAsyncResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFunctionsByCodeSigningConfigResponse:
    boto3_raw_data: "type_defs.ListFunctionsByCodeSigningConfigResponseTypeDef" = (
        dataclasses.field()
    )

    NextMarker = field("NextMarker")
    FunctionArns = field("FunctionArns")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListFunctionsByCodeSigningConfigResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFunctionsByCodeSigningConfigResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsResponse:
    boto3_raw_data: "type_defs.ListTagsResponseTypeDef" = dataclasses.field()

    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListTagsResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutFunctionCodeSigningConfigResponse:
    boto3_raw_data: "type_defs.PutFunctionCodeSigningConfigResponseTypeDef" = (
        dataclasses.field()
    )

    CodeSigningConfigArn = field("CodeSigningConfigArn")
    FunctionName = field("FunctionName")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutFunctionCodeSigningConfigResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutFunctionCodeSigningConfigResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutFunctionRecursionConfigResponse:
    boto3_raw_data: "type_defs.PutFunctionRecursionConfigResponseTypeDef" = (
        dataclasses.field()
    )

    RecursiveLoop = field("RecursiveLoop")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutFunctionRecursionConfigResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutFunctionRecursionConfigResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutProvisionedConcurrencyConfigResponse:
    boto3_raw_data: "type_defs.PutProvisionedConcurrencyConfigResponseTypeDef" = (
        dataclasses.field()
    )

    RequestedProvisionedConcurrentExecutions = field(
        "RequestedProvisionedConcurrentExecutions"
    )
    AvailableProvisionedConcurrentExecutions = field(
        "AvailableProvisionedConcurrentExecutions"
    )
    AllocatedProvisionedConcurrentExecutions = field(
        "AllocatedProvisionedConcurrentExecutions"
    )
    Status = field("Status")
    StatusReason = field("StatusReason")
    LastModified = field("LastModified")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutProvisionedConcurrencyConfigResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutProvisionedConcurrencyConfigResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutRuntimeManagementConfigResponse:
    boto3_raw_data: "type_defs.PutRuntimeManagementConfigResponseTypeDef" = (
        dataclasses.field()
    )

    UpdateRuntimeOn = field("UpdateRuntimeOn")
    FunctionArn = field("FunctionArn")
    RuntimeVersionArn = field("RuntimeVersionArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutRuntimeManagementConfigResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutRuntimeManagementConfigResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AliasConfigurationResponse:
    boto3_raw_data: "type_defs.AliasConfigurationResponseTypeDef" = dataclasses.field()

    AliasArn = field("AliasArn")
    Name = field("Name")
    FunctionVersion = field("FunctionVersion")
    Description = field("Description")

    @cached_property
    def RoutingConfig(self):  # pragma: no cover
        return AliasRoutingConfigurationOutput.make_one(
            self.boto3_raw_data["RoutingConfig"]
        )

    RevisionId = field("RevisionId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AliasConfigurationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AliasConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AliasConfiguration:
    boto3_raw_data: "type_defs.AliasConfigurationTypeDef" = dataclasses.field()

    AliasArn = field("AliasArn")
    Name = field("Name")
    FunctionVersion = field("FunctionVersion")
    Description = field("Description")

    @cached_property
    def RoutingConfig(self):  # pragma: no cover
        return AliasRoutingConfigurationOutput.make_one(
            self.boto3_raw_data["RoutingConfig"]
        )

    RevisionId = field("RevisionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AliasConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AliasConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FunctionCode:
    boto3_raw_data: "type_defs.FunctionCodeTypeDef" = dataclasses.field()

    ZipFile = field("ZipFile")
    S3Bucket = field("S3Bucket")
    S3Key = field("S3Key")
    S3ObjectVersion = field("S3ObjectVersion")
    ImageUri = field("ImageUri")
    SourceKMSKeyArn = field("SourceKMSKeyArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FunctionCodeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FunctionCodeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InvocationRequest:
    boto3_raw_data: "type_defs.InvocationRequestTypeDef" = dataclasses.field()

    FunctionName = field("FunctionName")
    InvocationType = field("InvocationType")
    LogType = field("LogType")
    ClientContext = field("ClientContext")
    Payload = field("Payload")
    Qualifier = field("Qualifier")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InvocationRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InvocationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InvokeAsyncRequest:
    boto3_raw_data: "type_defs.InvokeAsyncRequestTypeDef" = dataclasses.field()

    FunctionName = field("FunctionName")
    InvokeArgs = field("InvokeArgs")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InvokeAsyncRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InvokeAsyncRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InvokeWithResponseStreamRequest:
    boto3_raw_data: "type_defs.InvokeWithResponseStreamRequestTypeDef" = (
        dataclasses.field()
    )

    FunctionName = field("FunctionName")
    InvocationType = field("InvocationType")
    LogType = field("LogType")
    ClientContext = field("ClientContext")
    Qualifier = field("Qualifier")
    Payload = field("Payload")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.InvokeWithResponseStreamRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InvokeWithResponseStreamRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LayerVersionContentInput:
    boto3_raw_data: "type_defs.LayerVersionContentInputTypeDef" = dataclasses.field()

    S3Bucket = field("S3Bucket")
    S3Key = field("S3Key")
    S3ObjectVersion = field("S3ObjectVersion")
    ZipFile = field("ZipFile")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LayerVersionContentInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LayerVersionContentInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFunctionCodeRequest:
    boto3_raw_data: "type_defs.UpdateFunctionCodeRequestTypeDef" = dataclasses.field()

    FunctionName = field("FunctionName")
    ZipFile = field("ZipFile")
    S3Bucket = field("S3Bucket")
    S3Key = field("S3Key")
    S3ObjectVersion = field("S3ObjectVersion")
    ImageUri = field("ImageUri")
    Publish = field("Publish")
    DryRun = field("DryRun")
    RevisionId = field("RevisionId")
    Architectures = field("Architectures")
    SourceKMSKeyArn = field("SourceKMSKeyArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateFunctionCodeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFunctionCodeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CodeSigningConfig:
    boto3_raw_data: "type_defs.CodeSigningConfigTypeDef" = dataclasses.field()

    CodeSigningConfigId = field("CodeSigningConfigId")
    CodeSigningConfigArn = field("CodeSigningConfigArn")

    @cached_property
    def AllowedPublishers(self):  # pragma: no cover
        return AllowedPublishersOutput.make_one(
            self.boto3_raw_data["AllowedPublishers"]
        )

    @cached_property
    def CodeSigningPolicies(self):  # pragma: no cover
        return CodeSigningPolicies.make_one(self.boto3_raw_data["CodeSigningPolicies"])

    LastModified = field("LastModified")
    Description = field("Description")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CodeSigningConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CodeSigningConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFunctionUrlConfigResponse:
    boto3_raw_data: "type_defs.CreateFunctionUrlConfigResponseTypeDef" = (
        dataclasses.field()
    )

    FunctionUrl = field("FunctionUrl")
    FunctionArn = field("FunctionArn")
    AuthType = field("AuthType")

    @cached_property
    def Cors(self):  # pragma: no cover
        return CorsOutput.make_one(self.boto3_raw_data["Cors"])

    CreationTime = field("CreationTime")
    InvokeMode = field("InvokeMode")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateFunctionUrlConfigResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFunctionUrlConfigResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FunctionUrlConfig:
    boto3_raw_data: "type_defs.FunctionUrlConfigTypeDef" = dataclasses.field()

    FunctionUrl = field("FunctionUrl")
    FunctionArn = field("FunctionArn")
    CreationTime = field("CreationTime")
    LastModifiedTime = field("LastModifiedTime")
    AuthType = field("AuthType")

    @cached_property
    def Cors(self):  # pragma: no cover
        return CorsOutput.make_one(self.boto3_raw_data["Cors"])

    InvokeMode = field("InvokeMode")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FunctionUrlConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FunctionUrlConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFunctionUrlConfigResponse:
    boto3_raw_data: "type_defs.GetFunctionUrlConfigResponseTypeDef" = (
        dataclasses.field()
    )

    FunctionUrl = field("FunctionUrl")
    FunctionArn = field("FunctionArn")
    AuthType = field("AuthType")

    @cached_property
    def Cors(self):  # pragma: no cover
        return CorsOutput.make_one(self.boto3_raw_data["Cors"])

    CreationTime = field("CreationTime")
    LastModifiedTime = field("LastModifiedTime")
    InvokeMode = field("InvokeMode")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetFunctionUrlConfigResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFunctionUrlConfigResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFunctionUrlConfigResponse:
    boto3_raw_data: "type_defs.UpdateFunctionUrlConfigResponseTypeDef" = (
        dataclasses.field()
    )

    FunctionUrl = field("FunctionUrl")
    FunctionArn = field("FunctionArn")
    AuthType = field("AuthType")

    @cached_property
    def Cors(self):  # pragma: no cover
        return CorsOutput.make_one(self.boto3_raw_data["Cors"])

    CreationTime = field("CreationTime")
    LastModifiedTime = field("LastModifiedTime")
    InvokeMode = field("InvokeMode")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateFunctionUrlConfigResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFunctionUrlConfigResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DestinationConfig:
    boto3_raw_data: "type_defs.DestinationConfigTypeDef" = dataclasses.field()

    @cached_property
    def OnSuccess(self):  # pragma: no cover
        return OnSuccess.make_one(self.boto3_raw_data["OnSuccess"])

    @cached_property
    def OnFailure(self):  # pragma: no cover
        return OnFailure.make_one(self.boto3_raw_data["OnFailure"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DestinationConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DestinationConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnvironmentResponse:
    boto3_raw_data: "type_defs.EnvironmentResponseTypeDef" = dataclasses.field()

    Variables = field("Variables")

    @cached_property
    def Error(self):  # pragma: no cover
        return EnvironmentError.make_one(self.boto3_raw_data["Error"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EnvironmentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnvironmentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FilterCriteriaOutput:
    boto3_raw_data: "type_defs.FilterCriteriaOutputTypeDef" = dataclasses.field()

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FilterCriteriaOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FilterCriteriaOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FilterCriteria:
    boto3_raw_data: "type_defs.FilterCriteriaTypeDef" = dataclasses.field()

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FilterCriteriaTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FilterCriteriaTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFunctionConfigurationRequestWaitExtraExtra:
    boto3_raw_data: "type_defs.GetFunctionConfigurationRequestWaitExtraExtraTypeDef" = (
        dataclasses.field()
    )

    FunctionName = field("FunctionName")
    Qualifier = field("Qualifier")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetFunctionConfigurationRequestWaitExtraExtraTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFunctionConfigurationRequestWaitExtraExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFunctionConfigurationRequestWaitExtra:
    boto3_raw_data: "type_defs.GetFunctionConfigurationRequestWaitExtraTypeDef" = (
        dataclasses.field()
    )

    FunctionName = field("FunctionName")
    Qualifier = field("Qualifier")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetFunctionConfigurationRequestWaitExtraTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFunctionConfigurationRequestWaitExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFunctionConfigurationRequestWait:
    boto3_raw_data: "type_defs.GetFunctionConfigurationRequestWaitTypeDef" = (
        dataclasses.field()
    )

    FunctionName = field("FunctionName")
    Qualifier = field("Qualifier")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetFunctionConfigurationRequestWaitTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFunctionConfigurationRequestWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFunctionRequestWaitExtraExtra:
    boto3_raw_data: "type_defs.GetFunctionRequestWaitExtraExtraTypeDef" = (
        dataclasses.field()
    )

    FunctionName = field("FunctionName")
    Qualifier = field("Qualifier")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetFunctionRequestWaitExtraExtraTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFunctionRequestWaitExtraExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFunctionRequestWaitExtra:
    boto3_raw_data: "type_defs.GetFunctionRequestWaitExtraTypeDef" = dataclasses.field()

    FunctionName = field("FunctionName")
    Qualifier = field("Qualifier")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetFunctionRequestWaitExtraTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFunctionRequestWaitExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFunctionRequestWait:
    boto3_raw_data: "type_defs.GetFunctionRequestWaitTypeDef" = dataclasses.field()

    FunctionName = field("FunctionName")
    Qualifier = field("Qualifier")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetFunctionRequestWaitTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFunctionRequestWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLayerVersionResponse:
    boto3_raw_data: "type_defs.GetLayerVersionResponseTypeDef" = dataclasses.field()

    @cached_property
    def Content(self):  # pragma: no cover
        return LayerVersionContentOutput.make_one(self.boto3_raw_data["Content"])

    LayerArn = field("LayerArn")
    LayerVersionArn = field("LayerVersionArn")
    Description = field("Description")
    CreatedDate = field("CreatedDate")
    Version = field("Version")
    CompatibleRuntimes = field("CompatibleRuntimes")
    LicenseInfo = field("LicenseInfo")
    CompatibleArchitectures = field("CompatibleArchitectures")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetLayerVersionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLayerVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PublishLayerVersionResponse:
    boto3_raw_data: "type_defs.PublishLayerVersionResponseTypeDef" = dataclasses.field()

    @cached_property
    def Content(self):  # pragma: no cover
        return LayerVersionContentOutput.make_one(self.boto3_raw_data["Content"])

    LayerArn = field("LayerArn")
    LayerVersionArn = field("LayerVersionArn")
    Description = field("Description")
    CreatedDate = field("CreatedDate")
    Version = field("Version")
    CompatibleRuntimes = field("CompatibleRuntimes")
    LicenseInfo = field("LicenseInfo")
    CompatibleArchitectures = field("CompatibleArchitectures")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PublishLayerVersionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PublishLayerVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImageConfigResponse:
    boto3_raw_data: "type_defs.ImageConfigResponseTypeDef" = dataclasses.field()

    @cached_property
    def ImageConfig(self):  # pragma: no cover
        return ImageConfigOutput.make_one(self.boto3_raw_data["ImageConfig"])

    @cached_property
    def Error(self):  # pragma: no cover
        return ImageConfigError.make_one(self.boto3_raw_data["Error"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImageConfigResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImageConfigResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InvokeWithResponseStreamResponseEvent:
    boto3_raw_data: "type_defs.InvokeWithResponseStreamResponseEventTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PayloadChunk(self):  # pragma: no cover
        return InvokeResponseStreamUpdate.make_one(self.boto3_raw_data["PayloadChunk"])

    @cached_property
    def InvokeComplete(self):  # pragma: no cover
        return InvokeWithResponseStreamCompleteEvent.make_one(
            self.boto3_raw_data["InvokeComplete"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.InvokeWithResponseStreamResponseEventTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InvokeWithResponseStreamResponseEventTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KafkaSchemaRegistryConfigOutput:
    boto3_raw_data: "type_defs.KafkaSchemaRegistryConfigOutputTypeDef" = (
        dataclasses.field()
    )

    SchemaRegistryURI = field("SchemaRegistryURI")
    EventRecordFormat = field("EventRecordFormat")

    @cached_property
    def AccessConfigs(self):  # pragma: no cover
        return KafkaSchemaRegistryAccessConfig.make_many(
            self.boto3_raw_data["AccessConfigs"]
        )

    @cached_property
    def SchemaValidationConfigs(self):  # pragma: no cover
        return KafkaSchemaValidationConfig.make_many(
            self.boto3_raw_data["SchemaValidationConfigs"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.KafkaSchemaRegistryConfigOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KafkaSchemaRegistryConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KafkaSchemaRegistryConfig:
    boto3_raw_data: "type_defs.KafkaSchemaRegistryConfigTypeDef" = dataclasses.field()

    SchemaRegistryURI = field("SchemaRegistryURI")
    EventRecordFormat = field("EventRecordFormat")

    @cached_property
    def AccessConfigs(self):  # pragma: no cover
        return KafkaSchemaRegistryAccessConfig.make_many(
            self.boto3_raw_data["AccessConfigs"]
        )

    @cached_property
    def SchemaValidationConfigs(self):  # pragma: no cover
        return KafkaSchemaValidationConfig.make_many(
            self.boto3_raw_data["SchemaValidationConfigs"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KafkaSchemaRegistryConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KafkaSchemaRegistryConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LayersListItem:
    boto3_raw_data: "type_defs.LayersListItemTypeDef" = dataclasses.field()

    LayerName = field("LayerName")
    LayerArn = field("LayerArn")

    @cached_property
    def LatestMatchingVersion(self):  # pragma: no cover
        return LayerVersionsListItem.make_one(
            self.boto3_raw_data["LatestMatchingVersion"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LayersListItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LayersListItemTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLayerVersionsResponse:
    boto3_raw_data: "type_defs.ListLayerVersionsResponseTypeDef" = dataclasses.field()

    NextMarker = field("NextMarker")

    @cached_property
    def LayerVersions(self):  # pragma: no cover
        return LayerVersionsListItem.make_many(self.boto3_raw_data["LayerVersions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListLayerVersionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLayerVersionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAliasesRequestPaginate:
    boto3_raw_data: "type_defs.ListAliasesRequestPaginateTypeDef" = dataclasses.field()

    FunctionName = field("FunctionName")
    FunctionVersion = field("FunctionVersion")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAliasesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAliasesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCodeSigningConfigsRequestPaginate:
    boto3_raw_data: "type_defs.ListCodeSigningConfigsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCodeSigningConfigsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCodeSigningConfigsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEventSourceMappingsRequestPaginate:
    boto3_raw_data: "type_defs.ListEventSourceMappingsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    EventSourceArn = field("EventSourceArn")
    FunctionName = field("FunctionName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListEventSourceMappingsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEventSourceMappingsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFunctionEventInvokeConfigsRequestPaginate:
    boto3_raw_data: "type_defs.ListFunctionEventInvokeConfigsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    FunctionName = field("FunctionName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListFunctionEventInvokeConfigsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFunctionEventInvokeConfigsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFunctionUrlConfigsRequestPaginate:
    boto3_raw_data: "type_defs.ListFunctionUrlConfigsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    FunctionName = field("FunctionName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListFunctionUrlConfigsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFunctionUrlConfigsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFunctionsByCodeSigningConfigRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListFunctionsByCodeSigningConfigRequestPaginateTypeDef"
    ) = dataclasses.field()

    CodeSigningConfigArn = field("CodeSigningConfigArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListFunctionsByCodeSigningConfigRequestPaginateTypeDef"
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
                "type_defs.ListFunctionsByCodeSigningConfigRequestPaginateTypeDef"
            ]
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

    MasterRegion = field("MasterRegion")
    FunctionVersion = field("FunctionVersion")

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
class ListLayerVersionsRequestPaginate:
    boto3_raw_data: "type_defs.ListLayerVersionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    LayerName = field("LayerName")
    CompatibleRuntime = field("CompatibleRuntime")
    CompatibleArchitecture = field("CompatibleArchitecture")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListLayerVersionsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLayerVersionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLayersRequestPaginate:
    boto3_raw_data: "type_defs.ListLayersRequestPaginateTypeDef" = dataclasses.field()

    CompatibleRuntime = field("CompatibleRuntime")
    CompatibleArchitecture = field("CompatibleArchitecture")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListLayersRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLayersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProvisionedConcurrencyConfigsRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListProvisionedConcurrencyConfigsRequestPaginateTypeDef"
    ) = dataclasses.field()

    FunctionName = field("FunctionName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListProvisionedConcurrencyConfigsRequestPaginateTypeDef"
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
                "type_defs.ListProvisionedConcurrencyConfigsRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVersionsByFunctionRequestPaginate:
    boto3_raw_data: "type_defs.ListVersionsByFunctionRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    FunctionName = field("FunctionName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListVersionsByFunctionRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVersionsByFunctionRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProvisionedConcurrencyConfigsResponse:
    boto3_raw_data: "type_defs.ListProvisionedConcurrencyConfigsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ProvisionedConcurrencyConfigs(self):  # pragma: no cover
        return ProvisionedConcurrencyConfigListItem.make_many(
            self.boto3_raw_data["ProvisionedConcurrencyConfigs"]
        )

    NextMarker = field("NextMarker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListProvisionedConcurrencyConfigsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProvisionedConcurrencyConfigsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuntimeVersionConfig:
    boto3_raw_data: "type_defs.RuntimeVersionConfigTypeDef" = dataclasses.field()

    RuntimeVersionArn = field("RuntimeVersionArn")

    @cached_property
    def Error(self):  # pragma: no cover
        return RuntimeVersionError.make_one(self.boto3_raw_data["Error"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RuntimeVersionConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RuntimeVersionConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAliasesResponse:
    boto3_raw_data: "type_defs.ListAliasesResponseTypeDef" = dataclasses.field()

    NextMarker = field("NextMarker")

    @cached_property
    def Aliases(self):  # pragma: no cover
        return AliasConfiguration.make_many(self.boto3_raw_data["Aliases"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAliasesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAliasesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAliasRequest:
    boto3_raw_data: "type_defs.CreateAliasRequestTypeDef" = dataclasses.field()

    FunctionName = field("FunctionName")
    Name = field("Name")
    FunctionVersion = field("FunctionVersion")
    Description = field("Description")
    RoutingConfig = field("RoutingConfig")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAliasRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAliasRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAliasRequest:
    boto3_raw_data: "type_defs.UpdateAliasRequestTypeDef" = dataclasses.field()

    FunctionName = field("FunctionName")
    Name = field("Name")
    FunctionVersion = field("FunctionVersion")
    Description = field("Description")
    RoutingConfig = field("RoutingConfig")
    RevisionId = field("RevisionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAliasRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAliasRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCodeSigningConfigRequest:
    boto3_raw_data: "type_defs.CreateCodeSigningConfigRequestTypeDef" = (
        dataclasses.field()
    )

    AllowedPublishers = field("AllowedPublishers")
    Description = field("Description")

    @cached_property
    def CodeSigningPolicies(self):  # pragma: no cover
        return CodeSigningPolicies.make_one(self.boto3_raw_data["CodeSigningPolicies"])

    Tags = field("Tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateCodeSigningConfigRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCodeSigningConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCodeSigningConfigRequest:
    boto3_raw_data: "type_defs.UpdateCodeSigningConfigRequestTypeDef" = (
        dataclasses.field()
    )

    CodeSigningConfigArn = field("CodeSigningConfigArn")
    Description = field("Description")
    AllowedPublishers = field("AllowedPublishers")

    @cached_property
    def CodeSigningPolicies(self):  # pragma: no cover
        return CodeSigningPolicies.make_one(self.boto3_raw_data["CodeSigningPolicies"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateCodeSigningConfigRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCodeSigningConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PublishLayerVersionRequest:
    boto3_raw_data: "type_defs.PublishLayerVersionRequestTypeDef" = dataclasses.field()

    LayerName = field("LayerName")

    @cached_property
    def Content(self):  # pragma: no cover
        return LayerVersionContentInput.make_one(self.boto3_raw_data["Content"])

    Description = field("Description")
    CompatibleRuntimes = field("CompatibleRuntimes")
    LicenseInfo = field("LicenseInfo")
    CompatibleArchitectures = field("CompatibleArchitectures")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PublishLayerVersionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PublishLayerVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCodeSigningConfigResponse:
    boto3_raw_data: "type_defs.CreateCodeSigningConfigResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CodeSigningConfig(self):  # pragma: no cover
        return CodeSigningConfig.make_one(self.boto3_raw_data["CodeSigningConfig"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateCodeSigningConfigResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCodeSigningConfigResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCodeSigningConfigResponse:
    boto3_raw_data: "type_defs.GetCodeSigningConfigResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CodeSigningConfig(self):  # pragma: no cover
        return CodeSigningConfig.make_one(self.boto3_raw_data["CodeSigningConfig"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCodeSigningConfigResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCodeSigningConfigResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCodeSigningConfigsResponse:
    boto3_raw_data: "type_defs.ListCodeSigningConfigsResponseTypeDef" = (
        dataclasses.field()
    )

    NextMarker = field("NextMarker")

    @cached_property
    def CodeSigningConfigs(self):  # pragma: no cover
        return CodeSigningConfig.make_many(self.boto3_raw_data["CodeSigningConfigs"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListCodeSigningConfigsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCodeSigningConfigsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCodeSigningConfigResponse:
    boto3_raw_data: "type_defs.UpdateCodeSigningConfigResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CodeSigningConfig(self):  # pragma: no cover
        return CodeSigningConfig.make_one(self.boto3_raw_data["CodeSigningConfig"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateCodeSigningConfigResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCodeSigningConfigResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFunctionUrlConfigsResponse:
    boto3_raw_data: "type_defs.ListFunctionUrlConfigsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def FunctionUrlConfigs(self):  # pragma: no cover
        return FunctionUrlConfig.make_many(self.boto3_raw_data["FunctionUrlConfigs"])

    NextMarker = field("NextMarker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListFunctionUrlConfigsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFunctionUrlConfigsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFunctionUrlConfigRequest:
    boto3_raw_data: "type_defs.CreateFunctionUrlConfigRequestTypeDef" = (
        dataclasses.field()
    )

    FunctionName = field("FunctionName")
    AuthType = field("AuthType")
    Qualifier = field("Qualifier")
    Cors = field("Cors")
    InvokeMode = field("InvokeMode")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateFunctionUrlConfigRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFunctionUrlConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFunctionUrlConfigRequest:
    boto3_raw_data: "type_defs.UpdateFunctionUrlConfigRequestTypeDef" = (
        dataclasses.field()
    )

    FunctionName = field("FunctionName")
    Qualifier = field("Qualifier")
    AuthType = field("AuthType")
    Cors = field("Cors")
    InvokeMode = field("InvokeMode")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateFunctionUrlConfigRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFunctionUrlConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FunctionEventInvokeConfigResponse:
    boto3_raw_data: "type_defs.FunctionEventInvokeConfigResponseTypeDef" = (
        dataclasses.field()
    )

    LastModified = field("LastModified")
    FunctionArn = field("FunctionArn")
    MaximumRetryAttempts = field("MaximumRetryAttempts")
    MaximumEventAgeInSeconds = field("MaximumEventAgeInSeconds")

    @cached_property
    def DestinationConfig(self):  # pragma: no cover
        return DestinationConfig.make_one(self.boto3_raw_data["DestinationConfig"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.FunctionEventInvokeConfigResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FunctionEventInvokeConfigResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FunctionEventInvokeConfig:
    boto3_raw_data: "type_defs.FunctionEventInvokeConfigTypeDef" = dataclasses.field()

    LastModified = field("LastModified")
    FunctionArn = field("FunctionArn")
    MaximumRetryAttempts = field("MaximumRetryAttempts")
    MaximumEventAgeInSeconds = field("MaximumEventAgeInSeconds")

    @cached_property
    def DestinationConfig(self):  # pragma: no cover
        return DestinationConfig.make_one(self.boto3_raw_data["DestinationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FunctionEventInvokeConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FunctionEventInvokeConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutFunctionEventInvokeConfigRequest:
    boto3_raw_data: "type_defs.PutFunctionEventInvokeConfigRequestTypeDef" = (
        dataclasses.field()
    )

    FunctionName = field("FunctionName")
    Qualifier = field("Qualifier")
    MaximumRetryAttempts = field("MaximumRetryAttempts")
    MaximumEventAgeInSeconds = field("MaximumEventAgeInSeconds")

    @cached_property
    def DestinationConfig(self):  # pragma: no cover
        return DestinationConfig.make_one(self.boto3_raw_data["DestinationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutFunctionEventInvokeConfigRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutFunctionEventInvokeConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFunctionEventInvokeConfigRequest:
    boto3_raw_data: "type_defs.UpdateFunctionEventInvokeConfigRequestTypeDef" = (
        dataclasses.field()
    )

    FunctionName = field("FunctionName")
    Qualifier = field("Qualifier")
    MaximumRetryAttempts = field("MaximumRetryAttempts")
    MaximumEventAgeInSeconds = field("MaximumEventAgeInSeconds")

    @cached_property
    def DestinationConfig(self):  # pragma: no cover
        return DestinationConfig.make_one(self.boto3_raw_data["DestinationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateFunctionEventInvokeConfigRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFunctionEventInvokeConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFunctionRequest:
    boto3_raw_data: "type_defs.CreateFunctionRequestTypeDef" = dataclasses.field()

    FunctionName = field("FunctionName")
    Role = field("Role")

    @cached_property
    def Code(self):  # pragma: no cover
        return FunctionCode.make_one(self.boto3_raw_data["Code"])

    Runtime = field("Runtime")
    Handler = field("Handler")
    Description = field("Description")
    Timeout = field("Timeout")
    MemorySize = field("MemorySize")
    Publish = field("Publish")

    @cached_property
    def VpcConfig(self):  # pragma: no cover
        return VpcConfig.make_one(self.boto3_raw_data["VpcConfig"])

    PackageType = field("PackageType")

    @cached_property
    def DeadLetterConfig(self):  # pragma: no cover
        return DeadLetterConfig.make_one(self.boto3_raw_data["DeadLetterConfig"])

    @cached_property
    def Environment(self):  # pragma: no cover
        return Environment.make_one(self.boto3_raw_data["Environment"])

    KMSKeyArn = field("KMSKeyArn")

    @cached_property
    def TracingConfig(self):  # pragma: no cover
        return TracingConfig.make_one(self.boto3_raw_data["TracingConfig"])

    Tags = field("Tags")
    Layers = field("Layers")

    @cached_property
    def FileSystemConfigs(self):  # pragma: no cover
        return FileSystemConfig.make_many(self.boto3_raw_data["FileSystemConfigs"])

    ImageConfig = field("ImageConfig")
    CodeSigningConfigArn = field("CodeSigningConfigArn")
    Architectures = field("Architectures")

    @cached_property
    def EphemeralStorage(self):  # pragma: no cover
        return EphemeralStorage.make_one(self.boto3_raw_data["EphemeralStorage"])

    @cached_property
    def SnapStart(self):  # pragma: no cover
        return SnapStart.make_one(self.boto3_raw_data["SnapStart"])

    @cached_property
    def LoggingConfig(self):  # pragma: no cover
        return LoggingConfig.make_one(self.boto3_raw_data["LoggingConfig"])

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
class UpdateFunctionConfigurationRequest:
    boto3_raw_data: "type_defs.UpdateFunctionConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    FunctionName = field("FunctionName")
    Role = field("Role")
    Handler = field("Handler")
    Description = field("Description")
    Timeout = field("Timeout")
    MemorySize = field("MemorySize")

    @cached_property
    def VpcConfig(self):  # pragma: no cover
        return VpcConfig.make_one(self.boto3_raw_data["VpcConfig"])

    @cached_property
    def Environment(self):  # pragma: no cover
        return Environment.make_one(self.boto3_raw_data["Environment"])

    Runtime = field("Runtime")

    @cached_property
    def DeadLetterConfig(self):  # pragma: no cover
        return DeadLetterConfig.make_one(self.boto3_raw_data["DeadLetterConfig"])

    KMSKeyArn = field("KMSKeyArn")

    @cached_property
    def TracingConfig(self):  # pragma: no cover
        return TracingConfig.make_one(self.boto3_raw_data["TracingConfig"])

    RevisionId = field("RevisionId")
    Layers = field("Layers")

    @cached_property
    def FileSystemConfigs(self):  # pragma: no cover
        return FileSystemConfig.make_many(self.boto3_raw_data["FileSystemConfigs"])

    ImageConfig = field("ImageConfig")

    @cached_property
    def EphemeralStorage(self):  # pragma: no cover
        return EphemeralStorage.make_one(self.boto3_raw_data["EphemeralStorage"])

    @cached_property
    def SnapStart(self):  # pragma: no cover
        return SnapStart.make_one(self.boto3_raw_data["SnapStart"])

    @cached_property
    def LoggingConfig(self):  # pragma: no cover
        return LoggingConfig.make_one(self.boto3_raw_data["LoggingConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateFunctionConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFunctionConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InvokeWithResponseStreamResponse:
    boto3_raw_data: "type_defs.InvokeWithResponseStreamResponseTypeDef" = (
        dataclasses.field()
    )

    StatusCode = field("StatusCode")
    ExecutedVersion = field("ExecutedVersion")
    EventStream = field("EventStream")
    ResponseStreamContentType = field("ResponseStreamContentType")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.InvokeWithResponseStreamResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InvokeWithResponseStreamResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AmazonManagedKafkaEventSourceConfigOutput:
    boto3_raw_data: "type_defs.AmazonManagedKafkaEventSourceConfigOutputTypeDef" = (
        dataclasses.field()
    )

    ConsumerGroupId = field("ConsumerGroupId")

    @cached_property
    def SchemaRegistryConfig(self):  # pragma: no cover
        return KafkaSchemaRegistryConfigOutput.make_one(
            self.boto3_raw_data["SchemaRegistryConfig"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AmazonManagedKafkaEventSourceConfigOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AmazonManagedKafkaEventSourceConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SelfManagedKafkaEventSourceConfigOutput:
    boto3_raw_data: "type_defs.SelfManagedKafkaEventSourceConfigOutputTypeDef" = (
        dataclasses.field()
    )

    ConsumerGroupId = field("ConsumerGroupId")

    @cached_property
    def SchemaRegistryConfig(self):  # pragma: no cover
        return KafkaSchemaRegistryConfigOutput.make_one(
            self.boto3_raw_data["SchemaRegistryConfig"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SelfManagedKafkaEventSourceConfigOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SelfManagedKafkaEventSourceConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AmazonManagedKafkaEventSourceConfig:
    boto3_raw_data: "type_defs.AmazonManagedKafkaEventSourceConfigTypeDef" = (
        dataclasses.field()
    )

    ConsumerGroupId = field("ConsumerGroupId")

    @cached_property
    def SchemaRegistryConfig(self):  # pragma: no cover
        return KafkaSchemaRegistryConfig.make_one(
            self.boto3_raw_data["SchemaRegistryConfig"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AmazonManagedKafkaEventSourceConfigTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AmazonManagedKafkaEventSourceConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SelfManagedKafkaEventSourceConfig:
    boto3_raw_data: "type_defs.SelfManagedKafkaEventSourceConfigTypeDef" = (
        dataclasses.field()
    )

    ConsumerGroupId = field("ConsumerGroupId")

    @cached_property
    def SchemaRegistryConfig(self):  # pragma: no cover
        return KafkaSchemaRegistryConfig.make_one(
            self.boto3_raw_data["SchemaRegistryConfig"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SelfManagedKafkaEventSourceConfigTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SelfManagedKafkaEventSourceConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLayersResponse:
    boto3_raw_data: "type_defs.ListLayersResponseTypeDef" = dataclasses.field()

    NextMarker = field("NextMarker")

    @cached_property
    def Layers(self):  # pragma: no cover
        return LayersListItem.make_many(self.boto3_raw_data["Layers"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListLayersResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLayersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FunctionConfigurationResponse:
    boto3_raw_data: "type_defs.FunctionConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    FunctionName = field("FunctionName")
    FunctionArn = field("FunctionArn")
    Runtime = field("Runtime")
    Role = field("Role")
    Handler = field("Handler")
    CodeSize = field("CodeSize")
    Description = field("Description")
    Timeout = field("Timeout")
    MemorySize = field("MemorySize")
    LastModified = field("LastModified")
    CodeSha256 = field("CodeSha256")
    Version = field("Version")

    @cached_property
    def VpcConfig(self):  # pragma: no cover
        return VpcConfigResponse.make_one(self.boto3_raw_data["VpcConfig"])

    @cached_property
    def DeadLetterConfig(self):  # pragma: no cover
        return DeadLetterConfig.make_one(self.boto3_raw_data["DeadLetterConfig"])

    @cached_property
    def Environment(self):  # pragma: no cover
        return EnvironmentResponse.make_one(self.boto3_raw_data["Environment"])

    KMSKeyArn = field("KMSKeyArn")

    @cached_property
    def TracingConfig(self):  # pragma: no cover
        return TracingConfigResponse.make_one(self.boto3_raw_data["TracingConfig"])

    MasterArn = field("MasterArn")
    RevisionId = field("RevisionId")

    @cached_property
    def Layers(self):  # pragma: no cover
        return Layer.make_many(self.boto3_raw_data["Layers"])

    State = field("State")
    StateReason = field("StateReason")
    StateReasonCode = field("StateReasonCode")
    LastUpdateStatus = field("LastUpdateStatus")
    LastUpdateStatusReason = field("LastUpdateStatusReason")
    LastUpdateStatusReasonCode = field("LastUpdateStatusReasonCode")

    @cached_property
    def FileSystemConfigs(self):  # pragma: no cover
        return FileSystemConfig.make_many(self.boto3_raw_data["FileSystemConfigs"])

    PackageType = field("PackageType")

    @cached_property
    def ImageConfigResponse(self):  # pragma: no cover
        return ImageConfigResponse.make_one(self.boto3_raw_data["ImageConfigResponse"])

    SigningProfileVersionArn = field("SigningProfileVersionArn")
    SigningJobArn = field("SigningJobArn")
    Architectures = field("Architectures")

    @cached_property
    def EphemeralStorage(self):  # pragma: no cover
        return EphemeralStorage.make_one(self.boto3_raw_data["EphemeralStorage"])

    @cached_property
    def SnapStart(self):  # pragma: no cover
        return SnapStartResponse.make_one(self.boto3_raw_data["SnapStart"])

    @cached_property
    def RuntimeVersionConfig(self):  # pragma: no cover
        return RuntimeVersionConfig.make_one(
            self.boto3_raw_data["RuntimeVersionConfig"]
        )

    @cached_property
    def LoggingConfig(self):  # pragma: no cover
        return LoggingConfig.make_one(self.boto3_raw_data["LoggingConfig"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.FunctionConfigurationResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FunctionConfigurationResponseTypeDef"]
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

    FunctionName = field("FunctionName")
    FunctionArn = field("FunctionArn")
    Runtime = field("Runtime")
    Role = field("Role")
    Handler = field("Handler")
    CodeSize = field("CodeSize")
    Description = field("Description")
    Timeout = field("Timeout")
    MemorySize = field("MemorySize")
    LastModified = field("LastModified")
    CodeSha256 = field("CodeSha256")
    Version = field("Version")

    @cached_property
    def VpcConfig(self):  # pragma: no cover
        return VpcConfigResponse.make_one(self.boto3_raw_data["VpcConfig"])

    @cached_property
    def DeadLetterConfig(self):  # pragma: no cover
        return DeadLetterConfig.make_one(self.boto3_raw_data["DeadLetterConfig"])

    @cached_property
    def Environment(self):  # pragma: no cover
        return EnvironmentResponse.make_one(self.boto3_raw_data["Environment"])

    KMSKeyArn = field("KMSKeyArn")

    @cached_property
    def TracingConfig(self):  # pragma: no cover
        return TracingConfigResponse.make_one(self.boto3_raw_data["TracingConfig"])

    MasterArn = field("MasterArn")
    RevisionId = field("RevisionId")

    @cached_property
    def Layers(self):  # pragma: no cover
        return Layer.make_many(self.boto3_raw_data["Layers"])

    State = field("State")
    StateReason = field("StateReason")
    StateReasonCode = field("StateReasonCode")
    LastUpdateStatus = field("LastUpdateStatus")
    LastUpdateStatusReason = field("LastUpdateStatusReason")
    LastUpdateStatusReasonCode = field("LastUpdateStatusReasonCode")

    @cached_property
    def FileSystemConfigs(self):  # pragma: no cover
        return FileSystemConfig.make_many(self.boto3_raw_data["FileSystemConfigs"])

    PackageType = field("PackageType")

    @cached_property
    def ImageConfigResponse(self):  # pragma: no cover
        return ImageConfigResponse.make_one(self.boto3_raw_data["ImageConfigResponse"])

    SigningProfileVersionArn = field("SigningProfileVersionArn")
    SigningJobArn = field("SigningJobArn")
    Architectures = field("Architectures")

    @cached_property
    def EphemeralStorage(self):  # pragma: no cover
        return EphemeralStorage.make_one(self.boto3_raw_data["EphemeralStorage"])

    @cached_property
    def SnapStart(self):  # pragma: no cover
        return SnapStartResponse.make_one(self.boto3_raw_data["SnapStart"])

    @cached_property
    def RuntimeVersionConfig(self):  # pragma: no cover
        return RuntimeVersionConfig.make_one(
            self.boto3_raw_data["RuntimeVersionConfig"]
        )

    @cached_property
    def LoggingConfig(self):  # pragma: no cover
        return LoggingConfig.make_one(self.boto3_raw_data["LoggingConfig"])

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
class ListFunctionEventInvokeConfigsResponse:
    boto3_raw_data: "type_defs.ListFunctionEventInvokeConfigsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def FunctionEventInvokeConfigs(self):  # pragma: no cover
        return FunctionEventInvokeConfig.make_many(
            self.boto3_raw_data["FunctionEventInvokeConfigs"]
        )

    NextMarker = field("NextMarker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListFunctionEventInvokeConfigsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFunctionEventInvokeConfigsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventSourceMappingConfigurationResponse:
    boto3_raw_data: "type_defs.EventSourceMappingConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    UUID = field("UUID")
    StartingPosition = field("StartingPosition")
    StartingPositionTimestamp = field("StartingPositionTimestamp")
    BatchSize = field("BatchSize")
    MaximumBatchingWindowInSeconds = field("MaximumBatchingWindowInSeconds")
    ParallelizationFactor = field("ParallelizationFactor")
    EventSourceArn = field("EventSourceArn")

    @cached_property
    def FilterCriteria(self):  # pragma: no cover
        return FilterCriteriaOutput.make_one(self.boto3_raw_data["FilterCriteria"])

    FunctionArn = field("FunctionArn")
    LastModified = field("LastModified")
    LastProcessingResult = field("LastProcessingResult")
    State = field("State")
    StateTransitionReason = field("StateTransitionReason")

    @cached_property
    def DestinationConfig(self):  # pragma: no cover
        return DestinationConfig.make_one(self.boto3_raw_data["DestinationConfig"])

    Topics = field("Topics")
    Queues = field("Queues")

    @cached_property
    def SourceAccessConfigurations(self):  # pragma: no cover
        return SourceAccessConfiguration.make_many(
            self.boto3_raw_data["SourceAccessConfigurations"]
        )

    @cached_property
    def SelfManagedEventSource(self):  # pragma: no cover
        return SelfManagedEventSourceOutput.make_one(
            self.boto3_raw_data["SelfManagedEventSource"]
        )

    MaximumRecordAgeInSeconds = field("MaximumRecordAgeInSeconds")
    BisectBatchOnFunctionError = field("BisectBatchOnFunctionError")
    MaximumRetryAttempts = field("MaximumRetryAttempts")
    TumblingWindowInSeconds = field("TumblingWindowInSeconds")
    FunctionResponseTypes = field("FunctionResponseTypes")

    @cached_property
    def AmazonManagedKafkaEventSourceConfig(self):  # pragma: no cover
        return AmazonManagedKafkaEventSourceConfigOutput.make_one(
            self.boto3_raw_data["AmazonManagedKafkaEventSourceConfig"]
        )

    @cached_property
    def SelfManagedKafkaEventSourceConfig(self):  # pragma: no cover
        return SelfManagedKafkaEventSourceConfigOutput.make_one(
            self.boto3_raw_data["SelfManagedKafkaEventSourceConfig"]
        )

    @cached_property
    def ScalingConfig(self):  # pragma: no cover
        return ScalingConfig.make_one(self.boto3_raw_data["ScalingConfig"])

    @cached_property
    def DocumentDBEventSourceConfig(self):  # pragma: no cover
        return DocumentDBEventSourceConfig.make_one(
            self.boto3_raw_data["DocumentDBEventSourceConfig"]
        )

    KMSKeyArn = field("KMSKeyArn")

    @cached_property
    def FilterCriteriaError(self):  # pragma: no cover
        return FilterCriteriaError.make_one(self.boto3_raw_data["FilterCriteriaError"])

    EventSourceMappingArn = field("EventSourceMappingArn")

    @cached_property
    def MetricsConfig(self):  # pragma: no cover
        return EventSourceMappingMetricsConfigOutput.make_one(
            self.boto3_raw_data["MetricsConfig"]
        )

    @cached_property
    def ProvisionedPollerConfig(self):  # pragma: no cover
        return ProvisionedPollerConfig.make_one(
            self.boto3_raw_data["ProvisionedPollerConfig"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.EventSourceMappingConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EventSourceMappingConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventSourceMappingConfiguration:
    boto3_raw_data: "type_defs.EventSourceMappingConfigurationTypeDef" = (
        dataclasses.field()
    )

    UUID = field("UUID")
    StartingPosition = field("StartingPosition")
    StartingPositionTimestamp = field("StartingPositionTimestamp")
    BatchSize = field("BatchSize")
    MaximumBatchingWindowInSeconds = field("MaximumBatchingWindowInSeconds")
    ParallelizationFactor = field("ParallelizationFactor")
    EventSourceArn = field("EventSourceArn")

    @cached_property
    def FilterCriteria(self):  # pragma: no cover
        return FilterCriteriaOutput.make_one(self.boto3_raw_data["FilterCriteria"])

    FunctionArn = field("FunctionArn")
    LastModified = field("LastModified")
    LastProcessingResult = field("LastProcessingResult")
    State = field("State")
    StateTransitionReason = field("StateTransitionReason")

    @cached_property
    def DestinationConfig(self):  # pragma: no cover
        return DestinationConfig.make_one(self.boto3_raw_data["DestinationConfig"])

    Topics = field("Topics")
    Queues = field("Queues")

    @cached_property
    def SourceAccessConfigurations(self):  # pragma: no cover
        return SourceAccessConfiguration.make_many(
            self.boto3_raw_data["SourceAccessConfigurations"]
        )

    @cached_property
    def SelfManagedEventSource(self):  # pragma: no cover
        return SelfManagedEventSourceOutput.make_one(
            self.boto3_raw_data["SelfManagedEventSource"]
        )

    MaximumRecordAgeInSeconds = field("MaximumRecordAgeInSeconds")
    BisectBatchOnFunctionError = field("BisectBatchOnFunctionError")
    MaximumRetryAttempts = field("MaximumRetryAttempts")
    TumblingWindowInSeconds = field("TumblingWindowInSeconds")
    FunctionResponseTypes = field("FunctionResponseTypes")

    @cached_property
    def AmazonManagedKafkaEventSourceConfig(self):  # pragma: no cover
        return AmazonManagedKafkaEventSourceConfigOutput.make_one(
            self.boto3_raw_data["AmazonManagedKafkaEventSourceConfig"]
        )

    @cached_property
    def SelfManagedKafkaEventSourceConfig(self):  # pragma: no cover
        return SelfManagedKafkaEventSourceConfigOutput.make_one(
            self.boto3_raw_data["SelfManagedKafkaEventSourceConfig"]
        )

    @cached_property
    def ScalingConfig(self):  # pragma: no cover
        return ScalingConfig.make_one(self.boto3_raw_data["ScalingConfig"])

    @cached_property
    def DocumentDBEventSourceConfig(self):  # pragma: no cover
        return DocumentDBEventSourceConfig.make_one(
            self.boto3_raw_data["DocumentDBEventSourceConfig"]
        )

    KMSKeyArn = field("KMSKeyArn")

    @cached_property
    def FilterCriteriaError(self):  # pragma: no cover
        return FilterCriteriaError.make_one(self.boto3_raw_data["FilterCriteriaError"])

    EventSourceMappingArn = field("EventSourceMappingArn")

    @cached_property
    def MetricsConfig(self):  # pragma: no cover
        return EventSourceMappingMetricsConfigOutput.make_one(
            self.boto3_raw_data["MetricsConfig"]
        )

    @cached_property
    def ProvisionedPollerConfig(self):  # pragma: no cover
        return ProvisionedPollerConfig.make_one(
            self.boto3_raw_data["ProvisionedPollerConfig"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.EventSourceMappingConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EventSourceMappingConfigurationTypeDef"]
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
    def Configuration(self):  # pragma: no cover
        return FunctionConfiguration.make_one(self.boto3_raw_data["Configuration"])

    @cached_property
    def Code(self):  # pragma: no cover
        return FunctionCodeLocation.make_one(self.boto3_raw_data["Code"])

    Tags = field("Tags")

    @cached_property
    def TagsError(self):  # pragma: no cover
        return TagsError.make_one(self.boto3_raw_data["TagsError"])

    @cached_property
    def Concurrency(self):  # pragma: no cover
        return Concurrency.make_one(self.boto3_raw_data["Concurrency"])

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

    NextMarker = field("NextMarker")

    @cached_property
    def Functions(self):  # pragma: no cover
        return FunctionConfiguration.make_many(self.boto3_raw_data["Functions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

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
class ListVersionsByFunctionResponse:
    boto3_raw_data: "type_defs.ListVersionsByFunctionResponseTypeDef" = (
        dataclasses.field()
    )

    NextMarker = field("NextMarker")

    @cached_property
    def Versions(self):  # pragma: no cover
        return FunctionConfiguration.make_many(self.boto3_raw_data["Versions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListVersionsByFunctionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVersionsByFunctionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEventSourceMappingsResponse:
    boto3_raw_data: "type_defs.ListEventSourceMappingsResponseTypeDef" = (
        dataclasses.field()
    )

    NextMarker = field("NextMarker")

    @cached_property
    def EventSourceMappings(self):  # pragma: no cover
        return EventSourceMappingConfiguration.make_many(
            self.boto3_raw_data["EventSourceMappings"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListEventSourceMappingsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEventSourceMappingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEventSourceMappingRequest:
    boto3_raw_data: "type_defs.CreateEventSourceMappingRequestTypeDef" = (
        dataclasses.field()
    )

    FunctionName = field("FunctionName")
    EventSourceArn = field("EventSourceArn")
    Enabled = field("Enabled")
    BatchSize = field("BatchSize")
    FilterCriteria = field("FilterCriteria")
    MaximumBatchingWindowInSeconds = field("MaximumBatchingWindowInSeconds")
    ParallelizationFactor = field("ParallelizationFactor")
    StartingPosition = field("StartingPosition")
    StartingPositionTimestamp = field("StartingPositionTimestamp")

    @cached_property
    def DestinationConfig(self):  # pragma: no cover
        return DestinationConfig.make_one(self.boto3_raw_data["DestinationConfig"])

    MaximumRecordAgeInSeconds = field("MaximumRecordAgeInSeconds")
    BisectBatchOnFunctionError = field("BisectBatchOnFunctionError")
    MaximumRetryAttempts = field("MaximumRetryAttempts")
    Tags = field("Tags")
    TumblingWindowInSeconds = field("TumblingWindowInSeconds")
    Topics = field("Topics")
    Queues = field("Queues")

    @cached_property
    def SourceAccessConfigurations(self):  # pragma: no cover
        return SourceAccessConfiguration.make_many(
            self.boto3_raw_data["SourceAccessConfigurations"]
        )

    SelfManagedEventSource = field("SelfManagedEventSource")
    FunctionResponseTypes = field("FunctionResponseTypes")
    AmazonManagedKafkaEventSourceConfig = field("AmazonManagedKafkaEventSourceConfig")
    SelfManagedKafkaEventSourceConfig = field("SelfManagedKafkaEventSourceConfig")

    @cached_property
    def ScalingConfig(self):  # pragma: no cover
        return ScalingConfig.make_one(self.boto3_raw_data["ScalingConfig"])

    @cached_property
    def DocumentDBEventSourceConfig(self):  # pragma: no cover
        return DocumentDBEventSourceConfig.make_one(
            self.boto3_raw_data["DocumentDBEventSourceConfig"]
        )

    KMSKeyArn = field("KMSKeyArn")
    MetricsConfig = field("MetricsConfig")

    @cached_property
    def ProvisionedPollerConfig(self):  # pragma: no cover
        return ProvisionedPollerConfig.make_one(
            self.boto3_raw_data["ProvisionedPollerConfig"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateEventSourceMappingRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEventSourceMappingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateEventSourceMappingRequest:
    boto3_raw_data: "type_defs.UpdateEventSourceMappingRequestTypeDef" = (
        dataclasses.field()
    )

    UUID = field("UUID")
    FunctionName = field("FunctionName")
    Enabled = field("Enabled")
    BatchSize = field("BatchSize")
    FilterCriteria = field("FilterCriteria")
    MaximumBatchingWindowInSeconds = field("MaximumBatchingWindowInSeconds")

    @cached_property
    def DestinationConfig(self):  # pragma: no cover
        return DestinationConfig.make_one(self.boto3_raw_data["DestinationConfig"])

    MaximumRecordAgeInSeconds = field("MaximumRecordAgeInSeconds")
    BisectBatchOnFunctionError = field("BisectBatchOnFunctionError")
    MaximumRetryAttempts = field("MaximumRetryAttempts")
    ParallelizationFactor = field("ParallelizationFactor")

    @cached_property
    def SourceAccessConfigurations(self):  # pragma: no cover
        return SourceAccessConfiguration.make_many(
            self.boto3_raw_data["SourceAccessConfigurations"]
        )

    TumblingWindowInSeconds = field("TumblingWindowInSeconds")
    FunctionResponseTypes = field("FunctionResponseTypes")

    @cached_property
    def ScalingConfig(self):  # pragma: no cover
        return ScalingConfig.make_one(self.boto3_raw_data["ScalingConfig"])

    AmazonManagedKafkaEventSourceConfig = field("AmazonManagedKafkaEventSourceConfig")
    SelfManagedKafkaEventSourceConfig = field("SelfManagedKafkaEventSourceConfig")

    @cached_property
    def DocumentDBEventSourceConfig(self):  # pragma: no cover
        return DocumentDBEventSourceConfig.make_one(
            self.boto3_raw_data["DocumentDBEventSourceConfig"]
        )

    KMSKeyArn = field("KMSKeyArn")
    MetricsConfig = field("MetricsConfig")

    @cached_property
    def ProvisionedPollerConfig(self):  # pragma: no cover
        return ProvisionedPollerConfig.make_one(
            self.boto3_raw_data["ProvisionedPollerConfig"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateEventSourceMappingRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateEventSourceMappingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
