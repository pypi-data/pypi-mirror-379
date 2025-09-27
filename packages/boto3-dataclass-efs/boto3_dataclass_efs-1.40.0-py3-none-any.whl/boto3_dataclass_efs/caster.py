# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_efs import type_defs as bs_td


class EFSCaster:

    def create_access_point(
        self,
        res: "bs_td.AccessPointDescriptionResponseTypeDef",
    ) -> "dc_td.AccessPointDescriptionResponse":
        return dc_td.AccessPointDescriptionResponse.make_one(res)

    def create_file_system(
        self,
        res: "bs_td.FileSystemDescriptionResponseTypeDef",
    ) -> "dc_td.FileSystemDescriptionResponse":
        return dc_td.FileSystemDescriptionResponse.make_one(res)

    def create_mount_target(
        self,
        res: "bs_td.MountTargetDescriptionResponseTypeDef",
    ) -> "dc_td.MountTargetDescriptionResponse":
        return dc_td.MountTargetDescriptionResponse.make_one(res)

    def create_replication_configuration(
        self,
        res: "bs_td.ReplicationConfigurationDescriptionResponseTypeDef",
    ) -> "dc_td.ReplicationConfigurationDescriptionResponse":
        return dc_td.ReplicationConfigurationDescriptionResponse.make_one(res)

    def create_tags(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_access_point(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_file_system(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_file_system_policy(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_mount_target(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_replication_configuration(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_tags(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def describe_access_points(
        self,
        res: "bs_td.DescribeAccessPointsResponseTypeDef",
    ) -> "dc_td.DescribeAccessPointsResponse":
        return dc_td.DescribeAccessPointsResponse.make_one(res)

    def describe_account_preferences(
        self,
        res: "bs_td.DescribeAccountPreferencesResponseTypeDef",
    ) -> "dc_td.DescribeAccountPreferencesResponse":
        return dc_td.DescribeAccountPreferencesResponse.make_one(res)

    def describe_backup_policy(
        self,
        res: "bs_td.BackupPolicyDescriptionTypeDef",
    ) -> "dc_td.BackupPolicyDescription":
        return dc_td.BackupPolicyDescription.make_one(res)

    def describe_file_system_policy(
        self,
        res: "bs_td.FileSystemPolicyDescriptionTypeDef",
    ) -> "dc_td.FileSystemPolicyDescription":
        return dc_td.FileSystemPolicyDescription.make_one(res)

    def describe_file_systems(
        self,
        res: "bs_td.DescribeFileSystemsResponseTypeDef",
    ) -> "dc_td.DescribeFileSystemsResponse":
        return dc_td.DescribeFileSystemsResponse.make_one(res)

    def describe_lifecycle_configuration(
        self,
        res: "bs_td.LifecycleConfigurationDescriptionTypeDef",
    ) -> "dc_td.LifecycleConfigurationDescription":
        return dc_td.LifecycleConfigurationDescription.make_one(res)

    def describe_mount_target_security_groups(
        self,
        res: "bs_td.DescribeMountTargetSecurityGroupsResponseTypeDef",
    ) -> "dc_td.DescribeMountTargetSecurityGroupsResponse":
        return dc_td.DescribeMountTargetSecurityGroupsResponse.make_one(res)

    def describe_mount_targets(
        self,
        res: "bs_td.DescribeMountTargetsResponseTypeDef",
    ) -> "dc_td.DescribeMountTargetsResponse":
        return dc_td.DescribeMountTargetsResponse.make_one(res)

    def describe_replication_configurations(
        self,
        res: "bs_td.DescribeReplicationConfigurationsResponseTypeDef",
    ) -> "dc_td.DescribeReplicationConfigurationsResponse":
        return dc_td.DescribeReplicationConfigurationsResponse.make_one(res)

    def describe_tags(
        self,
        res: "bs_td.DescribeTagsResponseTypeDef",
    ) -> "dc_td.DescribeTagsResponse":
        return dc_td.DescribeTagsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def modify_mount_target_security_groups(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def put_account_preferences(
        self,
        res: "bs_td.PutAccountPreferencesResponseTypeDef",
    ) -> "dc_td.PutAccountPreferencesResponse":
        return dc_td.PutAccountPreferencesResponse.make_one(res)

    def put_backup_policy(
        self,
        res: "bs_td.BackupPolicyDescriptionTypeDef",
    ) -> "dc_td.BackupPolicyDescription":
        return dc_td.BackupPolicyDescription.make_one(res)

    def put_file_system_policy(
        self,
        res: "bs_td.FileSystemPolicyDescriptionTypeDef",
    ) -> "dc_td.FileSystemPolicyDescription":
        return dc_td.FileSystemPolicyDescription.make_one(res)

    def put_lifecycle_configuration(
        self,
        res: "bs_td.LifecycleConfigurationDescriptionTypeDef",
    ) -> "dc_td.LifecycleConfigurationDescription":
        return dc_td.LifecycleConfigurationDescription.make_one(res)

    def tag_resource(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def untag_resource(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_file_system(
        self,
        res: "bs_td.FileSystemDescriptionResponseTypeDef",
    ) -> "dc_td.FileSystemDescriptionResponse":
        return dc_td.FileSystemDescriptionResponse.make_one(res)

    def update_file_system_protection(
        self,
        res: "bs_td.FileSystemProtectionDescriptionResponseTypeDef",
    ) -> "dc_td.FileSystemProtectionDescriptionResponse":
        return dc_td.FileSystemProtectionDescriptionResponse.make_one(res)


efs_caster = EFSCaster()
