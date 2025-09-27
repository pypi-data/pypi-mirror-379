# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_batch import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class ArrayPropertiesDetail:
    boto3_raw_data: "type_defs.ArrayPropertiesDetailTypeDef" = dataclasses.field()

    statusSummary = field("statusSummary")
    size = field("size")
    index = field("index")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ArrayPropertiesDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ArrayPropertiesDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ArrayPropertiesSummary:
    boto3_raw_data: "type_defs.ArrayPropertiesSummaryTypeDef" = dataclasses.field()

    size = field("size")
    index = field("index")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ArrayPropertiesSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ArrayPropertiesSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ArrayProperties:
    boto3_raw_data: "type_defs.ArrayPropertiesTypeDef" = dataclasses.field()

    size = field("size")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ArrayPropertiesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ArrayPropertiesTypeDef"]],
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
    ipv6Address = field("ipv6Address")
    privateIpv4Address = field("privateIpv4Address")

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
class CancelJobRequest:
    boto3_raw_data: "type_defs.CancelJobRequestTypeDef" = dataclasses.field()

    jobId = field("jobId")
    reason = field("reason")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CancelJobRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CapacityLimit:
    boto3_raw_data: "type_defs.CapacityLimitTypeDef" = dataclasses.field()

    maxCapacity = field("maxCapacity")
    capacityUnit = field("capacityUnit")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CapacityLimitTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CapacityLimitTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EksConfiguration:
    boto3_raw_data: "type_defs.EksConfigurationTypeDef" = dataclasses.field()

    eksClusterArn = field("eksClusterArn")
    kubernetesNamespace = field("kubernetesNamespace")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EksConfigurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EksConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePolicy:
    boto3_raw_data: "type_defs.UpdatePolicyTypeDef" = dataclasses.field()

    terminateJobsOnUpdate = field("terminateJobsOnUpdate")
    jobExecutionTimeoutMinutes = field("jobExecutionTimeoutMinutes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdatePolicyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UpdatePolicyTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComputeEnvironmentOrder:
    boto3_raw_data: "type_defs.ComputeEnvironmentOrderTypeDef" = dataclasses.field()

    order = field("order")
    computeEnvironment = field("computeEnvironment")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ComputeEnvironmentOrderTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComputeEnvironmentOrderTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Ec2Configuration:
    boto3_raw_data: "type_defs.Ec2ConfigurationTypeDef" = dataclasses.field()

    imageType = field("imageType")
    imageIdOverride = field("imageIdOverride")
    imageKubernetesVersion = field("imageKubernetesVersion")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.Ec2ConfigurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.Ec2ConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConsumableResourceRequirement:
    boto3_raw_data: "type_defs.ConsumableResourceRequirementTypeDef" = (
        dataclasses.field()
    )

    consumableResource = field("consumableResource")
    quantity = field("quantity")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ConsumableResourceRequirementTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConsumableResourceRequirementTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConsumableResourceSummary:
    boto3_raw_data: "type_defs.ConsumableResourceSummaryTypeDef" = dataclasses.field()

    consumableResourceArn = field("consumableResourceArn")
    consumableResourceName = field("consumableResourceName")
    totalQuantity = field("totalQuantity")
    inUseQuantity = field("inUseQuantity")
    resourceType = field("resourceType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConsumableResourceSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConsumableResourceSummaryTypeDef"]
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
class FargatePlatformConfiguration:
    boto3_raw_data: "type_defs.FargatePlatformConfigurationTypeDef" = (
        dataclasses.field()
    )

    platformVersion = field("platformVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FargatePlatformConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FargatePlatformConfigurationTypeDef"]
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
class MountPoint:
    boto3_raw_data: "type_defs.MountPointTypeDef" = dataclasses.field()

    containerPath = field("containerPath")
    readOnly = field("readOnly")
    sourceVolume = field("sourceVolume")

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
class NetworkConfiguration:
    boto3_raw_data: "type_defs.NetworkConfigurationTypeDef" = dataclasses.field()

    assignPublicIp = field("assignPublicIp")

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
class RuntimePlatform:
    boto3_raw_data: "type_defs.RuntimePlatformTypeDef" = dataclasses.field()

    operatingSystemFamily = field("operatingSystemFamily")
    cpuArchitecture = field("cpuArchitecture")

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
class Ulimit:
    boto3_raw_data: "type_defs.UlimitTypeDef" = dataclasses.field()

    hardLimit = field("hardLimit")
    name = field("name")
    softLimit = field("softLimit")

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
class ContainerSummary:
    boto3_raw_data: "type_defs.ContainerSummaryTypeDef" = dataclasses.field()

    exitCode = field("exitCode")
    reason = field("reason")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ContainerSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContainerSummaryTypeDef"]
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
class CreateConsumableResourceRequest:
    boto3_raw_data: "type_defs.CreateConsumableResourceRequestTypeDef" = (
        dataclasses.field()
    )

    consumableResourceName = field("consumableResourceName")
    totalQuantity = field("totalQuantity")
    resourceType = field("resourceType")
    tags = field("tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateConsumableResourceRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateConsumableResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobStateTimeLimitAction:
    boto3_raw_data: "type_defs.JobStateTimeLimitActionTypeDef" = dataclasses.field()

    reason = field("reason")
    state = field("state")
    maxTimeSeconds = field("maxTimeSeconds")
    action = field("action")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.JobStateTimeLimitActionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JobStateTimeLimitActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceEnvironmentOrder:
    boto3_raw_data: "type_defs.ServiceEnvironmentOrderTypeDef" = dataclasses.field()

    order = field("order")
    serviceEnvironment = field("serviceEnvironment")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ServiceEnvironmentOrderTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceEnvironmentOrderTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteComputeEnvironmentRequest:
    boto3_raw_data: "type_defs.DeleteComputeEnvironmentRequestTypeDef" = (
        dataclasses.field()
    )

    computeEnvironment = field("computeEnvironment")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteComputeEnvironmentRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteComputeEnvironmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteConsumableResourceRequest:
    boto3_raw_data: "type_defs.DeleteConsumableResourceRequestTypeDef" = (
        dataclasses.field()
    )

    consumableResource = field("consumableResource")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteConsumableResourceRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteConsumableResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteJobQueueRequest:
    boto3_raw_data: "type_defs.DeleteJobQueueRequestTypeDef" = dataclasses.field()

    jobQueue = field("jobQueue")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteJobQueueRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteJobQueueRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSchedulingPolicyRequest:
    boto3_raw_data: "type_defs.DeleteSchedulingPolicyRequestTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteSchedulingPolicyRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSchedulingPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteServiceEnvironmentRequest:
    boto3_raw_data: "type_defs.DeleteServiceEnvironmentRequestTypeDef" = (
        dataclasses.field()
    )

    serviceEnvironment = field("serviceEnvironment")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteServiceEnvironmentRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteServiceEnvironmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeregisterJobDefinitionRequest:
    boto3_raw_data: "type_defs.DeregisterJobDefinitionRequestTypeDef" = (
        dataclasses.field()
    )

    jobDefinition = field("jobDefinition")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeregisterJobDefinitionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeregisterJobDefinitionRequestTypeDef"]
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
class DescribeComputeEnvironmentsRequest:
    boto3_raw_data: "type_defs.DescribeComputeEnvironmentsRequestTypeDef" = (
        dataclasses.field()
    )

    computeEnvironments = field("computeEnvironments")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeComputeEnvironmentsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeComputeEnvironmentsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeConsumableResourceRequest:
    boto3_raw_data: "type_defs.DescribeConsumableResourceRequestTypeDef" = (
        dataclasses.field()
    )

    consumableResource = field("consumableResource")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeConsumableResourceRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeConsumableResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeJobDefinitionsRequest:
    boto3_raw_data: "type_defs.DescribeJobDefinitionsRequestTypeDef" = (
        dataclasses.field()
    )

    jobDefinitions = field("jobDefinitions")
    maxResults = field("maxResults")
    jobDefinitionName = field("jobDefinitionName")
    status = field("status")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeJobDefinitionsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeJobDefinitionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeJobQueuesRequest:
    boto3_raw_data: "type_defs.DescribeJobQueuesRequestTypeDef" = dataclasses.field()

    jobQueues = field("jobQueues")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeJobQueuesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeJobQueuesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeJobsRequest:
    boto3_raw_data: "type_defs.DescribeJobsRequestTypeDef" = dataclasses.field()

    jobs = field("jobs")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeJobsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSchedulingPoliciesRequest:
    boto3_raw_data: "type_defs.DescribeSchedulingPoliciesRequestTypeDef" = (
        dataclasses.field()
    )

    arns = field("arns")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeSchedulingPoliciesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSchedulingPoliciesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeServiceEnvironmentsRequest:
    boto3_raw_data: "type_defs.DescribeServiceEnvironmentsRequestTypeDef" = (
        dataclasses.field()
    )

    serviceEnvironments = field("serviceEnvironments")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeServiceEnvironmentsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeServiceEnvironmentsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeServiceJobRequest:
    boto3_raw_data: "type_defs.DescribeServiceJobRequestTypeDef" = dataclasses.field()

    jobId = field("jobId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeServiceJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeServiceJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceJobTimeout:
    boto3_raw_data: "type_defs.ServiceJobTimeoutTypeDef" = dataclasses.field()

    attemptDurationSeconds = field("attemptDurationSeconds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ServiceJobTimeoutTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceJobTimeoutTypeDef"]
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
class EksAttemptContainerDetail:
    boto3_raw_data: "type_defs.EksAttemptContainerDetailTypeDef" = dataclasses.field()

    name = field("name")
    containerID = field("containerID")
    exitCode = field("exitCode")
    reason = field("reason")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EksAttemptContainerDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EksAttemptContainerDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EksContainerEnvironmentVariable:
    boto3_raw_data: "type_defs.EksContainerEnvironmentVariableTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    value = field("value")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.EksContainerEnvironmentVariableTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EksContainerEnvironmentVariableTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EksContainerResourceRequirementsOutput:
    boto3_raw_data: "type_defs.EksContainerResourceRequirementsOutputTypeDef" = (
        dataclasses.field()
    )

    limits = field("limits")
    requests = field("requests")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.EksContainerResourceRequirementsOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EksContainerResourceRequirementsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EksContainerSecurityContext:
    boto3_raw_data: "type_defs.EksContainerSecurityContextTypeDef" = dataclasses.field()

    runAsUser = field("runAsUser")
    runAsGroup = field("runAsGroup")
    privileged = field("privileged")
    allowPrivilegeEscalation = field("allowPrivilegeEscalation")
    readOnlyRootFilesystem = field("readOnlyRootFilesystem")
    runAsNonRoot = field("runAsNonRoot")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EksContainerSecurityContextTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EksContainerSecurityContextTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EksContainerVolumeMount:
    boto3_raw_data: "type_defs.EksContainerVolumeMountTypeDef" = dataclasses.field()

    name = field("name")
    mountPath = field("mountPath")
    subPath = field("subPath")
    readOnly = field("readOnly")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EksContainerVolumeMountTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EksContainerVolumeMountTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EksContainerResourceRequirements:
    boto3_raw_data: "type_defs.EksContainerResourceRequirementsTypeDef" = (
        dataclasses.field()
    )

    limits = field("limits")
    requests = field("requests")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.EksContainerResourceRequirementsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EksContainerResourceRequirementsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EksEmptyDir:
    boto3_raw_data: "type_defs.EksEmptyDirTypeDef" = dataclasses.field()

    medium = field("medium")
    sizeLimit = field("sizeLimit")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EksEmptyDirTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EksEmptyDirTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EksHostPath:
    boto3_raw_data: "type_defs.EksHostPathTypeDef" = dataclasses.field()

    path = field("path")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EksHostPathTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EksHostPathTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EksMetadataOutput:
    boto3_raw_data: "type_defs.EksMetadataOutputTypeDef" = dataclasses.field()

    labels = field("labels")
    annotations = field("annotations")
    namespace = field("namespace")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EksMetadataOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EksMetadataOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EksMetadata:
    boto3_raw_data: "type_defs.EksMetadataTypeDef" = dataclasses.field()

    labels = field("labels")
    annotations = field("annotations")
    namespace = field("namespace")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EksMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EksMetadataTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EksPersistentVolumeClaim:
    boto3_raw_data: "type_defs.EksPersistentVolumeClaimTypeDef" = dataclasses.field()

    claimName = field("claimName")
    readOnly = field("readOnly")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EksPersistentVolumeClaimTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EksPersistentVolumeClaimTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImagePullSecret:
    boto3_raw_data: "type_defs.ImagePullSecretTypeDef" = dataclasses.field()

    name = field("name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImagePullSecretTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ImagePullSecretTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EksSecret:
    boto3_raw_data: "type_defs.EksSecretTypeDef" = dataclasses.field()

    secretName = field("secretName")
    optional = field("optional")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EksSecretTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EksSecretTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvaluateOnExit:
    boto3_raw_data: "type_defs.EvaluateOnExitTypeDef" = dataclasses.field()

    action = field("action")
    onStatusReason = field("onStatusReason")
    onReason = field("onReason")
    onExitCode = field("onExitCode")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EvaluateOnExitTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EvaluateOnExitTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ShareAttributes:
    boto3_raw_data: "type_defs.ShareAttributesTypeDef" = dataclasses.field()

    shareIdentifier = field("shareIdentifier")
    weightFactor = field("weightFactor")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ShareAttributesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ShareAttributesTypeDef"]],
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
class FrontOfQueueJobSummary:
    boto3_raw_data: "type_defs.FrontOfQueueJobSummaryTypeDef" = dataclasses.field()

    jobArn = field("jobArn")
    earliestTimeAtPosition = field("earliestTimeAtPosition")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FrontOfQueueJobSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FrontOfQueueJobSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetJobQueueSnapshotRequest:
    boto3_raw_data: "type_defs.GetJobQueueSnapshotRequestTypeDef" = dataclasses.field()

    jobQueue = field("jobQueue")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetJobQueueSnapshotRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetJobQueueSnapshotRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Host:
    boto3_raw_data: "type_defs.HostTypeDef" = dataclasses.field()

    sourcePath = field("sourcePath")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HostTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.HostTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobTimeout:
    boto3_raw_data: "type_defs.JobTimeoutTypeDef" = dataclasses.field()

    attemptDurationSeconds = field("attemptDurationSeconds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobTimeoutTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JobTimeoutTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobDependency:
    boto3_raw_data: "type_defs.JobDependencyTypeDef" = dataclasses.field()

    jobId = field("jobId")
    type = field("type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobDependencyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JobDependencyTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NodeDetails:
    boto3_raw_data: "type_defs.NodeDetailsTypeDef" = dataclasses.field()

    nodeIndex = field("nodeIndex")
    isMainNode = field("isMainNode")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NodeDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.NodeDetailsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NodePropertiesSummary:
    boto3_raw_data: "type_defs.NodePropertiesSummaryTypeDef" = dataclasses.field()

    isMainNode = field("isMainNode")
    numNodes = field("numNodes")
    nodeIndex = field("nodeIndex")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NodePropertiesSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NodePropertiesSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KeyValuesPair:
    boto3_raw_data: "type_defs.KeyValuesPairTypeDef" = dataclasses.field()

    name = field("name")
    values = field("values")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.KeyValuesPairTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.KeyValuesPairTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceResourceId:
    boto3_raw_data: "type_defs.ServiceResourceIdTypeDef" = dataclasses.field()

    name = field("name")
    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ServiceResourceIdTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceResourceIdTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LaunchTemplateSpecificationOverrideOutput:
    boto3_raw_data: "type_defs.LaunchTemplateSpecificationOverrideOutputTypeDef" = (
        dataclasses.field()
    )

    launchTemplateId = field("launchTemplateId")
    launchTemplateName = field("launchTemplateName")
    version = field("version")
    targetInstanceTypes = field("targetInstanceTypes")
    userdataType = field("userdataType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.LaunchTemplateSpecificationOverrideOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LaunchTemplateSpecificationOverrideOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LaunchTemplateSpecificationOverride:
    boto3_raw_data: "type_defs.LaunchTemplateSpecificationOverrideTypeDef" = (
        dataclasses.field()
    )

    launchTemplateId = field("launchTemplateId")
    launchTemplateName = field("launchTemplateName")
    version = field("version")
    targetInstanceTypes = field("targetInstanceTypes")
    userdataType = field("userdataType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.LaunchTemplateSpecificationOverrideTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LaunchTemplateSpecificationOverrideTypeDef"]
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
class ListSchedulingPoliciesRequest:
    boto3_raw_data: "type_defs.ListSchedulingPoliciesRequestTypeDef" = (
        dataclasses.field()
    )

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListSchedulingPoliciesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSchedulingPoliciesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SchedulingPolicyListingDetail:
    boto3_raw_data: "type_defs.SchedulingPolicyListingDetailTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SchedulingPolicyListingDetailTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SchedulingPolicyListingDetailTypeDef"]
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
class ServiceJobEvaluateOnExit:
    boto3_raw_data: "type_defs.ServiceJobEvaluateOnExitTypeDef" = dataclasses.field()

    action = field("action")
    onStatusReason = field("onStatusReason")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ServiceJobEvaluateOnExitTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceJobEvaluateOnExitTypeDef"]
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
class TaskContainerDependency:
    boto3_raw_data: "type_defs.TaskContainerDependencyTypeDef" = dataclasses.field()

    containerName = field("containerName")
    condition = field("condition")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TaskContainerDependencyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TaskContainerDependencyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TerminateJobRequest:
    boto3_raw_data: "type_defs.TerminateJobRequestTypeDef" = dataclasses.field()

    jobId = field("jobId")
    reason = field("reason")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TerminateJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TerminateJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TerminateServiceJobRequest:
    boto3_raw_data: "type_defs.TerminateServiceJobRequestTypeDef" = dataclasses.field()

    jobId = field("jobId")
    reason = field("reason")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TerminateServiceJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TerminateServiceJobRequestTypeDef"]
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
class UpdateConsumableResourceRequest:
    boto3_raw_data: "type_defs.UpdateConsumableResourceRequestTypeDef" = (
        dataclasses.field()
    )

    consumableResource = field("consumableResource")
    operation = field("operation")
    quantity = field("quantity")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateConsumableResourceRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateConsumableResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttemptContainerDetail:
    boto3_raw_data: "type_defs.AttemptContainerDetailTypeDef" = dataclasses.field()

    containerInstanceArn = field("containerInstanceArn")
    taskArn = field("taskArn")
    exitCode = field("exitCode")
    reason = field("reason")
    logStreamName = field("logStreamName")

    @cached_property
    def networkInterfaces(self):  # pragma: no cover
        return NetworkInterface.make_many(self.boto3_raw_data["networkInterfaces"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AttemptContainerDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttemptContainerDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttemptTaskContainerDetails:
    boto3_raw_data: "type_defs.AttemptTaskContainerDetailsTypeDef" = dataclasses.field()

    exitCode = field("exitCode")
    name = field("name")
    reason = field("reason")
    logStreamName = field("logStreamName")

    @cached_property
    def networkInterfaces(self):  # pragma: no cover
        return NetworkInterface.make_many(self.boto3_raw_data["networkInterfaces"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AttemptTaskContainerDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttemptTaskContainerDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateServiceEnvironmentRequest:
    boto3_raw_data: "type_defs.CreateServiceEnvironmentRequestTypeDef" = (
        dataclasses.field()
    )

    serviceEnvironmentName = field("serviceEnvironmentName")
    serviceEnvironmentType = field("serviceEnvironmentType")

    @cached_property
    def capacityLimits(self):  # pragma: no cover
        return CapacityLimit.make_many(self.boto3_raw_data["capacityLimits"])

    state = field("state")
    tags = field("tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateServiceEnvironmentRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateServiceEnvironmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceEnvironmentDetail:
    boto3_raw_data: "type_defs.ServiceEnvironmentDetailTypeDef" = dataclasses.field()

    serviceEnvironmentName = field("serviceEnvironmentName")
    serviceEnvironmentArn = field("serviceEnvironmentArn")
    serviceEnvironmentType = field("serviceEnvironmentType")

    @cached_property
    def capacityLimits(self):  # pragma: no cover
        return CapacityLimit.make_many(self.boto3_raw_data["capacityLimits"])

    state = field("state")
    status = field("status")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ServiceEnvironmentDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceEnvironmentDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateServiceEnvironmentRequest:
    boto3_raw_data: "type_defs.UpdateServiceEnvironmentRequestTypeDef" = (
        dataclasses.field()
    )

    serviceEnvironment = field("serviceEnvironment")
    state = field("state")

    @cached_property
    def capacityLimits(self):  # pragma: no cover
        return CapacityLimit.make_many(self.boto3_raw_data["capacityLimits"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateServiceEnvironmentRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateServiceEnvironmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConsumableResourcePropertiesOutput:
    boto3_raw_data: "type_defs.ConsumableResourcePropertiesOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def consumableResourceList(self):  # pragma: no cover
        return ConsumableResourceRequirement.make_many(
            self.boto3_raw_data["consumableResourceList"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ConsumableResourcePropertiesOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConsumableResourcePropertiesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConsumableResourceProperties:
    boto3_raw_data: "type_defs.ConsumableResourcePropertiesTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def consumableResourceList(self):  # pragma: no cover
        return ConsumableResourceRequirement.make_many(
            self.boto3_raw_data["consumableResourceList"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConsumableResourcePropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConsumableResourcePropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContainerOverrides:
    boto3_raw_data: "type_defs.ContainerOverridesTypeDef" = dataclasses.field()

    vcpus = field("vcpus")
    memory = field("memory")
    command = field("command")
    instanceType = field("instanceType")

    @cached_property
    def environment(self):  # pragma: no cover
        return KeyValuePair.make_many(self.boto3_raw_data["environment"])

    @cached_property
    def resourceRequirements(self):  # pragma: no cover
        return ResourceRequirement.make_many(
            self.boto3_raw_data["resourceRequirements"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContainerOverridesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContainerOverridesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TaskContainerOverrides:
    boto3_raw_data: "type_defs.TaskContainerOverridesTypeDef" = dataclasses.field()

    command = field("command")

    @cached_property
    def environment(self):  # pragma: no cover
        return KeyValuePair.make_many(self.boto3_raw_data["environment"])

    name = field("name")

    @cached_property
    def resourceRequirements(self):  # pragma: no cover
        return ResourceRequirement.make_many(
            self.boto3_raw_data["resourceRequirements"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TaskContainerOverridesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TaskContainerOverridesTypeDef"]
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
class CreateComputeEnvironmentResponse:
    boto3_raw_data: "type_defs.CreateComputeEnvironmentResponseTypeDef" = (
        dataclasses.field()
    )

    computeEnvironmentName = field("computeEnvironmentName")
    computeEnvironmentArn = field("computeEnvironmentArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateComputeEnvironmentResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateComputeEnvironmentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateConsumableResourceResponse:
    boto3_raw_data: "type_defs.CreateConsumableResourceResponseTypeDef" = (
        dataclasses.field()
    )

    consumableResourceName = field("consumableResourceName")
    consumableResourceArn = field("consumableResourceArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateConsumableResourceResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateConsumableResourceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateJobQueueResponse:
    boto3_raw_data: "type_defs.CreateJobQueueResponseTypeDef" = dataclasses.field()

    jobQueueName = field("jobQueueName")
    jobQueueArn = field("jobQueueArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateJobQueueResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateJobQueueResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSchedulingPolicyResponse:
    boto3_raw_data: "type_defs.CreateSchedulingPolicyResponseTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    arn = field("arn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateSchedulingPolicyResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSchedulingPolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateServiceEnvironmentResponse:
    boto3_raw_data: "type_defs.CreateServiceEnvironmentResponseTypeDef" = (
        dataclasses.field()
    )

    serviceEnvironmentName = field("serviceEnvironmentName")
    serviceEnvironmentArn = field("serviceEnvironmentArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateServiceEnvironmentResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateServiceEnvironmentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeConsumableResourceResponse:
    boto3_raw_data: "type_defs.DescribeConsumableResourceResponseTypeDef" = (
        dataclasses.field()
    )

    consumableResourceName = field("consumableResourceName")
    consumableResourceArn = field("consumableResourceArn")
    totalQuantity = field("totalQuantity")
    inUseQuantity = field("inUseQuantity")
    availableQuantity = field("availableQuantity")
    resourceType = field("resourceType")
    createdAt = field("createdAt")
    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeConsumableResourceResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeConsumableResourceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConsumableResourcesResponse:
    boto3_raw_data: "type_defs.ListConsumableResourcesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def consumableResources(self):  # pragma: no cover
        return ConsumableResourceSummary.make_many(
            self.boto3_raw_data["consumableResources"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListConsumableResourcesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConsumableResourcesResponseTypeDef"]
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
class RegisterJobDefinitionResponse:
    boto3_raw_data: "type_defs.RegisterJobDefinitionResponseTypeDef" = (
        dataclasses.field()
    )

    jobDefinitionName = field("jobDefinitionName")
    jobDefinitionArn = field("jobDefinitionArn")
    revision = field("revision")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RegisterJobDefinitionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterJobDefinitionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SubmitJobResponse:
    boto3_raw_data: "type_defs.SubmitJobResponseTypeDef" = dataclasses.field()

    jobArn = field("jobArn")
    jobName = field("jobName")
    jobId = field("jobId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SubmitJobResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SubmitJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SubmitServiceJobResponse:
    boto3_raw_data: "type_defs.SubmitServiceJobResponseTypeDef" = dataclasses.field()

    jobArn = field("jobArn")
    jobName = field("jobName")
    jobId = field("jobId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SubmitServiceJobResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SubmitServiceJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateComputeEnvironmentResponse:
    boto3_raw_data: "type_defs.UpdateComputeEnvironmentResponseTypeDef" = (
        dataclasses.field()
    )

    computeEnvironmentName = field("computeEnvironmentName")
    computeEnvironmentArn = field("computeEnvironmentArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateComputeEnvironmentResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateComputeEnvironmentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateConsumableResourceResponse:
    boto3_raw_data: "type_defs.UpdateConsumableResourceResponseTypeDef" = (
        dataclasses.field()
    )

    consumableResourceName = field("consumableResourceName")
    consumableResourceArn = field("consumableResourceArn")
    totalQuantity = field("totalQuantity")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateConsumableResourceResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateConsumableResourceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateJobQueueResponse:
    boto3_raw_data: "type_defs.UpdateJobQueueResponseTypeDef" = dataclasses.field()

    jobQueueName = field("jobQueueName")
    jobQueueArn = field("jobQueueArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateJobQueueResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateJobQueueResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateServiceEnvironmentResponse:
    boto3_raw_data: "type_defs.UpdateServiceEnvironmentResponseTypeDef" = (
        dataclasses.field()
    )

    serviceEnvironmentName = field("serviceEnvironmentName")
    serviceEnvironmentArn = field("serviceEnvironmentArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateServiceEnvironmentResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateServiceEnvironmentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateJobQueueRequest:
    boto3_raw_data: "type_defs.CreateJobQueueRequestTypeDef" = dataclasses.field()

    jobQueueName = field("jobQueueName")
    priority = field("priority")
    state = field("state")
    schedulingPolicyArn = field("schedulingPolicyArn")

    @cached_property
    def computeEnvironmentOrder(self):  # pragma: no cover
        return ComputeEnvironmentOrder.make_many(
            self.boto3_raw_data["computeEnvironmentOrder"]
        )

    @cached_property
    def serviceEnvironmentOrder(self):  # pragma: no cover
        return ServiceEnvironmentOrder.make_many(
            self.boto3_raw_data["serviceEnvironmentOrder"]
        )

    jobQueueType = field("jobQueueType")
    tags = field("tags")

    @cached_property
    def jobStateTimeLimitActions(self):  # pragma: no cover
        return JobStateTimeLimitAction.make_many(
            self.boto3_raw_data["jobStateTimeLimitActions"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateJobQueueRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateJobQueueRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobQueueDetail:
    boto3_raw_data: "type_defs.JobQueueDetailTypeDef" = dataclasses.field()

    jobQueueName = field("jobQueueName")
    jobQueueArn = field("jobQueueArn")
    state = field("state")
    priority = field("priority")

    @cached_property
    def computeEnvironmentOrder(self):  # pragma: no cover
        return ComputeEnvironmentOrder.make_many(
            self.boto3_raw_data["computeEnvironmentOrder"]
        )

    schedulingPolicyArn = field("schedulingPolicyArn")
    status = field("status")
    statusReason = field("statusReason")

    @cached_property
    def serviceEnvironmentOrder(self):  # pragma: no cover
        return ServiceEnvironmentOrder.make_many(
            self.boto3_raw_data["serviceEnvironmentOrder"]
        )

    jobQueueType = field("jobQueueType")
    tags = field("tags")

    @cached_property
    def jobStateTimeLimitActions(self):  # pragma: no cover
        return JobStateTimeLimitAction.make_many(
            self.boto3_raw_data["jobStateTimeLimitActions"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobQueueDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JobQueueDetailTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateJobQueueRequest:
    boto3_raw_data: "type_defs.UpdateJobQueueRequestTypeDef" = dataclasses.field()

    jobQueue = field("jobQueue")
    state = field("state")
    schedulingPolicyArn = field("schedulingPolicyArn")
    priority = field("priority")

    @cached_property
    def computeEnvironmentOrder(self):  # pragma: no cover
        return ComputeEnvironmentOrder.make_many(
            self.boto3_raw_data["computeEnvironmentOrder"]
        )

    @cached_property
    def serviceEnvironmentOrder(self):  # pragma: no cover
        return ServiceEnvironmentOrder.make_many(
            self.boto3_raw_data["serviceEnvironmentOrder"]
        )

    @cached_property
    def jobStateTimeLimitActions(self):  # pragma: no cover
        return JobStateTimeLimitAction.make_many(
            self.boto3_raw_data["jobStateTimeLimitActions"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateJobQueueRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateJobQueueRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeComputeEnvironmentsRequestPaginate:
    boto3_raw_data: "type_defs.DescribeComputeEnvironmentsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    computeEnvironments = field("computeEnvironments")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeComputeEnvironmentsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeComputeEnvironmentsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeJobDefinitionsRequestPaginate:
    boto3_raw_data: "type_defs.DescribeJobDefinitionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    jobDefinitions = field("jobDefinitions")
    jobDefinitionName = field("jobDefinitionName")
    status = field("status")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeJobDefinitionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeJobDefinitionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeJobQueuesRequestPaginate:
    boto3_raw_data: "type_defs.DescribeJobQueuesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    jobQueues = field("jobQueues")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeJobQueuesRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeJobQueuesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeServiceEnvironmentsRequestPaginate:
    boto3_raw_data: "type_defs.DescribeServiceEnvironmentsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    serviceEnvironments = field("serviceEnvironments")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeServiceEnvironmentsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeServiceEnvironmentsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSchedulingPoliciesRequestPaginate:
    boto3_raw_data: "type_defs.ListSchedulingPoliciesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSchedulingPoliciesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSchedulingPoliciesRequestPaginateTypeDef"]
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
class EksAttemptDetail:
    boto3_raw_data: "type_defs.EksAttemptDetailTypeDef" = dataclasses.field()

    @cached_property
    def containers(self):  # pragma: no cover
        return EksAttemptContainerDetail.make_many(self.boto3_raw_data["containers"])

    @cached_property
    def initContainers(self):  # pragma: no cover
        return EksAttemptContainerDetail.make_many(
            self.boto3_raw_data["initContainers"]
        )

    eksClusterArn = field("eksClusterArn")
    podName = field("podName")
    podNamespace = field("podNamespace")
    nodeName = field("nodeName")
    startedAt = field("startedAt")
    stoppedAt = field("stoppedAt")
    statusReason = field("statusReason")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EksAttemptDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EksAttemptDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EksContainerDetail:
    boto3_raw_data: "type_defs.EksContainerDetailTypeDef" = dataclasses.field()

    name = field("name")
    image = field("image")
    imagePullPolicy = field("imagePullPolicy")
    command = field("command")
    args = field("args")

    @cached_property
    def env(self):  # pragma: no cover
        return EksContainerEnvironmentVariable.make_many(self.boto3_raw_data["env"])

    @cached_property
    def resources(self):  # pragma: no cover
        return EksContainerResourceRequirementsOutput.make_one(
            self.boto3_raw_data["resources"]
        )

    exitCode = field("exitCode")
    reason = field("reason")

    @cached_property
    def volumeMounts(self):  # pragma: no cover
        return EksContainerVolumeMount.make_many(self.boto3_raw_data["volumeMounts"])

    @cached_property
    def securityContext(self):  # pragma: no cover
        return EksContainerSecurityContext.make_one(
            self.boto3_raw_data["securityContext"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EksContainerDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EksContainerDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EksContainerOutput:
    boto3_raw_data: "type_defs.EksContainerOutputTypeDef" = dataclasses.field()

    image = field("image")
    name = field("name")
    imagePullPolicy = field("imagePullPolicy")
    command = field("command")
    args = field("args")

    @cached_property
    def env(self):  # pragma: no cover
        return EksContainerEnvironmentVariable.make_many(self.boto3_raw_data["env"])

    @cached_property
    def resources(self):  # pragma: no cover
        return EksContainerResourceRequirementsOutput.make_one(
            self.boto3_raw_data["resources"]
        )

    @cached_property
    def volumeMounts(self):  # pragma: no cover
        return EksContainerVolumeMount.make_many(self.boto3_raw_data["volumeMounts"])

    @cached_property
    def securityContext(self):  # pragma: no cover
        return EksContainerSecurityContext.make_one(
            self.boto3_raw_data["securityContext"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EksContainerOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EksContainerOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EksContainer:
    boto3_raw_data: "type_defs.EksContainerTypeDef" = dataclasses.field()

    image = field("image")
    name = field("name")
    imagePullPolicy = field("imagePullPolicy")
    command = field("command")
    args = field("args")

    @cached_property
    def env(self):  # pragma: no cover
        return EksContainerEnvironmentVariable.make_many(self.boto3_raw_data["env"])

    @cached_property
    def resources(self):  # pragma: no cover
        return EksContainerResourceRequirements.make_one(
            self.boto3_raw_data["resources"]
        )

    @cached_property
    def volumeMounts(self):  # pragma: no cover
        return EksContainerVolumeMount.make_many(self.boto3_raw_data["volumeMounts"])

    @cached_property
    def securityContext(self):  # pragma: no cover
        return EksContainerSecurityContext.make_one(
            self.boto3_raw_data["securityContext"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EksContainerTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EksContainerTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EksVolume:
    boto3_raw_data: "type_defs.EksVolumeTypeDef" = dataclasses.field()

    name = field("name")

    @cached_property
    def hostPath(self):  # pragma: no cover
        return EksHostPath.make_one(self.boto3_raw_data["hostPath"])

    @cached_property
    def emptyDir(self):  # pragma: no cover
        return EksEmptyDir.make_one(self.boto3_raw_data["emptyDir"])

    @cached_property
    def secret(self):  # pragma: no cover
        return EksSecret.make_one(self.boto3_raw_data["secret"])

    @cached_property
    def persistentVolumeClaim(self):  # pragma: no cover
        return EksPersistentVolumeClaim.make_one(
            self.boto3_raw_data["persistentVolumeClaim"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EksVolumeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EksVolumeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RetryStrategyOutput:
    boto3_raw_data: "type_defs.RetryStrategyOutputTypeDef" = dataclasses.field()

    attempts = field("attempts")

    @cached_property
    def evaluateOnExit(self):  # pragma: no cover
        return EvaluateOnExit.make_many(self.boto3_raw_data["evaluateOnExit"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RetryStrategyOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RetryStrategyOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RetryStrategy:
    boto3_raw_data: "type_defs.RetryStrategyTypeDef" = dataclasses.field()

    attempts = field("attempts")

    @cached_property
    def evaluateOnExit(self):  # pragma: no cover
        return EvaluateOnExit.make_many(self.boto3_raw_data["evaluateOnExit"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RetryStrategyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RetryStrategyTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FairsharePolicyOutput:
    boto3_raw_data: "type_defs.FairsharePolicyOutputTypeDef" = dataclasses.field()

    shareDecaySeconds = field("shareDecaySeconds")
    computeReservation = field("computeReservation")

    @cached_property
    def shareDistribution(self):  # pragma: no cover
        return ShareAttributes.make_many(self.boto3_raw_data["shareDistribution"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FairsharePolicyOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FairsharePolicyOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FairsharePolicy:
    boto3_raw_data: "type_defs.FairsharePolicyTypeDef" = dataclasses.field()

    shareDecaySeconds = field("shareDecaySeconds")
    computeReservation = field("computeReservation")

    @cached_property
    def shareDistribution(self):  # pragma: no cover
        return ShareAttributes.make_many(self.boto3_raw_data["shareDistribution"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FairsharePolicyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FairsharePolicyTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FrontOfQueueDetail:
    boto3_raw_data: "type_defs.FrontOfQueueDetailTypeDef" = dataclasses.field()

    @cached_property
    def jobs(self):  # pragma: no cover
        return FrontOfQueueJobSummary.make_many(self.boto3_raw_data["jobs"])

    lastUpdatedAt = field("lastUpdatedAt")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FrontOfQueueDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FrontOfQueueDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobSummary:
    boto3_raw_data: "type_defs.JobSummaryTypeDef" = dataclasses.field()

    jobId = field("jobId")
    jobName = field("jobName")
    jobArn = field("jobArn")
    createdAt = field("createdAt")
    status = field("status")
    statusReason = field("statusReason")
    startedAt = field("startedAt")
    stoppedAt = field("stoppedAt")

    @cached_property
    def container(self):  # pragma: no cover
        return ContainerSummary.make_one(self.boto3_raw_data["container"])

    @cached_property
    def arrayProperties(self):  # pragma: no cover
        return ArrayPropertiesSummary.make_one(self.boto3_raw_data["arrayProperties"])

    @cached_property
    def nodeProperties(self):  # pragma: no cover
        return NodePropertiesSummary.make_one(self.boto3_raw_data["nodeProperties"])

    jobDefinition = field("jobDefinition")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JobSummaryTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConsumableResourcesRequestPaginate:
    boto3_raw_data: "type_defs.ListConsumableResourcesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def filters(self):  # pragma: no cover
        return KeyValuesPair.make_many(self.boto3_raw_data["filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListConsumableResourcesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConsumableResourcesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConsumableResourcesRequest:
    boto3_raw_data: "type_defs.ListConsumableResourcesRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def filters(self):  # pragma: no cover
        return KeyValuesPair.make_many(self.boto3_raw_data["filters"])

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListConsumableResourcesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConsumableResourcesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListJobsByConsumableResourceRequestPaginate:
    boto3_raw_data: "type_defs.ListJobsByConsumableResourceRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    consumableResource = field("consumableResource")

    @cached_property
    def filters(self):  # pragma: no cover
        return KeyValuesPair.make_many(self.boto3_raw_data["filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListJobsByConsumableResourceRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListJobsByConsumableResourceRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListJobsByConsumableResourceRequest:
    boto3_raw_data: "type_defs.ListJobsByConsumableResourceRequestTypeDef" = (
        dataclasses.field()
    )

    consumableResource = field("consumableResource")

    @cached_property
    def filters(self):  # pragma: no cover
        return KeyValuesPair.make_many(self.boto3_raw_data["filters"])

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListJobsByConsumableResourceRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListJobsByConsumableResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListJobsRequestPaginate:
    boto3_raw_data: "type_defs.ListJobsRequestPaginateTypeDef" = dataclasses.field()

    jobQueue = field("jobQueue")
    arrayJobId = field("arrayJobId")
    multiNodeJobId = field("multiNodeJobId")
    jobStatus = field("jobStatus")

    @cached_property
    def filters(self):  # pragma: no cover
        return KeyValuesPair.make_many(self.boto3_raw_data["filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListJobsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListJobsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListJobsRequest:
    boto3_raw_data: "type_defs.ListJobsRequestTypeDef" = dataclasses.field()

    jobQueue = field("jobQueue")
    arrayJobId = field("arrayJobId")
    multiNodeJobId = field("multiNodeJobId")
    jobStatus = field("jobStatus")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @cached_property
    def filters(self):  # pragma: no cover
        return KeyValuesPair.make_many(self.boto3_raw_data["filters"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListJobsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListJobsRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServiceJobsRequestPaginate:
    boto3_raw_data: "type_defs.ListServiceJobsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    jobQueue = field("jobQueue")
    jobStatus = field("jobStatus")

    @cached_property
    def filters(self):  # pragma: no cover
        return KeyValuesPair.make_many(self.boto3_raw_data["filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListServiceJobsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServiceJobsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServiceJobsRequest:
    boto3_raw_data: "type_defs.ListServiceJobsRequestTypeDef" = dataclasses.field()

    jobQueue = field("jobQueue")
    jobStatus = field("jobStatus")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @cached_property
    def filters(self):  # pragma: no cover
        return KeyValuesPair.make_many(self.boto3_raw_data["filters"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListServiceJobsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServiceJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LatestServiceJobAttempt:
    boto3_raw_data: "type_defs.LatestServiceJobAttemptTypeDef" = dataclasses.field()

    @cached_property
    def serviceResourceId(self):  # pragma: no cover
        return ServiceResourceId.make_one(self.boto3_raw_data["serviceResourceId"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LatestServiceJobAttemptTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LatestServiceJobAttemptTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceJobAttemptDetail:
    boto3_raw_data: "type_defs.ServiceJobAttemptDetailTypeDef" = dataclasses.field()

    @cached_property
    def serviceResourceId(self):  # pragma: no cover
        return ServiceResourceId.make_one(self.boto3_raw_data["serviceResourceId"])

    startedAt = field("startedAt")
    stoppedAt = field("stoppedAt")
    statusReason = field("statusReason")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ServiceJobAttemptDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceJobAttemptDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LaunchTemplateSpecificationOutput:
    boto3_raw_data: "type_defs.LaunchTemplateSpecificationOutputTypeDef" = (
        dataclasses.field()
    )

    launchTemplateId = field("launchTemplateId")
    launchTemplateName = field("launchTemplateName")
    version = field("version")

    @cached_property
    def overrides(self):  # pragma: no cover
        return LaunchTemplateSpecificationOverrideOutput.make_many(
            self.boto3_raw_data["overrides"]
        )

    userdataType = field("userdataType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.LaunchTemplateSpecificationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LaunchTemplateSpecificationOutputTypeDef"]
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
class LinuxParameters:
    boto3_raw_data: "type_defs.LinuxParametersTypeDef" = dataclasses.field()

    @cached_property
    def devices(self):  # pragma: no cover
        return Device.make_many(self.boto3_raw_data["devices"])

    initProcessEnabled = field("initProcessEnabled")
    sharedMemorySize = field("sharedMemorySize")

    @cached_property
    def tmpfs(self):  # pragma: no cover
        return Tmpfs.make_many(self.boto3_raw_data["tmpfs"])

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
class ListSchedulingPoliciesResponse:
    boto3_raw_data: "type_defs.ListSchedulingPoliciesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def schedulingPolicies(self):  # pragma: no cover
        return SchedulingPolicyListingDetail.make_many(
            self.boto3_raw_data["schedulingPolicies"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListSchedulingPoliciesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSchedulingPoliciesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceJobRetryStrategyOutput:
    boto3_raw_data: "type_defs.ServiceJobRetryStrategyOutputTypeDef" = (
        dataclasses.field()
    )

    attempts = field("attempts")

    @cached_property
    def evaluateOnExit(self):  # pragma: no cover
        return ServiceJobEvaluateOnExit.make_many(self.boto3_raw_data["evaluateOnExit"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ServiceJobRetryStrategyOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceJobRetryStrategyOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceJobRetryStrategy:
    boto3_raw_data: "type_defs.ServiceJobRetryStrategyTypeDef" = dataclasses.field()

    attempts = field("attempts")

    @cached_property
    def evaluateOnExit(self):  # pragma: no cover
        return ServiceJobEvaluateOnExit.make_many(self.boto3_raw_data["evaluateOnExit"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ServiceJobRetryStrategyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceJobRetryStrategyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttemptEcsTaskDetails:
    boto3_raw_data: "type_defs.AttemptEcsTaskDetailsTypeDef" = dataclasses.field()

    containerInstanceArn = field("containerInstanceArn")
    taskArn = field("taskArn")

    @cached_property
    def containers(self):  # pragma: no cover
        return AttemptTaskContainerDetails.make_many(self.boto3_raw_data["containers"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AttemptEcsTaskDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttemptEcsTaskDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeServiceEnvironmentsResponse:
    boto3_raw_data: "type_defs.DescribeServiceEnvironmentsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def serviceEnvironments(self):  # pragma: no cover
        return ServiceEnvironmentDetail.make_many(
            self.boto3_raw_data["serviceEnvironments"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeServiceEnvironmentsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeServiceEnvironmentsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListJobsByConsumableResourceSummary:
    boto3_raw_data: "type_defs.ListJobsByConsumableResourceSummaryTypeDef" = (
        dataclasses.field()
    )

    jobArn = field("jobArn")
    jobQueueArn = field("jobQueueArn")
    jobName = field("jobName")
    jobStatus = field("jobStatus")
    quantity = field("quantity")
    createdAt = field("createdAt")

    @cached_property
    def consumableResourceProperties(self):  # pragma: no cover
        return ConsumableResourcePropertiesOutput.make_one(
            self.boto3_raw_data["consumableResourceProperties"]
        )

    jobDefinitionArn = field("jobDefinitionArn")
    shareIdentifier = field("shareIdentifier")
    statusReason = field("statusReason")
    startedAt = field("startedAt")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListJobsByConsumableResourceSummaryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListJobsByConsumableResourceSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TaskPropertiesOverride:
    boto3_raw_data: "type_defs.TaskPropertiesOverrideTypeDef" = dataclasses.field()

    @cached_property
    def containers(self):  # pragma: no cover
        return TaskContainerOverrides.make_many(self.boto3_raw_data["containers"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TaskPropertiesOverrideTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TaskPropertiesOverrideTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeJobQueuesResponse:
    boto3_raw_data: "type_defs.DescribeJobQueuesResponseTypeDef" = dataclasses.field()

    @cached_property
    def jobQueues(self):  # pragma: no cover
        return JobQueueDetail.make_many(self.boto3_raw_data["jobQueues"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeJobQueuesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeJobQueuesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Volume:
    boto3_raw_data: "type_defs.VolumeTypeDef" = dataclasses.field()

    @cached_property
    def host(self):  # pragma: no cover
        return Host.make_one(self.boto3_raw_data["host"])

    name = field("name")

    @cached_property
    def efsVolumeConfiguration(self):  # pragma: no cover
        return EFSVolumeConfiguration.make_one(
            self.boto3_raw_data["efsVolumeConfiguration"]
        )

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
class EksContainerOverride:
    boto3_raw_data: "type_defs.EksContainerOverrideTypeDef" = dataclasses.field()

    name = field("name")
    image = field("image")
    command = field("command")
    args = field("args")

    @cached_property
    def env(self):  # pragma: no cover
        return EksContainerEnvironmentVariable.make_many(self.boto3_raw_data["env"])

    resources = field("resources")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EksContainerOverrideTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EksContainerOverrideTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EksPodPropertiesDetail:
    boto3_raw_data: "type_defs.EksPodPropertiesDetailTypeDef" = dataclasses.field()

    serviceAccountName = field("serviceAccountName")
    hostNetwork = field("hostNetwork")
    dnsPolicy = field("dnsPolicy")

    @cached_property
    def imagePullSecrets(self):  # pragma: no cover
        return ImagePullSecret.make_many(self.boto3_raw_data["imagePullSecrets"])

    @cached_property
    def containers(self):  # pragma: no cover
        return EksContainerDetail.make_many(self.boto3_raw_data["containers"])

    @cached_property
    def initContainers(self):  # pragma: no cover
        return EksContainerDetail.make_many(self.boto3_raw_data["initContainers"])

    @cached_property
    def volumes(self):  # pragma: no cover
        return EksVolume.make_many(self.boto3_raw_data["volumes"])

    podName = field("podName")
    nodeName = field("nodeName")

    @cached_property
    def metadata(self):  # pragma: no cover
        return EksMetadataOutput.make_one(self.boto3_raw_data["metadata"])

    shareProcessNamespace = field("shareProcessNamespace")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EksPodPropertiesDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EksPodPropertiesDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EksPodPropertiesOutput:
    boto3_raw_data: "type_defs.EksPodPropertiesOutputTypeDef" = dataclasses.field()

    serviceAccountName = field("serviceAccountName")
    hostNetwork = field("hostNetwork")
    dnsPolicy = field("dnsPolicy")

    @cached_property
    def imagePullSecrets(self):  # pragma: no cover
        return ImagePullSecret.make_many(self.boto3_raw_data["imagePullSecrets"])

    @cached_property
    def containers(self):  # pragma: no cover
        return EksContainerOutput.make_many(self.boto3_raw_data["containers"])

    @cached_property
    def initContainers(self):  # pragma: no cover
        return EksContainerOutput.make_many(self.boto3_raw_data["initContainers"])

    @cached_property
    def volumes(self):  # pragma: no cover
        return EksVolume.make_many(self.boto3_raw_data["volumes"])

    @cached_property
    def metadata(self):  # pragma: no cover
        return EksMetadataOutput.make_one(self.boto3_raw_data["metadata"])

    shareProcessNamespace = field("shareProcessNamespace")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EksPodPropertiesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EksPodPropertiesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EksPodProperties:
    boto3_raw_data: "type_defs.EksPodPropertiesTypeDef" = dataclasses.field()

    serviceAccountName = field("serviceAccountName")
    hostNetwork = field("hostNetwork")
    dnsPolicy = field("dnsPolicy")

    @cached_property
    def imagePullSecrets(self):  # pragma: no cover
        return ImagePullSecret.make_many(self.boto3_raw_data["imagePullSecrets"])

    @cached_property
    def containers(self):  # pragma: no cover
        return EksContainer.make_many(self.boto3_raw_data["containers"])

    @cached_property
    def initContainers(self):  # pragma: no cover
        return EksContainer.make_many(self.boto3_raw_data["initContainers"])

    @cached_property
    def volumes(self):  # pragma: no cover
        return EksVolume.make_many(self.boto3_raw_data["volumes"])

    @cached_property
    def metadata(self):  # pragma: no cover
        return EksMetadata.make_one(self.boto3_raw_data["metadata"])

    shareProcessNamespace = field("shareProcessNamespace")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EksPodPropertiesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EksPodPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SchedulingPolicyDetail:
    boto3_raw_data: "type_defs.SchedulingPolicyDetailTypeDef" = dataclasses.field()

    name = field("name")
    arn = field("arn")

    @cached_property
    def fairsharePolicy(self):  # pragma: no cover
        return FairsharePolicyOutput.make_one(self.boto3_raw_data["fairsharePolicy"])

    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SchedulingPolicyDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SchedulingPolicyDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetJobQueueSnapshotResponse:
    boto3_raw_data: "type_defs.GetJobQueueSnapshotResponseTypeDef" = dataclasses.field()

    @cached_property
    def frontOfQueue(self):  # pragma: no cover
        return FrontOfQueueDetail.make_one(self.boto3_raw_data["frontOfQueue"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetJobQueueSnapshotResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetJobQueueSnapshotResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListJobsResponse:
    boto3_raw_data: "type_defs.ListJobsResponseTypeDef" = dataclasses.field()

    @cached_property
    def jobSummaryList(self):  # pragma: no cover
        return JobSummary.make_many(self.boto3_raw_data["jobSummaryList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListJobsResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceJobSummary:
    boto3_raw_data: "type_defs.ServiceJobSummaryTypeDef" = dataclasses.field()

    jobId = field("jobId")
    jobName = field("jobName")
    serviceJobType = field("serviceJobType")

    @cached_property
    def latestAttempt(self):  # pragma: no cover
        return LatestServiceJobAttempt.make_one(self.boto3_raw_data["latestAttempt"])

    createdAt = field("createdAt")
    jobArn = field("jobArn")
    shareIdentifier = field("shareIdentifier")
    status = field("status")
    statusReason = field("statusReason")
    startedAt = field("startedAt")
    stoppedAt = field("stoppedAt")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ServiceJobSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceJobSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComputeResourceOutput:
    boto3_raw_data: "type_defs.ComputeResourceOutputTypeDef" = dataclasses.field()

    type = field("type")
    maxvCpus = field("maxvCpus")
    subnets = field("subnets")
    allocationStrategy = field("allocationStrategy")
    minvCpus = field("minvCpus")
    desiredvCpus = field("desiredvCpus")
    instanceTypes = field("instanceTypes")
    imageId = field("imageId")
    securityGroupIds = field("securityGroupIds")
    ec2KeyPair = field("ec2KeyPair")
    instanceRole = field("instanceRole")
    tags = field("tags")
    placementGroup = field("placementGroup")
    bidPercentage = field("bidPercentage")
    spotIamFleetRole = field("spotIamFleetRole")

    @cached_property
    def launchTemplate(self):  # pragma: no cover
        return LaunchTemplateSpecificationOutput.make_one(
            self.boto3_raw_data["launchTemplate"]
        )

    @cached_property
    def ec2Configuration(self):  # pragma: no cover
        return Ec2Configuration.make_many(self.boto3_raw_data["ec2Configuration"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ComputeResourceOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComputeResourceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LaunchTemplateSpecification:
    boto3_raw_data: "type_defs.LaunchTemplateSpecificationTypeDef" = dataclasses.field()

    launchTemplateId = field("launchTemplateId")
    launchTemplateName = field("launchTemplateName")
    version = field("version")
    overrides = field("overrides")
    userdataType = field("userdataType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LaunchTemplateSpecificationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LaunchTemplateSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TaskContainerDetails:
    boto3_raw_data: "type_defs.TaskContainerDetailsTypeDef" = dataclasses.field()

    command = field("command")

    @cached_property
    def dependsOn(self):  # pragma: no cover
        return TaskContainerDependency.make_many(self.boto3_raw_data["dependsOn"])

    @cached_property
    def environment(self):  # pragma: no cover
        return KeyValuePair.make_many(self.boto3_raw_data["environment"])

    essential = field("essential")

    @cached_property
    def firelensConfiguration(self):  # pragma: no cover
        return FirelensConfigurationOutput.make_one(
            self.boto3_raw_data["firelensConfiguration"]
        )

    image = field("image")

    @cached_property
    def linuxParameters(self):  # pragma: no cover
        return LinuxParametersOutput.make_one(self.boto3_raw_data["linuxParameters"])

    @cached_property
    def logConfiguration(self):  # pragma: no cover
        return LogConfigurationOutput.make_one(self.boto3_raw_data["logConfiguration"])

    @cached_property
    def mountPoints(self):  # pragma: no cover
        return MountPoint.make_many(self.boto3_raw_data["mountPoints"])

    name = field("name")
    privileged = field("privileged")
    readonlyRootFilesystem = field("readonlyRootFilesystem")

    @cached_property
    def repositoryCredentials(self):  # pragma: no cover
        return RepositoryCredentials.make_one(
            self.boto3_raw_data["repositoryCredentials"]
        )

    @cached_property
    def resourceRequirements(self):  # pragma: no cover
        return ResourceRequirement.make_many(
            self.boto3_raw_data["resourceRequirements"]
        )

    @cached_property
    def secrets(self):  # pragma: no cover
        return Secret.make_many(self.boto3_raw_data["secrets"])

    @cached_property
    def ulimits(self):  # pragma: no cover
        return Ulimit.make_many(self.boto3_raw_data["ulimits"])

    user = field("user")
    exitCode = field("exitCode")
    reason = field("reason")
    logStreamName = field("logStreamName")

    @cached_property
    def networkInterfaces(self):  # pragma: no cover
        return NetworkInterface.make_many(self.boto3_raw_data["networkInterfaces"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TaskContainerDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TaskContainerDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TaskContainerPropertiesOutput:
    boto3_raw_data: "type_defs.TaskContainerPropertiesOutputTypeDef" = (
        dataclasses.field()
    )

    image = field("image")
    command = field("command")

    @cached_property
    def dependsOn(self):  # pragma: no cover
        return TaskContainerDependency.make_many(self.boto3_raw_data["dependsOn"])

    @cached_property
    def environment(self):  # pragma: no cover
        return KeyValuePair.make_many(self.boto3_raw_data["environment"])

    essential = field("essential")

    @cached_property
    def firelensConfiguration(self):  # pragma: no cover
        return FirelensConfigurationOutput.make_one(
            self.boto3_raw_data["firelensConfiguration"]
        )

    @cached_property
    def linuxParameters(self):  # pragma: no cover
        return LinuxParametersOutput.make_one(self.boto3_raw_data["linuxParameters"])

    @cached_property
    def logConfiguration(self):  # pragma: no cover
        return LogConfigurationOutput.make_one(self.boto3_raw_data["logConfiguration"])

    @cached_property
    def mountPoints(self):  # pragma: no cover
        return MountPoint.make_many(self.boto3_raw_data["mountPoints"])

    name = field("name")
    privileged = field("privileged")
    readonlyRootFilesystem = field("readonlyRootFilesystem")

    @cached_property
    def repositoryCredentials(self):  # pragma: no cover
        return RepositoryCredentials.make_one(
            self.boto3_raw_data["repositoryCredentials"]
        )

    @cached_property
    def resourceRequirements(self):  # pragma: no cover
        return ResourceRequirement.make_many(
            self.boto3_raw_data["resourceRequirements"]
        )

    @cached_property
    def secrets(self):  # pragma: no cover
        return Secret.make_many(self.boto3_raw_data["secrets"])

    @cached_property
    def ulimits(self):  # pragma: no cover
        return Ulimit.make_many(self.boto3_raw_data["ulimits"])

    user = field("user")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.TaskContainerPropertiesOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TaskContainerPropertiesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TaskContainerProperties:
    boto3_raw_data: "type_defs.TaskContainerPropertiesTypeDef" = dataclasses.field()

    image = field("image")
    command = field("command")

    @cached_property
    def dependsOn(self):  # pragma: no cover
        return TaskContainerDependency.make_many(self.boto3_raw_data["dependsOn"])

    @cached_property
    def environment(self):  # pragma: no cover
        return KeyValuePair.make_many(self.boto3_raw_data["environment"])

    essential = field("essential")

    @cached_property
    def firelensConfiguration(self):  # pragma: no cover
        return FirelensConfiguration.make_one(
            self.boto3_raw_data["firelensConfiguration"]
        )

    @cached_property
    def linuxParameters(self):  # pragma: no cover
        return LinuxParameters.make_one(self.boto3_raw_data["linuxParameters"])

    @cached_property
    def logConfiguration(self):  # pragma: no cover
        return LogConfiguration.make_one(self.boto3_raw_data["logConfiguration"])

    @cached_property
    def mountPoints(self):  # pragma: no cover
        return MountPoint.make_many(self.boto3_raw_data["mountPoints"])

    name = field("name")
    privileged = field("privileged")
    readonlyRootFilesystem = field("readonlyRootFilesystem")

    @cached_property
    def repositoryCredentials(self):  # pragma: no cover
        return RepositoryCredentials.make_one(
            self.boto3_raw_data["repositoryCredentials"]
        )

    @cached_property
    def resourceRequirements(self):  # pragma: no cover
        return ResourceRequirement.make_many(
            self.boto3_raw_data["resourceRequirements"]
        )

    @cached_property
    def secrets(self):  # pragma: no cover
        return Secret.make_many(self.boto3_raw_data["secrets"])

    @cached_property
    def ulimits(self):  # pragma: no cover
        return Ulimit.make_many(self.boto3_raw_data["ulimits"])

    user = field("user")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TaskContainerPropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TaskContainerPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeServiceJobResponse:
    boto3_raw_data: "type_defs.DescribeServiceJobResponseTypeDef" = dataclasses.field()

    @cached_property
    def attempts(self):  # pragma: no cover
        return ServiceJobAttemptDetail.make_many(self.boto3_raw_data["attempts"])

    createdAt = field("createdAt")
    isTerminated = field("isTerminated")
    jobArn = field("jobArn")
    jobId = field("jobId")
    jobName = field("jobName")
    jobQueue = field("jobQueue")

    @cached_property
    def latestAttempt(self):  # pragma: no cover
        return LatestServiceJobAttempt.make_one(self.boto3_raw_data["latestAttempt"])

    @cached_property
    def retryStrategy(self):  # pragma: no cover
        return ServiceJobRetryStrategyOutput.make_one(
            self.boto3_raw_data["retryStrategy"]
        )

    schedulingPriority = field("schedulingPriority")
    serviceRequestPayload = field("serviceRequestPayload")
    serviceJobType = field("serviceJobType")
    shareIdentifier = field("shareIdentifier")
    startedAt = field("startedAt")
    status = field("status")
    statusReason = field("statusReason")
    stoppedAt = field("stoppedAt")
    tags = field("tags")

    @cached_property
    def timeoutConfig(self):  # pragma: no cover
        return ServiceJobTimeout.make_one(self.boto3_raw_data["timeoutConfig"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeServiceJobResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeServiceJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttemptDetail:
    boto3_raw_data: "type_defs.AttemptDetailTypeDef" = dataclasses.field()

    @cached_property
    def container(self):  # pragma: no cover
        return AttemptContainerDetail.make_one(self.boto3_raw_data["container"])

    startedAt = field("startedAt")
    stoppedAt = field("stoppedAt")
    statusReason = field("statusReason")

    @cached_property
    def taskProperties(self):  # pragma: no cover
        return AttemptEcsTaskDetails.make_many(self.boto3_raw_data["taskProperties"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AttemptDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AttemptDetailTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListJobsByConsumableResourceResponse:
    boto3_raw_data: "type_defs.ListJobsByConsumableResourceResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def jobs(self):  # pragma: no cover
        return ListJobsByConsumableResourceSummary.make_many(
            self.boto3_raw_data["jobs"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListJobsByConsumableResourceResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListJobsByConsumableResourceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EcsPropertiesOverride:
    boto3_raw_data: "type_defs.EcsPropertiesOverrideTypeDef" = dataclasses.field()

    @cached_property
    def taskProperties(self):  # pragma: no cover
        return TaskPropertiesOverride.make_many(self.boto3_raw_data["taskProperties"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EcsPropertiesOverrideTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EcsPropertiesOverrideTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContainerDetail:
    boto3_raw_data: "type_defs.ContainerDetailTypeDef" = dataclasses.field()

    image = field("image")
    vcpus = field("vcpus")
    memory = field("memory")
    command = field("command")
    jobRoleArn = field("jobRoleArn")
    executionRoleArn = field("executionRoleArn")

    @cached_property
    def volumes(self):  # pragma: no cover
        return Volume.make_many(self.boto3_raw_data["volumes"])

    @cached_property
    def environment(self):  # pragma: no cover
        return KeyValuePair.make_many(self.boto3_raw_data["environment"])

    @cached_property
    def mountPoints(self):  # pragma: no cover
        return MountPoint.make_many(self.boto3_raw_data["mountPoints"])

    readonlyRootFilesystem = field("readonlyRootFilesystem")

    @cached_property
    def ulimits(self):  # pragma: no cover
        return Ulimit.make_many(self.boto3_raw_data["ulimits"])

    privileged = field("privileged")
    user = field("user")
    exitCode = field("exitCode")
    reason = field("reason")
    containerInstanceArn = field("containerInstanceArn")
    taskArn = field("taskArn")
    logStreamName = field("logStreamName")
    instanceType = field("instanceType")

    @cached_property
    def networkInterfaces(self):  # pragma: no cover
        return NetworkInterface.make_many(self.boto3_raw_data["networkInterfaces"])

    @cached_property
    def resourceRequirements(self):  # pragma: no cover
        return ResourceRequirement.make_many(
            self.boto3_raw_data["resourceRequirements"]
        )

    @cached_property
    def linuxParameters(self):  # pragma: no cover
        return LinuxParametersOutput.make_one(self.boto3_raw_data["linuxParameters"])

    @cached_property
    def logConfiguration(self):  # pragma: no cover
        return LogConfigurationOutput.make_one(self.boto3_raw_data["logConfiguration"])

    @cached_property
    def secrets(self):  # pragma: no cover
        return Secret.make_many(self.boto3_raw_data["secrets"])

    @cached_property
    def networkConfiguration(self):  # pragma: no cover
        return NetworkConfiguration.make_one(
            self.boto3_raw_data["networkConfiguration"]
        )

    @cached_property
    def fargatePlatformConfiguration(self):  # pragma: no cover
        return FargatePlatformConfiguration.make_one(
            self.boto3_raw_data["fargatePlatformConfiguration"]
        )

    @cached_property
    def ephemeralStorage(self):  # pragma: no cover
        return EphemeralStorage.make_one(self.boto3_raw_data["ephemeralStorage"])

    @cached_property
    def runtimePlatform(self):  # pragma: no cover
        return RuntimePlatform.make_one(self.boto3_raw_data["runtimePlatform"])

    @cached_property
    def repositoryCredentials(self):  # pragma: no cover
        return RepositoryCredentials.make_one(
            self.boto3_raw_data["repositoryCredentials"]
        )

    enableExecuteCommand = field("enableExecuteCommand")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ContainerDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ContainerDetailTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContainerPropertiesOutput:
    boto3_raw_data: "type_defs.ContainerPropertiesOutputTypeDef" = dataclasses.field()

    image = field("image")
    vcpus = field("vcpus")
    memory = field("memory")
    command = field("command")
    jobRoleArn = field("jobRoleArn")
    executionRoleArn = field("executionRoleArn")

    @cached_property
    def volumes(self):  # pragma: no cover
        return Volume.make_many(self.boto3_raw_data["volumes"])

    @cached_property
    def environment(self):  # pragma: no cover
        return KeyValuePair.make_many(self.boto3_raw_data["environment"])

    @cached_property
    def mountPoints(self):  # pragma: no cover
        return MountPoint.make_many(self.boto3_raw_data["mountPoints"])

    readonlyRootFilesystem = field("readonlyRootFilesystem")
    privileged = field("privileged")

    @cached_property
    def ulimits(self):  # pragma: no cover
        return Ulimit.make_many(self.boto3_raw_data["ulimits"])

    user = field("user")
    instanceType = field("instanceType")

    @cached_property
    def resourceRequirements(self):  # pragma: no cover
        return ResourceRequirement.make_many(
            self.boto3_raw_data["resourceRequirements"]
        )

    @cached_property
    def linuxParameters(self):  # pragma: no cover
        return LinuxParametersOutput.make_one(self.boto3_raw_data["linuxParameters"])

    @cached_property
    def logConfiguration(self):  # pragma: no cover
        return LogConfigurationOutput.make_one(self.boto3_raw_data["logConfiguration"])

    @cached_property
    def secrets(self):  # pragma: no cover
        return Secret.make_many(self.boto3_raw_data["secrets"])

    @cached_property
    def networkConfiguration(self):  # pragma: no cover
        return NetworkConfiguration.make_one(
            self.boto3_raw_data["networkConfiguration"]
        )

    @cached_property
    def fargatePlatformConfiguration(self):  # pragma: no cover
        return FargatePlatformConfiguration.make_one(
            self.boto3_raw_data["fargatePlatformConfiguration"]
        )

    enableExecuteCommand = field("enableExecuteCommand")

    @cached_property
    def ephemeralStorage(self):  # pragma: no cover
        return EphemeralStorage.make_one(self.boto3_raw_data["ephemeralStorage"])

    @cached_property
    def runtimePlatform(self):  # pragma: no cover
        return RuntimePlatform.make_one(self.boto3_raw_data["runtimePlatform"])

    @cached_property
    def repositoryCredentials(self):  # pragma: no cover
        return RepositoryCredentials.make_one(
            self.boto3_raw_data["repositoryCredentials"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContainerPropertiesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContainerPropertiesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContainerProperties:
    boto3_raw_data: "type_defs.ContainerPropertiesTypeDef" = dataclasses.field()

    image = field("image")
    vcpus = field("vcpus")
    memory = field("memory")
    command = field("command")
    jobRoleArn = field("jobRoleArn")
    executionRoleArn = field("executionRoleArn")

    @cached_property
    def volumes(self):  # pragma: no cover
        return Volume.make_many(self.boto3_raw_data["volumes"])

    @cached_property
    def environment(self):  # pragma: no cover
        return KeyValuePair.make_many(self.boto3_raw_data["environment"])

    @cached_property
    def mountPoints(self):  # pragma: no cover
        return MountPoint.make_many(self.boto3_raw_data["mountPoints"])

    readonlyRootFilesystem = field("readonlyRootFilesystem")
    privileged = field("privileged")

    @cached_property
    def ulimits(self):  # pragma: no cover
        return Ulimit.make_many(self.boto3_raw_data["ulimits"])

    user = field("user")
    instanceType = field("instanceType")

    @cached_property
    def resourceRequirements(self):  # pragma: no cover
        return ResourceRequirement.make_many(
            self.boto3_raw_data["resourceRequirements"]
        )

    @cached_property
    def linuxParameters(self):  # pragma: no cover
        return LinuxParameters.make_one(self.boto3_raw_data["linuxParameters"])

    @cached_property
    def logConfiguration(self):  # pragma: no cover
        return LogConfiguration.make_one(self.boto3_raw_data["logConfiguration"])

    @cached_property
    def secrets(self):  # pragma: no cover
        return Secret.make_many(self.boto3_raw_data["secrets"])

    @cached_property
    def networkConfiguration(self):  # pragma: no cover
        return NetworkConfiguration.make_one(
            self.boto3_raw_data["networkConfiguration"]
        )

    @cached_property
    def fargatePlatformConfiguration(self):  # pragma: no cover
        return FargatePlatformConfiguration.make_one(
            self.boto3_raw_data["fargatePlatformConfiguration"]
        )

    enableExecuteCommand = field("enableExecuteCommand")

    @cached_property
    def ephemeralStorage(self):  # pragma: no cover
        return EphemeralStorage.make_one(self.boto3_raw_data["ephemeralStorage"])

    @cached_property
    def runtimePlatform(self):  # pragma: no cover
        return RuntimePlatform.make_one(self.boto3_raw_data["runtimePlatform"])

    @cached_property
    def repositoryCredentials(self):  # pragma: no cover
        return RepositoryCredentials.make_one(
            self.boto3_raw_data["repositoryCredentials"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContainerPropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContainerPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EksPodPropertiesOverride:
    boto3_raw_data: "type_defs.EksPodPropertiesOverrideTypeDef" = dataclasses.field()

    @cached_property
    def containers(self):  # pragma: no cover
        return EksContainerOverride.make_many(self.boto3_raw_data["containers"])

    @cached_property
    def initContainers(self):  # pragma: no cover
        return EksContainerOverride.make_many(self.boto3_raw_data["initContainers"])

    metadata = field("metadata")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EksPodPropertiesOverrideTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EksPodPropertiesOverrideTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EksPropertiesDetail:
    boto3_raw_data: "type_defs.EksPropertiesDetailTypeDef" = dataclasses.field()

    @cached_property
    def podProperties(self):  # pragma: no cover
        return EksPodPropertiesDetail.make_one(self.boto3_raw_data["podProperties"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EksPropertiesDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EksPropertiesDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EksPropertiesOutput:
    boto3_raw_data: "type_defs.EksPropertiesOutputTypeDef" = dataclasses.field()

    @cached_property
    def podProperties(self):  # pragma: no cover
        return EksPodPropertiesOutput.make_one(self.boto3_raw_data["podProperties"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EksPropertiesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EksPropertiesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EksProperties:
    boto3_raw_data: "type_defs.EksPropertiesTypeDef" = dataclasses.field()

    @cached_property
    def podProperties(self):  # pragma: no cover
        return EksPodProperties.make_one(self.boto3_raw_data["podProperties"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EksPropertiesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EksPropertiesTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSchedulingPoliciesResponse:
    boto3_raw_data: "type_defs.DescribeSchedulingPoliciesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def schedulingPolicies(self):  # pragma: no cover
        return SchedulingPolicyDetail.make_many(
            self.boto3_raw_data["schedulingPolicies"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeSchedulingPoliciesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSchedulingPoliciesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSchedulingPolicyRequest:
    boto3_raw_data: "type_defs.CreateSchedulingPolicyRequestTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    fairsharePolicy = field("fairsharePolicy")
    tags = field("tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateSchedulingPolicyRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSchedulingPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSchedulingPolicyRequest:
    boto3_raw_data: "type_defs.UpdateSchedulingPolicyRequestTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    fairsharePolicy = field("fairsharePolicy")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateSchedulingPolicyRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSchedulingPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServiceJobsResponse:
    boto3_raw_data: "type_defs.ListServiceJobsResponseTypeDef" = dataclasses.field()

    @cached_property
    def jobSummaryList(self):  # pragma: no cover
        return ServiceJobSummary.make_many(self.boto3_raw_data["jobSummaryList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListServiceJobsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServiceJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComputeEnvironmentDetail:
    boto3_raw_data: "type_defs.ComputeEnvironmentDetailTypeDef" = dataclasses.field()

    computeEnvironmentName = field("computeEnvironmentName")
    computeEnvironmentArn = field("computeEnvironmentArn")
    unmanagedvCpus = field("unmanagedvCpus")
    ecsClusterArn = field("ecsClusterArn")
    tags = field("tags")
    type = field("type")
    state = field("state")
    status = field("status")
    statusReason = field("statusReason")

    @cached_property
    def computeResources(self):  # pragma: no cover
        return ComputeResourceOutput.make_one(self.boto3_raw_data["computeResources"])

    serviceRole = field("serviceRole")

    @cached_property
    def updatePolicy(self):  # pragma: no cover
        return UpdatePolicy.make_one(self.boto3_raw_data["updatePolicy"])

    @cached_property
    def eksConfiguration(self):  # pragma: no cover
        return EksConfiguration.make_one(self.boto3_raw_data["eksConfiguration"])

    containerOrchestrationType = field("containerOrchestrationType")
    uuid = field("uuid")
    context = field("context")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ComputeEnvironmentDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComputeEnvironmentDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComputeResource:
    boto3_raw_data: "type_defs.ComputeResourceTypeDef" = dataclasses.field()

    type = field("type")
    maxvCpus = field("maxvCpus")
    subnets = field("subnets")
    allocationStrategy = field("allocationStrategy")
    minvCpus = field("minvCpus")
    desiredvCpus = field("desiredvCpus")
    instanceTypes = field("instanceTypes")
    imageId = field("imageId")
    securityGroupIds = field("securityGroupIds")
    ec2KeyPair = field("ec2KeyPair")
    instanceRole = field("instanceRole")
    tags = field("tags")
    placementGroup = field("placementGroup")
    bidPercentage = field("bidPercentage")
    spotIamFleetRole = field("spotIamFleetRole")

    @cached_property
    def launchTemplate(self):  # pragma: no cover
        return LaunchTemplateSpecification.make_one(
            self.boto3_raw_data["launchTemplate"]
        )

    @cached_property
    def ec2Configuration(self):  # pragma: no cover
        return Ec2Configuration.make_many(self.boto3_raw_data["ec2Configuration"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ComputeResourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ComputeResourceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EcsTaskDetails:
    boto3_raw_data: "type_defs.EcsTaskDetailsTypeDef" = dataclasses.field()

    @cached_property
    def containers(self):  # pragma: no cover
        return TaskContainerDetails.make_many(self.boto3_raw_data["containers"])

    containerInstanceArn = field("containerInstanceArn")
    taskArn = field("taskArn")

    @cached_property
    def ephemeralStorage(self):  # pragma: no cover
        return EphemeralStorage.make_one(self.boto3_raw_data["ephemeralStorage"])

    executionRoleArn = field("executionRoleArn")
    platformVersion = field("platformVersion")
    ipcMode = field("ipcMode")
    taskRoleArn = field("taskRoleArn")
    pidMode = field("pidMode")

    @cached_property
    def networkConfiguration(self):  # pragma: no cover
        return NetworkConfiguration.make_one(
            self.boto3_raw_data["networkConfiguration"]
        )

    @cached_property
    def runtimePlatform(self):  # pragma: no cover
        return RuntimePlatform.make_one(self.boto3_raw_data["runtimePlatform"])

    @cached_property
    def volumes(self):  # pragma: no cover
        return Volume.make_many(self.boto3_raw_data["volumes"])

    enableExecuteCommand = field("enableExecuteCommand")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EcsTaskDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EcsTaskDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EcsTaskPropertiesOutput:
    boto3_raw_data: "type_defs.EcsTaskPropertiesOutputTypeDef" = dataclasses.field()

    @cached_property
    def containers(self):  # pragma: no cover
        return TaskContainerPropertiesOutput.make_many(
            self.boto3_raw_data["containers"]
        )

    @cached_property
    def ephemeralStorage(self):  # pragma: no cover
        return EphemeralStorage.make_one(self.boto3_raw_data["ephemeralStorage"])

    executionRoleArn = field("executionRoleArn")
    platformVersion = field("platformVersion")
    ipcMode = field("ipcMode")
    taskRoleArn = field("taskRoleArn")
    pidMode = field("pidMode")

    @cached_property
    def networkConfiguration(self):  # pragma: no cover
        return NetworkConfiguration.make_one(
            self.boto3_raw_data["networkConfiguration"]
        )

    @cached_property
    def runtimePlatform(self):  # pragma: no cover
        return RuntimePlatform.make_one(self.boto3_raw_data["runtimePlatform"])

    @cached_property
    def volumes(self):  # pragma: no cover
        return Volume.make_many(self.boto3_raw_data["volumes"])

    enableExecuteCommand = field("enableExecuteCommand")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EcsTaskPropertiesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EcsTaskPropertiesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EcsTaskProperties:
    boto3_raw_data: "type_defs.EcsTaskPropertiesTypeDef" = dataclasses.field()

    @cached_property
    def containers(self):  # pragma: no cover
        return TaskContainerProperties.make_many(self.boto3_raw_data["containers"])

    @cached_property
    def ephemeralStorage(self):  # pragma: no cover
        return EphemeralStorage.make_one(self.boto3_raw_data["ephemeralStorage"])

    executionRoleArn = field("executionRoleArn")
    platformVersion = field("platformVersion")
    ipcMode = field("ipcMode")
    taskRoleArn = field("taskRoleArn")
    pidMode = field("pidMode")

    @cached_property
    def networkConfiguration(self):  # pragma: no cover
        return NetworkConfiguration.make_one(
            self.boto3_raw_data["networkConfiguration"]
        )

    @cached_property
    def runtimePlatform(self):  # pragma: no cover
        return RuntimePlatform.make_one(self.boto3_raw_data["runtimePlatform"])

    @cached_property
    def volumes(self):  # pragma: no cover
        return Volume.make_many(self.boto3_raw_data["volumes"])

    enableExecuteCommand = field("enableExecuteCommand")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EcsTaskPropertiesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EcsTaskPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SubmitServiceJobRequest:
    boto3_raw_data: "type_defs.SubmitServiceJobRequestTypeDef" = dataclasses.field()

    jobName = field("jobName")
    jobQueue = field("jobQueue")
    serviceRequestPayload = field("serviceRequestPayload")
    serviceJobType = field("serviceJobType")
    retryStrategy = field("retryStrategy")
    schedulingPriority = field("schedulingPriority")
    shareIdentifier = field("shareIdentifier")

    @cached_property
    def timeoutConfig(self):  # pragma: no cover
        return ServiceJobTimeout.make_one(self.boto3_raw_data["timeoutConfig"])

    tags = field("tags")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SubmitServiceJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SubmitServiceJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EksPropertiesOverride:
    boto3_raw_data: "type_defs.EksPropertiesOverrideTypeDef" = dataclasses.field()

    @cached_property
    def podProperties(self):  # pragma: no cover
        return EksPodPropertiesOverride.make_one(self.boto3_raw_data["podProperties"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EksPropertiesOverrideTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EksPropertiesOverrideTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeComputeEnvironmentsResponse:
    boto3_raw_data: "type_defs.DescribeComputeEnvironmentsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def computeEnvironments(self):  # pragma: no cover
        return ComputeEnvironmentDetail.make_many(
            self.boto3_raw_data["computeEnvironments"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeComputeEnvironmentsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeComputeEnvironmentsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComputeResourceUpdate:
    boto3_raw_data: "type_defs.ComputeResourceUpdateTypeDef" = dataclasses.field()

    minvCpus = field("minvCpus")
    maxvCpus = field("maxvCpus")
    desiredvCpus = field("desiredvCpus")
    subnets = field("subnets")
    securityGroupIds = field("securityGroupIds")
    allocationStrategy = field("allocationStrategy")
    instanceTypes = field("instanceTypes")
    ec2KeyPair = field("ec2KeyPair")
    instanceRole = field("instanceRole")
    tags = field("tags")
    placementGroup = field("placementGroup")
    bidPercentage = field("bidPercentage")
    launchTemplate = field("launchTemplate")

    @cached_property
    def ec2Configuration(self):  # pragma: no cover
        return Ec2Configuration.make_many(self.boto3_raw_data["ec2Configuration"])

    updateToLatestImageVersion = field("updateToLatestImageVersion")
    type = field("type")
    imageId = field("imageId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ComputeResourceUpdateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComputeResourceUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EcsPropertiesDetail:
    boto3_raw_data: "type_defs.EcsPropertiesDetailTypeDef" = dataclasses.field()

    @cached_property
    def taskProperties(self):  # pragma: no cover
        return EcsTaskDetails.make_many(self.boto3_raw_data["taskProperties"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EcsPropertiesDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EcsPropertiesDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EcsPropertiesOutput:
    boto3_raw_data: "type_defs.EcsPropertiesOutputTypeDef" = dataclasses.field()

    @cached_property
    def taskProperties(self):  # pragma: no cover
        return EcsTaskPropertiesOutput.make_many(self.boto3_raw_data["taskProperties"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EcsPropertiesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EcsPropertiesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EcsProperties:
    boto3_raw_data: "type_defs.EcsPropertiesTypeDef" = dataclasses.field()

    @cached_property
    def taskProperties(self):  # pragma: no cover
        return EcsTaskProperties.make_many(self.boto3_raw_data["taskProperties"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EcsPropertiesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EcsPropertiesTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NodePropertyOverride:
    boto3_raw_data: "type_defs.NodePropertyOverrideTypeDef" = dataclasses.field()

    targetNodes = field("targetNodes")

    @cached_property
    def containerOverrides(self):  # pragma: no cover
        return ContainerOverrides.make_one(self.boto3_raw_data["containerOverrides"])

    @cached_property
    def ecsPropertiesOverride(self):  # pragma: no cover
        return EcsPropertiesOverride.make_one(
            self.boto3_raw_data["ecsPropertiesOverride"]
        )

    instanceTypes = field("instanceTypes")

    @cached_property
    def eksPropertiesOverride(self):  # pragma: no cover
        return EksPropertiesOverride.make_one(
            self.boto3_raw_data["eksPropertiesOverride"]
        )

    consumableResourcePropertiesOverride = field("consumableResourcePropertiesOverride")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NodePropertyOverrideTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NodePropertyOverrideTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateComputeEnvironmentRequest:
    boto3_raw_data: "type_defs.CreateComputeEnvironmentRequestTypeDef" = (
        dataclasses.field()
    )

    computeEnvironmentName = field("computeEnvironmentName")
    type = field("type")
    state = field("state")
    unmanagedvCpus = field("unmanagedvCpus")
    computeResources = field("computeResources")
    serviceRole = field("serviceRole")
    tags = field("tags")

    @cached_property
    def eksConfiguration(self):  # pragma: no cover
        return EksConfiguration.make_one(self.boto3_raw_data["eksConfiguration"])

    context = field("context")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateComputeEnvironmentRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateComputeEnvironmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateComputeEnvironmentRequest:
    boto3_raw_data: "type_defs.UpdateComputeEnvironmentRequestTypeDef" = (
        dataclasses.field()
    )

    computeEnvironment = field("computeEnvironment")
    state = field("state")
    unmanagedvCpus = field("unmanagedvCpus")

    @cached_property
    def computeResources(self):  # pragma: no cover
        return ComputeResourceUpdate.make_one(self.boto3_raw_data["computeResources"])

    serviceRole = field("serviceRole")

    @cached_property
    def updatePolicy(self):  # pragma: no cover
        return UpdatePolicy.make_one(self.boto3_raw_data["updatePolicy"])

    context = field("context")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateComputeEnvironmentRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateComputeEnvironmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NodeRangePropertyOutput:
    boto3_raw_data: "type_defs.NodeRangePropertyOutputTypeDef" = dataclasses.field()

    targetNodes = field("targetNodes")

    @cached_property
    def container(self):  # pragma: no cover
        return ContainerPropertiesOutput.make_one(self.boto3_raw_data["container"])

    instanceTypes = field("instanceTypes")

    @cached_property
    def ecsProperties(self):  # pragma: no cover
        return EcsPropertiesOutput.make_one(self.boto3_raw_data["ecsProperties"])

    @cached_property
    def eksProperties(self):  # pragma: no cover
        return EksPropertiesOutput.make_one(self.boto3_raw_data["eksProperties"])

    @cached_property
    def consumableResourceProperties(self):  # pragma: no cover
        return ConsumableResourcePropertiesOutput.make_one(
            self.boto3_raw_data["consumableResourceProperties"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NodeRangePropertyOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NodeRangePropertyOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NodeRangeProperty:
    boto3_raw_data: "type_defs.NodeRangePropertyTypeDef" = dataclasses.field()

    targetNodes = field("targetNodes")

    @cached_property
    def container(self):  # pragma: no cover
        return ContainerProperties.make_one(self.boto3_raw_data["container"])

    instanceTypes = field("instanceTypes")

    @cached_property
    def ecsProperties(self):  # pragma: no cover
        return EcsProperties.make_one(self.boto3_raw_data["ecsProperties"])

    @cached_property
    def eksProperties(self):  # pragma: no cover
        return EksProperties.make_one(self.boto3_raw_data["eksProperties"])

    @cached_property
    def consumableResourceProperties(self):  # pragma: no cover
        return ConsumableResourceProperties.make_one(
            self.boto3_raw_data["consumableResourceProperties"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NodeRangePropertyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NodeRangePropertyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NodeOverrides:
    boto3_raw_data: "type_defs.NodeOverridesTypeDef" = dataclasses.field()

    numNodes = field("numNodes")

    @cached_property
    def nodePropertyOverrides(self):  # pragma: no cover
        return NodePropertyOverride.make_many(
            self.boto3_raw_data["nodePropertyOverrides"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NodeOverridesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.NodeOverridesTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NodePropertiesOutput:
    boto3_raw_data: "type_defs.NodePropertiesOutputTypeDef" = dataclasses.field()

    numNodes = field("numNodes")
    mainNode = field("mainNode")

    @cached_property
    def nodeRangeProperties(self):  # pragma: no cover
        return NodeRangePropertyOutput.make_many(
            self.boto3_raw_data["nodeRangeProperties"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NodePropertiesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NodePropertiesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NodeProperties:
    boto3_raw_data: "type_defs.NodePropertiesTypeDef" = dataclasses.field()

    numNodes = field("numNodes")
    mainNode = field("mainNode")

    @cached_property
    def nodeRangeProperties(self):  # pragma: no cover
        return NodeRangeProperty.make_many(self.boto3_raw_data["nodeRangeProperties"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NodePropertiesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.NodePropertiesTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SubmitJobRequest:
    boto3_raw_data: "type_defs.SubmitJobRequestTypeDef" = dataclasses.field()

    jobName = field("jobName")
    jobQueue = field("jobQueue")
    jobDefinition = field("jobDefinition")
    shareIdentifier = field("shareIdentifier")
    schedulingPriorityOverride = field("schedulingPriorityOverride")

    @cached_property
    def arrayProperties(self):  # pragma: no cover
        return ArrayProperties.make_one(self.boto3_raw_data["arrayProperties"])

    @cached_property
    def dependsOn(self):  # pragma: no cover
        return JobDependency.make_many(self.boto3_raw_data["dependsOn"])

    parameters = field("parameters")

    @cached_property
    def containerOverrides(self):  # pragma: no cover
        return ContainerOverrides.make_one(self.boto3_raw_data["containerOverrides"])

    @cached_property
    def nodeOverrides(self):  # pragma: no cover
        return NodeOverrides.make_one(self.boto3_raw_data["nodeOverrides"])

    retryStrategy = field("retryStrategy")
    propagateTags = field("propagateTags")

    @cached_property
    def timeout(self):  # pragma: no cover
        return JobTimeout.make_one(self.boto3_raw_data["timeout"])

    tags = field("tags")

    @cached_property
    def eksPropertiesOverride(self):  # pragma: no cover
        return EksPropertiesOverride.make_one(
            self.boto3_raw_data["eksPropertiesOverride"]
        )

    @cached_property
    def ecsPropertiesOverride(self):  # pragma: no cover
        return EcsPropertiesOverride.make_one(
            self.boto3_raw_data["ecsPropertiesOverride"]
        )

    consumableResourcePropertiesOverride = field("consumableResourcePropertiesOverride")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SubmitJobRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SubmitJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobDefinition:
    boto3_raw_data: "type_defs.JobDefinitionTypeDef" = dataclasses.field()

    jobDefinitionName = field("jobDefinitionName")
    jobDefinitionArn = field("jobDefinitionArn")
    revision = field("revision")
    type = field("type")
    status = field("status")
    schedulingPriority = field("schedulingPriority")
    parameters = field("parameters")

    @cached_property
    def retryStrategy(self):  # pragma: no cover
        return RetryStrategyOutput.make_one(self.boto3_raw_data["retryStrategy"])

    @cached_property
    def containerProperties(self):  # pragma: no cover
        return ContainerPropertiesOutput.make_one(
            self.boto3_raw_data["containerProperties"]
        )

    @cached_property
    def timeout(self):  # pragma: no cover
        return JobTimeout.make_one(self.boto3_raw_data["timeout"])

    @cached_property
    def nodeProperties(self):  # pragma: no cover
        return NodePropertiesOutput.make_one(self.boto3_raw_data["nodeProperties"])

    tags = field("tags")
    propagateTags = field("propagateTags")
    platformCapabilities = field("platformCapabilities")

    @cached_property
    def ecsProperties(self):  # pragma: no cover
        return EcsPropertiesOutput.make_one(self.boto3_raw_data["ecsProperties"])

    @cached_property
    def eksProperties(self):  # pragma: no cover
        return EksPropertiesOutput.make_one(self.boto3_raw_data["eksProperties"])

    containerOrchestrationType = field("containerOrchestrationType")

    @cached_property
    def consumableResourceProperties(self):  # pragma: no cover
        return ConsumableResourcePropertiesOutput.make_one(
            self.boto3_raw_data["consumableResourceProperties"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobDefinitionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JobDefinitionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobDetail:
    boto3_raw_data: "type_defs.JobDetailTypeDef" = dataclasses.field()

    jobName = field("jobName")
    jobId = field("jobId")
    jobQueue = field("jobQueue")
    status = field("status")
    startedAt = field("startedAt")
    jobDefinition = field("jobDefinition")
    jobArn = field("jobArn")
    shareIdentifier = field("shareIdentifier")
    schedulingPriority = field("schedulingPriority")

    @cached_property
    def attempts(self):  # pragma: no cover
        return AttemptDetail.make_many(self.boto3_raw_data["attempts"])

    statusReason = field("statusReason")
    createdAt = field("createdAt")

    @cached_property
    def retryStrategy(self):  # pragma: no cover
        return RetryStrategyOutput.make_one(self.boto3_raw_data["retryStrategy"])

    stoppedAt = field("stoppedAt")

    @cached_property
    def dependsOn(self):  # pragma: no cover
        return JobDependency.make_many(self.boto3_raw_data["dependsOn"])

    parameters = field("parameters")

    @cached_property
    def container(self):  # pragma: no cover
        return ContainerDetail.make_one(self.boto3_raw_data["container"])

    @cached_property
    def nodeDetails(self):  # pragma: no cover
        return NodeDetails.make_one(self.boto3_raw_data["nodeDetails"])

    @cached_property
    def nodeProperties(self):  # pragma: no cover
        return NodePropertiesOutput.make_one(self.boto3_raw_data["nodeProperties"])

    @cached_property
    def arrayProperties(self):  # pragma: no cover
        return ArrayPropertiesDetail.make_one(self.boto3_raw_data["arrayProperties"])

    @cached_property
    def timeout(self):  # pragma: no cover
        return JobTimeout.make_one(self.boto3_raw_data["timeout"])

    tags = field("tags")
    propagateTags = field("propagateTags")
    platformCapabilities = field("platformCapabilities")

    @cached_property
    def eksProperties(self):  # pragma: no cover
        return EksPropertiesDetail.make_one(self.boto3_raw_data["eksProperties"])

    @cached_property
    def eksAttempts(self):  # pragma: no cover
        return EksAttemptDetail.make_many(self.boto3_raw_data["eksAttempts"])

    @cached_property
    def ecsProperties(self):  # pragma: no cover
        return EcsPropertiesDetail.make_one(self.boto3_raw_data["ecsProperties"])

    isCancelled = field("isCancelled")
    isTerminated = field("isTerminated")

    @cached_property
    def consumableResourceProperties(self):  # pragma: no cover
        return ConsumableResourcePropertiesOutput.make_one(
            self.boto3_raw_data["consumableResourceProperties"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JobDetailTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeJobDefinitionsResponse:
    boto3_raw_data: "type_defs.DescribeJobDefinitionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def jobDefinitions(self):  # pragma: no cover
        return JobDefinition.make_many(self.boto3_raw_data["jobDefinitions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeJobDefinitionsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeJobDefinitionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeJobsResponse:
    boto3_raw_data: "type_defs.DescribeJobsResponseTypeDef" = dataclasses.field()

    @cached_property
    def jobs(self):  # pragma: no cover
        return JobDetail.make_many(self.boto3_raw_data["jobs"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeJobsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterJobDefinitionRequest:
    boto3_raw_data: "type_defs.RegisterJobDefinitionRequestTypeDef" = (
        dataclasses.field()
    )

    jobDefinitionName = field("jobDefinitionName")
    type = field("type")
    parameters = field("parameters")
    schedulingPriority = field("schedulingPriority")
    containerProperties = field("containerProperties")
    nodeProperties = field("nodeProperties")
    retryStrategy = field("retryStrategy")
    propagateTags = field("propagateTags")

    @cached_property
    def timeout(self):  # pragma: no cover
        return JobTimeout.make_one(self.boto3_raw_data["timeout"])

    tags = field("tags")
    platformCapabilities = field("platformCapabilities")
    eksProperties = field("eksProperties")
    ecsProperties = field("ecsProperties")
    consumableResourceProperties = field("consumableResourceProperties")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RegisterJobDefinitionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterJobDefinitionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
