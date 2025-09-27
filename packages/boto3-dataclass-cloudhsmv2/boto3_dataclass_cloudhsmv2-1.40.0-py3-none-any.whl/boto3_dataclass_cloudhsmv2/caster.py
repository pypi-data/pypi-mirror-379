# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_cloudhsmv2 import type_defs as bs_td


class CLOUDHSMV2Caster:

    def copy_backup_to_region(
        self,
        res: "bs_td.CopyBackupToRegionResponseTypeDef",
    ) -> "dc_td.CopyBackupToRegionResponse":
        return dc_td.CopyBackupToRegionResponse.make_one(res)

    def create_cluster(
        self,
        res: "bs_td.CreateClusterResponseTypeDef",
    ) -> "dc_td.CreateClusterResponse":
        return dc_td.CreateClusterResponse.make_one(res)

    def create_hsm(
        self,
        res: "bs_td.CreateHsmResponseTypeDef",
    ) -> "dc_td.CreateHsmResponse":
        return dc_td.CreateHsmResponse.make_one(res)

    def delete_backup(
        self,
        res: "bs_td.DeleteBackupResponseTypeDef",
    ) -> "dc_td.DeleteBackupResponse":
        return dc_td.DeleteBackupResponse.make_one(res)

    def delete_cluster(
        self,
        res: "bs_td.DeleteClusterResponseTypeDef",
    ) -> "dc_td.DeleteClusterResponse":
        return dc_td.DeleteClusterResponse.make_one(res)

    def delete_hsm(
        self,
        res: "bs_td.DeleteHsmResponseTypeDef",
    ) -> "dc_td.DeleteHsmResponse":
        return dc_td.DeleteHsmResponse.make_one(res)

    def delete_resource_policy(
        self,
        res: "bs_td.DeleteResourcePolicyResponseTypeDef",
    ) -> "dc_td.DeleteResourcePolicyResponse":
        return dc_td.DeleteResourcePolicyResponse.make_one(res)

    def describe_backups(
        self,
        res: "bs_td.DescribeBackupsResponseTypeDef",
    ) -> "dc_td.DescribeBackupsResponse":
        return dc_td.DescribeBackupsResponse.make_one(res)

    def describe_clusters(
        self,
        res: "bs_td.DescribeClustersResponseTypeDef",
    ) -> "dc_td.DescribeClustersResponse":
        return dc_td.DescribeClustersResponse.make_one(res)

    def get_resource_policy(
        self,
        res: "bs_td.GetResourcePolicyResponseTypeDef",
    ) -> "dc_td.GetResourcePolicyResponse":
        return dc_td.GetResourcePolicyResponse.make_one(res)

    def initialize_cluster(
        self,
        res: "bs_td.InitializeClusterResponseTypeDef",
    ) -> "dc_td.InitializeClusterResponse":
        return dc_td.InitializeClusterResponse.make_one(res)

    def list_tags(
        self,
        res: "bs_td.ListTagsResponseTypeDef",
    ) -> "dc_td.ListTagsResponse":
        return dc_td.ListTagsResponse.make_one(res)

    def modify_backup_attributes(
        self,
        res: "bs_td.ModifyBackupAttributesResponseTypeDef",
    ) -> "dc_td.ModifyBackupAttributesResponse":
        return dc_td.ModifyBackupAttributesResponse.make_one(res)

    def modify_cluster(
        self,
        res: "bs_td.ModifyClusterResponseTypeDef",
    ) -> "dc_td.ModifyClusterResponse":
        return dc_td.ModifyClusterResponse.make_one(res)

    def put_resource_policy(
        self,
        res: "bs_td.PutResourcePolicyResponseTypeDef",
    ) -> "dc_td.PutResourcePolicyResponse":
        return dc_td.PutResourcePolicyResponse.make_one(res)

    def restore_backup(
        self,
        res: "bs_td.RestoreBackupResponseTypeDef",
    ) -> "dc_td.RestoreBackupResponse":
        return dc_td.RestoreBackupResponse.make_one(res)


cloudhsmv2_caster = CLOUDHSMV2Caster()
