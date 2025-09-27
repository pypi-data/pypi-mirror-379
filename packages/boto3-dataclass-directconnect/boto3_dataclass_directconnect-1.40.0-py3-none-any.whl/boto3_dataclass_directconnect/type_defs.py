# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_directconnect import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class RouteFilterPrefix:
    boto3_raw_data: "type_defs.RouteFilterPrefixTypeDef" = dataclasses.field()

    cidr = field("cidr")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RouteFilterPrefixTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteFilterPrefixTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResponseMetadata:
    boto3_raw_data: "type_defs.ResponseMetadataTypeDef" = dataclasses.field()

    RequestId = field("RequestId")
    HTTPStatusCode = field("HTTPStatusCode")
    HTTPHeaders = field("HTTPHeaders")
    RetryAttempts = field("RetryAttempts")
    HostId = field("HostId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResponseMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResponseMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AllocateConnectionOnInterconnectRequest:
    boto3_raw_data: "type_defs.AllocateConnectionOnInterconnectRequestTypeDef" = (
        dataclasses.field()
    )

    bandwidth = field("bandwidth")
    connectionName = field("connectionName")
    ownerAccount = field("ownerAccount")
    interconnectId = field("interconnectId")
    vlan = field("vlan")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AllocateConnectionOnInterconnectRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AllocateConnectionOnInterconnectRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Tag:
    boto3_raw_data: "type_defs.TagTypeDef" = dataclasses.field()

    key = field("key")
    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TagTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TagTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateConnectionWithLagRequest:
    boto3_raw_data: "type_defs.AssociateConnectionWithLagRequestTypeDef" = (
        dataclasses.field()
    )

    connectionId = field("connectionId")
    lagId = field("lagId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateConnectionWithLagRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateConnectionWithLagRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateHostedConnectionRequest:
    boto3_raw_data: "type_defs.AssociateHostedConnectionRequestTypeDef" = (
        dataclasses.field()
    )

    connectionId = field("connectionId")
    parentConnectionId = field("parentConnectionId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AssociateHostedConnectionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateHostedConnectionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateMacSecKeyRequest:
    boto3_raw_data: "type_defs.AssociateMacSecKeyRequestTypeDef" = dataclasses.field()

    connectionId = field("connectionId")
    secretARN = field("secretARN")
    ckn = field("ckn")
    cak = field("cak")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociateMacSecKeyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateMacSecKeyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MacSecKey:
    boto3_raw_data: "type_defs.MacSecKeyTypeDef" = dataclasses.field()

    secretARN = field("secretARN")
    ckn = field("ckn")
    state = field("state")
    startOn = field("startOn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MacSecKeyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MacSecKeyTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateVirtualInterfaceRequest:
    boto3_raw_data: "type_defs.AssociateVirtualInterfaceRequestTypeDef" = (
        dataclasses.field()
    )

    virtualInterfaceId = field("virtualInterfaceId")
    connectionId = field("connectionId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AssociateVirtualInterfaceRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateVirtualInterfaceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociatedCoreNetwork:
    boto3_raw_data: "type_defs.AssociatedCoreNetworkTypeDef" = dataclasses.field()

    id = field("id")
    ownerAccount = field("ownerAccount")
    attachmentId = field("attachmentId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociatedCoreNetworkTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociatedCoreNetworkTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociatedGateway:
    boto3_raw_data: "type_defs.AssociatedGatewayTypeDef" = dataclasses.field()

    id = field("id")
    type = field("type")
    ownerAccount = field("ownerAccount")
    region = field("region")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AssociatedGatewayTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociatedGatewayTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BGPPeer:
    boto3_raw_data: "type_defs.BGPPeerTypeDef" = dataclasses.field()

    bgpPeerId = field("bgpPeerId")
    asn = field("asn")
    asnLong = field("asnLong")
    authKey = field("authKey")
    addressFamily = field("addressFamily")
    amazonAddress = field("amazonAddress")
    customerAddress = field("customerAddress")
    bgpPeerState = field("bgpPeerState")
    bgpStatus = field("bgpStatus")
    awsDeviceV2 = field("awsDeviceV2")
    awsLogicalDeviceId = field("awsLogicalDeviceId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BGPPeerTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BGPPeerTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfirmConnectionRequest:
    boto3_raw_data: "type_defs.ConfirmConnectionRequestTypeDef" = dataclasses.field()

    connectionId = field("connectionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConfirmConnectionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfirmConnectionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfirmCustomerAgreementRequest:
    boto3_raw_data: "type_defs.ConfirmCustomerAgreementRequestTypeDef" = (
        dataclasses.field()
    )

    agreementName = field("agreementName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ConfirmCustomerAgreementRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfirmCustomerAgreementRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfirmPrivateVirtualInterfaceRequest:
    boto3_raw_data: "type_defs.ConfirmPrivateVirtualInterfaceRequestTypeDef" = (
        dataclasses.field()
    )

    virtualInterfaceId = field("virtualInterfaceId")
    virtualGatewayId = field("virtualGatewayId")
    directConnectGatewayId = field("directConnectGatewayId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ConfirmPrivateVirtualInterfaceRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfirmPrivateVirtualInterfaceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfirmPublicVirtualInterfaceRequest:
    boto3_raw_data: "type_defs.ConfirmPublicVirtualInterfaceRequestTypeDef" = (
        dataclasses.field()
    )

    virtualInterfaceId = field("virtualInterfaceId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ConfirmPublicVirtualInterfaceRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfirmPublicVirtualInterfaceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfirmTransitVirtualInterfaceRequest:
    boto3_raw_data: "type_defs.ConfirmTransitVirtualInterfaceRequestTypeDef" = (
        dataclasses.field()
    )

    virtualInterfaceId = field("virtualInterfaceId")
    directConnectGatewayId = field("directConnectGatewayId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ConfirmTransitVirtualInterfaceRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfirmTransitVirtualInterfaceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NewBGPPeer:
    boto3_raw_data: "type_defs.NewBGPPeerTypeDef" = dataclasses.field()

    asn = field("asn")
    asnLong = field("asnLong")
    authKey = field("authKey")
    addressFamily = field("addressFamily")
    amazonAddress = field("amazonAddress")
    customerAddress = field("customerAddress")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NewBGPPeerTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.NewBGPPeerTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomerAgreement:
    boto3_raw_data: "type_defs.CustomerAgreementTypeDef" = dataclasses.field()

    agreementName = field("agreementName")
    status = field("status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CustomerAgreementTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomerAgreementTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBGPPeerRequest:
    boto3_raw_data: "type_defs.DeleteBGPPeerRequestTypeDef" = dataclasses.field()

    virtualInterfaceId = field("virtualInterfaceId")
    asn = field("asn")
    asnLong = field("asnLong")
    customerAddress = field("customerAddress")
    bgpPeerId = field("bgpPeerId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteBGPPeerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBGPPeerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteConnectionRequest:
    boto3_raw_data: "type_defs.DeleteConnectionRequestTypeDef" = dataclasses.field()

    connectionId = field("connectionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteConnectionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteConnectionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDirectConnectGatewayAssociationProposalRequest:
    boto3_raw_data: (
        "type_defs.DeleteDirectConnectGatewayAssociationProposalRequestTypeDef"
    ) = dataclasses.field()

    proposalId = field("proposalId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteDirectConnectGatewayAssociationProposalRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.DeleteDirectConnectGatewayAssociationProposalRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDirectConnectGatewayAssociationRequest:
    boto3_raw_data: "type_defs.DeleteDirectConnectGatewayAssociationRequestTypeDef" = (
        dataclasses.field()
    )

    associationId = field("associationId")
    directConnectGatewayId = field("directConnectGatewayId")
    virtualGatewayId = field("virtualGatewayId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteDirectConnectGatewayAssociationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDirectConnectGatewayAssociationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDirectConnectGatewayRequest:
    boto3_raw_data: "type_defs.DeleteDirectConnectGatewayRequestTypeDef" = (
        dataclasses.field()
    )

    directConnectGatewayId = field("directConnectGatewayId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteDirectConnectGatewayRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDirectConnectGatewayRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteInterconnectRequest:
    boto3_raw_data: "type_defs.DeleteInterconnectRequestTypeDef" = dataclasses.field()

    interconnectId = field("interconnectId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteInterconnectRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteInterconnectRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteLagRequest:
    boto3_raw_data: "type_defs.DeleteLagRequestTypeDef" = dataclasses.field()

    lagId = field("lagId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteLagRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteLagRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteVirtualInterfaceRequest:
    boto3_raw_data: "type_defs.DeleteVirtualInterfaceRequestTypeDef" = (
        dataclasses.field()
    )

    virtualInterfaceId = field("virtualInterfaceId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteVirtualInterfaceRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteVirtualInterfaceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeConnectionLoaRequest:
    boto3_raw_data: "type_defs.DescribeConnectionLoaRequestTypeDef" = (
        dataclasses.field()
    )

    connectionId = field("connectionId")
    providerName = field("providerName")
    loaContentType = field("loaContentType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeConnectionLoaRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeConnectionLoaRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Loa:
    boto3_raw_data: "type_defs.LoaTypeDef" = dataclasses.field()

    loaContent = field("loaContent")
    loaContentType = field("loaContentType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LoaTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LoaTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeConnectionsOnInterconnectRequest:
    boto3_raw_data: "type_defs.DescribeConnectionsOnInterconnectRequestTypeDef" = (
        dataclasses.field()
    )

    interconnectId = field("interconnectId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeConnectionsOnInterconnectRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeConnectionsOnInterconnectRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeConnectionsRequest:
    boto3_raw_data: "type_defs.DescribeConnectionsRequestTypeDef" = dataclasses.field()

    connectionId = field("connectionId")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeConnectionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeConnectionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDirectConnectGatewayAssociationProposalsRequest:
    boto3_raw_data: (
        "type_defs.DescribeDirectConnectGatewayAssociationProposalsRequestTypeDef"
    ) = dataclasses.field()

    directConnectGatewayId = field("directConnectGatewayId")
    proposalId = field("proposalId")
    associatedGatewayId = field("associatedGatewayId")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDirectConnectGatewayAssociationProposalsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.DescribeDirectConnectGatewayAssociationProposalsRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PaginatorConfig:
    boto3_raw_data: "type_defs.PaginatorConfigTypeDef" = dataclasses.field()

    MaxItems = field("MaxItems")
    PageSize = field("PageSize")
    StartingToken = field("StartingToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PaginatorConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PaginatorConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDirectConnectGatewayAssociationsRequest:
    boto3_raw_data: (
        "type_defs.DescribeDirectConnectGatewayAssociationsRequestTypeDef"
    ) = dataclasses.field()

    associationId = field("associationId")
    associatedGatewayId = field("associatedGatewayId")
    directConnectGatewayId = field("directConnectGatewayId")
    maxResults = field("maxResults")
    nextToken = field("nextToken")
    virtualGatewayId = field("virtualGatewayId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDirectConnectGatewayAssociationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.DescribeDirectConnectGatewayAssociationsRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDirectConnectGatewayAttachmentsRequest:
    boto3_raw_data: (
        "type_defs.DescribeDirectConnectGatewayAttachmentsRequestTypeDef"
    ) = dataclasses.field()

    directConnectGatewayId = field("directConnectGatewayId")
    virtualInterfaceId = field("virtualInterfaceId")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDirectConnectGatewayAttachmentsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.DescribeDirectConnectGatewayAttachmentsRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DirectConnectGatewayAttachment:
    boto3_raw_data: "type_defs.DirectConnectGatewayAttachmentTypeDef" = (
        dataclasses.field()
    )

    directConnectGatewayId = field("directConnectGatewayId")
    virtualInterfaceId = field("virtualInterfaceId")
    virtualInterfaceRegion = field("virtualInterfaceRegion")
    virtualInterfaceOwnerAccount = field("virtualInterfaceOwnerAccount")
    attachmentState = field("attachmentState")
    attachmentType = field("attachmentType")
    stateChangeError = field("stateChangeError")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DirectConnectGatewayAttachmentTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DirectConnectGatewayAttachmentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDirectConnectGatewaysRequest:
    boto3_raw_data: "type_defs.DescribeDirectConnectGatewaysRequestTypeDef" = (
        dataclasses.field()
    )

    directConnectGatewayId = field("directConnectGatewayId")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDirectConnectGatewaysRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDirectConnectGatewaysRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeHostedConnectionsRequest:
    boto3_raw_data: "type_defs.DescribeHostedConnectionsRequestTypeDef" = (
        dataclasses.field()
    )

    connectionId = field("connectionId")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeHostedConnectionsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeHostedConnectionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeInterconnectLoaRequest:
    boto3_raw_data: "type_defs.DescribeInterconnectLoaRequestTypeDef" = (
        dataclasses.field()
    )

    interconnectId = field("interconnectId")
    providerName = field("providerName")
    loaContentType = field("loaContentType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeInterconnectLoaRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeInterconnectLoaRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeInterconnectsRequest:
    boto3_raw_data: "type_defs.DescribeInterconnectsRequestTypeDef" = (
        dataclasses.field()
    )

    interconnectId = field("interconnectId")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeInterconnectsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeInterconnectsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeLagsRequest:
    boto3_raw_data: "type_defs.DescribeLagsRequestTypeDef" = dataclasses.field()

    lagId = field("lagId")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeLagsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeLagsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeLoaRequest:
    boto3_raw_data: "type_defs.DescribeLoaRequestTypeDef" = dataclasses.field()

    connectionId = field("connectionId")
    providerName = field("providerName")
    loaContentType = field("loaContentType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeLoaRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeLoaRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRouterConfigurationRequest:
    boto3_raw_data: "type_defs.DescribeRouterConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    virtualInterfaceId = field("virtualInterfaceId")
    routerTypeIdentifier = field("routerTypeIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeRouterConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRouterConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouterType:
    boto3_raw_data: "type_defs.RouterTypeTypeDef" = dataclasses.field()

    vendor = field("vendor")
    platform = field("platform")
    software = field("software")
    xsltTemplateName = field("xsltTemplateName")
    xsltTemplateNameForMacSec = field("xsltTemplateNameForMacSec")
    routerTypeIdentifier = field("routerTypeIdentifier")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RouterTypeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RouterTypeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTagsRequest:
    boto3_raw_data: "type_defs.DescribeTagsRequestTypeDef" = dataclasses.field()

    resourceArns = field("resourceArns")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeTagsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTagsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeVirtualInterfacesRequest:
    boto3_raw_data: "type_defs.DescribeVirtualInterfacesRequestTypeDef" = (
        dataclasses.field()
    )

    connectionId = field("connectionId")
    virtualInterfaceId = field("virtualInterfaceId")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeVirtualInterfacesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeVirtualInterfacesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateConnectionFromLagRequest:
    boto3_raw_data: "type_defs.DisassociateConnectionFromLagRequestTypeDef" = (
        dataclasses.field()
    )

    connectionId = field("connectionId")
    lagId = field("lagId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateConnectionFromLagRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateConnectionFromLagRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateMacSecKeyRequest:
    boto3_raw_data: "type_defs.DisassociateMacSecKeyRequestTypeDef" = (
        dataclasses.field()
    )

    connectionId = field("connectionId")
    secretARN = field("secretARN")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DisassociateMacSecKeyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateMacSecKeyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVirtualInterfaceTestHistoryRequest:
    boto3_raw_data: "type_defs.ListVirtualInterfaceTestHistoryRequestTypeDef" = (
        dataclasses.field()
    )

    testId = field("testId")
    virtualInterfaceId = field("virtualInterfaceId")
    bgpPeers = field("bgpPeers")
    status = field("status")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListVirtualInterfaceTestHistoryRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVirtualInterfaceTestHistoryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VirtualInterfaceTestHistory:
    boto3_raw_data: "type_defs.VirtualInterfaceTestHistoryTypeDef" = dataclasses.field()

    testId = field("testId")
    virtualInterfaceId = field("virtualInterfaceId")
    bgpPeers = field("bgpPeers")
    status = field("status")
    ownerAccount = field("ownerAccount")
    testDurationInMinutes = field("testDurationInMinutes")
    startTime = field("startTime")
    endTime = field("endTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VirtualInterfaceTestHistoryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VirtualInterfaceTestHistoryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Location:
    boto3_raw_data: "type_defs.LocationTypeDef" = dataclasses.field()

    locationCode = field("locationCode")
    locationName = field("locationName")
    region = field("region")
    availablePortSpeeds = field("availablePortSpeeds")
    availableProviders = field("availableProviders")
    availableMacSecPortSpeeds = field("availableMacSecPortSpeeds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LocationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LocationTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartBgpFailoverTestRequest:
    boto3_raw_data: "type_defs.StartBgpFailoverTestRequestTypeDef" = dataclasses.field()

    virtualInterfaceId = field("virtualInterfaceId")
    bgpPeers = field("bgpPeers")
    testDurationInMinutes = field("testDurationInMinutes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartBgpFailoverTestRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartBgpFailoverTestRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopBgpFailoverTestRequest:
    boto3_raw_data: "type_defs.StopBgpFailoverTestRequestTypeDef" = dataclasses.field()

    virtualInterfaceId = field("virtualInterfaceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopBgpFailoverTestRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopBgpFailoverTestRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UntagResourceRequest:
    boto3_raw_data: "type_defs.UntagResourceRequestTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")
    tagKeys = field("tagKeys")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UntagResourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UntagResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateConnectionRequest:
    boto3_raw_data: "type_defs.UpdateConnectionRequestTypeDef" = dataclasses.field()

    connectionId = field("connectionId")
    connectionName = field("connectionName")
    encryptionMode = field("encryptionMode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateConnectionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateConnectionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDirectConnectGatewayRequest:
    boto3_raw_data: "type_defs.UpdateDirectConnectGatewayRequestTypeDef" = (
        dataclasses.field()
    )

    directConnectGatewayId = field("directConnectGatewayId")
    newDirectConnectGatewayName = field("newDirectConnectGatewayName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateDirectConnectGatewayRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDirectConnectGatewayRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateLagRequest:
    boto3_raw_data: "type_defs.UpdateLagRequestTypeDef" = dataclasses.field()

    lagId = field("lagId")
    lagName = field("lagName")
    minimumLinks = field("minimumLinks")
    encryptionMode = field("encryptionMode")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateLagRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateLagRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateVirtualInterfaceAttributesRequest:
    boto3_raw_data: "type_defs.UpdateVirtualInterfaceAttributesRequestTypeDef" = (
        dataclasses.field()
    )

    virtualInterfaceId = field("virtualInterfaceId")
    mtu = field("mtu")
    enableSiteLink = field("enableSiteLink")
    virtualInterfaceName = field("virtualInterfaceName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateVirtualInterfaceAttributesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateVirtualInterfaceAttributesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VirtualGateway:
    boto3_raw_data: "type_defs.VirtualGatewayTypeDef" = dataclasses.field()

    virtualGatewayId = field("virtualGatewayId")
    virtualGatewayState = field("virtualGatewayState")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VirtualGatewayTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VirtualGatewayTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AcceptDirectConnectGatewayAssociationProposalRequest:
    boto3_raw_data: (
        "type_defs.AcceptDirectConnectGatewayAssociationProposalRequestTypeDef"
    ) = dataclasses.field()

    directConnectGatewayId = field("directConnectGatewayId")
    proposalId = field("proposalId")
    associatedGatewayOwnerAccount = field("associatedGatewayOwnerAccount")

    @cached_property
    def overrideAllowedPrefixesToDirectConnectGateway(self):  # pragma: no cover
        return RouteFilterPrefix.make_many(
            self.boto3_raw_data["overrideAllowedPrefixesToDirectConnectGateway"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AcceptDirectConnectGatewayAssociationProposalRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.AcceptDirectConnectGatewayAssociationProposalRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDirectConnectGatewayAssociationProposalRequest:
    boto3_raw_data: (
        "type_defs.CreateDirectConnectGatewayAssociationProposalRequestTypeDef"
    ) = dataclasses.field()

    directConnectGatewayId = field("directConnectGatewayId")
    directConnectGatewayOwnerAccount = field("directConnectGatewayOwnerAccount")
    gatewayId = field("gatewayId")

    @cached_property
    def addAllowedPrefixesToDirectConnectGateway(self):  # pragma: no cover
        return RouteFilterPrefix.make_many(
            self.boto3_raw_data["addAllowedPrefixesToDirectConnectGateway"]
        )

    @cached_property
    def removeAllowedPrefixesToDirectConnectGateway(self):  # pragma: no cover
        return RouteFilterPrefix.make_many(
            self.boto3_raw_data["removeAllowedPrefixesToDirectConnectGateway"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateDirectConnectGatewayAssociationProposalRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.CreateDirectConnectGatewayAssociationProposalRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDirectConnectGatewayAssociationRequest:
    boto3_raw_data: "type_defs.CreateDirectConnectGatewayAssociationRequestTypeDef" = (
        dataclasses.field()
    )

    directConnectGatewayId = field("directConnectGatewayId")
    gatewayId = field("gatewayId")

    @cached_property
    def addAllowedPrefixesToDirectConnectGateway(self):  # pragma: no cover
        return RouteFilterPrefix.make_many(
            self.boto3_raw_data["addAllowedPrefixesToDirectConnectGateway"]
        )

    virtualGatewayId = field("virtualGatewayId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateDirectConnectGatewayAssociationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDirectConnectGatewayAssociationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDirectConnectGatewayAssociationRequest:
    boto3_raw_data: "type_defs.UpdateDirectConnectGatewayAssociationRequestTypeDef" = (
        dataclasses.field()
    )

    associationId = field("associationId")

    @cached_property
    def addAllowedPrefixesToDirectConnectGateway(self):  # pragma: no cover
        return RouteFilterPrefix.make_many(
            self.boto3_raw_data["addAllowedPrefixesToDirectConnectGateway"]
        )

    @cached_property
    def removeAllowedPrefixesToDirectConnectGateway(self):  # pragma: no cover
        return RouteFilterPrefix.make_many(
            self.boto3_raw_data["removeAllowedPrefixesToDirectConnectGateway"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateDirectConnectGatewayAssociationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDirectConnectGatewayAssociationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfirmConnectionResponse:
    boto3_raw_data: "type_defs.ConfirmConnectionResponseTypeDef" = dataclasses.field()

    connectionState = field("connectionState")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConfirmConnectionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfirmConnectionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfirmCustomerAgreementResponse:
    boto3_raw_data: "type_defs.ConfirmCustomerAgreementResponseTypeDef" = (
        dataclasses.field()
    )

    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ConfirmCustomerAgreementResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfirmCustomerAgreementResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfirmPrivateVirtualInterfaceResponse:
    boto3_raw_data: "type_defs.ConfirmPrivateVirtualInterfaceResponseTypeDef" = (
        dataclasses.field()
    )

    virtualInterfaceState = field("virtualInterfaceState")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ConfirmPrivateVirtualInterfaceResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfirmPrivateVirtualInterfaceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfirmPublicVirtualInterfaceResponse:
    boto3_raw_data: "type_defs.ConfirmPublicVirtualInterfaceResponseTypeDef" = (
        dataclasses.field()
    )

    virtualInterfaceState = field("virtualInterfaceState")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ConfirmPublicVirtualInterfaceResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfirmPublicVirtualInterfaceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfirmTransitVirtualInterfaceResponse:
    boto3_raw_data: "type_defs.ConfirmTransitVirtualInterfaceResponseTypeDef" = (
        dataclasses.field()
    )

    virtualInterfaceState = field("virtualInterfaceState")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ConfirmTransitVirtualInterfaceResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfirmTransitVirtualInterfaceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteInterconnectResponse:
    boto3_raw_data: "type_defs.DeleteInterconnectResponseTypeDef" = dataclasses.field()

    interconnectState = field("interconnectState")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteInterconnectResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteInterconnectResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteVirtualInterfaceResponse:
    boto3_raw_data: "type_defs.DeleteVirtualInterfaceResponseTypeDef" = (
        dataclasses.field()
    )

    virtualInterfaceState = field("virtualInterfaceState")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteVirtualInterfaceResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteVirtualInterfaceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoaResponse:
    boto3_raw_data: "type_defs.LoaResponseTypeDef" = dataclasses.field()

    loaContent = field("loaContent")
    loaContentType = field("loaContentType")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LoaResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LoaResponseTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AllocateHostedConnectionRequest:
    boto3_raw_data: "type_defs.AllocateHostedConnectionRequestTypeDef" = (
        dataclasses.field()
    )

    connectionId = field("connectionId")
    ownerAccount = field("ownerAccount")
    bandwidth = field("bandwidth")
    connectionName = field("connectionName")
    vlan = field("vlan")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AllocateHostedConnectionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AllocateHostedConnectionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateConnectionRequest:
    boto3_raw_data: "type_defs.CreateConnectionRequestTypeDef" = dataclasses.field()

    location = field("location")
    bandwidth = field("bandwidth")
    connectionName = field("connectionName")
    lagId = field("lagId")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    providerName = field("providerName")
    requestMACSec = field("requestMACSec")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateConnectionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateConnectionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDirectConnectGatewayRequest:
    boto3_raw_data: "type_defs.CreateDirectConnectGatewayRequestTypeDef" = (
        dataclasses.field()
    )

    directConnectGatewayName = field("directConnectGatewayName")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    amazonSideAsn = field("amazonSideAsn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateDirectConnectGatewayRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDirectConnectGatewayRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateInterconnectRequest:
    boto3_raw_data: "type_defs.CreateInterconnectRequestTypeDef" = dataclasses.field()

    interconnectName = field("interconnectName")
    bandwidth = field("bandwidth")
    location = field("location")
    lagId = field("lagId")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    providerName = field("providerName")
    requestMACSec = field("requestMACSec")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateInterconnectRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateInterconnectRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLagRequest:
    boto3_raw_data: "type_defs.CreateLagRequestTypeDef" = dataclasses.field()

    numberOfConnections = field("numberOfConnections")
    location = field("location")
    connectionsBandwidth = field("connectionsBandwidth")
    lagName = field("lagName")
    connectionId = field("connectionId")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @cached_property
    def childConnectionTags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["childConnectionTags"])

    providerName = field("providerName")
    requestMACSec = field("requestMACSec")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateLagRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLagRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DirectConnectGateway:
    boto3_raw_data: "type_defs.DirectConnectGatewayTypeDef" = dataclasses.field()

    directConnectGatewayId = field("directConnectGatewayId")
    directConnectGatewayName = field("directConnectGatewayName")
    amazonSideAsn = field("amazonSideAsn")
    ownerAccount = field("ownerAccount")
    directConnectGatewayState = field("directConnectGatewayState")
    stateChangeError = field("stateChangeError")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DirectConnectGatewayTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DirectConnectGatewayTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NewPrivateVirtualInterfaceAllocation:
    boto3_raw_data: "type_defs.NewPrivateVirtualInterfaceAllocationTypeDef" = (
        dataclasses.field()
    )

    virtualInterfaceName = field("virtualInterfaceName")
    vlan = field("vlan")
    asn = field("asn")
    asnLong = field("asnLong")
    mtu = field("mtu")
    authKey = field("authKey")
    amazonAddress = field("amazonAddress")
    addressFamily = field("addressFamily")
    customerAddress = field("customerAddress")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.NewPrivateVirtualInterfaceAllocationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NewPrivateVirtualInterfaceAllocationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NewPrivateVirtualInterface:
    boto3_raw_data: "type_defs.NewPrivateVirtualInterfaceTypeDef" = dataclasses.field()

    virtualInterfaceName = field("virtualInterfaceName")
    vlan = field("vlan")
    asn = field("asn")
    asnLong = field("asnLong")
    mtu = field("mtu")
    authKey = field("authKey")
    amazonAddress = field("amazonAddress")
    customerAddress = field("customerAddress")
    addressFamily = field("addressFamily")
    virtualGatewayId = field("virtualGatewayId")
    directConnectGatewayId = field("directConnectGatewayId")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    enableSiteLink = field("enableSiteLink")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NewPrivateVirtualInterfaceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NewPrivateVirtualInterfaceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NewPublicVirtualInterfaceAllocation:
    boto3_raw_data: "type_defs.NewPublicVirtualInterfaceAllocationTypeDef" = (
        dataclasses.field()
    )

    virtualInterfaceName = field("virtualInterfaceName")
    vlan = field("vlan")
    asn = field("asn")
    asnLong = field("asnLong")
    authKey = field("authKey")
    amazonAddress = field("amazonAddress")
    customerAddress = field("customerAddress")
    addressFamily = field("addressFamily")

    @cached_property
    def routeFilterPrefixes(self):  # pragma: no cover
        return RouteFilterPrefix.make_many(self.boto3_raw_data["routeFilterPrefixes"])

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.NewPublicVirtualInterfaceAllocationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NewPublicVirtualInterfaceAllocationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NewPublicVirtualInterface:
    boto3_raw_data: "type_defs.NewPublicVirtualInterfaceTypeDef" = dataclasses.field()

    virtualInterfaceName = field("virtualInterfaceName")
    vlan = field("vlan")
    asn = field("asn")
    asnLong = field("asnLong")
    authKey = field("authKey")
    amazonAddress = field("amazonAddress")
    customerAddress = field("customerAddress")
    addressFamily = field("addressFamily")

    @cached_property
    def routeFilterPrefixes(self):  # pragma: no cover
        return RouteFilterPrefix.make_many(self.boto3_raw_data["routeFilterPrefixes"])

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NewPublicVirtualInterfaceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NewPublicVirtualInterfaceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NewTransitVirtualInterfaceAllocation:
    boto3_raw_data: "type_defs.NewTransitVirtualInterfaceAllocationTypeDef" = (
        dataclasses.field()
    )

    virtualInterfaceName = field("virtualInterfaceName")
    vlan = field("vlan")
    asn = field("asn")
    asnLong = field("asnLong")
    mtu = field("mtu")
    authKey = field("authKey")
    amazonAddress = field("amazonAddress")
    customerAddress = field("customerAddress")
    addressFamily = field("addressFamily")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.NewTransitVirtualInterfaceAllocationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NewTransitVirtualInterfaceAllocationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NewTransitVirtualInterface:
    boto3_raw_data: "type_defs.NewTransitVirtualInterfaceTypeDef" = dataclasses.field()

    virtualInterfaceName = field("virtualInterfaceName")
    vlan = field("vlan")
    asn = field("asn")
    asnLong = field("asnLong")
    mtu = field("mtu")
    authKey = field("authKey")
    amazonAddress = field("amazonAddress")
    customerAddress = field("customerAddress")
    addressFamily = field("addressFamily")
    directConnectGatewayId = field("directConnectGatewayId")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    enableSiteLink = field("enableSiteLink")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NewTransitVirtualInterfaceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NewTransitVirtualInterfaceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceTag:
    boto3_raw_data: "type_defs.ResourceTagTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResourceTagTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResourceTagTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagResourceRequest:
    boto3_raw_data: "type_defs.TagResourceRequestTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TagResourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TagResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateMacSecKeyResponse:
    boto3_raw_data: "type_defs.AssociateMacSecKeyResponseTypeDef" = dataclasses.field()

    connectionId = field("connectionId")

    @cached_property
    def macSecKeys(self):  # pragma: no cover
        return MacSecKey.make_many(self.boto3_raw_data["macSecKeys"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociateMacSecKeyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateMacSecKeyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConnectionResponse:
    boto3_raw_data: "type_defs.ConnectionResponseTypeDef" = dataclasses.field()

    ownerAccount = field("ownerAccount")
    connectionId = field("connectionId")
    connectionName = field("connectionName")
    connectionState = field("connectionState")
    region = field("region")
    location = field("location")
    bandwidth = field("bandwidth")
    vlan = field("vlan")
    partnerName = field("partnerName")
    loaIssueTime = field("loaIssueTime")
    lagId = field("lagId")
    awsDevice = field("awsDevice")
    jumboFrameCapable = field("jumboFrameCapable")
    awsDeviceV2 = field("awsDeviceV2")
    awsLogicalDeviceId = field("awsLogicalDeviceId")
    hasLogicalRedundancy = field("hasLogicalRedundancy")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    providerName = field("providerName")
    macSecCapable = field("macSecCapable")
    portEncryptionStatus = field("portEncryptionStatus")
    encryptionMode = field("encryptionMode")

    @cached_property
    def macSecKeys(self):  # pragma: no cover
        return MacSecKey.make_many(self.boto3_raw_data["macSecKeys"])

    partnerInterconnectMacSecCapable = field("partnerInterconnectMacSecCapable")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConnectionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConnectionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Connection:
    boto3_raw_data: "type_defs.ConnectionTypeDef" = dataclasses.field()

    ownerAccount = field("ownerAccount")
    connectionId = field("connectionId")
    connectionName = field("connectionName")
    connectionState = field("connectionState")
    region = field("region")
    location = field("location")
    bandwidth = field("bandwidth")
    vlan = field("vlan")
    partnerName = field("partnerName")
    loaIssueTime = field("loaIssueTime")
    lagId = field("lagId")
    awsDevice = field("awsDevice")
    jumboFrameCapable = field("jumboFrameCapable")
    awsDeviceV2 = field("awsDeviceV2")
    awsLogicalDeviceId = field("awsLogicalDeviceId")
    hasLogicalRedundancy = field("hasLogicalRedundancy")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    providerName = field("providerName")
    macSecCapable = field("macSecCapable")
    portEncryptionStatus = field("portEncryptionStatus")
    encryptionMode = field("encryptionMode")

    @cached_property
    def macSecKeys(self):  # pragma: no cover
        return MacSecKey.make_many(self.boto3_raw_data["macSecKeys"])

    partnerInterconnectMacSecCapable = field("partnerInterconnectMacSecCapable")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConnectionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ConnectionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateMacSecKeyResponse:
    boto3_raw_data: "type_defs.DisassociateMacSecKeyResponseTypeDef" = (
        dataclasses.field()
    )

    connectionId = field("connectionId")

    @cached_property
    def macSecKeys(self):  # pragma: no cover
        return MacSecKey.make_many(self.boto3_raw_data["macSecKeys"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DisassociateMacSecKeyResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateMacSecKeyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InterconnectResponse:
    boto3_raw_data: "type_defs.InterconnectResponseTypeDef" = dataclasses.field()

    interconnectId = field("interconnectId")
    interconnectName = field("interconnectName")
    interconnectState = field("interconnectState")
    region = field("region")
    location = field("location")
    bandwidth = field("bandwidth")
    loaIssueTime = field("loaIssueTime")
    lagId = field("lagId")
    awsDevice = field("awsDevice")
    jumboFrameCapable = field("jumboFrameCapable")
    awsDeviceV2 = field("awsDeviceV2")
    awsLogicalDeviceId = field("awsLogicalDeviceId")
    hasLogicalRedundancy = field("hasLogicalRedundancy")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    providerName = field("providerName")
    macSecCapable = field("macSecCapable")
    portEncryptionStatus = field("portEncryptionStatus")
    encryptionMode = field("encryptionMode")

    @cached_property
    def macSecKeys(self):  # pragma: no cover
        return MacSecKey.make_many(self.boto3_raw_data["macSecKeys"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InterconnectResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InterconnectResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Interconnect:
    boto3_raw_data: "type_defs.InterconnectTypeDef" = dataclasses.field()

    interconnectId = field("interconnectId")
    interconnectName = field("interconnectName")
    interconnectState = field("interconnectState")
    region = field("region")
    location = field("location")
    bandwidth = field("bandwidth")
    loaIssueTime = field("loaIssueTime")
    lagId = field("lagId")
    awsDevice = field("awsDevice")
    jumboFrameCapable = field("jumboFrameCapable")
    awsDeviceV2 = field("awsDeviceV2")
    awsLogicalDeviceId = field("awsLogicalDeviceId")
    hasLogicalRedundancy = field("hasLogicalRedundancy")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    providerName = field("providerName")
    macSecCapable = field("macSecCapable")
    portEncryptionStatus = field("portEncryptionStatus")
    encryptionMode = field("encryptionMode")

    @cached_property
    def macSecKeys(self):  # pragma: no cover
        return MacSecKey.make_many(self.boto3_raw_data["macSecKeys"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InterconnectTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InterconnectTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DirectConnectGatewayAssociationProposal:
    boto3_raw_data: "type_defs.DirectConnectGatewayAssociationProposalTypeDef" = (
        dataclasses.field()
    )

    proposalId = field("proposalId")
    directConnectGatewayId = field("directConnectGatewayId")
    directConnectGatewayOwnerAccount = field("directConnectGatewayOwnerAccount")
    proposalState = field("proposalState")

    @cached_property
    def associatedGateway(self):  # pragma: no cover
        return AssociatedGateway.make_one(self.boto3_raw_data["associatedGateway"])

    @cached_property
    def existingAllowedPrefixesToDirectConnectGateway(self):  # pragma: no cover
        return RouteFilterPrefix.make_many(
            self.boto3_raw_data["existingAllowedPrefixesToDirectConnectGateway"]
        )

    @cached_property
    def requestedAllowedPrefixesToDirectConnectGateway(self):  # pragma: no cover
        return RouteFilterPrefix.make_many(
            self.boto3_raw_data["requestedAllowedPrefixesToDirectConnectGateway"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DirectConnectGatewayAssociationProposalTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DirectConnectGatewayAssociationProposalTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DirectConnectGatewayAssociation:
    boto3_raw_data: "type_defs.DirectConnectGatewayAssociationTypeDef" = (
        dataclasses.field()
    )

    directConnectGatewayId = field("directConnectGatewayId")
    directConnectGatewayOwnerAccount = field("directConnectGatewayOwnerAccount")
    associationState = field("associationState")
    stateChangeError = field("stateChangeError")

    @cached_property
    def associatedGateway(self):  # pragma: no cover
        return AssociatedGateway.make_one(self.boto3_raw_data["associatedGateway"])

    associationId = field("associationId")

    @cached_property
    def allowedPrefixesToDirectConnectGateway(self):  # pragma: no cover
        return RouteFilterPrefix.make_many(
            self.boto3_raw_data["allowedPrefixesToDirectConnectGateway"]
        )

    @cached_property
    def associatedCoreNetwork(self):  # pragma: no cover
        return AssociatedCoreNetwork.make_one(
            self.boto3_raw_data["associatedCoreNetwork"]
        )

    virtualGatewayId = field("virtualGatewayId")
    virtualGatewayRegion = field("virtualGatewayRegion")
    virtualGatewayOwnerAccount = field("virtualGatewayOwnerAccount")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DirectConnectGatewayAssociationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DirectConnectGatewayAssociationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VirtualInterfaceResponse:
    boto3_raw_data: "type_defs.VirtualInterfaceResponseTypeDef" = dataclasses.field()

    ownerAccount = field("ownerAccount")
    virtualInterfaceId = field("virtualInterfaceId")
    location = field("location")
    connectionId = field("connectionId")
    virtualInterfaceType = field("virtualInterfaceType")
    virtualInterfaceName = field("virtualInterfaceName")
    vlan = field("vlan")
    asn = field("asn")
    asnLong = field("asnLong")
    amazonSideAsn = field("amazonSideAsn")
    authKey = field("authKey")
    amazonAddress = field("amazonAddress")
    customerAddress = field("customerAddress")
    addressFamily = field("addressFamily")
    virtualInterfaceState = field("virtualInterfaceState")
    customerRouterConfig = field("customerRouterConfig")
    mtu = field("mtu")
    jumboFrameCapable = field("jumboFrameCapable")
    virtualGatewayId = field("virtualGatewayId")
    directConnectGatewayId = field("directConnectGatewayId")

    @cached_property
    def routeFilterPrefixes(self):  # pragma: no cover
        return RouteFilterPrefix.make_many(self.boto3_raw_data["routeFilterPrefixes"])

    @cached_property
    def bgpPeers(self):  # pragma: no cover
        return BGPPeer.make_many(self.boto3_raw_data["bgpPeers"])

    region = field("region")
    awsDeviceV2 = field("awsDeviceV2")
    awsLogicalDeviceId = field("awsLogicalDeviceId")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    siteLinkEnabled = field("siteLinkEnabled")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VirtualInterfaceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VirtualInterfaceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VirtualInterface:
    boto3_raw_data: "type_defs.VirtualInterfaceTypeDef" = dataclasses.field()

    ownerAccount = field("ownerAccount")
    virtualInterfaceId = field("virtualInterfaceId")
    location = field("location")
    connectionId = field("connectionId")
    virtualInterfaceType = field("virtualInterfaceType")
    virtualInterfaceName = field("virtualInterfaceName")
    vlan = field("vlan")
    asn = field("asn")
    asnLong = field("asnLong")
    amazonSideAsn = field("amazonSideAsn")
    authKey = field("authKey")
    amazonAddress = field("amazonAddress")
    customerAddress = field("customerAddress")
    addressFamily = field("addressFamily")
    virtualInterfaceState = field("virtualInterfaceState")
    customerRouterConfig = field("customerRouterConfig")
    mtu = field("mtu")
    jumboFrameCapable = field("jumboFrameCapable")
    virtualGatewayId = field("virtualGatewayId")
    directConnectGatewayId = field("directConnectGatewayId")

    @cached_property
    def routeFilterPrefixes(self):  # pragma: no cover
        return RouteFilterPrefix.make_many(self.boto3_raw_data["routeFilterPrefixes"])

    @cached_property
    def bgpPeers(self):  # pragma: no cover
        return BGPPeer.make_many(self.boto3_raw_data["bgpPeers"])

    region = field("region")
    awsDeviceV2 = field("awsDeviceV2")
    awsLogicalDeviceId = field("awsLogicalDeviceId")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    siteLinkEnabled = field("siteLinkEnabled")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VirtualInterfaceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VirtualInterfaceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBGPPeerRequest:
    boto3_raw_data: "type_defs.CreateBGPPeerRequestTypeDef" = dataclasses.field()

    virtualInterfaceId = field("virtualInterfaceId")

    @cached_property
    def newBGPPeer(self):  # pragma: no cover
        return NewBGPPeer.make_one(self.boto3_raw_data["newBGPPeer"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateBGPPeerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBGPPeerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCustomerMetadataResponse:
    boto3_raw_data: "type_defs.DescribeCustomerMetadataResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def agreements(self):  # pragma: no cover
        return CustomerAgreement.make_many(self.boto3_raw_data["agreements"])

    nniPartnerType = field("nniPartnerType")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeCustomerMetadataResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCustomerMetadataResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeConnectionLoaResponse:
    boto3_raw_data: "type_defs.DescribeConnectionLoaResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def loa(self):  # pragma: no cover
        return Loa.make_one(self.boto3_raw_data["loa"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeConnectionLoaResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeConnectionLoaResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeInterconnectLoaResponse:
    boto3_raw_data: "type_defs.DescribeInterconnectLoaResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def loa(self):  # pragma: no cover
        return Loa.make_one(self.boto3_raw_data["loa"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeInterconnectLoaResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeInterconnectLoaResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDirectConnectGatewayAssociationsRequestPaginate:
    boto3_raw_data: (
        "type_defs.DescribeDirectConnectGatewayAssociationsRequestPaginateTypeDef"
    ) = dataclasses.field()

    associationId = field("associationId")
    associatedGatewayId = field("associatedGatewayId")
    directConnectGatewayId = field("directConnectGatewayId")
    virtualGatewayId = field("virtualGatewayId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDirectConnectGatewayAssociationsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.DescribeDirectConnectGatewayAssociationsRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDirectConnectGatewayAttachmentsRequestPaginate:
    boto3_raw_data: (
        "type_defs.DescribeDirectConnectGatewayAttachmentsRequestPaginateTypeDef"
    ) = dataclasses.field()

    directConnectGatewayId = field("directConnectGatewayId")
    virtualInterfaceId = field("virtualInterfaceId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDirectConnectGatewayAttachmentsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.DescribeDirectConnectGatewayAttachmentsRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDirectConnectGatewaysRequestPaginate:
    boto3_raw_data: "type_defs.DescribeDirectConnectGatewaysRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    directConnectGatewayId = field("directConnectGatewayId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDirectConnectGatewaysRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDirectConnectGatewaysRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDirectConnectGatewayAttachmentsResult:
    boto3_raw_data: "type_defs.DescribeDirectConnectGatewayAttachmentsResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def directConnectGatewayAttachments(self):  # pragma: no cover
        return DirectConnectGatewayAttachment.make_many(
            self.boto3_raw_data["directConnectGatewayAttachments"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDirectConnectGatewayAttachmentsResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDirectConnectGatewayAttachmentsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRouterConfigurationResponse:
    boto3_raw_data: "type_defs.DescribeRouterConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    customerRouterConfig = field("customerRouterConfig")

    @cached_property
    def router(self):  # pragma: no cover
        return RouterType.make_one(self.boto3_raw_data["router"])

    virtualInterfaceId = field("virtualInterfaceId")
    virtualInterfaceName = field("virtualInterfaceName")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeRouterConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRouterConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVirtualInterfaceTestHistoryResponse:
    boto3_raw_data: "type_defs.ListVirtualInterfaceTestHistoryResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def virtualInterfaceTestHistory(self):  # pragma: no cover
        return VirtualInterfaceTestHistory.make_many(
            self.boto3_raw_data["virtualInterfaceTestHistory"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListVirtualInterfaceTestHistoryResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVirtualInterfaceTestHistoryResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartBgpFailoverTestResponse:
    boto3_raw_data: "type_defs.StartBgpFailoverTestResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def virtualInterfaceTest(self):  # pragma: no cover
        return VirtualInterfaceTestHistory.make_one(
            self.boto3_raw_data["virtualInterfaceTest"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartBgpFailoverTestResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartBgpFailoverTestResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopBgpFailoverTestResponse:
    boto3_raw_data: "type_defs.StopBgpFailoverTestResponseTypeDef" = dataclasses.field()

    @cached_property
    def virtualInterfaceTest(self):  # pragma: no cover
        return VirtualInterfaceTestHistory.make_one(
            self.boto3_raw_data["virtualInterfaceTest"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopBgpFailoverTestResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopBgpFailoverTestResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Locations:
    boto3_raw_data: "type_defs.LocationsTypeDef" = dataclasses.field()

    @cached_property
    def locations(self):  # pragma: no cover
        return Location.make_many(self.boto3_raw_data["locations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LocationsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LocationsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VirtualGateways:
    boto3_raw_data: "type_defs.VirtualGatewaysTypeDef" = dataclasses.field()

    @cached_property
    def virtualGateways(self):  # pragma: no cover
        return VirtualGateway.make_many(self.boto3_raw_data["virtualGateways"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VirtualGatewaysTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VirtualGatewaysTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDirectConnectGatewayResult:
    boto3_raw_data: "type_defs.CreateDirectConnectGatewayResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def directConnectGateway(self):  # pragma: no cover
        return DirectConnectGateway.make_one(
            self.boto3_raw_data["directConnectGateway"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateDirectConnectGatewayResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDirectConnectGatewayResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDirectConnectGatewayResult:
    boto3_raw_data: "type_defs.DeleteDirectConnectGatewayResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def directConnectGateway(self):  # pragma: no cover
        return DirectConnectGateway.make_one(
            self.boto3_raw_data["directConnectGateway"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteDirectConnectGatewayResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDirectConnectGatewayResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDirectConnectGatewaysResult:
    boto3_raw_data: "type_defs.DescribeDirectConnectGatewaysResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def directConnectGateways(self):  # pragma: no cover
        return DirectConnectGateway.make_many(
            self.boto3_raw_data["directConnectGateways"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDirectConnectGatewaysResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDirectConnectGatewaysResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDirectConnectGatewayResponse:
    boto3_raw_data: "type_defs.UpdateDirectConnectGatewayResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def directConnectGateway(self):  # pragma: no cover
        return DirectConnectGateway.make_one(
            self.boto3_raw_data["directConnectGateway"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateDirectConnectGatewayResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDirectConnectGatewayResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AllocatePrivateVirtualInterfaceRequest:
    boto3_raw_data: "type_defs.AllocatePrivateVirtualInterfaceRequestTypeDef" = (
        dataclasses.field()
    )

    connectionId = field("connectionId")
    ownerAccount = field("ownerAccount")

    @cached_property
    def newPrivateVirtualInterfaceAllocation(self):  # pragma: no cover
        return NewPrivateVirtualInterfaceAllocation.make_one(
            self.boto3_raw_data["newPrivateVirtualInterfaceAllocation"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AllocatePrivateVirtualInterfaceRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AllocatePrivateVirtualInterfaceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePrivateVirtualInterfaceRequest:
    boto3_raw_data: "type_defs.CreatePrivateVirtualInterfaceRequestTypeDef" = (
        dataclasses.field()
    )

    connectionId = field("connectionId")

    @cached_property
    def newPrivateVirtualInterface(self):  # pragma: no cover
        return NewPrivateVirtualInterface.make_one(
            self.boto3_raw_data["newPrivateVirtualInterface"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreatePrivateVirtualInterfaceRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePrivateVirtualInterfaceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AllocatePublicVirtualInterfaceRequest:
    boto3_raw_data: "type_defs.AllocatePublicVirtualInterfaceRequestTypeDef" = (
        dataclasses.field()
    )

    connectionId = field("connectionId")
    ownerAccount = field("ownerAccount")

    @cached_property
    def newPublicVirtualInterfaceAllocation(self):  # pragma: no cover
        return NewPublicVirtualInterfaceAllocation.make_one(
            self.boto3_raw_data["newPublicVirtualInterfaceAllocation"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AllocatePublicVirtualInterfaceRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AllocatePublicVirtualInterfaceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePublicVirtualInterfaceRequest:
    boto3_raw_data: "type_defs.CreatePublicVirtualInterfaceRequestTypeDef" = (
        dataclasses.field()
    )

    connectionId = field("connectionId")

    @cached_property
    def newPublicVirtualInterface(self):  # pragma: no cover
        return NewPublicVirtualInterface.make_one(
            self.boto3_raw_data["newPublicVirtualInterface"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreatePublicVirtualInterfaceRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePublicVirtualInterfaceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AllocateTransitVirtualInterfaceRequest:
    boto3_raw_data: "type_defs.AllocateTransitVirtualInterfaceRequestTypeDef" = (
        dataclasses.field()
    )

    connectionId = field("connectionId")
    ownerAccount = field("ownerAccount")

    @cached_property
    def newTransitVirtualInterfaceAllocation(self):  # pragma: no cover
        return NewTransitVirtualInterfaceAllocation.make_one(
            self.boto3_raw_data["newTransitVirtualInterfaceAllocation"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AllocateTransitVirtualInterfaceRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AllocateTransitVirtualInterfaceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTransitVirtualInterfaceRequest:
    boto3_raw_data: "type_defs.CreateTransitVirtualInterfaceRequestTypeDef" = (
        dataclasses.field()
    )

    connectionId = field("connectionId")

    @cached_property
    def newTransitVirtualInterface(self):  # pragma: no cover
        return NewTransitVirtualInterface.make_one(
            self.boto3_raw_data["newTransitVirtualInterface"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateTransitVirtualInterfaceRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTransitVirtualInterfaceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTagsResponse:
    boto3_raw_data: "type_defs.DescribeTagsResponseTypeDef" = dataclasses.field()

    @cached_property
    def resourceTags(self):  # pragma: no cover
        return ResourceTag.make_many(self.boto3_raw_data["resourceTags"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeTagsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTagsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Connections:
    boto3_raw_data: "type_defs.ConnectionsTypeDef" = dataclasses.field()

    @cached_property
    def connections(self):  # pragma: no cover
        return Connection.make_many(self.boto3_raw_data["connections"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConnectionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ConnectionsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LagResponse:
    boto3_raw_data: "type_defs.LagResponseTypeDef" = dataclasses.field()

    connectionsBandwidth = field("connectionsBandwidth")
    numberOfConnections = field("numberOfConnections")
    lagId = field("lagId")
    ownerAccount = field("ownerAccount")
    lagName = field("lagName")
    lagState = field("lagState")
    location = field("location")
    region = field("region")
    minimumLinks = field("minimumLinks")
    awsDevice = field("awsDevice")
    awsDeviceV2 = field("awsDeviceV2")
    awsLogicalDeviceId = field("awsLogicalDeviceId")

    @cached_property
    def connections(self):  # pragma: no cover
        return Connection.make_many(self.boto3_raw_data["connections"])

    allowsHostedConnections = field("allowsHostedConnections")
    jumboFrameCapable = field("jumboFrameCapable")
    hasLogicalRedundancy = field("hasLogicalRedundancy")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    providerName = field("providerName")
    macSecCapable = field("macSecCapable")
    encryptionMode = field("encryptionMode")

    @cached_property
    def macSecKeys(self):  # pragma: no cover
        return MacSecKey.make_many(self.boto3_raw_data["macSecKeys"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LagResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LagResponseTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Lag:
    boto3_raw_data: "type_defs.LagTypeDef" = dataclasses.field()

    connectionsBandwidth = field("connectionsBandwidth")
    numberOfConnections = field("numberOfConnections")
    lagId = field("lagId")
    ownerAccount = field("ownerAccount")
    lagName = field("lagName")
    lagState = field("lagState")
    location = field("location")
    region = field("region")
    minimumLinks = field("minimumLinks")
    awsDevice = field("awsDevice")
    awsDeviceV2 = field("awsDeviceV2")
    awsLogicalDeviceId = field("awsLogicalDeviceId")

    @cached_property
    def connections(self):  # pragma: no cover
        return Connection.make_many(self.boto3_raw_data["connections"])

    allowsHostedConnections = field("allowsHostedConnections")
    jumboFrameCapable = field("jumboFrameCapable")
    hasLogicalRedundancy = field("hasLogicalRedundancy")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    providerName = field("providerName")
    macSecCapable = field("macSecCapable")
    encryptionMode = field("encryptionMode")

    @cached_property
    def macSecKeys(self):  # pragma: no cover
        return MacSecKey.make_many(self.boto3_raw_data["macSecKeys"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LagTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LagTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Interconnects:
    boto3_raw_data: "type_defs.InterconnectsTypeDef" = dataclasses.field()

    @cached_property
    def interconnects(self):  # pragma: no cover
        return Interconnect.make_many(self.boto3_raw_data["interconnects"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InterconnectsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InterconnectsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDirectConnectGatewayAssociationProposalResult:
    boto3_raw_data: (
        "type_defs.CreateDirectConnectGatewayAssociationProposalResultTypeDef"
    ) = dataclasses.field()

    @cached_property
    def directConnectGatewayAssociationProposal(self):  # pragma: no cover
        return DirectConnectGatewayAssociationProposal.make_one(
            self.boto3_raw_data["directConnectGatewayAssociationProposal"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateDirectConnectGatewayAssociationProposalResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.CreateDirectConnectGatewayAssociationProposalResultTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDirectConnectGatewayAssociationProposalResult:
    boto3_raw_data: (
        "type_defs.DeleteDirectConnectGatewayAssociationProposalResultTypeDef"
    ) = dataclasses.field()

    @cached_property
    def directConnectGatewayAssociationProposal(self):  # pragma: no cover
        return DirectConnectGatewayAssociationProposal.make_one(
            self.boto3_raw_data["directConnectGatewayAssociationProposal"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteDirectConnectGatewayAssociationProposalResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.DeleteDirectConnectGatewayAssociationProposalResultTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDirectConnectGatewayAssociationProposalsResult:
    boto3_raw_data: (
        "type_defs.DescribeDirectConnectGatewayAssociationProposalsResultTypeDef"
    ) = dataclasses.field()

    @cached_property
    def directConnectGatewayAssociationProposals(self):  # pragma: no cover
        return DirectConnectGatewayAssociationProposal.make_many(
            self.boto3_raw_data["directConnectGatewayAssociationProposals"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDirectConnectGatewayAssociationProposalsResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.DescribeDirectConnectGatewayAssociationProposalsResultTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AcceptDirectConnectGatewayAssociationProposalResult:
    boto3_raw_data: (
        "type_defs.AcceptDirectConnectGatewayAssociationProposalResultTypeDef"
    ) = dataclasses.field()

    @cached_property
    def directConnectGatewayAssociation(self):  # pragma: no cover
        return DirectConnectGatewayAssociation.make_one(
            self.boto3_raw_data["directConnectGatewayAssociation"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AcceptDirectConnectGatewayAssociationProposalResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.AcceptDirectConnectGatewayAssociationProposalResultTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDirectConnectGatewayAssociationResult:
    boto3_raw_data: "type_defs.CreateDirectConnectGatewayAssociationResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def directConnectGatewayAssociation(self):  # pragma: no cover
        return DirectConnectGatewayAssociation.make_one(
            self.boto3_raw_data["directConnectGatewayAssociation"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateDirectConnectGatewayAssociationResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDirectConnectGatewayAssociationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDirectConnectGatewayAssociationResult:
    boto3_raw_data: "type_defs.DeleteDirectConnectGatewayAssociationResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def directConnectGatewayAssociation(self):  # pragma: no cover
        return DirectConnectGatewayAssociation.make_one(
            self.boto3_raw_data["directConnectGatewayAssociation"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteDirectConnectGatewayAssociationResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDirectConnectGatewayAssociationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDirectConnectGatewayAssociationsResult:
    boto3_raw_data: (
        "type_defs.DescribeDirectConnectGatewayAssociationsResultTypeDef"
    ) = dataclasses.field()

    @cached_property
    def directConnectGatewayAssociations(self):  # pragma: no cover
        return DirectConnectGatewayAssociation.make_many(
            self.boto3_raw_data["directConnectGatewayAssociations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDirectConnectGatewayAssociationsResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.DescribeDirectConnectGatewayAssociationsResultTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDirectConnectGatewayAssociationResult:
    boto3_raw_data: "type_defs.UpdateDirectConnectGatewayAssociationResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def directConnectGatewayAssociation(self):  # pragma: no cover
        return DirectConnectGatewayAssociation.make_one(
            self.boto3_raw_data["directConnectGatewayAssociation"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateDirectConnectGatewayAssociationResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDirectConnectGatewayAssociationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AllocateTransitVirtualInterfaceResult:
    boto3_raw_data: "type_defs.AllocateTransitVirtualInterfaceResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def virtualInterface(self):  # pragma: no cover
        return VirtualInterface.make_one(self.boto3_raw_data["virtualInterface"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AllocateTransitVirtualInterfaceResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AllocateTransitVirtualInterfaceResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBGPPeerResponse:
    boto3_raw_data: "type_defs.CreateBGPPeerResponseTypeDef" = dataclasses.field()

    @cached_property
    def virtualInterface(self):  # pragma: no cover
        return VirtualInterface.make_one(self.boto3_raw_data["virtualInterface"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateBGPPeerResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBGPPeerResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTransitVirtualInterfaceResult:
    boto3_raw_data: "type_defs.CreateTransitVirtualInterfaceResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def virtualInterface(self):  # pragma: no cover
        return VirtualInterface.make_one(self.boto3_raw_data["virtualInterface"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateTransitVirtualInterfaceResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTransitVirtualInterfaceResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBGPPeerResponse:
    boto3_raw_data: "type_defs.DeleteBGPPeerResponseTypeDef" = dataclasses.field()

    @cached_property
    def virtualInterface(self):  # pragma: no cover
        return VirtualInterface.make_one(self.boto3_raw_data["virtualInterface"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteBGPPeerResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBGPPeerResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VirtualInterfaces:
    boto3_raw_data: "type_defs.VirtualInterfacesTypeDef" = dataclasses.field()

    @cached_property
    def virtualInterfaces(self):  # pragma: no cover
        return VirtualInterface.make_many(self.boto3_raw_data["virtualInterfaces"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VirtualInterfacesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VirtualInterfacesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Lags:
    boto3_raw_data: "type_defs.LagsTypeDef" = dataclasses.field()

    @cached_property
    def lags(self):  # pragma: no cover
        return Lag.make_many(self.boto3_raw_data["lags"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LagsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LagsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
