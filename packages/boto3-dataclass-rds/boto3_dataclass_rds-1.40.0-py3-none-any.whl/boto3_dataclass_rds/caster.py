# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_rds import type_defs as bs_td


class RDSCaster:

    def add_role_to_db_cluster(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def add_role_to_db_instance(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def add_source_identifier_to_subscription(
        self,
        res: "bs_td.AddSourceIdentifierToSubscriptionResultTypeDef",
    ) -> "dc_td.AddSourceIdentifierToSubscriptionResult":
        return dc_td.AddSourceIdentifierToSubscriptionResult.make_one(res)

    def add_tags_to_resource(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def apply_pending_maintenance_action(
        self,
        res: "bs_td.ApplyPendingMaintenanceActionResultTypeDef",
    ) -> "dc_td.ApplyPendingMaintenanceActionResult":
        return dc_td.ApplyPendingMaintenanceActionResult.make_one(res)

    def authorize_db_security_group_ingress(
        self,
        res: "bs_td.AuthorizeDBSecurityGroupIngressResultTypeDef",
    ) -> "dc_td.AuthorizeDBSecurityGroupIngressResult":
        return dc_td.AuthorizeDBSecurityGroupIngressResult.make_one(res)

    def backtrack_db_cluster(
        self,
        res: "bs_td.DBClusterBacktrackResponseTypeDef",
    ) -> "dc_td.DBClusterBacktrackResponse":
        return dc_td.DBClusterBacktrackResponse.make_one(res)

    def cancel_export_task(
        self,
        res: "bs_td.ExportTaskResponseTypeDef",
    ) -> "dc_td.ExportTaskResponse":
        return dc_td.ExportTaskResponse.make_one(res)

    def copy_db_cluster_parameter_group(
        self,
        res: "bs_td.CopyDBClusterParameterGroupResultTypeDef",
    ) -> "dc_td.CopyDBClusterParameterGroupResult":
        return dc_td.CopyDBClusterParameterGroupResult.make_one(res)

    def copy_db_cluster_snapshot(
        self,
        res: "bs_td.CopyDBClusterSnapshotResultTypeDef",
    ) -> "dc_td.CopyDBClusterSnapshotResult":
        return dc_td.CopyDBClusterSnapshotResult.make_one(res)

    def copy_db_parameter_group(
        self,
        res: "bs_td.CopyDBParameterGroupResultTypeDef",
    ) -> "dc_td.CopyDBParameterGroupResult":
        return dc_td.CopyDBParameterGroupResult.make_one(res)

    def copy_db_snapshot(
        self,
        res: "bs_td.CopyDBSnapshotResultTypeDef",
    ) -> "dc_td.CopyDBSnapshotResult":
        return dc_td.CopyDBSnapshotResult.make_one(res)

    def copy_option_group(
        self,
        res: "bs_td.CopyOptionGroupResultTypeDef",
    ) -> "dc_td.CopyOptionGroupResult":
        return dc_td.CopyOptionGroupResult.make_one(res)

    def create_blue_green_deployment(
        self,
        res: "bs_td.CreateBlueGreenDeploymentResponseTypeDef",
    ) -> "dc_td.CreateBlueGreenDeploymentResponse":
        return dc_td.CreateBlueGreenDeploymentResponse.make_one(res)

    def create_custom_db_engine_version(
        self,
        res: "bs_td.DBEngineVersionResponseTypeDef",
    ) -> "dc_td.DBEngineVersionResponse":
        return dc_td.DBEngineVersionResponse.make_one(res)

    def create_db_cluster(
        self,
        res: "bs_td.CreateDBClusterResultTypeDef",
    ) -> "dc_td.CreateDBClusterResult":
        return dc_td.CreateDBClusterResult.make_one(res)

    def create_db_cluster_endpoint(
        self,
        res: "bs_td.DBClusterEndpointResponseTypeDef",
    ) -> "dc_td.DBClusterEndpointResponse":
        return dc_td.DBClusterEndpointResponse.make_one(res)

    def create_db_cluster_parameter_group(
        self,
        res: "bs_td.CreateDBClusterParameterGroupResultTypeDef",
    ) -> "dc_td.CreateDBClusterParameterGroupResult":
        return dc_td.CreateDBClusterParameterGroupResult.make_one(res)

    def create_db_cluster_snapshot(
        self,
        res: "bs_td.CreateDBClusterSnapshotResultTypeDef",
    ) -> "dc_td.CreateDBClusterSnapshotResult":
        return dc_td.CreateDBClusterSnapshotResult.make_one(res)

    def create_db_instance(
        self,
        res: "bs_td.CreateDBInstanceResultTypeDef",
    ) -> "dc_td.CreateDBInstanceResult":
        return dc_td.CreateDBInstanceResult.make_one(res)

    def create_db_instance_read_replica(
        self,
        res: "bs_td.CreateDBInstanceReadReplicaResultTypeDef",
    ) -> "dc_td.CreateDBInstanceReadReplicaResult":
        return dc_td.CreateDBInstanceReadReplicaResult.make_one(res)

    def create_db_parameter_group(
        self,
        res: "bs_td.CreateDBParameterGroupResultTypeDef",
    ) -> "dc_td.CreateDBParameterGroupResult":
        return dc_td.CreateDBParameterGroupResult.make_one(res)

    def create_db_proxy(
        self,
        res: "bs_td.CreateDBProxyResponseTypeDef",
    ) -> "dc_td.CreateDBProxyResponse":
        return dc_td.CreateDBProxyResponse.make_one(res)

    def create_db_proxy_endpoint(
        self,
        res: "bs_td.CreateDBProxyEndpointResponseTypeDef",
    ) -> "dc_td.CreateDBProxyEndpointResponse":
        return dc_td.CreateDBProxyEndpointResponse.make_one(res)

    def create_db_security_group(
        self,
        res: "bs_td.CreateDBSecurityGroupResultTypeDef",
    ) -> "dc_td.CreateDBSecurityGroupResult":
        return dc_td.CreateDBSecurityGroupResult.make_one(res)

    def create_db_shard_group(
        self,
        res: "bs_td.DBShardGroupResponseTypeDef",
    ) -> "dc_td.DBShardGroupResponse":
        return dc_td.DBShardGroupResponse.make_one(res)

    def create_db_snapshot(
        self,
        res: "bs_td.CreateDBSnapshotResultTypeDef",
    ) -> "dc_td.CreateDBSnapshotResult":
        return dc_td.CreateDBSnapshotResult.make_one(res)

    def create_db_subnet_group(
        self,
        res: "bs_td.CreateDBSubnetGroupResultTypeDef",
    ) -> "dc_td.CreateDBSubnetGroupResult":
        return dc_td.CreateDBSubnetGroupResult.make_one(res)

    def create_event_subscription(
        self,
        res: "bs_td.CreateEventSubscriptionResultTypeDef",
    ) -> "dc_td.CreateEventSubscriptionResult":
        return dc_td.CreateEventSubscriptionResult.make_one(res)

    def create_global_cluster(
        self,
        res: "bs_td.CreateGlobalClusterResultTypeDef",
    ) -> "dc_td.CreateGlobalClusterResult":
        return dc_td.CreateGlobalClusterResult.make_one(res)

    def create_integration(
        self,
        res: "bs_td.IntegrationResponseTypeDef",
    ) -> "dc_td.IntegrationResponse":
        return dc_td.IntegrationResponse.make_one(res)

    def create_option_group(
        self,
        res: "bs_td.CreateOptionGroupResultTypeDef",
    ) -> "dc_td.CreateOptionGroupResult":
        return dc_td.CreateOptionGroupResult.make_one(res)

    def create_tenant_database(
        self,
        res: "bs_td.CreateTenantDatabaseResultTypeDef",
    ) -> "dc_td.CreateTenantDatabaseResult":
        return dc_td.CreateTenantDatabaseResult.make_one(res)

    def delete_blue_green_deployment(
        self,
        res: "bs_td.DeleteBlueGreenDeploymentResponseTypeDef",
    ) -> "dc_td.DeleteBlueGreenDeploymentResponse":
        return dc_td.DeleteBlueGreenDeploymentResponse.make_one(res)

    def delete_custom_db_engine_version(
        self,
        res: "bs_td.DBEngineVersionResponseTypeDef",
    ) -> "dc_td.DBEngineVersionResponse":
        return dc_td.DBEngineVersionResponse.make_one(res)

    def delete_db_cluster(
        self,
        res: "bs_td.DeleteDBClusterResultTypeDef",
    ) -> "dc_td.DeleteDBClusterResult":
        return dc_td.DeleteDBClusterResult.make_one(res)

    def delete_db_cluster_automated_backup(
        self,
        res: "bs_td.DeleteDBClusterAutomatedBackupResultTypeDef",
    ) -> "dc_td.DeleteDBClusterAutomatedBackupResult":
        return dc_td.DeleteDBClusterAutomatedBackupResult.make_one(res)

    def delete_db_cluster_endpoint(
        self,
        res: "bs_td.DBClusterEndpointResponseTypeDef",
    ) -> "dc_td.DBClusterEndpointResponse":
        return dc_td.DBClusterEndpointResponse.make_one(res)

    def delete_db_cluster_parameter_group(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_db_cluster_snapshot(
        self,
        res: "bs_td.DeleteDBClusterSnapshotResultTypeDef",
    ) -> "dc_td.DeleteDBClusterSnapshotResult":
        return dc_td.DeleteDBClusterSnapshotResult.make_one(res)

    def delete_db_instance(
        self,
        res: "bs_td.DeleteDBInstanceResultTypeDef",
    ) -> "dc_td.DeleteDBInstanceResult":
        return dc_td.DeleteDBInstanceResult.make_one(res)

    def delete_db_instance_automated_backup(
        self,
        res: "bs_td.DeleteDBInstanceAutomatedBackupResultTypeDef",
    ) -> "dc_td.DeleteDBInstanceAutomatedBackupResult":
        return dc_td.DeleteDBInstanceAutomatedBackupResult.make_one(res)

    def delete_db_parameter_group(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_db_proxy(
        self,
        res: "bs_td.DeleteDBProxyResponseTypeDef",
    ) -> "dc_td.DeleteDBProxyResponse":
        return dc_td.DeleteDBProxyResponse.make_one(res)

    def delete_db_proxy_endpoint(
        self,
        res: "bs_td.DeleteDBProxyEndpointResponseTypeDef",
    ) -> "dc_td.DeleteDBProxyEndpointResponse":
        return dc_td.DeleteDBProxyEndpointResponse.make_one(res)

    def delete_db_security_group(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_db_shard_group(
        self,
        res: "bs_td.DBShardGroupResponseTypeDef",
    ) -> "dc_td.DBShardGroupResponse":
        return dc_td.DBShardGroupResponse.make_one(res)

    def delete_db_snapshot(
        self,
        res: "bs_td.DeleteDBSnapshotResultTypeDef",
    ) -> "dc_td.DeleteDBSnapshotResult":
        return dc_td.DeleteDBSnapshotResult.make_one(res)

    def delete_db_subnet_group(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_event_subscription(
        self,
        res: "bs_td.DeleteEventSubscriptionResultTypeDef",
    ) -> "dc_td.DeleteEventSubscriptionResult":
        return dc_td.DeleteEventSubscriptionResult.make_one(res)

    def delete_global_cluster(
        self,
        res: "bs_td.DeleteGlobalClusterResultTypeDef",
    ) -> "dc_td.DeleteGlobalClusterResult":
        return dc_td.DeleteGlobalClusterResult.make_one(res)

    def delete_integration(
        self,
        res: "bs_td.IntegrationResponseTypeDef",
    ) -> "dc_td.IntegrationResponse":
        return dc_td.IntegrationResponse.make_one(res)

    def delete_option_group(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_tenant_database(
        self,
        res: "bs_td.DeleteTenantDatabaseResultTypeDef",
    ) -> "dc_td.DeleteTenantDatabaseResult":
        return dc_td.DeleteTenantDatabaseResult.make_one(res)

    def describe_account_attributes(
        self,
        res: "bs_td.AccountAttributesMessageTypeDef",
    ) -> "dc_td.AccountAttributesMessage":
        return dc_td.AccountAttributesMessage.make_one(res)

    def describe_blue_green_deployments(
        self,
        res: "bs_td.DescribeBlueGreenDeploymentsResponseTypeDef",
    ) -> "dc_td.DescribeBlueGreenDeploymentsResponse":
        return dc_td.DescribeBlueGreenDeploymentsResponse.make_one(res)

    def describe_certificates(
        self,
        res: "bs_td.CertificateMessageTypeDef",
    ) -> "dc_td.CertificateMessage":
        return dc_td.CertificateMessage.make_one(res)

    def describe_db_cluster_automated_backups(
        self,
        res: "bs_td.DBClusterAutomatedBackupMessageTypeDef",
    ) -> "dc_td.DBClusterAutomatedBackupMessage":
        return dc_td.DBClusterAutomatedBackupMessage.make_one(res)

    def describe_db_cluster_backtracks(
        self,
        res: "bs_td.DBClusterBacktrackMessageTypeDef",
    ) -> "dc_td.DBClusterBacktrackMessage":
        return dc_td.DBClusterBacktrackMessage.make_one(res)

    def describe_db_cluster_endpoints(
        self,
        res: "bs_td.DBClusterEndpointMessageTypeDef",
    ) -> "dc_td.DBClusterEndpointMessage":
        return dc_td.DBClusterEndpointMessage.make_one(res)

    def describe_db_cluster_parameter_groups(
        self,
        res: "bs_td.DBClusterParameterGroupsMessageTypeDef",
    ) -> "dc_td.DBClusterParameterGroupsMessage":
        return dc_td.DBClusterParameterGroupsMessage.make_one(res)

    def describe_db_cluster_parameters(
        self,
        res: "bs_td.DBClusterParameterGroupDetailsTypeDef",
    ) -> "dc_td.DBClusterParameterGroupDetails":
        return dc_td.DBClusterParameterGroupDetails.make_one(res)

    def describe_db_cluster_snapshot_attributes(
        self,
        res: "bs_td.DescribeDBClusterSnapshotAttributesResultTypeDef",
    ) -> "dc_td.DescribeDBClusterSnapshotAttributesResult":
        return dc_td.DescribeDBClusterSnapshotAttributesResult.make_one(res)

    def describe_db_cluster_snapshots(
        self,
        res: "bs_td.DBClusterSnapshotMessageTypeDef",
    ) -> "dc_td.DBClusterSnapshotMessage":
        return dc_td.DBClusterSnapshotMessage.make_one(res)

    def describe_db_clusters(
        self,
        res: "bs_td.DBClusterMessageTypeDef",
    ) -> "dc_td.DBClusterMessage":
        return dc_td.DBClusterMessage.make_one(res)

    def describe_db_engine_versions(
        self,
        res: "bs_td.DBEngineVersionMessageTypeDef",
    ) -> "dc_td.DBEngineVersionMessage":
        return dc_td.DBEngineVersionMessage.make_one(res)

    def describe_db_instance_automated_backups(
        self,
        res: "bs_td.DBInstanceAutomatedBackupMessageTypeDef",
    ) -> "dc_td.DBInstanceAutomatedBackupMessage":
        return dc_td.DBInstanceAutomatedBackupMessage.make_one(res)

    def describe_db_instances(
        self,
        res: "bs_td.DBInstanceMessageTypeDef",
    ) -> "dc_td.DBInstanceMessage":
        return dc_td.DBInstanceMessage.make_one(res)

    def describe_db_log_files(
        self,
        res: "bs_td.DescribeDBLogFilesResponseTypeDef",
    ) -> "dc_td.DescribeDBLogFilesResponse":
        return dc_td.DescribeDBLogFilesResponse.make_one(res)

    def describe_db_major_engine_versions(
        self,
        res: "bs_td.DescribeDBMajorEngineVersionsResponseTypeDef",
    ) -> "dc_td.DescribeDBMajorEngineVersionsResponse":
        return dc_td.DescribeDBMajorEngineVersionsResponse.make_one(res)

    def describe_db_parameter_groups(
        self,
        res: "bs_td.DBParameterGroupsMessageTypeDef",
    ) -> "dc_td.DBParameterGroupsMessage":
        return dc_td.DBParameterGroupsMessage.make_one(res)

    def describe_db_parameters(
        self,
        res: "bs_td.DBParameterGroupDetailsTypeDef",
    ) -> "dc_td.DBParameterGroupDetails":
        return dc_td.DBParameterGroupDetails.make_one(res)

    def describe_db_proxies(
        self,
        res: "bs_td.DescribeDBProxiesResponseTypeDef",
    ) -> "dc_td.DescribeDBProxiesResponse":
        return dc_td.DescribeDBProxiesResponse.make_one(res)

    def describe_db_proxy_endpoints(
        self,
        res: "bs_td.DescribeDBProxyEndpointsResponseTypeDef",
    ) -> "dc_td.DescribeDBProxyEndpointsResponse":
        return dc_td.DescribeDBProxyEndpointsResponse.make_one(res)

    def describe_db_proxy_target_groups(
        self,
        res: "bs_td.DescribeDBProxyTargetGroupsResponseTypeDef",
    ) -> "dc_td.DescribeDBProxyTargetGroupsResponse":
        return dc_td.DescribeDBProxyTargetGroupsResponse.make_one(res)

    def describe_db_proxy_targets(
        self,
        res: "bs_td.DescribeDBProxyTargetsResponseTypeDef",
    ) -> "dc_td.DescribeDBProxyTargetsResponse":
        return dc_td.DescribeDBProxyTargetsResponse.make_one(res)

    def describe_db_recommendations(
        self,
        res: "bs_td.DBRecommendationsMessageTypeDef",
    ) -> "dc_td.DBRecommendationsMessage":
        return dc_td.DBRecommendationsMessage.make_one(res)

    def describe_db_security_groups(
        self,
        res: "bs_td.DBSecurityGroupMessageTypeDef",
    ) -> "dc_td.DBSecurityGroupMessage":
        return dc_td.DBSecurityGroupMessage.make_one(res)

    def describe_db_shard_groups(
        self,
        res: "bs_td.DescribeDBShardGroupsResponseTypeDef",
    ) -> "dc_td.DescribeDBShardGroupsResponse":
        return dc_td.DescribeDBShardGroupsResponse.make_one(res)

    def describe_db_snapshot_attributes(
        self,
        res: "bs_td.DescribeDBSnapshotAttributesResultTypeDef",
    ) -> "dc_td.DescribeDBSnapshotAttributesResult":
        return dc_td.DescribeDBSnapshotAttributesResult.make_one(res)

    def describe_db_snapshot_tenant_databases(
        self,
        res: "bs_td.DBSnapshotTenantDatabasesMessageTypeDef",
    ) -> "dc_td.DBSnapshotTenantDatabasesMessage":
        return dc_td.DBSnapshotTenantDatabasesMessage.make_one(res)

    def describe_db_snapshots(
        self,
        res: "bs_td.DBSnapshotMessageTypeDef",
    ) -> "dc_td.DBSnapshotMessage":
        return dc_td.DBSnapshotMessage.make_one(res)

    def describe_db_subnet_groups(
        self,
        res: "bs_td.DBSubnetGroupMessageTypeDef",
    ) -> "dc_td.DBSubnetGroupMessage":
        return dc_td.DBSubnetGroupMessage.make_one(res)

    def describe_engine_default_cluster_parameters(
        self,
        res: "bs_td.DescribeEngineDefaultClusterParametersResultTypeDef",
    ) -> "dc_td.DescribeEngineDefaultClusterParametersResult":
        return dc_td.DescribeEngineDefaultClusterParametersResult.make_one(res)

    def describe_engine_default_parameters(
        self,
        res: "bs_td.DescribeEngineDefaultParametersResultTypeDef",
    ) -> "dc_td.DescribeEngineDefaultParametersResult":
        return dc_td.DescribeEngineDefaultParametersResult.make_one(res)

    def describe_event_categories(
        self,
        res: "bs_td.EventCategoriesMessageTypeDef",
    ) -> "dc_td.EventCategoriesMessage":
        return dc_td.EventCategoriesMessage.make_one(res)

    def describe_event_subscriptions(
        self,
        res: "bs_td.EventSubscriptionsMessageTypeDef",
    ) -> "dc_td.EventSubscriptionsMessage":
        return dc_td.EventSubscriptionsMessage.make_one(res)

    def describe_events(
        self,
        res: "bs_td.EventsMessageTypeDef",
    ) -> "dc_td.EventsMessage":
        return dc_td.EventsMessage.make_one(res)

    def describe_export_tasks(
        self,
        res: "bs_td.ExportTasksMessageTypeDef",
    ) -> "dc_td.ExportTasksMessage":
        return dc_td.ExportTasksMessage.make_one(res)

    def describe_global_clusters(
        self,
        res: "bs_td.GlobalClustersMessageTypeDef",
    ) -> "dc_td.GlobalClustersMessage":
        return dc_td.GlobalClustersMessage.make_one(res)

    def describe_integrations(
        self,
        res: "bs_td.DescribeIntegrationsResponseTypeDef",
    ) -> "dc_td.DescribeIntegrationsResponse":
        return dc_td.DescribeIntegrationsResponse.make_one(res)

    def describe_option_group_options(
        self,
        res: "bs_td.OptionGroupOptionsMessageTypeDef",
    ) -> "dc_td.OptionGroupOptionsMessage":
        return dc_td.OptionGroupOptionsMessage.make_one(res)

    def describe_option_groups(
        self,
        res: "bs_td.OptionGroupsTypeDef",
    ) -> "dc_td.OptionGroups":
        return dc_td.OptionGroups.make_one(res)

    def describe_orderable_db_instance_options(
        self,
        res: "bs_td.OrderableDBInstanceOptionsMessageTypeDef",
    ) -> "dc_td.OrderableDBInstanceOptionsMessage":
        return dc_td.OrderableDBInstanceOptionsMessage.make_one(res)

    def describe_pending_maintenance_actions(
        self,
        res: "bs_td.PendingMaintenanceActionsMessageTypeDef",
    ) -> "dc_td.PendingMaintenanceActionsMessage":
        return dc_td.PendingMaintenanceActionsMessage.make_one(res)

    def describe_reserved_db_instances(
        self,
        res: "bs_td.ReservedDBInstanceMessageTypeDef",
    ) -> "dc_td.ReservedDBInstanceMessage":
        return dc_td.ReservedDBInstanceMessage.make_one(res)

    def describe_reserved_db_instances_offerings(
        self,
        res: "bs_td.ReservedDBInstancesOfferingMessageTypeDef",
    ) -> "dc_td.ReservedDBInstancesOfferingMessage":
        return dc_td.ReservedDBInstancesOfferingMessage.make_one(res)

    def describe_source_regions(
        self,
        res: "bs_td.SourceRegionMessageTypeDef",
    ) -> "dc_td.SourceRegionMessage":
        return dc_td.SourceRegionMessage.make_one(res)

    def describe_tenant_databases(
        self,
        res: "bs_td.TenantDatabasesMessageTypeDef",
    ) -> "dc_td.TenantDatabasesMessage":
        return dc_td.TenantDatabasesMessage.make_one(res)

    def describe_valid_db_instance_modifications(
        self,
        res: "bs_td.DescribeValidDBInstanceModificationsResultTypeDef",
    ) -> "dc_td.DescribeValidDBInstanceModificationsResult":
        return dc_td.DescribeValidDBInstanceModificationsResult.make_one(res)

    def disable_http_endpoint(
        self,
        res: "bs_td.DisableHttpEndpointResponseTypeDef",
    ) -> "dc_td.DisableHttpEndpointResponse":
        return dc_td.DisableHttpEndpointResponse.make_one(res)

    def download_db_log_file_portion(
        self,
        res: "bs_td.DownloadDBLogFilePortionDetailsTypeDef",
    ) -> "dc_td.DownloadDBLogFilePortionDetails":
        return dc_td.DownloadDBLogFilePortionDetails.make_one(res)

    def enable_http_endpoint(
        self,
        res: "bs_td.EnableHttpEndpointResponseTypeDef",
    ) -> "dc_td.EnableHttpEndpointResponse":
        return dc_td.EnableHttpEndpointResponse.make_one(res)

    def failover_db_cluster(
        self,
        res: "bs_td.FailoverDBClusterResultTypeDef",
    ) -> "dc_td.FailoverDBClusterResult":
        return dc_td.FailoverDBClusterResult.make_one(res)

    def failover_global_cluster(
        self,
        res: "bs_td.FailoverGlobalClusterResultTypeDef",
    ) -> "dc_td.FailoverGlobalClusterResult":
        return dc_td.FailoverGlobalClusterResult.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.TagListMessageTypeDef",
    ) -> "dc_td.TagListMessage":
        return dc_td.TagListMessage.make_one(res)

    def modify_activity_stream(
        self,
        res: "bs_td.ModifyActivityStreamResponseTypeDef",
    ) -> "dc_td.ModifyActivityStreamResponse":
        return dc_td.ModifyActivityStreamResponse.make_one(res)

    def modify_certificates(
        self,
        res: "bs_td.ModifyCertificatesResultTypeDef",
    ) -> "dc_td.ModifyCertificatesResult":
        return dc_td.ModifyCertificatesResult.make_one(res)

    def modify_current_db_cluster_capacity(
        self,
        res: "bs_td.DBClusterCapacityInfoTypeDef",
    ) -> "dc_td.DBClusterCapacityInfo":
        return dc_td.DBClusterCapacityInfo.make_one(res)

    def modify_custom_db_engine_version(
        self,
        res: "bs_td.DBEngineVersionResponseTypeDef",
    ) -> "dc_td.DBEngineVersionResponse":
        return dc_td.DBEngineVersionResponse.make_one(res)

    def modify_db_cluster(
        self,
        res: "bs_td.ModifyDBClusterResultTypeDef",
    ) -> "dc_td.ModifyDBClusterResult":
        return dc_td.ModifyDBClusterResult.make_one(res)

    def modify_db_cluster_endpoint(
        self,
        res: "bs_td.DBClusterEndpointResponseTypeDef",
    ) -> "dc_td.DBClusterEndpointResponse":
        return dc_td.DBClusterEndpointResponse.make_one(res)

    def modify_db_cluster_parameter_group(
        self,
        res: "bs_td.DBClusterParameterGroupNameMessageTypeDef",
    ) -> "dc_td.DBClusterParameterGroupNameMessage":
        return dc_td.DBClusterParameterGroupNameMessage.make_one(res)

    def modify_db_cluster_snapshot_attribute(
        self,
        res: "bs_td.ModifyDBClusterSnapshotAttributeResultTypeDef",
    ) -> "dc_td.ModifyDBClusterSnapshotAttributeResult":
        return dc_td.ModifyDBClusterSnapshotAttributeResult.make_one(res)

    def modify_db_instance(
        self,
        res: "bs_td.ModifyDBInstanceResultTypeDef",
    ) -> "dc_td.ModifyDBInstanceResult":
        return dc_td.ModifyDBInstanceResult.make_one(res)

    def modify_db_parameter_group(
        self,
        res: "bs_td.DBParameterGroupNameMessageTypeDef",
    ) -> "dc_td.DBParameterGroupNameMessage":
        return dc_td.DBParameterGroupNameMessage.make_one(res)

    def modify_db_proxy(
        self,
        res: "bs_td.ModifyDBProxyResponseTypeDef",
    ) -> "dc_td.ModifyDBProxyResponse":
        return dc_td.ModifyDBProxyResponse.make_one(res)

    def modify_db_proxy_endpoint(
        self,
        res: "bs_td.ModifyDBProxyEndpointResponseTypeDef",
    ) -> "dc_td.ModifyDBProxyEndpointResponse":
        return dc_td.ModifyDBProxyEndpointResponse.make_one(res)

    def modify_db_proxy_target_group(
        self,
        res: "bs_td.ModifyDBProxyTargetGroupResponseTypeDef",
    ) -> "dc_td.ModifyDBProxyTargetGroupResponse":
        return dc_td.ModifyDBProxyTargetGroupResponse.make_one(res)

    def modify_db_recommendation(
        self,
        res: "bs_td.DBRecommendationMessageTypeDef",
    ) -> "dc_td.DBRecommendationMessage":
        return dc_td.DBRecommendationMessage.make_one(res)

    def modify_db_shard_group(
        self,
        res: "bs_td.DBShardGroupResponseTypeDef",
    ) -> "dc_td.DBShardGroupResponse":
        return dc_td.DBShardGroupResponse.make_one(res)

    def modify_db_snapshot(
        self,
        res: "bs_td.ModifyDBSnapshotResultTypeDef",
    ) -> "dc_td.ModifyDBSnapshotResult":
        return dc_td.ModifyDBSnapshotResult.make_one(res)

    def modify_db_snapshot_attribute(
        self,
        res: "bs_td.ModifyDBSnapshotAttributeResultTypeDef",
    ) -> "dc_td.ModifyDBSnapshotAttributeResult":
        return dc_td.ModifyDBSnapshotAttributeResult.make_one(res)

    def modify_db_subnet_group(
        self,
        res: "bs_td.ModifyDBSubnetGroupResultTypeDef",
    ) -> "dc_td.ModifyDBSubnetGroupResult":
        return dc_td.ModifyDBSubnetGroupResult.make_one(res)

    def modify_event_subscription(
        self,
        res: "bs_td.ModifyEventSubscriptionResultTypeDef",
    ) -> "dc_td.ModifyEventSubscriptionResult":
        return dc_td.ModifyEventSubscriptionResult.make_one(res)

    def modify_global_cluster(
        self,
        res: "bs_td.ModifyGlobalClusterResultTypeDef",
    ) -> "dc_td.ModifyGlobalClusterResult":
        return dc_td.ModifyGlobalClusterResult.make_one(res)

    def modify_integration(
        self,
        res: "bs_td.IntegrationResponseTypeDef",
    ) -> "dc_td.IntegrationResponse":
        return dc_td.IntegrationResponse.make_one(res)

    def modify_option_group(
        self,
        res: "bs_td.ModifyOptionGroupResultTypeDef",
    ) -> "dc_td.ModifyOptionGroupResult":
        return dc_td.ModifyOptionGroupResult.make_one(res)

    def modify_tenant_database(
        self,
        res: "bs_td.ModifyTenantDatabaseResultTypeDef",
    ) -> "dc_td.ModifyTenantDatabaseResult":
        return dc_td.ModifyTenantDatabaseResult.make_one(res)

    def promote_read_replica(
        self,
        res: "bs_td.PromoteReadReplicaResultTypeDef",
    ) -> "dc_td.PromoteReadReplicaResult":
        return dc_td.PromoteReadReplicaResult.make_one(res)

    def promote_read_replica_db_cluster(
        self,
        res: "bs_td.PromoteReadReplicaDBClusterResultTypeDef",
    ) -> "dc_td.PromoteReadReplicaDBClusterResult":
        return dc_td.PromoteReadReplicaDBClusterResult.make_one(res)

    def purchase_reserved_db_instances_offering(
        self,
        res: "bs_td.PurchaseReservedDBInstancesOfferingResultTypeDef",
    ) -> "dc_td.PurchaseReservedDBInstancesOfferingResult":
        return dc_td.PurchaseReservedDBInstancesOfferingResult.make_one(res)

    def reboot_db_cluster(
        self,
        res: "bs_td.RebootDBClusterResultTypeDef",
    ) -> "dc_td.RebootDBClusterResult":
        return dc_td.RebootDBClusterResult.make_one(res)

    def reboot_db_instance(
        self,
        res: "bs_td.RebootDBInstanceResultTypeDef",
    ) -> "dc_td.RebootDBInstanceResult":
        return dc_td.RebootDBInstanceResult.make_one(res)

    def reboot_db_shard_group(
        self,
        res: "bs_td.DBShardGroupResponseTypeDef",
    ) -> "dc_td.DBShardGroupResponse":
        return dc_td.DBShardGroupResponse.make_one(res)

    def register_db_proxy_targets(
        self,
        res: "bs_td.RegisterDBProxyTargetsResponseTypeDef",
    ) -> "dc_td.RegisterDBProxyTargetsResponse":
        return dc_td.RegisterDBProxyTargetsResponse.make_one(res)

    def remove_from_global_cluster(
        self,
        res: "bs_td.RemoveFromGlobalClusterResultTypeDef",
    ) -> "dc_td.RemoveFromGlobalClusterResult":
        return dc_td.RemoveFromGlobalClusterResult.make_one(res)

    def remove_role_from_db_cluster(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def remove_role_from_db_instance(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def remove_source_identifier_from_subscription(
        self,
        res: "bs_td.RemoveSourceIdentifierFromSubscriptionResultTypeDef",
    ) -> "dc_td.RemoveSourceIdentifierFromSubscriptionResult":
        return dc_td.RemoveSourceIdentifierFromSubscriptionResult.make_one(res)

    def remove_tags_from_resource(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def reset_db_cluster_parameter_group(
        self,
        res: "bs_td.DBClusterParameterGroupNameMessageTypeDef",
    ) -> "dc_td.DBClusterParameterGroupNameMessage":
        return dc_td.DBClusterParameterGroupNameMessage.make_one(res)

    def reset_db_parameter_group(
        self,
        res: "bs_td.DBParameterGroupNameMessageTypeDef",
    ) -> "dc_td.DBParameterGroupNameMessage":
        return dc_td.DBParameterGroupNameMessage.make_one(res)

    def restore_db_cluster_from_s3(
        self,
        res: "bs_td.RestoreDBClusterFromS3ResultTypeDef",
    ) -> "dc_td.RestoreDBClusterFromS3Result":
        return dc_td.RestoreDBClusterFromS3Result.make_one(res)

    def restore_db_cluster_from_snapshot(
        self,
        res: "bs_td.RestoreDBClusterFromSnapshotResultTypeDef",
    ) -> "dc_td.RestoreDBClusterFromSnapshotResult":
        return dc_td.RestoreDBClusterFromSnapshotResult.make_one(res)

    def restore_db_cluster_to_point_in_time(
        self,
        res: "bs_td.RestoreDBClusterToPointInTimeResultTypeDef",
    ) -> "dc_td.RestoreDBClusterToPointInTimeResult":
        return dc_td.RestoreDBClusterToPointInTimeResult.make_one(res)

    def restore_db_instance_from_db_snapshot(
        self,
        res: "bs_td.RestoreDBInstanceFromDBSnapshotResultTypeDef",
    ) -> "dc_td.RestoreDBInstanceFromDBSnapshotResult":
        return dc_td.RestoreDBInstanceFromDBSnapshotResult.make_one(res)

    def restore_db_instance_from_s3(
        self,
        res: "bs_td.RestoreDBInstanceFromS3ResultTypeDef",
    ) -> "dc_td.RestoreDBInstanceFromS3Result":
        return dc_td.RestoreDBInstanceFromS3Result.make_one(res)

    def restore_db_instance_to_point_in_time(
        self,
        res: "bs_td.RestoreDBInstanceToPointInTimeResultTypeDef",
    ) -> "dc_td.RestoreDBInstanceToPointInTimeResult":
        return dc_td.RestoreDBInstanceToPointInTimeResult.make_one(res)

    def revoke_db_security_group_ingress(
        self,
        res: "bs_td.RevokeDBSecurityGroupIngressResultTypeDef",
    ) -> "dc_td.RevokeDBSecurityGroupIngressResult":
        return dc_td.RevokeDBSecurityGroupIngressResult.make_one(res)

    def start_activity_stream(
        self,
        res: "bs_td.StartActivityStreamResponseTypeDef",
    ) -> "dc_td.StartActivityStreamResponse":
        return dc_td.StartActivityStreamResponse.make_one(res)

    def start_db_cluster(
        self,
        res: "bs_td.StartDBClusterResultTypeDef",
    ) -> "dc_td.StartDBClusterResult":
        return dc_td.StartDBClusterResult.make_one(res)

    def start_db_instance(
        self,
        res: "bs_td.StartDBInstanceResultTypeDef",
    ) -> "dc_td.StartDBInstanceResult":
        return dc_td.StartDBInstanceResult.make_one(res)

    def start_db_instance_automated_backups_replication(
        self,
        res: "bs_td.StartDBInstanceAutomatedBackupsReplicationResultTypeDef",
    ) -> "dc_td.StartDBInstanceAutomatedBackupsReplicationResult":
        return dc_td.StartDBInstanceAutomatedBackupsReplicationResult.make_one(res)

    def start_export_task(
        self,
        res: "bs_td.ExportTaskResponseTypeDef",
    ) -> "dc_td.ExportTaskResponse":
        return dc_td.ExportTaskResponse.make_one(res)

    def stop_activity_stream(
        self,
        res: "bs_td.StopActivityStreamResponseTypeDef",
    ) -> "dc_td.StopActivityStreamResponse":
        return dc_td.StopActivityStreamResponse.make_one(res)

    def stop_db_cluster(
        self,
        res: "bs_td.StopDBClusterResultTypeDef",
    ) -> "dc_td.StopDBClusterResult":
        return dc_td.StopDBClusterResult.make_one(res)

    def stop_db_instance(
        self,
        res: "bs_td.StopDBInstanceResultTypeDef",
    ) -> "dc_td.StopDBInstanceResult":
        return dc_td.StopDBInstanceResult.make_one(res)

    def stop_db_instance_automated_backups_replication(
        self,
        res: "bs_td.StopDBInstanceAutomatedBackupsReplicationResultTypeDef",
    ) -> "dc_td.StopDBInstanceAutomatedBackupsReplicationResult":
        return dc_td.StopDBInstanceAutomatedBackupsReplicationResult.make_one(res)

    def switchover_blue_green_deployment(
        self,
        res: "bs_td.SwitchoverBlueGreenDeploymentResponseTypeDef",
    ) -> "dc_td.SwitchoverBlueGreenDeploymentResponse":
        return dc_td.SwitchoverBlueGreenDeploymentResponse.make_one(res)

    def switchover_global_cluster(
        self,
        res: "bs_td.SwitchoverGlobalClusterResultTypeDef",
    ) -> "dc_td.SwitchoverGlobalClusterResult":
        return dc_td.SwitchoverGlobalClusterResult.make_one(res)

    def switchover_read_replica(
        self,
        res: "bs_td.SwitchoverReadReplicaResultTypeDef",
    ) -> "dc_td.SwitchoverReadReplicaResult":
        return dc_td.SwitchoverReadReplicaResult.make_one(res)


rds_caster = RDSCaster()
