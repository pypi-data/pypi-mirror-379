# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_redshift import type_defs as bs_td


class REDSHIFTCaster:

    def accept_reserved_node_exchange(
        self,
        res: "bs_td.AcceptReservedNodeExchangeOutputMessageTypeDef",
    ) -> "dc_td.AcceptReservedNodeExchangeOutputMessage":
        return dc_td.AcceptReservedNodeExchangeOutputMessage.make_one(res)

    def add_partner(
        self,
        res: "bs_td.PartnerIntegrationOutputMessageTypeDef",
    ) -> "dc_td.PartnerIntegrationOutputMessage":
        return dc_td.PartnerIntegrationOutputMessage.make_one(res)

    def associate_data_share_consumer(
        self,
        res: "bs_td.DataShareResponseTypeDef",
    ) -> "dc_td.DataShareResponse":
        return dc_td.DataShareResponse.make_one(res)

    def authorize_cluster_security_group_ingress(
        self,
        res: "bs_td.AuthorizeClusterSecurityGroupIngressResultTypeDef",
    ) -> "dc_td.AuthorizeClusterSecurityGroupIngressResult":
        return dc_td.AuthorizeClusterSecurityGroupIngressResult.make_one(res)

    def authorize_data_share(
        self,
        res: "bs_td.DataShareResponseTypeDef",
    ) -> "dc_td.DataShareResponse":
        return dc_td.DataShareResponse.make_one(res)

    def authorize_endpoint_access(
        self,
        res: "bs_td.EndpointAuthorizationResponseTypeDef",
    ) -> "dc_td.EndpointAuthorizationResponse":
        return dc_td.EndpointAuthorizationResponse.make_one(res)

    def authorize_snapshot_access(
        self,
        res: "bs_td.AuthorizeSnapshotAccessResultTypeDef",
    ) -> "dc_td.AuthorizeSnapshotAccessResult":
        return dc_td.AuthorizeSnapshotAccessResult.make_one(res)

    def batch_delete_cluster_snapshots(
        self,
        res: "bs_td.BatchDeleteClusterSnapshotsResultTypeDef",
    ) -> "dc_td.BatchDeleteClusterSnapshotsResult":
        return dc_td.BatchDeleteClusterSnapshotsResult.make_one(res)

    def batch_modify_cluster_snapshots(
        self,
        res: "bs_td.BatchModifyClusterSnapshotsOutputMessageTypeDef",
    ) -> "dc_td.BatchModifyClusterSnapshotsOutputMessage":
        return dc_td.BatchModifyClusterSnapshotsOutputMessage.make_one(res)

    def cancel_resize(
        self,
        res: "bs_td.ResizeProgressMessageTypeDef",
    ) -> "dc_td.ResizeProgressMessage":
        return dc_td.ResizeProgressMessage.make_one(res)

    def copy_cluster_snapshot(
        self,
        res: "bs_td.CopyClusterSnapshotResultTypeDef",
    ) -> "dc_td.CopyClusterSnapshotResult":
        return dc_td.CopyClusterSnapshotResult.make_one(res)

    def create_authentication_profile(
        self,
        res: "bs_td.CreateAuthenticationProfileResultTypeDef",
    ) -> "dc_td.CreateAuthenticationProfileResult":
        return dc_td.CreateAuthenticationProfileResult.make_one(res)

    def create_cluster(
        self,
        res: "bs_td.CreateClusterResultTypeDef",
    ) -> "dc_td.CreateClusterResult":
        return dc_td.CreateClusterResult.make_one(res)

    def create_cluster_parameter_group(
        self,
        res: "bs_td.CreateClusterParameterGroupResultTypeDef",
    ) -> "dc_td.CreateClusterParameterGroupResult":
        return dc_td.CreateClusterParameterGroupResult.make_one(res)

    def create_cluster_security_group(
        self,
        res: "bs_td.CreateClusterSecurityGroupResultTypeDef",
    ) -> "dc_td.CreateClusterSecurityGroupResult":
        return dc_td.CreateClusterSecurityGroupResult.make_one(res)

    def create_cluster_snapshot(
        self,
        res: "bs_td.CreateClusterSnapshotResultTypeDef",
    ) -> "dc_td.CreateClusterSnapshotResult":
        return dc_td.CreateClusterSnapshotResult.make_one(res)

    def create_cluster_subnet_group(
        self,
        res: "bs_td.CreateClusterSubnetGroupResultTypeDef",
    ) -> "dc_td.CreateClusterSubnetGroupResult":
        return dc_td.CreateClusterSubnetGroupResult.make_one(res)

    def create_custom_domain_association(
        self,
        res: "bs_td.CreateCustomDomainAssociationResultTypeDef",
    ) -> "dc_td.CreateCustomDomainAssociationResult":
        return dc_td.CreateCustomDomainAssociationResult.make_one(res)

    def create_endpoint_access(
        self,
        res: "bs_td.EndpointAccessResponseTypeDef",
    ) -> "dc_td.EndpointAccessResponse":
        return dc_td.EndpointAccessResponse.make_one(res)

    def create_event_subscription(
        self,
        res: "bs_td.CreateEventSubscriptionResultTypeDef",
    ) -> "dc_td.CreateEventSubscriptionResult":
        return dc_td.CreateEventSubscriptionResult.make_one(res)

    def create_hsm_client_certificate(
        self,
        res: "bs_td.CreateHsmClientCertificateResultTypeDef",
    ) -> "dc_td.CreateHsmClientCertificateResult":
        return dc_td.CreateHsmClientCertificateResult.make_one(res)

    def create_hsm_configuration(
        self,
        res: "bs_td.CreateHsmConfigurationResultTypeDef",
    ) -> "dc_td.CreateHsmConfigurationResult":
        return dc_td.CreateHsmConfigurationResult.make_one(res)

    def create_integration(
        self,
        res: "bs_td.IntegrationResponseTypeDef",
    ) -> "dc_td.IntegrationResponse":
        return dc_td.IntegrationResponse.make_one(res)

    def create_redshift_idc_application(
        self,
        res: "bs_td.CreateRedshiftIdcApplicationResultTypeDef",
    ) -> "dc_td.CreateRedshiftIdcApplicationResult":
        return dc_td.CreateRedshiftIdcApplicationResult.make_one(res)

    def create_scheduled_action(
        self,
        res: "bs_td.ScheduledActionResponseTypeDef",
    ) -> "dc_td.ScheduledActionResponse":
        return dc_td.ScheduledActionResponse.make_one(res)

    def create_snapshot_copy_grant(
        self,
        res: "bs_td.CreateSnapshotCopyGrantResultTypeDef",
    ) -> "dc_td.CreateSnapshotCopyGrantResult":
        return dc_td.CreateSnapshotCopyGrantResult.make_one(res)

    def create_snapshot_schedule(
        self,
        res: "bs_td.SnapshotScheduleResponseTypeDef",
    ) -> "dc_td.SnapshotScheduleResponse":
        return dc_td.SnapshotScheduleResponse.make_one(res)

    def create_tags(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def create_usage_limit(
        self,
        res: "bs_td.UsageLimitResponseTypeDef",
    ) -> "dc_td.UsageLimitResponse":
        return dc_td.UsageLimitResponse.make_one(res)

    def deauthorize_data_share(
        self,
        res: "bs_td.DataShareResponseTypeDef",
    ) -> "dc_td.DataShareResponse":
        return dc_td.DataShareResponse.make_one(res)

    def delete_authentication_profile(
        self,
        res: "bs_td.DeleteAuthenticationProfileResultTypeDef",
    ) -> "dc_td.DeleteAuthenticationProfileResult":
        return dc_td.DeleteAuthenticationProfileResult.make_one(res)

    def delete_cluster(
        self,
        res: "bs_td.DeleteClusterResultTypeDef",
    ) -> "dc_td.DeleteClusterResult":
        return dc_td.DeleteClusterResult.make_one(res)

    def delete_cluster_parameter_group(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_cluster_security_group(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_cluster_snapshot(
        self,
        res: "bs_td.DeleteClusterSnapshotResultTypeDef",
    ) -> "dc_td.DeleteClusterSnapshotResult":
        return dc_td.DeleteClusterSnapshotResult.make_one(res)

    def delete_cluster_subnet_group(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_custom_domain_association(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_endpoint_access(
        self,
        res: "bs_td.EndpointAccessResponseTypeDef",
    ) -> "dc_td.EndpointAccessResponse":
        return dc_td.EndpointAccessResponse.make_one(res)

    def delete_event_subscription(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_hsm_client_certificate(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_hsm_configuration(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_integration(
        self,
        res: "bs_td.IntegrationResponseTypeDef",
    ) -> "dc_td.IntegrationResponse":
        return dc_td.IntegrationResponse.make_one(res)

    def delete_partner(
        self,
        res: "bs_td.PartnerIntegrationOutputMessageTypeDef",
    ) -> "dc_td.PartnerIntegrationOutputMessage":
        return dc_td.PartnerIntegrationOutputMessage.make_one(res)

    def delete_redshift_idc_application(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_resource_policy(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_scheduled_action(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_snapshot_copy_grant(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_snapshot_schedule(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_tags(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_usage_limit(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def deregister_namespace(
        self,
        res: "bs_td.DeregisterNamespaceOutputMessageTypeDef",
    ) -> "dc_td.DeregisterNamespaceOutputMessage":
        return dc_td.DeregisterNamespaceOutputMessage.make_one(res)

    def describe_account_attributes(
        self,
        res: "bs_td.AccountAttributeListTypeDef",
    ) -> "dc_td.AccountAttributeList":
        return dc_td.AccountAttributeList.make_one(res)

    def describe_authentication_profiles(
        self,
        res: "bs_td.DescribeAuthenticationProfilesResultTypeDef",
    ) -> "dc_td.DescribeAuthenticationProfilesResult":
        return dc_td.DescribeAuthenticationProfilesResult.make_one(res)

    def describe_cluster_db_revisions(
        self,
        res: "bs_td.ClusterDbRevisionsMessageTypeDef",
    ) -> "dc_td.ClusterDbRevisionsMessage":
        return dc_td.ClusterDbRevisionsMessage.make_one(res)

    def describe_cluster_parameter_groups(
        self,
        res: "bs_td.ClusterParameterGroupsMessageTypeDef",
    ) -> "dc_td.ClusterParameterGroupsMessage":
        return dc_td.ClusterParameterGroupsMessage.make_one(res)

    def describe_cluster_parameters(
        self,
        res: "bs_td.ClusterParameterGroupDetailsTypeDef",
    ) -> "dc_td.ClusterParameterGroupDetails":
        return dc_td.ClusterParameterGroupDetails.make_one(res)

    def describe_cluster_security_groups(
        self,
        res: "bs_td.ClusterSecurityGroupMessageTypeDef",
    ) -> "dc_td.ClusterSecurityGroupMessage":
        return dc_td.ClusterSecurityGroupMessage.make_one(res)

    def describe_cluster_snapshots(
        self,
        res: "bs_td.SnapshotMessageTypeDef",
    ) -> "dc_td.SnapshotMessage":
        return dc_td.SnapshotMessage.make_one(res)

    def describe_cluster_subnet_groups(
        self,
        res: "bs_td.ClusterSubnetGroupMessageTypeDef",
    ) -> "dc_td.ClusterSubnetGroupMessage":
        return dc_td.ClusterSubnetGroupMessage.make_one(res)

    def describe_cluster_tracks(
        self,
        res: "bs_td.TrackListMessageTypeDef",
    ) -> "dc_td.TrackListMessage":
        return dc_td.TrackListMessage.make_one(res)

    def describe_cluster_versions(
        self,
        res: "bs_td.ClusterVersionsMessageTypeDef",
    ) -> "dc_td.ClusterVersionsMessage":
        return dc_td.ClusterVersionsMessage.make_one(res)

    def describe_clusters(
        self,
        res: "bs_td.ClustersMessageTypeDef",
    ) -> "dc_td.ClustersMessage":
        return dc_td.ClustersMessage.make_one(res)

    def describe_custom_domain_associations(
        self,
        res: "bs_td.CustomDomainAssociationsMessageTypeDef",
    ) -> "dc_td.CustomDomainAssociationsMessage":
        return dc_td.CustomDomainAssociationsMessage.make_one(res)

    def describe_data_shares(
        self,
        res: "bs_td.DescribeDataSharesResultTypeDef",
    ) -> "dc_td.DescribeDataSharesResult":
        return dc_td.DescribeDataSharesResult.make_one(res)

    def describe_data_shares_for_consumer(
        self,
        res: "bs_td.DescribeDataSharesForConsumerResultTypeDef",
    ) -> "dc_td.DescribeDataSharesForConsumerResult":
        return dc_td.DescribeDataSharesForConsumerResult.make_one(res)

    def describe_data_shares_for_producer(
        self,
        res: "bs_td.DescribeDataSharesForProducerResultTypeDef",
    ) -> "dc_td.DescribeDataSharesForProducerResult":
        return dc_td.DescribeDataSharesForProducerResult.make_one(res)

    def describe_default_cluster_parameters(
        self,
        res: "bs_td.DescribeDefaultClusterParametersResultTypeDef",
    ) -> "dc_td.DescribeDefaultClusterParametersResult":
        return dc_td.DescribeDefaultClusterParametersResult.make_one(res)

    def describe_endpoint_access(
        self,
        res: "bs_td.EndpointAccessListTypeDef",
    ) -> "dc_td.EndpointAccessList":
        return dc_td.EndpointAccessList.make_one(res)

    def describe_endpoint_authorization(
        self,
        res: "bs_td.EndpointAuthorizationListTypeDef",
    ) -> "dc_td.EndpointAuthorizationList":
        return dc_td.EndpointAuthorizationList.make_one(res)

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

    def describe_hsm_client_certificates(
        self,
        res: "bs_td.HsmClientCertificateMessageTypeDef",
    ) -> "dc_td.HsmClientCertificateMessage":
        return dc_td.HsmClientCertificateMessage.make_one(res)

    def describe_hsm_configurations(
        self,
        res: "bs_td.HsmConfigurationMessageTypeDef",
    ) -> "dc_td.HsmConfigurationMessage":
        return dc_td.HsmConfigurationMessage.make_one(res)

    def describe_inbound_integrations(
        self,
        res: "bs_td.InboundIntegrationsMessageTypeDef",
    ) -> "dc_td.InboundIntegrationsMessage":
        return dc_td.InboundIntegrationsMessage.make_one(res)

    def describe_integrations(
        self,
        res: "bs_td.IntegrationsMessageTypeDef",
    ) -> "dc_td.IntegrationsMessage":
        return dc_td.IntegrationsMessage.make_one(res)

    def describe_logging_status(
        self,
        res: "bs_td.LoggingStatusTypeDef",
    ) -> "dc_td.LoggingStatus":
        return dc_td.LoggingStatus.make_one(res)

    def describe_node_configuration_options(
        self,
        res: "bs_td.NodeConfigurationOptionsMessageTypeDef",
    ) -> "dc_td.NodeConfigurationOptionsMessage":
        return dc_td.NodeConfigurationOptionsMessage.make_one(res)

    def describe_orderable_cluster_options(
        self,
        res: "bs_td.OrderableClusterOptionsMessageTypeDef",
    ) -> "dc_td.OrderableClusterOptionsMessage":
        return dc_td.OrderableClusterOptionsMessage.make_one(res)

    def describe_partners(
        self,
        res: "bs_td.DescribePartnersOutputMessageTypeDef",
    ) -> "dc_td.DescribePartnersOutputMessage":
        return dc_td.DescribePartnersOutputMessage.make_one(res)

    def describe_redshift_idc_applications(
        self,
        res: "bs_td.DescribeRedshiftIdcApplicationsResultTypeDef",
    ) -> "dc_td.DescribeRedshiftIdcApplicationsResult":
        return dc_td.DescribeRedshiftIdcApplicationsResult.make_one(res)

    def describe_reserved_node_exchange_status(
        self,
        res: "bs_td.DescribeReservedNodeExchangeStatusOutputMessageTypeDef",
    ) -> "dc_td.DescribeReservedNodeExchangeStatusOutputMessage":
        return dc_td.DescribeReservedNodeExchangeStatusOutputMessage.make_one(res)

    def describe_reserved_node_offerings(
        self,
        res: "bs_td.ReservedNodeOfferingsMessageTypeDef",
    ) -> "dc_td.ReservedNodeOfferingsMessage":
        return dc_td.ReservedNodeOfferingsMessage.make_one(res)

    def describe_reserved_nodes(
        self,
        res: "bs_td.ReservedNodesMessageTypeDef",
    ) -> "dc_td.ReservedNodesMessage":
        return dc_td.ReservedNodesMessage.make_one(res)

    def describe_resize(
        self,
        res: "bs_td.ResizeProgressMessageTypeDef",
    ) -> "dc_td.ResizeProgressMessage":
        return dc_td.ResizeProgressMessage.make_one(res)

    def describe_scheduled_actions(
        self,
        res: "bs_td.ScheduledActionsMessageTypeDef",
    ) -> "dc_td.ScheduledActionsMessage":
        return dc_td.ScheduledActionsMessage.make_one(res)

    def describe_snapshot_copy_grants(
        self,
        res: "bs_td.SnapshotCopyGrantMessageTypeDef",
    ) -> "dc_td.SnapshotCopyGrantMessage":
        return dc_td.SnapshotCopyGrantMessage.make_one(res)

    def describe_snapshot_schedules(
        self,
        res: "bs_td.DescribeSnapshotSchedulesOutputMessageTypeDef",
    ) -> "dc_td.DescribeSnapshotSchedulesOutputMessage":
        return dc_td.DescribeSnapshotSchedulesOutputMessage.make_one(res)

    def describe_storage(
        self,
        res: "bs_td.CustomerStorageMessageTypeDef",
    ) -> "dc_td.CustomerStorageMessage":
        return dc_td.CustomerStorageMessage.make_one(res)

    def describe_table_restore_status(
        self,
        res: "bs_td.TableRestoreStatusMessageTypeDef",
    ) -> "dc_td.TableRestoreStatusMessage":
        return dc_td.TableRestoreStatusMessage.make_one(res)

    def describe_tags(
        self,
        res: "bs_td.TaggedResourceListMessageTypeDef",
    ) -> "dc_td.TaggedResourceListMessage":
        return dc_td.TaggedResourceListMessage.make_one(res)

    def describe_usage_limits(
        self,
        res: "bs_td.UsageLimitListTypeDef",
    ) -> "dc_td.UsageLimitList":
        return dc_td.UsageLimitList.make_one(res)

    def disable_logging(
        self,
        res: "bs_td.LoggingStatusTypeDef",
    ) -> "dc_td.LoggingStatus":
        return dc_td.LoggingStatus.make_one(res)

    def disable_snapshot_copy(
        self,
        res: "bs_td.DisableSnapshotCopyResultTypeDef",
    ) -> "dc_td.DisableSnapshotCopyResult":
        return dc_td.DisableSnapshotCopyResult.make_one(res)

    def disassociate_data_share_consumer(
        self,
        res: "bs_td.DataShareResponseTypeDef",
    ) -> "dc_td.DataShareResponse":
        return dc_td.DataShareResponse.make_one(res)

    def enable_logging(
        self,
        res: "bs_td.LoggingStatusTypeDef",
    ) -> "dc_td.LoggingStatus":
        return dc_td.LoggingStatus.make_one(res)

    def enable_snapshot_copy(
        self,
        res: "bs_td.EnableSnapshotCopyResultTypeDef",
    ) -> "dc_td.EnableSnapshotCopyResult":
        return dc_td.EnableSnapshotCopyResult.make_one(res)

    def failover_primary_compute(
        self,
        res: "bs_td.FailoverPrimaryComputeResultTypeDef",
    ) -> "dc_td.FailoverPrimaryComputeResult":
        return dc_td.FailoverPrimaryComputeResult.make_one(res)

    def get_cluster_credentials(
        self,
        res: "bs_td.ClusterCredentialsTypeDef",
    ) -> "dc_td.ClusterCredentials":
        return dc_td.ClusterCredentials.make_one(res)

    def get_cluster_credentials_with_iam(
        self,
        res: "bs_td.ClusterExtendedCredentialsTypeDef",
    ) -> "dc_td.ClusterExtendedCredentials":
        return dc_td.ClusterExtendedCredentials.make_one(res)

    def get_reserved_node_exchange_configuration_options(
        self,
        res: "bs_td.GetReservedNodeExchangeConfigurationOptionsOutputMessageTypeDef",
    ) -> "dc_td.GetReservedNodeExchangeConfigurationOptionsOutputMessage":
        return dc_td.GetReservedNodeExchangeConfigurationOptionsOutputMessage.make_one(
            res
        )

    def get_reserved_node_exchange_offerings(
        self,
        res: "bs_td.GetReservedNodeExchangeOfferingsOutputMessageTypeDef",
    ) -> "dc_td.GetReservedNodeExchangeOfferingsOutputMessage":
        return dc_td.GetReservedNodeExchangeOfferingsOutputMessage.make_one(res)

    def get_resource_policy(
        self,
        res: "bs_td.GetResourcePolicyResultTypeDef",
    ) -> "dc_td.GetResourcePolicyResult":
        return dc_td.GetResourcePolicyResult.make_one(res)

    def list_recommendations(
        self,
        res: "bs_td.ListRecommendationsResultTypeDef",
    ) -> "dc_td.ListRecommendationsResult":
        return dc_td.ListRecommendationsResult.make_one(res)

    def modify_aqua_configuration(
        self,
        res: "bs_td.ModifyAquaOutputMessageTypeDef",
    ) -> "dc_td.ModifyAquaOutputMessage":
        return dc_td.ModifyAquaOutputMessage.make_one(res)

    def modify_authentication_profile(
        self,
        res: "bs_td.ModifyAuthenticationProfileResultTypeDef",
    ) -> "dc_td.ModifyAuthenticationProfileResult":
        return dc_td.ModifyAuthenticationProfileResult.make_one(res)

    def modify_cluster(
        self,
        res: "bs_td.ModifyClusterResultTypeDef",
    ) -> "dc_td.ModifyClusterResult":
        return dc_td.ModifyClusterResult.make_one(res)

    def modify_cluster_db_revision(
        self,
        res: "bs_td.ModifyClusterDbRevisionResultTypeDef",
    ) -> "dc_td.ModifyClusterDbRevisionResult":
        return dc_td.ModifyClusterDbRevisionResult.make_one(res)

    def modify_cluster_iam_roles(
        self,
        res: "bs_td.ModifyClusterIamRolesResultTypeDef",
    ) -> "dc_td.ModifyClusterIamRolesResult":
        return dc_td.ModifyClusterIamRolesResult.make_one(res)

    def modify_cluster_maintenance(
        self,
        res: "bs_td.ModifyClusterMaintenanceResultTypeDef",
    ) -> "dc_td.ModifyClusterMaintenanceResult":
        return dc_td.ModifyClusterMaintenanceResult.make_one(res)

    def modify_cluster_parameter_group(
        self,
        res: "bs_td.ClusterParameterGroupNameMessageTypeDef",
    ) -> "dc_td.ClusterParameterGroupNameMessage":
        return dc_td.ClusterParameterGroupNameMessage.make_one(res)

    def modify_cluster_snapshot(
        self,
        res: "bs_td.ModifyClusterSnapshotResultTypeDef",
    ) -> "dc_td.ModifyClusterSnapshotResult":
        return dc_td.ModifyClusterSnapshotResult.make_one(res)

    def modify_cluster_snapshot_schedule(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def modify_cluster_subnet_group(
        self,
        res: "bs_td.ModifyClusterSubnetGroupResultTypeDef",
    ) -> "dc_td.ModifyClusterSubnetGroupResult":
        return dc_td.ModifyClusterSubnetGroupResult.make_one(res)

    def modify_custom_domain_association(
        self,
        res: "bs_td.ModifyCustomDomainAssociationResultTypeDef",
    ) -> "dc_td.ModifyCustomDomainAssociationResult":
        return dc_td.ModifyCustomDomainAssociationResult.make_one(res)

    def modify_endpoint_access(
        self,
        res: "bs_td.EndpointAccessResponseTypeDef",
    ) -> "dc_td.EndpointAccessResponse":
        return dc_td.EndpointAccessResponse.make_one(res)

    def modify_event_subscription(
        self,
        res: "bs_td.ModifyEventSubscriptionResultTypeDef",
    ) -> "dc_td.ModifyEventSubscriptionResult":
        return dc_td.ModifyEventSubscriptionResult.make_one(res)

    def modify_integration(
        self,
        res: "bs_td.IntegrationResponseTypeDef",
    ) -> "dc_td.IntegrationResponse":
        return dc_td.IntegrationResponse.make_one(res)

    def modify_redshift_idc_application(
        self,
        res: "bs_td.ModifyRedshiftIdcApplicationResultTypeDef",
    ) -> "dc_td.ModifyRedshiftIdcApplicationResult":
        return dc_td.ModifyRedshiftIdcApplicationResult.make_one(res)

    def modify_scheduled_action(
        self,
        res: "bs_td.ScheduledActionResponseTypeDef",
    ) -> "dc_td.ScheduledActionResponse":
        return dc_td.ScheduledActionResponse.make_one(res)

    def modify_snapshot_copy_retention_period(
        self,
        res: "bs_td.ModifySnapshotCopyRetentionPeriodResultTypeDef",
    ) -> "dc_td.ModifySnapshotCopyRetentionPeriodResult":
        return dc_td.ModifySnapshotCopyRetentionPeriodResult.make_one(res)

    def modify_snapshot_schedule(
        self,
        res: "bs_td.SnapshotScheduleResponseTypeDef",
    ) -> "dc_td.SnapshotScheduleResponse":
        return dc_td.SnapshotScheduleResponse.make_one(res)

    def modify_usage_limit(
        self,
        res: "bs_td.UsageLimitResponseTypeDef",
    ) -> "dc_td.UsageLimitResponse":
        return dc_td.UsageLimitResponse.make_one(res)

    def pause_cluster(
        self,
        res: "bs_td.PauseClusterResultTypeDef",
    ) -> "dc_td.PauseClusterResult":
        return dc_td.PauseClusterResult.make_one(res)

    def purchase_reserved_node_offering(
        self,
        res: "bs_td.PurchaseReservedNodeOfferingResultTypeDef",
    ) -> "dc_td.PurchaseReservedNodeOfferingResult":
        return dc_td.PurchaseReservedNodeOfferingResult.make_one(res)

    def put_resource_policy(
        self,
        res: "bs_td.PutResourcePolicyResultTypeDef",
    ) -> "dc_td.PutResourcePolicyResult":
        return dc_td.PutResourcePolicyResult.make_one(res)

    def reboot_cluster(
        self,
        res: "bs_td.RebootClusterResultTypeDef",
    ) -> "dc_td.RebootClusterResult":
        return dc_td.RebootClusterResult.make_one(res)

    def register_namespace(
        self,
        res: "bs_td.RegisterNamespaceOutputMessageTypeDef",
    ) -> "dc_td.RegisterNamespaceOutputMessage":
        return dc_td.RegisterNamespaceOutputMessage.make_one(res)

    def reject_data_share(
        self,
        res: "bs_td.DataShareResponseTypeDef",
    ) -> "dc_td.DataShareResponse":
        return dc_td.DataShareResponse.make_one(res)

    def reset_cluster_parameter_group(
        self,
        res: "bs_td.ClusterParameterGroupNameMessageTypeDef",
    ) -> "dc_td.ClusterParameterGroupNameMessage":
        return dc_td.ClusterParameterGroupNameMessage.make_one(res)

    def resize_cluster(
        self,
        res: "bs_td.ResizeClusterResultTypeDef",
    ) -> "dc_td.ResizeClusterResult":
        return dc_td.ResizeClusterResult.make_one(res)

    def restore_from_cluster_snapshot(
        self,
        res: "bs_td.RestoreFromClusterSnapshotResultTypeDef",
    ) -> "dc_td.RestoreFromClusterSnapshotResult":
        return dc_td.RestoreFromClusterSnapshotResult.make_one(res)

    def restore_table_from_cluster_snapshot(
        self,
        res: "bs_td.RestoreTableFromClusterSnapshotResultTypeDef",
    ) -> "dc_td.RestoreTableFromClusterSnapshotResult":
        return dc_td.RestoreTableFromClusterSnapshotResult.make_one(res)

    def resume_cluster(
        self,
        res: "bs_td.ResumeClusterResultTypeDef",
    ) -> "dc_td.ResumeClusterResult":
        return dc_td.ResumeClusterResult.make_one(res)

    def revoke_cluster_security_group_ingress(
        self,
        res: "bs_td.RevokeClusterSecurityGroupIngressResultTypeDef",
    ) -> "dc_td.RevokeClusterSecurityGroupIngressResult":
        return dc_td.RevokeClusterSecurityGroupIngressResult.make_one(res)

    def revoke_endpoint_access(
        self,
        res: "bs_td.EndpointAuthorizationResponseTypeDef",
    ) -> "dc_td.EndpointAuthorizationResponse":
        return dc_td.EndpointAuthorizationResponse.make_one(res)

    def revoke_snapshot_access(
        self,
        res: "bs_td.RevokeSnapshotAccessResultTypeDef",
    ) -> "dc_td.RevokeSnapshotAccessResult":
        return dc_td.RevokeSnapshotAccessResult.make_one(res)

    def rotate_encryption_key(
        self,
        res: "bs_td.RotateEncryptionKeyResultTypeDef",
    ) -> "dc_td.RotateEncryptionKeyResult":
        return dc_td.RotateEncryptionKeyResult.make_one(res)

    def update_partner_status(
        self,
        res: "bs_td.PartnerIntegrationOutputMessageTypeDef",
    ) -> "dc_td.PartnerIntegrationOutputMessage":
        return dc_td.PartnerIntegrationOutputMessage.make_one(res)


redshift_caster = REDSHIFTCaster()
