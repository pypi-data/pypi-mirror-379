# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_opensearch import type_defs as bs_td


class OPENSEARCHCaster:

    def accept_inbound_connection(
        self,
        res: "bs_td.AcceptInboundConnectionResponseTypeDef",
    ) -> "dc_td.AcceptInboundConnectionResponse":
        return dc_td.AcceptInboundConnectionResponse.make_one(res)

    def add_data_source(
        self,
        res: "bs_td.AddDataSourceResponseTypeDef",
    ) -> "dc_td.AddDataSourceResponse":
        return dc_td.AddDataSourceResponse.make_one(res)

    def add_direct_query_data_source(
        self,
        res: "bs_td.AddDirectQueryDataSourceResponseTypeDef",
    ) -> "dc_td.AddDirectQueryDataSourceResponse":
        return dc_td.AddDirectQueryDataSourceResponse.make_one(res)

    def add_tags(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def associate_package(
        self,
        res: "bs_td.AssociatePackageResponseTypeDef",
    ) -> "dc_td.AssociatePackageResponse":
        return dc_td.AssociatePackageResponse.make_one(res)

    def associate_packages(
        self,
        res: "bs_td.AssociatePackagesResponseTypeDef",
    ) -> "dc_td.AssociatePackagesResponse":
        return dc_td.AssociatePackagesResponse.make_one(res)

    def authorize_vpc_endpoint_access(
        self,
        res: "bs_td.AuthorizeVpcEndpointAccessResponseTypeDef",
    ) -> "dc_td.AuthorizeVpcEndpointAccessResponse":
        return dc_td.AuthorizeVpcEndpointAccessResponse.make_one(res)

    def cancel_domain_config_change(
        self,
        res: "bs_td.CancelDomainConfigChangeResponseTypeDef",
    ) -> "dc_td.CancelDomainConfigChangeResponse":
        return dc_td.CancelDomainConfigChangeResponse.make_one(res)

    def cancel_service_software_update(
        self,
        res: "bs_td.CancelServiceSoftwareUpdateResponseTypeDef",
    ) -> "dc_td.CancelServiceSoftwareUpdateResponse":
        return dc_td.CancelServiceSoftwareUpdateResponse.make_one(res)

    def create_application(
        self,
        res: "bs_td.CreateApplicationResponseTypeDef",
    ) -> "dc_td.CreateApplicationResponse":
        return dc_td.CreateApplicationResponse.make_one(res)

    def create_domain(
        self,
        res: "bs_td.CreateDomainResponseTypeDef",
    ) -> "dc_td.CreateDomainResponse":
        return dc_td.CreateDomainResponse.make_one(res)

    def create_outbound_connection(
        self,
        res: "bs_td.CreateOutboundConnectionResponseTypeDef",
    ) -> "dc_td.CreateOutboundConnectionResponse":
        return dc_td.CreateOutboundConnectionResponse.make_one(res)

    def create_package(
        self,
        res: "bs_td.CreatePackageResponseTypeDef",
    ) -> "dc_td.CreatePackageResponse":
        return dc_td.CreatePackageResponse.make_one(res)

    def create_vpc_endpoint(
        self,
        res: "bs_td.CreateVpcEndpointResponseTypeDef",
    ) -> "dc_td.CreateVpcEndpointResponse":
        return dc_td.CreateVpcEndpointResponse.make_one(res)

    def delete_data_source(
        self,
        res: "bs_td.DeleteDataSourceResponseTypeDef",
    ) -> "dc_td.DeleteDataSourceResponse":
        return dc_td.DeleteDataSourceResponse.make_one(res)

    def delete_direct_query_data_source(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_domain(
        self,
        res: "bs_td.DeleteDomainResponseTypeDef",
    ) -> "dc_td.DeleteDomainResponse":
        return dc_td.DeleteDomainResponse.make_one(res)

    def delete_inbound_connection(
        self,
        res: "bs_td.DeleteInboundConnectionResponseTypeDef",
    ) -> "dc_td.DeleteInboundConnectionResponse":
        return dc_td.DeleteInboundConnectionResponse.make_one(res)

    def delete_outbound_connection(
        self,
        res: "bs_td.DeleteOutboundConnectionResponseTypeDef",
    ) -> "dc_td.DeleteOutboundConnectionResponse":
        return dc_td.DeleteOutboundConnectionResponse.make_one(res)

    def delete_package(
        self,
        res: "bs_td.DeletePackageResponseTypeDef",
    ) -> "dc_td.DeletePackageResponse":
        return dc_td.DeletePackageResponse.make_one(res)

    def delete_vpc_endpoint(
        self,
        res: "bs_td.DeleteVpcEndpointResponseTypeDef",
    ) -> "dc_td.DeleteVpcEndpointResponse":
        return dc_td.DeleteVpcEndpointResponse.make_one(res)

    def describe_domain(
        self,
        res: "bs_td.DescribeDomainResponseTypeDef",
    ) -> "dc_td.DescribeDomainResponse":
        return dc_td.DescribeDomainResponse.make_one(res)

    def describe_domain_auto_tunes(
        self,
        res: "bs_td.DescribeDomainAutoTunesResponseTypeDef",
    ) -> "dc_td.DescribeDomainAutoTunesResponse":
        return dc_td.DescribeDomainAutoTunesResponse.make_one(res)

    def describe_domain_change_progress(
        self,
        res: "bs_td.DescribeDomainChangeProgressResponseTypeDef",
    ) -> "dc_td.DescribeDomainChangeProgressResponse":
        return dc_td.DescribeDomainChangeProgressResponse.make_one(res)

    def describe_domain_config(
        self,
        res: "bs_td.DescribeDomainConfigResponseTypeDef",
    ) -> "dc_td.DescribeDomainConfigResponse":
        return dc_td.DescribeDomainConfigResponse.make_one(res)

    def describe_domain_health(
        self,
        res: "bs_td.DescribeDomainHealthResponseTypeDef",
    ) -> "dc_td.DescribeDomainHealthResponse":
        return dc_td.DescribeDomainHealthResponse.make_one(res)

    def describe_domain_nodes(
        self,
        res: "bs_td.DescribeDomainNodesResponseTypeDef",
    ) -> "dc_td.DescribeDomainNodesResponse":
        return dc_td.DescribeDomainNodesResponse.make_one(res)

    def describe_domains(
        self,
        res: "bs_td.DescribeDomainsResponseTypeDef",
    ) -> "dc_td.DescribeDomainsResponse":
        return dc_td.DescribeDomainsResponse.make_one(res)

    def describe_dry_run_progress(
        self,
        res: "bs_td.DescribeDryRunProgressResponseTypeDef",
    ) -> "dc_td.DescribeDryRunProgressResponse":
        return dc_td.DescribeDryRunProgressResponse.make_one(res)

    def describe_inbound_connections(
        self,
        res: "bs_td.DescribeInboundConnectionsResponseTypeDef",
    ) -> "dc_td.DescribeInboundConnectionsResponse":
        return dc_td.DescribeInboundConnectionsResponse.make_one(res)

    def describe_instance_type_limits(
        self,
        res: "bs_td.DescribeInstanceTypeLimitsResponseTypeDef",
    ) -> "dc_td.DescribeInstanceTypeLimitsResponse":
        return dc_td.DescribeInstanceTypeLimitsResponse.make_one(res)

    def describe_outbound_connections(
        self,
        res: "bs_td.DescribeOutboundConnectionsResponseTypeDef",
    ) -> "dc_td.DescribeOutboundConnectionsResponse":
        return dc_td.DescribeOutboundConnectionsResponse.make_one(res)

    def describe_packages(
        self,
        res: "bs_td.DescribePackagesResponseTypeDef",
    ) -> "dc_td.DescribePackagesResponse":
        return dc_td.DescribePackagesResponse.make_one(res)

    def describe_reserved_instance_offerings(
        self,
        res: "bs_td.DescribeReservedInstanceOfferingsResponseTypeDef",
    ) -> "dc_td.DescribeReservedInstanceOfferingsResponse":
        return dc_td.DescribeReservedInstanceOfferingsResponse.make_one(res)

    def describe_reserved_instances(
        self,
        res: "bs_td.DescribeReservedInstancesResponseTypeDef",
    ) -> "dc_td.DescribeReservedInstancesResponse":
        return dc_td.DescribeReservedInstancesResponse.make_one(res)

    def describe_vpc_endpoints(
        self,
        res: "bs_td.DescribeVpcEndpointsResponseTypeDef",
    ) -> "dc_td.DescribeVpcEndpointsResponse":
        return dc_td.DescribeVpcEndpointsResponse.make_one(res)

    def dissociate_package(
        self,
        res: "bs_td.DissociatePackageResponseTypeDef",
    ) -> "dc_td.DissociatePackageResponse":
        return dc_td.DissociatePackageResponse.make_one(res)

    def dissociate_packages(
        self,
        res: "bs_td.DissociatePackagesResponseTypeDef",
    ) -> "dc_td.DissociatePackagesResponse":
        return dc_td.DissociatePackagesResponse.make_one(res)

    def get_application(
        self,
        res: "bs_td.GetApplicationResponseTypeDef",
    ) -> "dc_td.GetApplicationResponse":
        return dc_td.GetApplicationResponse.make_one(res)

    def get_compatible_versions(
        self,
        res: "bs_td.GetCompatibleVersionsResponseTypeDef",
    ) -> "dc_td.GetCompatibleVersionsResponse":
        return dc_td.GetCompatibleVersionsResponse.make_one(res)

    def get_data_source(
        self,
        res: "bs_td.GetDataSourceResponseTypeDef",
    ) -> "dc_td.GetDataSourceResponse":
        return dc_td.GetDataSourceResponse.make_one(res)

    def get_direct_query_data_source(
        self,
        res: "bs_td.GetDirectQueryDataSourceResponseTypeDef",
    ) -> "dc_td.GetDirectQueryDataSourceResponse":
        return dc_td.GetDirectQueryDataSourceResponse.make_one(res)

    def get_domain_maintenance_status(
        self,
        res: "bs_td.GetDomainMaintenanceStatusResponseTypeDef",
    ) -> "dc_td.GetDomainMaintenanceStatusResponse":
        return dc_td.GetDomainMaintenanceStatusResponse.make_one(res)

    def get_package_version_history(
        self,
        res: "bs_td.GetPackageVersionHistoryResponseTypeDef",
    ) -> "dc_td.GetPackageVersionHistoryResponse":
        return dc_td.GetPackageVersionHistoryResponse.make_one(res)

    def get_upgrade_history(
        self,
        res: "bs_td.GetUpgradeHistoryResponseTypeDef",
    ) -> "dc_td.GetUpgradeHistoryResponse":
        return dc_td.GetUpgradeHistoryResponse.make_one(res)

    def get_upgrade_status(
        self,
        res: "bs_td.GetUpgradeStatusResponseTypeDef",
    ) -> "dc_td.GetUpgradeStatusResponse":
        return dc_td.GetUpgradeStatusResponse.make_one(res)

    def list_applications(
        self,
        res: "bs_td.ListApplicationsResponseTypeDef",
    ) -> "dc_td.ListApplicationsResponse":
        return dc_td.ListApplicationsResponse.make_one(res)

    def list_data_sources(
        self,
        res: "bs_td.ListDataSourcesResponseTypeDef",
    ) -> "dc_td.ListDataSourcesResponse":
        return dc_td.ListDataSourcesResponse.make_one(res)

    def list_direct_query_data_sources(
        self,
        res: "bs_td.ListDirectQueryDataSourcesResponseTypeDef",
    ) -> "dc_td.ListDirectQueryDataSourcesResponse":
        return dc_td.ListDirectQueryDataSourcesResponse.make_one(res)

    def list_domain_maintenances(
        self,
        res: "bs_td.ListDomainMaintenancesResponseTypeDef",
    ) -> "dc_td.ListDomainMaintenancesResponse":
        return dc_td.ListDomainMaintenancesResponse.make_one(res)

    def list_domain_names(
        self,
        res: "bs_td.ListDomainNamesResponseTypeDef",
    ) -> "dc_td.ListDomainNamesResponse":
        return dc_td.ListDomainNamesResponse.make_one(res)

    def list_domains_for_package(
        self,
        res: "bs_td.ListDomainsForPackageResponseTypeDef",
    ) -> "dc_td.ListDomainsForPackageResponse":
        return dc_td.ListDomainsForPackageResponse.make_one(res)

    def list_instance_type_details(
        self,
        res: "bs_td.ListInstanceTypeDetailsResponseTypeDef",
    ) -> "dc_td.ListInstanceTypeDetailsResponse":
        return dc_td.ListInstanceTypeDetailsResponse.make_one(res)

    def list_packages_for_domain(
        self,
        res: "bs_td.ListPackagesForDomainResponseTypeDef",
    ) -> "dc_td.ListPackagesForDomainResponse":
        return dc_td.ListPackagesForDomainResponse.make_one(res)

    def list_scheduled_actions(
        self,
        res: "bs_td.ListScheduledActionsResponseTypeDef",
    ) -> "dc_td.ListScheduledActionsResponse":
        return dc_td.ListScheduledActionsResponse.make_one(res)

    def list_tags(
        self,
        res: "bs_td.ListTagsResponseTypeDef",
    ) -> "dc_td.ListTagsResponse":
        return dc_td.ListTagsResponse.make_one(res)

    def list_versions(
        self,
        res: "bs_td.ListVersionsResponseTypeDef",
    ) -> "dc_td.ListVersionsResponse":
        return dc_td.ListVersionsResponse.make_one(res)

    def list_vpc_endpoint_access(
        self,
        res: "bs_td.ListVpcEndpointAccessResponseTypeDef",
    ) -> "dc_td.ListVpcEndpointAccessResponse":
        return dc_td.ListVpcEndpointAccessResponse.make_one(res)

    def list_vpc_endpoints(
        self,
        res: "bs_td.ListVpcEndpointsResponseTypeDef",
    ) -> "dc_td.ListVpcEndpointsResponse":
        return dc_td.ListVpcEndpointsResponse.make_one(res)

    def list_vpc_endpoints_for_domain(
        self,
        res: "bs_td.ListVpcEndpointsForDomainResponseTypeDef",
    ) -> "dc_td.ListVpcEndpointsForDomainResponse":
        return dc_td.ListVpcEndpointsForDomainResponse.make_one(res)

    def purchase_reserved_instance_offering(
        self,
        res: "bs_td.PurchaseReservedInstanceOfferingResponseTypeDef",
    ) -> "dc_td.PurchaseReservedInstanceOfferingResponse":
        return dc_td.PurchaseReservedInstanceOfferingResponse.make_one(res)

    def reject_inbound_connection(
        self,
        res: "bs_td.RejectInboundConnectionResponseTypeDef",
    ) -> "dc_td.RejectInboundConnectionResponse":
        return dc_td.RejectInboundConnectionResponse.make_one(res)

    def remove_tags(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def start_domain_maintenance(
        self,
        res: "bs_td.StartDomainMaintenanceResponseTypeDef",
    ) -> "dc_td.StartDomainMaintenanceResponse":
        return dc_td.StartDomainMaintenanceResponse.make_one(res)

    def start_service_software_update(
        self,
        res: "bs_td.StartServiceSoftwareUpdateResponseTypeDef",
    ) -> "dc_td.StartServiceSoftwareUpdateResponse":
        return dc_td.StartServiceSoftwareUpdateResponse.make_one(res)

    def update_application(
        self,
        res: "bs_td.UpdateApplicationResponseTypeDef",
    ) -> "dc_td.UpdateApplicationResponse":
        return dc_td.UpdateApplicationResponse.make_one(res)

    def update_data_source(
        self,
        res: "bs_td.UpdateDataSourceResponseTypeDef",
    ) -> "dc_td.UpdateDataSourceResponse":
        return dc_td.UpdateDataSourceResponse.make_one(res)

    def update_direct_query_data_source(
        self,
        res: "bs_td.UpdateDirectQueryDataSourceResponseTypeDef",
    ) -> "dc_td.UpdateDirectQueryDataSourceResponse":
        return dc_td.UpdateDirectQueryDataSourceResponse.make_one(res)

    def update_domain_config(
        self,
        res: "bs_td.UpdateDomainConfigResponseTypeDef",
    ) -> "dc_td.UpdateDomainConfigResponse":
        return dc_td.UpdateDomainConfigResponse.make_one(res)

    def update_package(
        self,
        res: "bs_td.UpdatePackageResponseTypeDef",
    ) -> "dc_td.UpdatePackageResponse":
        return dc_td.UpdatePackageResponse.make_one(res)

    def update_package_scope(
        self,
        res: "bs_td.UpdatePackageScopeResponseTypeDef",
    ) -> "dc_td.UpdatePackageScopeResponse":
        return dc_td.UpdatePackageScopeResponse.make_one(res)

    def update_scheduled_action(
        self,
        res: "bs_td.UpdateScheduledActionResponseTypeDef",
    ) -> "dc_td.UpdateScheduledActionResponse":
        return dc_td.UpdateScheduledActionResponse.make_one(res)

    def update_vpc_endpoint(
        self,
        res: "bs_td.UpdateVpcEndpointResponseTypeDef",
    ) -> "dc_td.UpdateVpcEndpointResponse":
        return dc_td.UpdateVpcEndpointResponse.make_one(res)

    def upgrade_domain(
        self,
        res: "bs_td.UpgradeDomainResponseTypeDef",
    ) -> "dc_td.UpgradeDomainResponse":
        return dc_td.UpgradeDomainResponse.make_one(res)


opensearch_caster = OPENSEARCHCaster()
