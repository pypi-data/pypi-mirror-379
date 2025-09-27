# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_ecs import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AdvancedConfiguration:
    boto3_raw_data: "type_defs.AdvancedConfigurationTypeDef" = dataclasses.field()

    alternateTargetGroupArn = field("alternateTargetGroupArn")
    productionListenerRule = field("productionListenerRule")
    testListenerRule = field("testListenerRule")
    roleArn = field("roleArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AdvancedConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AdvancedConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttachmentStateChange:
    boto3_raw_data: "type_defs.AttachmentStateChangeTypeDef" = dataclasses.field()

    attachmentArn = field("attachmentArn")
    status = field("status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AttachmentStateChangeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttachmentStateChangeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KeyValuePair:
    boto3_raw_data: "type_defs.KeyValuePairTypeDef" = dataclasses.field()

    name = field("name")
    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.KeyValuePairTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.KeyValuePairTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Attribute:
    boto3_raw_data: "type_defs.AttributeTypeDef" = dataclasses.field()

    name = field("name")
    value = field("value")
    targetType = field("targetType")
    targetId = field("targetId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AttributeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AttributeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ManagedScaling:
    boto3_raw_data: "type_defs.ManagedScalingTypeDef" = dataclasses.field()

    status = field("status")
    targetCapacity = field("targetCapacity")
    minimumScalingStepSize = field("minimumScalingStepSize")
    maximumScalingStepSize = field("maximumScalingStepSize")
    instanceWarmupPeriod = field("instanceWarmupPeriod")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ManagedScalingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ManagedScalingTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AwsVpcConfigurationOutput:
    boto3_raw_data: "type_defs.AwsVpcConfigurationOutputTypeDef" = dataclasses.field()

    subnets = field("subnets")
    securityGroups = field("securityGroups")
    assignPublicIp = field("assignPublicIp")

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

    subnets = field("subnets")
    securityGroups = field("securityGroups")
    assignPublicIp = field("assignPublicIp")

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
class ManagedStorageConfiguration:
    boto3_raw_data: "type_defs.ManagedStorageConfigurationTypeDef" = dataclasses.field()

    kmsKeyId = field("kmsKeyId")
    fargateEphemeralStorageKmsKeyId = field("fargateEphemeralStorageKmsKeyId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ManagedStorageConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ManagedStorageConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClusterServiceConnectDefaultsRequest:
    boto3_raw_data: "type_defs.ClusterServiceConnectDefaultsRequestTypeDef" = (
        dataclasses.field()
    )

    namespace = field("namespace")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ClusterServiceConnectDefaultsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClusterServiceConnectDefaultsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClusterServiceConnectDefaults:
    boto3_raw_data: "type_defs.ClusterServiceConnectDefaultsTypeDef" = (
        dataclasses.field()
    )

    namespace = field("namespace")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ClusterServiceConnectDefaultsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClusterServiceConnectDefaultsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClusterSetting:
    boto3_raw_data: "type_defs.ClusterSettingTypeDef" = dataclasses.field()

    name = field("name")
    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ClusterSettingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ClusterSettingTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContainerDependency:
    boto3_raw_data: "type_defs.ContainerDependencyTypeDef" = dataclasses.field()

    containerName = field("containerName")
    condition = field("condition")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContainerDependencyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContainerDependencyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContainerRestartPolicyOutput:
    boto3_raw_data: "type_defs.ContainerRestartPolicyOutputTypeDef" = (
        dataclasses.field()
    )

    enabled = field("enabled")
    ignoredExitCodes = field("ignoredExitCodes")
    restartAttemptPeriod = field("restartAttemptPeriod")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContainerRestartPolicyOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContainerRestartPolicyOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnvironmentFile:
    boto3_raw_data: "type_defs.EnvironmentFileTypeDef" = dataclasses.field()

    value = field("value")
    type = field("type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EnvironmentFileTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EnvironmentFileTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FirelensConfigurationOutput:
    boto3_raw_data: "type_defs.FirelensConfigurationOutputTypeDef" = dataclasses.field()

    type = field("type")
    options = field("options")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FirelensConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FirelensConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HealthCheckOutput:
    boto3_raw_data: "type_defs.HealthCheckOutputTypeDef" = dataclasses.field()

    command = field("command")
    interval = field("interval")
    timeout = field("timeout")
    retries = field("retries")
    startPeriod = field("startPeriod")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HealthCheckOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HealthCheckOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HostEntry:
    boto3_raw_data: "type_defs.HostEntryTypeDef" = dataclasses.field()

    hostname = field("hostname")
    ipAddress = field("ipAddress")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HostEntryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.HostEntryTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MountPoint:
    boto3_raw_data: "type_defs.MountPointTypeDef" = dataclasses.field()

    sourceVolume = field("sourceVolume")
    containerPath = field("containerPath")
    readOnly = field("readOnly")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MountPointTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MountPointTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PortMapping:
    boto3_raw_data: "type_defs.PortMappingTypeDef" = dataclasses.field()

    containerPort = field("containerPort")
    hostPort = field("hostPort")
    protocol = field("protocol")
    name = field("name")
    appProtocol = field("appProtocol")
    containerPortRange = field("containerPortRange")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PortMappingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PortMappingTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RepositoryCredentials:
    boto3_raw_data: "type_defs.RepositoryCredentialsTypeDef" = dataclasses.field()

    credentialsParameter = field("credentialsParameter")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RepositoryCredentialsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RepositoryCredentialsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceRequirement:
    boto3_raw_data: "type_defs.ResourceRequirementTypeDef" = dataclasses.field()

    value = field("value")
    type = field("type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResourceRequirementTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceRequirementTypeDef"]
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

    name = field("name")
    valueFrom = field("valueFrom")

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
class SystemControl:
    boto3_raw_data: "type_defs.SystemControlTypeDef" = dataclasses.field()

    namespace = field("namespace")
    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SystemControlTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SystemControlTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Ulimit:
    boto3_raw_data: "type_defs.UlimitTypeDef" = dataclasses.field()

    name = field("name")
    softLimit = field("softLimit")
    hardLimit = field("hardLimit")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UlimitTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UlimitTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VolumeFrom:
    boto3_raw_data: "type_defs.VolumeFromTypeDef" = dataclasses.field()

    sourceContainer = field("sourceContainer")
    readOnly = field("readOnly")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VolumeFromTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VolumeFromTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContainerImage:
    boto3_raw_data: "type_defs.ContainerImageTypeDef" = dataclasses.field()

    containerName = field("containerName")
    imageDigest = field("imageDigest")
    image = field("image")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ContainerImageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ContainerImageTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceHealthCheckResult:
    boto3_raw_data: "type_defs.InstanceHealthCheckResultTypeDef" = dataclasses.field()

    type = field("type")
    status = field("status")
    lastUpdated = field("lastUpdated")
    lastStatusChange = field("lastStatusChange")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InstanceHealthCheckResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstanceHealthCheckResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceOutput:
    boto3_raw_data: "type_defs.ResourceOutputTypeDef" = dataclasses.field()

    name = field("name")
    type = field("type")
    doubleValue = field("doubleValue")
    longValue = field("longValue")
    integerValue = field("integerValue")
    stringSetValue = field("stringSetValue")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResourceOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResourceOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VersionInfo:
    boto3_raw_data: "type_defs.VersionInfoTypeDef" = dataclasses.field()

    agentVersion = field("agentVersion")
    agentHash = field("agentHash")
    dockerVersion = field("dockerVersion")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VersionInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VersionInfoTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContainerRestartPolicy:
    boto3_raw_data: "type_defs.ContainerRestartPolicyTypeDef" = dataclasses.field()

    enabled = field("enabled")
    ignoredExitCodes = field("ignoredExitCodes")
    restartAttemptPeriod = field("restartAttemptPeriod")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContainerRestartPolicyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContainerRestartPolicyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NetworkBinding:
    boto3_raw_data: "type_defs.NetworkBindingTypeDef" = dataclasses.field()

    bindIP = field("bindIP")
    containerPort = field("containerPort")
    hostPort = field("hostPort")
    protocol = field("protocol")
    containerPortRange = field("containerPortRange")
    hostPortRange = field("hostPortRange")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NetworkBindingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.NetworkBindingTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ManagedAgent:
    boto3_raw_data: "type_defs.ManagedAgentTypeDef" = dataclasses.field()

    lastStartedAt = field("lastStartedAt")
    name = field("name")
    reason = field("reason")
    lastStatus = field("lastStatus")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ManagedAgentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ManagedAgentTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NetworkInterface:
    boto3_raw_data: "type_defs.NetworkInterfaceTypeDef" = dataclasses.field()

    attachmentId = field("attachmentId")
    privateIpv4Address = field("privateIpv4Address")
    ipv6Address = field("ipv6Address")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NetworkInterfaceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NetworkInterfaceTypeDef"]
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
class DeploymentController:
    boto3_raw_data: "type_defs.DeploymentControllerTypeDef" = dataclasses.field()

    type = field("type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeploymentControllerTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeploymentControllerTypeDef"]
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
class ServiceRegistry:
    boto3_raw_data: "type_defs.ServiceRegistryTypeDef" = dataclasses.field()

    registryArn = field("registryArn")
    port = field("port")
    containerName = field("containerName")
    containerPort = field("containerPort")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ServiceRegistryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ServiceRegistryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VpcLatticeConfiguration:
    boto3_raw_data: "type_defs.VpcLatticeConfigurationTypeDef" = dataclasses.field()

    roleArn = field("roleArn")
    targetGroupArn = field("targetGroupArn")
    portName = field("portName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VpcLatticeConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VpcLatticeConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Scale:
    boto3_raw_data: "type_defs.ScaleTypeDef" = dataclasses.field()

    value = field("value")
    unit = field("unit")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ScaleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ScaleTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAccountSettingRequest:
    boto3_raw_data: "type_defs.DeleteAccountSettingRequestTypeDef" = dataclasses.field()

    name = field("name")
    principalArn = field("principalArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAccountSettingRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAccountSettingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Setting:
    boto3_raw_data: "type_defs.SettingTypeDef" = dataclasses.field()

    name = field("name")
    value = field("value")
    principalArn = field("principalArn")
    type = field("type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SettingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SettingTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCapacityProviderRequest:
    boto3_raw_data: "type_defs.DeleteCapacityProviderRequestTypeDef" = (
        dataclasses.field()
    )

    capacityProvider = field("capacityProvider")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteCapacityProviderRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCapacityProviderRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteClusterRequest:
    boto3_raw_data: "type_defs.DeleteClusterRequestTypeDef" = dataclasses.field()

    cluster = field("cluster")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteClusterRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteClusterRequestTypeDef"]
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

    service = field("service")
    cluster = field("cluster")
    force = field("force")

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
class DeleteTaskDefinitionsRequest:
    boto3_raw_data: "type_defs.DeleteTaskDefinitionsRequestTypeDef" = (
        dataclasses.field()
    )

    taskDefinitions = field("taskDefinitions")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteTaskDefinitionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteTaskDefinitionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Failure:
    boto3_raw_data: "type_defs.FailureTypeDef" = dataclasses.field()

    arn = field("arn")
    reason = field("reason")
    detail = field("detail")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FailureTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FailureTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteTaskSetRequest:
    boto3_raw_data: "type_defs.DeleteTaskSetRequestTypeDef" = dataclasses.field()

    cluster = field("cluster")
    service = field("service")
    taskSet = field("taskSet")
    force = field("force")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteTaskSetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteTaskSetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeploymentAlarmsOutput:
    boto3_raw_data: "type_defs.DeploymentAlarmsOutputTypeDef" = dataclasses.field()

    alarmNames = field("alarmNames")
    rollback = field("rollback")
    enable = field("enable")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeploymentAlarmsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeploymentAlarmsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeploymentAlarms:
    boto3_raw_data: "type_defs.DeploymentAlarmsTypeDef" = dataclasses.field()

    alarmNames = field("alarmNames")
    rollback = field("rollback")
    enable = field("enable")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeploymentAlarmsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeploymentAlarmsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeploymentCircuitBreaker:
    boto3_raw_data: "type_defs.DeploymentCircuitBreakerTypeDef" = dataclasses.field()

    enable = field("enable")
    rollback = field("rollback")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeploymentCircuitBreakerTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeploymentCircuitBreakerTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeploymentLifecycleHookOutput:
    boto3_raw_data: "type_defs.DeploymentLifecycleHookOutputTypeDef" = (
        dataclasses.field()
    )

    hookTargetArn = field("hookTargetArn")
    roleArn = field("roleArn")
    lifecycleStages = field("lifecycleStages")
    hookDetails = field("hookDetails")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeploymentLifecycleHookOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeploymentLifecycleHookOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeploymentLifecycleHook:
    boto3_raw_data: "type_defs.DeploymentLifecycleHookTypeDef" = dataclasses.field()

    hookTargetArn = field("hookTargetArn")
    roleArn = field("roleArn")
    lifecycleStages = field("lifecycleStages")
    hookDetails = field("hookDetails")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeploymentLifecycleHookTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeploymentLifecycleHookTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeploymentEphemeralStorage:
    boto3_raw_data: "type_defs.DeploymentEphemeralStorageTypeDef" = dataclasses.field()

    kmsKeyId = field("kmsKeyId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeploymentEphemeralStorageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeploymentEphemeralStorageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceConnectServiceResource:
    boto3_raw_data: "type_defs.ServiceConnectServiceResourceTypeDef" = (
        dataclasses.field()
    )

    discoveryName = field("discoveryName")
    discoveryArn = field("discoveryArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ServiceConnectServiceResourceTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceConnectServiceResourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeregisterContainerInstanceRequest:
    boto3_raw_data: "type_defs.DeregisterContainerInstanceRequestTypeDef" = (
        dataclasses.field()
    )

    containerInstance = field("containerInstance")
    cluster = field("cluster")
    force = field("force")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeregisterContainerInstanceRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeregisterContainerInstanceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeregisterTaskDefinitionRequest:
    boto3_raw_data: "type_defs.DeregisterTaskDefinitionRequestTypeDef" = (
        dataclasses.field()
    )

    taskDefinition = field("taskDefinition")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeregisterTaskDefinitionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeregisterTaskDefinitionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCapacityProvidersRequest:
    boto3_raw_data: "type_defs.DescribeCapacityProvidersRequestTypeDef" = (
        dataclasses.field()
    )

    capacityProviders = field("capacityProviders")
    include = field("include")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeCapacityProvidersRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCapacityProvidersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeClustersRequest:
    boto3_raw_data: "type_defs.DescribeClustersRequestTypeDef" = dataclasses.field()

    clusters = field("clusters")
    include = field("include")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeClustersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeClustersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeContainerInstancesRequest:
    boto3_raw_data: "type_defs.DescribeContainerInstancesRequestTypeDef" = (
        dataclasses.field()
    )

    containerInstances = field("containerInstances")
    cluster = field("cluster")
    include = field("include")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeContainerInstancesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeContainerInstancesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeServiceDeploymentsRequest:
    boto3_raw_data: "type_defs.DescribeServiceDeploymentsRequestTypeDef" = (
        dataclasses.field()
    )

    serviceDeploymentArns = field("serviceDeploymentArns")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeServiceDeploymentsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeServiceDeploymentsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeServiceRevisionsRequest:
    boto3_raw_data: "type_defs.DescribeServiceRevisionsRequestTypeDef" = (
        dataclasses.field()
    )

    serviceRevisionArns = field("serviceRevisionArns")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeServiceRevisionsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeServiceRevisionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeServicesRequest:
    boto3_raw_data: "type_defs.DescribeServicesRequestTypeDef" = dataclasses.field()

    services = field("services")
    cluster = field("cluster")
    include = field("include")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeServicesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeServicesRequestTypeDef"]
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
class DescribeTaskDefinitionRequest:
    boto3_raw_data: "type_defs.DescribeTaskDefinitionRequestTypeDef" = (
        dataclasses.field()
    )

    taskDefinition = field("taskDefinition")
    include = field("include")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeTaskDefinitionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTaskDefinitionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTaskSetsRequest:
    boto3_raw_data: "type_defs.DescribeTaskSetsRequestTypeDef" = dataclasses.field()

    cluster = field("cluster")
    service = field("service")
    taskSets = field("taskSets")
    include = field("include")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeTaskSetsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTaskSetsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTasksRequest:
    boto3_raw_data: "type_defs.DescribeTasksRequestTypeDef" = dataclasses.field()

    tasks = field("tasks")
    cluster = field("cluster")
    include = field("include")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeTasksRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTasksRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeviceOutput:
    boto3_raw_data: "type_defs.DeviceOutputTypeDef" = dataclasses.field()

    hostPath = field("hostPath")
    containerPath = field("containerPath")
    permissions = field("permissions")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeviceOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DeviceOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Device:
    boto3_raw_data: "type_defs.DeviceTypeDef" = dataclasses.field()

    hostPath = field("hostPath")
    containerPath = field("containerPath")
    permissions = field("permissions")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeviceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DeviceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DiscoverPollEndpointRequest:
    boto3_raw_data: "type_defs.DiscoverPollEndpointRequestTypeDef" = dataclasses.field()

    containerInstance = field("containerInstance")
    cluster = field("cluster")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DiscoverPollEndpointRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DiscoverPollEndpointRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DockerVolumeConfigurationOutput:
    boto3_raw_data: "type_defs.DockerVolumeConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    scope = field("scope")
    autoprovision = field("autoprovision")
    driver = field("driver")
    driverOpts = field("driverOpts")
    labels = field("labels")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DockerVolumeConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DockerVolumeConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DockerVolumeConfiguration:
    boto3_raw_data: "type_defs.DockerVolumeConfigurationTypeDef" = dataclasses.field()

    scope = field("scope")
    autoprovision = field("autoprovision")
    driver = field("driver")
    driverOpts = field("driverOpts")
    labels = field("labels")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DockerVolumeConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DockerVolumeConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EFSAuthorizationConfig:
    boto3_raw_data: "type_defs.EFSAuthorizationConfigTypeDef" = dataclasses.field()

    accessPointId = field("accessPointId")
    iam = field("iam")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EFSAuthorizationConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EFSAuthorizationConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EphemeralStorage:
    boto3_raw_data: "type_defs.EphemeralStorageTypeDef" = dataclasses.field()

    sizeInGiB = field("sizeInGiB")

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
class ExecuteCommandLogConfiguration:
    boto3_raw_data: "type_defs.ExecuteCommandLogConfigurationTypeDef" = (
        dataclasses.field()
    )

    cloudWatchLogGroupName = field("cloudWatchLogGroupName")
    cloudWatchEncryptionEnabled = field("cloudWatchEncryptionEnabled")
    s3BucketName = field("s3BucketName")
    s3EncryptionEnabled = field("s3EncryptionEnabled")
    s3KeyPrefix = field("s3KeyPrefix")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ExecuteCommandLogConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExecuteCommandLogConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExecuteCommandRequest:
    boto3_raw_data: "type_defs.ExecuteCommandRequestTypeDef" = dataclasses.field()

    command = field("command")
    interactive = field("interactive")
    task = field("task")
    cluster = field("cluster")
    container = field("container")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExecuteCommandRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExecuteCommandRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Session:
    boto3_raw_data: "type_defs.SessionTypeDef" = dataclasses.field()

    sessionId = field("sessionId")
    streamUrl = field("streamUrl")
    tokenValue = field("tokenValue")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SessionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SessionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FSxWindowsFileServerAuthorizationConfig:
    boto3_raw_data: "type_defs.FSxWindowsFileServerAuthorizationConfigTypeDef" = (
        dataclasses.field()
    )

    credentialsParameter = field("credentialsParameter")
    domain = field("domain")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.FSxWindowsFileServerAuthorizationConfigTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FSxWindowsFileServerAuthorizationConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FirelensConfiguration:
    boto3_raw_data: "type_defs.FirelensConfigurationTypeDef" = dataclasses.field()

    type = field("type")
    options = field("options")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FirelensConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FirelensConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTaskProtectionRequest:
    boto3_raw_data: "type_defs.GetTaskProtectionRequestTypeDef" = dataclasses.field()

    cluster = field("cluster")
    tasks = field("tasks")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTaskProtectionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTaskProtectionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProtectedTask:
    boto3_raw_data: "type_defs.ProtectedTaskTypeDef" = dataclasses.field()

    taskArn = field("taskArn")
    protectionEnabled = field("protectionEnabled")
    expirationDate = field("expirationDate")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ProtectedTaskTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ProtectedTaskTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HealthCheck:
    boto3_raw_data: "type_defs.HealthCheckTypeDef" = dataclasses.field()

    command = field("command")
    interval = field("interval")
    timeout = field("timeout")
    retries = field("retries")
    startPeriod = field("startPeriod")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HealthCheckTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.HealthCheckTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HostVolumeProperties:
    boto3_raw_data: "type_defs.HostVolumePropertiesTypeDef" = dataclasses.field()

    sourcePath = field("sourcePath")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HostVolumePropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HostVolumePropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InferenceAcceleratorOverride:
    boto3_raw_data: "type_defs.InferenceAcceleratorOverrideTypeDef" = (
        dataclasses.field()
    )

    deviceName = field("deviceName")
    deviceType = field("deviceType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InferenceAcceleratorOverrideTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InferenceAcceleratorOverrideTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InferenceAccelerator:
    boto3_raw_data: "type_defs.InferenceAcceleratorTypeDef" = dataclasses.field()

    deviceName = field("deviceName")
    deviceType = field("deviceType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InferenceAcceleratorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InferenceAcceleratorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KernelCapabilitiesOutput:
    boto3_raw_data: "type_defs.KernelCapabilitiesOutputTypeDef" = dataclasses.field()

    add = field("add")
    drop = field("drop")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KernelCapabilitiesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KernelCapabilitiesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KernelCapabilities:
    boto3_raw_data: "type_defs.KernelCapabilitiesTypeDef" = dataclasses.field()

    add = field("add")
    drop = field("drop")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KernelCapabilitiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KernelCapabilitiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TmpfsOutput:
    boto3_raw_data: "type_defs.TmpfsOutputTypeDef" = dataclasses.field()

    containerPath = field("containerPath")
    size = field("size")
    mountOptions = field("mountOptions")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TmpfsOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TmpfsOutputTypeDef"]]
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
class ListAccountSettingsRequest:
    boto3_raw_data: "type_defs.ListAccountSettingsRequestTypeDef" = dataclasses.field()

    name = field("name")
    value = field("value")
    principalArn = field("principalArn")
    effectiveSettings = field("effectiveSettings")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAccountSettingsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAccountSettingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAttributesRequest:
    boto3_raw_data: "type_defs.ListAttributesRequestTypeDef" = dataclasses.field()

    targetType = field("targetType")
    cluster = field("cluster")
    attributeName = field("attributeName")
    attributeValue = field("attributeValue")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAttributesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAttributesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListClustersRequest:
    boto3_raw_data: "type_defs.ListClustersRequestTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListClustersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListClustersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListContainerInstancesRequest:
    boto3_raw_data: "type_defs.ListContainerInstancesRequestTypeDef" = (
        dataclasses.field()
    )

    cluster = field("cluster")
    filter = field("filter")
    nextToken = field("nextToken")
    maxResults = field("maxResults")
    status = field("status")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListContainerInstancesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListContainerInstancesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceDeploymentBrief:
    boto3_raw_data: "type_defs.ServiceDeploymentBriefTypeDef" = dataclasses.field()

    serviceDeploymentArn = field("serviceDeploymentArn")
    serviceArn = field("serviceArn")
    clusterArn = field("clusterArn")
    startedAt = field("startedAt")
    createdAt = field("createdAt")
    finishedAt = field("finishedAt")
    targetServiceRevisionArn = field("targetServiceRevisionArn")
    status = field("status")
    statusReason = field("statusReason")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ServiceDeploymentBriefTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceDeploymentBriefTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServicesByNamespaceRequest:
    boto3_raw_data: "type_defs.ListServicesByNamespaceRequestTypeDef" = (
        dataclasses.field()
    )

    namespace = field("namespace")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListServicesByNamespaceRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServicesByNamespaceRequestTypeDef"]
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

    cluster = field("cluster")
    nextToken = field("nextToken")
    maxResults = field("maxResults")
    launchType = field("launchType")
    schedulingStrategy = field("schedulingStrategy")

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
class ListTaskDefinitionFamiliesRequest:
    boto3_raw_data: "type_defs.ListTaskDefinitionFamiliesRequestTypeDef" = (
        dataclasses.field()
    )

    familyPrefix = field("familyPrefix")
    status = field("status")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListTaskDefinitionFamiliesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTaskDefinitionFamiliesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTaskDefinitionsRequest:
    boto3_raw_data: "type_defs.ListTaskDefinitionsRequestTypeDef" = dataclasses.field()

    familyPrefix = field("familyPrefix")
    status = field("status")
    sort = field("sort")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTaskDefinitionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTaskDefinitionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTasksRequest:
    boto3_raw_data: "type_defs.ListTasksRequestTypeDef" = dataclasses.field()

    cluster = field("cluster")
    containerInstance = field("containerInstance")
    family = field("family")
    nextToken = field("nextToken")
    maxResults = field("maxResults")
    startedBy = field("startedBy")
    serviceName = field("serviceName")
    desiredStatus = field("desiredStatus")
    launchType = field("launchType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListTasksRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTasksRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ManagedAgentStateChange:
    boto3_raw_data: "type_defs.ManagedAgentStateChangeTypeDef" = dataclasses.field()

    containerName = field("containerName")
    managedAgentName = field("managedAgentName")
    status = field("status")
    reason = field("reason")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ManagedAgentStateChangeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ManagedAgentStateChangeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PlatformDevice:
    boto3_raw_data: "type_defs.PlatformDeviceTypeDef" = dataclasses.field()

    id = field("id")
    type = field("type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PlatformDeviceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PlatformDeviceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutAccountSettingDefaultRequest:
    boto3_raw_data: "type_defs.PutAccountSettingDefaultRequestTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    value = field("value")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PutAccountSettingDefaultRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutAccountSettingDefaultRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutAccountSettingRequest:
    boto3_raw_data: "type_defs.PutAccountSettingRequestTypeDef" = dataclasses.field()

    name = field("name")
    value = field("value")
    principalArn = field("principalArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutAccountSettingRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutAccountSettingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuntimePlatform:
    boto3_raw_data: "type_defs.RuntimePlatformTypeDef" = dataclasses.field()

    cpuArchitecture = field("cpuArchitecture")
    operatingSystemFamily = field("operatingSystemFamily")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RuntimePlatformTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RuntimePlatformTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TaskDefinitionPlacementConstraint:
    boto3_raw_data: "type_defs.TaskDefinitionPlacementConstraintTypeDef" = (
        dataclasses.field()
    )

    type = field("type")
    expression = field("expression")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.TaskDefinitionPlacementConstraintTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TaskDefinitionPlacementConstraintTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceRevisionLoadBalancer:
    boto3_raw_data: "type_defs.ServiceRevisionLoadBalancerTypeDef" = dataclasses.field()

    targetGroupArn = field("targetGroupArn")
    productionListenerRule = field("productionListenerRule")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ServiceRevisionLoadBalancerTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceRevisionLoadBalancerTypeDef"]
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

    name = field("name")
    type = field("type")
    doubleValue = field("doubleValue")
    longValue = field("longValue")
    integerValue = field("integerValue")
    stringSetValue = field("stringSetValue")

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
class Rollback:
    boto3_raw_data: "type_defs.RollbackTypeDef" = dataclasses.field()

    reason = field("reason")
    startedAt = field("startedAt")
    serviceRevisionArn = field("serviceRevisionArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RollbackTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RollbackTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TimeoutConfiguration:
    boto3_raw_data: "type_defs.TimeoutConfigurationTypeDef" = dataclasses.field()

    idleTimeoutSeconds = field("idleTimeoutSeconds")
    perRequestTimeoutSeconds = field("perRequestTimeoutSeconds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TimeoutConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TimeoutConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceConnectTestTrafficHeaderMatchRules:
    boto3_raw_data: "type_defs.ServiceConnectTestTrafficHeaderMatchRulesTypeDef" = (
        dataclasses.field()
    )

    exact = field("exact")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ServiceConnectTestTrafficHeaderMatchRulesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceConnectTestTrafficHeaderMatchRulesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceConnectTlsCertificateAuthority:
    boto3_raw_data: "type_defs.ServiceConnectTlsCertificateAuthorityTypeDef" = (
        dataclasses.field()
    )

    awsPcaAuthorityArn = field("awsPcaAuthorityArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ServiceConnectTlsCertificateAuthorityTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceConnectTlsCertificateAuthorityTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceDeploymentAlarms:
    boto3_raw_data: "type_defs.ServiceDeploymentAlarmsTypeDef" = dataclasses.field()

    status = field("status")
    alarmNames = field("alarmNames")
    triggeredAlarmNames = field("triggeredAlarmNames")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ServiceDeploymentAlarmsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceDeploymentAlarmsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceDeploymentCircuitBreaker:
    boto3_raw_data: "type_defs.ServiceDeploymentCircuitBreakerTypeDef" = (
        dataclasses.field()
    )

    status = field("status")
    failureCount = field("failureCount")
    threshold = field("threshold")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ServiceDeploymentCircuitBreakerTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceDeploymentCircuitBreakerTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceRevisionSummary:
    boto3_raw_data: "type_defs.ServiceRevisionSummaryTypeDef" = dataclasses.field()

    arn = field("arn")
    requestedTaskCount = field("requestedTaskCount")
    runningTaskCount = field("runningTaskCount")
    pendingTaskCount = field("pendingTaskCount")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ServiceRevisionSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceRevisionSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceEvent:
    boto3_raw_data: "type_defs.ServiceEventTypeDef" = dataclasses.field()

    id = field("id")
    createdAt = field("createdAt")
    message = field("message")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ServiceEventTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ServiceEventTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopServiceDeploymentRequest:
    boto3_raw_data: "type_defs.StopServiceDeploymentRequestTypeDef" = (
        dataclasses.field()
    )

    serviceDeploymentArn = field("serviceDeploymentArn")
    stopType = field("stopType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopServiceDeploymentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopServiceDeploymentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopTaskRequest:
    boto3_raw_data: "type_defs.StopTaskRequestTypeDef" = dataclasses.field()

    task = field("task")
    cluster = field("cluster")
    reason = field("reason")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StopTaskRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StopTaskRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TaskEphemeralStorage:
    boto3_raw_data: "type_defs.TaskEphemeralStorageTypeDef" = dataclasses.field()

    sizeInGiB = field("sizeInGiB")
    kmsKeyId = field("kmsKeyId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TaskEphemeralStorageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TaskEphemeralStorageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TaskManagedEBSVolumeTerminationPolicy:
    boto3_raw_data: "type_defs.TaskManagedEBSVolumeTerminationPolicyTypeDef" = (
        dataclasses.field()
    )

    deleteOnTermination = field("deleteOnTermination")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.TaskManagedEBSVolumeTerminationPolicyTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TaskManagedEBSVolumeTerminationPolicyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Tmpfs:
    boto3_raw_data: "type_defs.TmpfsTypeDef" = dataclasses.field()

    containerPath = field("containerPath")
    size = field("size")
    mountOptions = field("mountOptions")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TmpfsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TmpfsTypeDef"]]
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
class UpdateContainerAgentRequest:
    boto3_raw_data: "type_defs.UpdateContainerAgentRequestTypeDef" = dataclasses.field()

    containerInstance = field("containerInstance")
    cluster = field("cluster")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateContainerAgentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateContainerAgentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateContainerInstancesStateRequest:
    boto3_raw_data: "type_defs.UpdateContainerInstancesStateRequestTypeDef" = (
        dataclasses.field()
    )

    containerInstances = field("containerInstances")
    status = field("status")
    cluster = field("cluster")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateContainerInstancesStateRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateContainerInstancesStateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateServicePrimaryTaskSetRequest:
    boto3_raw_data: "type_defs.UpdateServicePrimaryTaskSetRequestTypeDef" = (
        dataclasses.field()
    )

    cluster = field("cluster")
    service = field("service")
    primaryTaskSet = field("primaryTaskSet")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateServicePrimaryTaskSetRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateServicePrimaryTaskSetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateTaskProtectionRequest:
    boto3_raw_data: "type_defs.UpdateTaskProtectionRequestTypeDef" = dataclasses.field()

    cluster = field("cluster")
    tasks = field("tasks")
    protectionEnabled = field("protectionEnabled")
    expiresInMinutes = field("expiresInMinutes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateTaskProtectionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTaskProtectionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoadBalancer:
    boto3_raw_data: "type_defs.LoadBalancerTypeDef" = dataclasses.field()

    targetGroupArn = field("targetGroupArn")
    loadBalancerName = field("loadBalancerName")
    containerName = field("containerName")
    containerPort = field("containerPort")

    @cached_property
    def advancedConfiguration(self):  # pragma: no cover
        return AdvancedConfiguration.make_one(
            self.boto3_raw_data["advancedConfiguration"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LoadBalancerTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LoadBalancerTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SubmitAttachmentStateChangesRequest:
    boto3_raw_data: "type_defs.SubmitAttachmentStateChangesRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def attachments(self):  # pragma: no cover
        return AttachmentStateChange.make_many(self.boto3_raw_data["attachments"])

    cluster = field("cluster")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SubmitAttachmentStateChangesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SubmitAttachmentStateChangesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Attachment:
    boto3_raw_data: "type_defs.AttachmentTypeDef" = dataclasses.field()

    id = field("id")
    type = field("type")
    status = field("status")

    @cached_property
    def details(self):  # pragma: no cover
        return KeyValuePair.make_many(self.boto3_raw_data["details"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AttachmentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AttachmentTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProxyConfigurationOutput:
    boto3_raw_data: "type_defs.ProxyConfigurationOutputTypeDef" = dataclasses.field()

    containerName = field("containerName")
    type = field("type")

    @cached_property
    def properties(self):  # pragma: no cover
        return KeyValuePair.make_many(self.boto3_raw_data["properties"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProxyConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProxyConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProxyConfiguration:
    boto3_raw_data: "type_defs.ProxyConfigurationTypeDef" = dataclasses.field()

    containerName = field("containerName")
    type = field("type")

    @cached_property
    def properties(self):  # pragma: no cover
        return KeyValuePair.make_many(self.boto3_raw_data["properties"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProxyConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProxyConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAttributesRequest:
    boto3_raw_data: "type_defs.DeleteAttributesRequestTypeDef" = dataclasses.field()

    @cached_property
    def attributes(self):  # pragma: no cover
        return Attribute.make_many(self.boto3_raw_data["attributes"])

    cluster = field("cluster")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAttributesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAttributesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutAttributesRequest:
    boto3_raw_data: "type_defs.PutAttributesRequestTypeDef" = dataclasses.field()

    @cached_property
    def attributes(self):  # pragma: no cover
        return Attribute.make_many(self.boto3_raw_data["attributes"])

    cluster = field("cluster")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutAttributesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutAttributesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutoScalingGroupProvider:
    boto3_raw_data: "type_defs.AutoScalingGroupProviderTypeDef" = dataclasses.field()

    autoScalingGroupArn = field("autoScalingGroupArn")

    @cached_property
    def managedScaling(self):  # pragma: no cover
        return ManagedScaling.make_one(self.boto3_raw_data["managedScaling"])

    managedTerminationProtection = field("managedTerminationProtection")
    managedDraining = field("managedDraining")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AutoScalingGroupProviderTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutoScalingGroupProviderTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutoScalingGroupProviderUpdate:
    boto3_raw_data: "type_defs.AutoScalingGroupProviderUpdateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def managedScaling(self):  # pragma: no cover
        return ManagedScaling.make_one(self.boto3_raw_data["managedScaling"])

    managedTerminationProtection = field("managedTerminationProtection")
    managedDraining = field("managedDraining")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AutoScalingGroupProviderUpdateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutoScalingGroupProviderUpdateTypeDef"]
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
class NetworkConfiguration:
    boto3_raw_data: "type_defs.NetworkConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def awsvpcConfiguration(self):  # pragma: no cover
        return AwsVpcConfiguration.make_one(self.boto3_raw_data["awsvpcConfiguration"])

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
class PutClusterCapacityProvidersRequest:
    boto3_raw_data: "type_defs.PutClusterCapacityProvidersRequestTypeDef" = (
        dataclasses.field()
    )

    cluster = field("cluster")
    capacityProviders = field("capacityProviders")

    @cached_property
    def defaultCapacityProviderStrategy(self):  # pragma: no cover
        return CapacityProviderStrategyItem.make_many(
            self.boto3_raw_data["defaultCapacityProviderStrategy"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutClusterCapacityProvidersRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutClusterCapacityProvidersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EBSTagSpecificationOutput:
    boto3_raw_data: "type_defs.EBSTagSpecificationOutputTypeDef" = dataclasses.field()

    resourceType = field("resourceType")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    propagateTags = field("propagateTags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EBSTagSpecificationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EBSTagSpecificationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EBSTagSpecification:
    boto3_raw_data: "type_defs.EBSTagSpecificationTypeDef" = dataclasses.field()

    resourceType = field("resourceType")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    propagateTags = field("propagateTags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EBSTagSpecificationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EBSTagSpecificationTypeDef"]
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

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

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
class UpdateClusterSettingsRequest:
    boto3_raw_data: "type_defs.UpdateClusterSettingsRequestTypeDef" = (
        dataclasses.field()
    )

    cluster = field("cluster")

    @cached_property
    def settings(self):  # pragma: no cover
        return ClusterSetting.make_many(self.boto3_raw_data["settings"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateClusterSettingsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateClusterSettingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContainerOverrideOutput:
    boto3_raw_data: "type_defs.ContainerOverrideOutputTypeDef" = dataclasses.field()

    name = field("name")
    command = field("command")

    @cached_property
    def environment(self):  # pragma: no cover
        return KeyValuePair.make_many(self.boto3_raw_data["environment"])

    @cached_property
    def environmentFiles(self):  # pragma: no cover
        return EnvironmentFile.make_many(self.boto3_raw_data["environmentFiles"])

    cpu = field("cpu")
    memory = field("memory")
    memoryReservation = field("memoryReservation")

    @cached_property
    def resourceRequirements(self):  # pragma: no cover
        return ResourceRequirement.make_many(
            self.boto3_raw_data["resourceRequirements"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContainerOverrideOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContainerOverrideOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContainerOverride:
    boto3_raw_data: "type_defs.ContainerOverrideTypeDef" = dataclasses.field()

    name = field("name")
    command = field("command")

    @cached_property
    def environment(self):  # pragma: no cover
        return KeyValuePair.make_many(self.boto3_raw_data["environment"])

    @cached_property
    def environmentFiles(self):  # pragma: no cover
        return EnvironmentFile.make_many(self.boto3_raw_data["environmentFiles"])

    cpu = field("cpu")
    memory = field("memory")
    memoryReservation = field("memoryReservation")

    @cached_property
    def resourceRequirements(self):  # pragma: no cover
        return ResourceRequirement.make_many(
            self.boto3_raw_data["resourceRequirements"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ContainerOverrideTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContainerOverrideTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LogConfigurationOutput:
    boto3_raw_data: "type_defs.LogConfigurationOutputTypeDef" = dataclasses.field()

    logDriver = field("logDriver")
    options = field("options")

    @cached_property
    def secretOptions(self):  # pragma: no cover
        return Secret.make_many(self.boto3_raw_data["secretOptions"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LogConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LogConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LogConfiguration:
    boto3_raw_data: "type_defs.LogConfigurationTypeDef" = dataclasses.field()

    logDriver = field("logDriver")
    options = field("options")

    @cached_property
    def secretOptions(self):  # pragma: no cover
        return Secret.make_many(self.boto3_raw_data["secretOptions"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LogConfigurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LogConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContainerInstanceHealthStatus:
    boto3_raw_data: "type_defs.ContainerInstanceHealthStatusTypeDef" = (
        dataclasses.field()
    )

    overallStatus = field("overallStatus")

    @cached_property
    def details(self):  # pragma: no cover
        return InstanceHealthCheckResult.make_many(self.boto3_raw_data["details"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ContainerInstanceHealthStatusTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContainerInstanceHealthStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContainerStateChange:
    boto3_raw_data: "type_defs.ContainerStateChangeTypeDef" = dataclasses.field()

    containerName = field("containerName")
    imageDigest = field("imageDigest")
    runtimeId = field("runtimeId")
    exitCode = field("exitCode")

    @cached_property
    def networkBindings(self):  # pragma: no cover
        return NetworkBinding.make_many(self.boto3_raw_data["networkBindings"])

    reason = field("reason")
    status = field("status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContainerStateChangeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContainerStateChangeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SubmitContainerStateChangeRequest:
    boto3_raw_data: "type_defs.SubmitContainerStateChangeRequestTypeDef" = (
        dataclasses.field()
    )

    cluster = field("cluster")
    task = field("task")
    containerName = field("containerName")
    runtimeId = field("runtimeId")
    status = field("status")
    exitCode = field("exitCode")
    reason = field("reason")

    @cached_property
    def networkBindings(self):  # pragma: no cover
        return NetworkBinding.make_many(self.boto3_raw_data["networkBindings"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SubmitContainerStateChangeRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SubmitContainerStateChangeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Container:
    boto3_raw_data: "type_defs.ContainerTypeDef" = dataclasses.field()

    containerArn = field("containerArn")
    taskArn = field("taskArn")
    name = field("name")
    image = field("image")
    imageDigest = field("imageDigest")
    runtimeId = field("runtimeId")
    lastStatus = field("lastStatus")
    exitCode = field("exitCode")
    reason = field("reason")

    @cached_property
    def networkBindings(self):  # pragma: no cover
        return NetworkBinding.make_many(self.boto3_raw_data["networkBindings"])

    @cached_property
    def networkInterfaces(self):  # pragma: no cover
        return NetworkInterface.make_many(self.boto3_raw_data["networkInterfaces"])

    healthStatus = field("healthStatus")

    @cached_property
    def managedAgents(self):  # pragma: no cover
        return ManagedAgent.make_many(self.boto3_raw_data["managedAgents"])

    cpu = field("cpu")
    memory = field("memory")
    memoryReservation = field("memoryReservation")
    gpuIds = field("gpuIds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ContainerTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ContainerTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAttributesResponse:
    boto3_raw_data: "type_defs.DeleteAttributesResponseTypeDef" = dataclasses.field()

    @cached_property
    def attributes(self):  # pragma: no cover
        return Attribute.make_many(self.boto3_raw_data["attributes"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAttributesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAttributesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DiscoverPollEndpointResponse:
    boto3_raw_data: "type_defs.DiscoverPollEndpointResponseTypeDef" = (
        dataclasses.field()
    )

    endpoint = field("endpoint")
    telemetryEndpoint = field("telemetryEndpoint")
    serviceConnectEndpoint = field("serviceConnectEndpoint")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DiscoverPollEndpointResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DiscoverPollEndpointResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAttributesResponse:
    boto3_raw_data: "type_defs.ListAttributesResponseTypeDef" = dataclasses.field()

    @cached_property
    def attributes(self):  # pragma: no cover
        return Attribute.make_many(self.boto3_raw_data["attributes"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAttributesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAttributesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListClustersResponse:
    boto3_raw_data: "type_defs.ListClustersResponseTypeDef" = dataclasses.field()

    clusterArns = field("clusterArns")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListClustersResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListClustersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListContainerInstancesResponse:
    boto3_raw_data: "type_defs.ListContainerInstancesResponseTypeDef" = (
        dataclasses.field()
    )

    containerInstanceArns = field("containerInstanceArns")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListContainerInstancesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListContainerInstancesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServicesByNamespaceResponse:
    boto3_raw_data: "type_defs.ListServicesByNamespaceResponseTypeDef" = (
        dataclasses.field()
    )

    serviceArns = field("serviceArns")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListServicesByNamespaceResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServicesByNamespaceResponseTypeDef"]
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

    serviceArns = field("serviceArns")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

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
class ListTagsForResourceResponse:
    boto3_raw_data: "type_defs.ListTagsForResourceResponseTypeDef" = dataclasses.field()

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

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
class ListTaskDefinitionFamiliesResponse:
    boto3_raw_data: "type_defs.ListTaskDefinitionFamiliesResponseTypeDef" = (
        dataclasses.field()
    )

    families = field("families")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListTaskDefinitionFamiliesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTaskDefinitionFamiliesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTaskDefinitionsResponse:
    boto3_raw_data: "type_defs.ListTaskDefinitionsResponseTypeDef" = dataclasses.field()

    taskDefinitionArns = field("taskDefinitionArns")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTaskDefinitionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTaskDefinitionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTasksResponse:
    boto3_raw_data: "type_defs.ListTasksResponseTypeDef" = dataclasses.field()

    taskArns = field("taskArns")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListTasksResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTasksResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutAttributesResponse:
    boto3_raw_data: "type_defs.PutAttributesResponseTypeDef" = dataclasses.field()

    @cached_property
    def attributes(self):  # pragma: no cover
        return Attribute.make_many(self.boto3_raw_data["attributes"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutAttributesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutAttributesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopServiceDeploymentResponse:
    boto3_raw_data: "type_defs.StopServiceDeploymentResponseTypeDef" = (
        dataclasses.field()
    )

    serviceDeploymentArn = field("serviceDeploymentArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StopServiceDeploymentResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopServiceDeploymentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SubmitAttachmentStateChangesResponse:
    boto3_raw_data: "type_defs.SubmitAttachmentStateChangesResponseTypeDef" = (
        dataclasses.field()
    )

    acknowledgment = field("acknowledgment")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SubmitAttachmentStateChangesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SubmitAttachmentStateChangesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SubmitContainerStateChangeResponse:
    boto3_raw_data: "type_defs.SubmitContainerStateChangeResponseTypeDef" = (
        dataclasses.field()
    )

    acknowledgment = field("acknowledgment")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SubmitContainerStateChangeResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SubmitContainerStateChangeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SubmitTaskStateChangeResponse:
    boto3_raw_data: "type_defs.SubmitTaskStateChangeResponseTypeDef" = (
        dataclasses.field()
    )

    acknowledgment = field("acknowledgment")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SubmitTaskStateChangeResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SubmitTaskStateChangeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateTaskSetRequest:
    boto3_raw_data: "type_defs.UpdateTaskSetRequestTypeDef" = dataclasses.field()

    cluster = field("cluster")
    service = field("service")
    taskSet = field("taskSet")

    @cached_property
    def scale(self):  # pragma: no cover
        return Scale.make_one(self.boto3_raw_data["scale"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateTaskSetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTaskSetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatedAt:
    boto3_raw_data: "type_defs.CreatedAtTypeDef" = dataclasses.field()

    before = field("before")
    after = field("after")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreatedAtTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CreatedAtTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAccountSettingResponse:
    boto3_raw_data: "type_defs.DeleteAccountSettingResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def setting(self):  # pragma: no cover
        return Setting.make_one(self.boto3_raw_data["setting"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAccountSettingResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAccountSettingResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAccountSettingsResponse:
    boto3_raw_data: "type_defs.ListAccountSettingsResponseTypeDef" = dataclasses.field()

    @cached_property
    def settings(self):  # pragma: no cover
        return Setting.make_many(self.boto3_raw_data["settings"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAccountSettingsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAccountSettingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutAccountSettingDefaultResponse:
    boto3_raw_data: "type_defs.PutAccountSettingDefaultResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def setting(self):  # pragma: no cover
        return Setting.make_one(self.boto3_raw_data["setting"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PutAccountSettingDefaultResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutAccountSettingDefaultResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutAccountSettingResponse:
    boto3_raw_data: "type_defs.PutAccountSettingResponseTypeDef" = dataclasses.field()

    @cached_property
    def setting(self):  # pragma: no cover
        return Setting.make_one(self.boto3_raw_data["setting"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutAccountSettingResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutAccountSettingResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeploymentConfigurationOutput:
    boto3_raw_data: "type_defs.DeploymentConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def deploymentCircuitBreaker(self):  # pragma: no cover
        return DeploymentCircuitBreaker.make_one(
            self.boto3_raw_data["deploymentCircuitBreaker"]
        )

    maximumPercent = field("maximumPercent")
    minimumHealthyPercent = field("minimumHealthyPercent")

    @cached_property
    def alarms(self):  # pragma: no cover
        return DeploymentAlarmsOutput.make_one(self.boto3_raw_data["alarms"])

    strategy = field("strategy")
    bakeTimeInMinutes = field("bakeTimeInMinutes")

    @cached_property
    def lifecycleHooks(self):  # pragma: no cover
        return DeploymentLifecycleHookOutput.make_many(
            self.boto3_raw_data["lifecycleHooks"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeploymentConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeploymentConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeploymentConfiguration:
    boto3_raw_data: "type_defs.DeploymentConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def deploymentCircuitBreaker(self):  # pragma: no cover
        return DeploymentCircuitBreaker.make_one(
            self.boto3_raw_data["deploymentCircuitBreaker"]
        )

    maximumPercent = field("maximumPercent")
    minimumHealthyPercent = field("minimumHealthyPercent")

    @cached_property
    def alarms(self):  # pragma: no cover
        return DeploymentAlarms.make_one(self.boto3_raw_data["alarms"])

    strategy = field("strategy")
    bakeTimeInMinutes = field("bakeTimeInMinutes")

    @cached_property
    def lifecycleHooks(self):  # pragma: no cover
        return DeploymentLifecycleHook.make_many(self.boto3_raw_data["lifecycleHooks"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeploymentConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeploymentConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeServicesRequestWaitExtra:
    boto3_raw_data: "type_defs.DescribeServicesRequestWaitExtraTypeDef" = (
        dataclasses.field()
    )

    services = field("services")
    cluster = field("cluster")
    include = field("include")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeServicesRequestWaitExtraTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeServicesRequestWaitExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeServicesRequestWait:
    boto3_raw_data: "type_defs.DescribeServicesRequestWaitTypeDef" = dataclasses.field()

    services = field("services")
    cluster = field("cluster")
    include = field("include")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeServicesRequestWaitTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeServicesRequestWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTasksRequestWaitExtra:
    boto3_raw_data: "type_defs.DescribeTasksRequestWaitExtraTypeDef" = (
        dataclasses.field()
    )

    tasks = field("tasks")
    cluster = field("cluster")
    include = field("include")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeTasksRequestWaitExtraTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTasksRequestWaitExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTasksRequestWait:
    boto3_raw_data: "type_defs.DescribeTasksRequestWaitTypeDef" = dataclasses.field()

    tasks = field("tasks")
    cluster = field("cluster")
    include = field("include")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeTasksRequestWaitTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTasksRequestWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EFSVolumeConfiguration:
    boto3_raw_data: "type_defs.EFSVolumeConfigurationTypeDef" = dataclasses.field()

    fileSystemId = field("fileSystemId")
    rootDirectory = field("rootDirectory")
    transitEncryption = field("transitEncryption")
    transitEncryptionPort = field("transitEncryptionPort")

    @cached_property
    def authorizationConfig(self):  # pragma: no cover
        return EFSAuthorizationConfig.make_one(
            self.boto3_raw_data["authorizationConfig"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EFSVolumeConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EFSVolumeConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExecuteCommandConfiguration:
    boto3_raw_data: "type_defs.ExecuteCommandConfigurationTypeDef" = dataclasses.field()

    kmsKeyId = field("kmsKeyId")
    logging = field("logging")

    @cached_property
    def logConfiguration(self):  # pragma: no cover
        return ExecuteCommandLogConfiguration.make_one(
            self.boto3_raw_data["logConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExecuteCommandConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExecuteCommandConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExecuteCommandResponse:
    boto3_raw_data: "type_defs.ExecuteCommandResponseTypeDef" = dataclasses.field()

    clusterArn = field("clusterArn")
    containerArn = field("containerArn")
    containerName = field("containerName")
    interactive = field("interactive")

    @cached_property
    def session(self):  # pragma: no cover
        return Session.make_one(self.boto3_raw_data["session"])

    taskArn = field("taskArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExecuteCommandResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExecuteCommandResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FSxWindowsFileServerVolumeConfiguration:
    boto3_raw_data: "type_defs.FSxWindowsFileServerVolumeConfigurationTypeDef" = (
        dataclasses.field()
    )

    fileSystemId = field("fileSystemId")
    rootDirectory = field("rootDirectory")

    @cached_property
    def authorizationConfig(self):  # pragma: no cover
        return FSxWindowsFileServerAuthorizationConfig.make_one(
            self.boto3_raw_data["authorizationConfig"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.FSxWindowsFileServerVolumeConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FSxWindowsFileServerVolumeConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTaskProtectionResponse:
    boto3_raw_data: "type_defs.GetTaskProtectionResponseTypeDef" = dataclasses.field()

    @cached_property
    def protectedTasks(self):  # pragma: no cover
        return ProtectedTask.make_many(self.boto3_raw_data["protectedTasks"])

    @cached_property
    def failures(self):  # pragma: no cover
        return Failure.make_many(self.boto3_raw_data["failures"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTaskProtectionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTaskProtectionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateTaskProtectionResponse:
    boto3_raw_data: "type_defs.UpdateTaskProtectionResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def protectedTasks(self):  # pragma: no cover
        return ProtectedTask.make_many(self.boto3_raw_data["protectedTasks"])

    @cached_property
    def failures(self):  # pragma: no cover
        return Failure.make_many(self.boto3_raw_data["failures"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateTaskProtectionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTaskProtectionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LinuxParametersOutput:
    boto3_raw_data: "type_defs.LinuxParametersOutputTypeDef" = dataclasses.field()

    @cached_property
    def capabilities(self):  # pragma: no cover
        return KernelCapabilitiesOutput.make_one(self.boto3_raw_data["capabilities"])

    @cached_property
    def devices(self):  # pragma: no cover
        return DeviceOutput.make_many(self.boto3_raw_data["devices"])

    initProcessEnabled = field("initProcessEnabled")
    sharedMemorySize = field("sharedMemorySize")

    @cached_property
    def tmpfs(self):  # pragma: no cover
        return TmpfsOutput.make_many(self.boto3_raw_data["tmpfs"])

    maxSwap = field("maxSwap")
    swappiness = field("swappiness")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LinuxParametersOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LinuxParametersOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAccountSettingsRequestPaginate:
    boto3_raw_data: "type_defs.ListAccountSettingsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    value = field("value")
    principalArn = field("principalArn")
    effectiveSettings = field("effectiveSettings")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAccountSettingsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAccountSettingsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAttributesRequestPaginate:
    boto3_raw_data: "type_defs.ListAttributesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    targetType = field("targetType")
    cluster = field("cluster")
    attributeName = field("attributeName")
    attributeValue = field("attributeValue")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAttributesRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAttributesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListClustersRequestPaginate:
    boto3_raw_data: "type_defs.ListClustersRequestPaginateTypeDef" = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListClustersRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListClustersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListContainerInstancesRequestPaginate:
    boto3_raw_data: "type_defs.ListContainerInstancesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    cluster = field("cluster")
    filter = field("filter")
    status = field("status")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListContainerInstancesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListContainerInstancesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServicesByNamespaceRequestPaginate:
    boto3_raw_data: "type_defs.ListServicesByNamespaceRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    namespace = field("namespace")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListServicesByNamespaceRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServicesByNamespaceRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServicesRequestPaginate:
    boto3_raw_data: "type_defs.ListServicesRequestPaginateTypeDef" = dataclasses.field()

    cluster = field("cluster")
    launchType = field("launchType")
    schedulingStrategy = field("schedulingStrategy")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListServicesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServicesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTaskDefinitionFamiliesRequestPaginate:
    boto3_raw_data: "type_defs.ListTaskDefinitionFamiliesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    familyPrefix = field("familyPrefix")
    status = field("status")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListTaskDefinitionFamiliesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTaskDefinitionFamiliesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTaskDefinitionsRequestPaginate:
    boto3_raw_data: "type_defs.ListTaskDefinitionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    familyPrefix = field("familyPrefix")
    status = field("status")
    sort = field("sort")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListTaskDefinitionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTaskDefinitionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTasksRequestPaginate:
    boto3_raw_data: "type_defs.ListTasksRequestPaginateTypeDef" = dataclasses.field()

    cluster = field("cluster")
    containerInstance = field("containerInstance")
    family = field("family")
    startedBy = field("startedBy")
    serviceName = field("serviceName")
    desiredStatus = field("desiredStatus")
    launchType = field("launchType")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTasksRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTasksRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServiceDeploymentsResponse:
    boto3_raw_data: "type_defs.ListServiceDeploymentsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def serviceDeployments(self):  # pragma: no cover
        return ServiceDeploymentBrief.make_many(
            self.boto3_raw_data["serviceDeployments"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListServiceDeploymentsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServiceDeploymentsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResolvedConfiguration:
    boto3_raw_data: "type_defs.ResolvedConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def loadBalancers(self):  # pragma: no cover
        return ServiceRevisionLoadBalancer.make_many(
            self.boto3_raw_data["loadBalancers"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResolvedConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResolvedConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceConnectTestTrafficHeaderRules:
    boto3_raw_data: "type_defs.ServiceConnectTestTrafficHeaderRulesTypeDef" = (
        dataclasses.field()
    )

    name = field("name")

    @cached_property
    def value(self):  # pragma: no cover
        return ServiceConnectTestTrafficHeaderMatchRules.make_one(
            self.boto3_raw_data["value"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ServiceConnectTestTrafficHeaderRulesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceConnectTestTrafficHeaderRulesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceConnectTlsConfiguration:
    boto3_raw_data: "type_defs.ServiceConnectTlsConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def issuerCertificateAuthority(self):  # pragma: no cover
        return ServiceConnectTlsCertificateAuthority.make_one(
            self.boto3_raw_data["issuerCertificateAuthority"]
        )

    kmsKey = field("kmsKey")
    roleArn = field("roleArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ServiceConnectTlsConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceConnectTlsConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CapacityProvider:
    boto3_raw_data: "type_defs.CapacityProviderTypeDef" = dataclasses.field()

    capacityProviderArn = field("capacityProviderArn")
    name = field("name")
    status = field("status")

    @cached_property
    def autoScalingGroupProvider(self):  # pragma: no cover
        return AutoScalingGroupProvider.make_one(
            self.boto3_raw_data["autoScalingGroupProvider"]
        )

    updateStatus = field("updateStatus")
    updateStatusReason = field("updateStatusReason")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CapacityProviderTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CapacityProviderTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCapacityProviderRequest:
    boto3_raw_data: "type_defs.CreateCapacityProviderRequestTypeDef" = (
        dataclasses.field()
    )

    name = field("name")

    @cached_property
    def autoScalingGroupProvider(self):  # pragma: no cover
        return AutoScalingGroupProvider.make_one(
            self.boto3_raw_data["autoScalingGroupProvider"]
        )

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateCapacityProviderRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCapacityProviderRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCapacityProviderRequest:
    boto3_raw_data: "type_defs.UpdateCapacityProviderRequestTypeDef" = (
        dataclasses.field()
    )

    name = field("name")

    @cached_property
    def autoScalingGroupProvider(self):  # pragma: no cover
        return AutoScalingGroupProviderUpdate.make_one(
            self.boto3_raw_data["autoScalingGroupProvider"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateCapacityProviderRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCapacityProviderRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TaskSet:
    boto3_raw_data: "type_defs.TaskSetTypeDef" = dataclasses.field()

    id = field("id")
    taskSetArn = field("taskSetArn")
    serviceArn = field("serviceArn")
    clusterArn = field("clusterArn")
    startedBy = field("startedBy")
    externalId = field("externalId")
    status = field("status")
    taskDefinition = field("taskDefinition")
    computedDesiredCount = field("computedDesiredCount")
    pendingCount = field("pendingCount")
    runningCount = field("runningCount")
    createdAt = field("createdAt")
    updatedAt = field("updatedAt")
    launchType = field("launchType")

    @cached_property
    def capacityProviderStrategy(self):  # pragma: no cover
        return CapacityProviderStrategyItem.make_many(
            self.boto3_raw_data["capacityProviderStrategy"]
        )

    platformVersion = field("platformVersion")
    platformFamily = field("platformFamily")

    @cached_property
    def networkConfiguration(self):  # pragma: no cover
        return NetworkConfigurationOutput.make_one(
            self.boto3_raw_data["networkConfiguration"]
        )

    @cached_property
    def loadBalancers(self):  # pragma: no cover
        return LoadBalancer.make_many(self.boto3_raw_data["loadBalancers"])

    @cached_property
    def serviceRegistries(self):  # pragma: no cover
        return ServiceRegistry.make_many(self.boto3_raw_data["serviceRegistries"])

    @cached_property
    def scale(self):  # pragma: no cover
        return Scale.make_one(self.boto3_raw_data["scale"])

    stabilityStatus = field("stabilityStatus")
    stabilityStatusAt = field("stabilityStatusAt")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @cached_property
    def fargateEphemeralStorage(self):  # pragma: no cover
        return DeploymentEphemeralStorage.make_one(
            self.boto3_raw_data["fargateEphemeralStorage"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TaskSetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TaskSetTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceManagedEBSVolumeConfigurationOutput:
    boto3_raw_data: "type_defs.ServiceManagedEBSVolumeConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    roleArn = field("roleArn")
    encrypted = field("encrypted")
    kmsKeyId = field("kmsKeyId")
    volumeType = field("volumeType")
    sizeInGiB = field("sizeInGiB")
    snapshotId = field("snapshotId")
    volumeInitializationRate = field("volumeInitializationRate")
    iops = field("iops")
    throughput = field("throughput")

    @cached_property
    def tagSpecifications(self):  # pragma: no cover
        return EBSTagSpecificationOutput.make_many(
            self.boto3_raw_data["tagSpecifications"]
        )

    filesystemType = field("filesystemType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ServiceManagedEBSVolumeConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceManagedEBSVolumeConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TaskOverrideOutput:
    boto3_raw_data: "type_defs.TaskOverrideOutputTypeDef" = dataclasses.field()

    @cached_property
    def containerOverrides(self):  # pragma: no cover
        return ContainerOverrideOutput.make_many(
            self.boto3_raw_data["containerOverrides"]
        )

    cpu = field("cpu")

    @cached_property
    def inferenceAcceleratorOverrides(self):  # pragma: no cover
        return InferenceAcceleratorOverride.make_many(
            self.boto3_raw_data["inferenceAcceleratorOverrides"]
        )

    executionRoleArn = field("executionRoleArn")
    memory = field("memory")
    taskRoleArn = field("taskRoleArn")

    @cached_property
    def ephemeralStorage(self):  # pragma: no cover
        return EphemeralStorage.make_one(self.boto3_raw_data["ephemeralStorage"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TaskOverrideOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TaskOverrideOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TaskOverride:
    boto3_raw_data: "type_defs.TaskOverrideTypeDef" = dataclasses.field()

    @cached_property
    def containerOverrides(self):  # pragma: no cover
        return ContainerOverride.make_many(self.boto3_raw_data["containerOverrides"])

    cpu = field("cpu")

    @cached_property
    def inferenceAcceleratorOverrides(self):  # pragma: no cover
        return InferenceAcceleratorOverride.make_many(
            self.boto3_raw_data["inferenceAcceleratorOverrides"]
        )

    executionRoleArn = field("executionRoleArn")
    memory = field("memory")
    taskRoleArn = field("taskRoleArn")

    @cached_property
    def ephemeralStorage(self):  # pragma: no cover
        return EphemeralStorage.make_one(self.boto3_raw_data["ephemeralStorage"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TaskOverrideTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TaskOverrideTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContainerInstance:
    boto3_raw_data: "type_defs.ContainerInstanceTypeDef" = dataclasses.field()

    containerInstanceArn = field("containerInstanceArn")
    ec2InstanceId = field("ec2InstanceId")
    capacityProviderName = field("capacityProviderName")
    version = field("version")

    @cached_property
    def versionInfo(self):  # pragma: no cover
        return VersionInfo.make_one(self.boto3_raw_data["versionInfo"])

    @cached_property
    def remainingResources(self):  # pragma: no cover
        return ResourceOutput.make_many(self.boto3_raw_data["remainingResources"])

    @cached_property
    def registeredResources(self):  # pragma: no cover
        return ResourceOutput.make_many(self.boto3_raw_data["registeredResources"])

    status = field("status")
    statusReason = field("statusReason")
    agentConnected = field("agentConnected")
    runningTasksCount = field("runningTasksCount")
    pendingTasksCount = field("pendingTasksCount")
    agentUpdateStatus = field("agentUpdateStatus")

    @cached_property
    def attributes(self):  # pragma: no cover
        return Attribute.make_many(self.boto3_raw_data["attributes"])

    registeredAt = field("registeredAt")

    @cached_property
    def attachments(self):  # pragma: no cover
        return Attachment.make_many(self.boto3_raw_data["attachments"])

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @cached_property
    def healthStatus(self):  # pragma: no cover
        return ContainerInstanceHealthStatus.make_one(
            self.boto3_raw_data["healthStatus"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ContainerInstanceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContainerInstanceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SubmitTaskStateChangeRequest:
    boto3_raw_data: "type_defs.SubmitTaskStateChangeRequestTypeDef" = (
        dataclasses.field()
    )

    cluster = field("cluster")
    task = field("task")
    status = field("status")
    reason = field("reason")

    @cached_property
    def containers(self):  # pragma: no cover
        return ContainerStateChange.make_many(self.boto3_raw_data["containers"])

    @cached_property
    def attachments(self):  # pragma: no cover
        return AttachmentStateChange.make_many(self.boto3_raw_data["attachments"])

    @cached_property
    def managedAgents(self):  # pragma: no cover
        return ManagedAgentStateChange.make_many(self.boto3_raw_data["managedAgents"])

    pullStartedAt = field("pullStartedAt")
    pullStoppedAt = field("pullStoppedAt")
    executionStoppedAt = field("executionStoppedAt")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SubmitTaskStateChangeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SubmitTaskStateChangeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServiceDeploymentsRequest:
    boto3_raw_data: "type_defs.ListServiceDeploymentsRequestTypeDef" = (
        dataclasses.field()
    )

    service = field("service")
    cluster = field("cluster")
    status = field("status")

    @cached_property
    def createdAt(self):  # pragma: no cover
        return CreatedAt.make_one(self.boto3_raw_data["createdAt"])

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListServiceDeploymentsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServiceDeploymentsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceDeployment:
    boto3_raw_data: "type_defs.ServiceDeploymentTypeDef" = dataclasses.field()

    serviceDeploymentArn = field("serviceDeploymentArn")
    serviceArn = field("serviceArn")
    clusterArn = field("clusterArn")
    createdAt = field("createdAt")
    startedAt = field("startedAt")
    finishedAt = field("finishedAt")
    stoppedAt = field("stoppedAt")
    updatedAt = field("updatedAt")

    @cached_property
    def sourceServiceRevisions(self):  # pragma: no cover
        return ServiceRevisionSummary.make_many(
            self.boto3_raw_data["sourceServiceRevisions"]
        )

    @cached_property
    def targetServiceRevision(self):  # pragma: no cover
        return ServiceRevisionSummary.make_one(
            self.boto3_raw_data["targetServiceRevision"]
        )

    status = field("status")
    statusReason = field("statusReason")
    lifecycleStage = field("lifecycleStage")

    @cached_property
    def deploymentConfiguration(self):  # pragma: no cover
        return DeploymentConfigurationOutput.make_one(
            self.boto3_raw_data["deploymentConfiguration"]
        )

    @cached_property
    def rollback(self):  # pragma: no cover
        return Rollback.make_one(self.boto3_raw_data["rollback"])

    @cached_property
    def deploymentCircuitBreaker(self):  # pragma: no cover
        return ServiceDeploymentCircuitBreaker.make_one(
            self.boto3_raw_data["deploymentCircuitBreaker"]
        )

    @cached_property
    def alarms(self):  # pragma: no cover
        return ServiceDeploymentAlarms.make_one(self.boto3_raw_data["alarms"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ServiceDeploymentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceDeploymentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClusterConfiguration:
    boto3_raw_data: "type_defs.ClusterConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def executeCommandConfiguration(self):  # pragma: no cover
        return ExecuteCommandConfiguration.make_one(
            self.boto3_raw_data["executeCommandConfiguration"]
        )

    @cached_property
    def managedStorageConfiguration(self):  # pragma: no cover
        return ManagedStorageConfiguration.make_one(
            self.boto3_raw_data["managedStorageConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ClusterConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClusterConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VolumeOutput:
    boto3_raw_data: "type_defs.VolumeOutputTypeDef" = dataclasses.field()

    name = field("name")

    @cached_property
    def host(self):  # pragma: no cover
        return HostVolumeProperties.make_one(self.boto3_raw_data["host"])

    @cached_property
    def dockerVolumeConfiguration(self):  # pragma: no cover
        return DockerVolumeConfigurationOutput.make_one(
            self.boto3_raw_data["dockerVolumeConfiguration"]
        )

    @cached_property
    def efsVolumeConfiguration(self):  # pragma: no cover
        return EFSVolumeConfiguration.make_one(
            self.boto3_raw_data["efsVolumeConfiguration"]
        )

    @cached_property
    def fsxWindowsFileServerVolumeConfiguration(self):  # pragma: no cover
        return FSxWindowsFileServerVolumeConfiguration.make_one(
            self.boto3_raw_data["fsxWindowsFileServerVolumeConfiguration"]
        )

    configuredAtLaunch = field("configuredAtLaunch")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VolumeOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VolumeOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Volume:
    boto3_raw_data: "type_defs.VolumeTypeDef" = dataclasses.field()

    name = field("name")

    @cached_property
    def host(self):  # pragma: no cover
        return HostVolumeProperties.make_one(self.boto3_raw_data["host"])

    dockerVolumeConfiguration = field("dockerVolumeConfiguration")

    @cached_property
    def efsVolumeConfiguration(self):  # pragma: no cover
        return EFSVolumeConfiguration.make_one(
            self.boto3_raw_data["efsVolumeConfiguration"]
        )

    @cached_property
    def fsxWindowsFileServerVolumeConfiguration(self):  # pragma: no cover
        return FSxWindowsFileServerVolumeConfiguration.make_one(
            self.boto3_raw_data["fsxWindowsFileServerVolumeConfiguration"]
        )

    configuredAtLaunch = field("configuredAtLaunch")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VolumeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VolumeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContainerDefinitionOutput:
    boto3_raw_data: "type_defs.ContainerDefinitionOutputTypeDef" = dataclasses.field()

    name = field("name")
    image = field("image")

    @cached_property
    def repositoryCredentials(self):  # pragma: no cover
        return RepositoryCredentials.make_one(
            self.boto3_raw_data["repositoryCredentials"]
        )

    cpu = field("cpu")
    memory = field("memory")
    memoryReservation = field("memoryReservation")
    links = field("links")

    @cached_property
    def portMappings(self):  # pragma: no cover
        return PortMapping.make_many(self.boto3_raw_data["portMappings"])

    essential = field("essential")

    @cached_property
    def restartPolicy(self):  # pragma: no cover
        return ContainerRestartPolicyOutput.make_one(
            self.boto3_raw_data["restartPolicy"]
        )

    entryPoint = field("entryPoint")
    command = field("command")

    @cached_property
    def environment(self):  # pragma: no cover
        return KeyValuePair.make_many(self.boto3_raw_data["environment"])

    @cached_property
    def environmentFiles(self):  # pragma: no cover
        return EnvironmentFile.make_many(self.boto3_raw_data["environmentFiles"])

    @cached_property
    def mountPoints(self):  # pragma: no cover
        return MountPoint.make_many(self.boto3_raw_data["mountPoints"])

    @cached_property
    def volumesFrom(self):  # pragma: no cover
        return VolumeFrom.make_many(self.boto3_raw_data["volumesFrom"])

    @cached_property
    def linuxParameters(self):  # pragma: no cover
        return LinuxParametersOutput.make_one(self.boto3_raw_data["linuxParameters"])

    @cached_property
    def secrets(self):  # pragma: no cover
        return Secret.make_many(self.boto3_raw_data["secrets"])

    @cached_property
    def dependsOn(self):  # pragma: no cover
        return ContainerDependency.make_many(self.boto3_raw_data["dependsOn"])

    startTimeout = field("startTimeout")
    stopTimeout = field("stopTimeout")
    versionConsistency = field("versionConsistency")
    hostname = field("hostname")
    user = field("user")
    workingDirectory = field("workingDirectory")
    disableNetworking = field("disableNetworking")
    privileged = field("privileged")
    readonlyRootFilesystem = field("readonlyRootFilesystem")
    dnsServers = field("dnsServers")
    dnsSearchDomains = field("dnsSearchDomains")

    @cached_property
    def extraHosts(self):  # pragma: no cover
        return HostEntry.make_many(self.boto3_raw_data["extraHosts"])

    dockerSecurityOptions = field("dockerSecurityOptions")
    interactive = field("interactive")
    pseudoTerminal = field("pseudoTerminal")
    dockerLabels = field("dockerLabels")

    @cached_property
    def ulimits(self):  # pragma: no cover
        return Ulimit.make_many(self.boto3_raw_data["ulimits"])

    @cached_property
    def logConfiguration(self):  # pragma: no cover
        return LogConfigurationOutput.make_one(self.boto3_raw_data["logConfiguration"])

    @cached_property
    def healthCheck(self):  # pragma: no cover
        return HealthCheckOutput.make_one(self.boto3_raw_data["healthCheck"])

    @cached_property
    def systemControls(self):  # pragma: no cover
        return SystemControl.make_many(self.boto3_raw_data["systemControls"])

    @cached_property
    def resourceRequirements(self):  # pragma: no cover
        return ResourceRequirement.make_many(
            self.boto3_raw_data["resourceRequirements"]
        )

    @cached_property
    def firelensConfiguration(self):  # pragma: no cover
        return FirelensConfigurationOutput.make_one(
            self.boto3_raw_data["firelensConfiguration"]
        )

    credentialSpecs = field("credentialSpecs")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContainerDefinitionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContainerDefinitionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterContainerInstanceRequest:
    boto3_raw_data: "type_defs.RegisterContainerInstanceRequestTypeDef" = (
        dataclasses.field()
    )

    cluster = field("cluster")
    instanceIdentityDocument = field("instanceIdentityDocument")
    instanceIdentityDocumentSignature = field("instanceIdentityDocumentSignature")
    totalResources = field("totalResources")

    @cached_property
    def versionInfo(self):  # pragma: no cover
        return VersionInfo.make_one(self.boto3_raw_data["versionInfo"])

    containerInstanceArn = field("containerInstanceArn")

    @cached_property
    def attributes(self):  # pragma: no cover
        return Attribute.make_many(self.boto3_raw_data["attributes"])

    @cached_property
    def platformDevices(self):  # pragma: no cover
        return PlatformDevice.make_many(self.boto3_raw_data["platformDevices"])

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RegisterContainerInstanceRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterContainerInstanceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceConnectTestTrafficRules:
    boto3_raw_data: "type_defs.ServiceConnectTestTrafficRulesTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def header(self):  # pragma: no cover
        return ServiceConnectTestTrafficHeaderRules.make_one(
            self.boto3_raw_data["header"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ServiceConnectTestTrafficRulesTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceConnectTestTrafficRulesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LinuxParameters:
    boto3_raw_data: "type_defs.LinuxParametersTypeDef" = dataclasses.field()

    capabilities = field("capabilities")
    devices = field("devices")
    initProcessEnabled = field("initProcessEnabled")
    sharedMemorySize = field("sharedMemorySize")
    tmpfs = field("tmpfs")
    maxSwap = field("maxSwap")
    swappiness = field("swappiness")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LinuxParametersTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LinuxParametersTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCapacityProviderResponse:
    boto3_raw_data: "type_defs.CreateCapacityProviderResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def capacityProvider(self):  # pragma: no cover
        return CapacityProvider.make_one(self.boto3_raw_data["capacityProvider"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateCapacityProviderResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCapacityProviderResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCapacityProviderResponse:
    boto3_raw_data: "type_defs.DeleteCapacityProviderResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def capacityProvider(self):  # pragma: no cover
        return CapacityProvider.make_one(self.boto3_raw_data["capacityProvider"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteCapacityProviderResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCapacityProviderResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCapacityProvidersResponse:
    boto3_raw_data: "type_defs.DescribeCapacityProvidersResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def capacityProviders(self):  # pragma: no cover
        return CapacityProvider.make_many(self.boto3_raw_data["capacityProviders"])

    @cached_property
    def failures(self):  # pragma: no cover
        return Failure.make_many(self.boto3_raw_data["failures"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeCapacityProvidersResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCapacityProvidersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCapacityProviderResponse:
    boto3_raw_data: "type_defs.UpdateCapacityProviderResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def capacityProvider(self):  # pragma: no cover
        return CapacityProvider.make_one(self.boto3_raw_data["capacityProvider"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateCapacityProviderResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCapacityProviderResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTaskSetResponse:
    boto3_raw_data: "type_defs.CreateTaskSetResponseTypeDef" = dataclasses.field()

    @cached_property
    def taskSet(self):  # pragma: no cover
        return TaskSet.make_one(self.boto3_raw_data["taskSet"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateTaskSetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTaskSetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteTaskSetResponse:
    boto3_raw_data: "type_defs.DeleteTaskSetResponseTypeDef" = dataclasses.field()

    @cached_property
    def taskSet(self):  # pragma: no cover
        return TaskSet.make_one(self.boto3_raw_data["taskSet"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteTaskSetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteTaskSetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTaskSetsResponse:
    boto3_raw_data: "type_defs.DescribeTaskSetsResponseTypeDef" = dataclasses.field()

    @cached_property
    def taskSets(self):  # pragma: no cover
        return TaskSet.make_many(self.boto3_raw_data["taskSets"])

    @cached_property
    def failures(self):  # pragma: no cover
        return Failure.make_many(self.boto3_raw_data["failures"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeTaskSetsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTaskSetsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateServicePrimaryTaskSetResponse:
    boto3_raw_data: "type_defs.UpdateServicePrimaryTaskSetResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def taskSet(self):  # pragma: no cover
        return TaskSet.make_one(self.boto3_raw_data["taskSet"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateServicePrimaryTaskSetResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateServicePrimaryTaskSetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateTaskSetResponse:
    boto3_raw_data: "type_defs.UpdateTaskSetResponseTypeDef" = dataclasses.field()

    @cached_property
    def taskSet(self):  # pragma: no cover
        return TaskSet.make_one(self.boto3_raw_data["taskSet"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateTaskSetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTaskSetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTaskSetRequest:
    boto3_raw_data: "type_defs.CreateTaskSetRequestTypeDef" = dataclasses.field()

    service = field("service")
    cluster = field("cluster")
    taskDefinition = field("taskDefinition")
    externalId = field("externalId")
    networkConfiguration = field("networkConfiguration")

    @cached_property
    def loadBalancers(self):  # pragma: no cover
        return LoadBalancer.make_many(self.boto3_raw_data["loadBalancers"])

    @cached_property
    def serviceRegistries(self):  # pragma: no cover
        return ServiceRegistry.make_many(self.boto3_raw_data["serviceRegistries"])

    launchType = field("launchType")

    @cached_property
    def capacityProviderStrategy(self):  # pragma: no cover
        return CapacityProviderStrategyItem.make_many(
            self.boto3_raw_data["capacityProviderStrategy"]
        )

    platformVersion = field("platformVersion")

    @cached_property
    def scale(self):  # pragma: no cover
        return Scale.make_one(self.boto3_raw_data["scale"])

    clientToken = field("clientToken")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateTaskSetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTaskSetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceVolumeConfigurationOutput:
    boto3_raw_data: "type_defs.ServiceVolumeConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    name = field("name")

    @cached_property
    def managedEBSVolume(self):  # pragma: no cover
        return ServiceManagedEBSVolumeConfigurationOutput.make_one(
            self.boto3_raw_data["managedEBSVolume"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ServiceVolumeConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceVolumeConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceManagedEBSVolumeConfiguration:
    boto3_raw_data: "type_defs.ServiceManagedEBSVolumeConfigurationTypeDef" = (
        dataclasses.field()
    )

    roleArn = field("roleArn")
    encrypted = field("encrypted")
    kmsKeyId = field("kmsKeyId")
    volumeType = field("volumeType")
    sizeInGiB = field("sizeInGiB")
    snapshotId = field("snapshotId")
    volumeInitializationRate = field("volumeInitializationRate")
    iops = field("iops")
    throughput = field("throughput")
    tagSpecifications = field("tagSpecifications")
    filesystemType = field("filesystemType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ServiceManagedEBSVolumeConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceManagedEBSVolumeConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TaskManagedEBSVolumeConfiguration:
    boto3_raw_data: "type_defs.TaskManagedEBSVolumeConfigurationTypeDef" = (
        dataclasses.field()
    )

    roleArn = field("roleArn")
    encrypted = field("encrypted")
    kmsKeyId = field("kmsKeyId")
    volumeType = field("volumeType")
    sizeInGiB = field("sizeInGiB")
    snapshotId = field("snapshotId")
    volumeInitializationRate = field("volumeInitializationRate")
    iops = field("iops")
    throughput = field("throughput")
    tagSpecifications = field("tagSpecifications")

    @cached_property
    def terminationPolicy(self):  # pragma: no cover
        return TaskManagedEBSVolumeTerminationPolicy.make_one(
            self.boto3_raw_data["terminationPolicy"]
        )

    filesystemType = field("filesystemType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.TaskManagedEBSVolumeConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TaskManagedEBSVolumeConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Task:
    boto3_raw_data: "type_defs.TaskTypeDef" = dataclasses.field()

    @cached_property
    def attachments(self):  # pragma: no cover
        return Attachment.make_many(self.boto3_raw_data["attachments"])

    @cached_property
    def attributes(self):  # pragma: no cover
        return Attribute.make_many(self.boto3_raw_data["attributes"])

    availabilityZone = field("availabilityZone")
    capacityProviderName = field("capacityProviderName")
    clusterArn = field("clusterArn")
    connectivity = field("connectivity")
    connectivityAt = field("connectivityAt")
    containerInstanceArn = field("containerInstanceArn")

    @cached_property
    def containers(self):  # pragma: no cover
        return Container.make_many(self.boto3_raw_data["containers"])

    cpu = field("cpu")
    createdAt = field("createdAt")
    desiredStatus = field("desiredStatus")
    enableExecuteCommand = field("enableExecuteCommand")
    executionStoppedAt = field("executionStoppedAt")
    group = field("group")
    healthStatus = field("healthStatus")

    @cached_property
    def inferenceAccelerators(self):  # pragma: no cover
        return InferenceAccelerator.make_many(
            self.boto3_raw_data["inferenceAccelerators"]
        )

    lastStatus = field("lastStatus")
    launchType = field("launchType")
    memory = field("memory")

    @cached_property
    def overrides(self):  # pragma: no cover
        return TaskOverrideOutput.make_one(self.boto3_raw_data["overrides"])

    platformVersion = field("platformVersion")
    platformFamily = field("platformFamily")
    pullStartedAt = field("pullStartedAt")
    pullStoppedAt = field("pullStoppedAt")
    startedAt = field("startedAt")
    startedBy = field("startedBy")
    stopCode = field("stopCode")
    stoppedAt = field("stoppedAt")
    stoppedReason = field("stoppedReason")
    stoppingAt = field("stoppingAt")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    taskArn = field("taskArn")
    taskDefinitionArn = field("taskDefinitionArn")
    version = field("version")

    @cached_property
    def ephemeralStorage(self):  # pragma: no cover
        return EphemeralStorage.make_one(self.boto3_raw_data["ephemeralStorage"])

    @cached_property
    def fargateEphemeralStorage(self):  # pragma: no cover
        return TaskEphemeralStorage.make_one(
            self.boto3_raw_data["fargateEphemeralStorage"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TaskTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TaskTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeregisterContainerInstanceResponse:
    boto3_raw_data: "type_defs.DeregisterContainerInstanceResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def containerInstance(self):  # pragma: no cover
        return ContainerInstance.make_one(self.boto3_raw_data["containerInstance"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeregisterContainerInstanceResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeregisterContainerInstanceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeContainerInstancesResponse:
    boto3_raw_data: "type_defs.DescribeContainerInstancesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def containerInstances(self):  # pragma: no cover
        return ContainerInstance.make_many(self.boto3_raw_data["containerInstances"])

    @cached_property
    def failures(self):  # pragma: no cover
        return Failure.make_many(self.boto3_raw_data["failures"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeContainerInstancesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeContainerInstancesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterContainerInstanceResponse:
    boto3_raw_data: "type_defs.RegisterContainerInstanceResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def containerInstance(self):  # pragma: no cover
        return ContainerInstance.make_one(self.boto3_raw_data["containerInstance"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RegisterContainerInstanceResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterContainerInstanceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateContainerAgentResponse:
    boto3_raw_data: "type_defs.UpdateContainerAgentResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def containerInstance(self):  # pragma: no cover
        return ContainerInstance.make_one(self.boto3_raw_data["containerInstance"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateContainerAgentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateContainerAgentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateContainerInstancesStateResponse:
    boto3_raw_data: "type_defs.UpdateContainerInstancesStateResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def containerInstances(self):  # pragma: no cover
        return ContainerInstance.make_many(self.boto3_raw_data["containerInstances"])

    @cached_property
    def failures(self):  # pragma: no cover
        return Failure.make_many(self.boto3_raw_data["failures"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateContainerInstancesStateResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateContainerInstancesStateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeServiceDeploymentsResponse:
    boto3_raw_data: "type_defs.DescribeServiceDeploymentsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def serviceDeployments(self):  # pragma: no cover
        return ServiceDeployment.make_many(self.boto3_raw_data["serviceDeployments"])

    @cached_property
    def failures(self):  # pragma: no cover
        return Failure.make_many(self.boto3_raw_data["failures"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeServiceDeploymentsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeServiceDeploymentsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Cluster:
    boto3_raw_data: "type_defs.ClusterTypeDef" = dataclasses.field()

    clusterArn = field("clusterArn")
    clusterName = field("clusterName")

    @cached_property
    def configuration(self):  # pragma: no cover
        return ClusterConfiguration.make_one(self.boto3_raw_data["configuration"])

    status = field("status")
    registeredContainerInstancesCount = field("registeredContainerInstancesCount")
    runningTasksCount = field("runningTasksCount")
    pendingTasksCount = field("pendingTasksCount")
    activeServicesCount = field("activeServicesCount")

    @cached_property
    def statistics(self):  # pragma: no cover
        return KeyValuePair.make_many(self.boto3_raw_data["statistics"])

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @cached_property
    def settings(self):  # pragma: no cover
        return ClusterSetting.make_many(self.boto3_raw_data["settings"])

    capacityProviders = field("capacityProviders")

    @cached_property
    def defaultCapacityProviderStrategy(self):  # pragma: no cover
        return CapacityProviderStrategyItem.make_many(
            self.boto3_raw_data["defaultCapacityProviderStrategy"]
        )

    @cached_property
    def attachments(self):  # pragma: no cover
        return Attachment.make_many(self.boto3_raw_data["attachments"])

    attachmentsStatus = field("attachmentsStatus")

    @cached_property
    def serviceConnectDefaults(self):  # pragma: no cover
        return ClusterServiceConnectDefaults.make_one(
            self.boto3_raw_data["serviceConnectDefaults"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ClusterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ClusterTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateClusterRequest:
    boto3_raw_data: "type_defs.CreateClusterRequestTypeDef" = dataclasses.field()

    clusterName = field("clusterName")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @cached_property
    def settings(self):  # pragma: no cover
        return ClusterSetting.make_many(self.boto3_raw_data["settings"])

    @cached_property
    def configuration(self):  # pragma: no cover
        return ClusterConfiguration.make_one(self.boto3_raw_data["configuration"])

    capacityProviders = field("capacityProviders")

    @cached_property
    def defaultCapacityProviderStrategy(self):  # pragma: no cover
        return CapacityProviderStrategyItem.make_many(
            self.boto3_raw_data["defaultCapacityProviderStrategy"]
        )

    @cached_property
    def serviceConnectDefaults(self):  # pragma: no cover
        return ClusterServiceConnectDefaultsRequest.make_one(
            self.boto3_raw_data["serviceConnectDefaults"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateClusterRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateClusterRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateClusterRequest:
    boto3_raw_data: "type_defs.UpdateClusterRequestTypeDef" = dataclasses.field()

    cluster = field("cluster")

    @cached_property
    def settings(self):  # pragma: no cover
        return ClusterSetting.make_many(self.boto3_raw_data["settings"])

    @cached_property
    def configuration(self):  # pragma: no cover
        return ClusterConfiguration.make_one(self.boto3_raw_data["configuration"])

    @cached_property
    def serviceConnectDefaults(self):  # pragma: no cover
        return ClusterServiceConnectDefaultsRequest.make_one(
            self.boto3_raw_data["serviceConnectDefaults"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateClusterRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateClusterRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TaskDefinition:
    boto3_raw_data: "type_defs.TaskDefinitionTypeDef" = dataclasses.field()

    taskDefinitionArn = field("taskDefinitionArn")

    @cached_property
    def containerDefinitions(self):  # pragma: no cover
        return ContainerDefinitionOutput.make_many(
            self.boto3_raw_data["containerDefinitions"]
        )

    family = field("family")
    taskRoleArn = field("taskRoleArn")
    executionRoleArn = field("executionRoleArn")
    networkMode = field("networkMode")
    revision = field("revision")

    @cached_property
    def volumes(self):  # pragma: no cover
        return VolumeOutput.make_many(self.boto3_raw_data["volumes"])

    status = field("status")

    @cached_property
    def requiresAttributes(self):  # pragma: no cover
        return Attribute.make_many(self.boto3_raw_data["requiresAttributes"])

    @cached_property
    def placementConstraints(self):  # pragma: no cover
        return TaskDefinitionPlacementConstraint.make_many(
            self.boto3_raw_data["placementConstraints"]
        )

    compatibilities = field("compatibilities")

    @cached_property
    def runtimePlatform(self):  # pragma: no cover
        return RuntimePlatform.make_one(self.boto3_raw_data["runtimePlatform"])

    requiresCompatibilities = field("requiresCompatibilities")
    cpu = field("cpu")
    memory = field("memory")

    @cached_property
    def inferenceAccelerators(self):  # pragma: no cover
        return InferenceAccelerator.make_many(
            self.boto3_raw_data["inferenceAccelerators"]
        )

    pidMode = field("pidMode")
    ipcMode = field("ipcMode")

    @cached_property
    def proxyConfiguration(self):  # pragma: no cover
        return ProxyConfigurationOutput.make_one(
            self.boto3_raw_data["proxyConfiguration"]
        )

    registeredAt = field("registeredAt")
    deregisteredAt = field("deregisteredAt")
    registeredBy = field("registeredBy")

    @cached_property
    def ephemeralStorage(self):  # pragma: no cover
        return EphemeralStorage.make_one(self.boto3_raw_data["ephemeralStorage"])

    enableFaultInjection = field("enableFaultInjection")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TaskDefinitionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TaskDefinitionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceConnectClientAlias:
    boto3_raw_data: "type_defs.ServiceConnectClientAliasTypeDef" = dataclasses.field()

    port = field("port")
    dnsName = field("dnsName")

    @cached_property
    def testTrafficRules(self):  # pragma: no cover
        return ServiceConnectTestTrafficRules.make_one(
            self.boto3_raw_data["testTrafficRules"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ServiceConnectClientAliasTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceConnectClientAliasTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TaskVolumeConfiguration:
    boto3_raw_data: "type_defs.TaskVolumeConfigurationTypeDef" = dataclasses.field()

    name = field("name")

    @cached_property
    def managedEBSVolume(self):  # pragma: no cover
        return TaskManagedEBSVolumeConfiguration.make_one(
            self.boto3_raw_data["managedEBSVolume"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TaskVolumeConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TaskVolumeConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTasksResponse:
    boto3_raw_data: "type_defs.DescribeTasksResponseTypeDef" = dataclasses.field()

    @cached_property
    def tasks(self):  # pragma: no cover
        return Task.make_many(self.boto3_raw_data["tasks"])

    @cached_property
    def failures(self):  # pragma: no cover
        return Failure.make_many(self.boto3_raw_data["failures"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeTasksResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTasksResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RunTaskResponse:
    boto3_raw_data: "type_defs.RunTaskResponseTypeDef" = dataclasses.field()

    @cached_property
    def tasks(self):  # pragma: no cover
        return Task.make_many(self.boto3_raw_data["tasks"])

    @cached_property
    def failures(self):  # pragma: no cover
        return Failure.make_many(self.boto3_raw_data["failures"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RunTaskResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RunTaskResponseTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartTaskResponse:
    boto3_raw_data: "type_defs.StartTaskResponseTypeDef" = dataclasses.field()

    @cached_property
    def tasks(self):  # pragma: no cover
        return Task.make_many(self.boto3_raw_data["tasks"])

    @cached_property
    def failures(self):  # pragma: no cover
        return Failure.make_many(self.boto3_raw_data["failures"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StartTaskResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartTaskResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopTaskResponse:
    boto3_raw_data: "type_defs.StopTaskResponseTypeDef" = dataclasses.field()

    @cached_property
    def task(self):  # pragma: no cover
        return Task.make_one(self.boto3_raw_data["task"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StopTaskResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopTaskResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateClusterResponse:
    boto3_raw_data: "type_defs.CreateClusterResponseTypeDef" = dataclasses.field()

    @cached_property
    def cluster(self):  # pragma: no cover
        return Cluster.make_one(self.boto3_raw_data["cluster"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateClusterResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateClusterResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteClusterResponse:
    boto3_raw_data: "type_defs.DeleteClusterResponseTypeDef" = dataclasses.field()

    @cached_property
    def cluster(self):  # pragma: no cover
        return Cluster.make_one(self.boto3_raw_data["cluster"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteClusterResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteClusterResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeClustersResponse:
    boto3_raw_data: "type_defs.DescribeClustersResponseTypeDef" = dataclasses.field()

    @cached_property
    def clusters(self):  # pragma: no cover
        return Cluster.make_many(self.boto3_raw_data["clusters"])

    @cached_property
    def failures(self):  # pragma: no cover
        return Failure.make_many(self.boto3_raw_data["failures"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeClustersResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeClustersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutClusterCapacityProvidersResponse:
    boto3_raw_data: "type_defs.PutClusterCapacityProvidersResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def cluster(self):  # pragma: no cover
        return Cluster.make_one(self.boto3_raw_data["cluster"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutClusterCapacityProvidersResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutClusterCapacityProvidersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateClusterResponse:
    boto3_raw_data: "type_defs.UpdateClusterResponseTypeDef" = dataclasses.field()

    @cached_property
    def cluster(self):  # pragma: no cover
        return Cluster.make_one(self.boto3_raw_data["cluster"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateClusterResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateClusterResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateClusterSettingsResponse:
    boto3_raw_data: "type_defs.UpdateClusterSettingsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def cluster(self):  # pragma: no cover
        return Cluster.make_one(self.boto3_raw_data["cluster"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateClusterSettingsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateClusterSettingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteTaskDefinitionsResponse:
    boto3_raw_data: "type_defs.DeleteTaskDefinitionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def taskDefinitions(self):  # pragma: no cover
        return TaskDefinition.make_many(self.boto3_raw_data["taskDefinitions"])

    @cached_property
    def failures(self):  # pragma: no cover
        return Failure.make_many(self.boto3_raw_data["failures"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteTaskDefinitionsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteTaskDefinitionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeregisterTaskDefinitionResponse:
    boto3_raw_data: "type_defs.DeregisterTaskDefinitionResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def taskDefinition(self):  # pragma: no cover
        return TaskDefinition.make_one(self.boto3_raw_data["taskDefinition"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeregisterTaskDefinitionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeregisterTaskDefinitionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTaskDefinitionResponse:
    boto3_raw_data: "type_defs.DescribeTaskDefinitionResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def taskDefinition(self):  # pragma: no cover
        return TaskDefinition.make_one(self.boto3_raw_data["taskDefinition"])

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeTaskDefinitionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTaskDefinitionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterTaskDefinitionResponse:
    boto3_raw_data: "type_defs.RegisterTaskDefinitionResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def taskDefinition(self):  # pragma: no cover
        return TaskDefinition.make_one(self.boto3_raw_data["taskDefinition"])

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RegisterTaskDefinitionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterTaskDefinitionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceConnectServiceOutput:
    boto3_raw_data: "type_defs.ServiceConnectServiceOutputTypeDef" = dataclasses.field()

    portName = field("portName")
    discoveryName = field("discoveryName")

    @cached_property
    def clientAliases(self):  # pragma: no cover
        return ServiceConnectClientAlias.make_many(self.boto3_raw_data["clientAliases"])

    ingressPortOverride = field("ingressPortOverride")

    @cached_property
    def timeout(self):  # pragma: no cover
        return TimeoutConfiguration.make_one(self.boto3_raw_data["timeout"])

    @cached_property
    def tls(self):  # pragma: no cover
        return ServiceConnectTlsConfiguration.make_one(self.boto3_raw_data["tls"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ServiceConnectServiceOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceConnectServiceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceConnectService:
    boto3_raw_data: "type_defs.ServiceConnectServiceTypeDef" = dataclasses.field()

    portName = field("portName")
    discoveryName = field("discoveryName")

    @cached_property
    def clientAliases(self):  # pragma: no cover
        return ServiceConnectClientAlias.make_many(self.boto3_raw_data["clientAliases"])

    ingressPortOverride = field("ingressPortOverride")

    @cached_property
    def timeout(self):  # pragma: no cover
        return TimeoutConfiguration.make_one(self.boto3_raw_data["timeout"])

    @cached_property
    def tls(self):  # pragma: no cover
        return ServiceConnectTlsConfiguration.make_one(self.boto3_raw_data["tls"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ServiceConnectServiceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceConnectServiceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContainerDefinition:
    boto3_raw_data: "type_defs.ContainerDefinitionTypeDef" = dataclasses.field()

    name = field("name")
    image = field("image")

    @cached_property
    def repositoryCredentials(self):  # pragma: no cover
        return RepositoryCredentials.make_one(
            self.boto3_raw_data["repositoryCredentials"]
        )

    cpu = field("cpu")
    memory = field("memory")
    memoryReservation = field("memoryReservation")
    links = field("links")

    @cached_property
    def portMappings(self):  # pragma: no cover
        return PortMapping.make_many(self.boto3_raw_data["portMappings"])

    essential = field("essential")
    restartPolicy = field("restartPolicy")
    entryPoint = field("entryPoint")
    command = field("command")

    @cached_property
    def environment(self):  # pragma: no cover
        return KeyValuePair.make_many(self.boto3_raw_data["environment"])

    @cached_property
    def environmentFiles(self):  # pragma: no cover
        return EnvironmentFile.make_many(self.boto3_raw_data["environmentFiles"])

    @cached_property
    def mountPoints(self):  # pragma: no cover
        return MountPoint.make_many(self.boto3_raw_data["mountPoints"])

    @cached_property
    def volumesFrom(self):  # pragma: no cover
        return VolumeFrom.make_many(self.boto3_raw_data["volumesFrom"])

    linuxParameters = field("linuxParameters")

    @cached_property
    def secrets(self):  # pragma: no cover
        return Secret.make_many(self.boto3_raw_data["secrets"])

    @cached_property
    def dependsOn(self):  # pragma: no cover
        return ContainerDependency.make_many(self.boto3_raw_data["dependsOn"])

    startTimeout = field("startTimeout")
    stopTimeout = field("stopTimeout")
    versionConsistency = field("versionConsistency")
    hostname = field("hostname")
    user = field("user")
    workingDirectory = field("workingDirectory")
    disableNetworking = field("disableNetworking")
    privileged = field("privileged")
    readonlyRootFilesystem = field("readonlyRootFilesystem")
    dnsServers = field("dnsServers")
    dnsSearchDomains = field("dnsSearchDomains")

    @cached_property
    def extraHosts(self):  # pragma: no cover
        return HostEntry.make_many(self.boto3_raw_data["extraHosts"])

    dockerSecurityOptions = field("dockerSecurityOptions")
    interactive = field("interactive")
    pseudoTerminal = field("pseudoTerminal")
    dockerLabels = field("dockerLabels")

    @cached_property
    def ulimits(self):  # pragma: no cover
        return Ulimit.make_many(self.boto3_raw_data["ulimits"])

    logConfiguration = field("logConfiguration")
    healthCheck = field("healthCheck")

    @cached_property
    def systemControls(self):  # pragma: no cover
        return SystemControl.make_many(self.boto3_raw_data["systemControls"])

    @cached_property
    def resourceRequirements(self):  # pragma: no cover
        return ResourceRequirement.make_many(
            self.boto3_raw_data["resourceRequirements"]
        )

    firelensConfiguration = field("firelensConfiguration")
    credentialSpecs = field("credentialSpecs")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContainerDefinitionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContainerDefinitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceVolumeConfiguration:
    boto3_raw_data: "type_defs.ServiceVolumeConfigurationTypeDef" = dataclasses.field()

    name = field("name")
    managedEBSVolume = field("managedEBSVolume")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ServiceVolumeConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceVolumeConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RunTaskRequest:
    boto3_raw_data: "type_defs.RunTaskRequestTypeDef" = dataclasses.field()

    taskDefinition = field("taskDefinition")

    @cached_property
    def capacityProviderStrategy(self):  # pragma: no cover
        return CapacityProviderStrategyItem.make_many(
            self.boto3_raw_data["capacityProviderStrategy"]
        )

    cluster = field("cluster")
    count = field("count")
    enableECSManagedTags = field("enableECSManagedTags")
    enableExecuteCommand = field("enableExecuteCommand")
    group = field("group")
    launchType = field("launchType")
    networkConfiguration = field("networkConfiguration")
    overrides = field("overrides")

    @cached_property
    def placementConstraints(self):  # pragma: no cover
        return PlacementConstraint.make_many(
            self.boto3_raw_data["placementConstraints"]
        )

    @cached_property
    def placementStrategy(self):  # pragma: no cover
        return PlacementStrategy.make_many(self.boto3_raw_data["placementStrategy"])

    platformVersion = field("platformVersion")
    propagateTags = field("propagateTags")
    referenceId = field("referenceId")
    startedBy = field("startedBy")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    clientToken = field("clientToken")

    @cached_property
    def volumeConfigurations(self):  # pragma: no cover
        return TaskVolumeConfiguration.make_many(
            self.boto3_raw_data["volumeConfigurations"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RunTaskRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RunTaskRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartTaskRequest:
    boto3_raw_data: "type_defs.StartTaskRequestTypeDef" = dataclasses.field()

    containerInstances = field("containerInstances")
    taskDefinition = field("taskDefinition")
    cluster = field("cluster")
    enableECSManagedTags = field("enableECSManagedTags")
    enableExecuteCommand = field("enableExecuteCommand")
    group = field("group")
    networkConfiguration = field("networkConfiguration")
    overrides = field("overrides")
    propagateTags = field("propagateTags")
    referenceId = field("referenceId")
    startedBy = field("startedBy")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @cached_property
    def volumeConfigurations(self):  # pragma: no cover
        return TaskVolumeConfiguration.make_many(
            self.boto3_raw_data["volumeConfigurations"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StartTaskRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartTaskRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceConnectConfigurationOutput:
    boto3_raw_data: "type_defs.ServiceConnectConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    enabled = field("enabled")
    namespace = field("namespace")

    @cached_property
    def services(self):  # pragma: no cover
        return ServiceConnectServiceOutput.make_many(self.boto3_raw_data["services"])

    @cached_property
    def logConfiguration(self):  # pragma: no cover
        return LogConfigurationOutput.make_one(self.boto3_raw_data["logConfiguration"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ServiceConnectConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceConnectConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceConnectConfiguration:
    boto3_raw_data: "type_defs.ServiceConnectConfigurationTypeDef" = dataclasses.field()

    enabled = field("enabled")
    namespace = field("namespace")

    @cached_property
    def services(self):  # pragma: no cover
        return ServiceConnectService.make_many(self.boto3_raw_data["services"])

    @cached_property
    def logConfiguration(self):  # pragma: no cover
        return LogConfiguration.make_one(self.boto3_raw_data["logConfiguration"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ServiceConnectConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceConnectConfigurationTypeDef"]
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
    status = field("status")
    taskDefinition = field("taskDefinition")
    desiredCount = field("desiredCount")
    pendingCount = field("pendingCount")
    runningCount = field("runningCount")
    failedTasks = field("failedTasks")
    createdAt = field("createdAt")
    updatedAt = field("updatedAt")

    @cached_property
    def capacityProviderStrategy(self):  # pragma: no cover
        return CapacityProviderStrategyItem.make_many(
            self.boto3_raw_data["capacityProviderStrategy"]
        )

    launchType = field("launchType")
    platformVersion = field("platformVersion")
    platformFamily = field("platformFamily")

    @cached_property
    def networkConfiguration(self):  # pragma: no cover
        return NetworkConfigurationOutput.make_one(
            self.boto3_raw_data["networkConfiguration"]
        )

    rolloutState = field("rolloutState")
    rolloutStateReason = field("rolloutStateReason")

    @cached_property
    def serviceConnectConfiguration(self):  # pragma: no cover
        return ServiceConnectConfigurationOutput.make_one(
            self.boto3_raw_data["serviceConnectConfiguration"]
        )

    @cached_property
    def serviceConnectResources(self):  # pragma: no cover
        return ServiceConnectServiceResource.make_many(
            self.boto3_raw_data["serviceConnectResources"]
        )

    @cached_property
    def volumeConfigurations(self):  # pragma: no cover
        return ServiceVolumeConfigurationOutput.make_many(
            self.boto3_raw_data["volumeConfigurations"]
        )

    @cached_property
    def fargateEphemeralStorage(self):  # pragma: no cover
        return DeploymentEphemeralStorage.make_one(
            self.boto3_raw_data["fargateEphemeralStorage"]
        )

    @cached_property
    def vpcLatticeConfigurations(self):  # pragma: no cover
        return VpcLatticeConfiguration.make_many(
            self.boto3_raw_data["vpcLatticeConfigurations"]
        )

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
class ServiceRevision:
    boto3_raw_data: "type_defs.ServiceRevisionTypeDef" = dataclasses.field()

    serviceRevisionArn = field("serviceRevisionArn")
    serviceArn = field("serviceArn")
    clusterArn = field("clusterArn")
    taskDefinition = field("taskDefinition")

    @cached_property
    def capacityProviderStrategy(self):  # pragma: no cover
        return CapacityProviderStrategyItem.make_many(
            self.boto3_raw_data["capacityProviderStrategy"]
        )

    launchType = field("launchType")
    platformVersion = field("platformVersion")
    platformFamily = field("platformFamily")

    @cached_property
    def loadBalancers(self):  # pragma: no cover
        return LoadBalancer.make_many(self.boto3_raw_data["loadBalancers"])

    @cached_property
    def serviceRegistries(self):  # pragma: no cover
        return ServiceRegistry.make_many(self.boto3_raw_data["serviceRegistries"])

    @cached_property
    def networkConfiguration(self):  # pragma: no cover
        return NetworkConfigurationOutput.make_one(
            self.boto3_raw_data["networkConfiguration"]
        )

    @cached_property
    def containerImages(self):  # pragma: no cover
        return ContainerImage.make_many(self.boto3_raw_data["containerImages"])

    guardDutyEnabled = field("guardDutyEnabled")

    @cached_property
    def serviceConnectConfiguration(self):  # pragma: no cover
        return ServiceConnectConfigurationOutput.make_one(
            self.boto3_raw_data["serviceConnectConfiguration"]
        )

    @cached_property
    def volumeConfigurations(self):  # pragma: no cover
        return ServiceVolumeConfigurationOutput.make_many(
            self.boto3_raw_data["volumeConfigurations"]
        )

    @cached_property
    def fargateEphemeralStorage(self):  # pragma: no cover
        return DeploymentEphemeralStorage.make_one(
            self.boto3_raw_data["fargateEphemeralStorage"]
        )

    createdAt = field("createdAt")

    @cached_property
    def vpcLatticeConfigurations(self):  # pragma: no cover
        return VpcLatticeConfiguration.make_many(
            self.boto3_raw_data["vpcLatticeConfigurations"]
        )

    @cached_property
    def resolvedConfiguration(self):  # pragma: no cover
        return ResolvedConfiguration.make_one(
            self.boto3_raw_data["resolvedConfiguration"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ServiceRevisionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ServiceRevisionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterTaskDefinitionRequest:
    boto3_raw_data: "type_defs.RegisterTaskDefinitionRequestTypeDef" = (
        dataclasses.field()
    )

    family = field("family")
    containerDefinitions = field("containerDefinitions")
    taskRoleArn = field("taskRoleArn")
    executionRoleArn = field("executionRoleArn")
    networkMode = field("networkMode")
    volumes = field("volumes")

    @cached_property
    def placementConstraints(self):  # pragma: no cover
        return TaskDefinitionPlacementConstraint.make_many(
            self.boto3_raw_data["placementConstraints"]
        )

    requiresCompatibilities = field("requiresCompatibilities")
    cpu = field("cpu")
    memory = field("memory")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    pidMode = field("pidMode")
    ipcMode = field("ipcMode")
    proxyConfiguration = field("proxyConfiguration")

    @cached_property
    def inferenceAccelerators(self):  # pragma: no cover
        return InferenceAccelerator.make_many(
            self.boto3_raw_data["inferenceAccelerators"]
        )

    @cached_property
    def ephemeralStorage(self):  # pragma: no cover
        return EphemeralStorage.make_one(self.boto3_raw_data["ephemeralStorage"])

    @cached_property
    def runtimePlatform(self):  # pragma: no cover
        return RuntimePlatform.make_one(self.boto3_raw_data["runtimePlatform"])

    enableFaultInjection = field("enableFaultInjection")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RegisterTaskDefinitionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterTaskDefinitionRequestTypeDef"]
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

    serviceArn = field("serviceArn")
    serviceName = field("serviceName")
    clusterArn = field("clusterArn")

    @cached_property
    def loadBalancers(self):  # pragma: no cover
        return LoadBalancer.make_many(self.boto3_raw_data["loadBalancers"])

    @cached_property
    def serviceRegistries(self):  # pragma: no cover
        return ServiceRegistry.make_many(self.boto3_raw_data["serviceRegistries"])

    status = field("status")
    desiredCount = field("desiredCount")
    runningCount = field("runningCount")
    pendingCount = field("pendingCount")
    launchType = field("launchType")

    @cached_property
    def capacityProviderStrategy(self):  # pragma: no cover
        return CapacityProviderStrategyItem.make_many(
            self.boto3_raw_data["capacityProviderStrategy"]
        )

    platformVersion = field("platformVersion")
    platformFamily = field("platformFamily")
    taskDefinition = field("taskDefinition")

    @cached_property
    def deploymentConfiguration(self):  # pragma: no cover
        return DeploymentConfigurationOutput.make_one(
            self.boto3_raw_data["deploymentConfiguration"]
        )

    @cached_property
    def taskSets(self):  # pragma: no cover
        return TaskSet.make_many(self.boto3_raw_data["taskSets"])

    @cached_property
    def deployments(self):  # pragma: no cover
        return Deployment.make_many(self.boto3_raw_data["deployments"])

    roleArn = field("roleArn")

    @cached_property
    def events(self):  # pragma: no cover
        return ServiceEvent.make_many(self.boto3_raw_data["events"])

    createdAt = field("createdAt")

    @cached_property
    def placementConstraints(self):  # pragma: no cover
        return PlacementConstraint.make_many(
            self.boto3_raw_data["placementConstraints"]
        )

    @cached_property
    def placementStrategy(self):  # pragma: no cover
        return PlacementStrategy.make_many(self.boto3_raw_data["placementStrategy"])

    @cached_property
    def networkConfiguration(self):  # pragma: no cover
        return NetworkConfigurationOutput.make_one(
            self.boto3_raw_data["networkConfiguration"]
        )

    healthCheckGracePeriodSeconds = field("healthCheckGracePeriodSeconds")
    schedulingStrategy = field("schedulingStrategy")

    @cached_property
    def deploymentController(self):  # pragma: no cover
        return DeploymentController.make_one(
            self.boto3_raw_data["deploymentController"]
        )

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    createdBy = field("createdBy")
    enableECSManagedTags = field("enableECSManagedTags")
    propagateTags = field("propagateTags")
    enableExecuteCommand = field("enableExecuteCommand")
    availabilityZoneRebalancing = field("availabilityZoneRebalancing")

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
class DescribeServiceRevisionsResponse:
    boto3_raw_data: "type_defs.DescribeServiceRevisionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def serviceRevisions(self):  # pragma: no cover
        return ServiceRevision.make_many(self.boto3_raw_data["serviceRevisions"])

    @cached_property
    def failures(self):  # pragma: no cover
        return Failure.make_many(self.boto3_raw_data["failures"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeServiceRevisionsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeServiceRevisionsResponseTypeDef"]
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

    serviceName = field("serviceName")
    cluster = field("cluster")
    taskDefinition = field("taskDefinition")
    availabilityZoneRebalancing = field("availabilityZoneRebalancing")

    @cached_property
    def loadBalancers(self):  # pragma: no cover
        return LoadBalancer.make_many(self.boto3_raw_data["loadBalancers"])

    @cached_property
    def serviceRegistries(self):  # pragma: no cover
        return ServiceRegistry.make_many(self.boto3_raw_data["serviceRegistries"])

    desiredCount = field("desiredCount")
    clientToken = field("clientToken")
    launchType = field("launchType")

    @cached_property
    def capacityProviderStrategy(self):  # pragma: no cover
        return CapacityProviderStrategyItem.make_many(
            self.boto3_raw_data["capacityProviderStrategy"]
        )

    platformVersion = field("platformVersion")
    role = field("role")
    deploymentConfiguration = field("deploymentConfiguration")

    @cached_property
    def placementConstraints(self):  # pragma: no cover
        return PlacementConstraint.make_many(
            self.boto3_raw_data["placementConstraints"]
        )

    @cached_property
    def placementStrategy(self):  # pragma: no cover
        return PlacementStrategy.make_many(self.boto3_raw_data["placementStrategy"])

    networkConfiguration = field("networkConfiguration")
    healthCheckGracePeriodSeconds = field("healthCheckGracePeriodSeconds")
    schedulingStrategy = field("schedulingStrategy")

    @cached_property
    def deploymentController(self):  # pragma: no cover
        return DeploymentController.make_one(
            self.boto3_raw_data["deploymentController"]
        )

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    enableECSManagedTags = field("enableECSManagedTags")
    propagateTags = field("propagateTags")
    enableExecuteCommand = field("enableExecuteCommand")
    serviceConnectConfiguration = field("serviceConnectConfiguration")
    volumeConfigurations = field("volumeConfigurations")

    @cached_property
    def vpcLatticeConfigurations(self):  # pragma: no cover
        return VpcLatticeConfiguration.make_many(
            self.boto3_raw_data["vpcLatticeConfigurations"]
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

    service = field("service")
    cluster = field("cluster")
    desiredCount = field("desiredCount")
    taskDefinition = field("taskDefinition")

    @cached_property
    def capacityProviderStrategy(self):  # pragma: no cover
        return CapacityProviderStrategyItem.make_many(
            self.boto3_raw_data["capacityProviderStrategy"]
        )

    deploymentConfiguration = field("deploymentConfiguration")
    availabilityZoneRebalancing = field("availabilityZoneRebalancing")
    networkConfiguration = field("networkConfiguration")

    @cached_property
    def placementConstraints(self):  # pragma: no cover
        return PlacementConstraint.make_many(
            self.boto3_raw_data["placementConstraints"]
        )

    @cached_property
    def placementStrategy(self):  # pragma: no cover
        return PlacementStrategy.make_many(self.boto3_raw_data["placementStrategy"])

    platformVersion = field("platformVersion")
    forceNewDeployment = field("forceNewDeployment")
    healthCheckGracePeriodSeconds = field("healthCheckGracePeriodSeconds")

    @cached_property
    def deploymentController(self):  # pragma: no cover
        return DeploymentController.make_one(
            self.boto3_raw_data["deploymentController"]
        )

    enableExecuteCommand = field("enableExecuteCommand")
    enableECSManagedTags = field("enableECSManagedTags")

    @cached_property
    def loadBalancers(self):  # pragma: no cover
        return LoadBalancer.make_many(self.boto3_raw_data["loadBalancers"])

    propagateTags = field("propagateTags")

    @cached_property
    def serviceRegistries(self):  # pragma: no cover
        return ServiceRegistry.make_many(self.boto3_raw_data["serviceRegistries"])

    serviceConnectConfiguration = field("serviceConnectConfiguration")
    volumeConfigurations = field("volumeConfigurations")

    @cached_property
    def vpcLatticeConfigurations(self):  # pragma: no cover
        return VpcLatticeConfiguration.make_many(
            self.boto3_raw_data["vpcLatticeConfigurations"]
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


@dataclasses.dataclass(frozen=True)
class CreateServiceResponse:
    boto3_raw_data: "type_defs.CreateServiceResponseTypeDef" = dataclasses.field()

    @cached_property
    def service(self):  # pragma: no cover
        return Service.make_one(self.boto3_raw_data["service"])

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
    def service(self):  # pragma: no cover
        return Service.make_one(self.boto3_raw_data["service"])

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
class DescribeServicesResponse:
    boto3_raw_data: "type_defs.DescribeServicesResponseTypeDef" = dataclasses.field()

    @cached_property
    def services(self):  # pragma: no cover
        return Service.make_many(self.boto3_raw_data["services"])

    @cached_property
    def failures(self):  # pragma: no cover
        return Failure.make_many(self.boto3_raw_data["failures"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeServicesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeServicesResponseTypeDef"]
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
    def service(self):  # pragma: no cover
        return Service.make_one(self.boto3_raw_data["service"])

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
