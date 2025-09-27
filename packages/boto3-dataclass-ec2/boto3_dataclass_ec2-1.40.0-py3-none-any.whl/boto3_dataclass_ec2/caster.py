# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_ec2 import type_defs as bs_td


class EC2Caster:

    def accept_address_transfer(
        self,
        res: "bs_td.AcceptAddressTransferResultTypeDef",
    ) -> "dc_td.AcceptAddressTransferResult":
        return dc_td.AcceptAddressTransferResult.make_one(res)

    def accept_capacity_reservation_billing_ownership(
        self,
        res: "bs_td.AcceptCapacityReservationBillingOwnershipResultTypeDef",
    ) -> "dc_td.AcceptCapacityReservationBillingOwnershipResult":
        return dc_td.AcceptCapacityReservationBillingOwnershipResult.make_one(res)

    def accept_reserved_instances_exchange_quote(
        self,
        res: "bs_td.AcceptReservedInstancesExchangeQuoteResultTypeDef",
    ) -> "dc_td.AcceptReservedInstancesExchangeQuoteResult":
        return dc_td.AcceptReservedInstancesExchangeQuoteResult.make_one(res)

    def accept_transit_gateway_multicast_domain_associations(
        self,
        res: "bs_td.AcceptTransitGatewayMulticastDomainAssociationsResultTypeDef",
    ) -> "dc_td.AcceptTransitGatewayMulticastDomainAssociationsResult":
        return dc_td.AcceptTransitGatewayMulticastDomainAssociationsResult.make_one(res)

    def accept_transit_gateway_peering_attachment(
        self,
        res: "bs_td.AcceptTransitGatewayPeeringAttachmentResultTypeDef",
    ) -> "dc_td.AcceptTransitGatewayPeeringAttachmentResult":
        return dc_td.AcceptTransitGatewayPeeringAttachmentResult.make_one(res)

    def accept_transit_gateway_vpc_attachment(
        self,
        res: "bs_td.AcceptTransitGatewayVpcAttachmentResultTypeDef",
    ) -> "dc_td.AcceptTransitGatewayVpcAttachmentResult":
        return dc_td.AcceptTransitGatewayVpcAttachmentResult.make_one(res)

    def accept_vpc_endpoint_connections(
        self,
        res: "bs_td.AcceptVpcEndpointConnectionsResultTypeDef",
    ) -> "dc_td.AcceptVpcEndpointConnectionsResult":
        return dc_td.AcceptVpcEndpointConnectionsResult.make_one(res)

    def accept_vpc_peering_connection(
        self,
        res: "bs_td.AcceptVpcPeeringConnectionResultTypeDef",
    ) -> "dc_td.AcceptVpcPeeringConnectionResult":
        return dc_td.AcceptVpcPeeringConnectionResult.make_one(res)

    def advertise_byoip_cidr(
        self,
        res: "bs_td.AdvertiseByoipCidrResultTypeDef",
    ) -> "dc_td.AdvertiseByoipCidrResult":
        return dc_td.AdvertiseByoipCidrResult.make_one(res)

    def allocate_address(
        self,
        res: "bs_td.AllocateAddressResultTypeDef",
    ) -> "dc_td.AllocateAddressResult":
        return dc_td.AllocateAddressResult.make_one(res)

    def allocate_hosts(
        self,
        res: "bs_td.AllocateHostsResultTypeDef",
    ) -> "dc_td.AllocateHostsResult":
        return dc_td.AllocateHostsResult.make_one(res)

    def allocate_ipam_pool_cidr(
        self,
        res: "bs_td.AllocateIpamPoolCidrResultTypeDef",
    ) -> "dc_td.AllocateIpamPoolCidrResult":
        return dc_td.AllocateIpamPoolCidrResult.make_one(res)

    def apply_security_groups_to_client_vpn_target_network(
        self,
        res: "bs_td.ApplySecurityGroupsToClientVpnTargetNetworkResultTypeDef",
    ) -> "dc_td.ApplySecurityGroupsToClientVpnTargetNetworkResult":
        return dc_td.ApplySecurityGroupsToClientVpnTargetNetworkResult.make_one(res)

    def assign_ipv6_addresses(
        self,
        res: "bs_td.AssignIpv6AddressesResultTypeDef",
    ) -> "dc_td.AssignIpv6AddressesResult":
        return dc_td.AssignIpv6AddressesResult.make_one(res)

    def assign_private_ip_addresses(
        self,
        res: "bs_td.AssignPrivateIpAddressesResultTypeDef",
    ) -> "dc_td.AssignPrivateIpAddressesResult":
        return dc_td.AssignPrivateIpAddressesResult.make_one(res)

    def assign_private_nat_gateway_address(
        self,
        res: "bs_td.AssignPrivateNatGatewayAddressResultTypeDef",
    ) -> "dc_td.AssignPrivateNatGatewayAddressResult":
        return dc_td.AssignPrivateNatGatewayAddressResult.make_one(res)

    def associate_address(
        self,
        res: "bs_td.AssociateAddressResultTypeDef",
    ) -> "dc_td.AssociateAddressResult":
        return dc_td.AssociateAddressResult.make_one(res)

    def associate_capacity_reservation_billing_owner(
        self,
        res: "bs_td.AssociateCapacityReservationBillingOwnerResultTypeDef",
    ) -> "dc_td.AssociateCapacityReservationBillingOwnerResult":
        return dc_td.AssociateCapacityReservationBillingOwnerResult.make_one(res)

    def associate_client_vpn_target_network(
        self,
        res: "bs_td.AssociateClientVpnTargetNetworkResultTypeDef",
    ) -> "dc_td.AssociateClientVpnTargetNetworkResult":
        return dc_td.AssociateClientVpnTargetNetworkResult.make_one(res)

    def associate_dhcp_options(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def associate_enclave_certificate_iam_role(
        self,
        res: "bs_td.AssociateEnclaveCertificateIamRoleResultTypeDef",
    ) -> "dc_td.AssociateEnclaveCertificateIamRoleResult":
        return dc_td.AssociateEnclaveCertificateIamRoleResult.make_one(res)

    def associate_iam_instance_profile(
        self,
        res: "bs_td.AssociateIamInstanceProfileResultTypeDef",
    ) -> "dc_td.AssociateIamInstanceProfileResult":
        return dc_td.AssociateIamInstanceProfileResult.make_one(res)

    def associate_instance_event_window(
        self,
        res: "bs_td.AssociateInstanceEventWindowResultTypeDef",
    ) -> "dc_td.AssociateInstanceEventWindowResult":
        return dc_td.AssociateInstanceEventWindowResult.make_one(res)

    def associate_ipam_byoasn(
        self,
        res: "bs_td.AssociateIpamByoasnResultTypeDef",
    ) -> "dc_td.AssociateIpamByoasnResult":
        return dc_td.AssociateIpamByoasnResult.make_one(res)

    def associate_ipam_resource_discovery(
        self,
        res: "bs_td.AssociateIpamResourceDiscoveryResultTypeDef",
    ) -> "dc_td.AssociateIpamResourceDiscoveryResult":
        return dc_td.AssociateIpamResourceDiscoveryResult.make_one(res)

    def associate_nat_gateway_address(
        self,
        res: "bs_td.AssociateNatGatewayAddressResultTypeDef",
    ) -> "dc_td.AssociateNatGatewayAddressResult":
        return dc_td.AssociateNatGatewayAddressResult.make_one(res)

    def associate_route_server(
        self,
        res: "bs_td.AssociateRouteServerResultTypeDef",
    ) -> "dc_td.AssociateRouteServerResult":
        return dc_td.AssociateRouteServerResult.make_one(res)

    def associate_route_table(
        self,
        res: "bs_td.AssociateRouteTableResultTypeDef",
    ) -> "dc_td.AssociateRouteTableResult":
        return dc_td.AssociateRouteTableResult.make_one(res)

    def associate_security_group_vpc(
        self,
        res: "bs_td.AssociateSecurityGroupVpcResultTypeDef",
    ) -> "dc_td.AssociateSecurityGroupVpcResult":
        return dc_td.AssociateSecurityGroupVpcResult.make_one(res)

    def associate_subnet_cidr_block(
        self,
        res: "bs_td.AssociateSubnetCidrBlockResultTypeDef",
    ) -> "dc_td.AssociateSubnetCidrBlockResult":
        return dc_td.AssociateSubnetCidrBlockResult.make_one(res)

    def associate_transit_gateway_multicast_domain(
        self,
        res: "bs_td.AssociateTransitGatewayMulticastDomainResultTypeDef",
    ) -> "dc_td.AssociateTransitGatewayMulticastDomainResult":
        return dc_td.AssociateTransitGatewayMulticastDomainResult.make_one(res)

    def associate_transit_gateway_policy_table(
        self,
        res: "bs_td.AssociateTransitGatewayPolicyTableResultTypeDef",
    ) -> "dc_td.AssociateTransitGatewayPolicyTableResult":
        return dc_td.AssociateTransitGatewayPolicyTableResult.make_one(res)

    def associate_transit_gateway_route_table(
        self,
        res: "bs_td.AssociateTransitGatewayRouteTableResultTypeDef",
    ) -> "dc_td.AssociateTransitGatewayRouteTableResult":
        return dc_td.AssociateTransitGatewayRouteTableResult.make_one(res)

    def associate_trunk_interface(
        self,
        res: "bs_td.AssociateTrunkInterfaceResultTypeDef",
    ) -> "dc_td.AssociateTrunkInterfaceResult":
        return dc_td.AssociateTrunkInterfaceResult.make_one(res)

    def associate_vpc_cidr_block(
        self,
        res: "bs_td.AssociateVpcCidrBlockResultTypeDef",
    ) -> "dc_td.AssociateVpcCidrBlockResult":
        return dc_td.AssociateVpcCidrBlockResult.make_one(res)

    def attach_classic_link_vpc(
        self,
        res: "bs_td.AttachClassicLinkVpcResultTypeDef",
    ) -> "dc_td.AttachClassicLinkVpcResult":
        return dc_td.AttachClassicLinkVpcResult.make_one(res)

    def attach_internet_gateway(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def attach_network_interface(
        self,
        res: "bs_td.AttachNetworkInterfaceResultTypeDef",
    ) -> "dc_td.AttachNetworkInterfaceResult":
        return dc_td.AttachNetworkInterfaceResult.make_one(res)

    def attach_verified_access_trust_provider(
        self,
        res: "bs_td.AttachVerifiedAccessTrustProviderResultTypeDef",
    ) -> "dc_td.AttachVerifiedAccessTrustProviderResult":
        return dc_td.AttachVerifiedAccessTrustProviderResult.make_one(res)

    def attach_volume(
        self,
        res: "bs_td.VolumeAttachmentResponseTypeDef",
    ) -> "dc_td.VolumeAttachmentResponse":
        return dc_td.VolumeAttachmentResponse.make_one(res)

    def attach_vpn_gateway(
        self,
        res: "bs_td.AttachVpnGatewayResultTypeDef",
    ) -> "dc_td.AttachVpnGatewayResult":
        return dc_td.AttachVpnGatewayResult.make_one(res)

    def authorize_client_vpn_ingress(
        self,
        res: "bs_td.AuthorizeClientVpnIngressResultTypeDef",
    ) -> "dc_td.AuthorizeClientVpnIngressResult":
        return dc_td.AuthorizeClientVpnIngressResult.make_one(res)

    def authorize_security_group_egress(
        self,
        res: "bs_td.AuthorizeSecurityGroupEgressResultTypeDef",
    ) -> "dc_td.AuthorizeSecurityGroupEgressResult":
        return dc_td.AuthorizeSecurityGroupEgressResult.make_one(res)

    def authorize_security_group_ingress(
        self,
        res: "bs_td.AuthorizeSecurityGroupIngressResultTypeDef",
    ) -> "dc_td.AuthorizeSecurityGroupIngressResult":
        return dc_td.AuthorizeSecurityGroupIngressResult.make_one(res)

    def bundle_instance(
        self,
        res: "bs_td.BundleInstanceResultTypeDef",
    ) -> "dc_td.BundleInstanceResult":
        return dc_td.BundleInstanceResult.make_one(res)

    def cancel_bundle_task(
        self,
        res: "bs_td.CancelBundleTaskResultTypeDef",
    ) -> "dc_td.CancelBundleTaskResult":
        return dc_td.CancelBundleTaskResult.make_one(res)

    def cancel_capacity_reservation(
        self,
        res: "bs_td.CancelCapacityReservationResultTypeDef",
    ) -> "dc_td.CancelCapacityReservationResult":
        return dc_td.CancelCapacityReservationResult.make_one(res)

    def cancel_capacity_reservation_fleets(
        self,
        res: "bs_td.CancelCapacityReservationFleetsResultTypeDef",
    ) -> "dc_td.CancelCapacityReservationFleetsResult":
        return dc_td.CancelCapacityReservationFleetsResult.make_one(res)

    def cancel_conversion_task(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def cancel_declarative_policies_report(
        self,
        res: "bs_td.CancelDeclarativePoliciesReportResultTypeDef",
    ) -> "dc_td.CancelDeclarativePoliciesReportResult":
        return dc_td.CancelDeclarativePoliciesReportResult.make_one(res)

    def cancel_export_task(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def cancel_image_launch_permission(
        self,
        res: "bs_td.CancelImageLaunchPermissionResultTypeDef",
    ) -> "dc_td.CancelImageLaunchPermissionResult":
        return dc_td.CancelImageLaunchPermissionResult.make_one(res)

    def cancel_import_task(
        self,
        res: "bs_td.CancelImportTaskResultTypeDef",
    ) -> "dc_td.CancelImportTaskResult":
        return dc_td.CancelImportTaskResult.make_one(res)

    def cancel_reserved_instances_listing(
        self,
        res: "bs_td.CancelReservedInstancesListingResultTypeDef",
    ) -> "dc_td.CancelReservedInstancesListingResult":
        return dc_td.CancelReservedInstancesListingResult.make_one(res)

    def cancel_spot_fleet_requests(
        self,
        res: "bs_td.CancelSpotFleetRequestsResponseTypeDef",
    ) -> "dc_td.CancelSpotFleetRequestsResponse":
        return dc_td.CancelSpotFleetRequestsResponse.make_one(res)

    def cancel_spot_instance_requests(
        self,
        res: "bs_td.CancelSpotInstanceRequestsResultTypeDef",
    ) -> "dc_td.CancelSpotInstanceRequestsResult":
        return dc_td.CancelSpotInstanceRequestsResult.make_one(res)

    def confirm_product_instance(
        self,
        res: "bs_td.ConfirmProductInstanceResultTypeDef",
    ) -> "dc_td.ConfirmProductInstanceResult":
        return dc_td.ConfirmProductInstanceResult.make_one(res)

    def copy_fpga_image(
        self,
        res: "bs_td.CopyFpgaImageResultTypeDef",
    ) -> "dc_td.CopyFpgaImageResult":
        return dc_td.CopyFpgaImageResult.make_one(res)

    def copy_image(
        self,
        res: "bs_td.CopyImageResultTypeDef",
    ) -> "dc_td.CopyImageResult":
        return dc_td.CopyImageResult.make_one(res)

    def copy_snapshot(
        self,
        res: "bs_td.CopySnapshotResultTypeDef",
    ) -> "dc_td.CopySnapshotResult":
        return dc_td.CopySnapshotResult.make_one(res)

    def create_capacity_reservation(
        self,
        res: "bs_td.CreateCapacityReservationResultTypeDef",
    ) -> "dc_td.CreateCapacityReservationResult":
        return dc_td.CreateCapacityReservationResult.make_one(res)

    def create_capacity_reservation_by_splitting(
        self,
        res: "bs_td.CreateCapacityReservationBySplittingResultTypeDef",
    ) -> "dc_td.CreateCapacityReservationBySplittingResult":
        return dc_td.CreateCapacityReservationBySplittingResult.make_one(res)

    def create_capacity_reservation_fleet(
        self,
        res: "bs_td.CreateCapacityReservationFleetResultTypeDef",
    ) -> "dc_td.CreateCapacityReservationFleetResult":
        return dc_td.CreateCapacityReservationFleetResult.make_one(res)

    def create_carrier_gateway(
        self,
        res: "bs_td.CreateCarrierGatewayResultTypeDef",
    ) -> "dc_td.CreateCarrierGatewayResult":
        return dc_td.CreateCarrierGatewayResult.make_one(res)

    def create_client_vpn_endpoint(
        self,
        res: "bs_td.CreateClientVpnEndpointResultTypeDef",
    ) -> "dc_td.CreateClientVpnEndpointResult":
        return dc_td.CreateClientVpnEndpointResult.make_one(res)

    def create_client_vpn_route(
        self,
        res: "bs_td.CreateClientVpnRouteResultTypeDef",
    ) -> "dc_td.CreateClientVpnRouteResult":
        return dc_td.CreateClientVpnRouteResult.make_one(res)

    def create_coip_cidr(
        self,
        res: "bs_td.CreateCoipCidrResultTypeDef",
    ) -> "dc_td.CreateCoipCidrResult":
        return dc_td.CreateCoipCidrResult.make_one(res)

    def create_coip_pool(
        self,
        res: "bs_td.CreateCoipPoolResultTypeDef",
    ) -> "dc_td.CreateCoipPoolResult":
        return dc_td.CreateCoipPoolResult.make_one(res)

    def create_customer_gateway(
        self,
        res: "bs_td.CreateCustomerGatewayResultTypeDef",
    ) -> "dc_td.CreateCustomerGatewayResult":
        return dc_td.CreateCustomerGatewayResult.make_one(res)

    def create_default_subnet(
        self,
        res: "bs_td.CreateDefaultSubnetResultTypeDef",
    ) -> "dc_td.CreateDefaultSubnetResult":
        return dc_td.CreateDefaultSubnetResult.make_one(res)

    def create_default_vpc(
        self,
        res: "bs_td.CreateDefaultVpcResultTypeDef",
    ) -> "dc_td.CreateDefaultVpcResult":
        return dc_td.CreateDefaultVpcResult.make_one(res)

    def create_delegate_mac_volume_ownership_task(
        self,
        res: "bs_td.CreateDelegateMacVolumeOwnershipTaskResultTypeDef",
    ) -> "dc_td.CreateDelegateMacVolumeOwnershipTaskResult":
        return dc_td.CreateDelegateMacVolumeOwnershipTaskResult.make_one(res)

    def create_dhcp_options(
        self,
        res: "bs_td.CreateDhcpOptionsResultTypeDef",
    ) -> "dc_td.CreateDhcpOptionsResult":
        return dc_td.CreateDhcpOptionsResult.make_one(res)

    def create_egress_only_internet_gateway(
        self,
        res: "bs_td.CreateEgressOnlyInternetGatewayResultTypeDef",
    ) -> "dc_td.CreateEgressOnlyInternetGatewayResult":
        return dc_td.CreateEgressOnlyInternetGatewayResult.make_one(res)

    def create_fleet(
        self,
        res: "bs_td.CreateFleetResultTypeDef",
    ) -> "dc_td.CreateFleetResult":
        return dc_td.CreateFleetResult.make_one(res)

    def create_flow_logs(
        self,
        res: "bs_td.CreateFlowLogsResultTypeDef",
    ) -> "dc_td.CreateFlowLogsResult":
        return dc_td.CreateFlowLogsResult.make_one(res)

    def create_fpga_image(
        self,
        res: "bs_td.CreateFpgaImageResultTypeDef",
    ) -> "dc_td.CreateFpgaImageResult":
        return dc_td.CreateFpgaImageResult.make_one(res)

    def create_image(
        self,
        res: "bs_td.CreateImageResultTypeDef",
    ) -> "dc_td.CreateImageResult":
        return dc_td.CreateImageResult.make_one(res)

    def create_image_usage_report(
        self,
        res: "bs_td.CreateImageUsageReportResultTypeDef",
    ) -> "dc_td.CreateImageUsageReportResult":
        return dc_td.CreateImageUsageReportResult.make_one(res)

    def create_instance_connect_endpoint(
        self,
        res: "bs_td.CreateInstanceConnectEndpointResultTypeDef",
    ) -> "dc_td.CreateInstanceConnectEndpointResult":
        return dc_td.CreateInstanceConnectEndpointResult.make_one(res)

    def create_instance_event_window(
        self,
        res: "bs_td.CreateInstanceEventWindowResultTypeDef",
    ) -> "dc_td.CreateInstanceEventWindowResult":
        return dc_td.CreateInstanceEventWindowResult.make_one(res)

    def create_instance_export_task(
        self,
        res: "bs_td.CreateInstanceExportTaskResultTypeDef",
    ) -> "dc_td.CreateInstanceExportTaskResult":
        return dc_td.CreateInstanceExportTaskResult.make_one(res)

    def create_internet_gateway(
        self,
        res: "bs_td.CreateInternetGatewayResultTypeDef",
    ) -> "dc_td.CreateInternetGatewayResult":
        return dc_td.CreateInternetGatewayResult.make_one(res)

    def create_ipam(
        self,
        res: "bs_td.CreateIpamResultTypeDef",
    ) -> "dc_td.CreateIpamResult":
        return dc_td.CreateIpamResult.make_one(res)

    def create_ipam_external_resource_verification_token(
        self,
        res: "bs_td.CreateIpamExternalResourceVerificationTokenResultTypeDef",
    ) -> "dc_td.CreateIpamExternalResourceVerificationTokenResult":
        return dc_td.CreateIpamExternalResourceVerificationTokenResult.make_one(res)

    def create_ipam_pool(
        self,
        res: "bs_td.CreateIpamPoolResultTypeDef",
    ) -> "dc_td.CreateIpamPoolResult":
        return dc_td.CreateIpamPoolResult.make_one(res)

    def create_ipam_resource_discovery(
        self,
        res: "bs_td.CreateIpamResourceDiscoveryResultTypeDef",
    ) -> "dc_td.CreateIpamResourceDiscoveryResult":
        return dc_td.CreateIpamResourceDiscoveryResult.make_one(res)

    def create_ipam_scope(
        self,
        res: "bs_td.CreateIpamScopeResultTypeDef",
    ) -> "dc_td.CreateIpamScopeResult":
        return dc_td.CreateIpamScopeResult.make_one(res)

    def create_key_pair(
        self,
        res: "bs_td.KeyPairTypeDef",
    ) -> "dc_td.KeyPair":
        return dc_td.KeyPair.make_one(res)

    def create_launch_template(
        self,
        res: "bs_td.CreateLaunchTemplateResultTypeDef",
    ) -> "dc_td.CreateLaunchTemplateResult":
        return dc_td.CreateLaunchTemplateResult.make_one(res)

    def create_launch_template_version(
        self,
        res: "bs_td.CreateLaunchTemplateVersionResultTypeDef",
    ) -> "dc_td.CreateLaunchTemplateVersionResult":
        return dc_td.CreateLaunchTemplateVersionResult.make_one(res)

    def create_local_gateway_route(
        self,
        res: "bs_td.CreateLocalGatewayRouteResultTypeDef",
    ) -> "dc_td.CreateLocalGatewayRouteResult":
        return dc_td.CreateLocalGatewayRouteResult.make_one(res)

    def create_local_gateway_route_table(
        self,
        res: "bs_td.CreateLocalGatewayRouteTableResultTypeDef",
    ) -> "dc_td.CreateLocalGatewayRouteTableResult":
        return dc_td.CreateLocalGatewayRouteTableResult.make_one(res)

    def create_local_gateway_route_table_virtual_interface_group_association(
        self,
        res: "bs_td.CreateLocalGatewayRouteTableVirtualInterfaceGroupAssociationResultTypeDef",
    ) -> "dc_td.CreateLocalGatewayRouteTableVirtualInterfaceGroupAssociationResult":
        return dc_td.CreateLocalGatewayRouteTableVirtualInterfaceGroupAssociationResult.make_one(
            res
        )

    def create_local_gateway_route_table_vpc_association(
        self,
        res: "bs_td.CreateLocalGatewayRouteTableVpcAssociationResultTypeDef",
    ) -> "dc_td.CreateLocalGatewayRouteTableVpcAssociationResult":
        return dc_td.CreateLocalGatewayRouteTableVpcAssociationResult.make_one(res)

    def create_local_gateway_virtual_interface(
        self,
        res: "bs_td.CreateLocalGatewayVirtualInterfaceResultTypeDef",
    ) -> "dc_td.CreateLocalGatewayVirtualInterfaceResult":
        return dc_td.CreateLocalGatewayVirtualInterfaceResult.make_one(res)

    def create_local_gateway_virtual_interface_group(
        self,
        res: "bs_td.CreateLocalGatewayVirtualInterfaceGroupResultTypeDef",
    ) -> "dc_td.CreateLocalGatewayVirtualInterfaceGroupResult":
        return dc_td.CreateLocalGatewayVirtualInterfaceGroupResult.make_one(res)

    def create_mac_system_integrity_protection_modification_task(
        self,
        res: "bs_td.CreateMacSystemIntegrityProtectionModificationTaskResultTypeDef",
    ) -> "dc_td.CreateMacSystemIntegrityProtectionModificationTaskResult":
        return dc_td.CreateMacSystemIntegrityProtectionModificationTaskResult.make_one(
            res
        )

    def create_managed_prefix_list(
        self,
        res: "bs_td.CreateManagedPrefixListResultTypeDef",
    ) -> "dc_td.CreateManagedPrefixListResult":
        return dc_td.CreateManagedPrefixListResult.make_one(res)

    def create_nat_gateway(
        self,
        res: "bs_td.CreateNatGatewayResultTypeDef",
    ) -> "dc_td.CreateNatGatewayResult":
        return dc_td.CreateNatGatewayResult.make_one(res)

    def create_network_acl(
        self,
        res: "bs_td.CreateNetworkAclResultTypeDef",
    ) -> "dc_td.CreateNetworkAclResult":
        return dc_td.CreateNetworkAclResult.make_one(res)

    def create_network_acl_entry(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def create_network_insights_access_scope(
        self,
        res: "bs_td.CreateNetworkInsightsAccessScopeResultTypeDef",
    ) -> "dc_td.CreateNetworkInsightsAccessScopeResult":
        return dc_td.CreateNetworkInsightsAccessScopeResult.make_one(res)

    def create_network_insights_path(
        self,
        res: "bs_td.CreateNetworkInsightsPathResultTypeDef",
    ) -> "dc_td.CreateNetworkInsightsPathResult":
        return dc_td.CreateNetworkInsightsPathResult.make_one(res)

    def create_network_interface(
        self,
        res: "bs_td.CreateNetworkInterfaceResultTypeDef",
    ) -> "dc_td.CreateNetworkInterfaceResult":
        return dc_td.CreateNetworkInterfaceResult.make_one(res)

    def create_network_interface_permission(
        self,
        res: "bs_td.CreateNetworkInterfacePermissionResultTypeDef",
    ) -> "dc_td.CreateNetworkInterfacePermissionResult":
        return dc_td.CreateNetworkInterfacePermissionResult.make_one(res)

    def create_placement_group(
        self,
        res: "bs_td.CreatePlacementGroupResultTypeDef",
    ) -> "dc_td.CreatePlacementGroupResult":
        return dc_td.CreatePlacementGroupResult.make_one(res)

    def create_public_ipv4_pool(
        self,
        res: "bs_td.CreatePublicIpv4PoolResultTypeDef",
    ) -> "dc_td.CreatePublicIpv4PoolResult":
        return dc_td.CreatePublicIpv4PoolResult.make_one(res)

    def create_replace_root_volume_task(
        self,
        res: "bs_td.CreateReplaceRootVolumeTaskResultTypeDef",
    ) -> "dc_td.CreateReplaceRootVolumeTaskResult":
        return dc_td.CreateReplaceRootVolumeTaskResult.make_one(res)

    def create_reserved_instances_listing(
        self,
        res: "bs_td.CreateReservedInstancesListingResultTypeDef",
    ) -> "dc_td.CreateReservedInstancesListingResult":
        return dc_td.CreateReservedInstancesListingResult.make_one(res)

    def create_restore_image_task(
        self,
        res: "bs_td.CreateRestoreImageTaskResultTypeDef",
    ) -> "dc_td.CreateRestoreImageTaskResult":
        return dc_td.CreateRestoreImageTaskResult.make_one(res)

    def create_route(
        self,
        res: "bs_td.CreateRouteResultTypeDef",
    ) -> "dc_td.CreateRouteResult":
        return dc_td.CreateRouteResult.make_one(res)

    def create_route_server(
        self,
        res: "bs_td.CreateRouteServerResultTypeDef",
    ) -> "dc_td.CreateRouteServerResult":
        return dc_td.CreateRouteServerResult.make_one(res)

    def create_route_server_endpoint(
        self,
        res: "bs_td.CreateRouteServerEndpointResultTypeDef",
    ) -> "dc_td.CreateRouteServerEndpointResult":
        return dc_td.CreateRouteServerEndpointResult.make_one(res)

    def create_route_server_peer(
        self,
        res: "bs_td.CreateRouteServerPeerResultTypeDef",
    ) -> "dc_td.CreateRouteServerPeerResult":
        return dc_td.CreateRouteServerPeerResult.make_one(res)

    def create_route_table(
        self,
        res: "bs_td.CreateRouteTableResultTypeDef",
    ) -> "dc_td.CreateRouteTableResult":
        return dc_td.CreateRouteTableResult.make_one(res)

    def create_security_group(
        self,
        res: "bs_td.CreateSecurityGroupResultTypeDef",
    ) -> "dc_td.CreateSecurityGroupResult":
        return dc_td.CreateSecurityGroupResult.make_one(res)

    def create_snapshot(
        self,
        res: "bs_td.SnapshotResponseTypeDef",
    ) -> "dc_td.SnapshotResponse":
        return dc_td.SnapshotResponse.make_one(res)

    def create_snapshots(
        self,
        res: "bs_td.CreateSnapshotsResultTypeDef",
    ) -> "dc_td.CreateSnapshotsResult":
        return dc_td.CreateSnapshotsResult.make_one(res)

    def create_spot_datafeed_subscription(
        self,
        res: "bs_td.CreateSpotDatafeedSubscriptionResultTypeDef",
    ) -> "dc_td.CreateSpotDatafeedSubscriptionResult":
        return dc_td.CreateSpotDatafeedSubscriptionResult.make_one(res)

    def create_store_image_task(
        self,
        res: "bs_td.CreateStoreImageTaskResultTypeDef",
    ) -> "dc_td.CreateStoreImageTaskResult":
        return dc_td.CreateStoreImageTaskResult.make_one(res)

    def create_subnet(
        self,
        res: "bs_td.CreateSubnetResultTypeDef",
    ) -> "dc_td.CreateSubnetResult":
        return dc_td.CreateSubnetResult.make_one(res)

    def create_subnet_cidr_reservation(
        self,
        res: "bs_td.CreateSubnetCidrReservationResultTypeDef",
    ) -> "dc_td.CreateSubnetCidrReservationResult":
        return dc_td.CreateSubnetCidrReservationResult.make_one(res)

    def create_traffic_mirror_filter(
        self,
        res: "bs_td.CreateTrafficMirrorFilterResultTypeDef",
    ) -> "dc_td.CreateTrafficMirrorFilterResult":
        return dc_td.CreateTrafficMirrorFilterResult.make_one(res)

    def create_traffic_mirror_filter_rule(
        self,
        res: "bs_td.CreateTrafficMirrorFilterRuleResultTypeDef",
    ) -> "dc_td.CreateTrafficMirrorFilterRuleResult":
        return dc_td.CreateTrafficMirrorFilterRuleResult.make_one(res)

    def create_traffic_mirror_session(
        self,
        res: "bs_td.CreateTrafficMirrorSessionResultTypeDef",
    ) -> "dc_td.CreateTrafficMirrorSessionResult":
        return dc_td.CreateTrafficMirrorSessionResult.make_one(res)

    def create_traffic_mirror_target(
        self,
        res: "bs_td.CreateTrafficMirrorTargetResultTypeDef",
    ) -> "dc_td.CreateTrafficMirrorTargetResult":
        return dc_td.CreateTrafficMirrorTargetResult.make_one(res)

    def create_transit_gateway(
        self,
        res: "bs_td.CreateTransitGatewayResultTypeDef",
    ) -> "dc_td.CreateTransitGatewayResult":
        return dc_td.CreateTransitGatewayResult.make_one(res)

    def create_transit_gateway_connect(
        self,
        res: "bs_td.CreateTransitGatewayConnectResultTypeDef",
    ) -> "dc_td.CreateTransitGatewayConnectResult":
        return dc_td.CreateTransitGatewayConnectResult.make_one(res)

    def create_transit_gateway_connect_peer(
        self,
        res: "bs_td.CreateTransitGatewayConnectPeerResultTypeDef",
    ) -> "dc_td.CreateTransitGatewayConnectPeerResult":
        return dc_td.CreateTransitGatewayConnectPeerResult.make_one(res)

    def create_transit_gateway_multicast_domain(
        self,
        res: "bs_td.CreateTransitGatewayMulticastDomainResultTypeDef",
    ) -> "dc_td.CreateTransitGatewayMulticastDomainResult":
        return dc_td.CreateTransitGatewayMulticastDomainResult.make_one(res)

    def create_transit_gateway_peering_attachment(
        self,
        res: "bs_td.CreateTransitGatewayPeeringAttachmentResultTypeDef",
    ) -> "dc_td.CreateTransitGatewayPeeringAttachmentResult":
        return dc_td.CreateTransitGatewayPeeringAttachmentResult.make_one(res)

    def create_transit_gateway_policy_table(
        self,
        res: "bs_td.CreateTransitGatewayPolicyTableResultTypeDef",
    ) -> "dc_td.CreateTransitGatewayPolicyTableResult":
        return dc_td.CreateTransitGatewayPolicyTableResult.make_one(res)

    def create_transit_gateway_prefix_list_reference(
        self,
        res: "bs_td.CreateTransitGatewayPrefixListReferenceResultTypeDef",
    ) -> "dc_td.CreateTransitGatewayPrefixListReferenceResult":
        return dc_td.CreateTransitGatewayPrefixListReferenceResult.make_one(res)

    def create_transit_gateway_route(
        self,
        res: "bs_td.CreateTransitGatewayRouteResultTypeDef",
    ) -> "dc_td.CreateTransitGatewayRouteResult":
        return dc_td.CreateTransitGatewayRouteResult.make_one(res)

    def create_transit_gateway_route_table(
        self,
        res: "bs_td.CreateTransitGatewayRouteTableResultTypeDef",
    ) -> "dc_td.CreateTransitGatewayRouteTableResult":
        return dc_td.CreateTransitGatewayRouteTableResult.make_one(res)

    def create_transit_gateway_route_table_announcement(
        self,
        res: "bs_td.CreateTransitGatewayRouteTableAnnouncementResultTypeDef",
    ) -> "dc_td.CreateTransitGatewayRouteTableAnnouncementResult":
        return dc_td.CreateTransitGatewayRouteTableAnnouncementResult.make_one(res)

    def create_transit_gateway_vpc_attachment(
        self,
        res: "bs_td.CreateTransitGatewayVpcAttachmentResultTypeDef",
    ) -> "dc_td.CreateTransitGatewayVpcAttachmentResult":
        return dc_td.CreateTransitGatewayVpcAttachmentResult.make_one(res)

    def create_verified_access_endpoint(
        self,
        res: "bs_td.CreateVerifiedAccessEndpointResultTypeDef",
    ) -> "dc_td.CreateVerifiedAccessEndpointResult":
        return dc_td.CreateVerifiedAccessEndpointResult.make_one(res)

    def create_verified_access_group(
        self,
        res: "bs_td.CreateVerifiedAccessGroupResultTypeDef",
    ) -> "dc_td.CreateVerifiedAccessGroupResult":
        return dc_td.CreateVerifiedAccessGroupResult.make_one(res)

    def create_verified_access_instance(
        self,
        res: "bs_td.CreateVerifiedAccessInstanceResultTypeDef",
    ) -> "dc_td.CreateVerifiedAccessInstanceResult":
        return dc_td.CreateVerifiedAccessInstanceResult.make_one(res)

    def create_verified_access_trust_provider(
        self,
        res: "bs_td.CreateVerifiedAccessTrustProviderResultTypeDef",
    ) -> "dc_td.CreateVerifiedAccessTrustProviderResult":
        return dc_td.CreateVerifiedAccessTrustProviderResult.make_one(res)

    def create_volume(
        self,
        res: "bs_td.VolumeResponseTypeDef",
    ) -> "dc_td.VolumeResponse":
        return dc_td.VolumeResponse.make_one(res)

    def create_vpc(
        self,
        res: "bs_td.CreateVpcResultTypeDef",
    ) -> "dc_td.CreateVpcResult":
        return dc_td.CreateVpcResult.make_one(res)

    def create_vpc_block_public_access_exclusion(
        self,
        res: "bs_td.CreateVpcBlockPublicAccessExclusionResultTypeDef",
    ) -> "dc_td.CreateVpcBlockPublicAccessExclusionResult":
        return dc_td.CreateVpcBlockPublicAccessExclusionResult.make_one(res)

    def create_vpc_endpoint(
        self,
        res: "bs_td.CreateVpcEndpointResultTypeDef",
    ) -> "dc_td.CreateVpcEndpointResult":
        return dc_td.CreateVpcEndpointResult.make_one(res)

    def create_vpc_endpoint_connection_notification(
        self,
        res: "bs_td.CreateVpcEndpointConnectionNotificationResultTypeDef",
    ) -> "dc_td.CreateVpcEndpointConnectionNotificationResult":
        return dc_td.CreateVpcEndpointConnectionNotificationResult.make_one(res)

    def create_vpc_endpoint_service_configuration(
        self,
        res: "bs_td.CreateVpcEndpointServiceConfigurationResultTypeDef",
    ) -> "dc_td.CreateVpcEndpointServiceConfigurationResult":
        return dc_td.CreateVpcEndpointServiceConfigurationResult.make_one(res)

    def create_vpc_peering_connection(
        self,
        res: "bs_td.CreateVpcPeeringConnectionResultTypeDef",
    ) -> "dc_td.CreateVpcPeeringConnectionResult":
        return dc_td.CreateVpcPeeringConnectionResult.make_one(res)

    def create_vpn_connection(
        self,
        res: "bs_td.CreateVpnConnectionResultTypeDef",
    ) -> "dc_td.CreateVpnConnectionResult":
        return dc_td.CreateVpnConnectionResult.make_one(res)

    def create_vpn_connection_route(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def create_vpn_gateway(
        self,
        res: "bs_td.CreateVpnGatewayResultTypeDef",
    ) -> "dc_td.CreateVpnGatewayResult":
        return dc_td.CreateVpnGatewayResult.make_one(res)

    def delete_carrier_gateway(
        self,
        res: "bs_td.DeleteCarrierGatewayResultTypeDef",
    ) -> "dc_td.DeleteCarrierGatewayResult":
        return dc_td.DeleteCarrierGatewayResult.make_one(res)

    def delete_client_vpn_endpoint(
        self,
        res: "bs_td.DeleteClientVpnEndpointResultTypeDef",
    ) -> "dc_td.DeleteClientVpnEndpointResult":
        return dc_td.DeleteClientVpnEndpointResult.make_one(res)

    def delete_client_vpn_route(
        self,
        res: "bs_td.DeleteClientVpnRouteResultTypeDef",
    ) -> "dc_td.DeleteClientVpnRouteResult":
        return dc_td.DeleteClientVpnRouteResult.make_one(res)

    def delete_coip_cidr(
        self,
        res: "bs_td.DeleteCoipCidrResultTypeDef",
    ) -> "dc_td.DeleteCoipCidrResult":
        return dc_td.DeleteCoipCidrResult.make_one(res)

    def delete_coip_pool(
        self,
        res: "bs_td.DeleteCoipPoolResultTypeDef",
    ) -> "dc_td.DeleteCoipPoolResult":
        return dc_td.DeleteCoipPoolResult.make_one(res)

    def delete_customer_gateway(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_dhcp_options(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_egress_only_internet_gateway(
        self,
        res: "bs_td.DeleteEgressOnlyInternetGatewayResultTypeDef",
    ) -> "dc_td.DeleteEgressOnlyInternetGatewayResult":
        return dc_td.DeleteEgressOnlyInternetGatewayResult.make_one(res)

    def delete_fleets(
        self,
        res: "bs_td.DeleteFleetsResultTypeDef",
    ) -> "dc_td.DeleteFleetsResult":
        return dc_td.DeleteFleetsResult.make_one(res)

    def delete_flow_logs(
        self,
        res: "bs_td.DeleteFlowLogsResultTypeDef",
    ) -> "dc_td.DeleteFlowLogsResult":
        return dc_td.DeleteFlowLogsResult.make_one(res)

    def delete_fpga_image(
        self,
        res: "bs_td.DeleteFpgaImageResultTypeDef",
    ) -> "dc_td.DeleteFpgaImageResult":
        return dc_td.DeleteFpgaImageResult.make_one(res)

    def delete_image_usage_report(
        self,
        res: "bs_td.DeleteImageUsageReportResultTypeDef",
    ) -> "dc_td.DeleteImageUsageReportResult":
        return dc_td.DeleteImageUsageReportResult.make_one(res)

    def delete_instance_connect_endpoint(
        self,
        res: "bs_td.DeleteInstanceConnectEndpointResultTypeDef",
    ) -> "dc_td.DeleteInstanceConnectEndpointResult":
        return dc_td.DeleteInstanceConnectEndpointResult.make_one(res)

    def delete_instance_event_window(
        self,
        res: "bs_td.DeleteInstanceEventWindowResultTypeDef",
    ) -> "dc_td.DeleteInstanceEventWindowResult":
        return dc_td.DeleteInstanceEventWindowResult.make_one(res)

    def delete_internet_gateway(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_ipam(
        self,
        res: "bs_td.DeleteIpamResultTypeDef",
    ) -> "dc_td.DeleteIpamResult":
        return dc_td.DeleteIpamResult.make_one(res)

    def delete_ipam_external_resource_verification_token(
        self,
        res: "bs_td.DeleteIpamExternalResourceVerificationTokenResultTypeDef",
    ) -> "dc_td.DeleteIpamExternalResourceVerificationTokenResult":
        return dc_td.DeleteIpamExternalResourceVerificationTokenResult.make_one(res)

    def delete_ipam_pool(
        self,
        res: "bs_td.DeleteIpamPoolResultTypeDef",
    ) -> "dc_td.DeleteIpamPoolResult":
        return dc_td.DeleteIpamPoolResult.make_one(res)

    def delete_ipam_resource_discovery(
        self,
        res: "bs_td.DeleteIpamResourceDiscoveryResultTypeDef",
    ) -> "dc_td.DeleteIpamResourceDiscoveryResult":
        return dc_td.DeleteIpamResourceDiscoveryResult.make_one(res)

    def delete_ipam_scope(
        self,
        res: "bs_td.DeleteIpamScopeResultTypeDef",
    ) -> "dc_td.DeleteIpamScopeResult":
        return dc_td.DeleteIpamScopeResult.make_one(res)

    def delete_key_pair(
        self,
        res: "bs_td.DeleteKeyPairResultTypeDef",
    ) -> "dc_td.DeleteKeyPairResult":
        return dc_td.DeleteKeyPairResult.make_one(res)

    def delete_launch_template(
        self,
        res: "bs_td.DeleteLaunchTemplateResultTypeDef",
    ) -> "dc_td.DeleteLaunchTemplateResult":
        return dc_td.DeleteLaunchTemplateResult.make_one(res)

    def delete_launch_template_versions(
        self,
        res: "bs_td.DeleteLaunchTemplateVersionsResultTypeDef",
    ) -> "dc_td.DeleteLaunchTemplateVersionsResult":
        return dc_td.DeleteLaunchTemplateVersionsResult.make_one(res)

    def delete_local_gateway_route(
        self,
        res: "bs_td.DeleteLocalGatewayRouteResultTypeDef",
    ) -> "dc_td.DeleteLocalGatewayRouteResult":
        return dc_td.DeleteLocalGatewayRouteResult.make_one(res)

    def delete_local_gateway_route_table(
        self,
        res: "bs_td.DeleteLocalGatewayRouteTableResultTypeDef",
    ) -> "dc_td.DeleteLocalGatewayRouteTableResult":
        return dc_td.DeleteLocalGatewayRouteTableResult.make_one(res)

    def delete_local_gateway_route_table_virtual_interface_group_association(
        self,
        res: "bs_td.DeleteLocalGatewayRouteTableVirtualInterfaceGroupAssociationResultTypeDef",
    ) -> "dc_td.DeleteLocalGatewayRouteTableVirtualInterfaceGroupAssociationResult":
        return dc_td.DeleteLocalGatewayRouteTableVirtualInterfaceGroupAssociationResult.make_one(
            res
        )

    def delete_local_gateway_route_table_vpc_association(
        self,
        res: "bs_td.DeleteLocalGatewayRouteTableVpcAssociationResultTypeDef",
    ) -> "dc_td.DeleteLocalGatewayRouteTableVpcAssociationResult":
        return dc_td.DeleteLocalGatewayRouteTableVpcAssociationResult.make_one(res)

    def delete_local_gateway_virtual_interface(
        self,
        res: "bs_td.DeleteLocalGatewayVirtualInterfaceResultTypeDef",
    ) -> "dc_td.DeleteLocalGatewayVirtualInterfaceResult":
        return dc_td.DeleteLocalGatewayVirtualInterfaceResult.make_one(res)

    def delete_local_gateway_virtual_interface_group(
        self,
        res: "bs_td.DeleteLocalGatewayVirtualInterfaceGroupResultTypeDef",
    ) -> "dc_td.DeleteLocalGatewayVirtualInterfaceGroupResult":
        return dc_td.DeleteLocalGatewayVirtualInterfaceGroupResult.make_one(res)

    def delete_managed_prefix_list(
        self,
        res: "bs_td.DeleteManagedPrefixListResultTypeDef",
    ) -> "dc_td.DeleteManagedPrefixListResult":
        return dc_td.DeleteManagedPrefixListResult.make_one(res)

    def delete_nat_gateway(
        self,
        res: "bs_td.DeleteNatGatewayResultTypeDef",
    ) -> "dc_td.DeleteNatGatewayResult":
        return dc_td.DeleteNatGatewayResult.make_one(res)

    def delete_network_acl(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_network_acl_entry(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_network_insights_access_scope(
        self,
        res: "bs_td.DeleteNetworkInsightsAccessScopeResultTypeDef",
    ) -> "dc_td.DeleteNetworkInsightsAccessScopeResult":
        return dc_td.DeleteNetworkInsightsAccessScopeResult.make_one(res)

    def delete_network_insights_access_scope_analysis(
        self,
        res: "bs_td.DeleteNetworkInsightsAccessScopeAnalysisResultTypeDef",
    ) -> "dc_td.DeleteNetworkInsightsAccessScopeAnalysisResult":
        return dc_td.DeleteNetworkInsightsAccessScopeAnalysisResult.make_one(res)

    def delete_network_insights_analysis(
        self,
        res: "bs_td.DeleteNetworkInsightsAnalysisResultTypeDef",
    ) -> "dc_td.DeleteNetworkInsightsAnalysisResult":
        return dc_td.DeleteNetworkInsightsAnalysisResult.make_one(res)

    def delete_network_insights_path(
        self,
        res: "bs_td.DeleteNetworkInsightsPathResultTypeDef",
    ) -> "dc_td.DeleteNetworkInsightsPathResult":
        return dc_td.DeleteNetworkInsightsPathResult.make_one(res)

    def delete_network_interface(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_network_interface_permission(
        self,
        res: "bs_td.DeleteNetworkInterfacePermissionResultTypeDef",
    ) -> "dc_td.DeleteNetworkInterfacePermissionResult":
        return dc_td.DeleteNetworkInterfacePermissionResult.make_one(res)

    def delete_placement_group(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_public_ipv4_pool(
        self,
        res: "bs_td.DeletePublicIpv4PoolResultTypeDef",
    ) -> "dc_td.DeletePublicIpv4PoolResult":
        return dc_td.DeletePublicIpv4PoolResult.make_one(res)

    def delete_queued_reserved_instances(
        self,
        res: "bs_td.DeleteQueuedReservedInstancesResultTypeDef",
    ) -> "dc_td.DeleteQueuedReservedInstancesResult":
        return dc_td.DeleteQueuedReservedInstancesResult.make_one(res)

    def delete_route(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_route_server(
        self,
        res: "bs_td.DeleteRouteServerResultTypeDef",
    ) -> "dc_td.DeleteRouteServerResult":
        return dc_td.DeleteRouteServerResult.make_one(res)

    def delete_route_server_endpoint(
        self,
        res: "bs_td.DeleteRouteServerEndpointResultTypeDef",
    ) -> "dc_td.DeleteRouteServerEndpointResult":
        return dc_td.DeleteRouteServerEndpointResult.make_one(res)

    def delete_route_server_peer(
        self,
        res: "bs_td.DeleteRouteServerPeerResultTypeDef",
    ) -> "dc_td.DeleteRouteServerPeerResult":
        return dc_td.DeleteRouteServerPeerResult.make_one(res)

    def delete_route_table(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_security_group(
        self,
        res: "bs_td.DeleteSecurityGroupResultTypeDef",
    ) -> "dc_td.DeleteSecurityGroupResult":
        return dc_td.DeleteSecurityGroupResult.make_one(res)

    def delete_snapshot(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_spot_datafeed_subscription(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_subnet(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_subnet_cidr_reservation(
        self,
        res: "bs_td.DeleteSubnetCidrReservationResultTypeDef",
    ) -> "dc_td.DeleteSubnetCidrReservationResult":
        return dc_td.DeleteSubnetCidrReservationResult.make_one(res)

    def delete_traffic_mirror_filter(
        self,
        res: "bs_td.DeleteTrafficMirrorFilterResultTypeDef",
    ) -> "dc_td.DeleteTrafficMirrorFilterResult":
        return dc_td.DeleteTrafficMirrorFilterResult.make_one(res)

    def delete_traffic_mirror_filter_rule(
        self,
        res: "bs_td.DeleteTrafficMirrorFilterRuleResultTypeDef",
    ) -> "dc_td.DeleteTrafficMirrorFilterRuleResult":
        return dc_td.DeleteTrafficMirrorFilterRuleResult.make_one(res)

    def delete_traffic_mirror_session(
        self,
        res: "bs_td.DeleteTrafficMirrorSessionResultTypeDef",
    ) -> "dc_td.DeleteTrafficMirrorSessionResult":
        return dc_td.DeleteTrafficMirrorSessionResult.make_one(res)

    def delete_traffic_mirror_target(
        self,
        res: "bs_td.DeleteTrafficMirrorTargetResultTypeDef",
    ) -> "dc_td.DeleteTrafficMirrorTargetResult":
        return dc_td.DeleteTrafficMirrorTargetResult.make_one(res)

    def delete_transit_gateway(
        self,
        res: "bs_td.DeleteTransitGatewayResultTypeDef",
    ) -> "dc_td.DeleteTransitGatewayResult":
        return dc_td.DeleteTransitGatewayResult.make_one(res)

    def delete_transit_gateway_connect(
        self,
        res: "bs_td.DeleteTransitGatewayConnectResultTypeDef",
    ) -> "dc_td.DeleteTransitGatewayConnectResult":
        return dc_td.DeleteTransitGatewayConnectResult.make_one(res)

    def delete_transit_gateway_connect_peer(
        self,
        res: "bs_td.DeleteTransitGatewayConnectPeerResultTypeDef",
    ) -> "dc_td.DeleteTransitGatewayConnectPeerResult":
        return dc_td.DeleteTransitGatewayConnectPeerResult.make_one(res)

    def delete_transit_gateway_multicast_domain(
        self,
        res: "bs_td.DeleteTransitGatewayMulticastDomainResultTypeDef",
    ) -> "dc_td.DeleteTransitGatewayMulticastDomainResult":
        return dc_td.DeleteTransitGatewayMulticastDomainResult.make_one(res)

    def delete_transit_gateway_peering_attachment(
        self,
        res: "bs_td.DeleteTransitGatewayPeeringAttachmentResultTypeDef",
    ) -> "dc_td.DeleteTransitGatewayPeeringAttachmentResult":
        return dc_td.DeleteTransitGatewayPeeringAttachmentResult.make_one(res)

    def delete_transit_gateway_policy_table(
        self,
        res: "bs_td.DeleteTransitGatewayPolicyTableResultTypeDef",
    ) -> "dc_td.DeleteTransitGatewayPolicyTableResult":
        return dc_td.DeleteTransitGatewayPolicyTableResult.make_one(res)

    def delete_transit_gateway_prefix_list_reference(
        self,
        res: "bs_td.DeleteTransitGatewayPrefixListReferenceResultTypeDef",
    ) -> "dc_td.DeleteTransitGatewayPrefixListReferenceResult":
        return dc_td.DeleteTransitGatewayPrefixListReferenceResult.make_one(res)

    def delete_transit_gateway_route(
        self,
        res: "bs_td.DeleteTransitGatewayRouteResultTypeDef",
    ) -> "dc_td.DeleteTransitGatewayRouteResult":
        return dc_td.DeleteTransitGatewayRouteResult.make_one(res)

    def delete_transit_gateway_route_table(
        self,
        res: "bs_td.DeleteTransitGatewayRouteTableResultTypeDef",
    ) -> "dc_td.DeleteTransitGatewayRouteTableResult":
        return dc_td.DeleteTransitGatewayRouteTableResult.make_one(res)

    def delete_transit_gateway_route_table_announcement(
        self,
        res: "bs_td.DeleteTransitGatewayRouteTableAnnouncementResultTypeDef",
    ) -> "dc_td.DeleteTransitGatewayRouteTableAnnouncementResult":
        return dc_td.DeleteTransitGatewayRouteTableAnnouncementResult.make_one(res)

    def delete_transit_gateway_vpc_attachment(
        self,
        res: "bs_td.DeleteTransitGatewayVpcAttachmentResultTypeDef",
    ) -> "dc_td.DeleteTransitGatewayVpcAttachmentResult":
        return dc_td.DeleteTransitGatewayVpcAttachmentResult.make_one(res)

    def delete_verified_access_endpoint(
        self,
        res: "bs_td.DeleteVerifiedAccessEndpointResultTypeDef",
    ) -> "dc_td.DeleteVerifiedAccessEndpointResult":
        return dc_td.DeleteVerifiedAccessEndpointResult.make_one(res)

    def delete_verified_access_group(
        self,
        res: "bs_td.DeleteVerifiedAccessGroupResultTypeDef",
    ) -> "dc_td.DeleteVerifiedAccessGroupResult":
        return dc_td.DeleteVerifiedAccessGroupResult.make_one(res)

    def delete_verified_access_instance(
        self,
        res: "bs_td.DeleteVerifiedAccessInstanceResultTypeDef",
    ) -> "dc_td.DeleteVerifiedAccessInstanceResult":
        return dc_td.DeleteVerifiedAccessInstanceResult.make_one(res)

    def delete_verified_access_trust_provider(
        self,
        res: "bs_td.DeleteVerifiedAccessTrustProviderResultTypeDef",
    ) -> "dc_td.DeleteVerifiedAccessTrustProviderResult":
        return dc_td.DeleteVerifiedAccessTrustProviderResult.make_one(res)

    def delete_volume(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_vpc(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_vpc_block_public_access_exclusion(
        self,
        res: "bs_td.DeleteVpcBlockPublicAccessExclusionResultTypeDef",
    ) -> "dc_td.DeleteVpcBlockPublicAccessExclusionResult":
        return dc_td.DeleteVpcBlockPublicAccessExclusionResult.make_one(res)

    def delete_vpc_endpoint_connection_notifications(
        self,
        res: "bs_td.DeleteVpcEndpointConnectionNotificationsResultTypeDef",
    ) -> "dc_td.DeleteVpcEndpointConnectionNotificationsResult":
        return dc_td.DeleteVpcEndpointConnectionNotificationsResult.make_one(res)

    def delete_vpc_endpoint_service_configurations(
        self,
        res: "bs_td.DeleteVpcEndpointServiceConfigurationsResultTypeDef",
    ) -> "dc_td.DeleteVpcEndpointServiceConfigurationsResult":
        return dc_td.DeleteVpcEndpointServiceConfigurationsResult.make_one(res)

    def delete_vpc_endpoints(
        self,
        res: "bs_td.DeleteVpcEndpointsResultTypeDef",
    ) -> "dc_td.DeleteVpcEndpointsResult":
        return dc_td.DeleteVpcEndpointsResult.make_one(res)

    def delete_vpc_peering_connection(
        self,
        res: "bs_td.DeleteVpcPeeringConnectionResultTypeDef",
    ) -> "dc_td.DeleteVpcPeeringConnectionResult":
        return dc_td.DeleteVpcPeeringConnectionResult.make_one(res)

    def delete_vpn_connection(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_vpn_connection_route(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_vpn_gateway(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def deprovision_byoip_cidr(
        self,
        res: "bs_td.DeprovisionByoipCidrResultTypeDef",
    ) -> "dc_td.DeprovisionByoipCidrResult":
        return dc_td.DeprovisionByoipCidrResult.make_one(res)

    def deprovision_ipam_byoasn(
        self,
        res: "bs_td.DeprovisionIpamByoasnResultTypeDef",
    ) -> "dc_td.DeprovisionIpamByoasnResult":
        return dc_td.DeprovisionIpamByoasnResult.make_one(res)

    def deprovision_ipam_pool_cidr(
        self,
        res: "bs_td.DeprovisionIpamPoolCidrResultTypeDef",
    ) -> "dc_td.DeprovisionIpamPoolCidrResult":
        return dc_td.DeprovisionIpamPoolCidrResult.make_one(res)

    def deprovision_public_ipv4_pool_cidr(
        self,
        res: "bs_td.DeprovisionPublicIpv4PoolCidrResultTypeDef",
    ) -> "dc_td.DeprovisionPublicIpv4PoolCidrResult":
        return dc_td.DeprovisionPublicIpv4PoolCidrResult.make_one(res)

    def deregister_image(
        self,
        res: "bs_td.DeregisterImageResultTypeDef",
    ) -> "dc_td.DeregisterImageResult":
        return dc_td.DeregisterImageResult.make_one(res)

    def deregister_instance_event_notification_attributes(
        self,
        res: "bs_td.DeregisterInstanceEventNotificationAttributesResultTypeDef",
    ) -> "dc_td.DeregisterInstanceEventNotificationAttributesResult":
        return dc_td.DeregisterInstanceEventNotificationAttributesResult.make_one(res)

    def deregister_transit_gateway_multicast_group_members(
        self,
        res: "bs_td.DeregisterTransitGatewayMulticastGroupMembersResultTypeDef",
    ) -> "dc_td.DeregisterTransitGatewayMulticastGroupMembersResult":
        return dc_td.DeregisterTransitGatewayMulticastGroupMembersResult.make_one(res)

    def deregister_transit_gateway_multicast_group_sources(
        self,
        res: "bs_td.DeregisterTransitGatewayMulticastGroupSourcesResultTypeDef",
    ) -> "dc_td.DeregisterTransitGatewayMulticastGroupSourcesResult":
        return dc_td.DeregisterTransitGatewayMulticastGroupSourcesResult.make_one(res)

    def describe_account_attributes(
        self,
        res: "bs_td.DescribeAccountAttributesResultTypeDef",
    ) -> "dc_td.DescribeAccountAttributesResult":
        return dc_td.DescribeAccountAttributesResult.make_one(res)

    def describe_address_transfers(
        self,
        res: "bs_td.DescribeAddressTransfersResultTypeDef",
    ) -> "dc_td.DescribeAddressTransfersResult":
        return dc_td.DescribeAddressTransfersResult.make_one(res)

    def describe_addresses(
        self,
        res: "bs_td.DescribeAddressesResultTypeDef",
    ) -> "dc_td.DescribeAddressesResult":
        return dc_td.DescribeAddressesResult.make_one(res)

    def describe_addresses_attribute(
        self,
        res: "bs_td.DescribeAddressesAttributeResultTypeDef",
    ) -> "dc_td.DescribeAddressesAttributeResult":
        return dc_td.DescribeAddressesAttributeResult.make_one(res)

    def describe_aggregate_id_format(
        self,
        res: "bs_td.DescribeAggregateIdFormatResultTypeDef",
    ) -> "dc_td.DescribeAggregateIdFormatResult":
        return dc_td.DescribeAggregateIdFormatResult.make_one(res)

    def describe_availability_zones(
        self,
        res: "bs_td.DescribeAvailabilityZonesResultTypeDef",
    ) -> "dc_td.DescribeAvailabilityZonesResult":
        return dc_td.DescribeAvailabilityZonesResult.make_one(res)

    def describe_aws_network_performance_metric_subscriptions(
        self,
        res: "bs_td.DescribeAwsNetworkPerformanceMetricSubscriptionsResultTypeDef",
    ) -> "dc_td.DescribeAwsNetworkPerformanceMetricSubscriptionsResult":
        return dc_td.DescribeAwsNetworkPerformanceMetricSubscriptionsResult.make_one(
            res
        )

    def describe_bundle_tasks(
        self,
        res: "bs_td.DescribeBundleTasksResultTypeDef",
    ) -> "dc_td.DescribeBundleTasksResult":
        return dc_td.DescribeBundleTasksResult.make_one(res)

    def describe_byoip_cidrs(
        self,
        res: "bs_td.DescribeByoipCidrsResultTypeDef",
    ) -> "dc_td.DescribeByoipCidrsResult":
        return dc_td.DescribeByoipCidrsResult.make_one(res)

    def describe_capacity_block_extension_history(
        self,
        res: "bs_td.DescribeCapacityBlockExtensionHistoryResultTypeDef",
    ) -> "dc_td.DescribeCapacityBlockExtensionHistoryResult":
        return dc_td.DescribeCapacityBlockExtensionHistoryResult.make_one(res)

    def describe_capacity_block_extension_offerings(
        self,
        res: "bs_td.DescribeCapacityBlockExtensionOfferingsResultTypeDef",
    ) -> "dc_td.DescribeCapacityBlockExtensionOfferingsResult":
        return dc_td.DescribeCapacityBlockExtensionOfferingsResult.make_one(res)

    def describe_capacity_block_offerings(
        self,
        res: "bs_td.DescribeCapacityBlockOfferingsResultTypeDef",
    ) -> "dc_td.DescribeCapacityBlockOfferingsResult":
        return dc_td.DescribeCapacityBlockOfferingsResult.make_one(res)

    def describe_capacity_block_status(
        self,
        res: "bs_td.DescribeCapacityBlockStatusResultTypeDef",
    ) -> "dc_td.DescribeCapacityBlockStatusResult":
        return dc_td.DescribeCapacityBlockStatusResult.make_one(res)

    def describe_capacity_blocks(
        self,
        res: "bs_td.DescribeCapacityBlocksResultTypeDef",
    ) -> "dc_td.DescribeCapacityBlocksResult":
        return dc_td.DescribeCapacityBlocksResult.make_one(res)

    def describe_capacity_reservation_billing_requests(
        self,
        res: "bs_td.DescribeCapacityReservationBillingRequestsResultTypeDef",
    ) -> "dc_td.DescribeCapacityReservationBillingRequestsResult":
        return dc_td.DescribeCapacityReservationBillingRequestsResult.make_one(res)

    def describe_capacity_reservation_fleets(
        self,
        res: "bs_td.DescribeCapacityReservationFleetsResultTypeDef",
    ) -> "dc_td.DescribeCapacityReservationFleetsResult":
        return dc_td.DescribeCapacityReservationFleetsResult.make_one(res)

    def describe_capacity_reservations(
        self,
        res: "bs_td.DescribeCapacityReservationsResultTypeDef",
    ) -> "dc_td.DescribeCapacityReservationsResult":
        return dc_td.DescribeCapacityReservationsResult.make_one(res)

    def describe_carrier_gateways(
        self,
        res: "bs_td.DescribeCarrierGatewaysResultTypeDef",
    ) -> "dc_td.DescribeCarrierGatewaysResult":
        return dc_td.DescribeCarrierGatewaysResult.make_one(res)

    def describe_classic_link_instances(
        self,
        res: "bs_td.DescribeClassicLinkInstancesResultTypeDef",
    ) -> "dc_td.DescribeClassicLinkInstancesResult":
        return dc_td.DescribeClassicLinkInstancesResult.make_one(res)

    def describe_client_vpn_authorization_rules(
        self,
        res: "bs_td.DescribeClientVpnAuthorizationRulesResultTypeDef",
    ) -> "dc_td.DescribeClientVpnAuthorizationRulesResult":
        return dc_td.DescribeClientVpnAuthorizationRulesResult.make_one(res)

    def describe_client_vpn_connections(
        self,
        res: "bs_td.DescribeClientVpnConnectionsResultTypeDef",
    ) -> "dc_td.DescribeClientVpnConnectionsResult":
        return dc_td.DescribeClientVpnConnectionsResult.make_one(res)

    def describe_client_vpn_endpoints(
        self,
        res: "bs_td.DescribeClientVpnEndpointsResultTypeDef",
    ) -> "dc_td.DescribeClientVpnEndpointsResult":
        return dc_td.DescribeClientVpnEndpointsResult.make_one(res)

    def describe_client_vpn_routes(
        self,
        res: "bs_td.DescribeClientVpnRoutesResultTypeDef",
    ) -> "dc_td.DescribeClientVpnRoutesResult":
        return dc_td.DescribeClientVpnRoutesResult.make_one(res)

    def describe_client_vpn_target_networks(
        self,
        res: "bs_td.DescribeClientVpnTargetNetworksResultTypeDef",
    ) -> "dc_td.DescribeClientVpnTargetNetworksResult":
        return dc_td.DescribeClientVpnTargetNetworksResult.make_one(res)

    def describe_coip_pools(
        self,
        res: "bs_td.DescribeCoipPoolsResultTypeDef",
    ) -> "dc_td.DescribeCoipPoolsResult":
        return dc_td.DescribeCoipPoolsResult.make_one(res)

    def describe_conversion_tasks(
        self,
        res: "bs_td.DescribeConversionTasksResultTypeDef",
    ) -> "dc_td.DescribeConversionTasksResult":
        return dc_td.DescribeConversionTasksResult.make_one(res)

    def describe_customer_gateways(
        self,
        res: "bs_td.DescribeCustomerGatewaysResultTypeDef",
    ) -> "dc_td.DescribeCustomerGatewaysResult":
        return dc_td.DescribeCustomerGatewaysResult.make_one(res)

    def describe_declarative_policies_reports(
        self,
        res: "bs_td.DescribeDeclarativePoliciesReportsResultTypeDef",
    ) -> "dc_td.DescribeDeclarativePoliciesReportsResult":
        return dc_td.DescribeDeclarativePoliciesReportsResult.make_one(res)

    def describe_dhcp_options(
        self,
        res: "bs_td.DescribeDhcpOptionsResultTypeDef",
    ) -> "dc_td.DescribeDhcpOptionsResult":
        return dc_td.DescribeDhcpOptionsResult.make_one(res)

    def describe_egress_only_internet_gateways(
        self,
        res: "bs_td.DescribeEgressOnlyInternetGatewaysResultTypeDef",
    ) -> "dc_td.DescribeEgressOnlyInternetGatewaysResult":
        return dc_td.DescribeEgressOnlyInternetGatewaysResult.make_one(res)

    def describe_elastic_gpus(
        self,
        res: "bs_td.DescribeElasticGpusResultTypeDef",
    ) -> "dc_td.DescribeElasticGpusResult":
        return dc_td.DescribeElasticGpusResult.make_one(res)

    def describe_export_image_tasks(
        self,
        res: "bs_td.DescribeExportImageTasksResultTypeDef",
    ) -> "dc_td.DescribeExportImageTasksResult":
        return dc_td.DescribeExportImageTasksResult.make_one(res)

    def describe_export_tasks(
        self,
        res: "bs_td.DescribeExportTasksResultTypeDef",
    ) -> "dc_td.DescribeExportTasksResult":
        return dc_td.DescribeExportTasksResult.make_one(res)

    def describe_fast_launch_images(
        self,
        res: "bs_td.DescribeFastLaunchImagesResultTypeDef",
    ) -> "dc_td.DescribeFastLaunchImagesResult":
        return dc_td.DescribeFastLaunchImagesResult.make_one(res)

    def describe_fast_snapshot_restores(
        self,
        res: "bs_td.DescribeFastSnapshotRestoresResultTypeDef",
    ) -> "dc_td.DescribeFastSnapshotRestoresResult":
        return dc_td.DescribeFastSnapshotRestoresResult.make_one(res)

    def describe_fleet_history(
        self,
        res: "bs_td.DescribeFleetHistoryResultTypeDef",
    ) -> "dc_td.DescribeFleetHistoryResult":
        return dc_td.DescribeFleetHistoryResult.make_one(res)

    def describe_fleet_instances(
        self,
        res: "bs_td.DescribeFleetInstancesResultTypeDef",
    ) -> "dc_td.DescribeFleetInstancesResult":
        return dc_td.DescribeFleetInstancesResult.make_one(res)

    def describe_fleets(
        self,
        res: "bs_td.DescribeFleetsResultTypeDef",
    ) -> "dc_td.DescribeFleetsResult":
        return dc_td.DescribeFleetsResult.make_one(res)

    def describe_flow_logs(
        self,
        res: "bs_td.DescribeFlowLogsResultTypeDef",
    ) -> "dc_td.DescribeFlowLogsResult":
        return dc_td.DescribeFlowLogsResult.make_one(res)

    def describe_fpga_image_attribute(
        self,
        res: "bs_td.DescribeFpgaImageAttributeResultTypeDef",
    ) -> "dc_td.DescribeFpgaImageAttributeResult":
        return dc_td.DescribeFpgaImageAttributeResult.make_one(res)

    def describe_fpga_images(
        self,
        res: "bs_td.DescribeFpgaImagesResultTypeDef",
    ) -> "dc_td.DescribeFpgaImagesResult":
        return dc_td.DescribeFpgaImagesResult.make_one(res)

    def describe_host_reservation_offerings(
        self,
        res: "bs_td.DescribeHostReservationOfferingsResultTypeDef",
    ) -> "dc_td.DescribeHostReservationOfferingsResult":
        return dc_td.DescribeHostReservationOfferingsResult.make_one(res)

    def describe_host_reservations(
        self,
        res: "bs_td.DescribeHostReservationsResultTypeDef",
    ) -> "dc_td.DescribeHostReservationsResult":
        return dc_td.DescribeHostReservationsResult.make_one(res)

    def describe_hosts(
        self,
        res: "bs_td.DescribeHostsResultTypeDef",
    ) -> "dc_td.DescribeHostsResult":
        return dc_td.DescribeHostsResult.make_one(res)

    def describe_iam_instance_profile_associations(
        self,
        res: "bs_td.DescribeIamInstanceProfileAssociationsResultTypeDef",
    ) -> "dc_td.DescribeIamInstanceProfileAssociationsResult":
        return dc_td.DescribeIamInstanceProfileAssociationsResult.make_one(res)

    def describe_id_format(
        self,
        res: "bs_td.DescribeIdFormatResultTypeDef",
    ) -> "dc_td.DescribeIdFormatResult":
        return dc_td.DescribeIdFormatResult.make_one(res)

    def describe_identity_id_format(
        self,
        res: "bs_td.DescribeIdentityIdFormatResultTypeDef",
    ) -> "dc_td.DescribeIdentityIdFormatResult":
        return dc_td.DescribeIdentityIdFormatResult.make_one(res)

    def describe_image_attribute(
        self,
        res: "bs_td.ImageAttributeTypeDef",
    ) -> "dc_td.ImageAttribute":
        return dc_td.ImageAttribute.make_one(res)

    def describe_image_references(
        self,
        res: "bs_td.DescribeImageReferencesResultTypeDef",
    ) -> "dc_td.DescribeImageReferencesResult":
        return dc_td.DescribeImageReferencesResult.make_one(res)

    def describe_image_usage_report_entries(
        self,
        res: "bs_td.DescribeImageUsageReportEntriesResultTypeDef",
    ) -> "dc_td.DescribeImageUsageReportEntriesResult":
        return dc_td.DescribeImageUsageReportEntriesResult.make_one(res)

    def describe_image_usage_reports(
        self,
        res: "bs_td.DescribeImageUsageReportsResultTypeDef",
    ) -> "dc_td.DescribeImageUsageReportsResult":
        return dc_td.DescribeImageUsageReportsResult.make_one(res)

    def describe_images(
        self,
        res: "bs_td.DescribeImagesResultTypeDef",
    ) -> "dc_td.DescribeImagesResult":
        return dc_td.DescribeImagesResult.make_one(res)

    def describe_import_image_tasks(
        self,
        res: "bs_td.DescribeImportImageTasksResultTypeDef",
    ) -> "dc_td.DescribeImportImageTasksResult":
        return dc_td.DescribeImportImageTasksResult.make_one(res)

    def describe_import_snapshot_tasks(
        self,
        res: "bs_td.DescribeImportSnapshotTasksResultTypeDef",
    ) -> "dc_td.DescribeImportSnapshotTasksResult":
        return dc_td.DescribeImportSnapshotTasksResult.make_one(res)

    def describe_instance_attribute(
        self,
        res: "bs_td.InstanceAttributeTypeDef",
    ) -> "dc_td.InstanceAttribute":
        return dc_td.InstanceAttribute.make_one(res)

    def describe_instance_connect_endpoints(
        self,
        res: "bs_td.DescribeInstanceConnectEndpointsResultTypeDef",
    ) -> "dc_td.DescribeInstanceConnectEndpointsResult":
        return dc_td.DescribeInstanceConnectEndpointsResult.make_one(res)

    def describe_instance_credit_specifications(
        self,
        res: "bs_td.DescribeInstanceCreditSpecificationsResultTypeDef",
    ) -> "dc_td.DescribeInstanceCreditSpecificationsResult":
        return dc_td.DescribeInstanceCreditSpecificationsResult.make_one(res)

    def describe_instance_event_notification_attributes(
        self,
        res: "bs_td.DescribeInstanceEventNotificationAttributesResultTypeDef",
    ) -> "dc_td.DescribeInstanceEventNotificationAttributesResult":
        return dc_td.DescribeInstanceEventNotificationAttributesResult.make_one(res)

    def describe_instance_event_windows(
        self,
        res: "bs_td.DescribeInstanceEventWindowsResultTypeDef",
    ) -> "dc_td.DescribeInstanceEventWindowsResult":
        return dc_td.DescribeInstanceEventWindowsResult.make_one(res)

    def describe_instance_image_metadata(
        self,
        res: "bs_td.DescribeInstanceImageMetadataResultTypeDef",
    ) -> "dc_td.DescribeInstanceImageMetadataResult":
        return dc_td.DescribeInstanceImageMetadataResult.make_one(res)

    def describe_instance_status(
        self,
        res: "bs_td.DescribeInstanceStatusResultTypeDef",
    ) -> "dc_td.DescribeInstanceStatusResult":
        return dc_td.DescribeInstanceStatusResult.make_one(res)

    def describe_instance_topology(
        self,
        res: "bs_td.DescribeInstanceTopologyResultTypeDef",
    ) -> "dc_td.DescribeInstanceTopologyResult":
        return dc_td.DescribeInstanceTopologyResult.make_one(res)

    def describe_instance_type_offerings(
        self,
        res: "bs_td.DescribeInstanceTypeOfferingsResultTypeDef",
    ) -> "dc_td.DescribeInstanceTypeOfferingsResult":
        return dc_td.DescribeInstanceTypeOfferingsResult.make_one(res)

    def describe_instance_types(
        self,
        res: "bs_td.DescribeInstanceTypesResultTypeDef",
    ) -> "dc_td.DescribeInstanceTypesResult":
        return dc_td.DescribeInstanceTypesResult.make_one(res)

    def describe_instances(
        self,
        res: "bs_td.DescribeInstancesResultTypeDef",
    ) -> "dc_td.DescribeInstancesResult":
        return dc_td.DescribeInstancesResult.make_one(res)

    def describe_internet_gateways(
        self,
        res: "bs_td.DescribeInternetGatewaysResultTypeDef",
    ) -> "dc_td.DescribeInternetGatewaysResult":
        return dc_td.DescribeInternetGatewaysResult.make_one(res)

    def describe_ipam_byoasn(
        self,
        res: "bs_td.DescribeIpamByoasnResultTypeDef",
    ) -> "dc_td.DescribeIpamByoasnResult":
        return dc_td.DescribeIpamByoasnResult.make_one(res)

    def describe_ipam_external_resource_verification_tokens(
        self,
        res: "bs_td.DescribeIpamExternalResourceVerificationTokensResultTypeDef",
    ) -> "dc_td.DescribeIpamExternalResourceVerificationTokensResult":
        return dc_td.DescribeIpamExternalResourceVerificationTokensResult.make_one(res)

    def describe_ipam_pools(
        self,
        res: "bs_td.DescribeIpamPoolsResultTypeDef",
    ) -> "dc_td.DescribeIpamPoolsResult":
        return dc_td.DescribeIpamPoolsResult.make_one(res)

    def describe_ipam_resource_discoveries(
        self,
        res: "bs_td.DescribeIpamResourceDiscoveriesResultTypeDef",
    ) -> "dc_td.DescribeIpamResourceDiscoveriesResult":
        return dc_td.DescribeIpamResourceDiscoveriesResult.make_one(res)

    def describe_ipam_resource_discovery_associations(
        self,
        res: "bs_td.DescribeIpamResourceDiscoveryAssociationsResultTypeDef",
    ) -> "dc_td.DescribeIpamResourceDiscoveryAssociationsResult":
        return dc_td.DescribeIpamResourceDiscoveryAssociationsResult.make_one(res)

    def describe_ipam_scopes(
        self,
        res: "bs_td.DescribeIpamScopesResultTypeDef",
    ) -> "dc_td.DescribeIpamScopesResult":
        return dc_td.DescribeIpamScopesResult.make_one(res)

    def describe_ipams(
        self,
        res: "bs_td.DescribeIpamsResultTypeDef",
    ) -> "dc_td.DescribeIpamsResult":
        return dc_td.DescribeIpamsResult.make_one(res)

    def describe_ipv6_pools(
        self,
        res: "bs_td.DescribeIpv6PoolsResultTypeDef",
    ) -> "dc_td.DescribeIpv6PoolsResult":
        return dc_td.DescribeIpv6PoolsResult.make_one(res)

    def describe_key_pairs(
        self,
        res: "bs_td.DescribeKeyPairsResultTypeDef",
    ) -> "dc_td.DescribeKeyPairsResult":
        return dc_td.DescribeKeyPairsResult.make_one(res)

    def describe_launch_template_versions(
        self,
        res: "bs_td.DescribeLaunchTemplateVersionsResultTypeDef",
    ) -> "dc_td.DescribeLaunchTemplateVersionsResult":
        return dc_td.DescribeLaunchTemplateVersionsResult.make_one(res)

    def describe_launch_templates(
        self,
        res: "bs_td.DescribeLaunchTemplatesResultTypeDef",
    ) -> "dc_td.DescribeLaunchTemplatesResult":
        return dc_td.DescribeLaunchTemplatesResult.make_one(res)

    def describe_local_gateway_route_table_virtual_interface_group_associations(
        self,
        res: "bs_td.DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsResultTypeDef",
    ) -> "dc_td.DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsResult":
        return dc_td.DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsResult.make_one(
            res
        )

    def describe_local_gateway_route_table_vpc_associations(
        self,
        res: "bs_td.DescribeLocalGatewayRouteTableVpcAssociationsResultTypeDef",
    ) -> "dc_td.DescribeLocalGatewayRouteTableVpcAssociationsResult":
        return dc_td.DescribeLocalGatewayRouteTableVpcAssociationsResult.make_one(res)

    def describe_local_gateway_route_tables(
        self,
        res: "bs_td.DescribeLocalGatewayRouteTablesResultTypeDef",
    ) -> "dc_td.DescribeLocalGatewayRouteTablesResult":
        return dc_td.DescribeLocalGatewayRouteTablesResult.make_one(res)

    def describe_local_gateway_virtual_interface_groups(
        self,
        res: "bs_td.DescribeLocalGatewayVirtualInterfaceGroupsResultTypeDef",
    ) -> "dc_td.DescribeLocalGatewayVirtualInterfaceGroupsResult":
        return dc_td.DescribeLocalGatewayVirtualInterfaceGroupsResult.make_one(res)

    def describe_local_gateway_virtual_interfaces(
        self,
        res: "bs_td.DescribeLocalGatewayVirtualInterfacesResultTypeDef",
    ) -> "dc_td.DescribeLocalGatewayVirtualInterfacesResult":
        return dc_td.DescribeLocalGatewayVirtualInterfacesResult.make_one(res)

    def describe_local_gateways(
        self,
        res: "bs_td.DescribeLocalGatewaysResultTypeDef",
    ) -> "dc_td.DescribeLocalGatewaysResult":
        return dc_td.DescribeLocalGatewaysResult.make_one(res)

    def describe_locked_snapshots(
        self,
        res: "bs_td.DescribeLockedSnapshotsResultTypeDef",
    ) -> "dc_td.DescribeLockedSnapshotsResult":
        return dc_td.DescribeLockedSnapshotsResult.make_one(res)

    def describe_mac_hosts(
        self,
        res: "bs_td.DescribeMacHostsResultTypeDef",
    ) -> "dc_td.DescribeMacHostsResult":
        return dc_td.DescribeMacHostsResult.make_one(res)

    def describe_mac_modification_tasks(
        self,
        res: "bs_td.DescribeMacModificationTasksResultTypeDef",
    ) -> "dc_td.DescribeMacModificationTasksResult":
        return dc_td.DescribeMacModificationTasksResult.make_one(res)

    def describe_managed_prefix_lists(
        self,
        res: "bs_td.DescribeManagedPrefixListsResultTypeDef",
    ) -> "dc_td.DescribeManagedPrefixListsResult":
        return dc_td.DescribeManagedPrefixListsResult.make_one(res)

    def describe_moving_addresses(
        self,
        res: "bs_td.DescribeMovingAddressesResultTypeDef",
    ) -> "dc_td.DescribeMovingAddressesResult":
        return dc_td.DescribeMovingAddressesResult.make_one(res)

    def describe_nat_gateways(
        self,
        res: "bs_td.DescribeNatGatewaysResultTypeDef",
    ) -> "dc_td.DescribeNatGatewaysResult":
        return dc_td.DescribeNatGatewaysResult.make_one(res)

    def describe_network_acls(
        self,
        res: "bs_td.DescribeNetworkAclsResultTypeDef",
    ) -> "dc_td.DescribeNetworkAclsResult":
        return dc_td.DescribeNetworkAclsResult.make_one(res)

    def describe_network_insights_access_scope_analyses(
        self,
        res: "bs_td.DescribeNetworkInsightsAccessScopeAnalysesResultTypeDef",
    ) -> "dc_td.DescribeNetworkInsightsAccessScopeAnalysesResult":
        return dc_td.DescribeNetworkInsightsAccessScopeAnalysesResult.make_one(res)

    def describe_network_insights_access_scopes(
        self,
        res: "bs_td.DescribeNetworkInsightsAccessScopesResultTypeDef",
    ) -> "dc_td.DescribeNetworkInsightsAccessScopesResult":
        return dc_td.DescribeNetworkInsightsAccessScopesResult.make_one(res)

    def describe_network_insights_analyses(
        self,
        res: "bs_td.DescribeNetworkInsightsAnalysesResultTypeDef",
    ) -> "dc_td.DescribeNetworkInsightsAnalysesResult":
        return dc_td.DescribeNetworkInsightsAnalysesResult.make_one(res)

    def describe_network_insights_paths(
        self,
        res: "bs_td.DescribeNetworkInsightsPathsResultTypeDef",
    ) -> "dc_td.DescribeNetworkInsightsPathsResult":
        return dc_td.DescribeNetworkInsightsPathsResult.make_one(res)

    def describe_network_interface_attribute(
        self,
        res: "bs_td.DescribeNetworkInterfaceAttributeResultTypeDef",
    ) -> "dc_td.DescribeNetworkInterfaceAttributeResult":
        return dc_td.DescribeNetworkInterfaceAttributeResult.make_one(res)

    def describe_network_interface_permissions(
        self,
        res: "bs_td.DescribeNetworkInterfacePermissionsResultTypeDef",
    ) -> "dc_td.DescribeNetworkInterfacePermissionsResult":
        return dc_td.DescribeNetworkInterfacePermissionsResult.make_one(res)

    def describe_network_interfaces(
        self,
        res: "bs_td.DescribeNetworkInterfacesResultTypeDef",
    ) -> "dc_td.DescribeNetworkInterfacesResult":
        return dc_td.DescribeNetworkInterfacesResult.make_one(res)

    def describe_outpost_lags(
        self,
        res: "bs_td.DescribeOutpostLagsResultTypeDef",
    ) -> "dc_td.DescribeOutpostLagsResult":
        return dc_td.DescribeOutpostLagsResult.make_one(res)

    def describe_placement_groups(
        self,
        res: "bs_td.DescribePlacementGroupsResultTypeDef",
    ) -> "dc_td.DescribePlacementGroupsResult":
        return dc_td.DescribePlacementGroupsResult.make_one(res)

    def describe_prefix_lists(
        self,
        res: "bs_td.DescribePrefixListsResultTypeDef",
    ) -> "dc_td.DescribePrefixListsResult":
        return dc_td.DescribePrefixListsResult.make_one(res)

    def describe_principal_id_format(
        self,
        res: "bs_td.DescribePrincipalIdFormatResultTypeDef",
    ) -> "dc_td.DescribePrincipalIdFormatResult":
        return dc_td.DescribePrincipalIdFormatResult.make_one(res)

    def describe_public_ipv4_pools(
        self,
        res: "bs_td.DescribePublicIpv4PoolsResultTypeDef",
    ) -> "dc_td.DescribePublicIpv4PoolsResult":
        return dc_td.DescribePublicIpv4PoolsResult.make_one(res)

    def describe_regions(
        self,
        res: "bs_td.DescribeRegionsResultTypeDef",
    ) -> "dc_td.DescribeRegionsResult":
        return dc_td.DescribeRegionsResult.make_one(res)

    def describe_replace_root_volume_tasks(
        self,
        res: "bs_td.DescribeReplaceRootVolumeTasksResultTypeDef",
    ) -> "dc_td.DescribeReplaceRootVolumeTasksResult":
        return dc_td.DescribeReplaceRootVolumeTasksResult.make_one(res)

    def describe_reserved_instances(
        self,
        res: "bs_td.DescribeReservedInstancesResultTypeDef",
    ) -> "dc_td.DescribeReservedInstancesResult":
        return dc_td.DescribeReservedInstancesResult.make_one(res)

    def describe_reserved_instances_listings(
        self,
        res: "bs_td.DescribeReservedInstancesListingsResultTypeDef",
    ) -> "dc_td.DescribeReservedInstancesListingsResult":
        return dc_td.DescribeReservedInstancesListingsResult.make_one(res)

    def describe_reserved_instances_modifications(
        self,
        res: "bs_td.DescribeReservedInstancesModificationsResultTypeDef",
    ) -> "dc_td.DescribeReservedInstancesModificationsResult":
        return dc_td.DescribeReservedInstancesModificationsResult.make_one(res)

    def describe_reserved_instances_offerings(
        self,
        res: "bs_td.DescribeReservedInstancesOfferingsResultTypeDef",
    ) -> "dc_td.DescribeReservedInstancesOfferingsResult":
        return dc_td.DescribeReservedInstancesOfferingsResult.make_one(res)

    def describe_route_server_endpoints(
        self,
        res: "bs_td.DescribeRouteServerEndpointsResultTypeDef",
    ) -> "dc_td.DescribeRouteServerEndpointsResult":
        return dc_td.DescribeRouteServerEndpointsResult.make_one(res)

    def describe_route_server_peers(
        self,
        res: "bs_td.DescribeRouteServerPeersResultTypeDef",
    ) -> "dc_td.DescribeRouteServerPeersResult":
        return dc_td.DescribeRouteServerPeersResult.make_one(res)

    def describe_route_servers(
        self,
        res: "bs_td.DescribeRouteServersResultTypeDef",
    ) -> "dc_td.DescribeRouteServersResult":
        return dc_td.DescribeRouteServersResult.make_one(res)

    def describe_route_tables(
        self,
        res: "bs_td.DescribeRouteTablesResultTypeDef",
    ) -> "dc_td.DescribeRouteTablesResult":
        return dc_td.DescribeRouteTablesResult.make_one(res)

    def describe_scheduled_instance_availability(
        self,
        res: "bs_td.DescribeScheduledInstanceAvailabilityResultTypeDef",
    ) -> "dc_td.DescribeScheduledInstanceAvailabilityResult":
        return dc_td.DescribeScheduledInstanceAvailabilityResult.make_one(res)

    def describe_scheduled_instances(
        self,
        res: "bs_td.DescribeScheduledInstancesResultTypeDef",
    ) -> "dc_td.DescribeScheduledInstancesResult":
        return dc_td.DescribeScheduledInstancesResult.make_one(res)

    def describe_security_group_references(
        self,
        res: "bs_td.DescribeSecurityGroupReferencesResultTypeDef",
    ) -> "dc_td.DescribeSecurityGroupReferencesResult":
        return dc_td.DescribeSecurityGroupReferencesResult.make_one(res)

    def describe_security_group_rules(
        self,
        res: "bs_td.DescribeSecurityGroupRulesResultTypeDef",
    ) -> "dc_td.DescribeSecurityGroupRulesResult":
        return dc_td.DescribeSecurityGroupRulesResult.make_one(res)

    def describe_security_group_vpc_associations(
        self,
        res: "bs_td.DescribeSecurityGroupVpcAssociationsResultTypeDef",
    ) -> "dc_td.DescribeSecurityGroupVpcAssociationsResult":
        return dc_td.DescribeSecurityGroupVpcAssociationsResult.make_one(res)

    def describe_security_groups(
        self,
        res: "bs_td.DescribeSecurityGroupsResultTypeDef",
    ) -> "dc_td.DescribeSecurityGroupsResult":
        return dc_td.DescribeSecurityGroupsResult.make_one(res)

    def describe_service_link_virtual_interfaces(
        self,
        res: "bs_td.DescribeServiceLinkVirtualInterfacesResultTypeDef",
    ) -> "dc_td.DescribeServiceLinkVirtualInterfacesResult":
        return dc_td.DescribeServiceLinkVirtualInterfacesResult.make_one(res)

    def describe_snapshot_attribute(
        self,
        res: "bs_td.DescribeSnapshotAttributeResultTypeDef",
    ) -> "dc_td.DescribeSnapshotAttributeResult":
        return dc_td.DescribeSnapshotAttributeResult.make_one(res)

    def describe_snapshot_tier_status(
        self,
        res: "bs_td.DescribeSnapshotTierStatusResultTypeDef",
    ) -> "dc_td.DescribeSnapshotTierStatusResult":
        return dc_td.DescribeSnapshotTierStatusResult.make_one(res)

    def describe_snapshots(
        self,
        res: "bs_td.DescribeSnapshotsResultTypeDef",
    ) -> "dc_td.DescribeSnapshotsResult":
        return dc_td.DescribeSnapshotsResult.make_one(res)

    def describe_spot_datafeed_subscription(
        self,
        res: "bs_td.DescribeSpotDatafeedSubscriptionResultTypeDef",
    ) -> "dc_td.DescribeSpotDatafeedSubscriptionResult":
        return dc_td.DescribeSpotDatafeedSubscriptionResult.make_one(res)

    def describe_spot_fleet_instances(
        self,
        res: "bs_td.DescribeSpotFleetInstancesResponseTypeDef",
    ) -> "dc_td.DescribeSpotFleetInstancesResponse":
        return dc_td.DescribeSpotFleetInstancesResponse.make_one(res)

    def describe_spot_fleet_request_history(
        self,
        res: "bs_td.DescribeSpotFleetRequestHistoryResponseTypeDef",
    ) -> "dc_td.DescribeSpotFleetRequestHistoryResponse":
        return dc_td.DescribeSpotFleetRequestHistoryResponse.make_one(res)

    def describe_spot_fleet_requests(
        self,
        res: "bs_td.DescribeSpotFleetRequestsResponseTypeDef",
    ) -> "dc_td.DescribeSpotFleetRequestsResponse":
        return dc_td.DescribeSpotFleetRequestsResponse.make_one(res)

    def describe_spot_instance_requests(
        self,
        res: "bs_td.DescribeSpotInstanceRequestsResultTypeDef",
    ) -> "dc_td.DescribeSpotInstanceRequestsResult":
        return dc_td.DescribeSpotInstanceRequestsResult.make_one(res)

    def describe_spot_price_history(
        self,
        res: "bs_td.DescribeSpotPriceHistoryResultTypeDef",
    ) -> "dc_td.DescribeSpotPriceHistoryResult":
        return dc_td.DescribeSpotPriceHistoryResult.make_one(res)

    def describe_stale_security_groups(
        self,
        res: "bs_td.DescribeStaleSecurityGroupsResultTypeDef",
    ) -> "dc_td.DescribeStaleSecurityGroupsResult":
        return dc_td.DescribeStaleSecurityGroupsResult.make_one(res)

    def describe_store_image_tasks(
        self,
        res: "bs_td.DescribeStoreImageTasksResultTypeDef",
    ) -> "dc_td.DescribeStoreImageTasksResult":
        return dc_td.DescribeStoreImageTasksResult.make_one(res)

    def describe_subnets(
        self,
        res: "bs_td.DescribeSubnetsResultTypeDef",
    ) -> "dc_td.DescribeSubnetsResult":
        return dc_td.DescribeSubnetsResult.make_one(res)

    def describe_tags(
        self,
        res: "bs_td.DescribeTagsResultTypeDef",
    ) -> "dc_td.DescribeTagsResult":
        return dc_td.DescribeTagsResult.make_one(res)

    def describe_traffic_mirror_filter_rules(
        self,
        res: "bs_td.DescribeTrafficMirrorFilterRulesResultTypeDef",
    ) -> "dc_td.DescribeTrafficMirrorFilterRulesResult":
        return dc_td.DescribeTrafficMirrorFilterRulesResult.make_one(res)

    def describe_traffic_mirror_filters(
        self,
        res: "bs_td.DescribeTrafficMirrorFiltersResultTypeDef",
    ) -> "dc_td.DescribeTrafficMirrorFiltersResult":
        return dc_td.DescribeTrafficMirrorFiltersResult.make_one(res)

    def describe_traffic_mirror_sessions(
        self,
        res: "bs_td.DescribeTrafficMirrorSessionsResultTypeDef",
    ) -> "dc_td.DescribeTrafficMirrorSessionsResult":
        return dc_td.DescribeTrafficMirrorSessionsResult.make_one(res)

    def describe_traffic_mirror_targets(
        self,
        res: "bs_td.DescribeTrafficMirrorTargetsResultTypeDef",
    ) -> "dc_td.DescribeTrafficMirrorTargetsResult":
        return dc_td.DescribeTrafficMirrorTargetsResult.make_one(res)

    def describe_transit_gateway_attachments(
        self,
        res: "bs_td.DescribeTransitGatewayAttachmentsResultTypeDef",
    ) -> "dc_td.DescribeTransitGatewayAttachmentsResult":
        return dc_td.DescribeTransitGatewayAttachmentsResult.make_one(res)

    def describe_transit_gateway_connect_peers(
        self,
        res: "bs_td.DescribeTransitGatewayConnectPeersResultTypeDef",
    ) -> "dc_td.DescribeTransitGatewayConnectPeersResult":
        return dc_td.DescribeTransitGatewayConnectPeersResult.make_one(res)

    def describe_transit_gateway_connects(
        self,
        res: "bs_td.DescribeTransitGatewayConnectsResultTypeDef",
    ) -> "dc_td.DescribeTransitGatewayConnectsResult":
        return dc_td.DescribeTransitGatewayConnectsResult.make_one(res)

    def describe_transit_gateway_multicast_domains(
        self,
        res: "bs_td.DescribeTransitGatewayMulticastDomainsResultTypeDef",
    ) -> "dc_td.DescribeTransitGatewayMulticastDomainsResult":
        return dc_td.DescribeTransitGatewayMulticastDomainsResult.make_one(res)

    def describe_transit_gateway_peering_attachments(
        self,
        res: "bs_td.DescribeTransitGatewayPeeringAttachmentsResultTypeDef",
    ) -> "dc_td.DescribeTransitGatewayPeeringAttachmentsResult":
        return dc_td.DescribeTransitGatewayPeeringAttachmentsResult.make_one(res)

    def describe_transit_gateway_policy_tables(
        self,
        res: "bs_td.DescribeTransitGatewayPolicyTablesResultTypeDef",
    ) -> "dc_td.DescribeTransitGatewayPolicyTablesResult":
        return dc_td.DescribeTransitGatewayPolicyTablesResult.make_one(res)

    def describe_transit_gateway_route_table_announcements(
        self,
        res: "bs_td.DescribeTransitGatewayRouteTableAnnouncementsResultTypeDef",
    ) -> "dc_td.DescribeTransitGatewayRouteTableAnnouncementsResult":
        return dc_td.DescribeTransitGatewayRouteTableAnnouncementsResult.make_one(res)

    def describe_transit_gateway_route_tables(
        self,
        res: "bs_td.DescribeTransitGatewayRouteTablesResultTypeDef",
    ) -> "dc_td.DescribeTransitGatewayRouteTablesResult":
        return dc_td.DescribeTransitGatewayRouteTablesResult.make_one(res)

    def describe_transit_gateway_vpc_attachments(
        self,
        res: "bs_td.DescribeTransitGatewayVpcAttachmentsResultTypeDef",
    ) -> "dc_td.DescribeTransitGatewayVpcAttachmentsResult":
        return dc_td.DescribeTransitGatewayVpcAttachmentsResult.make_one(res)

    def describe_transit_gateways(
        self,
        res: "bs_td.DescribeTransitGatewaysResultTypeDef",
    ) -> "dc_td.DescribeTransitGatewaysResult":
        return dc_td.DescribeTransitGatewaysResult.make_one(res)

    def describe_trunk_interface_associations(
        self,
        res: "bs_td.DescribeTrunkInterfaceAssociationsResultTypeDef",
    ) -> "dc_td.DescribeTrunkInterfaceAssociationsResult":
        return dc_td.DescribeTrunkInterfaceAssociationsResult.make_one(res)

    def describe_verified_access_endpoints(
        self,
        res: "bs_td.DescribeVerifiedAccessEndpointsResultTypeDef",
    ) -> "dc_td.DescribeVerifiedAccessEndpointsResult":
        return dc_td.DescribeVerifiedAccessEndpointsResult.make_one(res)

    def describe_verified_access_groups(
        self,
        res: "bs_td.DescribeVerifiedAccessGroupsResultTypeDef",
    ) -> "dc_td.DescribeVerifiedAccessGroupsResult":
        return dc_td.DescribeVerifiedAccessGroupsResult.make_one(res)

    def describe_verified_access_instance_logging_configurations(
        self,
        res: "bs_td.DescribeVerifiedAccessInstanceLoggingConfigurationsResultTypeDef",
    ) -> "dc_td.DescribeVerifiedAccessInstanceLoggingConfigurationsResult":
        return dc_td.DescribeVerifiedAccessInstanceLoggingConfigurationsResult.make_one(
            res
        )

    def describe_verified_access_instances(
        self,
        res: "bs_td.DescribeVerifiedAccessInstancesResultTypeDef",
    ) -> "dc_td.DescribeVerifiedAccessInstancesResult":
        return dc_td.DescribeVerifiedAccessInstancesResult.make_one(res)

    def describe_verified_access_trust_providers(
        self,
        res: "bs_td.DescribeVerifiedAccessTrustProvidersResultTypeDef",
    ) -> "dc_td.DescribeVerifiedAccessTrustProvidersResult":
        return dc_td.DescribeVerifiedAccessTrustProvidersResult.make_one(res)

    def describe_volume_attribute(
        self,
        res: "bs_td.DescribeVolumeAttributeResultTypeDef",
    ) -> "dc_td.DescribeVolumeAttributeResult":
        return dc_td.DescribeVolumeAttributeResult.make_one(res)

    def describe_volume_status(
        self,
        res: "bs_td.DescribeVolumeStatusResultTypeDef",
    ) -> "dc_td.DescribeVolumeStatusResult":
        return dc_td.DescribeVolumeStatusResult.make_one(res)

    def describe_volumes(
        self,
        res: "bs_td.DescribeVolumesResultTypeDef",
    ) -> "dc_td.DescribeVolumesResult":
        return dc_td.DescribeVolumesResult.make_one(res)

    def describe_volumes_modifications(
        self,
        res: "bs_td.DescribeVolumesModificationsResultTypeDef",
    ) -> "dc_td.DescribeVolumesModificationsResult":
        return dc_td.DescribeVolumesModificationsResult.make_one(res)

    def describe_vpc_attribute(
        self,
        res: "bs_td.DescribeVpcAttributeResultTypeDef",
    ) -> "dc_td.DescribeVpcAttributeResult":
        return dc_td.DescribeVpcAttributeResult.make_one(res)

    def describe_vpc_block_public_access_exclusions(
        self,
        res: "bs_td.DescribeVpcBlockPublicAccessExclusionsResultTypeDef",
    ) -> "dc_td.DescribeVpcBlockPublicAccessExclusionsResult":
        return dc_td.DescribeVpcBlockPublicAccessExclusionsResult.make_one(res)

    def describe_vpc_block_public_access_options(
        self,
        res: "bs_td.DescribeVpcBlockPublicAccessOptionsResultTypeDef",
    ) -> "dc_td.DescribeVpcBlockPublicAccessOptionsResult":
        return dc_td.DescribeVpcBlockPublicAccessOptionsResult.make_one(res)

    def describe_vpc_classic_link(
        self,
        res: "bs_td.DescribeVpcClassicLinkResultTypeDef",
    ) -> "dc_td.DescribeVpcClassicLinkResult":
        return dc_td.DescribeVpcClassicLinkResult.make_one(res)

    def describe_vpc_classic_link_dns_support(
        self,
        res: "bs_td.DescribeVpcClassicLinkDnsSupportResultTypeDef",
    ) -> "dc_td.DescribeVpcClassicLinkDnsSupportResult":
        return dc_td.DescribeVpcClassicLinkDnsSupportResult.make_one(res)

    def describe_vpc_endpoint_associations(
        self,
        res: "bs_td.DescribeVpcEndpointAssociationsResultTypeDef",
    ) -> "dc_td.DescribeVpcEndpointAssociationsResult":
        return dc_td.DescribeVpcEndpointAssociationsResult.make_one(res)

    def describe_vpc_endpoint_connection_notifications(
        self,
        res: "bs_td.DescribeVpcEndpointConnectionNotificationsResultTypeDef",
    ) -> "dc_td.DescribeVpcEndpointConnectionNotificationsResult":
        return dc_td.DescribeVpcEndpointConnectionNotificationsResult.make_one(res)

    def describe_vpc_endpoint_connections(
        self,
        res: "bs_td.DescribeVpcEndpointConnectionsResultTypeDef",
    ) -> "dc_td.DescribeVpcEndpointConnectionsResult":
        return dc_td.DescribeVpcEndpointConnectionsResult.make_one(res)

    def describe_vpc_endpoint_service_configurations(
        self,
        res: "bs_td.DescribeVpcEndpointServiceConfigurationsResultTypeDef",
    ) -> "dc_td.DescribeVpcEndpointServiceConfigurationsResult":
        return dc_td.DescribeVpcEndpointServiceConfigurationsResult.make_one(res)

    def describe_vpc_endpoint_service_permissions(
        self,
        res: "bs_td.DescribeVpcEndpointServicePermissionsResultTypeDef",
    ) -> "dc_td.DescribeVpcEndpointServicePermissionsResult":
        return dc_td.DescribeVpcEndpointServicePermissionsResult.make_one(res)

    def describe_vpc_endpoint_services(
        self,
        res: "bs_td.DescribeVpcEndpointServicesResultTypeDef",
    ) -> "dc_td.DescribeVpcEndpointServicesResult":
        return dc_td.DescribeVpcEndpointServicesResult.make_one(res)

    def describe_vpc_endpoints(
        self,
        res: "bs_td.DescribeVpcEndpointsResultTypeDef",
    ) -> "dc_td.DescribeVpcEndpointsResult":
        return dc_td.DescribeVpcEndpointsResult.make_one(res)

    def describe_vpc_peering_connections(
        self,
        res: "bs_td.DescribeVpcPeeringConnectionsResultTypeDef",
    ) -> "dc_td.DescribeVpcPeeringConnectionsResult":
        return dc_td.DescribeVpcPeeringConnectionsResult.make_one(res)

    def describe_vpcs(
        self,
        res: "bs_td.DescribeVpcsResultTypeDef",
    ) -> "dc_td.DescribeVpcsResult":
        return dc_td.DescribeVpcsResult.make_one(res)

    def describe_vpn_connections(
        self,
        res: "bs_td.DescribeVpnConnectionsResultTypeDef",
    ) -> "dc_td.DescribeVpnConnectionsResult":
        return dc_td.DescribeVpnConnectionsResult.make_one(res)

    def describe_vpn_gateways(
        self,
        res: "bs_td.DescribeVpnGatewaysResultTypeDef",
    ) -> "dc_td.DescribeVpnGatewaysResult":
        return dc_td.DescribeVpnGatewaysResult.make_one(res)

    def detach_classic_link_vpc(
        self,
        res: "bs_td.DetachClassicLinkVpcResultTypeDef",
    ) -> "dc_td.DetachClassicLinkVpcResult":
        return dc_td.DetachClassicLinkVpcResult.make_one(res)

    def detach_internet_gateway(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def detach_network_interface(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def detach_verified_access_trust_provider(
        self,
        res: "bs_td.DetachVerifiedAccessTrustProviderResultTypeDef",
    ) -> "dc_td.DetachVerifiedAccessTrustProviderResult":
        return dc_td.DetachVerifiedAccessTrustProviderResult.make_one(res)

    def detach_volume(
        self,
        res: "bs_td.VolumeAttachmentResponseTypeDef",
    ) -> "dc_td.VolumeAttachmentResponse":
        return dc_td.VolumeAttachmentResponse.make_one(res)

    def detach_vpn_gateway(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def disable_address_transfer(
        self,
        res: "bs_td.DisableAddressTransferResultTypeDef",
    ) -> "dc_td.DisableAddressTransferResult":
        return dc_td.DisableAddressTransferResult.make_one(res)

    def disable_allowed_images_settings(
        self,
        res: "bs_td.DisableAllowedImagesSettingsResultTypeDef",
    ) -> "dc_td.DisableAllowedImagesSettingsResult":
        return dc_td.DisableAllowedImagesSettingsResult.make_one(res)

    def disable_aws_network_performance_metric_subscription(
        self,
        res: "bs_td.DisableAwsNetworkPerformanceMetricSubscriptionResultTypeDef",
    ) -> "dc_td.DisableAwsNetworkPerformanceMetricSubscriptionResult":
        return dc_td.DisableAwsNetworkPerformanceMetricSubscriptionResult.make_one(res)

    def disable_ebs_encryption_by_default(
        self,
        res: "bs_td.DisableEbsEncryptionByDefaultResultTypeDef",
    ) -> "dc_td.DisableEbsEncryptionByDefaultResult":
        return dc_td.DisableEbsEncryptionByDefaultResult.make_one(res)

    def disable_fast_launch(
        self,
        res: "bs_td.DisableFastLaunchResultTypeDef",
    ) -> "dc_td.DisableFastLaunchResult":
        return dc_td.DisableFastLaunchResult.make_one(res)

    def disable_fast_snapshot_restores(
        self,
        res: "bs_td.DisableFastSnapshotRestoresResultTypeDef",
    ) -> "dc_td.DisableFastSnapshotRestoresResult":
        return dc_td.DisableFastSnapshotRestoresResult.make_one(res)

    def disable_image(
        self,
        res: "bs_td.DisableImageResultTypeDef",
    ) -> "dc_td.DisableImageResult":
        return dc_td.DisableImageResult.make_one(res)

    def disable_image_block_public_access(
        self,
        res: "bs_td.DisableImageBlockPublicAccessResultTypeDef",
    ) -> "dc_td.DisableImageBlockPublicAccessResult":
        return dc_td.DisableImageBlockPublicAccessResult.make_one(res)

    def disable_image_deprecation(
        self,
        res: "bs_td.DisableImageDeprecationResultTypeDef",
    ) -> "dc_td.DisableImageDeprecationResult":
        return dc_td.DisableImageDeprecationResult.make_one(res)

    def disable_image_deregistration_protection(
        self,
        res: "bs_td.DisableImageDeregistrationProtectionResultTypeDef",
    ) -> "dc_td.DisableImageDeregistrationProtectionResult":
        return dc_td.DisableImageDeregistrationProtectionResult.make_one(res)

    def disable_ipam_organization_admin_account(
        self,
        res: "bs_td.DisableIpamOrganizationAdminAccountResultTypeDef",
    ) -> "dc_td.DisableIpamOrganizationAdminAccountResult":
        return dc_td.DisableIpamOrganizationAdminAccountResult.make_one(res)

    def disable_route_server_propagation(
        self,
        res: "bs_td.DisableRouteServerPropagationResultTypeDef",
    ) -> "dc_td.DisableRouteServerPropagationResult":
        return dc_td.DisableRouteServerPropagationResult.make_one(res)

    def disable_serial_console_access(
        self,
        res: "bs_td.DisableSerialConsoleAccessResultTypeDef",
    ) -> "dc_td.DisableSerialConsoleAccessResult":
        return dc_td.DisableSerialConsoleAccessResult.make_one(res)

    def disable_snapshot_block_public_access(
        self,
        res: "bs_td.DisableSnapshotBlockPublicAccessResultTypeDef",
    ) -> "dc_td.DisableSnapshotBlockPublicAccessResult":
        return dc_td.DisableSnapshotBlockPublicAccessResult.make_one(res)

    def disable_transit_gateway_route_table_propagation(
        self,
        res: "bs_td.DisableTransitGatewayRouteTablePropagationResultTypeDef",
    ) -> "dc_td.DisableTransitGatewayRouteTablePropagationResult":
        return dc_td.DisableTransitGatewayRouteTablePropagationResult.make_one(res)

    def disable_vgw_route_propagation(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def disable_vpc_classic_link(
        self,
        res: "bs_td.DisableVpcClassicLinkResultTypeDef",
    ) -> "dc_td.DisableVpcClassicLinkResult":
        return dc_td.DisableVpcClassicLinkResult.make_one(res)

    def disable_vpc_classic_link_dns_support(
        self,
        res: "bs_td.DisableVpcClassicLinkDnsSupportResultTypeDef",
    ) -> "dc_td.DisableVpcClassicLinkDnsSupportResult":
        return dc_td.DisableVpcClassicLinkDnsSupportResult.make_one(res)

    def disassociate_address(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def disassociate_capacity_reservation_billing_owner(
        self,
        res: "bs_td.DisassociateCapacityReservationBillingOwnerResultTypeDef",
    ) -> "dc_td.DisassociateCapacityReservationBillingOwnerResult":
        return dc_td.DisassociateCapacityReservationBillingOwnerResult.make_one(res)

    def disassociate_client_vpn_target_network(
        self,
        res: "bs_td.DisassociateClientVpnTargetNetworkResultTypeDef",
    ) -> "dc_td.DisassociateClientVpnTargetNetworkResult":
        return dc_td.DisassociateClientVpnTargetNetworkResult.make_one(res)

    def disassociate_enclave_certificate_iam_role(
        self,
        res: "bs_td.DisassociateEnclaveCertificateIamRoleResultTypeDef",
    ) -> "dc_td.DisassociateEnclaveCertificateIamRoleResult":
        return dc_td.DisassociateEnclaveCertificateIamRoleResult.make_one(res)

    def disassociate_iam_instance_profile(
        self,
        res: "bs_td.DisassociateIamInstanceProfileResultTypeDef",
    ) -> "dc_td.DisassociateIamInstanceProfileResult":
        return dc_td.DisassociateIamInstanceProfileResult.make_one(res)

    def disassociate_instance_event_window(
        self,
        res: "bs_td.DisassociateInstanceEventWindowResultTypeDef",
    ) -> "dc_td.DisassociateInstanceEventWindowResult":
        return dc_td.DisassociateInstanceEventWindowResult.make_one(res)

    def disassociate_ipam_byoasn(
        self,
        res: "bs_td.DisassociateIpamByoasnResultTypeDef",
    ) -> "dc_td.DisassociateIpamByoasnResult":
        return dc_td.DisassociateIpamByoasnResult.make_one(res)

    def disassociate_ipam_resource_discovery(
        self,
        res: "bs_td.DisassociateIpamResourceDiscoveryResultTypeDef",
    ) -> "dc_td.DisassociateIpamResourceDiscoveryResult":
        return dc_td.DisassociateIpamResourceDiscoveryResult.make_one(res)

    def disassociate_nat_gateway_address(
        self,
        res: "bs_td.DisassociateNatGatewayAddressResultTypeDef",
    ) -> "dc_td.DisassociateNatGatewayAddressResult":
        return dc_td.DisassociateNatGatewayAddressResult.make_one(res)

    def disassociate_route_server(
        self,
        res: "bs_td.DisassociateRouteServerResultTypeDef",
    ) -> "dc_td.DisassociateRouteServerResult":
        return dc_td.DisassociateRouteServerResult.make_one(res)

    def disassociate_route_table(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def disassociate_security_group_vpc(
        self,
        res: "bs_td.DisassociateSecurityGroupVpcResultTypeDef",
    ) -> "dc_td.DisassociateSecurityGroupVpcResult":
        return dc_td.DisassociateSecurityGroupVpcResult.make_one(res)

    def disassociate_subnet_cidr_block(
        self,
        res: "bs_td.DisassociateSubnetCidrBlockResultTypeDef",
    ) -> "dc_td.DisassociateSubnetCidrBlockResult":
        return dc_td.DisassociateSubnetCidrBlockResult.make_one(res)

    def disassociate_transit_gateway_multicast_domain(
        self,
        res: "bs_td.DisassociateTransitGatewayMulticastDomainResultTypeDef",
    ) -> "dc_td.DisassociateTransitGatewayMulticastDomainResult":
        return dc_td.DisassociateTransitGatewayMulticastDomainResult.make_one(res)

    def disassociate_transit_gateway_policy_table(
        self,
        res: "bs_td.DisassociateTransitGatewayPolicyTableResultTypeDef",
    ) -> "dc_td.DisassociateTransitGatewayPolicyTableResult":
        return dc_td.DisassociateTransitGatewayPolicyTableResult.make_one(res)

    def disassociate_transit_gateway_route_table(
        self,
        res: "bs_td.DisassociateTransitGatewayRouteTableResultTypeDef",
    ) -> "dc_td.DisassociateTransitGatewayRouteTableResult":
        return dc_td.DisassociateTransitGatewayRouteTableResult.make_one(res)

    def disassociate_trunk_interface(
        self,
        res: "bs_td.DisassociateTrunkInterfaceResultTypeDef",
    ) -> "dc_td.DisassociateTrunkInterfaceResult":
        return dc_td.DisassociateTrunkInterfaceResult.make_one(res)

    def disassociate_vpc_cidr_block(
        self,
        res: "bs_td.DisassociateVpcCidrBlockResultTypeDef",
    ) -> "dc_td.DisassociateVpcCidrBlockResult":
        return dc_td.DisassociateVpcCidrBlockResult.make_one(res)

    def enable_address_transfer(
        self,
        res: "bs_td.EnableAddressTransferResultTypeDef",
    ) -> "dc_td.EnableAddressTransferResult":
        return dc_td.EnableAddressTransferResult.make_one(res)

    def enable_allowed_images_settings(
        self,
        res: "bs_td.EnableAllowedImagesSettingsResultTypeDef",
    ) -> "dc_td.EnableAllowedImagesSettingsResult":
        return dc_td.EnableAllowedImagesSettingsResult.make_one(res)

    def enable_aws_network_performance_metric_subscription(
        self,
        res: "bs_td.EnableAwsNetworkPerformanceMetricSubscriptionResultTypeDef",
    ) -> "dc_td.EnableAwsNetworkPerformanceMetricSubscriptionResult":
        return dc_td.EnableAwsNetworkPerformanceMetricSubscriptionResult.make_one(res)

    def enable_ebs_encryption_by_default(
        self,
        res: "bs_td.EnableEbsEncryptionByDefaultResultTypeDef",
    ) -> "dc_td.EnableEbsEncryptionByDefaultResult":
        return dc_td.EnableEbsEncryptionByDefaultResult.make_one(res)

    def enable_fast_launch(
        self,
        res: "bs_td.EnableFastLaunchResultTypeDef",
    ) -> "dc_td.EnableFastLaunchResult":
        return dc_td.EnableFastLaunchResult.make_one(res)

    def enable_fast_snapshot_restores(
        self,
        res: "bs_td.EnableFastSnapshotRestoresResultTypeDef",
    ) -> "dc_td.EnableFastSnapshotRestoresResult":
        return dc_td.EnableFastSnapshotRestoresResult.make_one(res)

    def enable_image(
        self,
        res: "bs_td.EnableImageResultTypeDef",
    ) -> "dc_td.EnableImageResult":
        return dc_td.EnableImageResult.make_one(res)

    def enable_image_block_public_access(
        self,
        res: "bs_td.EnableImageBlockPublicAccessResultTypeDef",
    ) -> "dc_td.EnableImageBlockPublicAccessResult":
        return dc_td.EnableImageBlockPublicAccessResult.make_one(res)

    def enable_image_deprecation(
        self,
        res: "bs_td.EnableImageDeprecationResultTypeDef",
    ) -> "dc_td.EnableImageDeprecationResult":
        return dc_td.EnableImageDeprecationResult.make_one(res)

    def enable_image_deregistration_protection(
        self,
        res: "bs_td.EnableImageDeregistrationProtectionResultTypeDef",
    ) -> "dc_td.EnableImageDeregistrationProtectionResult":
        return dc_td.EnableImageDeregistrationProtectionResult.make_one(res)

    def enable_ipam_organization_admin_account(
        self,
        res: "bs_td.EnableIpamOrganizationAdminAccountResultTypeDef",
    ) -> "dc_td.EnableIpamOrganizationAdminAccountResult":
        return dc_td.EnableIpamOrganizationAdminAccountResult.make_one(res)

    def enable_reachability_analyzer_organization_sharing(
        self,
        res: "bs_td.EnableReachabilityAnalyzerOrganizationSharingResultTypeDef",
    ) -> "dc_td.EnableReachabilityAnalyzerOrganizationSharingResult":
        return dc_td.EnableReachabilityAnalyzerOrganizationSharingResult.make_one(res)

    def enable_route_server_propagation(
        self,
        res: "bs_td.EnableRouteServerPropagationResultTypeDef",
    ) -> "dc_td.EnableRouteServerPropagationResult":
        return dc_td.EnableRouteServerPropagationResult.make_one(res)

    def enable_serial_console_access(
        self,
        res: "bs_td.EnableSerialConsoleAccessResultTypeDef",
    ) -> "dc_td.EnableSerialConsoleAccessResult":
        return dc_td.EnableSerialConsoleAccessResult.make_one(res)

    def enable_snapshot_block_public_access(
        self,
        res: "bs_td.EnableSnapshotBlockPublicAccessResultTypeDef",
    ) -> "dc_td.EnableSnapshotBlockPublicAccessResult":
        return dc_td.EnableSnapshotBlockPublicAccessResult.make_one(res)

    def enable_transit_gateway_route_table_propagation(
        self,
        res: "bs_td.EnableTransitGatewayRouteTablePropagationResultTypeDef",
    ) -> "dc_td.EnableTransitGatewayRouteTablePropagationResult":
        return dc_td.EnableTransitGatewayRouteTablePropagationResult.make_one(res)

    def enable_vgw_route_propagation(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def enable_volume_io(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def enable_vpc_classic_link(
        self,
        res: "bs_td.EnableVpcClassicLinkResultTypeDef",
    ) -> "dc_td.EnableVpcClassicLinkResult":
        return dc_td.EnableVpcClassicLinkResult.make_one(res)

    def enable_vpc_classic_link_dns_support(
        self,
        res: "bs_td.EnableVpcClassicLinkDnsSupportResultTypeDef",
    ) -> "dc_td.EnableVpcClassicLinkDnsSupportResult":
        return dc_td.EnableVpcClassicLinkDnsSupportResult.make_one(res)

    def export_client_vpn_client_certificate_revocation_list(
        self,
        res: "bs_td.ExportClientVpnClientCertificateRevocationListResultTypeDef",
    ) -> "dc_td.ExportClientVpnClientCertificateRevocationListResult":
        return dc_td.ExportClientVpnClientCertificateRevocationListResult.make_one(res)

    def export_client_vpn_client_configuration(
        self,
        res: "bs_td.ExportClientVpnClientConfigurationResultTypeDef",
    ) -> "dc_td.ExportClientVpnClientConfigurationResult":
        return dc_td.ExportClientVpnClientConfigurationResult.make_one(res)

    def export_image(
        self,
        res: "bs_td.ExportImageResultTypeDef",
    ) -> "dc_td.ExportImageResult":
        return dc_td.ExportImageResult.make_one(res)

    def export_transit_gateway_routes(
        self,
        res: "bs_td.ExportTransitGatewayRoutesResultTypeDef",
    ) -> "dc_td.ExportTransitGatewayRoutesResult":
        return dc_td.ExportTransitGatewayRoutesResult.make_one(res)

    def export_verified_access_instance_client_configuration(
        self,
        res: "bs_td.ExportVerifiedAccessInstanceClientConfigurationResultTypeDef",
    ) -> "dc_td.ExportVerifiedAccessInstanceClientConfigurationResult":
        return dc_td.ExportVerifiedAccessInstanceClientConfigurationResult.make_one(res)

    def get_active_vpn_tunnel_status(
        self,
        res: "bs_td.GetActiveVpnTunnelStatusResultTypeDef",
    ) -> "dc_td.GetActiveVpnTunnelStatusResult":
        return dc_td.GetActiveVpnTunnelStatusResult.make_one(res)

    def get_allowed_images_settings(
        self,
        res: "bs_td.GetAllowedImagesSettingsResultTypeDef",
    ) -> "dc_td.GetAllowedImagesSettingsResult":
        return dc_td.GetAllowedImagesSettingsResult.make_one(res)

    def get_associated_enclave_certificate_iam_roles(
        self,
        res: "bs_td.GetAssociatedEnclaveCertificateIamRolesResultTypeDef",
    ) -> "dc_td.GetAssociatedEnclaveCertificateIamRolesResult":
        return dc_td.GetAssociatedEnclaveCertificateIamRolesResult.make_one(res)

    def get_associated_ipv6_pool_cidrs(
        self,
        res: "bs_td.GetAssociatedIpv6PoolCidrsResultTypeDef",
    ) -> "dc_td.GetAssociatedIpv6PoolCidrsResult":
        return dc_td.GetAssociatedIpv6PoolCidrsResult.make_one(res)

    def get_aws_network_performance_data(
        self,
        res: "bs_td.GetAwsNetworkPerformanceDataResultTypeDef",
    ) -> "dc_td.GetAwsNetworkPerformanceDataResult":
        return dc_td.GetAwsNetworkPerformanceDataResult.make_one(res)

    def get_capacity_reservation_usage(
        self,
        res: "bs_td.GetCapacityReservationUsageResultTypeDef",
    ) -> "dc_td.GetCapacityReservationUsageResult":
        return dc_td.GetCapacityReservationUsageResult.make_one(res)

    def get_coip_pool_usage(
        self,
        res: "bs_td.GetCoipPoolUsageResultTypeDef",
    ) -> "dc_td.GetCoipPoolUsageResult":
        return dc_td.GetCoipPoolUsageResult.make_one(res)

    def get_console_output(
        self,
        res: "bs_td.GetConsoleOutputResultTypeDef",
    ) -> "dc_td.GetConsoleOutputResult":
        return dc_td.GetConsoleOutputResult.make_one(res)

    def get_console_screenshot(
        self,
        res: "bs_td.GetConsoleScreenshotResultTypeDef",
    ) -> "dc_td.GetConsoleScreenshotResult":
        return dc_td.GetConsoleScreenshotResult.make_one(res)

    def get_declarative_policies_report_summary(
        self,
        res: "bs_td.GetDeclarativePoliciesReportSummaryResultTypeDef",
    ) -> "dc_td.GetDeclarativePoliciesReportSummaryResult":
        return dc_td.GetDeclarativePoliciesReportSummaryResult.make_one(res)

    def get_default_credit_specification(
        self,
        res: "bs_td.GetDefaultCreditSpecificationResultTypeDef",
    ) -> "dc_td.GetDefaultCreditSpecificationResult":
        return dc_td.GetDefaultCreditSpecificationResult.make_one(res)

    def get_ebs_default_kms_key_id(
        self,
        res: "bs_td.GetEbsDefaultKmsKeyIdResultTypeDef",
    ) -> "dc_td.GetEbsDefaultKmsKeyIdResult":
        return dc_td.GetEbsDefaultKmsKeyIdResult.make_one(res)

    def get_ebs_encryption_by_default(
        self,
        res: "bs_td.GetEbsEncryptionByDefaultResultTypeDef",
    ) -> "dc_td.GetEbsEncryptionByDefaultResult":
        return dc_td.GetEbsEncryptionByDefaultResult.make_one(res)

    def get_flow_logs_integration_template(
        self,
        res: "bs_td.GetFlowLogsIntegrationTemplateResultTypeDef",
    ) -> "dc_td.GetFlowLogsIntegrationTemplateResult":
        return dc_td.GetFlowLogsIntegrationTemplateResult.make_one(res)

    def get_groups_for_capacity_reservation(
        self,
        res: "bs_td.GetGroupsForCapacityReservationResultTypeDef",
    ) -> "dc_td.GetGroupsForCapacityReservationResult":
        return dc_td.GetGroupsForCapacityReservationResult.make_one(res)

    def get_host_reservation_purchase_preview(
        self,
        res: "bs_td.GetHostReservationPurchasePreviewResultTypeDef",
    ) -> "dc_td.GetHostReservationPurchasePreviewResult":
        return dc_td.GetHostReservationPurchasePreviewResult.make_one(res)

    def get_image_block_public_access_state(
        self,
        res: "bs_td.GetImageBlockPublicAccessStateResultTypeDef",
    ) -> "dc_td.GetImageBlockPublicAccessStateResult":
        return dc_td.GetImageBlockPublicAccessStateResult.make_one(res)

    def get_instance_metadata_defaults(
        self,
        res: "bs_td.GetInstanceMetadataDefaultsResultTypeDef",
    ) -> "dc_td.GetInstanceMetadataDefaultsResult":
        return dc_td.GetInstanceMetadataDefaultsResult.make_one(res)

    def get_instance_tpm_ek_pub(
        self,
        res: "bs_td.GetInstanceTpmEkPubResultTypeDef",
    ) -> "dc_td.GetInstanceTpmEkPubResult":
        return dc_td.GetInstanceTpmEkPubResult.make_one(res)

    def get_instance_types_from_instance_requirements(
        self,
        res: "bs_td.GetInstanceTypesFromInstanceRequirementsResultTypeDef",
    ) -> "dc_td.GetInstanceTypesFromInstanceRequirementsResult":
        return dc_td.GetInstanceTypesFromInstanceRequirementsResult.make_one(res)

    def get_instance_uefi_data(
        self,
        res: "bs_td.GetInstanceUefiDataResultTypeDef",
    ) -> "dc_td.GetInstanceUefiDataResult":
        return dc_td.GetInstanceUefiDataResult.make_one(res)

    def get_ipam_address_history(
        self,
        res: "bs_td.GetIpamAddressHistoryResultTypeDef",
    ) -> "dc_td.GetIpamAddressHistoryResult":
        return dc_td.GetIpamAddressHistoryResult.make_one(res)

    def get_ipam_discovered_accounts(
        self,
        res: "bs_td.GetIpamDiscoveredAccountsResultTypeDef",
    ) -> "dc_td.GetIpamDiscoveredAccountsResult":
        return dc_td.GetIpamDiscoveredAccountsResult.make_one(res)

    def get_ipam_discovered_public_addresses(
        self,
        res: "bs_td.GetIpamDiscoveredPublicAddressesResultTypeDef",
    ) -> "dc_td.GetIpamDiscoveredPublicAddressesResult":
        return dc_td.GetIpamDiscoveredPublicAddressesResult.make_one(res)

    def get_ipam_discovered_resource_cidrs(
        self,
        res: "bs_td.GetIpamDiscoveredResourceCidrsResultTypeDef",
    ) -> "dc_td.GetIpamDiscoveredResourceCidrsResult":
        return dc_td.GetIpamDiscoveredResourceCidrsResult.make_one(res)

    def get_ipam_pool_allocations(
        self,
        res: "bs_td.GetIpamPoolAllocationsResultTypeDef",
    ) -> "dc_td.GetIpamPoolAllocationsResult":
        return dc_td.GetIpamPoolAllocationsResult.make_one(res)

    def get_ipam_pool_cidrs(
        self,
        res: "bs_td.GetIpamPoolCidrsResultTypeDef",
    ) -> "dc_td.GetIpamPoolCidrsResult":
        return dc_td.GetIpamPoolCidrsResult.make_one(res)

    def get_ipam_resource_cidrs(
        self,
        res: "bs_td.GetIpamResourceCidrsResultTypeDef",
    ) -> "dc_td.GetIpamResourceCidrsResult":
        return dc_td.GetIpamResourceCidrsResult.make_one(res)

    def get_launch_template_data(
        self,
        res: "bs_td.GetLaunchTemplateDataResultTypeDef",
    ) -> "dc_td.GetLaunchTemplateDataResult":
        return dc_td.GetLaunchTemplateDataResult.make_one(res)

    def get_managed_prefix_list_associations(
        self,
        res: "bs_td.GetManagedPrefixListAssociationsResultTypeDef",
    ) -> "dc_td.GetManagedPrefixListAssociationsResult":
        return dc_td.GetManagedPrefixListAssociationsResult.make_one(res)

    def get_managed_prefix_list_entries(
        self,
        res: "bs_td.GetManagedPrefixListEntriesResultTypeDef",
    ) -> "dc_td.GetManagedPrefixListEntriesResult":
        return dc_td.GetManagedPrefixListEntriesResult.make_one(res)

    def get_network_insights_access_scope_analysis_findings(
        self,
        res: "bs_td.GetNetworkInsightsAccessScopeAnalysisFindingsResultTypeDef",
    ) -> "dc_td.GetNetworkInsightsAccessScopeAnalysisFindingsResult":
        return dc_td.GetNetworkInsightsAccessScopeAnalysisFindingsResult.make_one(res)

    def get_network_insights_access_scope_content(
        self,
        res: "bs_td.GetNetworkInsightsAccessScopeContentResultTypeDef",
    ) -> "dc_td.GetNetworkInsightsAccessScopeContentResult":
        return dc_td.GetNetworkInsightsAccessScopeContentResult.make_one(res)

    def get_password_data(
        self,
        res: "bs_td.GetPasswordDataResultTypeDef",
    ) -> "dc_td.GetPasswordDataResult":
        return dc_td.GetPasswordDataResult.make_one(res)

    def get_reserved_instances_exchange_quote(
        self,
        res: "bs_td.GetReservedInstancesExchangeQuoteResultTypeDef",
    ) -> "dc_td.GetReservedInstancesExchangeQuoteResult":
        return dc_td.GetReservedInstancesExchangeQuoteResult.make_one(res)

    def get_route_server_associations(
        self,
        res: "bs_td.GetRouteServerAssociationsResultTypeDef",
    ) -> "dc_td.GetRouteServerAssociationsResult":
        return dc_td.GetRouteServerAssociationsResult.make_one(res)

    def get_route_server_propagations(
        self,
        res: "bs_td.GetRouteServerPropagationsResultTypeDef",
    ) -> "dc_td.GetRouteServerPropagationsResult":
        return dc_td.GetRouteServerPropagationsResult.make_one(res)

    def get_route_server_routing_database(
        self,
        res: "bs_td.GetRouteServerRoutingDatabaseResultTypeDef",
    ) -> "dc_td.GetRouteServerRoutingDatabaseResult":
        return dc_td.GetRouteServerRoutingDatabaseResult.make_one(res)

    def get_security_groups_for_vpc(
        self,
        res: "bs_td.GetSecurityGroupsForVpcResultTypeDef",
    ) -> "dc_td.GetSecurityGroupsForVpcResult":
        return dc_td.GetSecurityGroupsForVpcResult.make_one(res)

    def get_serial_console_access_status(
        self,
        res: "bs_td.GetSerialConsoleAccessStatusResultTypeDef",
    ) -> "dc_td.GetSerialConsoleAccessStatusResult":
        return dc_td.GetSerialConsoleAccessStatusResult.make_one(res)

    def get_snapshot_block_public_access_state(
        self,
        res: "bs_td.GetSnapshotBlockPublicAccessStateResultTypeDef",
    ) -> "dc_td.GetSnapshotBlockPublicAccessStateResult":
        return dc_td.GetSnapshotBlockPublicAccessStateResult.make_one(res)

    def get_spot_placement_scores(
        self,
        res: "bs_td.GetSpotPlacementScoresResultTypeDef",
    ) -> "dc_td.GetSpotPlacementScoresResult":
        return dc_td.GetSpotPlacementScoresResult.make_one(res)

    def get_subnet_cidr_reservations(
        self,
        res: "bs_td.GetSubnetCidrReservationsResultTypeDef",
    ) -> "dc_td.GetSubnetCidrReservationsResult":
        return dc_td.GetSubnetCidrReservationsResult.make_one(res)

    def get_transit_gateway_attachment_propagations(
        self,
        res: "bs_td.GetTransitGatewayAttachmentPropagationsResultTypeDef",
    ) -> "dc_td.GetTransitGatewayAttachmentPropagationsResult":
        return dc_td.GetTransitGatewayAttachmentPropagationsResult.make_one(res)

    def get_transit_gateway_multicast_domain_associations(
        self,
        res: "bs_td.GetTransitGatewayMulticastDomainAssociationsResultTypeDef",
    ) -> "dc_td.GetTransitGatewayMulticastDomainAssociationsResult":
        return dc_td.GetTransitGatewayMulticastDomainAssociationsResult.make_one(res)

    def get_transit_gateway_policy_table_associations(
        self,
        res: "bs_td.GetTransitGatewayPolicyTableAssociationsResultTypeDef",
    ) -> "dc_td.GetTransitGatewayPolicyTableAssociationsResult":
        return dc_td.GetTransitGatewayPolicyTableAssociationsResult.make_one(res)

    def get_transit_gateway_policy_table_entries(
        self,
        res: "bs_td.GetTransitGatewayPolicyTableEntriesResultTypeDef",
    ) -> "dc_td.GetTransitGatewayPolicyTableEntriesResult":
        return dc_td.GetTransitGatewayPolicyTableEntriesResult.make_one(res)

    def get_transit_gateway_prefix_list_references(
        self,
        res: "bs_td.GetTransitGatewayPrefixListReferencesResultTypeDef",
    ) -> "dc_td.GetTransitGatewayPrefixListReferencesResult":
        return dc_td.GetTransitGatewayPrefixListReferencesResult.make_one(res)

    def get_transit_gateway_route_table_associations(
        self,
        res: "bs_td.GetTransitGatewayRouteTableAssociationsResultTypeDef",
    ) -> "dc_td.GetTransitGatewayRouteTableAssociationsResult":
        return dc_td.GetTransitGatewayRouteTableAssociationsResult.make_one(res)

    def get_transit_gateway_route_table_propagations(
        self,
        res: "bs_td.GetTransitGatewayRouteTablePropagationsResultTypeDef",
    ) -> "dc_td.GetTransitGatewayRouteTablePropagationsResult":
        return dc_td.GetTransitGatewayRouteTablePropagationsResult.make_one(res)

    def get_verified_access_endpoint_policy(
        self,
        res: "bs_td.GetVerifiedAccessEndpointPolicyResultTypeDef",
    ) -> "dc_td.GetVerifiedAccessEndpointPolicyResult":
        return dc_td.GetVerifiedAccessEndpointPolicyResult.make_one(res)

    def get_verified_access_endpoint_targets(
        self,
        res: "bs_td.GetVerifiedAccessEndpointTargetsResultTypeDef",
    ) -> "dc_td.GetVerifiedAccessEndpointTargetsResult":
        return dc_td.GetVerifiedAccessEndpointTargetsResult.make_one(res)

    def get_verified_access_group_policy(
        self,
        res: "bs_td.GetVerifiedAccessGroupPolicyResultTypeDef",
    ) -> "dc_td.GetVerifiedAccessGroupPolicyResult":
        return dc_td.GetVerifiedAccessGroupPolicyResult.make_one(res)

    def get_vpn_connection_device_sample_configuration(
        self,
        res: "bs_td.GetVpnConnectionDeviceSampleConfigurationResultTypeDef",
    ) -> "dc_td.GetVpnConnectionDeviceSampleConfigurationResult":
        return dc_td.GetVpnConnectionDeviceSampleConfigurationResult.make_one(res)

    def get_vpn_connection_device_types(
        self,
        res: "bs_td.GetVpnConnectionDeviceTypesResultTypeDef",
    ) -> "dc_td.GetVpnConnectionDeviceTypesResult":
        return dc_td.GetVpnConnectionDeviceTypesResult.make_one(res)

    def get_vpn_tunnel_replacement_status(
        self,
        res: "bs_td.GetVpnTunnelReplacementStatusResultTypeDef",
    ) -> "dc_td.GetVpnTunnelReplacementStatusResult":
        return dc_td.GetVpnTunnelReplacementStatusResult.make_one(res)

    def import_client_vpn_client_certificate_revocation_list(
        self,
        res: "bs_td.ImportClientVpnClientCertificateRevocationListResultTypeDef",
    ) -> "dc_td.ImportClientVpnClientCertificateRevocationListResult":
        return dc_td.ImportClientVpnClientCertificateRevocationListResult.make_one(res)

    def import_image(
        self,
        res: "bs_td.ImportImageResultTypeDef",
    ) -> "dc_td.ImportImageResult":
        return dc_td.ImportImageResult.make_one(res)

    def import_instance(
        self,
        res: "bs_td.ImportInstanceResultTypeDef",
    ) -> "dc_td.ImportInstanceResult":
        return dc_td.ImportInstanceResult.make_one(res)

    def import_key_pair(
        self,
        res: "bs_td.ImportKeyPairResultTypeDef",
    ) -> "dc_td.ImportKeyPairResult":
        return dc_td.ImportKeyPairResult.make_one(res)

    def import_snapshot(
        self,
        res: "bs_td.ImportSnapshotResultTypeDef",
    ) -> "dc_td.ImportSnapshotResult":
        return dc_td.ImportSnapshotResult.make_one(res)

    def import_volume(
        self,
        res: "bs_td.ImportVolumeResultTypeDef",
    ) -> "dc_td.ImportVolumeResult":
        return dc_td.ImportVolumeResult.make_one(res)

    def list_images_in_recycle_bin(
        self,
        res: "bs_td.ListImagesInRecycleBinResultTypeDef",
    ) -> "dc_td.ListImagesInRecycleBinResult":
        return dc_td.ListImagesInRecycleBinResult.make_one(res)

    def list_snapshots_in_recycle_bin(
        self,
        res: "bs_td.ListSnapshotsInRecycleBinResultTypeDef",
    ) -> "dc_td.ListSnapshotsInRecycleBinResult":
        return dc_td.ListSnapshotsInRecycleBinResult.make_one(res)

    def lock_snapshot(
        self,
        res: "bs_td.LockSnapshotResultTypeDef",
    ) -> "dc_td.LockSnapshotResult":
        return dc_td.LockSnapshotResult.make_one(res)

    def modify_address_attribute(
        self,
        res: "bs_td.ModifyAddressAttributeResultTypeDef",
    ) -> "dc_td.ModifyAddressAttributeResult":
        return dc_td.ModifyAddressAttributeResult.make_one(res)

    def modify_availability_zone_group(
        self,
        res: "bs_td.ModifyAvailabilityZoneGroupResultTypeDef",
    ) -> "dc_td.ModifyAvailabilityZoneGroupResult":
        return dc_td.ModifyAvailabilityZoneGroupResult.make_one(res)

    def modify_capacity_reservation(
        self,
        res: "bs_td.ModifyCapacityReservationResultTypeDef",
    ) -> "dc_td.ModifyCapacityReservationResult":
        return dc_td.ModifyCapacityReservationResult.make_one(res)

    def modify_capacity_reservation_fleet(
        self,
        res: "bs_td.ModifyCapacityReservationFleetResultTypeDef",
    ) -> "dc_td.ModifyCapacityReservationFleetResult":
        return dc_td.ModifyCapacityReservationFleetResult.make_one(res)

    def modify_client_vpn_endpoint(
        self,
        res: "bs_td.ModifyClientVpnEndpointResultTypeDef",
    ) -> "dc_td.ModifyClientVpnEndpointResult":
        return dc_td.ModifyClientVpnEndpointResult.make_one(res)

    def modify_default_credit_specification(
        self,
        res: "bs_td.ModifyDefaultCreditSpecificationResultTypeDef",
    ) -> "dc_td.ModifyDefaultCreditSpecificationResult":
        return dc_td.ModifyDefaultCreditSpecificationResult.make_one(res)

    def modify_ebs_default_kms_key_id(
        self,
        res: "bs_td.ModifyEbsDefaultKmsKeyIdResultTypeDef",
    ) -> "dc_td.ModifyEbsDefaultKmsKeyIdResult":
        return dc_td.ModifyEbsDefaultKmsKeyIdResult.make_one(res)

    def modify_fleet(
        self,
        res: "bs_td.ModifyFleetResultTypeDef",
    ) -> "dc_td.ModifyFleetResult":
        return dc_td.ModifyFleetResult.make_one(res)

    def modify_fpga_image_attribute(
        self,
        res: "bs_td.ModifyFpgaImageAttributeResultTypeDef",
    ) -> "dc_td.ModifyFpgaImageAttributeResult":
        return dc_td.ModifyFpgaImageAttributeResult.make_one(res)

    def modify_hosts(
        self,
        res: "bs_td.ModifyHostsResultTypeDef",
    ) -> "dc_td.ModifyHostsResult":
        return dc_td.ModifyHostsResult.make_one(res)

    def modify_id_format(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def modify_identity_id_format(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def modify_image_attribute(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def modify_instance_attribute(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def modify_instance_capacity_reservation_attributes(
        self,
        res: "bs_td.ModifyInstanceCapacityReservationAttributesResultTypeDef",
    ) -> "dc_td.ModifyInstanceCapacityReservationAttributesResult":
        return dc_td.ModifyInstanceCapacityReservationAttributesResult.make_one(res)

    def modify_instance_connect_endpoint(
        self,
        res: "bs_td.ModifyInstanceConnectEndpointResultTypeDef",
    ) -> "dc_td.ModifyInstanceConnectEndpointResult":
        return dc_td.ModifyInstanceConnectEndpointResult.make_one(res)

    def modify_instance_cpu_options(
        self,
        res: "bs_td.ModifyInstanceCpuOptionsResultTypeDef",
    ) -> "dc_td.ModifyInstanceCpuOptionsResult":
        return dc_td.ModifyInstanceCpuOptionsResult.make_one(res)

    def modify_instance_credit_specification(
        self,
        res: "bs_td.ModifyInstanceCreditSpecificationResultTypeDef",
    ) -> "dc_td.ModifyInstanceCreditSpecificationResult":
        return dc_td.ModifyInstanceCreditSpecificationResult.make_one(res)

    def modify_instance_event_start_time(
        self,
        res: "bs_td.ModifyInstanceEventStartTimeResultTypeDef",
    ) -> "dc_td.ModifyInstanceEventStartTimeResult":
        return dc_td.ModifyInstanceEventStartTimeResult.make_one(res)

    def modify_instance_event_window(
        self,
        res: "bs_td.ModifyInstanceEventWindowResultTypeDef",
    ) -> "dc_td.ModifyInstanceEventWindowResult":
        return dc_td.ModifyInstanceEventWindowResult.make_one(res)

    def modify_instance_maintenance_options(
        self,
        res: "bs_td.ModifyInstanceMaintenanceOptionsResultTypeDef",
    ) -> "dc_td.ModifyInstanceMaintenanceOptionsResult":
        return dc_td.ModifyInstanceMaintenanceOptionsResult.make_one(res)

    def modify_instance_metadata_defaults(
        self,
        res: "bs_td.ModifyInstanceMetadataDefaultsResultTypeDef",
    ) -> "dc_td.ModifyInstanceMetadataDefaultsResult":
        return dc_td.ModifyInstanceMetadataDefaultsResult.make_one(res)

    def modify_instance_metadata_options(
        self,
        res: "bs_td.ModifyInstanceMetadataOptionsResultTypeDef",
    ) -> "dc_td.ModifyInstanceMetadataOptionsResult":
        return dc_td.ModifyInstanceMetadataOptionsResult.make_one(res)

    def modify_instance_network_performance_options(
        self,
        res: "bs_td.ModifyInstanceNetworkPerformanceResultTypeDef",
    ) -> "dc_td.ModifyInstanceNetworkPerformanceResult":
        return dc_td.ModifyInstanceNetworkPerformanceResult.make_one(res)

    def modify_instance_placement(
        self,
        res: "bs_td.ModifyInstancePlacementResultTypeDef",
    ) -> "dc_td.ModifyInstancePlacementResult":
        return dc_td.ModifyInstancePlacementResult.make_one(res)

    def modify_ipam(
        self,
        res: "bs_td.ModifyIpamResultTypeDef",
    ) -> "dc_td.ModifyIpamResult":
        return dc_td.ModifyIpamResult.make_one(res)

    def modify_ipam_pool(
        self,
        res: "bs_td.ModifyIpamPoolResultTypeDef",
    ) -> "dc_td.ModifyIpamPoolResult":
        return dc_td.ModifyIpamPoolResult.make_one(res)

    def modify_ipam_resource_cidr(
        self,
        res: "bs_td.ModifyIpamResourceCidrResultTypeDef",
    ) -> "dc_td.ModifyIpamResourceCidrResult":
        return dc_td.ModifyIpamResourceCidrResult.make_one(res)

    def modify_ipam_resource_discovery(
        self,
        res: "bs_td.ModifyIpamResourceDiscoveryResultTypeDef",
    ) -> "dc_td.ModifyIpamResourceDiscoveryResult":
        return dc_td.ModifyIpamResourceDiscoveryResult.make_one(res)

    def modify_ipam_scope(
        self,
        res: "bs_td.ModifyIpamScopeResultTypeDef",
    ) -> "dc_td.ModifyIpamScopeResult":
        return dc_td.ModifyIpamScopeResult.make_one(res)

    def modify_launch_template(
        self,
        res: "bs_td.ModifyLaunchTemplateResultTypeDef",
    ) -> "dc_td.ModifyLaunchTemplateResult":
        return dc_td.ModifyLaunchTemplateResult.make_one(res)

    def modify_local_gateway_route(
        self,
        res: "bs_td.ModifyLocalGatewayRouteResultTypeDef",
    ) -> "dc_td.ModifyLocalGatewayRouteResult":
        return dc_td.ModifyLocalGatewayRouteResult.make_one(res)

    def modify_managed_prefix_list(
        self,
        res: "bs_td.ModifyManagedPrefixListResultTypeDef",
    ) -> "dc_td.ModifyManagedPrefixListResult":
        return dc_td.ModifyManagedPrefixListResult.make_one(res)

    def modify_network_interface_attribute(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def modify_private_dns_name_options(
        self,
        res: "bs_td.ModifyPrivateDnsNameOptionsResultTypeDef",
    ) -> "dc_td.ModifyPrivateDnsNameOptionsResult":
        return dc_td.ModifyPrivateDnsNameOptionsResult.make_one(res)

    def modify_public_ip_dns_name_options(
        self,
        res: "bs_td.ModifyPublicIpDnsNameOptionsResultTypeDef",
    ) -> "dc_td.ModifyPublicIpDnsNameOptionsResult":
        return dc_td.ModifyPublicIpDnsNameOptionsResult.make_one(res)

    def modify_reserved_instances(
        self,
        res: "bs_td.ModifyReservedInstancesResultTypeDef",
    ) -> "dc_td.ModifyReservedInstancesResult":
        return dc_td.ModifyReservedInstancesResult.make_one(res)

    def modify_route_server(
        self,
        res: "bs_td.ModifyRouteServerResultTypeDef",
    ) -> "dc_td.ModifyRouteServerResult":
        return dc_td.ModifyRouteServerResult.make_one(res)

    def modify_security_group_rules(
        self,
        res: "bs_td.ModifySecurityGroupRulesResultTypeDef",
    ) -> "dc_td.ModifySecurityGroupRulesResult":
        return dc_td.ModifySecurityGroupRulesResult.make_one(res)

    def modify_snapshot_attribute(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def modify_snapshot_tier(
        self,
        res: "bs_td.ModifySnapshotTierResultTypeDef",
    ) -> "dc_td.ModifySnapshotTierResult":
        return dc_td.ModifySnapshotTierResult.make_one(res)

    def modify_spot_fleet_request(
        self,
        res: "bs_td.ModifySpotFleetRequestResponseTypeDef",
    ) -> "dc_td.ModifySpotFleetRequestResponse":
        return dc_td.ModifySpotFleetRequestResponse.make_one(res)

    def modify_subnet_attribute(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def modify_traffic_mirror_filter_network_services(
        self,
        res: "bs_td.ModifyTrafficMirrorFilterNetworkServicesResultTypeDef",
    ) -> "dc_td.ModifyTrafficMirrorFilterNetworkServicesResult":
        return dc_td.ModifyTrafficMirrorFilterNetworkServicesResult.make_one(res)

    def modify_traffic_mirror_filter_rule(
        self,
        res: "bs_td.ModifyTrafficMirrorFilterRuleResultTypeDef",
    ) -> "dc_td.ModifyTrafficMirrorFilterRuleResult":
        return dc_td.ModifyTrafficMirrorFilterRuleResult.make_one(res)

    def modify_traffic_mirror_session(
        self,
        res: "bs_td.ModifyTrafficMirrorSessionResultTypeDef",
    ) -> "dc_td.ModifyTrafficMirrorSessionResult":
        return dc_td.ModifyTrafficMirrorSessionResult.make_one(res)

    def modify_transit_gateway(
        self,
        res: "bs_td.ModifyTransitGatewayResultTypeDef",
    ) -> "dc_td.ModifyTransitGatewayResult":
        return dc_td.ModifyTransitGatewayResult.make_one(res)

    def modify_transit_gateway_prefix_list_reference(
        self,
        res: "bs_td.ModifyTransitGatewayPrefixListReferenceResultTypeDef",
    ) -> "dc_td.ModifyTransitGatewayPrefixListReferenceResult":
        return dc_td.ModifyTransitGatewayPrefixListReferenceResult.make_one(res)

    def modify_transit_gateway_vpc_attachment(
        self,
        res: "bs_td.ModifyTransitGatewayVpcAttachmentResultTypeDef",
    ) -> "dc_td.ModifyTransitGatewayVpcAttachmentResult":
        return dc_td.ModifyTransitGatewayVpcAttachmentResult.make_one(res)

    def modify_verified_access_endpoint(
        self,
        res: "bs_td.ModifyVerifiedAccessEndpointResultTypeDef",
    ) -> "dc_td.ModifyVerifiedAccessEndpointResult":
        return dc_td.ModifyVerifiedAccessEndpointResult.make_one(res)

    def modify_verified_access_endpoint_policy(
        self,
        res: "bs_td.ModifyVerifiedAccessEndpointPolicyResultTypeDef",
    ) -> "dc_td.ModifyVerifiedAccessEndpointPolicyResult":
        return dc_td.ModifyVerifiedAccessEndpointPolicyResult.make_one(res)

    def modify_verified_access_group(
        self,
        res: "bs_td.ModifyVerifiedAccessGroupResultTypeDef",
    ) -> "dc_td.ModifyVerifiedAccessGroupResult":
        return dc_td.ModifyVerifiedAccessGroupResult.make_one(res)

    def modify_verified_access_group_policy(
        self,
        res: "bs_td.ModifyVerifiedAccessGroupPolicyResultTypeDef",
    ) -> "dc_td.ModifyVerifiedAccessGroupPolicyResult":
        return dc_td.ModifyVerifiedAccessGroupPolicyResult.make_one(res)

    def modify_verified_access_instance(
        self,
        res: "bs_td.ModifyVerifiedAccessInstanceResultTypeDef",
    ) -> "dc_td.ModifyVerifiedAccessInstanceResult":
        return dc_td.ModifyVerifiedAccessInstanceResult.make_one(res)

    def modify_verified_access_instance_logging_configuration(
        self,
        res: "bs_td.ModifyVerifiedAccessInstanceLoggingConfigurationResultTypeDef",
    ) -> "dc_td.ModifyVerifiedAccessInstanceLoggingConfigurationResult":
        return dc_td.ModifyVerifiedAccessInstanceLoggingConfigurationResult.make_one(
            res
        )

    def modify_verified_access_trust_provider(
        self,
        res: "bs_td.ModifyVerifiedAccessTrustProviderResultTypeDef",
    ) -> "dc_td.ModifyVerifiedAccessTrustProviderResult":
        return dc_td.ModifyVerifiedAccessTrustProviderResult.make_one(res)

    def modify_volume(
        self,
        res: "bs_td.ModifyVolumeResultTypeDef",
    ) -> "dc_td.ModifyVolumeResult":
        return dc_td.ModifyVolumeResult.make_one(res)

    def modify_volume_attribute(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def modify_vpc_attribute(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def modify_vpc_block_public_access_exclusion(
        self,
        res: "bs_td.ModifyVpcBlockPublicAccessExclusionResultTypeDef",
    ) -> "dc_td.ModifyVpcBlockPublicAccessExclusionResult":
        return dc_td.ModifyVpcBlockPublicAccessExclusionResult.make_one(res)

    def modify_vpc_block_public_access_options(
        self,
        res: "bs_td.ModifyVpcBlockPublicAccessOptionsResultTypeDef",
    ) -> "dc_td.ModifyVpcBlockPublicAccessOptionsResult":
        return dc_td.ModifyVpcBlockPublicAccessOptionsResult.make_one(res)

    def modify_vpc_endpoint(
        self,
        res: "bs_td.ModifyVpcEndpointResultTypeDef",
    ) -> "dc_td.ModifyVpcEndpointResult":
        return dc_td.ModifyVpcEndpointResult.make_one(res)

    def modify_vpc_endpoint_connection_notification(
        self,
        res: "bs_td.ModifyVpcEndpointConnectionNotificationResultTypeDef",
    ) -> "dc_td.ModifyVpcEndpointConnectionNotificationResult":
        return dc_td.ModifyVpcEndpointConnectionNotificationResult.make_one(res)

    def modify_vpc_endpoint_service_configuration(
        self,
        res: "bs_td.ModifyVpcEndpointServiceConfigurationResultTypeDef",
    ) -> "dc_td.ModifyVpcEndpointServiceConfigurationResult":
        return dc_td.ModifyVpcEndpointServiceConfigurationResult.make_one(res)

    def modify_vpc_endpoint_service_payer_responsibility(
        self,
        res: "bs_td.ModifyVpcEndpointServicePayerResponsibilityResultTypeDef",
    ) -> "dc_td.ModifyVpcEndpointServicePayerResponsibilityResult":
        return dc_td.ModifyVpcEndpointServicePayerResponsibilityResult.make_one(res)

    def modify_vpc_endpoint_service_permissions(
        self,
        res: "bs_td.ModifyVpcEndpointServicePermissionsResultTypeDef",
    ) -> "dc_td.ModifyVpcEndpointServicePermissionsResult":
        return dc_td.ModifyVpcEndpointServicePermissionsResult.make_one(res)

    def modify_vpc_peering_connection_options(
        self,
        res: "bs_td.ModifyVpcPeeringConnectionOptionsResultTypeDef",
    ) -> "dc_td.ModifyVpcPeeringConnectionOptionsResult":
        return dc_td.ModifyVpcPeeringConnectionOptionsResult.make_one(res)

    def modify_vpc_tenancy(
        self,
        res: "bs_td.ModifyVpcTenancyResultTypeDef",
    ) -> "dc_td.ModifyVpcTenancyResult":
        return dc_td.ModifyVpcTenancyResult.make_one(res)

    def modify_vpn_connection(
        self,
        res: "bs_td.ModifyVpnConnectionResultTypeDef",
    ) -> "dc_td.ModifyVpnConnectionResult":
        return dc_td.ModifyVpnConnectionResult.make_one(res)

    def modify_vpn_connection_options(
        self,
        res: "bs_td.ModifyVpnConnectionOptionsResultTypeDef",
    ) -> "dc_td.ModifyVpnConnectionOptionsResult":
        return dc_td.ModifyVpnConnectionOptionsResult.make_one(res)

    def modify_vpn_tunnel_certificate(
        self,
        res: "bs_td.ModifyVpnTunnelCertificateResultTypeDef",
    ) -> "dc_td.ModifyVpnTunnelCertificateResult":
        return dc_td.ModifyVpnTunnelCertificateResult.make_one(res)

    def modify_vpn_tunnel_options(
        self,
        res: "bs_td.ModifyVpnTunnelOptionsResultTypeDef",
    ) -> "dc_td.ModifyVpnTunnelOptionsResult":
        return dc_td.ModifyVpnTunnelOptionsResult.make_one(res)

    def monitor_instances(
        self,
        res: "bs_td.MonitorInstancesResultTypeDef",
    ) -> "dc_td.MonitorInstancesResult":
        return dc_td.MonitorInstancesResult.make_one(res)

    def move_address_to_vpc(
        self,
        res: "bs_td.MoveAddressToVpcResultTypeDef",
    ) -> "dc_td.MoveAddressToVpcResult":
        return dc_td.MoveAddressToVpcResult.make_one(res)

    def move_byoip_cidr_to_ipam(
        self,
        res: "bs_td.MoveByoipCidrToIpamResultTypeDef",
    ) -> "dc_td.MoveByoipCidrToIpamResult":
        return dc_td.MoveByoipCidrToIpamResult.make_one(res)

    def move_capacity_reservation_instances(
        self,
        res: "bs_td.MoveCapacityReservationInstancesResultTypeDef",
    ) -> "dc_td.MoveCapacityReservationInstancesResult":
        return dc_td.MoveCapacityReservationInstancesResult.make_one(res)

    def provision_byoip_cidr(
        self,
        res: "bs_td.ProvisionByoipCidrResultTypeDef",
    ) -> "dc_td.ProvisionByoipCidrResult":
        return dc_td.ProvisionByoipCidrResult.make_one(res)

    def provision_ipam_byoasn(
        self,
        res: "bs_td.ProvisionIpamByoasnResultTypeDef",
    ) -> "dc_td.ProvisionIpamByoasnResult":
        return dc_td.ProvisionIpamByoasnResult.make_one(res)

    def provision_ipam_pool_cidr(
        self,
        res: "bs_td.ProvisionIpamPoolCidrResultTypeDef",
    ) -> "dc_td.ProvisionIpamPoolCidrResult":
        return dc_td.ProvisionIpamPoolCidrResult.make_one(res)

    def provision_public_ipv4_pool_cidr(
        self,
        res: "bs_td.ProvisionPublicIpv4PoolCidrResultTypeDef",
    ) -> "dc_td.ProvisionPublicIpv4PoolCidrResult":
        return dc_td.ProvisionPublicIpv4PoolCidrResult.make_one(res)

    def purchase_capacity_block(
        self,
        res: "bs_td.PurchaseCapacityBlockResultTypeDef",
    ) -> "dc_td.PurchaseCapacityBlockResult":
        return dc_td.PurchaseCapacityBlockResult.make_one(res)

    def purchase_capacity_block_extension(
        self,
        res: "bs_td.PurchaseCapacityBlockExtensionResultTypeDef",
    ) -> "dc_td.PurchaseCapacityBlockExtensionResult":
        return dc_td.PurchaseCapacityBlockExtensionResult.make_one(res)

    def purchase_host_reservation(
        self,
        res: "bs_td.PurchaseHostReservationResultTypeDef",
    ) -> "dc_td.PurchaseHostReservationResult":
        return dc_td.PurchaseHostReservationResult.make_one(res)

    def purchase_reserved_instances_offering(
        self,
        res: "bs_td.PurchaseReservedInstancesOfferingResultTypeDef",
    ) -> "dc_td.PurchaseReservedInstancesOfferingResult":
        return dc_td.PurchaseReservedInstancesOfferingResult.make_one(res)

    def purchase_scheduled_instances(
        self,
        res: "bs_td.PurchaseScheduledInstancesResultTypeDef",
    ) -> "dc_td.PurchaseScheduledInstancesResult":
        return dc_td.PurchaseScheduledInstancesResult.make_one(res)

    def reboot_instances(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def register_image(
        self,
        res: "bs_td.RegisterImageResultTypeDef",
    ) -> "dc_td.RegisterImageResult":
        return dc_td.RegisterImageResult.make_one(res)

    def register_instance_event_notification_attributes(
        self,
        res: "bs_td.RegisterInstanceEventNotificationAttributesResultTypeDef",
    ) -> "dc_td.RegisterInstanceEventNotificationAttributesResult":
        return dc_td.RegisterInstanceEventNotificationAttributesResult.make_one(res)

    def register_transit_gateway_multicast_group_members(
        self,
        res: "bs_td.RegisterTransitGatewayMulticastGroupMembersResultTypeDef",
    ) -> "dc_td.RegisterTransitGatewayMulticastGroupMembersResult":
        return dc_td.RegisterTransitGatewayMulticastGroupMembersResult.make_one(res)

    def register_transit_gateway_multicast_group_sources(
        self,
        res: "bs_td.RegisterTransitGatewayMulticastGroupSourcesResultTypeDef",
    ) -> "dc_td.RegisterTransitGatewayMulticastGroupSourcesResult":
        return dc_td.RegisterTransitGatewayMulticastGroupSourcesResult.make_one(res)

    def reject_capacity_reservation_billing_ownership(
        self,
        res: "bs_td.RejectCapacityReservationBillingOwnershipResultTypeDef",
    ) -> "dc_td.RejectCapacityReservationBillingOwnershipResult":
        return dc_td.RejectCapacityReservationBillingOwnershipResult.make_one(res)

    def reject_transit_gateway_multicast_domain_associations(
        self,
        res: "bs_td.RejectTransitGatewayMulticastDomainAssociationsResultTypeDef",
    ) -> "dc_td.RejectTransitGatewayMulticastDomainAssociationsResult":
        return dc_td.RejectTransitGatewayMulticastDomainAssociationsResult.make_one(res)

    def reject_transit_gateway_peering_attachment(
        self,
        res: "bs_td.RejectTransitGatewayPeeringAttachmentResultTypeDef",
    ) -> "dc_td.RejectTransitGatewayPeeringAttachmentResult":
        return dc_td.RejectTransitGatewayPeeringAttachmentResult.make_one(res)

    def reject_transit_gateway_vpc_attachment(
        self,
        res: "bs_td.RejectTransitGatewayVpcAttachmentResultTypeDef",
    ) -> "dc_td.RejectTransitGatewayVpcAttachmentResult":
        return dc_td.RejectTransitGatewayVpcAttachmentResult.make_one(res)

    def reject_vpc_endpoint_connections(
        self,
        res: "bs_td.RejectVpcEndpointConnectionsResultTypeDef",
    ) -> "dc_td.RejectVpcEndpointConnectionsResult":
        return dc_td.RejectVpcEndpointConnectionsResult.make_one(res)

    def reject_vpc_peering_connection(
        self,
        res: "bs_td.RejectVpcPeeringConnectionResultTypeDef",
    ) -> "dc_td.RejectVpcPeeringConnectionResult":
        return dc_td.RejectVpcPeeringConnectionResult.make_one(res)

    def release_address(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def release_hosts(
        self,
        res: "bs_td.ReleaseHostsResultTypeDef",
    ) -> "dc_td.ReleaseHostsResult":
        return dc_td.ReleaseHostsResult.make_one(res)

    def release_ipam_pool_allocation(
        self,
        res: "bs_td.ReleaseIpamPoolAllocationResultTypeDef",
    ) -> "dc_td.ReleaseIpamPoolAllocationResult":
        return dc_td.ReleaseIpamPoolAllocationResult.make_one(res)

    def replace_iam_instance_profile_association(
        self,
        res: "bs_td.ReplaceIamInstanceProfileAssociationResultTypeDef",
    ) -> "dc_td.ReplaceIamInstanceProfileAssociationResult":
        return dc_td.ReplaceIamInstanceProfileAssociationResult.make_one(res)

    def replace_image_criteria_in_allowed_images_settings(
        self,
        res: "bs_td.ReplaceImageCriteriaInAllowedImagesSettingsResultTypeDef",
    ) -> "dc_td.ReplaceImageCriteriaInAllowedImagesSettingsResult":
        return dc_td.ReplaceImageCriteriaInAllowedImagesSettingsResult.make_one(res)

    def replace_network_acl_association(
        self,
        res: "bs_td.ReplaceNetworkAclAssociationResultTypeDef",
    ) -> "dc_td.ReplaceNetworkAclAssociationResult":
        return dc_td.ReplaceNetworkAclAssociationResult.make_one(res)

    def replace_network_acl_entry(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def replace_route(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def replace_route_table_association(
        self,
        res: "bs_td.ReplaceRouteTableAssociationResultTypeDef",
    ) -> "dc_td.ReplaceRouteTableAssociationResult":
        return dc_td.ReplaceRouteTableAssociationResult.make_one(res)

    def replace_transit_gateway_route(
        self,
        res: "bs_td.ReplaceTransitGatewayRouteResultTypeDef",
    ) -> "dc_td.ReplaceTransitGatewayRouteResult":
        return dc_td.ReplaceTransitGatewayRouteResult.make_one(res)

    def replace_vpn_tunnel(
        self,
        res: "bs_td.ReplaceVpnTunnelResultTypeDef",
    ) -> "dc_td.ReplaceVpnTunnelResult":
        return dc_td.ReplaceVpnTunnelResult.make_one(res)

    def report_instance_status(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def request_spot_fleet(
        self,
        res: "bs_td.RequestSpotFleetResponseTypeDef",
    ) -> "dc_td.RequestSpotFleetResponse":
        return dc_td.RequestSpotFleetResponse.make_one(res)

    def request_spot_instances(
        self,
        res: "bs_td.RequestSpotInstancesResultTypeDef",
    ) -> "dc_td.RequestSpotInstancesResult":
        return dc_td.RequestSpotInstancesResult.make_one(res)

    def reset_address_attribute(
        self,
        res: "bs_td.ResetAddressAttributeResultTypeDef",
    ) -> "dc_td.ResetAddressAttributeResult":
        return dc_td.ResetAddressAttributeResult.make_one(res)

    def reset_ebs_default_kms_key_id(
        self,
        res: "bs_td.ResetEbsDefaultKmsKeyIdResultTypeDef",
    ) -> "dc_td.ResetEbsDefaultKmsKeyIdResult":
        return dc_td.ResetEbsDefaultKmsKeyIdResult.make_one(res)

    def reset_fpga_image_attribute(
        self,
        res: "bs_td.ResetFpgaImageAttributeResultTypeDef",
    ) -> "dc_td.ResetFpgaImageAttributeResult":
        return dc_td.ResetFpgaImageAttributeResult.make_one(res)

    def reset_image_attribute(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def reset_instance_attribute(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def reset_network_interface_attribute(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def reset_snapshot_attribute(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def restore_address_to_classic(
        self,
        res: "bs_td.RestoreAddressToClassicResultTypeDef",
    ) -> "dc_td.RestoreAddressToClassicResult":
        return dc_td.RestoreAddressToClassicResult.make_one(res)

    def restore_image_from_recycle_bin(
        self,
        res: "bs_td.RestoreImageFromRecycleBinResultTypeDef",
    ) -> "dc_td.RestoreImageFromRecycleBinResult":
        return dc_td.RestoreImageFromRecycleBinResult.make_one(res)

    def restore_managed_prefix_list_version(
        self,
        res: "bs_td.RestoreManagedPrefixListVersionResultTypeDef",
    ) -> "dc_td.RestoreManagedPrefixListVersionResult":
        return dc_td.RestoreManagedPrefixListVersionResult.make_one(res)

    def restore_snapshot_from_recycle_bin(
        self,
        res: "bs_td.RestoreSnapshotFromRecycleBinResultTypeDef",
    ) -> "dc_td.RestoreSnapshotFromRecycleBinResult":
        return dc_td.RestoreSnapshotFromRecycleBinResult.make_one(res)

    def restore_snapshot_tier(
        self,
        res: "bs_td.RestoreSnapshotTierResultTypeDef",
    ) -> "dc_td.RestoreSnapshotTierResult":
        return dc_td.RestoreSnapshotTierResult.make_one(res)

    def revoke_client_vpn_ingress(
        self,
        res: "bs_td.RevokeClientVpnIngressResultTypeDef",
    ) -> "dc_td.RevokeClientVpnIngressResult":
        return dc_td.RevokeClientVpnIngressResult.make_one(res)

    def revoke_security_group_egress(
        self,
        res: "bs_td.RevokeSecurityGroupEgressResultTypeDef",
    ) -> "dc_td.RevokeSecurityGroupEgressResult":
        return dc_td.RevokeSecurityGroupEgressResult.make_one(res)

    def revoke_security_group_ingress(
        self,
        res: "bs_td.RevokeSecurityGroupIngressResultTypeDef",
    ) -> "dc_td.RevokeSecurityGroupIngressResult":
        return dc_td.RevokeSecurityGroupIngressResult.make_one(res)

    def run_instances(
        self,
        res: "bs_td.ReservationResponseTypeDef",
    ) -> "dc_td.ReservationResponse":
        return dc_td.ReservationResponse.make_one(res)

    def run_scheduled_instances(
        self,
        res: "bs_td.RunScheduledInstancesResultTypeDef",
    ) -> "dc_td.RunScheduledInstancesResult":
        return dc_td.RunScheduledInstancesResult.make_one(res)

    def search_local_gateway_routes(
        self,
        res: "bs_td.SearchLocalGatewayRoutesResultTypeDef",
    ) -> "dc_td.SearchLocalGatewayRoutesResult":
        return dc_td.SearchLocalGatewayRoutesResult.make_one(res)

    def search_transit_gateway_multicast_groups(
        self,
        res: "bs_td.SearchTransitGatewayMulticastGroupsResultTypeDef",
    ) -> "dc_td.SearchTransitGatewayMulticastGroupsResult":
        return dc_td.SearchTransitGatewayMulticastGroupsResult.make_one(res)

    def search_transit_gateway_routes(
        self,
        res: "bs_td.SearchTransitGatewayRoutesResultTypeDef",
    ) -> "dc_td.SearchTransitGatewayRoutesResult":
        return dc_td.SearchTransitGatewayRoutesResult.make_one(res)

    def send_diagnostic_interrupt(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def start_declarative_policies_report(
        self,
        res: "bs_td.StartDeclarativePoliciesReportResultTypeDef",
    ) -> "dc_td.StartDeclarativePoliciesReportResult":
        return dc_td.StartDeclarativePoliciesReportResult.make_one(res)

    def start_instances(
        self,
        res: "bs_td.StartInstancesResultTypeDef",
    ) -> "dc_td.StartInstancesResult":
        return dc_td.StartInstancesResult.make_one(res)

    def start_network_insights_access_scope_analysis(
        self,
        res: "bs_td.StartNetworkInsightsAccessScopeAnalysisResultTypeDef",
    ) -> "dc_td.StartNetworkInsightsAccessScopeAnalysisResult":
        return dc_td.StartNetworkInsightsAccessScopeAnalysisResult.make_one(res)

    def start_network_insights_analysis(
        self,
        res: "bs_td.StartNetworkInsightsAnalysisResultTypeDef",
    ) -> "dc_td.StartNetworkInsightsAnalysisResult":
        return dc_td.StartNetworkInsightsAnalysisResult.make_one(res)

    def start_vpc_endpoint_service_private_dns_verification(
        self,
        res: "bs_td.StartVpcEndpointServicePrivateDnsVerificationResultTypeDef",
    ) -> "dc_td.StartVpcEndpointServicePrivateDnsVerificationResult":
        return dc_td.StartVpcEndpointServicePrivateDnsVerificationResult.make_one(res)

    def stop_instances(
        self,
        res: "bs_td.StopInstancesResultTypeDef",
    ) -> "dc_td.StopInstancesResult":
        return dc_td.StopInstancesResult.make_one(res)

    def terminate_client_vpn_connections(
        self,
        res: "bs_td.TerminateClientVpnConnectionsResultTypeDef",
    ) -> "dc_td.TerminateClientVpnConnectionsResult":
        return dc_td.TerminateClientVpnConnectionsResult.make_one(res)

    def terminate_instances(
        self,
        res: "bs_td.TerminateInstancesResultTypeDef",
    ) -> "dc_td.TerminateInstancesResult":
        return dc_td.TerminateInstancesResult.make_one(res)

    def unassign_ipv6_addresses(
        self,
        res: "bs_td.UnassignIpv6AddressesResultTypeDef",
    ) -> "dc_td.UnassignIpv6AddressesResult":
        return dc_td.UnassignIpv6AddressesResult.make_one(res)

    def unassign_private_ip_addresses(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def unassign_private_nat_gateway_address(
        self,
        res: "bs_td.UnassignPrivateNatGatewayAddressResultTypeDef",
    ) -> "dc_td.UnassignPrivateNatGatewayAddressResult":
        return dc_td.UnassignPrivateNatGatewayAddressResult.make_one(res)

    def unlock_snapshot(
        self,
        res: "bs_td.UnlockSnapshotResultTypeDef",
    ) -> "dc_td.UnlockSnapshotResult":
        return dc_td.UnlockSnapshotResult.make_one(res)

    def unmonitor_instances(
        self,
        res: "bs_td.UnmonitorInstancesResultTypeDef",
    ) -> "dc_td.UnmonitorInstancesResult":
        return dc_td.UnmonitorInstancesResult.make_one(res)

    def update_security_group_rule_descriptions_egress(
        self,
        res: "bs_td.UpdateSecurityGroupRuleDescriptionsEgressResultTypeDef",
    ) -> "dc_td.UpdateSecurityGroupRuleDescriptionsEgressResult":
        return dc_td.UpdateSecurityGroupRuleDescriptionsEgressResult.make_one(res)

    def update_security_group_rule_descriptions_ingress(
        self,
        res: "bs_td.UpdateSecurityGroupRuleDescriptionsIngressResultTypeDef",
    ) -> "dc_td.UpdateSecurityGroupRuleDescriptionsIngressResult":
        return dc_td.UpdateSecurityGroupRuleDescriptionsIngressResult.make_one(res)

    def withdraw_byoip_cidr(
        self,
        res: "bs_td.WithdrawByoipCidrResultTypeDef",
    ) -> "dc_td.WithdrawByoipCidrResult":
        return dc_td.WithdrawByoipCidrResult.make_one(res)


ec2_caster = EC2Caster()
