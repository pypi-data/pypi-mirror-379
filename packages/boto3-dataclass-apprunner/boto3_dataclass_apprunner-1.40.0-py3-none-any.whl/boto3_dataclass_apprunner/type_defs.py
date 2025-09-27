# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_apprunner import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AssociateCustomDomainRequest:
    boto3_raw_data: "type_defs.AssociateCustomDomainRequestTypeDef" = (
        dataclasses.field()
    )

    ServiceArn = field("ServiceArn")
    DomainName = field("DomainName")
    EnableWWWSubdomain = field("EnableWWWSubdomain")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociateCustomDomainRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateCustomDomainRequestTypeDef"]
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
class VpcDNSTarget:
    boto3_raw_data: "type_defs.VpcDNSTargetTypeDef" = dataclasses.field()

    VpcIngressConnectionArn = field("VpcIngressConnectionArn")
    VpcId = field("VpcId")
    DomainName = field("DomainName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VpcDNSTargetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VpcDNSTargetTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AuthenticationConfiguration:
    boto3_raw_data: "type_defs.AuthenticationConfigurationTypeDef" = dataclasses.field()

    ConnectionArn = field("ConnectionArn")
    AccessRoleArn = field("AccessRoleArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AuthenticationConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AuthenticationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutoScalingConfigurationSummary:
    boto3_raw_data: "type_defs.AutoScalingConfigurationSummaryTypeDef" = (
        dataclasses.field()
    )

    AutoScalingConfigurationArn = field("AutoScalingConfigurationArn")
    AutoScalingConfigurationName = field("AutoScalingConfigurationName")
    AutoScalingConfigurationRevision = field("AutoScalingConfigurationRevision")
    Status = field("Status")
    CreatedAt = field("CreatedAt")
    HasAssociatedService = field("HasAssociatedService")
    IsDefault = field("IsDefault")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AutoScalingConfigurationSummaryTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutoScalingConfigurationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutoScalingConfiguration:
    boto3_raw_data: "type_defs.AutoScalingConfigurationTypeDef" = dataclasses.field()

    AutoScalingConfigurationArn = field("AutoScalingConfigurationArn")
    AutoScalingConfigurationName = field("AutoScalingConfigurationName")
    AutoScalingConfigurationRevision = field("AutoScalingConfigurationRevision")
    Latest = field("Latest")
    Status = field("Status")
    MaxConcurrency = field("MaxConcurrency")
    MinSize = field("MinSize")
    MaxSize = field("MaxSize")
    CreatedAt = field("CreatedAt")
    DeletedAt = field("DeletedAt")
    HasAssociatedService = field("HasAssociatedService")
    IsDefault = field("IsDefault")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AutoScalingConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutoScalingConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CertificateValidationRecord:
    boto3_raw_data: "type_defs.CertificateValidationRecordTypeDef" = dataclasses.field()

    Name = field("Name")
    Type = field("Type")
    Value = field("Value")
    Status = field("Status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CertificateValidationRecordTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CertificateValidationRecordTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CodeConfigurationValuesOutput:
    boto3_raw_data: "type_defs.CodeConfigurationValuesOutputTypeDef" = (
        dataclasses.field()
    )

    Runtime = field("Runtime")
    BuildCommand = field("BuildCommand")
    StartCommand = field("StartCommand")
    Port = field("Port")
    RuntimeEnvironmentVariables = field("RuntimeEnvironmentVariables")
    RuntimeEnvironmentSecrets = field("RuntimeEnvironmentSecrets")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CodeConfigurationValuesOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CodeConfigurationValuesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CodeConfigurationValues:
    boto3_raw_data: "type_defs.CodeConfigurationValuesTypeDef" = dataclasses.field()

    Runtime = field("Runtime")
    BuildCommand = field("BuildCommand")
    StartCommand = field("StartCommand")
    Port = field("Port")
    RuntimeEnvironmentVariables = field("RuntimeEnvironmentVariables")
    RuntimeEnvironmentSecrets = field("RuntimeEnvironmentSecrets")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CodeConfigurationValuesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CodeConfigurationValuesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SourceCodeVersion:
    boto3_raw_data: "type_defs.SourceCodeVersionTypeDef" = dataclasses.field()

    Type = field("Type")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SourceCodeVersionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SourceCodeVersionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConnectionSummary:
    boto3_raw_data: "type_defs.ConnectionSummaryTypeDef" = dataclasses.field()

    ConnectionName = field("ConnectionName")
    ConnectionArn = field("ConnectionArn")
    ProviderType = field("ProviderType")
    Status = field("Status")
    CreatedAt = field("CreatedAt")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConnectionSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConnectionSummaryTypeDef"]
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

    ConnectionName = field("ConnectionName")
    ConnectionArn = field("ConnectionArn")
    ProviderType = field("ProviderType")
    Status = field("Status")
    CreatedAt = field("CreatedAt")

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
class TraceConfiguration:
    boto3_raw_data: "type_defs.TraceConfigurationTypeDef" = dataclasses.field()

    Vendor = field("Vendor")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TraceConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TraceConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EncryptionConfiguration:
    boto3_raw_data: "type_defs.EncryptionConfigurationTypeDef" = dataclasses.field()

    KmsKey = field("KmsKey")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EncryptionConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EncryptionConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HealthCheckConfiguration:
    boto3_raw_data: "type_defs.HealthCheckConfigurationTypeDef" = dataclasses.field()

    Protocol = field("Protocol")
    Path = field("Path")
    Interval = field("Interval")
    Timeout = field("Timeout")
    HealthyThreshold = field("HealthyThreshold")
    UnhealthyThreshold = field("UnhealthyThreshold")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HealthCheckConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HealthCheckConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceConfiguration:
    boto3_raw_data: "type_defs.InstanceConfigurationTypeDef" = dataclasses.field()

    Cpu = field("Cpu")
    Memory = field("Memory")
    InstanceRoleArn = field("InstanceRoleArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InstanceConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstanceConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceObservabilityConfiguration:
    boto3_raw_data: "type_defs.ServiceObservabilityConfigurationTypeDef" = (
        dataclasses.field()
    )

    ObservabilityEnabled = field("ObservabilityEnabled")
    ObservabilityConfigurationArn = field("ObservabilityConfigurationArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ServiceObservabilityConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceObservabilityConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VpcConnector:
    boto3_raw_data: "type_defs.VpcConnectorTypeDef" = dataclasses.field()

    VpcConnectorName = field("VpcConnectorName")
    VpcConnectorArn = field("VpcConnectorArn")
    VpcConnectorRevision = field("VpcConnectorRevision")
    Subnets = field("Subnets")
    SecurityGroups = field("SecurityGroups")
    Status = field("Status")
    CreatedAt = field("CreatedAt")
    DeletedAt = field("DeletedAt")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VpcConnectorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VpcConnectorTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IngressVpcConfiguration:
    boto3_raw_data: "type_defs.IngressVpcConfigurationTypeDef" = dataclasses.field()

    VpcId = field("VpcId")
    VpcEndpointId = field("VpcEndpointId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IngressVpcConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IngressVpcConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAutoScalingConfigurationRequest:
    boto3_raw_data: "type_defs.DeleteAutoScalingConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    AutoScalingConfigurationArn = field("AutoScalingConfigurationArn")
    DeleteAllRevisions = field("DeleteAllRevisions")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteAutoScalingConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAutoScalingConfigurationRequestTypeDef"]
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

    ConnectionArn = field("ConnectionArn")

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
class DeleteObservabilityConfigurationRequest:
    boto3_raw_data: "type_defs.DeleteObservabilityConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    ObservabilityConfigurationArn = field("ObservabilityConfigurationArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteObservabilityConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteObservabilityConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteServiceRequest:
    boto3_raw_data: "type_defs.DeleteServiceRequestTypeDef" = dataclasses.field()

    ServiceArn = field("ServiceArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteServiceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteServiceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteVpcConnectorRequest:
    boto3_raw_data: "type_defs.DeleteVpcConnectorRequestTypeDef" = dataclasses.field()

    VpcConnectorArn = field("VpcConnectorArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteVpcConnectorRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteVpcConnectorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteVpcIngressConnectionRequest:
    boto3_raw_data: "type_defs.DeleteVpcIngressConnectionRequestTypeDef" = (
        dataclasses.field()
    )

    VpcIngressConnectionArn = field("VpcIngressConnectionArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteVpcIngressConnectionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteVpcIngressConnectionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAutoScalingConfigurationRequest:
    boto3_raw_data: "type_defs.DescribeAutoScalingConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    AutoScalingConfigurationArn = field("AutoScalingConfigurationArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAutoScalingConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAutoScalingConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCustomDomainsRequest:
    boto3_raw_data: "type_defs.DescribeCustomDomainsRequestTypeDef" = (
        dataclasses.field()
    )

    ServiceArn = field("ServiceArn")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeCustomDomainsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCustomDomainsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeObservabilityConfigurationRequest:
    boto3_raw_data: "type_defs.DescribeObservabilityConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    ObservabilityConfigurationArn = field("ObservabilityConfigurationArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeObservabilityConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeObservabilityConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeServiceRequest:
    boto3_raw_data: "type_defs.DescribeServiceRequestTypeDef" = dataclasses.field()

    ServiceArn = field("ServiceArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeServiceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeServiceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeVpcConnectorRequest:
    boto3_raw_data: "type_defs.DescribeVpcConnectorRequestTypeDef" = dataclasses.field()

    VpcConnectorArn = field("VpcConnectorArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeVpcConnectorRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeVpcConnectorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeVpcIngressConnectionRequest:
    boto3_raw_data: "type_defs.DescribeVpcIngressConnectionRequestTypeDef" = (
        dataclasses.field()
    )

    VpcIngressConnectionArn = field("VpcIngressConnectionArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeVpcIngressConnectionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeVpcIngressConnectionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateCustomDomainRequest:
    boto3_raw_data: "type_defs.DisassociateCustomDomainRequestTypeDef" = (
        dataclasses.field()
    )

    ServiceArn = field("ServiceArn")
    DomainName = field("DomainName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DisassociateCustomDomainRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateCustomDomainRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EgressConfiguration:
    boto3_raw_data: "type_defs.EgressConfigurationTypeDef" = dataclasses.field()

    EgressType = field("EgressType")
    VpcConnectorArn = field("VpcConnectorArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EgressConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EgressConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImageConfigurationOutput:
    boto3_raw_data: "type_defs.ImageConfigurationOutputTypeDef" = dataclasses.field()

    RuntimeEnvironmentVariables = field("RuntimeEnvironmentVariables")
    StartCommand = field("StartCommand")
    Port = field("Port")
    RuntimeEnvironmentSecrets = field("RuntimeEnvironmentSecrets")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImageConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImageConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImageConfiguration:
    boto3_raw_data: "type_defs.ImageConfigurationTypeDef" = dataclasses.field()

    RuntimeEnvironmentVariables = field("RuntimeEnvironmentVariables")
    StartCommand = field("StartCommand")
    Port = field("Port")
    RuntimeEnvironmentSecrets = field("RuntimeEnvironmentSecrets")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImageConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImageConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IngressConfiguration:
    boto3_raw_data: "type_defs.IngressConfigurationTypeDef" = dataclasses.field()

    IsPubliclyAccessible = field("IsPubliclyAccessible")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IngressConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IngressConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAutoScalingConfigurationsRequest:
    boto3_raw_data: "type_defs.ListAutoScalingConfigurationsRequestTypeDef" = (
        dataclasses.field()
    )

    AutoScalingConfigurationName = field("AutoScalingConfigurationName")
    LatestOnly = field("LatestOnly")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAutoScalingConfigurationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAutoScalingConfigurationsRequestTypeDef"]
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

    ConnectionName = field("ConnectionName")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

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
class ListObservabilityConfigurationsRequest:
    boto3_raw_data: "type_defs.ListObservabilityConfigurationsRequestTypeDef" = (
        dataclasses.field()
    )

    ObservabilityConfigurationName = field("ObservabilityConfigurationName")
    LatestOnly = field("LatestOnly")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListObservabilityConfigurationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListObservabilityConfigurationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ObservabilityConfigurationSummary:
    boto3_raw_data: "type_defs.ObservabilityConfigurationSummaryTypeDef" = (
        dataclasses.field()
    )

    ObservabilityConfigurationArn = field("ObservabilityConfigurationArn")
    ObservabilityConfigurationName = field("ObservabilityConfigurationName")
    ObservabilityConfigurationRevision = field("ObservabilityConfigurationRevision")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ObservabilityConfigurationSummaryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ObservabilityConfigurationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOperationsRequest:
    boto3_raw_data: "type_defs.ListOperationsRequestTypeDef" = dataclasses.field()

    ServiceArn = field("ServiceArn")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListOperationsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOperationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OperationSummary:
    boto3_raw_data: "type_defs.OperationSummaryTypeDef" = dataclasses.field()

    Id = field("Id")
    Type = field("Type")
    Status = field("Status")
    TargetArn = field("TargetArn")
    StartedAt = field("StartedAt")
    EndedAt = field("EndedAt")
    UpdatedAt = field("UpdatedAt")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OperationSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OperationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServicesForAutoScalingConfigurationRequest:
    boto3_raw_data: (
        "type_defs.ListServicesForAutoScalingConfigurationRequestTypeDef"
    ) = dataclasses.field()

    AutoScalingConfigurationArn = field("AutoScalingConfigurationArn")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListServicesForAutoScalingConfigurationRequestTypeDef"
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
                "type_defs.ListServicesForAutoScalingConfigurationRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServicesRequest:
    boto3_raw_data: "type_defs.ListServicesRequestTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListServicesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServicesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceSummary:
    boto3_raw_data: "type_defs.ServiceSummaryTypeDef" = dataclasses.field()

    ServiceName = field("ServiceName")
    ServiceId = field("ServiceId")
    ServiceArn = field("ServiceArn")
    ServiceUrl = field("ServiceUrl")
    CreatedAt = field("CreatedAt")
    UpdatedAt = field("UpdatedAt")
    Status = field("Status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ServiceSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ServiceSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceRequest:
    boto3_raw_data: "type_defs.ListTagsForResourceRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")

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
class ListVpcConnectorsRequest:
    boto3_raw_data: "type_defs.ListVpcConnectorsRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListVpcConnectorsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVpcConnectorsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVpcIngressConnectionsFilter:
    boto3_raw_data: "type_defs.ListVpcIngressConnectionsFilterTypeDef" = (
        dataclasses.field()
    )

    ServiceArn = field("ServiceArn")
    VpcEndpointId = field("VpcEndpointId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListVpcIngressConnectionsFilterTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVpcIngressConnectionsFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VpcIngressConnectionSummary:
    boto3_raw_data: "type_defs.VpcIngressConnectionSummaryTypeDef" = dataclasses.field()

    VpcIngressConnectionArn = field("VpcIngressConnectionArn")
    ServiceArn = field("ServiceArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VpcIngressConnectionSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VpcIngressConnectionSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PauseServiceRequest:
    boto3_raw_data: "type_defs.PauseServiceRequestTypeDef" = dataclasses.field()

    ServiceArn = field("ServiceArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PauseServiceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PauseServiceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResumeServiceRequest:
    boto3_raw_data: "type_defs.ResumeServiceRequestTypeDef" = dataclasses.field()

    ServiceArn = field("ServiceArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResumeServiceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResumeServiceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartDeploymentRequest:
    boto3_raw_data: "type_defs.StartDeploymentRequestTypeDef" = dataclasses.field()

    ServiceArn = field("ServiceArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartDeploymentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartDeploymentRequestTypeDef"]
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

    ResourceArn = field("ResourceArn")
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
class UpdateDefaultAutoScalingConfigurationRequest:
    boto3_raw_data: "type_defs.UpdateDefaultAutoScalingConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    AutoScalingConfigurationArn = field("AutoScalingConfigurationArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateDefaultAutoScalingConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDefaultAutoScalingConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServicesForAutoScalingConfigurationResponse:
    boto3_raw_data: (
        "type_defs.ListServicesForAutoScalingConfigurationResponseTypeDef"
    ) = dataclasses.field()

    ServiceArnList = field("ServiceArnList")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListServicesForAutoScalingConfigurationResponseTypeDef"
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
                "type_defs.ListServicesForAutoScalingConfigurationResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartDeploymentResponse:
    boto3_raw_data: "type_defs.StartDeploymentResponseTypeDef" = dataclasses.field()

    OperationId = field("OperationId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartDeploymentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartDeploymentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAutoScalingConfigurationsResponse:
    boto3_raw_data: "type_defs.ListAutoScalingConfigurationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AutoScalingConfigurationSummaryList(self):  # pragma: no cover
        return AutoScalingConfigurationSummary.make_many(
            self.boto3_raw_data["AutoScalingConfigurationSummaryList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAutoScalingConfigurationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAutoScalingConfigurationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAutoScalingConfigurationResponse:
    boto3_raw_data: "type_defs.CreateAutoScalingConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AutoScalingConfiguration(self):  # pragma: no cover
        return AutoScalingConfiguration.make_one(
            self.boto3_raw_data["AutoScalingConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateAutoScalingConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAutoScalingConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAutoScalingConfigurationResponse:
    boto3_raw_data: "type_defs.DeleteAutoScalingConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AutoScalingConfiguration(self):  # pragma: no cover
        return AutoScalingConfiguration.make_one(
            self.boto3_raw_data["AutoScalingConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteAutoScalingConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAutoScalingConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAutoScalingConfigurationResponse:
    boto3_raw_data: "type_defs.DescribeAutoScalingConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AutoScalingConfiguration(self):  # pragma: no cover
        return AutoScalingConfiguration.make_one(
            self.boto3_raw_data["AutoScalingConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAutoScalingConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAutoScalingConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDefaultAutoScalingConfigurationResponse:
    boto3_raw_data: "type_defs.UpdateDefaultAutoScalingConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AutoScalingConfiguration(self):  # pragma: no cover
        return AutoScalingConfiguration.make_one(
            self.boto3_raw_data["AutoScalingConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateDefaultAutoScalingConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDefaultAutoScalingConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomDomain:
    boto3_raw_data: "type_defs.CustomDomainTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    EnableWWWSubdomain = field("EnableWWWSubdomain")
    Status = field("Status")

    @cached_property
    def CertificateValidationRecords(self):  # pragma: no cover
        return CertificateValidationRecord.make_many(
            self.boto3_raw_data["CertificateValidationRecords"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CustomDomainTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CustomDomainTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CodeConfigurationOutput:
    boto3_raw_data: "type_defs.CodeConfigurationOutputTypeDef" = dataclasses.field()

    ConfigurationSource = field("ConfigurationSource")

    @cached_property
    def CodeConfigurationValues(self):  # pragma: no cover
        return CodeConfigurationValuesOutput.make_one(
            self.boto3_raw_data["CodeConfigurationValues"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CodeConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CodeConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CodeConfiguration:
    boto3_raw_data: "type_defs.CodeConfigurationTypeDef" = dataclasses.field()

    ConfigurationSource = field("ConfigurationSource")

    @cached_property
    def CodeConfigurationValues(self):  # pragma: no cover
        return CodeConfigurationValues.make_one(
            self.boto3_raw_data["CodeConfigurationValues"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CodeConfigurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CodeConfigurationTypeDef"]
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
    def ConnectionSummaryList(self):  # pragma: no cover
        return ConnectionSummary.make_many(self.boto3_raw_data["ConnectionSummaryList"])

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
class CreateConnectionResponse:
    boto3_raw_data: "type_defs.CreateConnectionResponseTypeDef" = dataclasses.field()

    @cached_property
    def Connection(self):  # pragma: no cover
        return Connection.make_one(self.boto3_raw_data["Connection"])

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
class DeleteConnectionResponse:
    boto3_raw_data: "type_defs.DeleteConnectionResponseTypeDef" = dataclasses.field()

    @cached_property
    def Connection(self):  # pragma: no cover
        return Connection.make_one(self.boto3_raw_data["Connection"])

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
class CreateAutoScalingConfigurationRequest:
    boto3_raw_data: "type_defs.CreateAutoScalingConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    AutoScalingConfigurationName = field("AutoScalingConfigurationName")
    MaxConcurrency = field("MaxConcurrency")
    MinSize = field("MinSize")
    MaxSize = field("MaxSize")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateAutoScalingConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAutoScalingConfigurationRequestTypeDef"]
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

    ConnectionName = field("ConnectionName")
    ProviderType = field("ProviderType")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

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
class CreateVpcConnectorRequest:
    boto3_raw_data: "type_defs.CreateVpcConnectorRequestTypeDef" = dataclasses.field()

    VpcConnectorName = field("VpcConnectorName")
    Subnets = field("Subnets")
    SecurityGroups = field("SecurityGroups")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateVpcConnectorRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateVpcConnectorRequestTypeDef"]
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
class TagResourceRequest:
    boto3_raw_data: "type_defs.TagResourceRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")

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
class CreateObservabilityConfigurationRequest:
    boto3_raw_data: "type_defs.CreateObservabilityConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    ObservabilityConfigurationName = field("ObservabilityConfigurationName")

    @cached_property
    def TraceConfiguration(self):  # pragma: no cover
        return TraceConfiguration.make_one(self.boto3_raw_data["TraceConfiguration"])

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateObservabilityConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateObservabilityConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ObservabilityConfiguration:
    boto3_raw_data: "type_defs.ObservabilityConfigurationTypeDef" = dataclasses.field()

    ObservabilityConfigurationArn = field("ObservabilityConfigurationArn")
    ObservabilityConfigurationName = field("ObservabilityConfigurationName")

    @cached_property
    def TraceConfiguration(self):  # pragma: no cover
        return TraceConfiguration.make_one(self.boto3_raw_data["TraceConfiguration"])

    ObservabilityConfigurationRevision = field("ObservabilityConfigurationRevision")
    Latest = field("Latest")
    Status = field("Status")
    CreatedAt = field("CreatedAt")
    DeletedAt = field("DeletedAt")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ObservabilityConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ObservabilityConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateVpcConnectorResponse:
    boto3_raw_data: "type_defs.CreateVpcConnectorResponseTypeDef" = dataclasses.field()

    @cached_property
    def VpcConnector(self):  # pragma: no cover
        return VpcConnector.make_one(self.boto3_raw_data["VpcConnector"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateVpcConnectorResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateVpcConnectorResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteVpcConnectorResponse:
    boto3_raw_data: "type_defs.DeleteVpcConnectorResponseTypeDef" = dataclasses.field()

    @cached_property
    def VpcConnector(self):  # pragma: no cover
        return VpcConnector.make_one(self.boto3_raw_data["VpcConnector"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteVpcConnectorResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteVpcConnectorResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeVpcConnectorResponse:
    boto3_raw_data: "type_defs.DescribeVpcConnectorResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def VpcConnector(self):  # pragma: no cover
        return VpcConnector.make_one(self.boto3_raw_data["VpcConnector"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeVpcConnectorResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeVpcConnectorResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVpcConnectorsResponse:
    boto3_raw_data: "type_defs.ListVpcConnectorsResponseTypeDef" = dataclasses.field()

    @cached_property
    def VpcConnectors(self):  # pragma: no cover
        return VpcConnector.make_many(self.boto3_raw_data["VpcConnectors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListVpcConnectorsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVpcConnectorsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateVpcIngressConnectionRequest:
    boto3_raw_data: "type_defs.CreateVpcIngressConnectionRequestTypeDef" = (
        dataclasses.field()
    )

    ServiceArn = field("ServiceArn")
    VpcIngressConnectionName = field("VpcIngressConnectionName")

    @cached_property
    def IngressVpcConfiguration(self):  # pragma: no cover
        return IngressVpcConfiguration.make_one(
            self.boto3_raw_data["IngressVpcConfiguration"]
        )

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateVpcIngressConnectionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateVpcIngressConnectionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateVpcIngressConnectionRequest:
    boto3_raw_data: "type_defs.UpdateVpcIngressConnectionRequestTypeDef" = (
        dataclasses.field()
    )

    VpcIngressConnectionArn = field("VpcIngressConnectionArn")

    @cached_property
    def IngressVpcConfiguration(self):  # pragma: no cover
        return IngressVpcConfiguration.make_one(
            self.boto3_raw_data["IngressVpcConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateVpcIngressConnectionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateVpcIngressConnectionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VpcIngressConnection:
    boto3_raw_data: "type_defs.VpcIngressConnectionTypeDef" = dataclasses.field()

    VpcIngressConnectionArn = field("VpcIngressConnectionArn")
    VpcIngressConnectionName = field("VpcIngressConnectionName")
    ServiceArn = field("ServiceArn")
    Status = field("Status")
    AccountId = field("AccountId")
    DomainName = field("DomainName")

    @cached_property
    def IngressVpcConfiguration(self):  # pragma: no cover
        return IngressVpcConfiguration.make_one(
            self.boto3_raw_data["IngressVpcConfiguration"]
        )

    CreatedAt = field("CreatedAt")
    DeletedAt = field("DeletedAt")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VpcIngressConnectionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VpcIngressConnectionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImageRepositoryOutput:
    boto3_raw_data: "type_defs.ImageRepositoryOutputTypeDef" = dataclasses.field()

    ImageIdentifier = field("ImageIdentifier")
    ImageRepositoryType = field("ImageRepositoryType")

    @cached_property
    def ImageConfiguration(self):  # pragma: no cover
        return ImageConfigurationOutput.make_one(
            self.boto3_raw_data["ImageConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImageRepositoryOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImageRepositoryOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImageRepository:
    boto3_raw_data: "type_defs.ImageRepositoryTypeDef" = dataclasses.field()

    ImageIdentifier = field("ImageIdentifier")
    ImageRepositoryType = field("ImageRepositoryType")

    @cached_property
    def ImageConfiguration(self):  # pragma: no cover
        return ImageConfiguration.make_one(self.boto3_raw_data["ImageConfiguration"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImageRepositoryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ImageRepositoryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NetworkConfiguration:
    boto3_raw_data: "type_defs.NetworkConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def EgressConfiguration(self):  # pragma: no cover
        return EgressConfiguration.make_one(self.boto3_raw_data["EgressConfiguration"])

    @cached_property
    def IngressConfiguration(self):  # pragma: no cover
        return IngressConfiguration.make_one(
            self.boto3_raw_data["IngressConfiguration"]
        )

    IpAddressType = field("IpAddressType")

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
class ListObservabilityConfigurationsResponse:
    boto3_raw_data: "type_defs.ListObservabilityConfigurationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ObservabilityConfigurationSummaryList(self):  # pragma: no cover
        return ObservabilityConfigurationSummary.make_many(
            self.boto3_raw_data["ObservabilityConfigurationSummaryList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListObservabilityConfigurationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListObservabilityConfigurationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOperationsResponse:
    boto3_raw_data: "type_defs.ListOperationsResponseTypeDef" = dataclasses.field()

    @cached_property
    def OperationSummaryList(self):  # pragma: no cover
        return OperationSummary.make_many(self.boto3_raw_data["OperationSummaryList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListOperationsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOperationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServicesResponse:
    boto3_raw_data: "type_defs.ListServicesResponseTypeDef" = dataclasses.field()

    @cached_property
    def ServiceSummaryList(self):  # pragma: no cover
        return ServiceSummary.make_many(self.boto3_raw_data["ServiceSummaryList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListServicesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServicesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVpcIngressConnectionsRequest:
    boto3_raw_data: "type_defs.ListVpcIngressConnectionsRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filter(self):  # pragma: no cover
        return ListVpcIngressConnectionsFilter.make_one(self.boto3_raw_data["Filter"])

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListVpcIngressConnectionsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVpcIngressConnectionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVpcIngressConnectionsResponse:
    boto3_raw_data: "type_defs.ListVpcIngressConnectionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def VpcIngressConnectionSummaryList(self):  # pragma: no cover
        return VpcIngressConnectionSummary.make_many(
            self.boto3_raw_data["VpcIngressConnectionSummaryList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListVpcIngressConnectionsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVpcIngressConnectionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateCustomDomainResponse:
    boto3_raw_data: "type_defs.AssociateCustomDomainResponseTypeDef" = (
        dataclasses.field()
    )

    DNSTarget = field("DNSTarget")
    ServiceArn = field("ServiceArn")

    @cached_property
    def CustomDomain(self):  # pragma: no cover
        return CustomDomain.make_one(self.boto3_raw_data["CustomDomain"])

    @cached_property
    def VpcDNSTargets(self):  # pragma: no cover
        return VpcDNSTarget.make_many(self.boto3_raw_data["VpcDNSTargets"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AssociateCustomDomainResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateCustomDomainResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCustomDomainsResponse:
    boto3_raw_data: "type_defs.DescribeCustomDomainsResponseTypeDef" = (
        dataclasses.field()
    )

    DNSTarget = field("DNSTarget")
    ServiceArn = field("ServiceArn")

    @cached_property
    def CustomDomains(self):  # pragma: no cover
        return CustomDomain.make_many(self.boto3_raw_data["CustomDomains"])

    @cached_property
    def VpcDNSTargets(self):  # pragma: no cover
        return VpcDNSTarget.make_many(self.boto3_raw_data["VpcDNSTargets"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeCustomDomainsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCustomDomainsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateCustomDomainResponse:
    boto3_raw_data: "type_defs.DisassociateCustomDomainResponseTypeDef" = (
        dataclasses.field()
    )

    DNSTarget = field("DNSTarget")
    ServiceArn = field("ServiceArn")

    @cached_property
    def CustomDomain(self):  # pragma: no cover
        return CustomDomain.make_one(self.boto3_raw_data["CustomDomain"])

    @cached_property
    def VpcDNSTargets(self):  # pragma: no cover
        return VpcDNSTarget.make_many(self.boto3_raw_data["VpcDNSTargets"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DisassociateCustomDomainResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateCustomDomainResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CodeRepositoryOutput:
    boto3_raw_data: "type_defs.CodeRepositoryOutputTypeDef" = dataclasses.field()

    RepositoryUrl = field("RepositoryUrl")

    @cached_property
    def SourceCodeVersion(self):  # pragma: no cover
        return SourceCodeVersion.make_one(self.boto3_raw_data["SourceCodeVersion"])

    @cached_property
    def CodeConfiguration(self):  # pragma: no cover
        return CodeConfigurationOutput.make_one(
            self.boto3_raw_data["CodeConfiguration"]
        )

    SourceDirectory = field("SourceDirectory")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CodeRepositoryOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CodeRepositoryOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CodeRepository:
    boto3_raw_data: "type_defs.CodeRepositoryTypeDef" = dataclasses.field()

    RepositoryUrl = field("RepositoryUrl")

    @cached_property
    def SourceCodeVersion(self):  # pragma: no cover
        return SourceCodeVersion.make_one(self.boto3_raw_data["SourceCodeVersion"])

    @cached_property
    def CodeConfiguration(self):  # pragma: no cover
        return CodeConfiguration.make_one(self.boto3_raw_data["CodeConfiguration"])

    SourceDirectory = field("SourceDirectory")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CodeRepositoryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CodeRepositoryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateObservabilityConfigurationResponse:
    boto3_raw_data: "type_defs.CreateObservabilityConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ObservabilityConfiguration(self):  # pragma: no cover
        return ObservabilityConfiguration.make_one(
            self.boto3_raw_data["ObservabilityConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateObservabilityConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateObservabilityConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteObservabilityConfigurationResponse:
    boto3_raw_data: "type_defs.DeleteObservabilityConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ObservabilityConfiguration(self):  # pragma: no cover
        return ObservabilityConfiguration.make_one(
            self.boto3_raw_data["ObservabilityConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteObservabilityConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteObservabilityConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeObservabilityConfigurationResponse:
    boto3_raw_data: "type_defs.DescribeObservabilityConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ObservabilityConfiguration(self):  # pragma: no cover
        return ObservabilityConfiguration.make_one(
            self.boto3_raw_data["ObservabilityConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeObservabilityConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeObservabilityConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateVpcIngressConnectionResponse:
    boto3_raw_data: "type_defs.CreateVpcIngressConnectionResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def VpcIngressConnection(self):  # pragma: no cover
        return VpcIngressConnection.make_one(
            self.boto3_raw_data["VpcIngressConnection"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateVpcIngressConnectionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateVpcIngressConnectionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteVpcIngressConnectionResponse:
    boto3_raw_data: "type_defs.DeleteVpcIngressConnectionResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def VpcIngressConnection(self):  # pragma: no cover
        return VpcIngressConnection.make_one(
            self.boto3_raw_data["VpcIngressConnection"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteVpcIngressConnectionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteVpcIngressConnectionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeVpcIngressConnectionResponse:
    boto3_raw_data: "type_defs.DescribeVpcIngressConnectionResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def VpcIngressConnection(self):  # pragma: no cover
        return VpcIngressConnection.make_one(
            self.boto3_raw_data["VpcIngressConnection"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeVpcIngressConnectionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeVpcIngressConnectionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateVpcIngressConnectionResponse:
    boto3_raw_data: "type_defs.UpdateVpcIngressConnectionResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def VpcIngressConnection(self):  # pragma: no cover
        return VpcIngressConnection.make_one(
            self.boto3_raw_data["VpcIngressConnection"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateVpcIngressConnectionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateVpcIngressConnectionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SourceConfigurationOutput:
    boto3_raw_data: "type_defs.SourceConfigurationOutputTypeDef" = dataclasses.field()

    @cached_property
    def CodeRepository(self):  # pragma: no cover
        return CodeRepositoryOutput.make_one(self.boto3_raw_data["CodeRepository"])

    @cached_property
    def ImageRepository(self):  # pragma: no cover
        return ImageRepositoryOutput.make_one(self.boto3_raw_data["ImageRepository"])

    AutoDeploymentsEnabled = field("AutoDeploymentsEnabled")

    @cached_property
    def AuthenticationConfiguration(self):  # pragma: no cover
        return AuthenticationConfiguration.make_one(
            self.boto3_raw_data["AuthenticationConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SourceConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SourceConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SourceConfiguration:
    boto3_raw_data: "type_defs.SourceConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def CodeRepository(self):  # pragma: no cover
        return CodeRepository.make_one(self.boto3_raw_data["CodeRepository"])

    @cached_property
    def ImageRepository(self):  # pragma: no cover
        return ImageRepository.make_one(self.boto3_raw_data["ImageRepository"])

    AutoDeploymentsEnabled = field("AutoDeploymentsEnabled")

    @cached_property
    def AuthenticationConfiguration(self):  # pragma: no cover
        return AuthenticationConfiguration.make_one(
            self.boto3_raw_data["AuthenticationConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SourceConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SourceConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Service:
    boto3_raw_data: "type_defs.ServiceTypeDef" = dataclasses.field()

    ServiceName = field("ServiceName")
    ServiceId = field("ServiceId")
    ServiceArn = field("ServiceArn")
    CreatedAt = field("CreatedAt")
    UpdatedAt = field("UpdatedAt")
    Status = field("Status")

    @cached_property
    def SourceConfiguration(self):  # pragma: no cover
        return SourceConfigurationOutput.make_one(
            self.boto3_raw_data["SourceConfiguration"]
        )

    @cached_property
    def InstanceConfiguration(self):  # pragma: no cover
        return InstanceConfiguration.make_one(
            self.boto3_raw_data["InstanceConfiguration"]
        )

    @cached_property
    def AutoScalingConfigurationSummary(self):  # pragma: no cover
        return AutoScalingConfigurationSummary.make_one(
            self.boto3_raw_data["AutoScalingConfigurationSummary"]
        )

    @cached_property
    def NetworkConfiguration(self):  # pragma: no cover
        return NetworkConfiguration.make_one(
            self.boto3_raw_data["NetworkConfiguration"]
        )

    ServiceUrl = field("ServiceUrl")
    DeletedAt = field("DeletedAt")

    @cached_property
    def EncryptionConfiguration(self):  # pragma: no cover
        return EncryptionConfiguration.make_one(
            self.boto3_raw_data["EncryptionConfiguration"]
        )

    @cached_property
    def HealthCheckConfiguration(self):  # pragma: no cover
        return HealthCheckConfiguration.make_one(
            self.boto3_raw_data["HealthCheckConfiguration"]
        )

    @cached_property
    def ObservabilityConfiguration(self):  # pragma: no cover
        return ServiceObservabilityConfiguration.make_one(
            self.boto3_raw_data["ObservabilityConfiguration"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ServiceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ServiceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateServiceResponse:
    boto3_raw_data: "type_defs.CreateServiceResponseTypeDef" = dataclasses.field()

    @cached_property
    def Service(self):  # pragma: no cover
        return Service.make_one(self.boto3_raw_data["Service"])

    OperationId = field("OperationId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateServiceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateServiceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteServiceResponse:
    boto3_raw_data: "type_defs.DeleteServiceResponseTypeDef" = dataclasses.field()

    @cached_property
    def Service(self):  # pragma: no cover
        return Service.make_one(self.boto3_raw_data["Service"])

    OperationId = field("OperationId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteServiceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteServiceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeServiceResponse:
    boto3_raw_data: "type_defs.DescribeServiceResponseTypeDef" = dataclasses.field()

    @cached_property
    def Service(self):  # pragma: no cover
        return Service.make_one(self.boto3_raw_data["Service"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeServiceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeServiceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PauseServiceResponse:
    boto3_raw_data: "type_defs.PauseServiceResponseTypeDef" = dataclasses.field()

    @cached_property
    def Service(self):  # pragma: no cover
        return Service.make_one(self.boto3_raw_data["Service"])

    OperationId = field("OperationId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PauseServiceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PauseServiceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResumeServiceResponse:
    boto3_raw_data: "type_defs.ResumeServiceResponseTypeDef" = dataclasses.field()

    @cached_property
    def Service(self):  # pragma: no cover
        return Service.make_one(self.boto3_raw_data["Service"])

    OperationId = field("OperationId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResumeServiceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResumeServiceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateServiceResponse:
    boto3_raw_data: "type_defs.UpdateServiceResponseTypeDef" = dataclasses.field()

    @cached_property
    def Service(self):  # pragma: no cover
        return Service.make_one(self.boto3_raw_data["Service"])

    OperationId = field("OperationId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateServiceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateServiceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateServiceRequest:
    boto3_raw_data: "type_defs.CreateServiceRequestTypeDef" = dataclasses.field()

    ServiceName = field("ServiceName")
    SourceConfiguration = field("SourceConfiguration")

    @cached_property
    def InstanceConfiguration(self):  # pragma: no cover
        return InstanceConfiguration.make_one(
            self.boto3_raw_data["InstanceConfiguration"]
        )

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def EncryptionConfiguration(self):  # pragma: no cover
        return EncryptionConfiguration.make_one(
            self.boto3_raw_data["EncryptionConfiguration"]
        )

    @cached_property
    def HealthCheckConfiguration(self):  # pragma: no cover
        return HealthCheckConfiguration.make_one(
            self.boto3_raw_data["HealthCheckConfiguration"]
        )

    AutoScalingConfigurationArn = field("AutoScalingConfigurationArn")

    @cached_property
    def NetworkConfiguration(self):  # pragma: no cover
        return NetworkConfiguration.make_one(
            self.boto3_raw_data["NetworkConfiguration"]
        )

    @cached_property
    def ObservabilityConfiguration(self):  # pragma: no cover
        return ServiceObservabilityConfiguration.make_one(
            self.boto3_raw_data["ObservabilityConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateServiceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateServiceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateServiceRequest:
    boto3_raw_data: "type_defs.UpdateServiceRequestTypeDef" = dataclasses.field()

    ServiceArn = field("ServiceArn")
    SourceConfiguration = field("SourceConfiguration")

    @cached_property
    def InstanceConfiguration(self):  # pragma: no cover
        return InstanceConfiguration.make_one(
            self.boto3_raw_data["InstanceConfiguration"]
        )

    AutoScalingConfigurationArn = field("AutoScalingConfigurationArn")

    @cached_property
    def HealthCheckConfiguration(self):  # pragma: no cover
        return HealthCheckConfiguration.make_one(
            self.boto3_raw_data["HealthCheckConfiguration"]
        )

    @cached_property
    def NetworkConfiguration(self):  # pragma: no cover
        return NetworkConfiguration.make_one(
            self.boto3_raw_data["NetworkConfiguration"]
        )

    @cached_property
    def ObservabilityConfiguration(self):  # pragma: no cover
        return ServiceObservabilityConfiguration.make_one(
            self.boto3_raw_data["ObservabilityConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateServiceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateServiceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
