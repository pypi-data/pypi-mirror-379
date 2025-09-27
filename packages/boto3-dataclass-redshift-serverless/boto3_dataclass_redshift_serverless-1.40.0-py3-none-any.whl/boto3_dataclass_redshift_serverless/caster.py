# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_redshift_serverless import type_defs as bs_td


class REDSHIFT_SERVERLESSCaster:

    def convert_recovery_point_to_snapshot(
        self,
        res: "bs_td.ConvertRecoveryPointToSnapshotResponseTypeDef",
    ) -> "dc_td.ConvertRecoveryPointToSnapshotResponse":
        return dc_td.ConvertRecoveryPointToSnapshotResponse.make_one(res)

    def create_custom_domain_association(
        self,
        res: "bs_td.CreateCustomDomainAssociationResponseTypeDef",
    ) -> "dc_td.CreateCustomDomainAssociationResponse":
        return dc_td.CreateCustomDomainAssociationResponse.make_one(res)

    def create_endpoint_access(
        self,
        res: "bs_td.CreateEndpointAccessResponseTypeDef",
    ) -> "dc_td.CreateEndpointAccessResponse":
        return dc_td.CreateEndpointAccessResponse.make_one(res)

    def create_namespace(
        self,
        res: "bs_td.CreateNamespaceResponseTypeDef",
    ) -> "dc_td.CreateNamespaceResponse":
        return dc_td.CreateNamespaceResponse.make_one(res)

    def create_reservation(
        self,
        res: "bs_td.CreateReservationResponseTypeDef",
    ) -> "dc_td.CreateReservationResponse":
        return dc_td.CreateReservationResponse.make_one(res)

    def create_scheduled_action(
        self,
        res: "bs_td.CreateScheduledActionResponseTypeDef",
    ) -> "dc_td.CreateScheduledActionResponse":
        return dc_td.CreateScheduledActionResponse.make_one(res)

    def create_snapshot(
        self,
        res: "bs_td.CreateSnapshotResponseTypeDef",
    ) -> "dc_td.CreateSnapshotResponse":
        return dc_td.CreateSnapshotResponse.make_one(res)

    def create_snapshot_copy_configuration(
        self,
        res: "bs_td.CreateSnapshotCopyConfigurationResponseTypeDef",
    ) -> "dc_td.CreateSnapshotCopyConfigurationResponse":
        return dc_td.CreateSnapshotCopyConfigurationResponse.make_one(res)

    def create_usage_limit(
        self,
        res: "bs_td.CreateUsageLimitResponseTypeDef",
    ) -> "dc_td.CreateUsageLimitResponse":
        return dc_td.CreateUsageLimitResponse.make_one(res)

    def create_workgroup(
        self,
        res: "bs_td.CreateWorkgroupResponseTypeDef",
    ) -> "dc_td.CreateWorkgroupResponse":
        return dc_td.CreateWorkgroupResponse.make_one(res)

    def delete_endpoint_access(
        self,
        res: "bs_td.DeleteEndpointAccessResponseTypeDef",
    ) -> "dc_td.DeleteEndpointAccessResponse":
        return dc_td.DeleteEndpointAccessResponse.make_one(res)

    def delete_namespace(
        self,
        res: "bs_td.DeleteNamespaceResponseTypeDef",
    ) -> "dc_td.DeleteNamespaceResponse":
        return dc_td.DeleteNamespaceResponse.make_one(res)

    def delete_scheduled_action(
        self,
        res: "bs_td.DeleteScheduledActionResponseTypeDef",
    ) -> "dc_td.DeleteScheduledActionResponse":
        return dc_td.DeleteScheduledActionResponse.make_one(res)

    def delete_snapshot(
        self,
        res: "bs_td.DeleteSnapshotResponseTypeDef",
    ) -> "dc_td.DeleteSnapshotResponse":
        return dc_td.DeleteSnapshotResponse.make_one(res)

    def delete_snapshot_copy_configuration(
        self,
        res: "bs_td.DeleteSnapshotCopyConfigurationResponseTypeDef",
    ) -> "dc_td.DeleteSnapshotCopyConfigurationResponse":
        return dc_td.DeleteSnapshotCopyConfigurationResponse.make_one(res)

    def delete_usage_limit(
        self,
        res: "bs_td.DeleteUsageLimitResponseTypeDef",
    ) -> "dc_td.DeleteUsageLimitResponse":
        return dc_td.DeleteUsageLimitResponse.make_one(res)

    def delete_workgroup(
        self,
        res: "bs_td.DeleteWorkgroupResponseTypeDef",
    ) -> "dc_td.DeleteWorkgroupResponse":
        return dc_td.DeleteWorkgroupResponse.make_one(res)

    def get_credentials(
        self,
        res: "bs_td.GetCredentialsResponseTypeDef",
    ) -> "dc_td.GetCredentialsResponse":
        return dc_td.GetCredentialsResponse.make_one(res)

    def get_custom_domain_association(
        self,
        res: "bs_td.GetCustomDomainAssociationResponseTypeDef",
    ) -> "dc_td.GetCustomDomainAssociationResponse":
        return dc_td.GetCustomDomainAssociationResponse.make_one(res)

    def get_endpoint_access(
        self,
        res: "bs_td.GetEndpointAccessResponseTypeDef",
    ) -> "dc_td.GetEndpointAccessResponse":
        return dc_td.GetEndpointAccessResponse.make_one(res)

    def get_namespace(
        self,
        res: "bs_td.GetNamespaceResponseTypeDef",
    ) -> "dc_td.GetNamespaceResponse":
        return dc_td.GetNamespaceResponse.make_one(res)

    def get_recovery_point(
        self,
        res: "bs_td.GetRecoveryPointResponseTypeDef",
    ) -> "dc_td.GetRecoveryPointResponse":
        return dc_td.GetRecoveryPointResponse.make_one(res)

    def get_reservation(
        self,
        res: "bs_td.GetReservationResponseTypeDef",
    ) -> "dc_td.GetReservationResponse":
        return dc_td.GetReservationResponse.make_one(res)

    def get_reservation_offering(
        self,
        res: "bs_td.GetReservationOfferingResponseTypeDef",
    ) -> "dc_td.GetReservationOfferingResponse":
        return dc_td.GetReservationOfferingResponse.make_one(res)

    def get_resource_policy(
        self,
        res: "bs_td.GetResourcePolicyResponseTypeDef",
    ) -> "dc_td.GetResourcePolicyResponse":
        return dc_td.GetResourcePolicyResponse.make_one(res)

    def get_scheduled_action(
        self,
        res: "bs_td.GetScheduledActionResponseTypeDef",
    ) -> "dc_td.GetScheduledActionResponse":
        return dc_td.GetScheduledActionResponse.make_one(res)

    def get_snapshot(
        self,
        res: "bs_td.GetSnapshotResponseTypeDef",
    ) -> "dc_td.GetSnapshotResponse":
        return dc_td.GetSnapshotResponse.make_one(res)

    def get_table_restore_status(
        self,
        res: "bs_td.GetTableRestoreStatusResponseTypeDef",
    ) -> "dc_td.GetTableRestoreStatusResponse":
        return dc_td.GetTableRestoreStatusResponse.make_one(res)

    def get_track(
        self,
        res: "bs_td.GetTrackResponseTypeDef",
    ) -> "dc_td.GetTrackResponse":
        return dc_td.GetTrackResponse.make_one(res)

    def get_usage_limit(
        self,
        res: "bs_td.GetUsageLimitResponseTypeDef",
    ) -> "dc_td.GetUsageLimitResponse":
        return dc_td.GetUsageLimitResponse.make_one(res)

    def get_workgroup(
        self,
        res: "bs_td.GetWorkgroupResponseTypeDef",
    ) -> "dc_td.GetWorkgroupResponse":
        return dc_td.GetWorkgroupResponse.make_one(res)

    def list_custom_domain_associations(
        self,
        res: "bs_td.ListCustomDomainAssociationsResponseTypeDef",
    ) -> "dc_td.ListCustomDomainAssociationsResponse":
        return dc_td.ListCustomDomainAssociationsResponse.make_one(res)

    def list_endpoint_access(
        self,
        res: "bs_td.ListEndpointAccessResponseTypeDef",
    ) -> "dc_td.ListEndpointAccessResponse":
        return dc_td.ListEndpointAccessResponse.make_one(res)

    def list_managed_workgroups(
        self,
        res: "bs_td.ListManagedWorkgroupsResponseTypeDef",
    ) -> "dc_td.ListManagedWorkgroupsResponse":
        return dc_td.ListManagedWorkgroupsResponse.make_one(res)

    def list_namespaces(
        self,
        res: "bs_td.ListNamespacesResponseTypeDef",
    ) -> "dc_td.ListNamespacesResponse":
        return dc_td.ListNamespacesResponse.make_one(res)

    def list_recovery_points(
        self,
        res: "bs_td.ListRecoveryPointsResponseTypeDef",
    ) -> "dc_td.ListRecoveryPointsResponse":
        return dc_td.ListRecoveryPointsResponse.make_one(res)

    def list_reservation_offerings(
        self,
        res: "bs_td.ListReservationOfferingsResponseTypeDef",
    ) -> "dc_td.ListReservationOfferingsResponse":
        return dc_td.ListReservationOfferingsResponse.make_one(res)

    def list_reservations(
        self,
        res: "bs_td.ListReservationsResponseTypeDef",
    ) -> "dc_td.ListReservationsResponse":
        return dc_td.ListReservationsResponse.make_one(res)

    def list_scheduled_actions(
        self,
        res: "bs_td.ListScheduledActionsResponseTypeDef",
    ) -> "dc_td.ListScheduledActionsResponse":
        return dc_td.ListScheduledActionsResponse.make_one(res)

    def list_snapshot_copy_configurations(
        self,
        res: "bs_td.ListSnapshotCopyConfigurationsResponseTypeDef",
    ) -> "dc_td.ListSnapshotCopyConfigurationsResponse":
        return dc_td.ListSnapshotCopyConfigurationsResponse.make_one(res)

    def list_snapshots(
        self,
        res: "bs_td.ListSnapshotsResponseTypeDef",
    ) -> "dc_td.ListSnapshotsResponse":
        return dc_td.ListSnapshotsResponse.make_one(res)

    def list_table_restore_status(
        self,
        res: "bs_td.ListTableRestoreStatusResponseTypeDef",
    ) -> "dc_td.ListTableRestoreStatusResponse":
        return dc_td.ListTableRestoreStatusResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def list_tracks(
        self,
        res: "bs_td.ListTracksResponseTypeDef",
    ) -> "dc_td.ListTracksResponse":
        return dc_td.ListTracksResponse.make_one(res)

    def list_usage_limits(
        self,
        res: "bs_td.ListUsageLimitsResponseTypeDef",
    ) -> "dc_td.ListUsageLimitsResponse":
        return dc_td.ListUsageLimitsResponse.make_one(res)

    def list_workgroups(
        self,
        res: "bs_td.ListWorkgroupsResponseTypeDef",
    ) -> "dc_td.ListWorkgroupsResponse":
        return dc_td.ListWorkgroupsResponse.make_one(res)

    def put_resource_policy(
        self,
        res: "bs_td.PutResourcePolicyResponseTypeDef",
    ) -> "dc_td.PutResourcePolicyResponse":
        return dc_td.PutResourcePolicyResponse.make_one(res)

    def restore_from_recovery_point(
        self,
        res: "bs_td.RestoreFromRecoveryPointResponseTypeDef",
    ) -> "dc_td.RestoreFromRecoveryPointResponse":
        return dc_td.RestoreFromRecoveryPointResponse.make_one(res)

    def restore_from_snapshot(
        self,
        res: "bs_td.RestoreFromSnapshotResponseTypeDef",
    ) -> "dc_td.RestoreFromSnapshotResponse":
        return dc_td.RestoreFromSnapshotResponse.make_one(res)

    def restore_table_from_recovery_point(
        self,
        res: "bs_td.RestoreTableFromRecoveryPointResponseTypeDef",
    ) -> "dc_td.RestoreTableFromRecoveryPointResponse":
        return dc_td.RestoreTableFromRecoveryPointResponse.make_one(res)

    def restore_table_from_snapshot(
        self,
        res: "bs_td.RestoreTableFromSnapshotResponseTypeDef",
    ) -> "dc_td.RestoreTableFromSnapshotResponse":
        return dc_td.RestoreTableFromSnapshotResponse.make_one(res)

    def update_custom_domain_association(
        self,
        res: "bs_td.UpdateCustomDomainAssociationResponseTypeDef",
    ) -> "dc_td.UpdateCustomDomainAssociationResponse":
        return dc_td.UpdateCustomDomainAssociationResponse.make_one(res)

    def update_endpoint_access(
        self,
        res: "bs_td.UpdateEndpointAccessResponseTypeDef",
    ) -> "dc_td.UpdateEndpointAccessResponse":
        return dc_td.UpdateEndpointAccessResponse.make_one(res)

    def update_namespace(
        self,
        res: "bs_td.UpdateNamespaceResponseTypeDef",
    ) -> "dc_td.UpdateNamespaceResponse":
        return dc_td.UpdateNamespaceResponse.make_one(res)

    def update_scheduled_action(
        self,
        res: "bs_td.UpdateScheduledActionResponseTypeDef",
    ) -> "dc_td.UpdateScheduledActionResponse":
        return dc_td.UpdateScheduledActionResponse.make_one(res)

    def update_snapshot(
        self,
        res: "bs_td.UpdateSnapshotResponseTypeDef",
    ) -> "dc_td.UpdateSnapshotResponse":
        return dc_td.UpdateSnapshotResponse.make_one(res)

    def update_snapshot_copy_configuration(
        self,
        res: "bs_td.UpdateSnapshotCopyConfigurationResponseTypeDef",
    ) -> "dc_td.UpdateSnapshotCopyConfigurationResponse":
        return dc_td.UpdateSnapshotCopyConfigurationResponse.make_one(res)

    def update_usage_limit(
        self,
        res: "bs_td.UpdateUsageLimitResponseTypeDef",
    ) -> "dc_td.UpdateUsageLimitResponse":
        return dc_td.UpdateUsageLimitResponse.make_one(res)

    def update_workgroup(
        self,
        res: "bs_td.UpdateWorkgroupResponseTypeDef",
    ) -> "dc_td.UpdateWorkgroupResponse":
        return dc_td.UpdateWorkgroupResponse.make_one(res)


redshift_serverless_caster = REDSHIFT_SERVERLESSCaster()
