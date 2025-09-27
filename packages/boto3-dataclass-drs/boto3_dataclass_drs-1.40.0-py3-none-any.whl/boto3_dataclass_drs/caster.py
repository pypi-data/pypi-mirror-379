# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_drs import type_defs as bs_td


class DRSCaster:

    def associate_source_network_stack(
        self,
        res: "bs_td.AssociateSourceNetworkStackResponseTypeDef",
    ) -> "dc_td.AssociateSourceNetworkStackResponse":
        return dc_td.AssociateSourceNetworkStackResponse.make_one(res)

    def create_extended_source_server(
        self,
        res: "bs_td.CreateExtendedSourceServerResponseTypeDef",
    ) -> "dc_td.CreateExtendedSourceServerResponse":
        return dc_td.CreateExtendedSourceServerResponse.make_one(res)

    def create_launch_configuration_template(
        self,
        res: "bs_td.CreateLaunchConfigurationTemplateResponseTypeDef",
    ) -> "dc_td.CreateLaunchConfigurationTemplateResponse":
        return dc_td.CreateLaunchConfigurationTemplateResponse.make_one(res)

    def create_replication_configuration_template(
        self,
        res: "bs_td.ReplicationConfigurationTemplateResponseTypeDef",
    ) -> "dc_td.ReplicationConfigurationTemplateResponse":
        return dc_td.ReplicationConfigurationTemplateResponse.make_one(res)

    def create_source_network(
        self,
        res: "bs_td.CreateSourceNetworkResponseTypeDef",
    ) -> "dc_td.CreateSourceNetworkResponse":
        return dc_td.CreateSourceNetworkResponse.make_one(res)

    def delete_recovery_instance(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def describe_job_log_items(
        self,
        res: "bs_td.DescribeJobLogItemsResponseTypeDef",
    ) -> "dc_td.DescribeJobLogItemsResponse":
        return dc_td.DescribeJobLogItemsResponse.make_one(res)

    def describe_jobs(
        self,
        res: "bs_td.DescribeJobsResponseTypeDef",
    ) -> "dc_td.DescribeJobsResponse":
        return dc_td.DescribeJobsResponse.make_one(res)

    def describe_launch_configuration_templates(
        self,
        res: "bs_td.DescribeLaunchConfigurationTemplatesResponseTypeDef",
    ) -> "dc_td.DescribeLaunchConfigurationTemplatesResponse":
        return dc_td.DescribeLaunchConfigurationTemplatesResponse.make_one(res)

    def describe_recovery_instances(
        self,
        res: "bs_td.DescribeRecoveryInstancesResponseTypeDef",
    ) -> "dc_td.DescribeRecoveryInstancesResponse":
        return dc_td.DescribeRecoveryInstancesResponse.make_one(res)

    def describe_recovery_snapshots(
        self,
        res: "bs_td.DescribeRecoverySnapshotsResponseTypeDef",
    ) -> "dc_td.DescribeRecoverySnapshotsResponse":
        return dc_td.DescribeRecoverySnapshotsResponse.make_one(res)

    def describe_replication_configuration_templates(
        self,
        res: "bs_td.DescribeReplicationConfigurationTemplatesResponseTypeDef",
    ) -> "dc_td.DescribeReplicationConfigurationTemplatesResponse":
        return dc_td.DescribeReplicationConfigurationTemplatesResponse.make_one(res)

    def describe_source_networks(
        self,
        res: "bs_td.DescribeSourceNetworksResponseTypeDef",
    ) -> "dc_td.DescribeSourceNetworksResponse":
        return dc_td.DescribeSourceNetworksResponse.make_one(res)

    def describe_source_servers(
        self,
        res: "bs_td.DescribeSourceServersResponseTypeDef",
    ) -> "dc_td.DescribeSourceServersResponse":
        return dc_td.DescribeSourceServersResponse.make_one(res)

    def disconnect_recovery_instance(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def disconnect_source_server(
        self,
        res: "bs_td.SourceServerResponseTypeDef",
    ) -> "dc_td.SourceServerResponse":
        return dc_td.SourceServerResponse.make_one(res)

    def export_source_network_cfn_template(
        self,
        res: "bs_td.ExportSourceNetworkCfnTemplateResponseTypeDef",
    ) -> "dc_td.ExportSourceNetworkCfnTemplateResponse":
        return dc_td.ExportSourceNetworkCfnTemplateResponse.make_one(res)

    def get_failback_replication_configuration(
        self,
        res: "bs_td.GetFailbackReplicationConfigurationResponseTypeDef",
    ) -> "dc_td.GetFailbackReplicationConfigurationResponse":
        return dc_td.GetFailbackReplicationConfigurationResponse.make_one(res)

    def get_launch_configuration(
        self,
        res: "bs_td.LaunchConfigurationTypeDef",
    ) -> "dc_td.LaunchConfiguration":
        return dc_td.LaunchConfiguration.make_one(res)

    def get_replication_configuration(
        self,
        res: "bs_td.ReplicationConfigurationTypeDef",
    ) -> "dc_td.ReplicationConfiguration":
        return dc_td.ReplicationConfiguration.make_one(res)

    def list_extensible_source_servers(
        self,
        res: "bs_td.ListExtensibleSourceServersResponseTypeDef",
    ) -> "dc_td.ListExtensibleSourceServersResponse":
        return dc_td.ListExtensibleSourceServersResponse.make_one(res)

    def list_launch_actions(
        self,
        res: "bs_td.ListLaunchActionsResponseTypeDef",
    ) -> "dc_td.ListLaunchActionsResponse":
        return dc_td.ListLaunchActionsResponse.make_one(res)

    def list_staging_accounts(
        self,
        res: "bs_td.ListStagingAccountsResponseTypeDef",
    ) -> "dc_td.ListStagingAccountsResponse":
        return dc_td.ListStagingAccountsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def put_launch_action(
        self,
        res: "bs_td.PutLaunchActionResponseTypeDef",
    ) -> "dc_td.PutLaunchActionResponse":
        return dc_td.PutLaunchActionResponse.make_one(res)

    def retry_data_replication(
        self,
        res: "bs_td.SourceServerResponseTypeDef",
    ) -> "dc_td.SourceServerResponse":
        return dc_td.SourceServerResponse.make_one(res)

    def reverse_replication(
        self,
        res: "bs_td.ReverseReplicationResponseTypeDef",
    ) -> "dc_td.ReverseReplicationResponse":
        return dc_td.ReverseReplicationResponse.make_one(res)

    def start_failback_launch(
        self,
        res: "bs_td.StartFailbackLaunchResponseTypeDef",
    ) -> "dc_td.StartFailbackLaunchResponse":
        return dc_td.StartFailbackLaunchResponse.make_one(res)

    def start_recovery(
        self,
        res: "bs_td.StartRecoveryResponseTypeDef",
    ) -> "dc_td.StartRecoveryResponse":
        return dc_td.StartRecoveryResponse.make_one(res)

    def start_replication(
        self,
        res: "bs_td.StartReplicationResponseTypeDef",
    ) -> "dc_td.StartReplicationResponse":
        return dc_td.StartReplicationResponse.make_one(res)

    def start_source_network_recovery(
        self,
        res: "bs_td.StartSourceNetworkRecoveryResponseTypeDef",
    ) -> "dc_td.StartSourceNetworkRecoveryResponse":
        return dc_td.StartSourceNetworkRecoveryResponse.make_one(res)

    def start_source_network_replication(
        self,
        res: "bs_td.StartSourceNetworkReplicationResponseTypeDef",
    ) -> "dc_td.StartSourceNetworkReplicationResponse":
        return dc_td.StartSourceNetworkReplicationResponse.make_one(res)

    def stop_failback(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def stop_replication(
        self,
        res: "bs_td.StopReplicationResponseTypeDef",
    ) -> "dc_td.StopReplicationResponse":
        return dc_td.StopReplicationResponse.make_one(res)

    def stop_source_network_replication(
        self,
        res: "bs_td.StopSourceNetworkReplicationResponseTypeDef",
    ) -> "dc_td.StopSourceNetworkReplicationResponse":
        return dc_td.StopSourceNetworkReplicationResponse.make_one(res)

    def tag_resource(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def terminate_recovery_instances(
        self,
        res: "bs_td.TerminateRecoveryInstancesResponseTypeDef",
    ) -> "dc_td.TerminateRecoveryInstancesResponse":
        return dc_td.TerminateRecoveryInstancesResponse.make_one(res)

    def untag_resource(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_failback_replication_configuration(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_launch_configuration(
        self,
        res: "bs_td.LaunchConfigurationTypeDef",
    ) -> "dc_td.LaunchConfiguration":
        return dc_td.LaunchConfiguration.make_one(res)

    def update_launch_configuration_template(
        self,
        res: "bs_td.UpdateLaunchConfigurationTemplateResponseTypeDef",
    ) -> "dc_td.UpdateLaunchConfigurationTemplateResponse":
        return dc_td.UpdateLaunchConfigurationTemplateResponse.make_one(res)

    def update_replication_configuration(
        self,
        res: "bs_td.ReplicationConfigurationTypeDef",
    ) -> "dc_td.ReplicationConfiguration":
        return dc_td.ReplicationConfiguration.make_one(res)

    def update_replication_configuration_template(
        self,
        res: "bs_td.ReplicationConfigurationTemplateResponseTypeDef",
    ) -> "dc_td.ReplicationConfigurationTemplateResponse":
        return dc_td.ReplicationConfigurationTemplateResponse.make_one(res)


drs_caster = DRSCaster()
