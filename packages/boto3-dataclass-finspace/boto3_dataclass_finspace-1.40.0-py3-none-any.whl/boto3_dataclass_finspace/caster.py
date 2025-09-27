# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_finspace import type_defs as bs_td


class FINSPACECaster:

    def create_environment(
        self,
        res: "bs_td.CreateEnvironmentResponseTypeDef",
    ) -> "dc_td.CreateEnvironmentResponse":
        return dc_td.CreateEnvironmentResponse.make_one(res)

    def create_kx_changeset(
        self,
        res: "bs_td.CreateKxChangesetResponseTypeDef",
    ) -> "dc_td.CreateKxChangesetResponse":
        return dc_td.CreateKxChangesetResponse.make_one(res)

    def create_kx_cluster(
        self,
        res: "bs_td.CreateKxClusterResponseTypeDef",
    ) -> "dc_td.CreateKxClusterResponse":
        return dc_td.CreateKxClusterResponse.make_one(res)

    def create_kx_database(
        self,
        res: "bs_td.CreateKxDatabaseResponseTypeDef",
    ) -> "dc_td.CreateKxDatabaseResponse":
        return dc_td.CreateKxDatabaseResponse.make_one(res)

    def create_kx_dataview(
        self,
        res: "bs_td.CreateKxDataviewResponseTypeDef",
    ) -> "dc_td.CreateKxDataviewResponse":
        return dc_td.CreateKxDataviewResponse.make_one(res)

    def create_kx_environment(
        self,
        res: "bs_td.CreateKxEnvironmentResponseTypeDef",
    ) -> "dc_td.CreateKxEnvironmentResponse":
        return dc_td.CreateKxEnvironmentResponse.make_one(res)

    def create_kx_scaling_group(
        self,
        res: "bs_td.CreateKxScalingGroupResponseTypeDef",
    ) -> "dc_td.CreateKxScalingGroupResponse":
        return dc_td.CreateKxScalingGroupResponse.make_one(res)

    def create_kx_user(
        self,
        res: "bs_td.CreateKxUserResponseTypeDef",
    ) -> "dc_td.CreateKxUserResponse":
        return dc_td.CreateKxUserResponse.make_one(res)

    def create_kx_volume(
        self,
        res: "bs_td.CreateKxVolumeResponseTypeDef",
    ) -> "dc_td.CreateKxVolumeResponse":
        return dc_td.CreateKxVolumeResponse.make_one(res)

    def get_environment(
        self,
        res: "bs_td.GetEnvironmentResponseTypeDef",
    ) -> "dc_td.GetEnvironmentResponse":
        return dc_td.GetEnvironmentResponse.make_one(res)

    def get_kx_changeset(
        self,
        res: "bs_td.GetKxChangesetResponseTypeDef",
    ) -> "dc_td.GetKxChangesetResponse":
        return dc_td.GetKxChangesetResponse.make_one(res)

    def get_kx_cluster(
        self,
        res: "bs_td.GetKxClusterResponseTypeDef",
    ) -> "dc_td.GetKxClusterResponse":
        return dc_td.GetKxClusterResponse.make_one(res)

    def get_kx_connection_string(
        self,
        res: "bs_td.GetKxConnectionStringResponseTypeDef",
    ) -> "dc_td.GetKxConnectionStringResponse":
        return dc_td.GetKxConnectionStringResponse.make_one(res)

    def get_kx_database(
        self,
        res: "bs_td.GetKxDatabaseResponseTypeDef",
    ) -> "dc_td.GetKxDatabaseResponse":
        return dc_td.GetKxDatabaseResponse.make_one(res)

    def get_kx_dataview(
        self,
        res: "bs_td.GetKxDataviewResponseTypeDef",
    ) -> "dc_td.GetKxDataviewResponse":
        return dc_td.GetKxDataviewResponse.make_one(res)

    def get_kx_environment(
        self,
        res: "bs_td.GetKxEnvironmentResponseTypeDef",
    ) -> "dc_td.GetKxEnvironmentResponse":
        return dc_td.GetKxEnvironmentResponse.make_one(res)

    def get_kx_scaling_group(
        self,
        res: "bs_td.GetKxScalingGroupResponseTypeDef",
    ) -> "dc_td.GetKxScalingGroupResponse":
        return dc_td.GetKxScalingGroupResponse.make_one(res)

    def get_kx_user(
        self,
        res: "bs_td.GetKxUserResponseTypeDef",
    ) -> "dc_td.GetKxUserResponse":
        return dc_td.GetKxUserResponse.make_one(res)

    def get_kx_volume(
        self,
        res: "bs_td.GetKxVolumeResponseTypeDef",
    ) -> "dc_td.GetKxVolumeResponse":
        return dc_td.GetKxVolumeResponse.make_one(res)

    def list_environments(
        self,
        res: "bs_td.ListEnvironmentsResponseTypeDef",
    ) -> "dc_td.ListEnvironmentsResponse":
        return dc_td.ListEnvironmentsResponse.make_one(res)

    def list_kx_changesets(
        self,
        res: "bs_td.ListKxChangesetsResponseTypeDef",
    ) -> "dc_td.ListKxChangesetsResponse":
        return dc_td.ListKxChangesetsResponse.make_one(res)

    def list_kx_cluster_nodes(
        self,
        res: "bs_td.ListKxClusterNodesResponseTypeDef",
    ) -> "dc_td.ListKxClusterNodesResponse":
        return dc_td.ListKxClusterNodesResponse.make_one(res)

    def list_kx_clusters(
        self,
        res: "bs_td.ListKxClustersResponseTypeDef",
    ) -> "dc_td.ListKxClustersResponse":
        return dc_td.ListKxClustersResponse.make_one(res)

    def list_kx_databases(
        self,
        res: "bs_td.ListKxDatabasesResponseTypeDef",
    ) -> "dc_td.ListKxDatabasesResponse":
        return dc_td.ListKxDatabasesResponse.make_one(res)

    def list_kx_dataviews(
        self,
        res: "bs_td.ListKxDataviewsResponseTypeDef",
    ) -> "dc_td.ListKxDataviewsResponse":
        return dc_td.ListKxDataviewsResponse.make_one(res)

    def list_kx_environments(
        self,
        res: "bs_td.ListKxEnvironmentsResponseTypeDef",
    ) -> "dc_td.ListKxEnvironmentsResponse":
        return dc_td.ListKxEnvironmentsResponse.make_one(res)

    def list_kx_scaling_groups(
        self,
        res: "bs_td.ListKxScalingGroupsResponseTypeDef",
    ) -> "dc_td.ListKxScalingGroupsResponse":
        return dc_td.ListKxScalingGroupsResponse.make_one(res)

    def list_kx_users(
        self,
        res: "bs_td.ListKxUsersResponseTypeDef",
    ) -> "dc_td.ListKxUsersResponse":
        return dc_td.ListKxUsersResponse.make_one(res)

    def list_kx_volumes(
        self,
        res: "bs_td.ListKxVolumesResponseTypeDef",
    ) -> "dc_td.ListKxVolumesResponse":
        return dc_td.ListKxVolumesResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def update_environment(
        self,
        res: "bs_td.UpdateEnvironmentResponseTypeDef",
    ) -> "dc_td.UpdateEnvironmentResponse":
        return dc_td.UpdateEnvironmentResponse.make_one(res)

    def update_kx_database(
        self,
        res: "bs_td.UpdateKxDatabaseResponseTypeDef",
    ) -> "dc_td.UpdateKxDatabaseResponse":
        return dc_td.UpdateKxDatabaseResponse.make_one(res)

    def update_kx_dataview(
        self,
        res: "bs_td.UpdateKxDataviewResponseTypeDef",
    ) -> "dc_td.UpdateKxDataviewResponse":
        return dc_td.UpdateKxDataviewResponse.make_one(res)

    def update_kx_environment(
        self,
        res: "bs_td.UpdateKxEnvironmentResponseTypeDef",
    ) -> "dc_td.UpdateKxEnvironmentResponse":
        return dc_td.UpdateKxEnvironmentResponse.make_one(res)

    def update_kx_environment_network(
        self,
        res: "bs_td.UpdateKxEnvironmentNetworkResponseTypeDef",
    ) -> "dc_td.UpdateKxEnvironmentNetworkResponse":
        return dc_td.UpdateKxEnvironmentNetworkResponse.make_one(res)

    def update_kx_user(
        self,
        res: "bs_td.UpdateKxUserResponseTypeDef",
    ) -> "dc_td.UpdateKxUserResponse":
        return dc_td.UpdateKxUserResponse.make_one(res)

    def update_kx_volume(
        self,
        res: "bs_td.UpdateKxVolumeResponseTypeDef",
    ) -> "dc_td.UpdateKxVolumeResponse":
        return dc_td.UpdateKxVolumeResponse.make_one(res)


finspace_caster = FINSPACECaster()
