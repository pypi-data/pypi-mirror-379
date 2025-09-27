# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_efs import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class PosixUserOutput:
    boto3_raw_data: "type_defs.PosixUserOutputTypeDef" = dataclasses.field()

    Uid = field("Uid")
    Gid = field("Gid")
    SecondaryGids = field("SecondaryGids")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PosixUserOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PosixUserOutputTypeDef"]],
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
class BackupPolicy:
    boto3_raw_data: "type_defs.BackupPolicyTypeDef" = dataclasses.field()

    Status = field("Status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BackupPolicyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BackupPolicyTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMountTargetRequest:
    boto3_raw_data: "type_defs.CreateMountTargetRequestTypeDef" = dataclasses.field()

    FileSystemId = field("FileSystemId")
    SubnetId = field("SubnetId")
    IpAddress = field("IpAddress")
    Ipv6Address = field("Ipv6Address")
    IpAddressType = field("IpAddressType")
    SecurityGroups = field("SecurityGroups")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateMountTargetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMountTargetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DestinationToCreate:
    boto3_raw_data: "type_defs.DestinationToCreateTypeDef" = dataclasses.field()

    Region = field("Region")
    AvailabilityZoneName = field("AvailabilityZoneName")
    KmsKeyId = field("KmsKeyId")
    FileSystemId = field("FileSystemId")
    RoleArn = field("RoleArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DestinationToCreateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DestinationToCreateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreationInfo:
    boto3_raw_data: "type_defs.CreationInfoTypeDef" = dataclasses.field()

    OwnerUid = field("OwnerUid")
    OwnerGid = field("OwnerGid")
    Permissions = field("Permissions")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreationInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CreationInfoTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAccessPointRequest:
    boto3_raw_data: "type_defs.DeleteAccessPointRequestTypeDef" = dataclasses.field()

    AccessPointId = field("AccessPointId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAccessPointRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAccessPointRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteFileSystemPolicyRequest:
    boto3_raw_data: "type_defs.DeleteFileSystemPolicyRequestTypeDef" = (
        dataclasses.field()
    )

    FileSystemId = field("FileSystemId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteFileSystemPolicyRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteFileSystemPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteFileSystemRequest:
    boto3_raw_data: "type_defs.DeleteFileSystemRequestTypeDef" = dataclasses.field()

    FileSystemId = field("FileSystemId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteFileSystemRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteFileSystemRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteMountTargetRequest:
    boto3_raw_data: "type_defs.DeleteMountTargetRequestTypeDef" = dataclasses.field()

    MountTargetId = field("MountTargetId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteMountTargetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteMountTargetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteReplicationConfigurationRequest:
    boto3_raw_data: "type_defs.DeleteReplicationConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    SourceFileSystemId = field("SourceFileSystemId")
    DeletionMode = field("DeletionMode")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteReplicationConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteReplicationConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteTagsRequest:
    boto3_raw_data: "type_defs.DeleteTagsRequestTypeDef" = dataclasses.field()

    FileSystemId = field("FileSystemId")
    TagKeys = field("TagKeys")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteTagsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteTagsRequestTypeDef"]
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
class DescribeAccessPointsRequest:
    boto3_raw_data: "type_defs.DescribeAccessPointsRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    AccessPointId = field("AccessPointId")
    FileSystemId = field("FileSystemId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeAccessPointsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAccessPointsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAccountPreferencesRequest:
    boto3_raw_data: "type_defs.DescribeAccountPreferencesRequestTypeDef" = (
        dataclasses.field()
    )

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAccountPreferencesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAccountPreferencesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceIdPreference:
    boto3_raw_data: "type_defs.ResourceIdPreferenceTypeDef" = dataclasses.field()

    ResourceIdType = field("ResourceIdType")
    Resources = field("Resources")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResourceIdPreferenceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceIdPreferenceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeBackupPolicyRequest:
    boto3_raw_data: "type_defs.DescribeBackupPolicyRequestTypeDef" = dataclasses.field()

    FileSystemId = field("FileSystemId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeBackupPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBackupPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFileSystemPolicyRequest:
    boto3_raw_data: "type_defs.DescribeFileSystemPolicyRequestTypeDef" = (
        dataclasses.field()
    )

    FileSystemId = field("FileSystemId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeFileSystemPolicyRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFileSystemPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFileSystemsRequest:
    boto3_raw_data: "type_defs.DescribeFileSystemsRequestTypeDef" = dataclasses.field()

    MaxItems = field("MaxItems")
    Marker = field("Marker")
    CreationToken = field("CreationToken")
    FileSystemId = field("FileSystemId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeFileSystemsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFileSystemsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeLifecycleConfigurationRequest:
    boto3_raw_data: "type_defs.DescribeLifecycleConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    FileSystemId = field("FileSystemId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeLifecycleConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeLifecycleConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMountTargetSecurityGroupsRequest:
    boto3_raw_data: "type_defs.DescribeMountTargetSecurityGroupsRequestTypeDef" = (
        dataclasses.field()
    )

    MountTargetId = field("MountTargetId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeMountTargetSecurityGroupsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMountTargetSecurityGroupsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMountTargetsRequest:
    boto3_raw_data: "type_defs.DescribeMountTargetsRequestTypeDef" = dataclasses.field()

    MaxItems = field("MaxItems")
    Marker = field("Marker")
    FileSystemId = field("FileSystemId")
    MountTargetId = field("MountTargetId")
    AccessPointId = field("AccessPointId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeMountTargetsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMountTargetsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MountTargetDescription:
    boto3_raw_data: "type_defs.MountTargetDescriptionTypeDef" = dataclasses.field()

    MountTargetId = field("MountTargetId")
    FileSystemId = field("FileSystemId")
    SubnetId = field("SubnetId")
    LifeCycleState = field("LifeCycleState")
    OwnerId = field("OwnerId")
    IpAddress = field("IpAddress")
    Ipv6Address = field("Ipv6Address")
    NetworkInterfaceId = field("NetworkInterfaceId")
    AvailabilityZoneId = field("AvailabilityZoneId")
    AvailabilityZoneName = field("AvailabilityZoneName")
    VpcId = field("VpcId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MountTargetDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MountTargetDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReplicationConfigurationsRequest:
    boto3_raw_data: "type_defs.DescribeReplicationConfigurationsRequestTypeDef" = (
        dataclasses.field()
    )

    FileSystemId = field("FileSystemId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeReplicationConfigurationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeReplicationConfigurationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTagsRequest:
    boto3_raw_data: "type_defs.DescribeTagsRequestTypeDef" = dataclasses.field()

    FileSystemId = field("FileSystemId")
    MaxItems = field("MaxItems")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeTagsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTagsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Destination:
    boto3_raw_data: "type_defs.DestinationTypeDef" = dataclasses.field()

    Status = field("Status")
    FileSystemId = field("FileSystemId")
    Region = field("Region")
    LastReplicatedTimestamp = field("LastReplicatedTimestamp")
    OwnerId = field("OwnerId")
    StatusMessage = field("StatusMessage")
    RoleArn = field("RoleArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DestinationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DestinationTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FileSystemProtectionDescription:
    boto3_raw_data: "type_defs.FileSystemProtectionDescriptionTypeDef" = (
        dataclasses.field()
    )

    ReplicationOverwriteProtection = field("ReplicationOverwriteProtection")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.FileSystemProtectionDescriptionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FileSystemProtectionDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FileSystemSize:
    boto3_raw_data: "type_defs.FileSystemSizeTypeDef" = dataclasses.field()

    Value = field("Value")
    Timestamp = field("Timestamp")
    ValueInIA = field("ValueInIA")
    ValueInStandard = field("ValueInStandard")
    ValueInArchive = field("ValueInArchive")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FileSystemSizeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FileSystemSizeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LifecyclePolicy:
    boto3_raw_data: "type_defs.LifecyclePolicyTypeDef" = dataclasses.field()

    TransitionToIA = field("TransitionToIA")
    TransitionToPrimaryStorageClass = field("TransitionToPrimaryStorageClass")
    TransitionToArchive = field("TransitionToArchive")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LifecyclePolicyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LifecyclePolicyTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceRequest:
    boto3_raw_data: "type_defs.ListTagsForResourceRequestTypeDef" = dataclasses.field()

    ResourceId = field("ResourceId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

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
class ModifyMountTargetSecurityGroupsRequest:
    boto3_raw_data: "type_defs.ModifyMountTargetSecurityGroupsRequestTypeDef" = (
        dataclasses.field()
    )

    MountTargetId = field("MountTargetId")
    SecurityGroups = field("SecurityGroups")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ModifyMountTargetSecurityGroupsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyMountTargetSecurityGroupsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PosixUser:
    boto3_raw_data: "type_defs.PosixUserTypeDef" = dataclasses.field()

    Uid = field("Uid")
    Gid = field("Gid")
    SecondaryGids = field("SecondaryGids")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PosixUserTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PosixUserTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutAccountPreferencesRequest:
    boto3_raw_data: "type_defs.PutAccountPreferencesRequestTypeDef" = (
        dataclasses.field()
    )

    ResourceIdType = field("ResourceIdType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutAccountPreferencesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutAccountPreferencesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutFileSystemPolicyRequest:
    boto3_raw_data: "type_defs.PutFileSystemPolicyRequestTypeDef" = dataclasses.field()

    FileSystemId = field("FileSystemId")
    Policy = field("Policy")
    BypassPolicyLockoutSafetyCheck = field("BypassPolicyLockoutSafetyCheck")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutFileSystemPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutFileSystemPolicyRequestTypeDef"]
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

    ResourceId = field("ResourceId")
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
class UpdateFileSystemProtectionRequest:
    boto3_raw_data: "type_defs.UpdateFileSystemProtectionRequestTypeDef" = (
        dataclasses.field()
    )

    FileSystemId = field("FileSystemId")
    ReplicationOverwriteProtection = field("ReplicationOverwriteProtection")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateFileSystemProtectionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFileSystemProtectionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFileSystemRequest:
    boto3_raw_data: "type_defs.UpdateFileSystemRequestTypeDef" = dataclasses.field()

    FileSystemId = field("FileSystemId")
    ThroughputMode = field("ThroughputMode")
    ProvisionedThroughputInMibps = field("ProvisionedThroughputInMibps")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateFileSystemRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFileSystemRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMountTargetSecurityGroupsResponse:
    boto3_raw_data: "type_defs.DescribeMountTargetSecurityGroupsResponseTypeDef" = (
        dataclasses.field()
    )

    SecurityGroups = field("SecurityGroups")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeMountTargetSecurityGroupsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMountTargetSecurityGroupsResponseTypeDef"]
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
class FileSystemPolicyDescription:
    boto3_raw_data: "type_defs.FileSystemPolicyDescriptionTypeDef" = dataclasses.field()

    FileSystemId = field("FileSystemId")
    Policy = field("Policy")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FileSystemPolicyDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FileSystemPolicyDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FileSystemProtectionDescriptionResponse:
    boto3_raw_data: "type_defs.FileSystemProtectionDescriptionResponseTypeDef" = (
        dataclasses.field()
    )

    ReplicationOverwriteProtection = field("ReplicationOverwriteProtection")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.FileSystemProtectionDescriptionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FileSystemProtectionDescriptionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MountTargetDescriptionResponse:
    boto3_raw_data: "type_defs.MountTargetDescriptionResponseTypeDef" = (
        dataclasses.field()
    )

    OwnerId = field("OwnerId")
    MountTargetId = field("MountTargetId")
    FileSystemId = field("FileSystemId")
    SubnetId = field("SubnetId")
    LifeCycleState = field("LifeCycleState")
    IpAddress = field("IpAddress")
    Ipv6Address = field("Ipv6Address")
    NetworkInterfaceId = field("NetworkInterfaceId")
    AvailabilityZoneId = field("AvailabilityZoneId")
    AvailabilityZoneName = field("AvailabilityZoneName")
    VpcId = field("VpcId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.MountTargetDescriptionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MountTargetDescriptionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFileSystemRequest:
    boto3_raw_data: "type_defs.CreateFileSystemRequestTypeDef" = dataclasses.field()

    CreationToken = field("CreationToken")
    PerformanceMode = field("PerformanceMode")
    Encrypted = field("Encrypted")
    KmsKeyId = field("KmsKeyId")
    ThroughputMode = field("ThroughputMode")
    ProvisionedThroughputInMibps = field("ProvisionedThroughputInMibps")
    AvailabilityZoneName = field("AvailabilityZoneName")
    Backup = field("Backup")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateFileSystemRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFileSystemRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTagsRequest:
    boto3_raw_data: "type_defs.CreateTagsRequestTypeDef" = dataclasses.field()

    FileSystemId = field("FileSystemId")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateTagsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTagsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTagsResponse:
    boto3_raw_data: "type_defs.DescribeTagsResponseTypeDef" = dataclasses.field()

    Marker = field("Marker")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    NextMarker = field("NextMarker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeTagsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTagsResponseTypeDef"]
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

    NextToken = field("NextToken")

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

    ResourceId = field("ResourceId")

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
class BackupPolicyDescription:
    boto3_raw_data: "type_defs.BackupPolicyDescriptionTypeDef" = dataclasses.field()

    @cached_property
    def BackupPolicy(self):  # pragma: no cover
        return BackupPolicy.make_one(self.boto3_raw_data["BackupPolicy"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BackupPolicyDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BackupPolicyDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutBackupPolicyRequest:
    boto3_raw_data: "type_defs.PutBackupPolicyRequestTypeDef" = dataclasses.field()

    FileSystemId = field("FileSystemId")

    @cached_property
    def BackupPolicy(self):  # pragma: no cover
        return BackupPolicy.make_one(self.boto3_raw_data["BackupPolicy"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutBackupPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutBackupPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateReplicationConfigurationRequest:
    boto3_raw_data: "type_defs.CreateReplicationConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    SourceFileSystemId = field("SourceFileSystemId")

    @cached_property
    def Destinations(self):  # pragma: no cover
        return DestinationToCreate.make_many(self.boto3_raw_data["Destinations"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateReplicationConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateReplicationConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RootDirectory:
    boto3_raw_data: "type_defs.RootDirectoryTypeDef" = dataclasses.field()

    Path = field("Path")

    @cached_property
    def CreationInfo(self):  # pragma: no cover
        return CreationInfo.make_one(self.boto3_raw_data["CreationInfo"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RootDirectoryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RootDirectoryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAccessPointsRequestPaginate:
    boto3_raw_data: "type_defs.DescribeAccessPointsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    AccessPointId = field("AccessPointId")
    FileSystemId = field("FileSystemId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAccessPointsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAccessPointsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFileSystemsRequestPaginate:
    boto3_raw_data: "type_defs.DescribeFileSystemsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    CreationToken = field("CreationToken")
    FileSystemId = field("FileSystemId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeFileSystemsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFileSystemsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMountTargetsRequestPaginate:
    boto3_raw_data: "type_defs.DescribeMountTargetsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    FileSystemId = field("FileSystemId")
    MountTargetId = field("MountTargetId")
    AccessPointId = field("AccessPointId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeMountTargetsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMountTargetsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReplicationConfigurationsRequestPaginate:
    boto3_raw_data: (
        "type_defs.DescribeReplicationConfigurationsRequestPaginateTypeDef"
    ) = dataclasses.field()

    FileSystemId = field("FileSystemId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeReplicationConfigurationsRequestPaginateTypeDef"
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
                "type_defs.DescribeReplicationConfigurationsRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTagsRequestPaginate:
    boto3_raw_data: "type_defs.DescribeTagsRequestPaginateTypeDef" = dataclasses.field()

    FileSystemId = field("FileSystemId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeTagsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTagsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAccountPreferencesResponse:
    boto3_raw_data: "type_defs.DescribeAccountPreferencesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ResourceIdPreference(self):  # pragma: no cover
        return ResourceIdPreference.make_one(
            self.boto3_raw_data["ResourceIdPreference"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAccountPreferencesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAccountPreferencesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutAccountPreferencesResponse:
    boto3_raw_data: "type_defs.PutAccountPreferencesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ResourceIdPreference(self):  # pragma: no cover
        return ResourceIdPreference.make_one(
            self.boto3_raw_data["ResourceIdPreference"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PutAccountPreferencesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutAccountPreferencesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMountTargetsResponse:
    boto3_raw_data: "type_defs.DescribeMountTargetsResponseTypeDef" = (
        dataclasses.field()
    )

    Marker = field("Marker")

    @cached_property
    def MountTargets(self):  # pragma: no cover
        return MountTargetDescription.make_many(self.boto3_raw_data["MountTargets"])

    NextMarker = field("NextMarker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeMountTargetsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMountTargetsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicationConfigurationDescriptionResponse:
    boto3_raw_data: "type_defs.ReplicationConfigurationDescriptionResponseTypeDef" = (
        dataclasses.field()
    )

    SourceFileSystemId = field("SourceFileSystemId")
    SourceFileSystemRegion = field("SourceFileSystemRegion")
    SourceFileSystemArn = field("SourceFileSystemArn")
    OriginalSourceFileSystemArn = field("OriginalSourceFileSystemArn")
    CreationTime = field("CreationTime")

    @cached_property
    def Destinations(self):  # pragma: no cover
        return Destination.make_many(self.boto3_raw_data["Destinations"])

    SourceFileSystemOwnerId = field("SourceFileSystemOwnerId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ReplicationConfigurationDescriptionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplicationConfigurationDescriptionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicationConfigurationDescription:
    boto3_raw_data: "type_defs.ReplicationConfigurationDescriptionTypeDef" = (
        dataclasses.field()
    )

    SourceFileSystemId = field("SourceFileSystemId")
    SourceFileSystemRegion = field("SourceFileSystemRegion")
    SourceFileSystemArn = field("SourceFileSystemArn")
    OriginalSourceFileSystemArn = field("OriginalSourceFileSystemArn")
    CreationTime = field("CreationTime")

    @cached_property
    def Destinations(self):  # pragma: no cover
        return Destination.make_many(self.boto3_raw_data["Destinations"])

    SourceFileSystemOwnerId = field("SourceFileSystemOwnerId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ReplicationConfigurationDescriptionTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplicationConfigurationDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FileSystemDescriptionResponse:
    boto3_raw_data: "type_defs.FileSystemDescriptionResponseTypeDef" = (
        dataclasses.field()
    )

    OwnerId = field("OwnerId")
    CreationToken = field("CreationToken")
    FileSystemId = field("FileSystemId")
    FileSystemArn = field("FileSystemArn")
    CreationTime = field("CreationTime")
    LifeCycleState = field("LifeCycleState")
    Name = field("Name")
    NumberOfMountTargets = field("NumberOfMountTargets")

    @cached_property
    def SizeInBytes(self):  # pragma: no cover
        return FileSystemSize.make_one(self.boto3_raw_data["SizeInBytes"])

    PerformanceMode = field("PerformanceMode")
    Encrypted = field("Encrypted")
    KmsKeyId = field("KmsKeyId")
    ThroughputMode = field("ThroughputMode")
    ProvisionedThroughputInMibps = field("ProvisionedThroughputInMibps")
    AvailabilityZoneName = field("AvailabilityZoneName")
    AvailabilityZoneId = field("AvailabilityZoneId")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def FileSystemProtection(self):  # pragma: no cover
        return FileSystemProtectionDescription.make_one(
            self.boto3_raw_data["FileSystemProtection"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.FileSystemDescriptionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FileSystemDescriptionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FileSystemDescription:
    boto3_raw_data: "type_defs.FileSystemDescriptionTypeDef" = dataclasses.field()

    OwnerId = field("OwnerId")
    CreationToken = field("CreationToken")
    FileSystemId = field("FileSystemId")
    CreationTime = field("CreationTime")
    LifeCycleState = field("LifeCycleState")
    NumberOfMountTargets = field("NumberOfMountTargets")

    @cached_property
    def SizeInBytes(self):  # pragma: no cover
        return FileSystemSize.make_one(self.boto3_raw_data["SizeInBytes"])

    PerformanceMode = field("PerformanceMode")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    FileSystemArn = field("FileSystemArn")
    Name = field("Name")
    Encrypted = field("Encrypted")
    KmsKeyId = field("KmsKeyId")
    ThroughputMode = field("ThroughputMode")
    ProvisionedThroughputInMibps = field("ProvisionedThroughputInMibps")
    AvailabilityZoneName = field("AvailabilityZoneName")
    AvailabilityZoneId = field("AvailabilityZoneId")

    @cached_property
    def FileSystemProtection(self):  # pragma: no cover
        return FileSystemProtectionDescription.make_one(
            self.boto3_raw_data["FileSystemProtection"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FileSystemDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FileSystemDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LifecycleConfigurationDescription:
    boto3_raw_data: "type_defs.LifecycleConfigurationDescriptionTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def LifecyclePolicies(self):  # pragma: no cover
        return LifecyclePolicy.make_many(self.boto3_raw_data["LifecyclePolicies"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.LifecycleConfigurationDescriptionTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LifecycleConfigurationDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutLifecycleConfigurationRequest:
    boto3_raw_data: "type_defs.PutLifecycleConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    FileSystemId = field("FileSystemId")

    @cached_property
    def LifecyclePolicies(self):  # pragma: no cover
        return LifecyclePolicy.make_many(self.boto3_raw_data["LifecyclePolicies"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PutLifecycleConfigurationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutLifecycleConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccessPointDescriptionResponse:
    boto3_raw_data: "type_defs.AccessPointDescriptionResponseTypeDef" = (
        dataclasses.field()
    )

    ClientToken = field("ClientToken")
    Name = field("Name")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    AccessPointId = field("AccessPointId")
    AccessPointArn = field("AccessPointArn")
    FileSystemId = field("FileSystemId")

    @cached_property
    def PosixUser(self):  # pragma: no cover
        return PosixUserOutput.make_one(self.boto3_raw_data["PosixUser"])

    @cached_property
    def RootDirectory(self):  # pragma: no cover
        return RootDirectory.make_one(self.boto3_raw_data["RootDirectory"])

    OwnerId = field("OwnerId")
    LifeCycleState = field("LifeCycleState")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AccessPointDescriptionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccessPointDescriptionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccessPointDescription:
    boto3_raw_data: "type_defs.AccessPointDescriptionTypeDef" = dataclasses.field()

    ClientToken = field("ClientToken")
    Name = field("Name")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    AccessPointId = field("AccessPointId")
    AccessPointArn = field("AccessPointArn")
    FileSystemId = field("FileSystemId")

    @cached_property
    def PosixUser(self):  # pragma: no cover
        return PosixUserOutput.make_one(self.boto3_raw_data["PosixUser"])

    @cached_property
    def RootDirectory(self):  # pragma: no cover
        return RootDirectory.make_one(self.boto3_raw_data["RootDirectory"])

    OwnerId = field("OwnerId")
    LifeCycleState = field("LifeCycleState")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AccessPointDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccessPointDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReplicationConfigurationsResponse:
    boto3_raw_data: "type_defs.DescribeReplicationConfigurationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Replications(self):  # pragma: no cover
        return ReplicationConfigurationDescription.make_many(
            self.boto3_raw_data["Replications"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeReplicationConfigurationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeReplicationConfigurationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFileSystemsResponse:
    boto3_raw_data: "type_defs.DescribeFileSystemsResponseTypeDef" = dataclasses.field()

    Marker = field("Marker")

    @cached_property
    def FileSystems(self):  # pragma: no cover
        return FileSystemDescription.make_many(self.boto3_raw_data["FileSystems"])

    NextMarker = field("NextMarker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeFileSystemsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFileSystemsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAccessPointRequest:
    boto3_raw_data: "type_defs.CreateAccessPointRequestTypeDef" = dataclasses.field()

    ClientToken = field("ClientToken")
    FileSystemId = field("FileSystemId")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    PosixUser = field("PosixUser")

    @cached_property
    def RootDirectory(self):  # pragma: no cover
        return RootDirectory.make_one(self.boto3_raw_data["RootDirectory"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAccessPointRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAccessPointRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAccessPointsResponse:
    boto3_raw_data: "type_defs.DescribeAccessPointsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AccessPoints(self):  # pragma: no cover
        return AccessPointDescription.make_many(self.boto3_raw_data["AccessPoints"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeAccessPointsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAccessPointsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
