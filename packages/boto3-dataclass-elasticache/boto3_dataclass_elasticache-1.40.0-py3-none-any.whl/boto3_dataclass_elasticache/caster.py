# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_elasticache import type_defs as bs_td


class ELASTICACHECaster:

    def add_tags_to_resource(
        self,
        res: "bs_td.TagListMessageTypeDef",
    ) -> "dc_td.TagListMessage":
        return dc_td.TagListMessage.make_one(res)

    def authorize_cache_security_group_ingress(
        self,
        res: "bs_td.AuthorizeCacheSecurityGroupIngressResultTypeDef",
    ) -> "dc_td.AuthorizeCacheSecurityGroupIngressResult":
        return dc_td.AuthorizeCacheSecurityGroupIngressResult.make_one(res)

    def batch_apply_update_action(
        self,
        res: "bs_td.UpdateActionResultsMessageTypeDef",
    ) -> "dc_td.UpdateActionResultsMessage":
        return dc_td.UpdateActionResultsMessage.make_one(res)

    def batch_stop_update_action(
        self,
        res: "bs_td.UpdateActionResultsMessageTypeDef",
    ) -> "dc_td.UpdateActionResultsMessage":
        return dc_td.UpdateActionResultsMessage.make_one(res)

    def complete_migration(
        self,
        res: "bs_td.CompleteMigrationResponseTypeDef",
    ) -> "dc_td.CompleteMigrationResponse":
        return dc_td.CompleteMigrationResponse.make_one(res)

    def copy_serverless_cache_snapshot(
        self,
        res: "bs_td.CopyServerlessCacheSnapshotResponseTypeDef",
    ) -> "dc_td.CopyServerlessCacheSnapshotResponse":
        return dc_td.CopyServerlessCacheSnapshotResponse.make_one(res)

    def copy_snapshot(
        self,
        res: "bs_td.CopySnapshotResultTypeDef",
    ) -> "dc_td.CopySnapshotResult":
        return dc_td.CopySnapshotResult.make_one(res)

    def create_cache_cluster(
        self,
        res: "bs_td.CreateCacheClusterResultTypeDef",
    ) -> "dc_td.CreateCacheClusterResult":
        return dc_td.CreateCacheClusterResult.make_one(res)

    def create_cache_parameter_group(
        self,
        res: "bs_td.CreateCacheParameterGroupResultTypeDef",
    ) -> "dc_td.CreateCacheParameterGroupResult":
        return dc_td.CreateCacheParameterGroupResult.make_one(res)

    def create_cache_security_group(
        self,
        res: "bs_td.CreateCacheSecurityGroupResultTypeDef",
    ) -> "dc_td.CreateCacheSecurityGroupResult":
        return dc_td.CreateCacheSecurityGroupResult.make_one(res)

    def create_cache_subnet_group(
        self,
        res: "bs_td.CreateCacheSubnetGroupResultTypeDef",
    ) -> "dc_td.CreateCacheSubnetGroupResult":
        return dc_td.CreateCacheSubnetGroupResult.make_one(res)

    def create_global_replication_group(
        self,
        res: "bs_td.CreateGlobalReplicationGroupResultTypeDef",
    ) -> "dc_td.CreateGlobalReplicationGroupResult":
        return dc_td.CreateGlobalReplicationGroupResult.make_one(res)

    def create_replication_group(
        self,
        res: "bs_td.CreateReplicationGroupResultTypeDef",
    ) -> "dc_td.CreateReplicationGroupResult":
        return dc_td.CreateReplicationGroupResult.make_one(res)

    def create_serverless_cache(
        self,
        res: "bs_td.CreateServerlessCacheResponseTypeDef",
    ) -> "dc_td.CreateServerlessCacheResponse":
        return dc_td.CreateServerlessCacheResponse.make_one(res)

    def create_serverless_cache_snapshot(
        self,
        res: "bs_td.CreateServerlessCacheSnapshotResponseTypeDef",
    ) -> "dc_td.CreateServerlessCacheSnapshotResponse":
        return dc_td.CreateServerlessCacheSnapshotResponse.make_one(res)

    def create_snapshot(
        self,
        res: "bs_td.CreateSnapshotResultTypeDef",
    ) -> "dc_td.CreateSnapshotResult":
        return dc_td.CreateSnapshotResult.make_one(res)

    def create_user(
        self,
        res: "bs_td.UserResponseTypeDef",
    ) -> "dc_td.UserResponse":
        return dc_td.UserResponse.make_one(res)

    def create_user_group(
        self,
        res: "bs_td.UserGroupResponseTypeDef",
    ) -> "dc_td.UserGroupResponse":
        return dc_td.UserGroupResponse.make_one(res)

    def decrease_node_groups_in_global_replication_group(
        self,
        res: "bs_td.DecreaseNodeGroupsInGlobalReplicationGroupResultTypeDef",
    ) -> "dc_td.DecreaseNodeGroupsInGlobalReplicationGroupResult":
        return dc_td.DecreaseNodeGroupsInGlobalReplicationGroupResult.make_one(res)

    def decrease_replica_count(
        self,
        res: "bs_td.DecreaseReplicaCountResultTypeDef",
    ) -> "dc_td.DecreaseReplicaCountResult":
        return dc_td.DecreaseReplicaCountResult.make_one(res)

    def delete_cache_cluster(
        self,
        res: "bs_td.DeleteCacheClusterResultTypeDef",
    ) -> "dc_td.DeleteCacheClusterResult":
        return dc_td.DeleteCacheClusterResult.make_one(res)

    def delete_cache_parameter_group(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_cache_security_group(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_cache_subnet_group(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_global_replication_group(
        self,
        res: "bs_td.DeleteGlobalReplicationGroupResultTypeDef",
    ) -> "dc_td.DeleteGlobalReplicationGroupResult":
        return dc_td.DeleteGlobalReplicationGroupResult.make_one(res)

    def delete_replication_group(
        self,
        res: "bs_td.DeleteReplicationGroupResultTypeDef",
    ) -> "dc_td.DeleteReplicationGroupResult":
        return dc_td.DeleteReplicationGroupResult.make_one(res)

    def delete_serverless_cache(
        self,
        res: "bs_td.DeleteServerlessCacheResponseTypeDef",
    ) -> "dc_td.DeleteServerlessCacheResponse":
        return dc_td.DeleteServerlessCacheResponse.make_one(res)

    def delete_serverless_cache_snapshot(
        self,
        res: "bs_td.DeleteServerlessCacheSnapshotResponseTypeDef",
    ) -> "dc_td.DeleteServerlessCacheSnapshotResponse":
        return dc_td.DeleteServerlessCacheSnapshotResponse.make_one(res)

    def delete_snapshot(
        self,
        res: "bs_td.DeleteSnapshotResultTypeDef",
    ) -> "dc_td.DeleteSnapshotResult":
        return dc_td.DeleteSnapshotResult.make_one(res)

    def delete_user(
        self,
        res: "bs_td.UserResponseTypeDef",
    ) -> "dc_td.UserResponse":
        return dc_td.UserResponse.make_one(res)

    def delete_user_group(
        self,
        res: "bs_td.UserGroupResponseTypeDef",
    ) -> "dc_td.UserGroupResponse":
        return dc_td.UserGroupResponse.make_one(res)

    def describe_cache_clusters(
        self,
        res: "bs_td.CacheClusterMessageTypeDef",
    ) -> "dc_td.CacheClusterMessage":
        return dc_td.CacheClusterMessage.make_one(res)

    def describe_cache_engine_versions(
        self,
        res: "bs_td.CacheEngineVersionMessageTypeDef",
    ) -> "dc_td.CacheEngineVersionMessage":
        return dc_td.CacheEngineVersionMessage.make_one(res)

    def describe_cache_parameter_groups(
        self,
        res: "bs_td.CacheParameterGroupsMessageTypeDef",
    ) -> "dc_td.CacheParameterGroupsMessage":
        return dc_td.CacheParameterGroupsMessage.make_one(res)

    def describe_cache_parameters(
        self,
        res: "bs_td.CacheParameterGroupDetailsTypeDef",
    ) -> "dc_td.CacheParameterGroupDetails":
        return dc_td.CacheParameterGroupDetails.make_one(res)

    def describe_cache_security_groups(
        self,
        res: "bs_td.CacheSecurityGroupMessageTypeDef",
    ) -> "dc_td.CacheSecurityGroupMessage":
        return dc_td.CacheSecurityGroupMessage.make_one(res)

    def describe_cache_subnet_groups(
        self,
        res: "bs_td.CacheSubnetGroupMessageTypeDef",
    ) -> "dc_td.CacheSubnetGroupMessage":
        return dc_td.CacheSubnetGroupMessage.make_one(res)

    def describe_engine_default_parameters(
        self,
        res: "bs_td.DescribeEngineDefaultParametersResultTypeDef",
    ) -> "dc_td.DescribeEngineDefaultParametersResult":
        return dc_td.DescribeEngineDefaultParametersResult.make_one(res)

    def describe_events(
        self,
        res: "bs_td.EventsMessageTypeDef",
    ) -> "dc_td.EventsMessage":
        return dc_td.EventsMessage.make_one(res)

    def describe_global_replication_groups(
        self,
        res: "bs_td.DescribeGlobalReplicationGroupsResultTypeDef",
    ) -> "dc_td.DescribeGlobalReplicationGroupsResult":
        return dc_td.DescribeGlobalReplicationGroupsResult.make_one(res)

    def describe_replication_groups(
        self,
        res: "bs_td.ReplicationGroupMessageTypeDef",
    ) -> "dc_td.ReplicationGroupMessage":
        return dc_td.ReplicationGroupMessage.make_one(res)

    def describe_reserved_cache_nodes(
        self,
        res: "bs_td.ReservedCacheNodeMessageTypeDef",
    ) -> "dc_td.ReservedCacheNodeMessage":
        return dc_td.ReservedCacheNodeMessage.make_one(res)

    def describe_reserved_cache_nodes_offerings(
        self,
        res: "bs_td.ReservedCacheNodesOfferingMessageTypeDef",
    ) -> "dc_td.ReservedCacheNodesOfferingMessage":
        return dc_td.ReservedCacheNodesOfferingMessage.make_one(res)

    def describe_serverless_cache_snapshots(
        self,
        res: "bs_td.DescribeServerlessCacheSnapshotsResponseTypeDef",
    ) -> "dc_td.DescribeServerlessCacheSnapshotsResponse":
        return dc_td.DescribeServerlessCacheSnapshotsResponse.make_one(res)

    def describe_serverless_caches(
        self,
        res: "bs_td.DescribeServerlessCachesResponseTypeDef",
    ) -> "dc_td.DescribeServerlessCachesResponse":
        return dc_td.DescribeServerlessCachesResponse.make_one(res)

    def describe_service_updates(
        self,
        res: "bs_td.ServiceUpdatesMessageTypeDef",
    ) -> "dc_td.ServiceUpdatesMessage":
        return dc_td.ServiceUpdatesMessage.make_one(res)

    def describe_snapshots(
        self,
        res: "bs_td.DescribeSnapshotsListMessageTypeDef",
    ) -> "dc_td.DescribeSnapshotsListMessage":
        return dc_td.DescribeSnapshotsListMessage.make_one(res)

    def describe_update_actions(
        self,
        res: "bs_td.UpdateActionsMessageTypeDef",
    ) -> "dc_td.UpdateActionsMessage":
        return dc_td.UpdateActionsMessage.make_one(res)

    def describe_user_groups(
        self,
        res: "bs_td.DescribeUserGroupsResultTypeDef",
    ) -> "dc_td.DescribeUserGroupsResult":
        return dc_td.DescribeUserGroupsResult.make_one(res)

    def describe_users(
        self,
        res: "bs_td.DescribeUsersResultTypeDef",
    ) -> "dc_td.DescribeUsersResult":
        return dc_td.DescribeUsersResult.make_one(res)

    def disassociate_global_replication_group(
        self,
        res: "bs_td.DisassociateGlobalReplicationGroupResultTypeDef",
    ) -> "dc_td.DisassociateGlobalReplicationGroupResult":
        return dc_td.DisassociateGlobalReplicationGroupResult.make_one(res)

    def export_serverless_cache_snapshot(
        self,
        res: "bs_td.ExportServerlessCacheSnapshotResponseTypeDef",
    ) -> "dc_td.ExportServerlessCacheSnapshotResponse":
        return dc_td.ExportServerlessCacheSnapshotResponse.make_one(res)

    def failover_global_replication_group(
        self,
        res: "bs_td.FailoverGlobalReplicationGroupResultTypeDef",
    ) -> "dc_td.FailoverGlobalReplicationGroupResult":
        return dc_td.FailoverGlobalReplicationGroupResult.make_one(res)

    def increase_node_groups_in_global_replication_group(
        self,
        res: "bs_td.IncreaseNodeGroupsInGlobalReplicationGroupResultTypeDef",
    ) -> "dc_td.IncreaseNodeGroupsInGlobalReplicationGroupResult":
        return dc_td.IncreaseNodeGroupsInGlobalReplicationGroupResult.make_one(res)

    def increase_replica_count(
        self,
        res: "bs_td.IncreaseReplicaCountResultTypeDef",
    ) -> "dc_td.IncreaseReplicaCountResult":
        return dc_td.IncreaseReplicaCountResult.make_one(res)

    def list_allowed_node_type_modifications(
        self,
        res: "bs_td.AllowedNodeTypeModificationsMessageTypeDef",
    ) -> "dc_td.AllowedNodeTypeModificationsMessage":
        return dc_td.AllowedNodeTypeModificationsMessage.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.TagListMessageTypeDef",
    ) -> "dc_td.TagListMessage":
        return dc_td.TagListMessage.make_one(res)

    def modify_cache_cluster(
        self,
        res: "bs_td.ModifyCacheClusterResultTypeDef",
    ) -> "dc_td.ModifyCacheClusterResult":
        return dc_td.ModifyCacheClusterResult.make_one(res)

    def modify_cache_parameter_group(
        self,
        res: "bs_td.CacheParameterGroupNameMessageTypeDef",
    ) -> "dc_td.CacheParameterGroupNameMessage":
        return dc_td.CacheParameterGroupNameMessage.make_one(res)

    def modify_cache_subnet_group(
        self,
        res: "bs_td.ModifyCacheSubnetGroupResultTypeDef",
    ) -> "dc_td.ModifyCacheSubnetGroupResult":
        return dc_td.ModifyCacheSubnetGroupResult.make_one(res)

    def modify_global_replication_group(
        self,
        res: "bs_td.ModifyGlobalReplicationGroupResultTypeDef",
    ) -> "dc_td.ModifyGlobalReplicationGroupResult":
        return dc_td.ModifyGlobalReplicationGroupResult.make_one(res)

    def modify_replication_group(
        self,
        res: "bs_td.ModifyReplicationGroupResultTypeDef",
    ) -> "dc_td.ModifyReplicationGroupResult":
        return dc_td.ModifyReplicationGroupResult.make_one(res)

    def modify_replication_group_shard_configuration(
        self,
        res: "bs_td.ModifyReplicationGroupShardConfigurationResultTypeDef",
    ) -> "dc_td.ModifyReplicationGroupShardConfigurationResult":
        return dc_td.ModifyReplicationGroupShardConfigurationResult.make_one(res)

    def modify_serverless_cache(
        self,
        res: "bs_td.ModifyServerlessCacheResponseTypeDef",
    ) -> "dc_td.ModifyServerlessCacheResponse":
        return dc_td.ModifyServerlessCacheResponse.make_one(res)

    def modify_user(
        self,
        res: "bs_td.UserResponseTypeDef",
    ) -> "dc_td.UserResponse":
        return dc_td.UserResponse.make_one(res)

    def modify_user_group(
        self,
        res: "bs_td.UserGroupResponseTypeDef",
    ) -> "dc_td.UserGroupResponse":
        return dc_td.UserGroupResponse.make_one(res)

    def purchase_reserved_cache_nodes_offering(
        self,
        res: "bs_td.PurchaseReservedCacheNodesOfferingResultTypeDef",
    ) -> "dc_td.PurchaseReservedCacheNodesOfferingResult":
        return dc_td.PurchaseReservedCacheNodesOfferingResult.make_one(res)

    def rebalance_slots_in_global_replication_group(
        self,
        res: "bs_td.RebalanceSlotsInGlobalReplicationGroupResultTypeDef",
    ) -> "dc_td.RebalanceSlotsInGlobalReplicationGroupResult":
        return dc_td.RebalanceSlotsInGlobalReplicationGroupResult.make_one(res)

    def reboot_cache_cluster(
        self,
        res: "bs_td.RebootCacheClusterResultTypeDef",
    ) -> "dc_td.RebootCacheClusterResult":
        return dc_td.RebootCacheClusterResult.make_one(res)

    def remove_tags_from_resource(
        self,
        res: "bs_td.TagListMessageTypeDef",
    ) -> "dc_td.TagListMessage":
        return dc_td.TagListMessage.make_one(res)

    def reset_cache_parameter_group(
        self,
        res: "bs_td.CacheParameterGroupNameMessageTypeDef",
    ) -> "dc_td.CacheParameterGroupNameMessage":
        return dc_td.CacheParameterGroupNameMessage.make_one(res)

    def revoke_cache_security_group_ingress(
        self,
        res: "bs_td.RevokeCacheSecurityGroupIngressResultTypeDef",
    ) -> "dc_td.RevokeCacheSecurityGroupIngressResult":
        return dc_td.RevokeCacheSecurityGroupIngressResult.make_one(res)

    def start_migration(
        self,
        res: "bs_td.StartMigrationResponseTypeDef",
    ) -> "dc_td.StartMigrationResponse":
        return dc_td.StartMigrationResponse.make_one(res)

    def test_failover(
        self,
        res: "bs_td.TestFailoverResultTypeDef",
    ) -> "dc_td.TestFailoverResult":
        return dc_td.TestFailoverResult.make_one(res)

    def test_migration(
        self,
        res: "bs_td.TestMigrationResponseTypeDef",
    ) -> "dc_td.TestMigrationResponse":
        return dc_td.TestMigrationResponse.make_one(res)


elasticache_caster = ELASTICACHECaster()
