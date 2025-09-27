# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_directconnect import type_defs as bs_td


class DIRECTCONNECTCaster:

    def accept_direct_connect_gateway_association_proposal(
        self,
        res: "bs_td.AcceptDirectConnectGatewayAssociationProposalResultTypeDef",
    ) -> "dc_td.AcceptDirectConnectGatewayAssociationProposalResult":
        return dc_td.AcceptDirectConnectGatewayAssociationProposalResult.make_one(res)

    def allocate_connection_on_interconnect(
        self,
        res: "bs_td.ConnectionResponseTypeDef",
    ) -> "dc_td.ConnectionResponse":
        return dc_td.ConnectionResponse.make_one(res)

    def allocate_hosted_connection(
        self,
        res: "bs_td.ConnectionResponseTypeDef",
    ) -> "dc_td.ConnectionResponse":
        return dc_td.ConnectionResponse.make_one(res)

    def allocate_private_virtual_interface(
        self,
        res: "bs_td.VirtualInterfaceResponseTypeDef",
    ) -> "dc_td.VirtualInterfaceResponse":
        return dc_td.VirtualInterfaceResponse.make_one(res)

    def allocate_public_virtual_interface(
        self,
        res: "bs_td.VirtualInterfaceResponseTypeDef",
    ) -> "dc_td.VirtualInterfaceResponse":
        return dc_td.VirtualInterfaceResponse.make_one(res)

    def allocate_transit_virtual_interface(
        self,
        res: "bs_td.AllocateTransitVirtualInterfaceResultTypeDef",
    ) -> "dc_td.AllocateTransitVirtualInterfaceResult":
        return dc_td.AllocateTransitVirtualInterfaceResult.make_one(res)

    def associate_connection_with_lag(
        self,
        res: "bs_td.ConnectionResponseTypeDef",
    ) -> "dc_td.ConnectionResponse":
        return dc_td.ConnectionResponse.make_one(res)

    def associate_hosted_connection(
        self,
        res: "bs_td.ConnectionResponseTypeDef",
    ) -> "dc_td.ConnectionResponse":
        return dc_td.ConnectionResponse.make_one(res)

    def associate_mac_sec_key(
        self,
        res: "bs_td.AssociateMacSecKeyResponseTypeDef",
    ) -> "dc_td.AssociateMacSecKeyResponse":
        return dc_td.AssociateMacSecKeyResponse.make_one(res)

    def associate_virtual_interface(
        self,
        res: "bs_td.VirtualInterfaceResponseTypeDef",
    ) -> "dc_td.VirtualInterfaceResponse":
        return dc_td.VirtualInterfaceResponse.make_one(res)

    def confirm_connection(
        self,
        res: "bs_td.ConfirmConnectionResponseTypeDef",
    ) -> "dc_td.ConfirmConnectionResponse":
        return dc_td.ConfirmConnectionResponse.make_one(res)

    def confirm_customer_agreement(
        self,
        res: "bs_td.ConfirmCustomerAgreementResponseTypeDef",
    ) -> "dc_td.ConfirmCustomerAgreementResponse":
        return dc_td.ConfirmCustomerAgreementResponse.make_one(res)

    def confirm_private_virtual_interface(
        self,
        res: "bs_td.ConfirmPrivateVirtualInterfaceResponseTypeDef",
    ) -> "dc_td.ConfirmPrivateVirtualInterfaceResponse":
        return dc_td.ConfirmPrivateVirtualInterfaceResponse.make_one(res)

    def confirm_public_virtual_interface(
        self,
        res: "bs_td.ConfirmPublicVirtualInterfaceResponseTypeDef",
    ) -> "dc_td.ConfirmPublicVirtualInterfaceResponse":
        return dc_td.ConfirmPublicVirtualInterfaceResponse.make_one(res)

    def confirm_transit_virtual_interface(
        self,
        res: "bs_td.ConfirmTransitVirtualInterfaceResponseTypeDef",
    ) -> "dc_td.ConfirmTransitVirtualInterfaceResponse":
        return dc_td.ConfirmTransitVirtualInterfaceResponse.make_one(res)

    def create_bgp_peer(
        self,
        res: "bs_td.CreateBGPPeerResponseTypeDef",
    ) -> "dc_td.CreateBGPPeerResponse":
        return dc_td.CreateBGPPeerResponse.make_one(res)

    def create_connection(
        self,
        res: "bs_td.ConnectionResponseTypeDef",
    ) -> "dc_td.ConnectionResponse":
        return dc_td.ConnectionResponse.make_one(res)

    def create_direct_connect_gateway(
        self,
        res: "bs_td.CreateDirectConnectGatewayResultTypeDef",
    ) -> "dc_td.CreateDirectConnectGatewayResult":
        return dc_td.CreateDirectConnectGatewayResult.make_one(res)

    def create_direct_connect_gateway_association(
        self,
        res: "bs_td.CreateDirectConnectGatewayAssociationResultTypeDef",
    ) -> "dc_td.CreateDirectConnectGatewayAssociationResult":
        return dc_td.CreateDirectConnectGatewayAssociationResult.make_one(res)

    def create_direct_connect_gateway_association_proposal(
        self,
        res: "bs_td.CreateDirectConnectGatewayAssociationProposalResultTypeDef",
    ) -> "dc_td.CreateDirectConnectGatewayAssociationProposalResult":
        return dc_td.CreateDirectConnectGatewayAssociationProposalResult.make_one(res)

    def create_interconnect(
        self,
        res: "bs_td.InterconnectResponseTypeDef",
    ) -> "dc_td.InterconnectResponse":
        return dc_td.InterconnectResponse.make_one(res)

    def create_lag(
        self,
        res: "bs_td.LagResponseTypeDef",
    ) -> "dc_td.LagResponse":
        return dc_td.LagResponse.make_one(res)

    def create_private_virtual_interface(
        self,
        res: "bs_td.VirtualInterfaceResponseTypeDef",
    ) -> "dc_td.VirtualInterfaceResponse":
        return dc_td.VirtualInterfaceResponse.make_one(res)

    def create_public_virtual_interface(
        self,
        res: "bs_td.VirtualInterfaceResponseTypeDef",
    ) -> "dc_td.VirtualInterfaceResponse":
        return dc_td.VirtualInterfaceResponse.make_one(res)

    def create_transit_virtual_interface(
        self,
        res: "bs_td.CreateTransitVirtualInterfaceResultTypeDef",
    ) -> "dc_td.CreateTransitVirtualInterfaceResult":
        return dc_td.CreateTransitVirtualInterfaceResult.make_one(res)

    def delete_bgp_peer(
        self,
        res: "bs_td.DeleteBGPPeerResponseTypeDef",
    ) -> "dc_td.DeleteBGPPeerResponse":
        return dc_td.DeleteBGPPeerResponse.make_one(res)

    def delete_connection(
        self,
        res: "bs_td.ConnectionResponseTypeDef",
    ) -> "dc_td.ConnectionResponse":
        return dc_td.ConnectionResponse.make_one(res)

    def delete_direct_connect_gateway(
        self,
        res: "bs_td.DeleteDirectConnectGatewayResultTypeDef",
    ) -> "dc_td.DeleteDirectConnectGatewayResult":
        return dc_td.DeleteDirectConnectGatewayResult.make_one(res)

    def delete_direct_connect_gateway_association(
        self,
        res: "bs_td.DeleteDirectConnectGatewayAssociationResultTypeDef",
    ) -> "dc_td.DeleteDirectConnectGatewayAssociationResult":
        return dc_td.DeleteDirectConnectGatewayAssociationResult.make_one(res)

    def delete_direct_connect_gateway_association_proposal(
        self,
        res: "bs_td.DeleteDirectConnectGatewayAssociationProposalResultTypeDef",
    ) -> "dc_td.DeleteDirectConnectGatewayAssociationProposalResult":
        return dc_td.DeleteDirectConnectGatewayAssociationProposalResult.make_one(res)

    def delete_interconnect(
        self,
        res: "bs_td.DeleteInterconnectResponseTypeDef",
    ) -> "dc_td.DeleteInterconnectResponse":
        return dc_td.DeleteInterconnectResponse.make_one(res)

    def delete_lag(
        self,
        res: "bs_td.LagResponseTypeDef",
    ) -> "dc_td.LagResponse":
        return dc_td.LagResponse.make_one(res)

    def delete_virtual_interface(
        self,
        res: "bs_td.DeleteVirtualInterfaceResponseTypeDef",
    ) -> "dc_td.DeleteVirtualInterfaceResponse":
        return dc_td.DeleteVirtualInterfaceResponse.make_one(res)

    def describe_connection_loa(
        self,
        res: "bs_td.DescribeConnectionLoaResponseTypeDef",
    ) -> "dc_td.DescribeConnectionLoaResponse":
        return dc_td.DescribeConnectionLoaResponse.make_one(res)

    def describe_connections(
        self,
        res: "bs_td.ConnectionsTypeDef",
    ) -> "dc_td.Connections":
        return dc_td.Connections.make_one(res)

    def describe_connections_on_interconnect(
        self,
        res: "bs_td.ConnectionsTypeDef",
    ) -> "dc_td.Connections":
        return dc_td.Connections.make_one(res)

    def describe_customer_metadata(
        self,
        res: "bs_td.DescribeCustomerMetadataResponseTypeDef",
    ) -> "dc_td.DescribeCustomerMetadataResponse":
        return dc_td.DescribeCustomerMetadataResponse.make_one(res)

    def describe_direct_connect_gateway_association_proposals(
        self,
        res: "bs_td.DescribeDirectConnectGatewayAssociationProposalsResultTypeDef",
    ) -> "dc_td.DescribeDirectConnectGatewayAssociationProposalsResult":
        return dc_td.DescribeDirectConnectGatewayAssociationProposalsResult.make_one(
            res
        )

    def describe_direct_connect_gateway_associations(
        self,
        res: "bs_td.DescribeDirectConnectGatewayAssociationsResultTypeDef",
    ) -> "dc_td.DescribeDirectConnectGatewayAssociationsResult":
        return dc_td.DescribeDirectConnectGatewayAssociationsResult.make_one(res)

    def describe_direct_connect_gateway_attachments(
        self,
        res: "bs_td.DescribeDirectConnectGatewayAttachmentsResultTypeDef",
    ) -> "dc_td.DescribeDirectConnectGatewayAttachmentsResult":
        return dc_td.DescribeDirectConnectGatewayAttachmentsResult.make_one(res)

    def describe_direct_connect_gateways(
        self,
        res: "bs_td.DescribeDirectConnectGatewaysResultTypeDef",
    ) -> "dc_td.DescribeDirectConnectGatewaysResult":
        return dc_td.DescribeDirectConnectGatewaysResult.make_one(res)

    def describe_hosted_connections(
        self,
        res: "bs_td.ConnectionsTypeDef",
    ) -> "dc_td.Connections":
        return dc_td.Connections.make_one(res)

    def describe_interconnect_loa(
        self,
        res: "bs_td.DescribeInterconnectLoaResponseTypeDef",
    ) -> "dc_td.DescribeInterconnectLoaResponse":
        return dc_td.DescribeInterconnectLoaResponse.make_one(res)

    def describe_interconnects(
        self,
        res: "bs_td.InterconnectsTypeDef",
    ) -> "dc_td.Interconnects":
        return dc_td.Interconnects.make_one(res)

    def describe_lags(
        self,
        res: "bs_td.LagsTypeDef",
    ) -> "dc_td.Lags":
        return dc_td.Lags.make_one(res)

    def describe_loa(
        self,
        res: "bs_td.LoaResponseTypeDef",
    ) -> "dc_td.LoaResponse":
        return dc_td.LoaResponse.make_one(res)

    def describe_locations(
        self,
        res: "bs_td.LocationsTypeDef",
    ) -> "dc_td.Locations":
        return dc_td.Locations.make_one(res)

    def describe_router_configuration(
        self,
        res: "bs_td.DescribeRouterConfigurationResponseTypeDef",
    ) -> "dc_td.DescribeRouterConfigurationResponse":
        return dc_td.DescribeRouterConfigurationResponse.make_one(res)

    def describe_tags(
        self,
        res: "bs_td.DescribeTagsResponseTypeDef",
    ) -> "dc_td.DescribeTagsResponse":
        return dc_td.DescribeTagsResponse.make_one(res)

    def describe_virtual_gateways(
        self,
        res: "bs_td.VirtualGatewaysTypeDef",
    ) -> "dc_td.VirtualGateways":
        return dc_td.VirtualGateways.make_one(res)

    def describe_virtual_interfaces(
        self,
        res: "bs_td.VirtualInterfacesTypeDef",
    ) -> "dc_td.VirtualInterfaces":
        return dc_td.VirtualInterfaces.make_one(res)

    def disassociate_connection_from_lag(
        self,
        res: "bs_td.ConnectionResponseTypeDef",
    ) -> "dc_td.ConnectionResponse":
        return dc_td.ConnectionResponse.make_one(res)

    def disassociate_mac_sec_key(
        self,
        res: "bs_td.DisassociateMacSecKeyResponseTypeDef",
    ) -> "dc_td.DisassociateMacSecKeyResponse":
        return dc_td.DisassociateMacSecKeyResponse.make_one(res)

    def list_virtual_interface_test_history(
        self,
        res: "bs_td.ListVirtualInterfaceTestHistoryResponseTypeDef",
    ) -> "dc_td.ListVirtualInterfaceTestHistoryResponse":
        return dc_td.ListVirtualInterfaceTestHistoryResponse.make_one(res)

    def start_bgp_failover_test(
        self,
        res: "bs_td.StartBgpFailoverTestResponseTypeDef",
    ) -> "dc_td.StartBgpFailoverTestResponse":
        return dc_td.StartBgpFailoverTestResponse.make_one(res)

    def stop_bgp_failover_test(
        self,
        res: "bs_td.StopBgpFailoverTestResponseTypeDef",
    ) -> "dc_td.StopBgpFailoverTestResponse":
        return dc_td.StopBgpFailoverTestResponse.make_one(res)

    def update_connection(
        self,
        res: "bs_td.ConnectionResponseTypeDef",
    ) -> "dc_td.ConnectionResponse":
        return dc_td.ConnectionResponse.make_one(res)

    def update_direct_connect_gateway(
        self,
        res: "bs_td.UpdateDirectConnectGatewayResponseTypeDef",
    ) -> "dc_td.UpdateDirectConnectGatewayResponse":
        return dc_td.UpdateDirectConnectGatewayResponse.make_one(res)

    def update_direct_connect_gateway_association(
        self,
        res: "bs_td.UpdateDirectConnectGatewayAssociationResultTypeDef",
    ) -> "dc_td.UpdateDirectConnectGatewayAssociationResult":
        return dc_td.UpdateDirectConnectGatewayAssociationResult.make_one(res)

    def update_lag(
        self,
        res: "bs_td.LagResponseTypeDef",
    ) -> "dc_td.LagResponse":
        return dc_td.LagResponse.make_one(res)

    def update_virtual_interface_attributes(
        self,
        res: "bs_td.VirtualInterfaceResponseTypeDef",
    ) -> "dc_td.VirtualInterfaceResponse":
        return dc_td.VirtualInterfaceResponse.make_one(res)


directconnect_caster = DIRECTCONNECTCaster()
