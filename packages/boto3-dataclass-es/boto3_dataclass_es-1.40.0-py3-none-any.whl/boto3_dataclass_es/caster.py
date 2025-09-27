# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_es import type_defs as bs_td


class ESCaster:

    def accept_inbound_cross_cluster_search_connection(
        self,
        res: "bs_td.AcceptInboundCrossClusterSearchConnectionResponseTypeDef",
    ) -> "dc_td.AcceptInboundCrossClusterSearchConnectionResponse":
        return dc_td.AcceptInboundCrossClusterSearchConnectionResponse.make_one(res)

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

    def cancel_elasticsearch_service_software_update(
        self,
        res: "bs_td.CancelElasticsearchServiceSoftwareUpdateResponseTypeDef",
    ) -> "dc_td.CancelElasticsearchServiceSoftwareUpdateResponse":
        return dc_td.CancelElasticsearchServiceSoftwareUpdateResponse.make_one(res)

    def create_elasticsearch_domain(
        self,
        res: "bs_td.CreateElasticsearchDomainResponseTypeDef",
    ) -> "dc_td.CreateElasticsearchDomainResponse":
        return dc_td.CreateElasticsearchDomainResponse.make_one(res)

    def create_outbound_cross_cluster_search_connection(
        self,
        res: "bs_td.CreateOutboundCrossClusterSearchConnectionResponseTypeDef",
    ) -> "dc_td.CreateOutboundCrossClusterSearchConnectionResponse":
        return dc_td.CreateOutboundCrossClusterSearchConnectionResponse.make_one(res)

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

    def delete_elasticsearch_domain(
        self,
        res: "bs_td.DeleteElasticsearchDomainResponseTypeDef",
    ) -> "dc_td.DeleteElasticsearchDomainResponse":
        return dc_td.DeleteElasticsearchDomainResponse.make_one(res)

    def delete_elasticsearch_service_role(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_inbound_cross_cluster_search_connection(
        self,
        res: "bs_td.DeleteInboundCrossClusterSearchConnectionResponseTypeDef",
    ) -> "dc_td.DeleteInboundCrossClusterSearchConnectionResponse":
        return dc_td.DeleteInboundCrossClusterSearchConnectionResponse.make_one(res)

    def delete_outbound_cross_cluster_search_connection(
        self,
        res: "bs_td.DeleteOutboundCrossClusterSearchConnectionResponseTypeDef",
    ) -> "dc_td.DeleteOutboundCrossClusterSearchConnectionResponse":
        return dc_td.DeleteOutboundCrossClusterSearchConnectionResponse.make_one(res)

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

    def describe_elasticsearch_domain(
        self,
        res: "bs_td.DescribeElasticsearchDomainResponseTypeDef",
    ) -> "dc_td.DescribeElasticsearchDomainResponse":
        return dc_td.DescribeElasticsearchDomainResponse.make_one(res)

    def describe_elasticsearch_domain_config(
        self,
        res: "bs_td.DescribeElasticsearchDomainConfigResponseTypeDef",
    ) -> "dc_td.DescribeElasticsearchDomainConfigResponse":
        return dc_td.DescribeElasticsearchDomainConfigResponse.make_one(res)

    def describe_elasticsearch_domains(
        self,
        res: "bs_td.DescribeElasticsearchDomainsResponseTypeDef",
    ) -> "dc_td.DescribeElasticsearchDomainsResponse":
        return dc_td.DescribeElasticsearchDomainsResponse.make_one(res)

    def describe_elasticsearch_instance_type_limits(
        self,
        res: "bs_td.DescribeElasticsearchInstanceTypeLimitsResponseTypeDef",
    ) -> "dc_td.DescribeElasticsearchInstanceTypeLimitsResponse":
        return dc_td.DescribeElasticsearchInstanceTypeLimitsResponse.make_one(res)

    def describe_inbound_cross_cluster_search_connections(
        self,
        res: "bs_td.DescribeInboundCrossClusterSearchConnectionsResponseTypeDef",
    ) -> "dc_td.DescribeInboundCrossClusterSearchConnectionsResponse":
        return dc_td.DescribeInboundCrossClusterSearchConnectionsResponse.make_one(res)

    def describe_outbound_cross_cluster_search_connections(
        self,
        res: "bs_td.DescribeOutboundCrossClusterSearchConnectionsResponseTypeDef",
    ) -> "dc_td.DescribeOutboundCrossClusterSearchConnectionsResponse":
        return dc_td.DescribeOutboundCrossClusterSearchConnectionsResponse.make_one(res)

    def describe_packages(
        self,
        res: "bs_td.DescribePackagesResponseTypeDef",
    ) -> "dc_td.DescribePackagesResponse":
        return dc_td.DescribePackagesResponse.make_one(res)

    def describe_reserved_elasticsearch_instance_offerings(
        self,
        res: "bs_td.DescribeReservedElasticsearchInstanceOfferingsResponseTypeDef",
    ) -> "dc_td.DescribeReservedElasticsearchInstanceOfferingsResponse":
        return dc_td.DescribeReservedElasticsearchInstanceOfferingsResponse.make_one(
            res
        )

    def describe_reserved_elasticsearch_instances(
        self,
        res: "bs_td.DescribeReservedElasticsearchInstancesResponseTypeDef",
    ) -> "dc_td.DescribeReservedElasticsearchInstancesResponse":
        return dc_td.DescribeReservedElasticsearchInstancesResponse.make_one(res)

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

    def get_compatible_elasticsearch_versions(
        self,
        res: "bs_td.GetCompatibleElasticsearchVersionsResponseTypeDef",
    ) -> "dc_td.GetCompatibleElasticsearchVersionsResponse":
        return dc_td.GetCompatibleElasticsearchVersionsResponse.make_one(res)

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

    def list_elasticsearch_instance_types(
        self,
        res: "bs_td.ListElasticsearchInstanceTypesResponseTypeDef",
    ) -> "dc_td.ListElasticsearchInstanceTypesResponse":
        return dc_td.ListElasticsearchInstanceTypesResponse.make_one(res)

    def list_elasticsearch_versions(
        self,
        res: "bs_td.ListElasticsearchVersionsResponseTypeDef",
    ) -> "dc_td.ListElasticsearchVersionsResponse":
        return dc_td.ListElasticsearchVersionsResponse.make_one(res)

    def list_packages_for_domain(
        self,
        res: "bs_td.ListPackagesForDomainResponseTypeDef",
    ) -> "dc_td.ListPackagesForDomainResponse":
        return dc_td.ListPackagesForDomainResponse.make_one(res)

    def list_tags(
        self,
        res: "bs_td.ListTagsResponseTypeDef",
    ) -> "dc_td.ListTagsResponse":
        return dc_td.ListTagsResponse.make_one(res)

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

    def purchase_reserved_elasticsearch_instance_offering(
        self,
        res: "bs_td.PurchaseReservedElasticsearchInstanceOfferingResponseTypeDef",
    ) -> "dc_td.PurchaseReservedElasticsearchInstanceOfferingResponse":
        return dc_td.PurchaseReservedElasticsearchInstanceOfferingResponse.make_one(res)

    def reject_inbound_cross_cluster_search_connection(
        self,
        res: "bs_td.RejectInboundCrossClusterSearchConnectionResponseTypeDef",
    ) -> "dc_td.RejectInboundCrossClusterSearchConnectionResponse":
        return dc_td.RejectInboundCrossClusterSearchConnectionResponse.make_one(res)

    def remove_tags(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def start_elasticsearch_service_software_update(
        self,
        res: "bs_td.StartElasticsearchServiceSoftwareUpdateResponseTypeDef",
    ) -> "dc_td.StartElasticsearchServiceSoftwareUpdateResponse":
        return dc_td.StartElasticsearchServiceSoftwareUpdateResponse.make_one(res)

    def update_elasticsearch_domain_config(
        self,
        res: "bs_td.UpdateElasticsearchDomainConfigResponseTypeDef",
    ) -> "dc_td.UpdateElasticsearchDomainConfigResponse":
        return dc_td.UpdateElasticsearchDomainConfigResponse.make_one(res)

    def update_package(
        self,
        res: "bs_td.UpdatePackageResponseTypeDef",
    ) -> "dc_td.UpdatePackageResponse":
        return dc_td.UpdatePackageResponse.make_one(res)

    def update_vpc_endpoint(
        self,
        res: "bs_td.UpdateVpcEndpointResponseTypeDef",
    ) -> "dc_td.UpdateVpcEndpointResponse":
        return dc_td.UpdateVpcEndpointResponse.make_one(res)

    def upgrade_elasticsearch_domain(
        self,
        res: "bs_td.UpgradeElasticsearchDomainResponseTypeDef",
    ) -> "dc_td.UpgradeElasticsearchDomainResponse":
        return dc_td.UpgradeElasticsearchDomainResponse.make_one(res)


es_caster = ESCaster()
