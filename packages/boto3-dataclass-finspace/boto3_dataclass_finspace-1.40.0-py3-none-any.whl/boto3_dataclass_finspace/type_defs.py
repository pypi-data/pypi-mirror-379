# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_finspace import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AutoScalingConfiguration:
    boto3_raw_data: "type_defs.AutoScalingConfigurationTypeDef" = dataclasses.field()

    minNodeCount = field("minNodeCount")
    maxNodeCount = field("maxNodeCount")
    autoScalingMetric = field("autoScalingMetric")
    metricTarget = field("metricTarget")
    scaleInCooldownSeconds = field("scaleInCooldownSeconds")
    scaleOutCooldownSeconds = field("scaleOutCooldownSeconds")

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
class CapacityConfiguration:
    boto3_raw_data: "type_defs.CapacityConfigurationTypeDef" = dataclasses.field()

    nodeType = field("nodeType")
    nodeCount = field("nodeCount")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CapacityConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CapacityConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChangeRequest:
    boto3_raw_data: "type_defs.ChangeRequestTypeDef" = dataclasses.field()

    changeType = field("changeType")
    dbPath = field("dbPath")
    s3Path = field("s3Path")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ChangeRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ChangeRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CodeConfiguration:
    boto3_raw_data: "type_defs.CodeConfigurationTypeDef" = dataclasses.field()

    s3Bucket = field("s3Bucket")
    s3Key = field("s3Key")
    s3ObjectVersion = field("s3ObjectVersion")

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
class SuperuserParameters:
    boto3_raw_data: "type_defs.SuperuserParametersTypeDef" = dataclasses.field()

    emailAddress = field("emailAddress")
    firstName = field("firstName")
    lastName = field("lastName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SuperuserParametersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SuperuserParametersTypeDef"]
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
class ErrorInfo:
    boto3_raw_data: "type_defs.ErrorInfoTypeDef" = dataclasses.field()

    errorMessage = field("errorMessage")
    errorType = field("errorType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ErrorInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ErrorInfoTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KxCacheStorageConfiguration:
    boto3_raw_data: "type_defs.KxCacheStorageConfigurationTypeDef" = dataclasses.field()

    type = field("type")
    size = field("size")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KxCacheStorageConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KxCacheStorageConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KxCommandLineArgument:
    boto3_raw_data: "type_defs.KxCommandLineArgumentTypeDef" = dataclasses.field()

    key = field("key")
    value = field("value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KxCommandLineArgumentTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KxCommandLineArgumentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KxSavedownStorageConfiguration:
    boto3_raw_data: "type_defs.KxSavedownStorageConfigurationTypeDef" = (
        dataclasses.field()
    )

    type = field("type")
    size = field("size")
    volumeName = field("volumeName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.KxSavedownStorageConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KxSavedownStorageConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KxScalingGroupConfiguration:
    boto3_raw_data: "type_defs.KxScalingGroupConfigurationTypeDef" = dataclasses.field()

    scalingGroupName = field("scalingGroupName")
    memoryReservation = field("memoryReservation")
    nodeCount = field("nodeCount")
    memoryLimit = field("memoryLimit")
    cpu = field("cpu")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KxScalingGroupConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KxScalingGroupConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TickerplantLogConfigurationOutput:
    boto3_raw_data: "type_defs.TickerplantLogConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    tickerplantLogVolumes = field("tickerplantLogVolumes")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.TickerplantLogConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TickerplantLogConfigurationOutputTypeDef"]
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

    volumeName = field("volumeName")
    volumeType = field("volumeType")

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
class VpcConfigurationOutput:
    boto3_raw_data: "type_defs.VpcConfigurationOutputTypeDef" = dataclasses.field()

    vpcId = field("vpcId")
    securityGroupIds = field("securityGroupIds")
    subnetIds = field("subnetIds")
    ipAddressType = field("ipAddressType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VpcConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VpcConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateKxDatabaseRequest:
    boto3_raw_data: "type_defs.CreateKxDatabaseRequestTypeDef" = dataclasses.field()

    environmentId = field("environmentId")
    databaseName = field("databaseName")
    clientToken = field("clientToken")
    description = field("description")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateKxDatabaseRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateKxDatabaseRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KxDataviewSegmentConfigurationOutput:
    boto3_raw_data: "type_defs.KxDataviewSegmentConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    dbPaths = field("dbPaths")
    volumeName = field("volumeName")
    onDemand = field("onDemand")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.KxDataviewSegmentConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KxDataviewSegmentConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateKxEnvironmentRequest:
    boto3_raw_data: "type_defs.CreateKxEnvironmentRequestTypeDef" = dataclasses.field()

    name = field("name")
    kmsKeyId = field("kmsKeyId")
    description = field("description")
    tags = field("tags")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateKxEnvironmentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateKxEnvironmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateKxScalingGroupRequest:
    boto3_raw_data: "type_defs.CreateKxScalingGroupRequestTypeDef" = dataclasses.field()

    clientToken = field("clientToken")
    environmentId = field("environmentId")
    scalingGroupName = field("scalingGroupName")
    hostType = field("hostType")
    availabilityZoneId = field("availabilityZoneId")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateKxScalingGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateKxScalingGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateKxUserRequest:
    boto3_raw_data: "type_defs.CreateKxUserRequestTypeDef" = dataclasses.field()

    environmentId = field("environmentId")
    userName = field("userName")
    iamRole = field("iamRole")
    tags = field("tags")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateKxUserRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateKxUserRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KxNAS1Configuration:
    boto3_raw_data: "type_defs.KxNAS1ConfigurationTypeDef" = dataclasses.field()

    type = field("type")
    size = field("size")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KxNAS1ConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KxNAS1ConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomDNSServer:
    boto3_raw_data: "type_defs.CustomDNSServerTypeDef" = dataclasses.field()

    customDNSServerName = field("customDNSServerName")
    customDNSServerIP = field("customDNSServerIP")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CustomDNSServerTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CustomDNSServerTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteEnvironmentRequest:
    boto3_raw_data: "type_defs.DeleteEnvironmentRequestTypeDef" = dataclasses.field()

    environmentId = field("environmentId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteEnvironmentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteEnvironmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteKxClusterNodeRequest:
    boto3_raw_data: "type_defs.DeleteKxClusterNodeRequestTypeDef" = dataclasses.field()

    environmentId = field("environmentId")
    clusterName = field("clusterName")
    nodeId = field("nodeId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteKxClusterNodeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteKxClusterNodeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteKxClusterRequest:
    boto3_raw_data: "type_defs.DeleteKxClusterRequestTypeDef" = dataclasses.field()

    environmentId = field("environmentId")
    clusterName = field("clusterName")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteKxClusterRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteKxClusterRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteKxDatabaseRequest:
    boto3_raw_data: "type_defs.DeleteKxDatabaseRequestTypeDef" = dataclasses.field()

    environmentId = field("environmentId")
    databaseName = field("databaseName")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteKxDatabaseRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteKxDatabaseRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteKxDataviewRequest:
    boto3_raw_data: "type_defs.DeleteKxDataviewRequestTypeDef" = dataclasses.field()

    environmentId = field("environmentId")
    databaseName = field("databaseName")
    dataviewName = field("dataviewName")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteKxDataviewRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteKxDataviewRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteKxEnvironmentRequest:
    boto3_raw_data: "type_defs.DeleteKxEnvironmentRequestTypeDef" = dataclasses.field()

    environmentId = field("environmentId")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteKxEnvironmentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteKxEnvironmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteKxScalingGroupRequest:
    boto3_raw_data: "type_defs.DeleteKxScalingGroupRequestTypeDef" = dataclasses.field()

    environmentId = field("environmentId")
    scalingGroupName = field("scalingGroupName")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteKxScalingGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteKxScalingGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteKxUserRequest:
    boto3_raw_data: "type_defs.DeleteKxUserRequestTypeDef" = dataclasses.field()

    userName = field("userName")
    environmentId = field("environmentId")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteKxUserRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteKxUserRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteKxVolumeRequest:
    boto3_raw_data: "type_defs.DeleteKxVolumeRequestTypeDef" = dataclasses.field()

    environmentId = field("environmentId")
    volumeName = field("volumeName")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteKxVolumeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteKxVolumeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FederationParametersOutput:
    boto3_raw_data: "type_defs.FederationParametersOutputTypeDef" = dataclasses.field()

    samlMetadataDocument = field("samlMetadataDocument")
    samlMetadataURL = field("samlMetadataURL")
    applicationCallBackURL = field("applicationCallBackURL")
    federationURN = field("federationURN")
    federationProviderName = field("federationProviderName")
    attributeMap = field("attributeMap")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FederationParametersOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FederationParametersOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FederationParameters:
    boto3_raw_data: "type_defs.FederationParametersTypeDef" = dataclasses.field()

    samlMetadataDocument = field("samlMetadataDocument")
    samlMetadataURL = field("samlMetadataURL")
    applicationCallBackURL = field("applicationCallBackURL")
    federationURN = field("federationURN")
    federationProviderName = field("federationProviderName")
    attributeMap = field("attributeMap")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FederationParametersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FederationParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEnvironmentRequest:
    boto3_raw_data: "type_defs.GetEnvironmentRequestTypeDef" = dataclasses.field()

    environmentId = field("environmentId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetEnvironmentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEnvironmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetKxChangesetRequest:
    boto3_raw_data: "type_defs.GetKxChangesetRequestTypeDef" = dataclasses.field()

    environmentId = field("environmentId")
    databaseName = field("databaseName")
    changesetId = field("changesetId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetKxChangesetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetKxChangesetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetKxClusterRequest:
    boto3_raw_data: "type_defs.GetKxClusterRequestTypeDef" = dataclasses.field()

    environmentId = field("environmentId")
    clusterName = field("clusterName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetKxClusterRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetKxClusterRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetKxConnectionStringRequest:
    boto3_raw_data: "type_defs.GetKxConnectionStringRequestTypeDef" = (
        dataclasses.field()
    )

    userArn = field("userArn")
    environmentId = field("environmentId")
    clusterName = field("clusterName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetKxConnectionStringRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetKxConnectionStringRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetKxDatabaseRequest:
    boto3_raw_data: "type_defs.GetKxDatabaseRequestTypeDef" = dataclasses.field()

    environmentId = field("environmentId")
    databaseName = field("databaseName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetKxDatabaseRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetKxDatabaseRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetKxDataviewRequest:
    boto3_raw_data: "type_defs.GetKxDataviewRequestTypeDef" = dataclasses.field()

    environmentId = field("environmentId")
    databaseName = field("databaseName")
    dataviewName = field("dataviewName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetKxDataviewRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetKxDataviewRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetKxEnvironmentRequest:
    boto3_raw_data: "type_defs.GetKxEnvironmentRequestTypeDef" = dataclasses.field()

    environmentId = field("environmentId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetKxEnvironmentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetKxEnvironmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetKxScalingGroupRequest:
    boto3_raw_data: "type_defs.GetKxScalingGroupRequestTypeDef" = dataclasses.field()

    environmentId = field("environmentId")
    scalingGroupName = field("scalingGroupName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetKxScalingGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetKxScalingGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetKxUserRequest:
    boto3_raw_data: "type_defs.GetKxUserRequestTypeDef" = dataclasses.field()

    userName = field("userName")
    environmentId = field("environmentId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetKxUserRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetKxUserRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetKxVolumeRequest:
    boto3_raw_data: "type_defs.GetKxVolumeRequestTypeDef" = dataclasses.field()

    environmentId = field("environmentId")
    volumeName = field("volumeName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetKxVolumeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetKxVolumeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KxAttachedCluster:
    boto3_raw_data: "type_defs.KxAttachedClusterTypeDef" = dataclasses.field()

    clusterName = field("clusterName")
    clusterType = field("clusterType")
    clusterStatus = field("clusterStatus")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.KxAttachedClusterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KxAttachedClusterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IcmpTypeCode:
    boto3_raw_data: "type_defs.IcmpTypeCodeTypeDef" = dataclasses.field()

    type = field("type")
    code = field("code")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IcmpTypeCodeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IcmpTypeCodeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KxChangesetListEntry:
    boto3_raw_data: "type_defs.KxChangesetListEntryTypeDef" = dataclasses.field()

    changesetId = field("changesetId")
    createdTimestamp = field("createdTimestamp")
    activeFromTimestamp = field("activeFromTimestamp")
    lastModifiedTimestamp = field("lastModifiedTimestamp")
    status = field("status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KxChangesetListEntryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KxChangesetListEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KxClusterCodeDeploymentConfiguration:
    boto3_raw_data: "type_defs.KxClusterCodeDeploymentConfigurationTypeDef" = (
        dataclasses.field()
    )

    deploymentStrategy = field("deploymentStrategy")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.KxClusterCodeDeploymentConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KxClusterCodeDeploymentConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KxDatabaseCacheConfigurationOutput:
    boto3_raw_data: "type_defs.KxDatabaseCacheConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    cacheType = field("cacheType")
    dbPaths = field("dbPaths")
    dataviewName = field("dataviewName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.KxDatabaseCacheConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KxDatabaseCacheConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KxDatabaseCacheConfiguration:
    boto3_raw_data: "type_defs.KxDatabaseCacheConfigurationTypeDef" = (
        dataclasses.field()
    )

    cacheType = field("cacheType")
    dbPaths = field("dbPaths")
    dataviewName = field("dataviewName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KxDatabaseCacheConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KxDatabaseCacheConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KxDatabaseListEntry:
    boto3_raw_data: "type_defs.KxDatabaseListEntryTypeDef" = dataclasses.field()

    databaseName = field("databaseName")
    createdTimestamp = field("createdTimestamp")
    lastModifiedTimestamp = field("lastModifiedTimestamp")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KxDatabaseListEntryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KxDatabaseListEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KxDataviewSegmentConfiguration:
    boto3_raw_data: "type_defs.KxDataviewSegmentConfigurationTypeDef" = (
        dataclasses.field()
    )

    dbPaths = field("dbPaths")
    volumeName = field("volumeName")
    onDemand = field("onDemand")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.KxDataviewSegmentConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KxDataviewSegmentConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KxDeploymentConfiguration:
    boto3_raw_data: "type_defs.KxDeploymentConfigurationTypeDef" = dataclasses.field()

    deploymentStrategy = field("deploymentStrategy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KxDeploymentConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KxDeploymentConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KxNode:
    boto3_raw_data: "type_defs.KxNodeTypeDef" = dataclasses.field()

    nodeId = field("nodeId")
    availabilityZoneId = field("availabilityZoneId")
    launchTime = field("launchTime")
    status = field("status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.KxNodeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.KxNodeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KxScalingGroup:
    boto3_raw_data: "type_defs.KxScalingGroupTypeDef" = dataclasses.field()

    scalingGroupName = field("scalingGroupName")
    hostType = field("hostType")
    clusters = field("clusters")
    availabilityZoneId = field("availabilityZoneId")
    status = field("status")
    statusReason = field("statusReason")
    lastModifiedTimestamp = field("lastModifiedTimestamp")
    createdTimestamp = field("createdTimestamp")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.KxScalingGroupTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.KxScalingGroupTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KxUser:
    boto3_raw_data: "type_defs.KxUserTypeDef" = dataclasses.field()

    userArn = field("userArn")
    userName = field("userName")
    iamRole = field("iamRole")
    createTimestamp = field("createTimestamp")
    updateTimestamp = field("updateTimestamp")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.KxUserTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.KxUserTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KxVolume:
    boto3_raw_data: "type_defs.KxVolumeTypeDef" = dataclasses.field()

    volumeName = field("volumeName")
    volumeType = field("volumeType")
    status = field("status")
    description = field("description")
    statusReason = field("statusReason")
    azMode = field("azMode")
    availabilityZoneIds = field("availabilityZoneIds")
    createdTimestamp = field("createdTimestamp")
    lastModifiedTimestamp = field("lastModifiedTimestamp")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.KxVolumeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.KxVolumeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEnvironmentsRequest:
    boto3_raw_data: "type_defs.ListEnvironmentsRequestTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEnvironmentsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEnvironmentsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListKxChangesetsRequest:
    boto3_raw_data: "type_defs.ListKxChangesetsRequestTypeDef" = dataclasses.field()

    environmentId = field("environmentId")
    databaseName = field("databaseName")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListKxChangesetsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListKxChangesetsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListKxClusterNodesRequest:
    boto3_raw_data: "type_defs.ListKxClusterNodesRequestTypeDef" = dataclasses.field()

    environmentId = field("environmentId")
    clusterName = field("clusterName")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListKxClusterNodesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListKxClusterNodesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListKxClustersRequest:
    boto3_raw_data: "type_defs.ListKxClustersRequestTypeDef" = dataclasses.field()

    environmentId = field("environmentId")
    clusterType = field("clusterType")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListKxClustersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListKxClustersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListKxDatabasesRequest:
    boto3_raw_data: "type_defs.ListKxDatabasesRequestTypeDef" = dataclasses.field()

    environmentId = field("environmentId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListKxDatabasesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListKxDatabasesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListKxDataviewsRequest:
    boto3_raw_data: "type_defs.ListKxDataviewsRequestTypeDef" = dataclasses.field()

    environmentId = field("environmentId")
    databaseName = field("databaseName")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListKxDataviewsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListKxDataviewsRequestTypeDef"]
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
class ListKxEnvironmentsRequest:
    boto3_raw_data: "type_defs.ListKxEnvironmentsRequestTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListKxEnvironmentsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListKxEnvironmentsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListKxScalingGroupsRequest:
    boto3_raw_data: "type_defs.ListKxScalingGroupsRequestTypeDef" = dataclasses.field()

    environmentId = field("environmentId")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListKxScalingGroupsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListKxScalingGroupsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListKxUsersRequest:
    boto3_raw_data: "type_defs.ListKxUsersRequestTypeDef" = dataclasses.field()

    environmentId = field("environmentId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListKxUsersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListKxUsersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListKxVolumesRequest:
    boto3_raw_data: "type_defs.ListKxVolumesRequestTypeDef" = dataclasses.field()

    environmentId = field("environmentId")
    maxResults = field("maxResults")
    nextToken = field("nextToken")
    volumeType = field("volumeType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListKxVolumesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListKxVolumesRequestTypeDef"]
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
class PortRange:
    boto3_raw_data: "type_defs.PortRangeTypeDef" = dataclasses.field()

    from_ = field("from")
    to = field("to")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PortRangeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PortRangeTypeDef"]]
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
class TickerplantLogConfiguration:
    boto3_raw_data: "type_defs.TickerplantLogConfigurationTypeDef" = dataclasses.field()

    tickerplantLogVolumes = field("tickerplantLogVolumes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TickerplantLogConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TickerplantLogConfigurationTypeDef"]
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
class UpdateKxDatabaseRequest:
    boto3_raw_data: "type_defs.UpdateKxDatabaseRequestTypeDef" = dataclasses.field()

    environmentId = field("environmentId")
    databaseName = field("databaseName")
    clientToken = field("clientToken")
    description = field("description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateKxDatabaseRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateKxDatabaseRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateKxEnvironmentRequest:
    boto3_raw_data: "type_defs.UpdateKxEnvironmentRequestTypeDef" = dataclasses.field()

    environmentId = field("environmentId")
    name = field("name")
    description = field("description")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateKxEnvironmentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateKxEnvironmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateKxUserRequest:
    boto3_raw_data: "type_defs.UpdateKxUserRequestTypeDef" = dataclasses.field()

    environmentId = field("environmentId")
    userName = field("userName")
    iamRole = field("iamRole")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateKxUserRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateKxUserRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VpcConfiguration:
    boto3_raw_data: "type_defs.VpcConfigurationTypeDef" = dataclasses.field()

    vpcId = field("vpcId")
    securityGroupIds = field("securityGroupIds")
    subnetIds = field("subnetIds")
    ipAddressType = field("ipAddressType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VpcConfigurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VpcConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateKxChangesetRequest:
    boto3_raw_data: "type_defs.CreateKxChangesetRequestTypeDef" = dataclasses.field()

    environmentId = field("environmentId")
    databaseName = field("databaseName")

    @cached_property
    def changeRequests(self):  # pragma: no cover
        return ChangeRequest.make_many(self.boto3_raw_data["changeRequests"])

    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateKxChangesetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateKxChangesetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEnvironmentResponse:
    boto3_raw_data: "type_defs.CreateEnvironmentResponseTypeDef" = dataclasses.field()

    environmentId = field("environmentId")
    environmentArn = field("environmentArn")
    environmentUrl = field("environmentUrl")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateEnvironmentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEnvironmentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateKxDatabaseResponse:
    boto3_raw_data: "type_defs.CreateKxDatabaseResponseTypeDef" = dataclasses.field()

    databaseName = field("databaseName")
    databaseArn = field("databaseArn")
    environmentId = field("environmentId")
    description = field("description")
    createdTimestamp = field("createdTimestamp")
    lastModifiedTimestamp = field("lastModifiedTimestamp")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateKxDatabaseResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateKxDatabaseResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateKxEnvironmentResponse:
    boto3_raw_data: "type_defs.CreateKxEnvironmentResponseTypeDef" = dataclasses.field()

    name = field("name")
    status = field("status")
    environmentId = field("environmentId")
    description = field("description")
    environmentArn = field("environmentArn")
    kmsKeyId = field("kmsKeyId")
    creationTimestamp = field("creationTimestamp")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateKxEnvironmentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateKxEnvironmentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateKxScalingGroupResponse:
    boto3_raw_data: "type_defs.CreateKxScalingGroupResponseTypeDef" = (
        dataclasses.field()
    )

    environmentId = field("environmentId")
    scalingGroupName = field("scalingGroupName")
    hostType = field("hostType")
    availabilityZoneId = field("availabilityZoneId")
    status = field("status")
    lastModifiedTimestamp = field("lastModifiedTimestamp")
    createdTimestamp = field("createdTimestamp")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateKxScalingGroupResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateKxScalingGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateKxUserResponse:
    boto3_raw_data: "type_defs.CreateKxUserResponseTypeDef" = dataclasses.field()

    userName = field("userName")
    userArn = field("userArn")
    environmentId = field("environmentId")
    iamRole = field("iamRole")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateKxUserResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateKxUserResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetKxConnectionStringResponse:
    boto3_raw_data: "type_defs.GetKxConnectionStringResponseTypeDef" = (
        dataclasses.field()
    )

    signedConnectionString = field("signedConnectionString")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetKxConnectionStringResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetKxConnectionStringResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetKxDatabaseResponse:
    boto3_raw_data: "type_defs.GetKxDatabaseResponseTypeDef" = dataclasses.field()

    databaseName = field("databaseName")
    databaseArn = field("databaseArn")
    environmentId = field("environmentId")
    description = field("description")
    createdTimestamp = field("createdTimestamp")
    lastModifiedTimestamp = field("lastModifiedTimestamp")
    lastCompletedChangesetId = field("lastCompletedChangesetId")
    numBytes = field("numBytes")
    numChangesets = field("numChangesets")
    numFiles = field("numFiles")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetKxDatabaseResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetKxDatabaseResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetKxScalingGroupResponse:
    boto3_raw_data: "type_defs.GetKxScalingGroupResponseTypeDef" = dataclasses.field()

    scalingGroupName = field("scalingGroupName")
    scalingGroupArn = field("scalingGroupArn")
    hostType = field("hostType")
    clusters = field("clusters")
    availabilityZoneId = field("availabilityZoneId")
    status = field("status")
    statusReason = field("statusReason")
    lastModifiedTimestamp = field("lastModifiedTimestamp")
    createdTimestamp = field("createdTimestamp")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetKxScalingGroupResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetKxScalingGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetKxUserResponse:
    boto3_raw_data: "type_defs.GetKxUserResponseTypeDef" = dataclasses.field()

    userName = field("userName")
    userArn = field("userArn")
    environmentId = field("environmentId")
    iamRole = field("iamRole")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetKxUserResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetKxUserResponseTypeDef"]
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
class UpdateKxDatabaseResponse:
    boto3_raw_data: "type_defs.UpdateKxDatabaseResponseTypeDef" = dataclasses.field()

    databaseName = field("databaseName")
    environmentId = field("environmentId")
    description = field("description")
    lastModifiedTimestamp = field("lastModifiedTimestamp")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateKxDatabaseResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateKxDatabaseResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateKxUserResponse:
    boto3_raw_data: "type_defs.UpdateKxUserResponseTypeDef" = dataclasses.field()

    userName = field("userName")
    userArn = field("userArn")
    environmentId = field("environmentId")
    iamRole = field("iamRole")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateKxUserResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateKxUserResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateKxChangesetResponse:
    boto3_raw_data: "type_defs.CreateKxChangesetResponseTypeDef" = dataclasses.field()

    changesetId = field("changesetId")
    databaseName = field("databaseName")
    environmentId = field("environmentId")

    @cached_property
    def changeRequests(self):  # pragma: no cover
        return ChangeRequest.make_many(self.boto3_raw_data["changeRequests"])

    createdTimestamp = field("createdTimestamp")
    lastModifiedTimestamp = field("lastModifiedTimestamp")
    status = field("status")

    @cached_property
    def errorInfo(self):  # pragma: no cover
        return ErrorInfo.make_one(self.boto3_raw_data["errorInfo"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateKxChangesetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateKxChangesetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetKxChangesetResponse:
    boto3_raw_data: "type_defs.GetKxChangesetResponseTypeDef" = dataclasses.field()

    changesetId = field("changesetId")
    databaseName = field("databaseName")
    environmentId = field("environmentId")

    @cached_property
    def changeRequests(self):  # pragma: no cover
        return ChangeRequest.make_many(self.boto3_raw_data["changeRequests"])

    createdTimestamp = field("createdTimestamp")
    activeFromTimestamp = field("activeFromTimestamp")
    lastModifiedTimestamp = field("lastModifiedTimestamp")
    status = field("status")

    @cached_property
    def errorInfo(self):  # pragma: no cover
        return ErrorInfo.make_one(self.boto3_raw_data["errorInfo"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetKxChangesetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetKxChangesetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KxCluster:
    boto3_raw_data: "type_defs.KxClusterTypeDef" = dataclasses.field()

    status = field("status")
    statusReason = field("statusReason")
    clusterName = field("clusterName")
    clusterType = field("clusterType")
    clusterDescription = field("clusterDescription")
    releaseLabel = field("releaseLabel")

    @cached_property
    def volumes(self):  # pragma: no cover
        return Volume.make_many(self.boto3_raw_data["volumes"])

    initializationScript = field("initializationScript")
    executionRole = field("executionRole")
    azMode = field("azMode")
    availabilityZoneId = field("availabilityZoneId")
    lastModifiedTimestamp = field("lastModifiedTimestamp")
    createdTimestamp = field("createdTimestamp")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.KxClusterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.KxClusterTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateKxDataviewResponse:
    boto3_raw_data: "type_defs.CreateKxDataviewResponseTypeDef" = dataclasses.field()

    dataviewName = field("dataviewName")
    databaseName = field("databaseName")
    environmentId = field("environmentId")
    azMode = field("azMode")
    availabilityZoneId = field("availabilityZoneId")
    changesetId = field("changesetId")

    @cached_property
    def segmentConfigurations(self):  # pragma: no cover
        return KxDataviewSegmentConfigurationOutput.make_many(
            self.boto3_raw_data["segmentConfigurations"]
        )

    description = field("description")
    autoUpdate = field("autoUpdate")
    readWrite = field("readWrite")
    createdTimestamp = field("createdTimestamp")
    lastModifiedTimestamp = field("lastModifiedTimestamp")
    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateKxDataviewResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateKxDataviewResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KxDataviewActiveVersion:
    boto3_raw_data: "type_defs.KxDataviewActiveVersionTypeDef" = dataclasses.field()

    changesetId = field("changesetId")

    @cached_property
    def segmentConfigurations(self):  # pragma: no cover
        return KxDataviewSegmentConfigurationOutput.make_many(
            self.boto3_raw_data["segmentConfigurations"]
        )

    attachedClusters = field("attachedClusters")
    createdTimestamp = field("createdTimestamp")
    versionId = field("versionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KxDataviewActiveVersionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KxDataviewActiveVersionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KxDataviewConfigurationOutput:
    boto3_raw_data: "type_defs.KxDataviewConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    dataviewName = field("dataviewName")
    dataviewVersionId = field("dataviewVersionId")
    changesetId = field("changesetId")

    @cached_property
    def segmentConfigurations(self):  # pragma: no cover
        return KxDataviewSegmentConfigurationOutput.make_many(
            self.boto3_raw_data["segmentConfigurations"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.KxDataviewConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KxDataviewConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateKxVolumeRequest:
    boto3_raw_data: "type_defs.CreateKxVolumeRequestTypeDef" = dataclasses.field()

    environmentId = field("environmentId")
    volumeType = field("volumeType")
    volumeName = field("volumeName")
    azMode = field("azMode")
    availabilityZoneIds = field("availabilityZoneIds")
    clientToken = field("clientToken")
    description = field("description")

    @cached_property
    def nas1Configuration(self):  # pragma: no cover
        return KxNAS1Configuration.make_one(self.boto3_raw_data["nas1Configuration"])

    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateKxVolumeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateKxVolumeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateKxVolumeResponse:
    boto3_raw_data: "type_defs.CreateKxVolumeResponseTypeDef" = dataclasses.field()

    environmentId = field("environmentId")
    volumeName = field("volumeName")
    volumeType = field("volumeType")
    volumeArn = field("volumeArn")

    @cached_property
    def nas1Configuration(self):  # pragma: no cover
        return KxNAS1Configuration.make_one(self.boto3_raw_data["nas1Configuration"])

    status = field("status")
    statusReason = field("statusReason")
    azMode = field("azMode")
    description = field("description")
    availabilityZoneIds = field("availabilityZoneIds")
    createdTimestamp = field("createdTimestamp")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateKxVolumeResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateKxVolumeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateKxVolumeRequest:
    boto3_raw_data: "type_defs.UpdateKxVolumeRequestTypeDef" = dataclasses.field()

    environmentId = field("environmentId")
    volumeName = field("volumeName")
    description = field("description")
    clientToken = field("clientToken")

    @cached_property
    def nas1Configuration(self):  # pragma: no cover
        return KxNAS1Configuration.make_one(self.boto3_raw_data["nas1Configuration"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateKxVolumeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateKxVolumeRequestTypeDef"]
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

    name = field("name")
    environmentId = field("environmentId")
    awsAccountId = field("awsAccountId")
    status = field("status")
    environmentUrl = field("environmentUrl")
    description = field("description")
    environmentArn = field("environmentArn")
    sageMakerStudioDomainUrl = field("sageMakerStudioDomainUrl")
    kmsKeyId = field("kmsKeyId")
    dedicatedServiceAccountId = field("dedicatedServiceAccountId")
    federationMode = field("federationMode")

    @cached_property
    def federationParameters(self):  # pragma: no cover
        return FederationParametersOutput.make_one(
            self.boto3_raw_data["federationParameters"]
        )

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
class GetKxVolumeResponse:
    boto3_raw_data: "type_defs.GetKxVolumeResponseTypeDef" = dataclasses.field()

    environmentId = field("environmentId")
    volumeName = field("volumeName")
    volumeType = field("volumeType")
    volumeArn = field("volumeArn")

    @cached_property
    def nas1Configuration(self):  # pragma: no cover
        return KxNAS1Configuration.make_one(self.boto3_raw_data["nas1Configuration"])

    status = field("status")
    statusReason = field("statusReason")
    createdTimestamp = field("createdTimestamp")
    description = field("description")
    azMode = field("azMode")
    availabilityZoneIds = field("availabilityZoneIds")
    lastModifiedTimestamp = field("lastModifiedTimestamp")

    @cached_property
    def attachedClusters(self):  # pragma: no cover
        return KxAttachedCluster.make_many(self.boto3_raw_data["attachedClusters"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetKxVolumeResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetKxVolumeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateKxVolumeResponse:
    boto3_raw_data: "type_defs.UpdateKxVolumeResponseTypeDef" = dataclasses.field()

    environmentId = field("environmentId")
    volumeName = field("volumeName")
    volumeType = field("volumeType")
    volumeArn = field("volumeArn")

    @cached_property
    def nas1Configuration(self):  # pragma: no cover
        return KxNAS1Configuration.make_one(self.boto3_raw_data["nas1Configuration"])

    status = field("status")
    description = field("description")
    statusReason = field("statusReason")
    createdTimestamp = field("createdTimestamp")
    azMode = field("azMode")
    availabilityZoneIds = field("availabilityZoneIds")
    lastModifiedTimestamp = field("lastModifiedTimestamp")

    @cached_property
    def attachedClusters(self):  # pragma: no cover
        return KxAttachedCluster.make_many(self.boto3_raw_data["attachedClusters"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateKxVolumeResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateKxVolumeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListKxChangesetsResponse:
    boto3_raw_data: "type_defs.ListKxChangesetsResponseTypeDef" = dataclasses.field()

    @cached_property
    def kxChangesets(self):  # pragma: no cover
        return KxChangesetListEntry.make_many(self.boto3_raw_data["kxChangesets"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListKxChangesetsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListKxChangesetsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateKxClusterCodeConfigurationRequest:
    boto3_raw_data: "type_defs.UpdateKxClusterCodeConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    environmentId = field("environmentId")
    clusterName = field("clusterName")

    @cached_property
    def code(self):  # pragma: no cover
        return CodeConfiguration.make_one(self.boto3_raw_data["code"])

    clientToken = field("clientToken")
    initializationScript = field("initializationScript")

    @cached_property
    def commandLineArguments(self):  # pragma: no cover
        return KxCommandLineArgument.make_many(
            self.boto3_raw_data["commandLineArguments"]
        )

    @cached_property
    def deploymentConfiguration(self):  # pragma: no cover
        return KxClusterCodeDeploymentConfiguration.make_one(
            self.boto3_raw_data["deploymentConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateKxClusterCodeConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateKxClusterCodeConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListKxDatabasesResponse:
    boto3_raw_data: "type_defs.ListKxDatabasesResponseTypeDef" = dataclasses.field()

    @cached_property
    def kxDatabases(self):  # pragma: no cover
        return KxDatabaseListEntry.make_many(self.boto3_raw_data["kxDatabases"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListKxDatabasesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListKxDatabasesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListKxClusterNodesResponse:
    boto3_raw_data: "type_defs.ListKxClusterNodesResponseTypeDef" = dataclasses.field()

    @cached_property
    def nodes(self):  # pragma: no cover
        return KxNode.make_many(self.boto3_raw_data["nodes"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListKxClusterNodesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListKxClusterNodesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListKxScalingGroupsResponse:
    boto3_raw_data: "type_defs.ListKxScalingGroupsResponseTypeDef" = dataclasses.field()

    @cached_property
    def scalingGroups(self):  # pragma: no cover
        return KxScalingGroup.make_many(self.boto3_raw_data["scalingGroups"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListKxScalingGroupsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListKxScalingGroupsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListKxUsersResponse:
    boto3_raw_data: "type_defs.ListKxUsersResponseTypeDef" = dataclasses.field()

    @cached_property
    def users(self):  # pragma: no cover
        return KxUser.make_many(self.boto3_raw_data["users"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListKxUsersResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListKxUsersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListKxVolumesResponse:
    boto3_raw_data: "type_defs.ListKxVolumesResponseTypeDef" = dataclasses.field()

    @cached_property
    def kxVolumeSummaries(self):  # pragma: no cover
        return KxVolume.make_many(self.boto3_raw_data["kxVolumeSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListKxVolumesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListKxVolumesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListKxEnvironmentsRequestPaginate:
    boto3_raw_data: "type_defs.ListKxEnvironmentsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListKxEnvironmentsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListKxEnvironmentsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NetworkACLEntry:
    boto3_raw_data: "type_defs.NetworkACLEntryTypeDef" = dataclasses.field()

    ruleNumber = field("ruleNumber")
    protocol = field("protocol")
    ruleAction = field("ruleAction")
    cidrBlock = field("cidrBlock")

    @cached_property
    def portRange(self):  # pragma: no cover
        return PortRange.make_one(self.boto3_raw_data["portRange"])

    @cached_property
    def icmpTypeCode(self):  # pragma: no cover
        return IcmpTypeCode.make_one(self.boto3_raw_data["icmpTypeCode"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NetworkACLEntryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.NetworkACLEntryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListKxClustersResponse:
    boto3_raw_data: "type_defs.ListKxClustersResponseTypeDef" = dataclasses.field()

    @cached_property
    def kxClusterSummaries(self):  # pragma: no cover
        return KxCluster.make_many(self.boto3_raw_data["kxClusterSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListKxClustersResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListKxClustersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetKxDataviewResponse:
    boto3_raw_data: "type_defs.GetKxDataviewResponseTypeDef" = dataclasses.field()

    databaseName = field("databaseName")
    dataviewName = field("dataviewName")
    azMode = field("azMode")
    availabilityZoneId = field("availabilityZoneId")
    changesetId = field("changesetId")

    @cached_property
    def segmentConfigurations(self):  # pragma: no cover
        return KxDataviewSegmentConfigurationOutput.make_many(
            self.boto3_raw_data["segmentConfigurations"]
        )

    @cached_property
    def activeVersions(self):  # pragma: no cover
        return KxDataviewActiveVersion.make_many(self.boto3_raw_data["activeVersions"])

    description = field("description")
    autoUpdate = field("autoUpdate")
    readWrite = field("readWrite")
    environmentId = field("environmentId")
    createdTimestamp = field("createdTimestamp")
    lastModifiedTimestamp = field("lastModifiedTimestamp")
    status = field("status")
    statusReason = field("statusReason")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetKxDataviewResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetKxDataviewResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KxDataviewListEntry:
    boto3_raw_data: "type_defs.KxDataviewListEntryTypeDef" = dataclasses.field()

    environmentId = field("environmentId")
    databaseName = field("databaseName")
    dataviewName = field("dataviewName")
    azMode = field("azMode")
    availabilityZoneId = field("availabilityZoneId")
    changesetId = field("changesetId")

    @cached_property
    def segmentConfigurations(self):  # pragma: no cover
        return KxDataviewSegmentConfigurationOutput.make_many(
            self.boto3_raw_data["segmentConfigurations"]
        )

    @cached_property
    def activeVersions(self):  # pragma: no cover
        return KxDataviewActiveVersion.make_many(self.boto3_raw_data["activeVersions"])

    status = field("status")
    description = field("description")
    autoUpdate = field("autoUpdate")
    readWrite = field("readWrite")
    createdTimestamp = field("createdTimestamp")
    lastModifiedTimestamp = field("lastModifiedTimestamp")
    statusReason = field("statusReason")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KxDataviewListEntryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KxDataviewListEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateKxDataviewResponse:
    boto3_raw_data: "type_defs.UpdateKxDataviewResponseTypeDef" = dataclasses.field()

    environmentId = field("environmentId")
    databaseName = field("databaseName")
    dataviewName = field("dataviewName")
    azMode = field("azMode")
    availabilityZoneId = field("availabilityZoneId")
    changesetId = field("changesetId")

    @cached_property
    def segmentConfigurations(self):  # pragma: no cover
        return KxDataviewSegmentConfigurationOutput.make_many(
            self.boto3_raw_data["segmentConfigurations"]
        )

    @cached_property
    def activeVersions(self):  # pragma: no cover
        return KxDataviewActiveVersion.make_many(self.boto3_raw_data["activeVersions"])

    status = field("status")
    autoUpdate = field("autoUpdate")
    readWrite = field("readWrite")
    description = field("description")
    createdTimestamp = field("createdTimestamp")
    lastModifiedTimestamp = field("lastModifiedTimestamp")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateKxDataviewResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateKxDataviewResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KxDatabaseConfigurationOutput:
    boto3_raw_data: "type_defs.KxDatabaseConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    databaseName = field("databaseName")

    @cached_property
    def cacheConfigurations(self):  # pragma: no cover
        return KxDatabaseCacheConfigurationOutput.make_many(
            self.boto3_raw_data["cacheConfigurations"]
        )

    changesetId = field("changesetId")
    dataviewName = field("dataviewName")

    @cached_property
    def dataviewConfiguration(self):  # pragma: no cover
        return KxDataviewConfigurationOutput.make_one(
            self.boto3_raw_data["dataviewConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.KxDatabaseConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KxDatabaseConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEnvironmentResponse:
    boto3_raw_data: "type_defs.GetEnvironmentResponseTypeDef" = dataclasses.field()

    @cached_property
    def environment(self):  # pragma: no cover
        return Environment.make_one(self.boto3_raw_data["environment"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetEnvironmentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEnvironmentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEnvironmentsResponse:
    boto3_raw_data: "type_defs.ListEnvironmentsResponseTypeDef" = dataclasses.field()

    @cached_property
    def environments(self):  # pragma: no cover
        return Environment.make_many(self.boto3_raw_data["environments"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEnvironmentsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEnvironmentsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateEnvironmentResponse:
    boto3_raw_data: "type_defs.UpdateEnvironmentResponseTypeDef" = dataclasses.field()

    @cached_property
    def environment(self):  # pragma: no cover
        return Environment.make_one(self.boto3_raw_data["environment"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateEnvironmentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateEnvironmentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEnvironmentRequest:
    boto3_raw_data: "type_defs.CreateEnvironmentRequestTypeDef" = dataclasses.field()

    name = field("name")
    description = field("description")
    kmsKeyId = field("kmsKeyId")
    tags = field("tags")
    federationMode = field("federationMode")
    federationParameters = field("federationParameters")

    @cached_property
    def superuserParameters(self):  # pragma: no cover
        return SuperuserParameters.make_one(self.boto3_raw_data["superuserParameters"])

    dataBundles = field("dataBundles")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateEnvironmentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEnvironmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateEnvironmentRequest:
    boto3_raw_data: "type_defs.UpdateEnvironmentRequestTypeDef" = dataclasses.field()

    environmentId = field("environmentId")
    name = field("name")
    description = field("description")
    federationMode = field("federationMode")
    federationParameters = field("federationParameters")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateEnvironmentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateEnvironmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateKxDataviewRequest:
    boto3_raw_data: "type_defs.CreateKxDataviewRequestTypeDef" = dataclasses.field()

    environmentId = field("environmentId")
    databaseName = field("databaseName")
    dataviewName = field("dataviewName")
    azMode = field("azMode")
    clientToken = field("clientToken")
    availabilityZoneId = field("availabilityZoneId")
    changesetId = field("changesetId")
    segmentConfigurations = field("segmentConfigurations")
    autoUpdate = field("autoUpdate")
    readWrite = field("readWrite")
    description = field("description")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateKxDataviewRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateKxDataviewRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KxDataviewConfiguration:
    boto3_raw_data: "type_defs.KxDataviewConfigurationTypeDef" = dataclasses.field()

    dataviewName = field("dataviewName")
    dataviewVersionId = field("dataviewVersionId")
    changesetId = field("changesetId")
    segmentConfigurations = field("segmentConfigurations")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KxDataviewConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KxDataviewConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateKxDataviewRequest:
    boto3_raw_data: "type_defs.UpdateKxDataviewRequestTypeDef" = dataclasses.field()

    environmentId = field("environmentId")
    databaseName = field("databaseName")
    dataviewName = field("dataviewName")
    clientToken = field("clientToken")
    description = field("description")
    changesetId = field("changesetId")
    segmentConfigurations = field("segmentConfigurations")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateKxDataviewRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateKxDataviewRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TransitGatewayConfigurationOutput:
    boto3_raw_data: "type_defs.TransitGatewayConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    transitGatewayID = field("transitGatewayID")
    routableCIDRSpace = field("routableCIDRSpace")

    @cached_property
    def attachmentNetworkAclConfiguration(self):  # pragma: no cover
        return NetworkACLEntry.make_many(
            self.boto3_raw_data["attachmentNetworkAclConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.TransitGatewayConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TransitGatewayConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TransitGatewayConfiguration:
    boto3_raw_data: "type_defs.TransitGatewayConfigurationTypeDef" = dataclasses.field()

    transitGatewayID = field("transitGatewayID")
    routableCIDRSpace = field("routableCIDRSpace")

    @cached_property
    def attachmentNetworkAclConfiguration(self):  # pragma: no cover
        return NetworkACLEntry.make_many(
            self.boto3_raw_data["attachmentNetworkAclConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TransitGatewayConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TransitGatewayConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListKxDataviewsResponse:
    boto3_raw_data: "type_defs.ListKxDataviewsResponseTypeDef" = dataclasses.field()

    @cached_property
    def kxDataviews(self):  # pragma: no cover
        return KxDataviewListEntry.make_many(self.boto3_raw_data["kxDataviews"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListKxDataviewsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListKxDataviewsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateKxClusterResponse:
    boto3_raw_data: "type_defs.CreateKxClusterResponseTypeDef" = dataclasses.field()

    environmentId = field("environmentId")
    status = field("status")
    statusReason = field("statusReason")
    clusterName = field("clusterName")
    clusterType = field("clusterType")

    @cached_property
    def tickerplantLogConfiguration(self):  # pragma: no cover
        return TickerplantLogConfigurationOutput.make_one(
            self.boto3_raw_data["tickerplantLogConfiguration"]
        )

    @cached_property
    def volumes(self):  # pragma: no cover
        return Volume.make_many(self.boto3_raw_data["volumes"])

    @cached_property
    def databases(self):  # pragma: no cover
        return KxDatabaseConfigurationOutput.make_many(self.boto3_raw_data["databases"])

    @cached_property
    def cacheStorageConfigurations(self):  # pragma: no cover
        return KxCacheStorageConfiguration.make_many(
            self.boto3_raw_data["cacheStorageConfigurations"]
        )

    @cached_property
    def autoScalingConfiguration(self):  # pragma: no cover
        return AutoScalingConfiguration.make_one(
            self.boto3_raw_data["autoScalingConfiguration"]
        )

    clusterDescription = field("clusterDescription")

    @cached_property
    def capacityConfiguration(self):  # pragma: no cover
        return CapacityConfiguration.make_one(
            self.boto3_raw_data["capacityConfiguration"]
        )

    releaseLabel = field("releaseLabel")

    @cached_property
    def vpcConfiguration(self):  # pragma: no cover
        return VpcConfigurationOutput.make_one(self.boto3_raw_data["vpcConfiguration"])

    initializationScript = field("initializationScript")

    @cached_property
    def commandLineArguments(self):  # pragma: no cover
        return KxCommandLineArgument.make_many(
            self.boto3_raw_data["commandLineArguments"]
        )

    @cached_property
    def code(self):  # pragma: no cover
        return CodeConfiguration.make_one(self.boto3_raw_data["code"])

    executionRole = field("executionRole")
    lastModifiedTimestamp = field("lastModifiedTimestamp")

    @cached_property
    def savedownStorageConfiguration(self):  # pragma: no cover
        return KxSavedownStorageConfiguration.make_one(
            self.boto3_raw_data["savedownStorageConfiguration"]
        )

    azMode = field("azMode")
    availabilityZoneId = field("availabilityZoneId")
    createdTimestamp = field("createdTimestamp")

    @cached_property
    def scalingGroupConfiguration(self):  # pragma: no cover
        return KxScalingGroupConfiguration.make_one(
            self.boto3_raw_data["scalingGroupConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateKxClusterResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateKxClusterResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetKxClusterResponse:
    boto3_raw_data: "type_defs.GetKxClusterResponseTypeDef" = dataclasses.field()

    status = field("status")
    statusReason = field("statusReason")
    clusterName = field("clusterName")
    clusterType = field("clusterType")

    @cached_property
    def tickerplantLogConfiguration(self):  # pragma: no cover
        return TickerplantLogConfigurationOutput.make_one(
            self.boto3_raw_data["tickerplantLogConfiguration"]
        )

    @cached_property
    def volumes(self):  # pragma: no cover
        return Volume.make_many(self.boto3_raw_data["volumes"])

    @cached_property
    def databases(self):  # pragma: no cover
        return KxDatabaseConfigurationOutput.make_many(self.boto3_raw_data["databases"])

    @cached_property
    def cacheStorageConfigurations(self):  # pragma: no cover
        return KxCacheStorageConfiguration.make_many(
            self.boto3_raw_data["cacheStorageConfigurations"]
        )

    @cached_property
    def autoScalingConfiguration(self):  # pragma: no cover
        return AutoScalingConfiguration.make_one(
            self.boto3_raw_data["autoScalingConfiguration"]
        )

    clusterDescription = field("clusterDescription")

    @cached_property
    def capacityConfiguration(self):  # pragma: no cover
        return CapacityConfiguration.make_one(
            self.boto3_raw_data["capacityConfiguration"]
        )

    releaseLabel = field("releaseLabel")

    @cached_property
    def vpcConfiguration(self):  # pragma: no cover
        return VpcConfigurationOutput.make_one(self.boto3_raw_data["vpcConfiguration"])

    initializationScript = field("initializationScript")

    @cached_property
    def commandLineArguments(self):  # pragma: no cover
        return KxCommandLineArgument.make_many(
            self.boto3_raw_data["commandLineArguments"]
        )

    @cached_property
    def code(self):  # pragma: no cover
        return CodeConfiguration.make_one(self.boto3_raw_data["code"])

    executionRole = field("executionRole")
    lastModifiedTimestamp = field("lastModifiedTimestamp")

    @cached_property
    def savedownStorageConfiguration(self):  # pragma: no cover
        return KxSavedownStorageConfiguration.make_one(
            self.boto3_raw_data["savedownStorageConfiguration"]
        )

    azMode = field("azMode")
    availabilityZoneId = field("availabilityZoneId")
    createdTimestamp = field("createdTimestamp")

    @cached_property
    def scalingGroupConfiguration(self):  # pragma: no cover
        return KxScalingGroupConfiguration.make_one(
            self.boto3_raw_data["scalingGroupConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetKxClusterResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetKxClusterResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetKxEnvironmentResponse:
    boto3_raw_data: "type_defs.GetKxEnvironmentResponseTypeDef" = dataclasses.field()

    name = field("name")
    environmentId = field("environmentId")
    awsAccountId = field("awsAccountId")
    status = field("status")
    tgwStatus = field("tgwStatus")
    dnsStatus = field("dnsStatus")
    errorMessage = field("errorMessage")
    description = field("description")
    environmentArn = field("environmentArn")
    kmsKeyId = field("kmsKeyId")
    dedicatedServiceAccountId = field("dedicatedServiceAccountId")

    @cached_property
    def transitGatewayConfiguration(self):  # pragma: no cover
        return TransitGatewayConfigurationOutput.make_one(
            self.boto3_raw_data["transitGatewayConfiguration"]
        )

    @cached_property
    def customDNSConfiguration(self):  # pragma: no cover
        return CustomDNSServer.make_many(self.boto3_raw_data["customDNSConfiguration"])

    creationTimestamp = field("creationTimestamp")
    updateTimestamp = field("updateTimestamp")
    availabilityZoneIds = field("availabilityZoneIds")
    certificateAuthorityArn = field("certificateAuthorityArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetKxEnvironmentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetKxEnvironmentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KxEnvironment:
    boto3_raw_data: "type_defs.KxEnvironmentTypeDef" = dataclasses.field()

    name = field("name")
    environmentId = field("environmentId")
    awsAccountId = field("awsAccountId")
    status = field("status")
    tgwStatus = field("tgwStatus")
    dnsStatus = field("dnsStatus")
    errorMessage = field("errorMessage")
    description = field("description")
    environmentArn = field("environmentArn")
    kmsKeyId = field("kmsKeyId")
    dedicatedServiceAccountId = field("dedicatedServiceAccountId")

    @cached_property
    def transitGatewayConfiguration(self):  # pragma: no cover
        return TransitGatewayConfigurationOutput.make_one(
            self.boto3_raw_data["transitGatewayConfiguration"]
        )

    @cached_property
    def customDNSConfiguration(self):  # pragma: no cover
        return CustomDNSServer.make_many(self.boto3_raw_data["customDNSConfiguration"])

    creationTimestamp = field("creationTimestamp")
    updateTimestamp = field("updateTimestamp")
    availabilityZoneIds = field("availabilityZoneIds")
    certificateAuthorityArn = field("certificateAuthorityArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.KxEnvironmentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.KxEnvironmentTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateKxEnvironmentNetworkResponse:
    boto3_raw_data: "type_defs.UpdateKxEnvironmentNetworkResponseTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    environmentId = field("environmentId")
    awsAccountId = field("awsAccountId")
    status = field("status")
    tgwStatus = field("tgwStatus")
    dnsStatus = field("dnsStatus")
    errorMessage = field("errorMessage")
    description = field("description")
    environmentArn = field("environmentArn")
    kmsKeyId = field("kmsKeyId")
    dedicatedServiceAccountId = field("dedicatedServiceAccountId")

    @cached_property
    def transitGatewayConfiguration(self):  # pragma: no cover
        return TransitGatewayConfigurationOutput.make_one(
            self.boto3_raw_data["transitGatewayConfiguration"]
        )

    @cached_property
    def customDNSConfiguration(self):  # pragma: no cover
        return CustomDNSServer.make_many(self.boto3_raw_data["customDNSConfiguration"])

    creationTimestamp = field("creationTimestamp")
    updateTimestamp = field("updateTimestamp")
    availabilityZoneIds = field("availabilityZoneIds")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateKxEnvironmentNetworkResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateKxEnvironmentNetworkResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateKxEnvironmentResponse:
    boto3_raw_data: "type_defs.UpdateKxEnvironmentResponseTypeDef" = dataclasses.field()

    name = field("name")
    environmentId = field("environmentId")
    awsAccountId = field("awsAccountId")
    status = field("status")
    tgwStatus = field("tgwStatus")
    dnsStatus = field("dnsStatus")
    errorMessage = field("errorMessage")
    description = field("description")
    environmentArn = field("environmentArn")
    kmsKeyId = field("kmsKeyId")
    dedicatedServiceAccountId = field("dedicatedServiceAccountId")

    @cached_property
    def transitGatewayConfiguration(self):  # pragma: no cover
        return TransitGatewayConfigurationOutput.make_one(
            self.boto3_raw_data["transitGatewayConfiguration"]
        )

    @cached_property
    def customDNSConfiguration(self):  # pragma: no cover
        return CustomDNSServer.make_many(self.boto3_raw_data["customDNSConfiguration"])

    creationTimestamp = field("creationTimestamp")
    updateTimestamp = field("updateTimestamp")
    availabilityZoneIds = field("availabilityZoneIds")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateKxEnvironmentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateKxEnvironmentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KxDatabaseConfiguration:
    boto3_raw_data: "type_defs.KxDatabaseConfigurationTypeDef" = dataclasses.field()

    databaseName = field("databaseName")
    cacheConfigurations = field("cacheConfigurations")
    changesetId = field("changesetId")
    dataviewName = field("dataviewName")
    dataviewConfiguration = field("dataviewConfiguration")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KxDatabaseConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KxDatabaseConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListKxEnvironmentsResponse:
    boto3_raw_data: "type_defs.ListKxEnvironmentsResponseTypeDef" = dataclasses.field()

    @cached_property
    def environments(self):  # pragma: no cover
        return KxEnvironment.make_many(self.boto3_raw_data["environments"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListKxEnvironmentsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListKxEnvironmentsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateKxEnvironmentNetworkRequest:
    boto3_raw_data: "type_defs.UpdateKxEnvironmentNetworkRequestTypeDef" = (
        dataclasses.field()
    )

    environmentId = field("environmentId")
    transitGatewayConfiguration = field("transitGatewayConfiguration")

    @cached_property
    def customDNSConfiguration(self):  # pragma: no cover
        return CustomDNSServer.make_many(self.boto3_raw_data["customDNSConfiguration"])

    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateKxEnvironmentNetworkRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateKxEnvironmentNetworkRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateKxClusterRequest:
    boto3_raw_data: "type_defs.CreateKxClusterRequestTypeDef" = dataclasses.field()

    environmentId = field("environmentId")
    clusterName = field("clusterName")
    clusterType = field("clusterType")
    releaseLabel = field("releaseLabel")
    vpcConfiguration = field("vpcConfiguration")
    azMode = field("azMode")
    clientToken = field("clientToken")
    tickerplantLogConfiguration = field("tickerplantLogConfiguration")
    databases = field("databases")

    @cached_property
    def cacheStorageConfigurations(self):  # pragma: no cover
        return KxCacheStorageConfiguration.make_many(
            self.boto3_raw_data["cacheStorageConfigurations"]
        )

    @cached_property
    def autoScalingConfiguration(self):  # pragma: no cover
        return AutoScalingConfiguration.make_one(
            self.boto3_raw_data["autoScalingConfiguration"]
        )

    clusterDescription = field("clusterDescription")

    @cached_property
    def capacityConfiguration(self):  # pragma: no cover
        return CapacityConfiguration.make_one(
            self.boto3_raw_data["capacityConfiguration"]
        )

    initializationScript = field("initializationScript")

    @cached_property
    def commandLineArguments(self):  # pragma: no cover
        return KxCommandLineArgument.make_many(
            self.boto3_raw_data["commandLineArguments"]
        )

    @cached_property
    def code(self):  # pragma: no cover
        return CodeConfiguration.make_one(self.boto3_raw_data["code"])

    executionRole = field("executionRole")

    @cached_property
    def savedownStorageConfiguration(self):  # pragma: no cover
        return KxSavedownStorageConfiguration.make_one(
            self.boto3_raw_data["savedownStorageConfiguration"]
        )

    availabilityZoneId = field("availabilityZoneId")
    tags = field("tags")

    @cached_property
    def scalingGroupConfiguration(self):  # pragma: no cover
        return KxScalingGroupConfiguration.make_one(
            self.boto3_raw_data["scalingGroupConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateKxClusterRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateKxClusterRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateKxClusterDatabasesRequest:
    boto3_raw_data: "type_defs.UpdateKxClusterDatabasesRequestTypeDef" = (
        dataclasses.field()
    )

    environmentId = field("environmentId")
    clusterName = field("clusterName")
    databases = field("databases")
    clientToken = field("clientToken")

    @cached_property
    def deploymentConfiguration(self):  # pragma: no cover
        return KxDeploymentConfiguration.make_one(
            self.boto3_raw_data["deploymentConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateKxClusterDatabasesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateKxClusterDatabasesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
