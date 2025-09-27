# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_appmesh import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AwsCloudMapInstanceAttribute:
    boto3_raw_data: "type_defs.AwsCloudMapInstanceAttributeTypeDef" = (
        dataclasses.field()
    )

    key = field("key")
    value = field("value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AwsCloudMapInstanceAttributeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AwsCloudMapInstanceAttributeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListenerTlsFileCertificate:
    boto3_raw_data: "type_defs.ListenerTlsFileCertificateTypeDef" = dataclasses.field()

    certificateChain = field("certificateChain")
    privateKey = field("privateKey")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListenerTlsFileCertificateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListenerTlsFileCertificateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListenerTlsSdsCertificate:
    boto3_raw_data: "type_defs.ListenerTlsSdsCertificateTypeDef" = dataclasses.field()

    secretName = field("secretName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListenerTlsSdsCertificateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListenerTlsSdsCertificateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagRef:
    boto3_raw_data: "type_defs.TagRefTypeDef" = dataclasses.field()

    key = field("key")
    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TagRefTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TagRefTypeDef"]]
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
class DeleteGatewayRouteInput:
    boto3_raw_data: "type_defs.DeleteGatewayRouteInputTypeDef" = dataclasses.field()

    gatewayRouteName = field("gatewayRouteName")
    meshName = field("meshName")
    virtualGatewayName = field("virtualGatewayName")
    meshOwner = field("meshOwner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteGatewayRouteInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteGatewayRouteInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteMeshInput:
    boto3_raw_data: "type_defs.DeleteMeshInputTypeDef" = dataclasses.field()

    meshName = field("meshName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteMeshInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DeleteMeshInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRouteInput:
    boto3_raw_data: "type_defs.DeleteRouteInputTypeDef" = dataclasses.field()

    meshName = field("meshName")
    routeName = field("routeName")
    virtualRouterName = field("virtualRouterName")
    meshOwner = field("meshOwner")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteRouteInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRouteInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteVirtualGatewayInput:
    boto3_raw_data: "type_defs.DeleteVirtualGatewayInputTypeDef" = dataclasses.field()

    meshName = field("meshName")
    virtualGatewayName = field("virtualGatewayName")
    meshOwner = field("meshOwner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteVirtualGatewayInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteVirtualGatewayInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteVirtualNodeInput:
    boto3_raw_data: "type_defs.DeleteVirtualNodeInputTypeDef" = dataclasses.field()

    meshName = field("meshName")
    virtualNodeName = field("virtualNodeName")
    meshOwner = field("meshOwner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteVirtualNodeInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteVirtualNodeInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteVirtualRouterInput:
    boto3_raw_data: "type_defs.DeleteVirtualRouterInputTypeDef" = dataclasses.field()

    meshName = field("meshName")
    virtualRouterName = field("virtualRouterName")
    meshOwner = field("meshOwner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteVirtualRouterInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteVirtualRouterInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteVirtualServiceInput:
    boto3_raw_data: "type_defs.DeleteVirtualServiceInputTypeDef" = dataclasses.field()

    meshName = field("meshName")
    virtualServiceName = field("virtualServiceName")
    meshOwner = field("meshOwner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteVirtualServiceInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteVirtualServiceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeGatewayRouteInput:
    boto3_raw_data: "type_defs.DescribeGatewayRouteInputTypeDef" = dataclasses.field()

    gatewayRouteName = field("gatewayRouteName")
    meshName = field("meshName")
    virtualGatewayName = field("virtualGatewayName")
    meshOwner = field("meshOwner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeGatewayRouteInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeGatewayRouteInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMeshInput:
    boto3_raw_data: "type_defs.DescribeMeshInputTypeDef" = dataclasses.field()

    meshName = field("meshName")
    meshOwner = field("meshOwner")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DescribeMeshInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMeshInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRouteInput:
    boto3_raw_data: "type_defs.DescribeRouteInputTypeDef" = dataclasses.field()

    meshName = field("meshName")
    routeName = field("routeName")
    virtualRouterName = field("virtualRouterName")
    meshOwner = field("meshOwner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeRouteInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRouteInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeVirtualGatewayInput:
    boto3_raw_data: "type_defs.DescribeVirtualGatewayInputTypeDef" = dataclasses.field()

    meshName = field("meshName")
    virtualGatewayName = field("virtualGatewayName")
    meshOwner = field("meshOwner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeVirtualGatewayInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeVirtualGatewayInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeVirtualNodeInput:
    boto3_raw_data: "type_defs.DescribeVirtualNodeInputTypeDef" = dataclasses.field()

    meshName = field("meshName")
    virtualNodeName = field("virtualNodeName")
    meshOwner = field("meshOwner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeVirtualNodeInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeVirtualNodeInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeVirtualRouterInput:
    boto3_raw_data: "type_defs.DescribeVirtualRouterInputTypeDef" = dataclasses.field()

    meshName = field("meshName")
    virtualRouterName = field("virtualRouterName")
    meshOwner = field("meshOwner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeVirtualRouterInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeVirtualRouterInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeVirtualServiceInput:
    boto3_raw_data: "type_defs.DescribeVirtualServiceInputTypeDef" = dataclasses.field()

    meshName = field("meshName")
    virtualServiceName = field("virtualServiceName")
    meshOwner = field("meshOwner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeVirtualServiceInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeVirtualServiceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DnsServiceDiscovery:
    boto3_raw_data: "type_defs.DnsServiceDiscoveryTypeDef" = dataclasses.field()

    hostname = field("hostname")
    ipPreference = field("ipPreference")
    responseType = field("responseType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DnsServiceDiscoveryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DnsServiceDiscoveryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Duration:
    boto3_raw_data: "type_defs.DurationTypeDef" = dataclasses.field()

    unit = field("unit")
    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DurationTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EgressFilter:
    boto3_raw_data: "type_defs.EgressFilterTypeDef" = dataclasses.field()

    type = field("type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EgressFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EgressFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GatewayRouteStatus:
    boto3_raw_data: "type_defs.GatewayRouteStatusTypeDef" = dataclasses.field()

    status = field("status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GatewayRouteStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GatewayRouteStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceMetadata:
    boto3_raw_data: "type_defs.ResourceMetadataTypeDef" = dataclasses.field()

    arn = field("arn")
    createdAt = field("createdAt")
    lastUpdatedAt = field("lastUpdatedAt")
    meshOwner = field("meshOwner")
    resourceOwner = field("resourceOwner")
    uid = field("uid")
    version = field("version")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResourceMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GatewayRouteHostnameMatch:
    boto3_raw_data: "type_defs.GatewayRouteHostnameMatchTypeDef" = dataclasses.field()

    exact = field("exact")
    suffix = field("suffix")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GatewayRouteHostnameMatchTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GatewayRouteHostnameMatchTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GatewayRouteHostnameRewrite:
    boto3_raw_data: "type_defs.GatewayRouteHostnameRewriteTypeDef" = dataclasses.field()

    defaultTargetHostname = field("defaultTargetHostname")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GatewayRouteHostnameRewriteTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GatewayRouteHostnameRewriteTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GatewayRouteRef:
    boto3_raw_data: "type_defs.GatewayRouteRefTypeDef" = dataclasses.field()

    arn = field("arn")
    createdAt = field("createdAt")
    gatewayRouteName = field("gatewayRouteName")
    lastUpdatedAt = field("lastUpdatedAt")
    meshName = field("meshName")
    meshOwner = field("meshOwner")
    resourceOwner = field("resourceOwner")
    version = field("version")
    virtualGatewayName = field("virtualGatewayName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GatewayRouteRefTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GatewayRouteRefTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GatewayRouteVirtualService:
    boto3_raw_data: "type_defs.GatewayRouteVirtualServiceTypeDef" = dataclasses.field()

    virtualServiceName = field("virtualServiceName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GatewayRouteVirtualServiceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GatewayRouteVirtualServiceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MatchRange:
    boto3_raw_data: "type_defs.MatchRangeTypeDef" = dataclasses.field()

    end = field("end")
    start = field("start")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MatchRangeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MatchRangeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WeightedTarget:
    boto3_raw_data: "type_defs.WeightedTargetTypeDef" = dataclasses.field()

    virtualNode = field("virtualNode")
    weight = field("weight")
    port = field("port")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WeightedTargetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WeightedTargetTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HealthCheckPolicy:
    boto3_raw_data: "type_defs.HealthCheckPolicyTypeDef" = dataclasses.field()

    healthyThreshold = field("healthyThreshold")
    intervalMillis = field("intervalMillis")
    protocol = field("protocol")
    timeoutMillis = field("timeoutMillis")
    unhealthyThreshold = field("unhealthyThreshold")
    path = field("path")
    port = field("port")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HealthCheckPolicyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HealthCheckPolicyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HttpPathMatch:
    boto3_raw_data: "type_defs.HttpPathMatchTypeDef" = dataclasses.field()

    exact = field("exact")
    regex = field("regex")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HttpPathMatchTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.HttpPathMatchTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HttpGatewayRoutePathRewrite:
    boto3_raw_data: "type_defs.HttpGatewayRoutePathRewriteTypeDef" = dataclasses.field()

    exact = field("exact")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HttpGatewayRoutePathRewriteTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HttpGatewayRoutePathRewriteTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HttpGatewayRoutePrefixRewrite:
    boto3_raw_data: "type_defs.HttpGatewayRoutePrefixRewriteTypeDef" = (
        dataclasses.field()
    )

    defaultPrefix = field("defaultPrefix")
    value = field("value")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.HttpGatewayRoutePrefixRewriteTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HttpGatewayRoutePrefixRewriteTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryParameterMatch:
    boto3_raw_data: "type_defs.QueryParameterMatchTypeDef" = dataclasses.field()

    exact = field("exact")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.QueryParameterMatchTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QueryParameterMatchTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JsonFormatRef:
    boto3_raw_data: "type_defs.JsonFormatRefTypeDef" = dataclasses.field()

    key = field("key")
    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JsonFormatRefTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JsonFormatRefTypeDef"]],
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
class ListGatewayRoutesInput:
    boto3_raw_data: "type_defs.ListGatewayRoutesInputTypeDef" = dataclasses.field()

    meshName = field("meshName")
    virtualGatewayName = field("virtualGatewayName")
    limit = field("limit")
    meshOwner = field("meshOwner")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListGatewayRoutesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGatewayRoutesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMeshesInput:
    boto3_raw_data: "type_defs.ListMeshesInputTypeDef" = dataclasses.field()

    limit = field("limit")
    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListMeshesInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListMeshesInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MeshRef:
    boto3_raw_data: "type_defs.MeshRefTypeDef" = dataclasses.field()

    arn = field("arn")
    createdAt = field("createdAt")
    lastUpdatedAt = field("lastUpdatedAt")
    meshName = field("meshName")
    meshOwner = field("meshOwner")
    resourceOwner = field("resourceOwner")
    version = field("version")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MeshRefTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MeshRefTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRoutesInput:
    boto3_raw_data: "type_defs.ListRoutesInputTypeDef" = dataclasses.field()

    meshName = field("meshName")
    virtualRouterName = field("virtualRouterName")
    limit = field("limit")
    meshOwner = field("meshOwner")
    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListRoutesInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListRoutesInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteRef:
    boto3_raw_data: "type_defs.RouteRefTypeDef" = dataclasses.field()

    arn = field("arn")
    createdAt = field("createdAt")
    lastUpdatedAt = field("lastUpdatedAt")
    meshName = field("meshName")
    meshOwner = field("meshOwner")
    resourceOwner = field("resourceOwner")
    routeName = field("routeName")
    version = field("version")
    virtualRouterName = field("virtualRouterName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RouteRefTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RouteRefTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceInput:
    boto3_raw_data: "type_defs.ListTagsForResourceInputTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")
    limit = field("limit")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForResourceInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVirtualGatewaysInput:
    boto3_raw_data: "type_defs.ListVirtualGatewaysInputTypeDef" = dataclasses.field()

    meshName = field("meshName")
    limit = field("limit")
    meshOwner = field("meshOwner")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListVirtualGatewaysInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVirtualGatewaysInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VirtualGatewayRef:
    boto3_raw_data: "type_defs.VirtualGatewayRefTypeDef" = dataclasses.field()

    arn = field("arn")
    createdAt = field("createdAt")
    lastUpdatedAt = field("lastUpdatedAt")
    meshName = field("meshName")
    meshOwner = field("meshOwner")
    resourceOwner = field("resourceOwner")
    version = field("version")
    virtualGatewayName = field("virtualGatewayName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VirtualGatewayRefTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VirtualGatewayRefTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVirtualNodesInput:
    boto3_raw_data: "type_defs.ListVirtualNodesInputTypeDef" = dataclasses.field()

    meshName = field("meshName")
    limit = field("limit")
    meshOwner = field("meshOwner")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListVirtualNodesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVirtualNodesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VirtualNodeRef:
    boto3_raw_data: "type_defs.VirtualNodeRefTypeDef" = dataclasses.field()

    arn = field("arn")
    createdAt = field("createdAt")
    lastUpdatedAt = field("lastUpdatedAt")
    meshName = field("meshName")
    meshOwner = field("meshOwner")
    resourceOwner = field("resourceOwner")
    version = field("version")
    virtualNodeName = field("virtualNodeName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VirtualNodeRefTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VirtualNodeRefTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVirtualRoutersInput:
    boto3_raw_data: "type_defs.ListVirtualRoutersInputTypeDef" = dataclasses.field()

    meshName = field("meshName")
    limit = field("limit")
    meshOwner = field("meshOwner")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListVirtualRoutersInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVirtualRoutersInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VirtualRouterRef:
    boto3_raw_data: "type_defs.VirtualRouterRefTypeDef" = dataclasses.field()

    arn = field("arn")
    createdAt = field("createdAt")
    lastUpdatedAt = field("lastUpdatedAt")
    meshName = field("meshName")
    meshOwner = field("meshOwner")
    resourceOwner = field("resourceOwner")
    version = field("version")
    virtualRouterName = field("virtualRouterName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VirtualRouterRefTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VirtualRouterRefTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVirtualServicesInput:
    boto3_raw_data: "type_defs.ListVirtualServicesInputTypeDef" = dataclasses.field()

    meshName = field("meshName")
    limit = field("limit")
    meshOwner = field("meshOwner")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListVirtualServicesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVirtualServicesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VirtualServiceRef:
    boto3_raw_data: "type_defs.VirtualServiceRefTypeDef" = dataclasses.field()

    arn = field("arn")
    createdAt = field("createdAt")
    lastUpdatedAt = field("lastUpdatedAt")
    meshName = field("meshName")
    meshOwner = field("meshOwner")
    resourceOwner = field("resourceOwner")
    version = field("version")
    virtualServiceName = field("virtualServiceName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VirtualServiceRefTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VirtualServiceRefTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PortMapping:
    boto3_raw_data: "type_defs.PortMappingTypeDef" = dataclasses.field()

    port = field("port")
    protocol = field("protocol")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PortMappingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PortMappingTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListenerTlsAcmCertificate:
    boto3_raw_data: "type_defs.ListenerTlsAcmCertificateTypeDef" = dataclasses.field()

    certificateArn = field("certificateArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListenerTlsAcmCertificateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListenerTlsAcmCertificateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TlsValidationContextFileTrust:
    boto3_raw_data: "type_defs.TlsValidationContextFileTrustTypeDef" = (
        dataclasses.field()
    )

    certificateChain = field("certificateChain")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.TlsValidationContextFileTrustTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TlsValidationContextFileTrustTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TlsValidationContextSdsTrust:
    boto3_raw_data: "type_defs.TlsValidationContextSdsTrustTypeDef" = (
        dataclasses.field()
    )

    secretName = field("secretName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TlsValidationContextSdsTrustTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TlsValidationContextSdsTrustTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MeshStatus:
    boto3_raw_data: "type_defs.MeshStatusTypeDef" = dataclasses.field()

    status = field("status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MeshStatusTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MeshStatusTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MeshServiceDiscovery:
    boto3_raw_data: "type_defs.MeshServiceDiscoveryTypeDef" = dataclasses.field()

    ipPreference = field("ipPreference")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MeshServiceDiscoveryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MeshServiceDiscoveryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteStatus:
    boto3_raw_data: "type_defs.RouteStatusTypeDef" = dataclasses.field()

    status = field("status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RouteStatusTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RouteStatusTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SubjectAlternativeNameMatchersOutput:
    boto3_raw_data: "type_defs.SubjectAlternativeNameMatchersOutputTypeDef" = (
        dataclasses.field()
    )

    exact = field("exact")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SubjectAlternativeNameMatchersOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SubjectAlternativeNameMatchersOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SubjectAlternativeNameMatchers:
    boto3_raw_data: "type_defs.SubjectAlternativeNameMatchersTypeDef" = (
        dataclasses.field()
    )

    exact = field("exact")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SubjectAlternativeNameMatchersTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SubjectAlternativeNameMatchersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TcpRouteMatch:
    boto3_raw_data: "type_defs.TcpRouteMatchTypeDef" = dataclasses.field()

    port = field("port")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TcpRouteMatchTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TcpRouteMatchTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TlsValidationContextAcmTrustOutput:
    boto3_raw_data: "type_defs.TlsValidationContextAcmTrustOutputTypeDef" = (
        dataclasses.field()
    )

    certificateAuthorityArns = field("certificateAuthorityArns")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.TlsValidationContextAcmTrustOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TlsValidationContextAcmTrustOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TlsValidationContextAcmTrust:
    boto3_raw_data: "type_defs.TlsValidationContextAcmTrustTypeDef" = (
        dataclasses.field()
    )

    certificateAuthorityArns = field("certificateAuthorityArns")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TlsValidationContextAcmTrustTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TlsValidationContextAcmTrustTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UntagResourceInput:
    boto3_raw_data: "type_defs.UntagResourceInputTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")
    tagKeys = field("tagKeys")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UntagResourceInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UntagResourceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VirtualGatewayListenerTlsFileCertificate:
    boto3_raw_data: "type_defs.VirtualGatewayListenerTlsFileCertificateTypeDef" = (
        dataclasses.field()
    )

    certificateChain = field("certificateChain")
    privateKey = field("privateKey")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.VirtualGatewayListenerTlsFileCertificateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VirtualGatewayListenerTlsFileCertificateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VirtualGatewayListenerTlsSdsCertificate:
    boto3_raw_data: "type_defs.VirtualGatewayListenerTlsSdsCertificateTypeDef" = (
        dataclasses.field()
    )

    secretName = field("secretName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.VirtualGatewayListenerTlsSdsCertificateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VirtualGatewayListenerTlsSdsCertificateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VirtualGatewayGrpcConnectionPool:
    boto3_raw_data: "type_defs.VirtualGatewayGrpcConnectionPoolTypeDef" = (
        dataclasses.field()
    )

    maxRequests = field("maxRequests")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.VirtualGatewayGrpcConnectionPoolTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VirtualGatewayGrpcConnectionPoolTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VirtualGatewayHttp2ConnectionPool:
    boto3_raw_data: "type_defs.VirtualGatewayHttp2ConnectionPoolTypeDef" = (
        dataclasses.field()
    )

    maxRequests = field("maxRequests")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.VirtualGatewayHttp2ConnectionPoolTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VirtualGatewayHttp2ConnectionPoolTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VirtualGatewayHttpConnectionPool:
    boto3_raw_data: "type_defs.VirtualGatewayHttpConnectionPoolTypeDef" = (
        dataclasses.field()
    )

    maxConnections = field("maxConnections")
    maxPendingRequests = field("maxPendingRequests")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.VirtualGatewayHttpConnectionPoolTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VirtualGatewayHttpConnectionPoolTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VirtualGatewayStatus:
    boto3_raw_data: "type_defs.VirtualGatewayStatusTypeDef" = dataclasses.field()

    status = field("status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VirtualGatewayStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VirtualGatewayStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VirtualGatewayHealthCheckPolicy:
    boto3_raw_data: "type_defs.VirtualGatewayHealthCheckPolicyTypeDef" = (
        dataclasses.field()
    )

    healthyThreshold = field("healthyThreshold")
    intervalMillis = field("intervalMillis")
    protocol = field("protocol")
    timeoutMillis = field("timeoutMillis")
    unhealthyThreshold = field("unhealthyThreshold")
    path = field("path")
    port = field("port")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.VirtualGatewayHealthCheckPolicyTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VirtualGatewayHealthCheckPolicyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VirtualGatewayPortMapping:
    boto3_raw_data: "type_defs.VirtualGatewayPortMappingTypeDef" = dataclasses.field()

    port = field("port")
    protocol = field("protocol")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VirtualGatewayPortMappingTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VirtualGatewayPortMappingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VirtualGatewayListenerTlsAcmCertificate:
    boto3_raw_data: "type_defs.VirtualGatewayListenerTlsAcmCertificateTypeDef" = (
        dataclasses.field()
    )

    certificateArn = field("certificateArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.VirtualGatewayListenerTlsAcmCertificateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VirtualGatewayListenerTlsAcmCertificateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VirtualGatewayTlsValidationContextFileTrust:
    boto3_raw_data: "type_defs.VirtualGatewayTlsValidationContextFileTrustTypeDef" = (
        dataclasses.field()
    )

    certificateChain = field("certificateChain")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.VirtualGatewayTlsValidationContextFileTrustTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VirtualGatewayTlsValidationContextFileTrustTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VirtualGatewayTlsValidationContextSdsTrust:
    boto3_raw_data: "type_defs.VirtualGatewayTlsValidationContextSdsTrustTypeDef" = (
        dataclasses.field()
    )

    secretName = field("secretName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.VirtualGatewayTlsValidationContextSdsTrustTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VirtualGatewayTlsValidationContextSdsTrustTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VirtualGatewayTlsValidationContextAcmTrustOutput:
    boto3_raw_data: (
        "type_defs.VirtualGatewayTlsValidationContextAcmTrustOutputTypeDef"
    ) = dataclasses.field()

    certificateAuthorityArns = field("certificateAuthorityArns")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.VirtualGatewayTlsValidationContextAcmTrustOutputTypeDef"
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
                "type_defs.VirtualGatewayTlsValidationContextAcmTrustOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VirtualGatewayTlsValidationContextAcmTrust:
    boto3_raw_data: "type_defs.VirtualGatewayTlsValidationContextAcmTrustTypeDef" = (
        dataclasses.field()
    )

    certificateAuthorityArns = field("certificateAuthorityArns")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.VirtualGatewayTlsValidationContextAcmTrustTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VirtualGatewayTlsValidationContextAcmTrustTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VirtualNodeGrpcConnectionPool:
    boto3_raw_data: "type_defs.VirtualNodeGrpcConnectionPoolTypeDef" = (
        dataclasses.field()
    )

    maxRequests = field("maxRequests")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.VirtualNodeGrpcConnectionPoolTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VirtualNodeGrpcConnectionPoolTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VirtualNodeHttp2ConnectionPool:
    boto3_raw_data: "type_defs.VirtualNodeHttp2ConnectionPoolTypeDef" = (
        dataclasses.field()
    )

    maxRequests = field("maxRequests")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.VirtualNodeHttp2ConnectionPoolTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VirtualNodeHttp2ConnectionPoolTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VirtualNodeHttpConnectionPool:
    boto3_raw_data: "type_defs.VirtualNodeHttpConnectionPoolTypeDef" = (
        dataclasses.field()
    )

    maxConnections = field("maxConnections")
    maxPendingRequests = field("maxPendingRequests")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.VirtualNodeHttpConnectionPoolTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VirtualNodeHttpConnectionPoolTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VirtualNodeTcpConnectionPool:
    boto3_raw_data: "type_defs.VirtualNodeTcpConnectionPoolTypeDef" = (
        dataclasses.field()
    )

    maxConnections = field("maxConnections")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VirtualNodeTcpConnectionPoolTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VirtualNodeTcpConnectionPoolTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VirtualNodeStatus:
    boto3_raw_data: "type_defs.VirtualNodeStatusTypeDef" = dataclasses.field()

    status = field("status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VirtualNodeStatusTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VirtualNodeStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VirtualNodeServiceProvider:
    boto3_raw_data: "type_defs.VirtualNodeServiceProviderTypeDef" = dataclasses.field()

    virtualNodeName = field("virtualNodeName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VirtualNodeServiceProviderTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VirtualNodeServiceProviderTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VirtualRouterStatus:
    boto3_raw_data: "type_defs.VirtualRouterStatusTypeDef" = dataclasses.field()

    status = field("status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VirtualRouterStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VirtualRouterStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VirtualRouterServiceProvider:
    boto3_raw_data: "type_defs.VirtualRouterServiceProviderTypeDef" = (
        dataclasses.field()
    )

    virtualRouterName = field("virtualRouterName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VirtualRouterServiceProviderTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VirtualRouterServiceProviderTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VirtualServiceStatus:
    boto3_raw_data: "type_defs.VirtualServiceStatusTypeDef" = dataclasses.field()

    status = field("status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VirtualServiceStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VirtualServiceStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AwsCloudMapServiceDiscoveryOutput:
    boto3_raw_data: "type_defs.AwsCloudMapServiceDiscoveryOutputTypeDef" = (
        dataclasses.field()
    )

    namespaceName = field("namespaceName")
    serviceName = field("serviceName")

    @cached_property
    def attributes(self):  # pragma: no cover
        return AwsCloudMapInstanceAttribute.make_many(self.boto3_raw_data["attributes"])

    ipPreference = field("ipPreference")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AwsCloudMapServiceDiscoveryOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AwsCloudMapServiceDiscoveryOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AwsCloudMapServiceDiscovery:
    boto3_raw_data: "type_defs.AwsCloudMapServiceDiscoveryTypeDef" = dataclasses.field()

    namespaceName = field("namespaceName")
    serviceName = field("serviceName")

    @cached_property
    def attributes(self):  # pragma: no cover
        return AwsCloudMapInstanceAttribute.make_many(self.boto3_raw_data["attributes"])

    ipPreference = field("ipPreference")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AwsCloudMapServiceDiscoveryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AwsCloudMapServiceDiscoveryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClientTlsCertificate:
    boto3_raw_data: "type_defs.ClientTlsCertificateTypeDef" = dataclasses.field()

    @cached_property
    def file(self):  # pragma: no cover
        return ListenerTlsFileCertificate.make_one(self.boto3_raw_data["file"])

    @cached_property
    def sds(self):  # pragma: no cover
        return ListenerTlsSdsCertificate.make_one(self.boto3_raw_data["sds"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ClientTlsCertificateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClientTlsCertificateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagResourceInput:
    boto3_raw_data: "type_defs.TagResourceInputTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")

    @cached_property
    def tags(self):  # pragma: no cover
        return TagRef.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TagResourceInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TagResourceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceOutput:
    boto3_raw_data: "type_defs.ListTagsForResourceOutputTypeDef" = dataclasses.field()

    @cached_property
    def tags(self):  # pragma: no cover
        return TagRef.make_many(self.boto3_raw_data["tags"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForResourceOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GrpcRetryPolicyOutput:
    boto3_raw_data: "type_defs.GrpcRetryPolicyOutputTypeDef" = dataclasses.field()

    maxRetries = field("maxRetries")

    @cached_property
    def perRetryTimeout(self):  # pragma: no cover
        return Duration.make_one(self.boto3_raw_data["perRetryTimeout"])

    grpcRetryEvents = field("grpcRetryEvents")
    httpRetryEvents = field("httpRetryEvents")
    tcpRetryEvents = field("tcpRetryEvents")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GrpcRetryPolicyOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GrpcRetryPolicyOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GrpcRetryPolicy:
    boto3_raw_data: "type_defs.GrpcRetryPolicyTypeDef" = dataclasses.field()

    maxRetries = field("maxRetries")

    @cached_property
    def perRetryTimeout(self):  # pragma: no cover
        return Duration.make_one(self.boto3_raw_data["perRetryTimeout"])

    grpcRetryEvents = field("grpcRetryEvents")
    httpRetryEvents = field("httpRetryEvents")
    tcpRetryEvents = field("tcpRetryEvents")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GrpcRetryPolicyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GrpcRetryPolicyTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GrpcTimeout:
    boto3_raw_data: "type_defs.GrpcTimeoutTypeDef" = dataclasses.field()

    @cached_property
    def idle(self):  # pragma: no cover
        return Duration.make_one(self.boto3_raw_data["idle"])

    @cached_property
    def perRequest(self):  # pragma: no cover
        return Duration.make_one(self.boto3_raw_data["perRequest"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GrpcTimeoutTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GrpcTimeoutTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HttpRetryPolicyOutput:
    boto3_raw_data: "type_defs.HttpRetryPolicyOutputTypeDef" = dataclasses.field()

    maxRetries = field("maxRetries")

    @cached_property
    def perRetryTimeout(self):  # pragma: no cover
        return Duration.make_one(self.boto3_raw_data["perRetryTimeout"])

    httpRetryEvents = field("httpRetryEvents")
    tcpRetryEvents = field("tcpRetryEvents")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HttpRetryPolicyOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HttpRetryPolicyOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HttpRetryPolicy:
    boto3_raw_data: "type_defs.HttpRetryPolicyTypeDef" = dataclasses.field()

    maxRetries = field("maxRetries")

    @cached_property
    def perRetryTimeout(self):  # pragma: no cover
        return Duration.make_one(self.boto3_raw_data["perRetryTimeout"])

    httpRetryEvents = field("httpRetryEvents")
    tcpRetryEvents = field("tcpRetryEvents")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HttpRetryPolicyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.HttpRetryPolicyTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HttpTimeout:
    boto3_raw_data: "type_defs.HttpTimeoutTypeDef" = dataclasses.field()

    @cached_property
    def idle(self):  # pragma: no cover
        return Duration.make_one(self.boto3_raw_data["idle"])

    @cached_property
    def perRequest(self):  # pragma: no cover
        return Duration.make_one(self.boto3_raw_data["perRequest"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HttpTimeoutTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.HttpTimeoutTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OutlierDetection:
    boto3_raw_data: "type_defs.OutlierDetectionTypeDef" = dataclasses.field()

    @cached_property
    def baseEjectionDuration(self):  # pragma: no cover
        return Duration.make_one(self.boto3_raw_data["baseEjectionDuration"])

    @cached_property
    def interval(self):  # pragma: no cover
        return Duration.make_one(self.boto3_raw_data["interval"])

    maxEjectionPercent = field("maxEjectionPercent")
    maxServerErrors = field("maxServerErrors")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OutlierDetectionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OutlierDetectionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TcpTimeout:
    boto3_raw_data: "type_defs.TcpTimeoutTypeDef" = dataclasses.field()

    @cached_property
    def idle(self):  # pragma: no cover
        return Duration.make_one(self.boto3_raw_data["idle"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TcpTimeoutTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TcpTimeoutTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GrpcGatewayRouteRewrite:
    boto3_raw_data: "type_defs.GrpcGatewayRouteRewriteTypeDef" = dataclasses.field()

    @cached_property
    def hostname(self):  # pragma: no cover
        return GatewayRouteHostnameRewrite.make_one(self.boto3_raw_data["hostname"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GrpcGatewayRouteRewriteTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GrpcGatewayRouteRewriteTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGatewayRoutesOutput:
    boto3_raw_data: "type_defs.ListGatewayRoutesOutputTypeDef" = dataclasses.field()

    @cached_property
    def gatewayRoutes(self):  # pragma: no cover
        return GatewayRouteRef.make_many(self.boto3_raw_data["gatewayRoutes"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListGatewayRoutesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGatewayRoutesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GatewayRouteTarget:
    boto3_raw_data: "type_defs.GatewayRouteTargetTypeDef" = dataclasses.field()

    @cached_property
    def virtualService(self):  # pragma: no cover
        return GatewayRouteVirtualService.make_one(
            self.boto3_raw_data["virtualService"]
        )

    port = field("port")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GatewayRouteTargetTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GatewayRouteTargetTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GrpcMetadataMatchMethod:
    boto3_raw_data: "type_defs.GrpcMetadataMatchMethodTypeDef" = dataclasses.field()

    exact = field("exact")
    prefix = field("prefix")

    @cached_property
    def range(self):  # pragma: no cover
        return MatchRange.make_one(self.boto3_raw_data["range"])

    regex = field("regex")
    suffix = field("suffix")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GrpcMetadataMatchMethodTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GrpcMetadataMatchMethodTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GrpcRouteMetadataMatchMethod:
    boto3_raw_data: "type_defs.GrpcRouteMetadataMatchMethodTypeDef" = (
        dataclasses.field()
    )

    exact = field("exact")
    prefix = field("prefix")

    @cached_property
    def range(self):  # pragma: no cover
        return MatchRange.make_one(self.boto3_raw_data["range"])

    regex = field("regex")
    suffix = field("suffix")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GrpcRouteMetadataMatchMethodTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GrpcRouteMetadataMatchMethodTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HeaderMatchMethod:
    boto3_raw_data: "type_defs.HeaderMatchMethodTypeDef" = dataclasses.field()

    exact = field("exact")
    prefix = field("prefix")

    @cached_property
    def range(self):  # pragma: no cover
        return MatchRange.make_one(self.boto3_raw_data["range"])

    regex = field("regex")
    suffix = field("suffix")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HeaderMatchMethodTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HeaderMatchMethodTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GrpcRouteActionOutput:
    boto3_raw_data: "type_defs.GrpcRouteActionOutputTypeDef" = dataclasses.field()

    @cached_property
    def weightedTargets(self):  # pragma: no cover
        return WeightedTarget.make_many(self.boto3_raw_data["weightedTargets"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GrpcRouteActionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GrpcRouteActionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GrpcRouteAction:
    boto3_raw_data: "type_defs.GrpcRouteActionTypeDef" = dataclasses.field()

    @cached_property
    def weightedTargets(self):  # pragma: no cover
        return WeightedTarget.make_many(self.boto3_raw_data["weightedTargets"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GrpcRouteActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GrpcRouteActionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HttpRouteActionOutput:
    boto3_raw_data: "type_defs.HttpRouteActionOutputTypeDef" = dataclasses.field()

    @cached_property
    def weightedTargets(self):  # pragma: no cover
        return WeightedTarget.make_many(self.boto3_raw_data["weightedTargets"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HttpRouteActionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HttpRouteActionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HttpRouteAction:
    boto3_raw_data: "type_defs.HttpRouteActionTypeDef" = dataclasses.field()

    @cached_property
    def weightedTargets(self):  # pragma: no cover
        return WeightedTarget.make_many(self.boto3_raw_data["weightedTargets"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HttpRouteActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.HttpRouteActionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TcpRouteActionOutput:
    boto3_raw_data: "type_defs.TcpRouteActionOutputTypeDef" = dataclasses.field()

    @cached_property
    def weightedTargets(self):  # pragma: no cover
        return WeightedTarget.make_many(self.boto3_raw_data["weightedTargets"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TcpRouteActionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TcpRouteActionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TcpRouteAction:
    boto3_raw_data: "type_defs.TcpRouteActionTypeDef" = dataclasses.field()

    @cached_property
    def weightedTargets(self):  # pragma: no cover
        return WeightedTarget.make_many(self.boto3_raw_data["weightedTargets"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TcpRouteActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TcpRouteActionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HttpGatewayRouteRewrite:
    boto3_raw_data: "type_defs.HttpGatewayRouteRewriteTypeDef" = dataclasses.field()

    @cached_property
    def hostname(self):  # pragma: no cover
        return GatewayRouteHostnameRewrite.make_one(self.boto3_raw_data["hostname"])

    @cached_property
    def path(self):  # pragma: no cover
        return HttpGatewayRoutePathRewrite.make_one(self.boto3_raw_data["path"])

    @cached_property
    def prefix(self):  # pragma: no cover
        return HttpGatewayRoutePrefixRewrite.make_one(self.boto3_raw_data["prefix"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HttpGatewayRouteRewriteTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HttpGatewayRouteRewriteTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HttpQueryParameter:
    boto3_raw_data: "type_defs.HttpQueryParameterTypeDef" = dataclasses.field()

    name = field("name")

    @cached_property
    def match(self):  # pragma: no cover
        return QueryParameterMatch.make_one(self.boto3_raw_data["match"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HttpQueryParameterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HttpQueryParameterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoggingFormatOutput:
    boto3_raw_data: "type_defs.LoggingFormatOutputTypeDef" = dataclasses.field()

    @cached_property
    def json(self):  # pragma: no cover
        return JsonFormatRef.make_many(self.boto3_raw_data["json"])

    text = field("text")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LoggingFormatOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LoggingFormatOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoggingFormat:
    boto3_raw_data: "type_defs.LoggingFormatTypeDef" = dataclasses.field()

    @cached_property
    def json(self):  # pragma: no cover
        return JsonFormatRef.make_many(self.boto3_raw_data["json"])

    text = field("text")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LoggingFormatTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LoggingFormatTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGatewayRoutesInputPaginate:
    boto3_raw_data: "type_defs.ListGatewayRoutesInputPaginateTypeDef" = (
        dataclasses.field()
    )

    meshName = field("meshName")
    virtualGatewayName = field("virtualGatewayName")
    meshOwner = field("meshOwner")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListGatewayRoutesInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGatewayRoutesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMeshesInputPaginate:
    boto3_raw_data: "type_defs.ListMeshesInputPaginateTypeDef" = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMeshesInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMeshesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRoutesInputPaginate:
    boto3_raw_data: "type_defs.ListRoutesInputPaginateTypeDef" = dataclasses.field()

    meshName = field("meshName")
    virtualRouterName = field("virtualRouterName")
    meshOwner = field("meshOwner")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRoutesInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRoutesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceInputPaginate:
    boto3_raw_data: "type_defs.ListTagsForResourceInputPaginateTypeDef" = (
        dataclasses.field()
    )

    resourceArn = field("resourceArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListTagsForResourceInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVirtualGatewaysInputPaginate:
    boto3_raw_data: "type_defs.ListVirtualGatewaysInputPaginateTypeDef" = (
        dataclasses.field()
    )

    meshName = field("meshName")
    meshOwner = field("meshOwner")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListVirtualGatewaysInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVirtualGatewaysInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVirtualNodesInputPaginate:
    boto3_raw_data: "type_defs.ListVirtualNodesInputPaginateTypeDef" = (
        dataclasses.field()
    )

    meshName = field("meshName")
    meshOwner = field("meshOwner")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListVirtualNodesInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVirtualNodesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVirtualRoutersInputPaginate:
    boto3_raw_data: "type_defs.ListVirtualRoutersInputPaginateTypeDef" = (
        dataclasses.field()
    )

    meshName = field("meshName")
    meshOwner = field("meshOwner")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListVirtualRoutersInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVirtualRoutersInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVirtualServicesInputPaginate:
    boto3_raw_data: "type_defs.ListVirtualServicesInputPaginateTypeDef" = (
        dataclasses.field()
    )

    meshName = field("meshName")
    meshOwner = field("meshOwner")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListVirtualServicesInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVirtualServicesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMeshesOutput:
    boto3_raw_data: "type_defs.ListMeshesOutputTypeDef" = dataclasses.field()

    @cached_property
    def meshes(self):  # pragma: no cover
        return MeshRef.make_many(self.boto3_raw_data["meshes"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListMeshesOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMeshesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRoutesOutput:
    boto3_raw_data: "type_defs.ListRoutesOutputTypeDef" = dataclasses.field()

    @cached_property
    def routes(self):  # pragma: no cover
        return RouteRef.make_many(self.boto3_raw_data["routes"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListRoutesOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRoutesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVirtualGatewaysOutput:
    boto3_raw_data: "type_defs.ListVirtualGatewaysOutputTypeDef" = dataclasses.field()

    @cached_property
    def virtualGateways(self):  # pragma: no cover
        return VirtualGatewayRef.make_many(self.boto3_raw_data["virtualGateways"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListVirtualGatewaysOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVirtualGatewaysOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVirtualNodesOutput:
    boto3_raw_data: "type_defs.ListVirtualNodesOutputTypeDef" = dataclasses.field()

    @cached_property
    def virtualNodes(self):  # pragma: no cover
        return VirtualNodeRef.make_many(self.boto3_raw_data["virtualNodes"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListVirtualNodesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVirtualNodesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVirtualRoutersOutput:
    boto3_raw_data: "type_defs.ListVirtualRoutersOutputTypeDef" = dataclasses.field()

    @cached_property
    def virtualRouters(self):  # pragma: no cover
        return VirtualRouterRef.make_many(self.boto3_raw_data["virtualRouters"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListVirtualRoutersOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVirtualRoutersOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVirtualServicesOutput:
    boto3_raw_data: "type_defs.ListVirtualServicesOutputTypeDef" = dataclasses.field()

    @cached_property
    def virtualServices(self):  # pragma: no cover
        return VirtualServiceRef.make_many(self.boto3_raw_data["virtualServices"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListVirtualServicesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVirtualServicesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VirtualRouterListener:
    boto3_raw_data: "type_defs.VirtualRouterListenerTypeDef" = dataclasses.field()

    @cached_property
    def portMapping(self):  # pragma: no cover
        return PortMapping.make_one(self.boto3_raw_data["portMapping"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VirtualRouterListenerTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VirtualRouterListenerTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListenerTlsCertificate:
    boto3_raw_data: "type_defs.ListenerTlsCertificateTypeDef" = dataclasses.field()

    @cached_property
    def acm(self):  # pragma: no cover
        return ListenerTlsAcmCertificate.make_one(self.boto3_raw_data["acm"])

    @cached_property
    def file(self):  # pragma: no cover
        return ListenerTlsFileCertificate.make_one(self.boto3_raw_data["file"])

    @cached_property
    def sds(self):  # pragma: no cover
        return ListenerTlsSdsCertificate.make_one(self.boto3_raw_data["sds"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListenerTlsCertificateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListenerTlsCertificateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListenerTlsValidationContextTrust:
    boto3_raw_data: "type_defs.ListenerTlsValidationContextTrustTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def file(self):  # pragma: no cover
        return TlsValidationContextFileTrust.make_one(self.boto3_raw_data["file"])

    @cached_property
    def sds(self):  # pragma: no cover
        return TlsValidationContextSdsTrust.make_one(self.boto3_raw_data["sds"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListenerTlsValidationContextTrustTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListenerTlsValidationContextTrustTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MeshSpec:
    boto3_raw_data: "type_defs.MeshSpecTypeDef" = dataclasses.field()

    @cached_property
    def egressFilter(self):  # pragma: no cover
        return EgressFilter.make_one(self.boto3_raw_data["egressFilter"])

    @cached_property
    def serviceDiscovery(self):  # pragma: no cover
        return MeshServiceDiscovery.make_one(self.boto3_raw_data["serviceDiscovery"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MeshSpecTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MeshSpecTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SubjectAlternativeNamesOutput:
    boto3_raw_data: "type_defs.SubjectAlternativeNamesOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def match(self):  # pragma: no cover
        return SubjectAlternativeNameMatchersOutput.make_one(
            self.boto3_raw_data["match"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SubjectAlternativeNamesOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SubjectAlternativeNamesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SubjectAlternativeNames:
    boto3_raw_data: "type_defs.SubjectAlternativeNamesTypeDef" = dataclasses.field()

    @cached_property
    def match(self):  # pragma: no cover
        return SubjectAlternativeNameMatchers.make_one(self.boto3_raw_data["match"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SubjectAlternativeNamesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SubjectAlternativeNamesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TlsValidationContextTrustOutput:
    boto3_raw_data: "type_defs.TlsValidationContextTrustOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def acm(self):  # pragma: no cover
        return TlsValidationContextAcmTrustOutput.make_one(self.boto3_raw_data["acm"])

    @cached_property
    def file(self):  # pragma: no cover
        return TlsValidationContextFileTrust.make_one(self.boto3_raw_data["file"])

    @cached_property
    def sds(self):  # pragma: no cover
        return TlsValidationContextSdsTrust.make_one(self.boto3_raw_data["sds"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.TlsValidationContextTrustOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TlsValidationContextTrustOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TlsValidationContextTrust:
    boto3_raw_data: "type_defs.TlsValidationContextTrustTypeDef" = dataclasses.field()

    @cached_property
    def acm(self):  # pragma: no cover
        return TlsValidationContextAcmTrust.make_one(self.boto3_raw_data["acm"])

    @cached_property
    def file(self):  # pragma: no cover
        return TlsValidationContextFileTrust.make_one(self.boto3_raw_data["file"])

    @cached_property
    def sds(self):  # pragma: no cover
        return TlsValidationContextSdsTrust.make_one(self.boto3_raw_data["sds"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TlsValidationContextTrustTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TlsValidationContextTrustTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VirtualGatewayClientTlsCertificate:
    boto3_raw_data: "type_defs.VirtualGatewayClientTlsCertificateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def file(self):  # pragma: no cover
        return VirtualGatewayListenerTlsFileCertificate.make_one(
            self.boto3_raw_data["file"]
        )

    @cached_property
    def sds(self):  # pragma: no cover
        return VirtualGatewayListenerTlsSdsCertificate.make_one(
            self.boto3_raw_data["sds"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.VirtualGatewayClientTlsCertificateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VirtualGatewayClientTlsCertificateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VirtualGatewayConnectionPool:
    boto3_raw_data: "type_defs.VirtualGatewayConnectionPoolTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def grpc(self):  # pragma: no cover
        return VirtualGatewayGrpcConnectionPool.make_one(self.boto3_raw_data["grpc"])

    @cached_property
    def http(self):  # pragma: no cover
        return VirtualGatewayHttpConnectionPool.make_one(self.boto3_raw_data["http"])

    @cached_property
    def http2(self):  # pragma: no cover
        return VirtualGatewayHttp2ConnectionPool.make_one(self.boto3_raw_data["http2"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VirtualGatewayConnectionPoolTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VirtualGatewayConnectionPoolTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VirtualGatewayListenerTlsCertificate:
    boto3_raw_data: "type_defs.VirtualGatewayListenerTlsCertificateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def acm(self):  # pragma: no cover
        return VirtualGatewayListenerTlsAcmCertificate.make_one(
            self.boto3_raw_data["acm"]
        )

    @cached_property
    def file(self):  # pragma: no cover
        return VirtualGatewayListenerTlsFileCertificate.make_one(
            self.boto3_raw_data["file"]
        )

    @cached_property
    def sds(self):  # pragma: no cover
        return VirtualGatewayListenerTlsSdsCertificate.make_one(
            self.boto3_raw_data["sds"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.VirtualGatewayListenerTlsCertificateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VirtualGatewayListenerTlsCertificateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VirtualGatewayListenerTlsValidationContextTrust:
    boto3_raw_data: (
        "type_defs.VirtualGatewayListenerTlsValidationContextTrustTypeDef"
    ) = dataclasses.field()

    @cached_property
    def file(self):  # pragma: no cover
        return VirtualGatewayTlsValidationContextFileTrust.make_one(
            self.boto3_raw_data["file"]
        )

    @cached_property
    def sds(self):  # pragma: no cover
        return VirtualGatewayTlsValidationContextSdsTrust.make_one(
            self.boto3_raw_data["sds"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.VirtualGatewayListenerTlsValidationContextTrustTypeDef"
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
                "type_defs.VirtualGatewayListenerTlsValidationContextTrustTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VirtualGatewayTlsValidationContextTrustOutput:
    boto3_raw_data: "type_defs.VirtualGatewayTlsValidationContextTrustOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def acm(self):  # pragma: no cover
        return VirtualGatewayTlsValidationContextAcmTrustOutput.make_one(
            self.boto3_raw_data["acm"]
        )

    @cached_property
    def file(self):  # pragma: no cover
        return VirtualGatewayTlsValidationContextFileTrust.make_one(
            self.boto3_raw_data["file"]
        )

    @cached_property
    def sds(self):  # pragma: no cover
        return VirtualGatewayTlsValidationContextSdsTrust.make_one(
            self.boto3_raw_data["sds"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.VirtualGatewayTlsValidationContextTrustOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VirtualGatewayTlsValidationContextTrustOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VirtualGatewayTlsValidationContextTrust:
    boto3_raw_data: "type_defs.VirtualGatewayTlsValidationContextTrustTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def acm(self):  # pragma: no cover
        return VirtualGatewayTlsValidationContextAcmTrust.make_one(
            self.boto3_raw_data["acm"]
        )

    @cached_property
    def file(self):  # pragma: no cover
        return VirtualGatewayTlsValidationContextFileTrust.make_one(
            self.boto3_raw_data["file"]
        )

    @cached_property
    def sds(self):  # pragma: no cover
        return VirtualGatewayTlsValidationContextSdsTrust.make_one(
            self.boto3_raw_data["sds"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.VirtualGatewayTlsValidationContextTrustTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VirtualGatewayTlsValidationContextTrustTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VirtualNodeConnectionPool:
    boto3_raw_data: "type_defs.VirtualNodeConnectionPoolTypeDef" = dataclasses.field()

    @cached_property
    def grpc(self):  # pragma: no cover
        return VirtualNodeGrpcConnectionPool.make_one(self.boto3_raw_data["grpc"])

    @cached_property
    def http(self):  # pragma: no cover
        return VirtualNodeHttpConnectionPool.make_one(self.boto3_raw_data["http"])

    @cached_property
    def http2(self):  # pragma: no cover
        return VirtualNodeHttp2ConnectionPool.make_one(self.boto3_raw_data["http2"])

    @cached_property
    def tcp(self):  # pragma: no cover
        return VirtualNodeTcpConnectionPool.make_one(self.boto3_raw_data["tcp"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VirtualNodeConnectionPoolTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VirtualNodeConnectionPoolTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VirtualServiceProvider:
    boto3_raw_data: "type_defs.VirtualServiceProviderTypeDef" = dataclasses.field()

    @cached_property
    def virtualNode(self):  # pragma: no cover
        return VirtualNodeServiceProvider.make_one(self.boto3_raw_data["virtualNode"])

    @cached_property
    def virtualRouter(self):  # pragma: no cover
        return VirtualRouterServiceProvider.make_one(
            self.boto3_raw_data["virtualRouter"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VirtualServiceProviderTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VirtualServiceProviderTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceDiscoveryOutput:
    boto3_raw_data: "type_defs.ServiceDiscoveryOutputTypeDef" = dataclasses.field()

    @cached_property
    def awsCloudMap(self):  # pragma: no cover
        return AwsCloudMapServiceDiscoveryOutput.make_one(
            self.boto3_raw_data["awsCloudMap"]
        )

    @cached_property
    def dns(self):  # pragma: no cover
        return DnsServiceDiscovery.make_one(self.boto3_raw_data["dns"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ServiceDiscoveryOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceDiscoveryOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceDiscovery:
    boto3_raw_data: "type_defs.ServiceDiscoveryTypeDef" = dataclasses.field()

    @cached_property
    def awsCloudMap(self):  # pragma: no cover
        return AwsCloudMapServiceDiscovery.make_one(self.boto3_raw_data["awsCloudMap"])

    @cached_property
    def dns(self):  # pragma: no cover
        return DnsServiceDiscovery.make_one(self.boto3_raw_data["dns"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ServiceDiscoveryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceDiscoveryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListenerTimeout:
    boto3_raw_data: "type_defs.ListenerTimeoutTypeDef" = dataclasses.field()

    @cached_property
    def grpc(self):  # pragma: no cover
        return GrpcTimeout.make_one(self.boto3_raw_data["grpc"])

    @cached_property
    def http(self):  # pragma: no cover
        return HttpTimeout.make_one(self.boto3_raw_data["http"])

    @cached_property
    def http2(self):  # pragma: no cover
        return HttpTimeout.make_one(self.boto3_raw_data["http2"])

    @cached_property
    def tcp(self):  # pragma: no cover
        return TcpTimeout.make_one(self.boto3_raw_data["tcp"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListenerTimeoutTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListenerTimeoutTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GrpcGatewayRouteAction:
    boto3_raw_data: "type_defs.GrpcGatewayRouteActionTypeDef" = dataclasses.field()

    @cached_property
    def target(self):  # pragma: no cover
        return GatewayRouteTarget.make_one(self.boto3_raw_data["target"])

    @cached_property
    def rewrite(self):  # pragma: no cover
        return GrpcGatewayRouteRewrite.make_one(self.boto3_raw_data["rewrite"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GrpcGatewayRouteActionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GrpcGatewayRouteActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GrpcGatewayRouteMetadata:
    boto3_raw_data: "type_defs.GrpcGatewayRouteMetadataTypeDef" = dataclasses.field()

    name = field("name")
    invert = field("invert")

    @cached_property
    def match(self):  # pragma: no cover
        return GrpcMetadataMatchMethod.make_one(self.boto3_raw_data["match"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GrpcGatewayRouteMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GrpcGatewayRouteMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GrpcRouteMetadata:
    boto3_raw_data: "type_defs.GrpcRouteMetadataTypeDef" = dataclasses.field()

    name = field("name")
    invert = field("invert")

    @cached_property
    def match(self):  # pragma: no cover
        return GrpcRouteMetadataMatchMethod.make_one(self.boto3_raw_data["match"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GrpcRouteMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GrpcRouteMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HttpGatewayRouteHeader:
    boto3_raw_data: "type_defs.HttpGatewayRouteHeaderTypeDef" = dataclasses.field()

    name = field("name")
    invert = field("invert")

    @cached_property
    def match(self):  # pragma: no cover
        return HeaderMatchMethod.make_one(self.boto3_raw_data["match"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HttpGatewayRouteHeaderTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HttpGatewayRouteHeaderTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HttpRouteHeader:
    boto3_raw_data: "type_defs.HttpRouteHeaderTypeDef" = dataclasses.field()

    name = field("name")
    invert = field("invert")

    @cached_property
    def match(self):  # pragma: no cover
        return HeaderMatchMethod.make_one(self.boto3_raw_data["match"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HttpRouteHeaderTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.HttpRouteHeaderTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TcpRouteOutput:
    boto3_raw_data: "type_defs.TcpRouteOutputTypeDef" = dataclasses.field()

    @cached_property
    def action(self):  # pragma: no cover
        return TcpRouteActionOutput.make_one(self.boto3_raw_data["action"])

    @cached_property
    def match(self):  # pragma: no cover
        return TcpRouteMatch.make_one(self.boto3_raw_data["match"])

    @cached_property
    def timeout(self):  # pragma: no cover
        return TcpTimeout.make_one(self.boto3_raw_data["timeout"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TcpRouteOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TcpRouteOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TcpRoute:
    boto3_raw_data: "type_defs.TcpRouteTypeDef" = dataclasses.field()

    @cached_property
    def action(self):  # pragma: no cover
        return TcpRouteAction.make_one(self.boto3_raw_data["action"])

    @cached_property
    def match(self):  # pragma: no cover
        return TcpRouteMatch.make_one(self.boto3_raw_data["match"])

    @cached_property
    def timeout(self):  # pragma: no cover
        return TcpTimeout.make_one(self.boto3_raw_data["timeout"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TcpRouteTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TcpRouteTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HttpGatewayRouteAction:
    boto3_raw_data: "type_defs.HttpGatewayRouteActionTypeDef" = dataclasses.field()

    @cached_property
    def target(self):  # pragma: no cover
        return GatewayRouteTarget.make_one(self.boto3_raw_data["target"])

    @cached_property
    def rewrite(self):  # pragma: no cover
        return HttpGatewayRouteRewrite.make_one(self.boto3_raw_data["rewrite"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HttpGatewayRouteActionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HttpGatewayRouteActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FileAccessLogOutput:
    boto3_raw_data: "type_defs.FileAccessLogOutputTypeDef" = dataclasses.field()

    path = field("path")

    @cached_property
    def format(self):  # pragma: no cover
        return LoggingFormatOutput.make_one(self.boto3_raw_data["format"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FileAccessLogOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FileAccessLogOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VirtualGatewayFileAccessLogOutput:
    boto3_raw_data: "type_defs.VirtualGatewayFileAccessLogOutputTypeDef" = (
        dataclasses.field()
    )

    path = field("path")

    @cached_property
    def format(self):  # pragma: no cover
        return LoggingFormatOutput.make_one(self.boto3_raw_data["format"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.VirtualGatewayFileAccessLogOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VirtualGatewayFileAccessLogOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FileAccessLog:
    boto3_raw_data: "type_defs.FileAccessLogTypeDef" = dataclasses.field()

    path = field("path")

    @cached_property
    def format(self):  # pragma: no cover
        return LoggingFormat.make_one(self.boto3_raw_data["format"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FileAccessLogTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FileAccessLogTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VirtualGatewayFileAccessLog:
    boto3_raw_data: "type_defs.VirtualGatewayFileAccessLogTypeDef" = dataclasses.field()

    path = field("path")

    @cached_property
    def format(self):  # pragma: no cover
        return LoggingFormat.make_one(self.boto3_raw_data["format"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VirtualGatewayFileAccessLogTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VirtualGatewayFileAccessLogTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VirtualRouterSpecOutput:
    boto3_raw_data: "type_defs.VirtualRouterSpecOutputTypeDef" = dataclasses.field()

    @cached_property
    def listeners(self):  # pragma: no cover
        return VirtualRouterListener.make_many(self.boto3_raw_data["listeners"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VirtualRouterSpecOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VirtualRouterSpecOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VirtualRouterSpec:
    boto3_raw_data: "type_defs.VirtualRouterSpecTypeDef" = dataclasses.field()

    @cached_property
    def listeners(self):  # pragma: no cover
        return VirtualRouterListener.make_many(self.boto3_raw_data["listeners"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VirtualRouterSpecTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VirtualRouterSpecTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMeshInput:
    boto3_raw_data: "type_defs.CreateMeshInputTypeDef" = dataclasses.field()

    meshName = field("meshName")
    clientToken = field("clientToken")

    @cached_property
    def spec(self):  # pragma: no cover
        return MeshSpec.make_one(self.boto3_raw_data["spec"])

    @cached_property
    def tags(self):  # pragma: no cover
        return TagRef.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateMeshInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CreateMeshInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MeshData:
    boto3_raw_data: "type_defs.MeshDataTypeDef" = dataclasses.field()

    meshName = field("meshName")

    @cached_property
    def metadata(self):  # pragma: no cover
        return ResourceMetadata.make_one(self.boto3_raw_data["metadata"])

    @cached_property
    def spec(self):  # pragma: no cover
        return MeshSpec.make_one(self.boto3_raw_data["spec"])

    @cached_property
    def status(self):  # pragma: no cover
        return MeshStatus.make_one(self.boto3_raw_data["status"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MeshDataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MeshDataTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateMeshInput:
    boto3_raw_data: "type_defs.UpdateMeshInputTypeDef" = dataclasses.field()

    meshName = field("meshName")
    clientToken = field("clientToken")

    @cached_property
    def spec(self):  # pragma: no cover
        return MeshSpec.make_one(self.boto3_raw_data["spec"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateMeshInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UpdateMeshInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListenerTlsValidationContextOutput:
    boto3_raw_data: "type_defs.ListenerTlsValidationContextOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def trust(self):  # pragma: no cover
        return ListenerTlsValidationContextTrust.make_one(self.boto3_raw_data["trust"])

    @cached_property
    def subjectAlternativeNames(self):  # pragma: no cover
        return SubjectAlternativeNamesOutput.make_one(
            self.boto3_raw_data["subjectAlternativeNames"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListenerTlsValidationContextOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListenerTlsValidationContextOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListenerTlsValidationContext:
    boto3_raw_data: "type_defs.ListenerTlsValidationContextTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def trust(self):  # pragma: no cover
        return ListenerTlsValidationContextTrust.make_one(self.boto3_raw_data["trust"])

    @cached_property
    def subjectAlternativeNames(self):  # pragma: no cover
        return SubjectAlternativeNames.make_one(
            self.boto3_raw_data["subjectAlternativeNames"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListenerTlsValidationContextTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListenerTlsValidationContextTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TlsValidationContextOutput:
    boto3_raw_data: "type_defs.TlsValidationContextOutputTypeDef" = dataclasses.field()

    @cached_property
    def trust(self):  # pragma: no cover
        return TlsValidationContextTrustOutput.make_one(self.boto3_raw_data["trust"])

    @cached_property
    def subjectAlternativeNames(self):  # pragma: no cover
        return SubjectAlternativeNamesOutput.make_one(
            self.boto3_raw_data["subjectAlternativeNames"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TlsValidationContextOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TlsValidationContextOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TlsValidationContext:
    boto3_raw_data: "type_defs.TlsValidationContextTypeDef" = dataclasses.field()

    @cached_property
    def trust(self):  # pragma: no cover
        return TlsValidationContextTrust.make_one(self.boto3_raw_data["trust"])

    @cached_property
    def subjectAlternativeNames(self):  # pragma: no cover
        return SubjectAlternativeNames.make_one(
            self.boto3_raw_data["subjectAlternativeNames"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TlsValidationContextTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TlsValidationContextTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VirtualGatewayListenerTlsValidationContextOutput:
    boto3_raw_data: (
        "type_defs.VirtualGatewayListenerTlsValidationContextOutputTypeDef"
    ) = dataclasses.field()

    @cached_property
    def trust(self):  # pragma: no cover
        return VirtualGatewayListenerTlsValidationContextTrust.make_one(
            self.boto3_raw_data["trust"]
        )

    @cached_property
    def subjectAlternativeNames(self):  # pragma: no cover
        return SubjectAlternativeNamesOutput.make_one(
            self.boto3_raw_data["subjectAlternativeNames"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.VirtualGatewayListenerTlsValidationContextOutputTypeDef"
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
                "type_defs.VirtualGatewayListenerTlsValidationContextOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VirtualGatewayListenerTlsValidationContext:
    boto3_raw_data: "type_defs.VirtualGatewayListenerTlsValidationContextTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def trust(self):  # pragma: no cover
        return VirtualGatewayListenerTlsValidationContextTrust.make_one(
            self.boto3_raw_data["trust"]
        )

    @cached_property
    def subjectAlternativeNames(self):  # pragma: no cover
        return SubjectAlternativeNames.make_one(
            self.boto3_raw_data["subjectAlternativeNames"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.VirtualGatewayListenerTlsValidationContextTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VirtualGatewayListenerTlsValidationContextTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VirtualGatewayTlsValidationContextOutput:
    boto3_raw_data: "type_defs.VirtualGatewayTlsValidationContextOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def trust(self):  # pragma: no cover
        return VirtualGatewayTlsValidationContextTrustOutput.make_one(
            self.boto3_raw_data["trust"]
        )

    @cached_property
    def subjectAlternativeNames(self):  # pragma: no cover
        return SubjectAlternativeNamesOutput.make_one(
            self.boto3_raw_data["subjectAlternativeNames"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.VirtualGatewayTlsValidationContextOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VirtualGatewayTlsValidationContextOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VirtualGatewayTlsValidationContext:
    boto3_raw_data: "type_defs.VirtualGatewayTlsValidationContextTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def trust(self):  # pragma: no cover
        return VirtualGatewayTlsValidationContextTrust.make_one(
            self.boto3_raw_data["trust"]
        )

    @cached_property
    def subjectAlternativeNames(self):  # pragma: no cover
        return SubjectAlternativeNames.make_one(
            self.boto3_raw_data["subjectAlternativeNames"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.VirtualGatewayTlsValidationContextTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VirtualGatewayTlsValidationContextTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VirtualServiceSpec:
    boto3_raw_data: "type_defs.VirtualServiceSpecTypeDef" = dataclasses.field()

    @cached_property
    def provider(self):  # pragma: no cover
        return VirtualServiceProvider.make_one(self.boto3_raw_data["provider"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VirtualServiceSpecTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VirtualServiceSpecTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GrpcGatewayRouteMatchOutput:
    boto3_raw_data: "type_defs.GrpcGatewayRouteMatchOutputTypeDef" = dataclasses.field()

    @cached_property
    def hostname(self):  # pragma: no cover
        return GatewayRouteHostnameMatch.make_one(self.boto3_raw_data["hostname"])

    @cached_property
    def metadata(self):  # pragma: no cover
        return GrpcGatewayRouteMetadata.make_many(self.boto3_raw_data["metadata"])

    port = field("port")
    serviceName = field("serviceName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GrpcGatewayRouteMatchOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GrpcGatewayRouteMatchOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GrpcGatewayRouteMatch:
    boto3_raw_data: "type_defs.GrpcGatewayRouteMatchTypeDef" = dataclasses.field()

    @cached_property
    def hostname(self):  # pragma: no cover
        return GatewayRouteHostnameMatch.make_one(self.boto3_raw_data["hostname"])

    @cached_property
    def metadata(self):  # pragma: no cover
        return GrpcGatewayRouteMetadata.make_many(self.boto3_raw_data["metadata"])

    port = field("port")
    serviceName = field("serviceName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GrpcGatewayRouteMatchTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GrpcGatewayRouteMatchTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GrpcRouteMatchOutput:
    boto3_raw_data: "type_defs.GrpcRouteMatchOutputTypeDef" = dataclasses.field()

    @cached_property
    def metadata(self):  # pragma: no cover
        return GrpcRouteMetadata.make_many(self.boto3_raw_data["metadata"])

    methodName = field("methodName")
    port = field("port")
    serviceName = field("serviceName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GrpcRouteMatchOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GrpcRouteMatchOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GrpcRouteMatch:
    boto3_raw_data: "type_defs.GrpcRouteMatchTypeDef" = dataclasses.field()

    @cached_property
    def metadata(self):  # pragma: no cover
        return GrpcRouteMetadata.make_many(self.boto3_raw_data["metadata"])

    methodName = field("methodName")
    port = field("port")
    serviceName = field("serviceName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GrpcRouteMatchTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GrpcRouteMatchTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HttpGatewayRouteMatchOutput:
    boto3_raw_data: "type_defs.HttpGatewayRouteMatchOutputTypeDef" = dataclasses.field()

    @cached_property
    def headers(self):  # pragma: no cover
        return HttpGatewayRouteHeader.make_many(self.boto3_raw_data["headers"])

    @cached_property
    def hostname(self):  # pragma: no cover
        return GatewayRouteHostnameMatch.make_one(self.boto3_raw_data["hostname"])

    method = field("method")

    @cached_property
    def path(self):  # pragma: no cover
        return HttpPathMatch.make_one(self.boto3_raw_data["path"])

    port = field("port")
    prefix = field("prefix")

    @cached_property
    def queryParameters(self):  # pragma: no cover
        return HttpQueryParameter.make_many(self.boto3_raw_data["queryParameters"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HttpGatewayRouteMatchOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HttpGatewayRouteMatchOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HttpGatewayRouteMatch:
    boto3_raw_data: "type_defs.HttpGatewayRouteMatchTypeDef" = dataclasses.field()

    @cached_property
    def headers(self):  # pragma: no cover
        return HttpGatewayRouteHeader.make_many(self.boto3_raw_data["headers"])

    @cached_property
    def hostname(self):  # pragma: no cover
        return GatewayRouteHostnameMatch.make_one(self.boto3_raw_data["hostname"])

    method = field("method")

    @cached_property
    def path(self):  # pragma: no cover
        return HttpPathMatch.make_one(self.boto3_raw_data["path"])

    port = field("port")
    prefix = field("prefix")

    @cached_property
    def queryParameters(self):  # pragma: no cover
        return HttpQueryParameter.make_many(self.boto3_raw_data["queryParameters"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HttpGatewayRouteMatchTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HttpGatewayRouteMatchTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HttpRouteMatchOutput:
    boto3_raw_data: "type_defs.HttpRouteMatchOutputTypeDef" = dataclasses.field()

    @cached_property
    def headers(self):  # pragma: no cover
        return HttpRouteHeader.make_many(self.boto3_raw_data["headers"])

    method = field("method")

    @cached_property
    def path(self):  # pragma: no cover
        return HttpPathMatch.make_one(self.boto3_raw_data["path"])

    port = field("port")
    prefix = field("prefix")

    @cached_property
    def queryParameters(self):  # pragma: no cover
        return HttpQueryParameter.make_many(self.boto3_raw_data["queryParameters"])

    scheme = field("scheme")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HttpRouteMatchOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HttpRouteMatchOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HttpRouteMatch:
    boto3_raw_data: "type_defs.HttpRouteMatchTypeDef" = dataclasses.field()

    @cached_property
    def headers(self):  # pragma: no cover
        return HttpRouteHeader.make_many(self.boto3_raw_data["headers"])

    method = field("method")

    @cached_property
    def path(self):  # pragma: no cover
        return HttpPathMatch.make_one(self.boto3_raw_data["path"])

    port = field("port")
    prefix = field("prefix")

    @cached_property
    def queryParameters(self):  # pragma: no cover
        return HttpQueryParameter.make_many(self.boto3_raw_data["queryParameters"])

    scheme = field("scheme")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HttpRouteMatchTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.HttpRouteMatchTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccessLogOutput:
    boto3_raw_data: "type_defs.AccessLogOutputTypeDef" = dataclasses.field()

    @cached_property
    def file(self):  # pragma: no cover
        return FileAccessLogOutput.make_one(self.boto3_raw_data["file"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AccessLogOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AccessLogOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VirtualGatewayAccessLogOutput:
    boto3_raw_data: "type_defs.VirtualGatewayAccessLogOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def file(self):  # pragma: no cover
        return VirtualGatewayFileAccessLogOutput.make_one(self.boto3_raw_data["file"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.VirtualGatewayAccessLogOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VirtualGatewayAccessLogOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccessLog:
    boto3_raw_data: "type_defs.AccessLogTypeDef" = dataclasses.field()

    @cached_property
    def file(self):  # pragma: no cover
        return FileAccessLog.make_one(self.boto3_raw_data["file"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AccessLogTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AccessLogTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VirtualGatewayAccessLog:
    boto3_raw_data: "type_defs.VirtualGatewayAccessLogTypeDef" = dataclasses.field()

    @cached_property
    def file(self):  # pragma: no cover
        return VirtualGatewayFileAccessLog.make_one(self.boto3_raw_data["file"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VirtualGatewayAccessLogTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VirtualGatewayAccessLogTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VirtualRouterData:
    boto3_raw_data: "type_defs.VirtualRouterDataTypeDef" = dataclasses.field()

    meshName = field("meshName")

    @cached_property
    def metadata(self):  # pragma: no cover
        return ResourceMetadata.make_one(self.boto3_raw_data["metadata"])

    @cached_property
    def spec(self):  # pragma: no cover
        return VirtualRouterSpecOutput.make_one(self.boto3_raw_data["spec"])

    @cached_property
    def status(self):  # pragma: no cover
        return VirtualRouterStatus.make_one(self.boto3_raw_data["status"])

    virtualRouterName = field("virtualRouterName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VirtualRouterDataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VirtualRouterDataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMeshOutput:
    boto3_raw_data: "type_defs.CreateMeshOutputTypeDef" = dataclasses.field()

    @cached_property
    def mesh(self):  # pragma: no cover
        return MeshData.make_one(self.boto3_raw_data["mesh"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateMeshOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMeshOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteMeshOutput:
    boto3_raw_data: "type_defs.DeleteMeshOutputTypeDef" = dataclasses.field()

    @cached_property
    def mesh(self):  # pragma: no cover
        return MeshData.make_one(self.boto3_raw_data["mesh"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteMeshOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteMeshOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMeshOutput:
    boto3_raw_data: "type_defs.DescribeMeshOutputTypeDef" = dataclasses.field()

    @cached_property
    def mesh(self):  # pragma: no cover
        return MeshData.make_one(self.boto3_raw_data["mesh"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeMeshOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMeshOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateMeshOutput:
    boto3_raw_data: "type_defs.UpdateMeshOutputTypeDef" = dataclasses.field()

    @cached_property
    def mesh(self):  # pragma: no cover
        return MeshData.make_one(self.boto3_raw_data["mesh"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateMeshOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateMeshOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListenerTlsOutput:
    boto3_raw_data: "type_defs.ListenerTlsOutputTypeDef" = dataclasses.field()

    @cached_property
    def certificate(self):  # pragma: no cover
        return ListenerTlsCertificate.make_one(self.boto3_raw_data["certificate"])

    mode = field("mode")

    @cached_property
    def validation(self):  # pragma: no cover
        return ListenerTlsValidationContextOutput.make_one(
            self.boto3_raw_data["validation"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListenerTlsOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListenerTlsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListenerTls:
    boto3_raw_data: "type_defs.ListenerTlsTypeDef" = dataclasses.field()

    @cached_property
    def certificate(self):  # pragma: no cover
        return ListenerTlsCertificate.make_one(self.boto3_raw_data["certificate"])

    mode = field("mode")

    @cached_property
    def validation(self):  # pragma: no cover
        return ListenerTlsValidationContext.make_one(self.boto3_raw_data["validation"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListenerTlsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListenerTlsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClientPolicyTlsOutput:
    boto3_raw_data: "type_defs.ClientPolicyTlsOutputTypeDef" = dataclasses.field()

    @cached_property
    def validation(self):  # pragma: no cover
        return TlsValidationContextOutput.make_one(self.boto3_raw_data["validation"])

    @cached_property
    def certificate(self):  # pragma: no cover
        return ClientTlsCertificate.make_one(self.boto3_raw_data["certificate"])

    enforce = field("enforce")
    ports = field("ports")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ClientPolicyTlsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClientPolicyTlsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClientPolicyTls:
    boto3_raw_data: "type_defs.ClientPolicyTlsTypeDef" = dataclasses.field()

    @cached_property
    def validation(self):  # pragma: no cover
        return TlsValidationContext.make_one(self.boto3_raw_data["validation"])

    @cached_property
    def certificate(self):  # pragma: no cover
        return ClientTlsCertificate.make_one(self.boto3_raw_data["certificate"])

    enforce = field("enforce")
    ports = field("ports")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ClientPolicyTlsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ClientPolicyTlsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VirtualGatewayListenerTlsOutput:
    boto3_raw_data: "type_defs.VirtualGatewayListenerTlsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def certificate(self):  # pragma: no cover
        return VirtualGatewayListenerTlsCertificate.make_one(
            self.boto3_raw_data["certificate"]
        )

    mode = field("mode")

    @cached_property
    def validation(self):  # pragma: no cover
        return VirtualGatewayListenerTlsValidationContextOutput.make_one(
            self.boto3_raw_data["validation"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.VirtualGatewayListenerTlsOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VirtualGatewayListenerTlsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VirtualGatewayListenerTls:
    boto3_raw_data: "type_defs.VirtualGatewayListenerTlsTypeDef" = dataclasses.field()

    @cached_property
    def certificate(self):  # pragma: no cover
        return VirtualGatewayListenerTlsCertificate.make_one(
            self.boto3_raw_data["certificate"]
        )

    mode = field("mode")

    @cached_property
    def validation(self):  # pragma: no cover
        return VirtualGatewayListenerTlsValidationContext.make_one(
            self.boto3_raw_data["validation"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VirtualGatewayListenerTlsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VirtualGatewayListenerTlsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VirtualGatewayClientPolicyTlsOutput:
    boto3_raw_data: "type_defs.VirtualGatewayClientPolicyTlsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def validation(self):  # pragma: no cover
        return VirtualGatewayTlsValidationContextOutput.make_one(
            self.boto3_raw_data["validation"]
        )

    @cached_property
    def certificate(self):  # pragma: no cover
        return VirtualGatewayClientTlsCertificate.make_one(
            self.boto3_raw_data["certificate"]
        )

    enforce = field("enforce")
    ports = field("ports")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.VirtualGatewayClientPolicyTlsOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VirtualGatewayClientPolicyTlsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VirtualGatewayClientPolicyTls:
    boto3_raw_data: "type_defs.VirtualGatewayClientPolicyTlsTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def validation(self):  # pragma: no cover
        return VirtualGatewayTlsValidationContext.make_one(
            self.boto3_raw_data["validation"]
        )

    @cached_property
    def certificate(self):  # pragma: no cover
        return VirtualGatewayClientTlsCertificate.make_one(
            self.boto3_raw_data["certificate"]
        )

    enforce = field("enforce")
    ports = field("ports")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.VirtualGatewayClientPolicyTlsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VirtualGatewayClientPolicyTlsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateVirtualServiceInput:
    boto3_raw_data: "type_defs.CreateVirtualServiceInputTypeDef" = dataclasses.field()

    meshName = field("meshName")

    @cached_property
    def spec(self):  # pragma: no cover
        return VirtualServiceSpec.make_one(self.boto3_raw_data["spec"])

    virtualServiceName = field("virtualServiceName")
    clientToken = field("clientToken")
    meshOwner = field("meshOwner")

    @cached_property
    def tags(self):  # pragma: no cover
        return TagRef.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateVirtualServiceInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateVirtualServiceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateVirtualServiceInput:
    boto3_raw_data: "type_defs.UpdateVirtualServiceInputTypeDef" = dataclasses.field()

    meshName = field("meshName")

    @cached_property
    def spec(self):  # pragma: no cover
        return VirtualServiceSpec.make_one(self.boto3_raw_data["spec"])

    virtualServiceName = field("virtualServiceName")
    clientToken = field("clientToken")
    meshOwner = field("meshOwner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateVirtualServiceInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateVirtualServiceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VirtualServiceData:
    boto3_raw_data: "type_defs.VirtualServiceDataTypeDef" = dataclasses.field()

    meshName = field("meshName")

    @cached_property
    def metadata(self):  # pragma: no cover
        return ResourceMetadata.make_one(self.boto3_raw_data["metadata"])

    @cached_property
    def spec(self):  # pragma: no cover
        return VirtualServiceSpec.make_one(self.boto3_raw_data["spec"])

    @cached_property
    def status(self):  # pragma: no cover
        return VirtualServiceStatus.make_one(self.boto3_raw_data["status"])

    virtualServiceName = field("virtualServiceName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VirtualServiceDataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VirtualServiceDataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GrpcGatewayRouteOutput:
    boto3_raw_data: "type_defs.GrpcGatewayRouteOutputTypeDef" = dataclasses.field()

    @cached_property
    def action(self):  # pragma: no cover
        return GrpcGatewayRouteAction.make_one(self.boto3_raw_data["action"])

    @cached_property
    def match(self):  # pragma: no cover
        return GrpcGatewayRouteMatchOutput.make_one(self.boto3_raw_data["match"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GrpcGatewayRouteOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GrpcGatewayRouteOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GrpcGatewayRoute:
    boto3_raw_data: "type_defs.GrpcGatewayRouteTypeDef" = dataclasses.field()

    @cached_property
    def action(self):  # pragma: no cover
        return GrpcGatewayRouteAction.make_one(self.boto3_raw_data["action"])

    @cached_property
    def match(self):  # pragma: no cover
        return GrpcGatewayRouteMatch.make_one(self.boto3_raw_data["match"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GrpcGatewayRouteTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GrpcGatewayRouteTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GrpcRouteOutput:
    boto3_raw_data: "type_defs.GrpcRouteOutputTypeDef" = dataclasses.field()

    @cached_property
    def action(self):  # pragma: no cover
        return GrpcRouteActionOutput.make_one(self.boto3_raw_data["action"])

    @cached_property
    def match(self):  # pragma: no cover
        return GrpcRouteMatchOutput.make_one(self.boto3_raw_data["match"])

    @cached_property
    def retryPolicy(self):  # pragma: no cover
        return GrpcRetryPolicyOutput.make_one(self.boto3_raw_data["retryPolicy"])

    @cached_property
    def timeout(self):  # pragma: no cover
        return GrpcTimeout.make_one(self.boto3_raw_data["timeout"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GrpcRouteOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GrpcRouteOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GrpcRoute:
    boto3_raw_data: "type_defs.GrpcRouteTypeDef" = dataclasses.field()

    @cached_property
    def action(self):  # pragma: no cover
        return GrpcRouteAction.make_one(self.boto3_raw_data["action"])

    @cached_property
    def match(self):  # pragma: no cover
        return GrpcRouteMatch.make_one(self.boto3_raw_data["match"])

    @cached_property
    def retryPolicy(self):  # pragma: no cover
        return GrpcRetryPolicy.make_one(self.boto3_raw_data["retryPolicy"])

    @cached_property
    def timeout(self):  # pragma: no cover
        return GrpcTimeout.make_one(self.boto3_raw_data["timeout"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GrpcRouteTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GrpcRouteTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HttpGatewayRouteOutput:
    boto3_raw_data: "type_defs.HttpGatewayRouteOutputTypeDef" = dataclasses.field()

    @cached_property
    def action(self):  # pragma: no cover
        return HttpGatewayRouteAction.make_one(self.boto3_raw_data["action"])

    @cached_property
    def match(self):  # pragma: no cover
        return HttpGatewayRouteMatchOutput.make_one(self.boto3_raw_data["match"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HttpGatewayRouteOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HttpGatewayRouteOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HttpGatewayRoute:
    boto3_raw_data: "type_defs.HttpGatewayRouteTypeDef" = dataclasses.field()

    @cached_property
    def action(self):  # pragma: no cover
        return HttpGatewayRouteAction.make_one(self.boto3_raw_data["action"])

    @cached_property
    def match(self):  # pragma: no cover
        return HttpGatewayRouteMatch.make_one(self.boto3_raw_data["match"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HttpGatewayRouteTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HttpGatewayRouteTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HttpRouteOutput:
    boto3_raw_data: "type_defs.HttpRouteOutputTypeDef" = dataclasses.field()

    @cached_property
    def action(self):  # pragma: no cover
        return HttpRouteActionOutput.make_one(self.boto3_raw_data["action"])

    @cached_property
    def match(self):  # pragma: no cover
        return HttpRouteMatchOutput.make_one(self.boto3_raw_data["match"])

    @cached_property
    def retryPolicy(self):  # pragma: no cover
        return HttpRetryPolicyOutput.make_one(self.boto3_raw_data["retryPolicy"])

    @cached_property
    def timeout(self):  # pragma: no cover
        return HttpTimeout.make_one(self.boto3_raw_data["timeout"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HttpRouteOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.HttpRouteOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HttpRoute:
    boto3_raw_data: "type_defs.HttpRouteTypeDef" = dataclasses.field()

    @cached_property
    def action(self):  # pragma: no cover
        return HttpRouteAction.make_one(self.boto3_raw_data["action"])

    @cached_property
    def match(self):  # pragma: no cover
        return HttpRouteMatch.make_one(self.boto3_raw_data["match"])

    @cached_property
    def retryPolicy(self):  # pragma: no cover
        return HttpRetryPolicy.make_one(self.boto3_raw_data["retryPolicy"])

    @cached_property
    def timeout(self):  # pragma: no cover
        return HttpTimeout.make_one(self.boto3_raw_data["timeout"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HttpRouteTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.HttpRouteTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoggingOutput:
    boto3_raw_data: "type_defs.LoggingOutputTypeDef" = dataclasses.field()

    @cached_property
    def accessLog(self):  # pragma: no cover
        return AccessLogOutput.make_one(self.boto3_raw_data["accessLog"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LoggingOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LoggingOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VirtualGatewayLoggingOutput:
    boto3_raw_data: "type_defs.VirtualGatewayLoggingOutputTypeDef" = dataclasses.field()

    @cached_property
    def accessLog(self):  # pragma: no cover
        return VirtualGatewayAccessLogOutput.make_one(self.boto3_raw_data["accessLog"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VirtualGatewayLoggingOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VirtualGatewayLoggingOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Logging:
    boto3_raw_data: "type_defs.LoggingTypeDef" = dataclasses.field()

    @cached_property
    def accessLog(self):  # pragma: no cover
        return AccessLog.make_one(self.boto3_raw_data["accessLog"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LoggingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LoggingTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VirtualGatewayLogging:
    boto3_raw_data: "type_defs.VirtualGatewayLoggingTypeDef" = dataclasses.field()

    @cached_property
    def accessLog(self):  # pragma: no cover
        return VirtualGatewayAccessLog.make_one(self.boto3_raw_data["accessLog"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VirtualGatewayLoggingTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VirtualGatewayLoggingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateVirtualRouterOutput:
    boto3_raw_data: "type_defs.CreateVirtualRouterOutputTypeDef" = dataclasses.field()

    @cached_property
    def virtualRouter(self):  # pragma: no cover
        return VirtualRouterData.make_one(self.boto3_raw_data["virtualRouter"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateVirtualRouterOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateVirtualRouterOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteVirtualRouterOutput:
    boto3_raw_data: "type_defs.DeleteVirtualRouterOutputTypeDef" = dataclasses.field()

    @cached_property
    def virtualRouter(self):  # pragma: no cover
        return VirtualRouterData.make_one(self.boto3_raw_data["virtualRouter"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteVirtualRouterOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteVirtualRouterOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeVirtualRouterOutput:
    boto3_raw_data: "type_defs.DescribeVirtualRouterOutputTypeDef" = dataclasses.field()

    @cached_property
    def virtualRouter(self):  # pragma: no cover
        return VirtualRouterData.make_one(self.boto3_raw_data["virtualRouter"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeVirtualRouterOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeVirtualRouterOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateVirtualRouterOutput:
    boto3_raw_data: "type_defs.UpdateVirtualRouterOutputTypeDef" = dataclasses.field()

    @cached_property
    def virtualRouter(self):  # pragma: no cover
        return VirtualRouterData.make_one(self.boto3_raw_data["virtualRouter"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateVirtualRouterOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateVirtualRouterOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateVirtualRouterInput:
    boto3_raw_data: "type_defs.CreateVirtualRouterInputTypeDef" = dataclasses.field()

    meshName = field("meshName")
    spec = field("spec")
    virtualRouterName = field("virtualRouterName")
    clientToken = field("clientToken")
    meshOwner = field("meshOwner")

    @cached_property
    def tags(self):  # pragma: no cover
        return TagRef.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateVirtualRouterInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateVirtualRouterInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateVirtualRouterInput:
    boto3_raw_data: "type_defs.UpdateVirtualRouterInputTypeDef" = dataclasses.field()

    meshName = field("meshName")
    spec = field("spec")
    virtualRouterName = field("virtualRouterName")
    clientToken = field("clientToken")
    meshOwner = field("meshOwner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateVirtualRouterInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateVirtualRouterInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListenerOutput:
    boto3_raw_data: "type_defs.ListenerOutputTypeDef" = dataclasses.field()

    @cached_property
    def portMapping(self):  # pragma: no cover
        return PortMapping.make_one(self.boto3_raw_data["portMapping"])

    @cached_property
    def connectionPool(self):  # pragma: no cover
        return VirtualNodeConnectionPool.make_one(self.boto3_raw_data["connectionPool"])

    @cached_property
    def healthCheck(self):  # pragma: no cover
        return HealthCheckPolicy.make_one(self.boto3_raw_data["healthCheck"])

    @cached_property
    def outlierDetection(self):  # pragma: no cover
        return OutlierDetection.make_one(self.boto3_raw_data["outlierDetection"])

    @cached_property
    def timeout(self):  # pragma: no cover
        return ListenerTimeout.make_one(self.boto3_raw_data["timeout"])

    @cached_property
    def tls(self):  # pragma: no cover
        return ListenerTlsOutput.make_one(self.boto3_raw_data["tls"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListenerOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListenerOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Listener:
    boto3_raw_data: "type_defs.ListenerTypeDef" = dataclasses.field()

    @cached_property
    def portMapping(self):  # pragma: no cover
        return PortMapping.make_one(self.boto3_raw_data["portMapping"])

    @cached_property
    def connectionPool(self):  # pragma: no cover
        return VirtualNodeConnectionPool.make_one(self.boto3_raw_data["connectionPool"])

    @cached_property
    def healthCheck(self):  # pragma: no cover
        return HealthCheckPolicy.make_one(self.boto3_raw_data["healthCheck"])

    @cached_property
    def outlierDetection(self):  # pragma: no cover
        return OutlierDetection.make_one(self.boto3_raw_data["outlierDetection"])

    @cached_property
    def timeout(self):  # pragma: no cover
        return ListenerTimeout.make_one(self.boto3_raw_data["timeout"])

    @cached_property
    def tls(self):  # pragma: no cover
        return ListenerTls.make_one(self.boto3_raw_data["tls"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListenerTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListenerTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClientPolicyOutput:
    boto3_raw_data: "type_defs.ClientPolicyOutputTypeDef" = dataclasses.field()

    @cached_property
    def tls(self):  # pragma: no cover
        return ClientPolicyTlsOutput.make_one(self.boto3_raw_data["tls"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ClientPolicyOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClientPolicyOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClientPolicy:
    boto3_raw_data: "type_defs.ClientPolicyTypeDef" = dataclasses.field()

    @cached_property
    def tls(self):  # pragma: no cover
        return ClientPolicyTls.make_one(self.boto3_raw_data["tls"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ClientPolicyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ClientPolicyTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VirtualGatewayListenerOutput:
    boto3_raw_data: "type_defs.VirtualGatewayListenerOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def portMapping(self):  # pragma: no cover
        return VirtualGatewayPortMapping.make_one(self.boto3_raw_data["portMapping"])

    @cached_property
    def connectionPool(self):  # pragma: no cover
        return VirtualGatewayConnectionPool.make_one(
            self.boto3_raw_data["connectionPool"]
        )

    @cached_property
    def healthCheck(self):  # pragma: no cover
        return VirtualGatewayHealthCheckPolicy.make_one(
            self.boto3_raw_data["healthCheck"]
        )

    @cached_property
    def tls(self):  # pragma: no cover
        return VirtualGatewayListenerTlsOutput.make_one(self.boto3_raw_data["tls"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VirtualGatewayListenerOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VirtualGatewayListenerOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VirtualGatewayListener:
    boto3_raw_data: "type_defs.VirtualGatewayListenerTypeDef" = dataclasses.field()

    @cached_property
    def portMapping(self):  # pragma: no cover
        return VirtualGatewayPortMapping.make_one(self.boto3_raw_data["portMapping"])

    @cached_property
    def connectionPool(self):  # pragma: no cover
        return VirtualGatewayConnectionPool.make_one(
            self.boto3_raw_data["connectionPool"]
        )

    @cached_property
    def healthCheck(self):  # pragma: no cover
        return VirtualGatewayHealthCheckPolicy.make_one(
            self.boto3_raw_data["healthCheck"]
        )

    @cached_property
    def tls(self):  # pragma: no cover
        return VirtualGatewayListenerTls.make_one(self.boto3_raw_data["tls"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VirtualGatewayListenerTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VirtualGatewayListenerTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VirtualGatewayClientPolicyOutput:
    boto3_raw_data: "type_defs.VirtualGatewayClientPolicyOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def tls(self):  # pragma: no cover
        return VirtualGatewayClientPolicyTlsOutput.make_one(self.boto3_raw_data["tls"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.VirtualGatewayClientPolicyOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VirtualGatewayClientPolicyOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VirtualGatewayClientPolicy:
    boto3_raw_data: "type_defs.VirtualGatewayClientPolicyTypeDef" = dataclasses.field()

    @cached_property
    def tls(self):  # pragma: no cover
        return VirtualGatewayClientPolicyTls.make_one(self.boto3_raw_data["tls"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VirtualGatewayClientPolicyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VirtualGatewayClientPolicyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateVirtualServiceOutput:
    boto3_raw_data: "type_defs.CreateVirtualServiceOutputTypeDef" = dataclasses.field()

    @cached_property
    def virtualService(self):  # pragma: no cover
        return VirtualServiceData.make_one(self.boto3_raw_data["virtualService"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateVirtualServiceOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateVirtualServiceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteVirtualServiceOutput:
    boto3_raw_data: "type_defs.DeleteVirtualServiceOutputTypeDef" = dataclasses.field()

    @cached_property
    def virtualService(self):  # pragma: no cover
        return VirtualServiceData.make_one(self.boto3_raw_data["virtualService"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteVirtualServiceOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteVirtualServiceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeVirtualServiceOutput:
    boto3_raw_data: "type_defs.DescribeVirtualServiceOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def virtualService(self):  # pragma: no cover
        return VirtualServiceData.make_one(self.boto3_raw_data["virtualService"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeVirtualServiceOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeVirtualServiceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateVirtualServiceOutput:
    boto3_raw_data: "type_defs.UpdateVirtualServiceOutputTypeDef" = dataclasses.field()

    @cached_property
    def virtualService(self):  # pragma: no cover
        return VirtualServiceData.make_one(self.boto3_raw_data["virtualService"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateVirtualServiceOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateVirtualServiceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GatewayRouteSpecOutput:
    boto3_raw_data: "type_defs.GatewayRouteSpecOutputTypeDef" = dataclasses.field()

    @cached_property
    def grpcRoute(self):  # pragma: no cover
        return GrpcGatewayRouteOutput.make_one(self.boto3_raw_data["grpcRoute"])

    @cached_property
    def http2Route(self):  # pragma: no cover
        return HttpGatewayRouteOutput.make_one(self.boto3_raw_data["http2Route"])

    @cached_property
    def httpRoute(self):  # pragma: no cover
        return HttpGatewayRouteOutput.make_one(self.boto3_raw_data["httpRoute"])

    priority = field("priority")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GatewayRouteSpecOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GatewayRouteSpecOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GatewayRouteSpec:
    boto3_raw_data: "type_defs.GatewayRouteSpecTypeDef" = dataclasses.field()

    @cached_property
    def grpcRoute(self):  # pragma: no cover
        return GrpcGatewayRoute.make_one(self.boto3_raw_data["grpcRoute"])

    @cached_property
    def http2Route(self):  # pragma: no cover
        return HttpGatewayRoute.make_one(self.boto3_raw_data["http2Route"])

    @cached_property
    def httpRoute(self):  # pragma: no cover
        return HttpGatewayRoute.make_one(self.boto3_raw_data["httpRoute"])

    priority = field("priority")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GatewayRouteSpecTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GatewayRouteSpecTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteSpecOutput:
    boto3_raw_data: "type_defs.RouteSpecOutputTypeDef" = dataclasses.field()

    @cached_property
    def grpcRoute(self):  # pragma: no cover
        return GrpcRouteOutput.make_one(self.boto3_raw_data["grpcRoute"])

    @cached_property
    def http2Route(self):  # pragma: no cover
        return HttpRouteOutput.make_one(self.boto3_raw_data["http2Route"])

    @cached_property
    def httpRoute(self):  # pragma: no cover
        return HttpRouteOutput.make_one(self.boto3_raw_data["httpRoute"])

    priority = field("priority")

    @cached_property
    def tcpRoute(self):  # pragma: no cover
        return TcpRouteOutput.make_one(self.boto3_raw_data["tcpRoute"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RouteSpecOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RouteSpecOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteSpec:
    boto3_raw_data: "type_defs.RouteSpecTypeDef" = dataclasses.field()

    @cached_property
    def grpcRoute(self):  # pragma: no cover
        return GrpcRoute.make_one(self.boto3_raw_data["grpcRoute"])

    @cached_property
    def http2Route(self):  # pragma: no cover
        return HttpRoute.make_one(self.boto3_raw_data["http2Route"])

    @cached_property
    def httpRoute(self):  # pragma: no cover
        return HttpRoute.make_one(self.boto3_raw_data["httpRoute"])

    priority = field("priority")

    @cached_property
    def tcpRoute(self):  # pragma: no cover
        return TcpRoute.make_one(self.boto3_raw_data["tcpRoute"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RouteSpecTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RouteSpecTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BackendDefaultsOutput:
    boto3_raw_data: "type_defs.BackendDefaultsOutputTypeDef" = dataclasses.field()

    @cached_property
    def clientPolicy(self):  # pragma: no cover
        return ClientPolicyOutput.make_one(self.boto3_raw_data["clientPolicy"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BackendDefaultsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BackendDefaultsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VirtualServiceBackendOutput:
    boto3_raw_data: "type_defs.VirtualServiceBackendOutputTypeDef" = dataclasses.field()

    virtualServiceName = field("virtualServiceName")

    @cached_property
    def clientPolicy(self):  # pragma: no cover
        return ClientPolicyOutput.make_one(self.boto3_raw_data["clientPolicy"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VirtualServiceBackendOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VirtualServiceBackendOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BackendDefaults:
    boto3_raw_data: "type_defs.BackendDefaultsTypeDef" = dataclasses.field()

    @cached_property
    def clientPolicy(self):  # pragma: no cover
        return ClientPolicy.make_one(self.boto3_raw_data["clientPolicy"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BackendDefaultsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BackendDefaultsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VirtualServiceBackend:
    boto3_raw_data: "type_defs.VirtualServiceBackendTypeDef" = dataclasses.field()

    virtualServiceName = field("virtualServiceName")

    @cached_property
    def clientPolicy(self):  # pragma: no cover
        return ClientPolicy.make_one(self.boto3_raw_data["clientPolicy"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VirtualServiceBackendTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VirtualServiceBackendTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VirtualGatewayBackendDefaultsOutput:
    boto3_raw_data: "type_defs.VirtualGatewayBackendDefaultsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def clientPolicy(self):  # pragma: no cover
        return VirtualGatewayClientPolicyOutput.make_one(
            self.boto3_raw_data["clientPolicy"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.VirtualGatewayBackendDefaultsOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VirtualGatewayBackendDefaultsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VirtualGatewayBackendDefaults:
    boto3_raw_data: "type_defs.VirtualGatewayBackendDefaultsTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def clientPolicy(self):  # pragma: no cover
        return VirtualGatewayClientPolicy.make_one(self.boto3_raw_data["clientPolicy"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.VirtualGatewayBackendDefaultsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VirtualGatewayBackendDefaultsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GatewayRouteData:
    boto3_raw_data: "type_defs.GatewayRouteDataTypeDef" = dataclasses.field()

    gatewayRouteName = field("gatewayRouteName")
    meshName = field("meshName")

    @cached_property
    def metadata(self):  # pragma: no cover
        return ResourceMetadata.make_one(self.boto3_raw_data["metadata"])

    @cached_property
    def spec(self):  # pragma: no cover
        return GatewayRouteSpecOutput.make_one(self.boto3_raw_data["spec"])

    @cached_property
    def status(self):  # pragma: no cover
        return GatewayRouteStatus.make_one(self.boto3_raw_data["status"])

    virtualGatewayName = field("virtualGatewayName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GatewayRouteDataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GatewayRouteDataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteData:
    boto3_raw_data: "type_defs.RouteDataTypeDef" = dataclasses.field()

    meshName = field("meshName")

    @cached_property
    def metadata(self):  # pragma: no cover
        return ResourceMetadata.make_one(self.boto3_raw_data["metadata"])

    routeName = field("routeName")

    @cached_property
    def spec(self):  # pragma: no cover
        return RouteSpecOutput.make_one(self.boto3_raw_data["spec"])

    @cached_property
    def status(self):  # pragma: no cover
        return RouteStatus.make_one(self.boto3_raw_data["status"])

    virtualRouterName = field("virtualRouterName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RouteDataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RouteDataTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BackendOutput:
    boto3_raw_data: "type_defs.BackendOutputTypeDef" = dataclasses.field()

    @cached_property
    def virtualService(self):  # pragma: no cover
        return VirtualServiceBackendOutput.make_one(
            self.boto3_raw_data["virtualService"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BackendOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BackendOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Backend:
    boto3_raw_data: "type_defs.BackendTypeDef" = dataclasses.field()

    @cached_property
    def virtualService(self):  # pragma: no cover
        return VirtualServiceBackend.make_one(self.boto3_raw_data["virtualService"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BackendTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BackendTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VirtualGatewaySpecOutput:
    boto3_raw_data: "type_defs.VirtualGatewaySpecOutputTypeDef" = dataclasses.field()

    @cached_property
    def listeners(self):  # pragma: no cover
        return VirtualGatewayListenerOutput.make_many(self.boto3_raw_data["listeners"])

    @cached_property
    def backendDefaults(self):  # pragma: no cover
        return VirtualGatewayBackendDefaultsOutput.make_one(
            self.boto3_raw_data["backendDefaults"]
        )

    @cached_property
    def logging(self):  # pragma: no cover
        return VirtualGatewayLoggingOutput.make_one(self.boto3_raw_data["logging"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VirtualGatewaySpecOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VirtualGatewaySpecOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VirtualGatewaySpec:
    boto3_raw_data: "type_defs.VirtualGatewaySpecTypeDef" = dataclasses.field()

    @cached_property
    def listeners(self):  # pragma: no cover
        return VirtualGatewayListener.make_many(self.boto3_raw_data["listeners"])

    @cached_property
    def backendDefaults(self):  # pragma: no cover
        return VirtualGatewayBackendDefaults.make_one(
            self.boto3_raw_data["backendDefaults"]
        )

    @cached_property
    def logging(self):  # pragma: no cover
        return VirtualGatewayLogging.make_one(self.boto3_raw_data["logging"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VirtualGatewaySpecTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VirtualGatewaySpecTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateGatewayRouteOutput:
    boto3_raw_data: "type_defs.CreateGatewayRouteOutputTypeDef" = dataclasses.field()

    @cached_property
    def gatewayRoute(self):  # pragma: no cover
        return GatewayRouteData.make_one(self.boto3_raw_data["gatewayRoute"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateGatewayRouteOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateGatewayRouteOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteGatewayRouteOutput:
    boto3_raw_data: "type_defs.DeleteGatewayRouteOutputTypeDef" = dataclasses.field()

    @cached_property
    def gatewayRoute(self):  # pragma: no cover
        return GatewayRouteData.make_one(self.boto3_raw_data["gatewayRoute"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteGatewayRouteOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteGatewayRouteOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeGatewayRouteOutput:
    boto3_raw_data: "type_defs.DescribeGatewayRouteOutputTypeDef" = dataclasses.field()

    @cached_property
    def gatewayRoute(self):  # pragma: no cover
        return GatewayRouteData.make_one(self.boto3_raw_data["gatewayRoute"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeGatewayRouteOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeGatewayRouteOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateGatewayRouteOutput:
    boto3_raw_data: "type_defs.UpdateGatewayRouteOutputTypeDef" = dataclasses.field()

    @cached_property
    def gatewayRoute(self):  # pragma: no cover
        return GatewayRouteData.make_one(self.boto3_raw_data["gatewayRoute"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateGatewayRouteOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateGatewayRouteOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateGatewayRouteInput:
    boto3_raw_data: "type_defs.CreateGatewayRouteInputTypeDef" = dataclasses.field()

    gatewayRouteName = field("gatewayRouteName")
    meshName = field("meshName")
    spec = field("spec")
    virtualGatewayName = field("virtualGatewayName")
    clientToken = field("clientToken")
    meshOwner = field("meshOwner")

    @cached_property
    def tags(self):  # pragma: no cover
        return TagRef.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateGatewayRouteInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateGatewayRouteInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateGatewayRouteInput:
    boto3_raw_data: "type_defs.UpdateGatewayRouteInputTypeDef" = dataclasses.field()

    gatewayRouteName = field("gatewayRouteName")
    meshName = field("meshName")
    spec = field("spec")
    virtualGatewayName = field("virtualGatewayName")
    clientToken = field("clientToken")
    meshOwner = field("meshOwner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateGatewayRouteInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateGatewayRouteInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRouteOutput:
    boto3_raw_data: "type_defs.CreateRouteOutputTypeDef" = dataclasses.field()

    @cached_property
    def route(self):  # pragma: no cover
        return RouteData.make_one(self.boto3_raw_data["route"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateRouteOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRouteOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRouteOutput:
    boto3_raw_data: "type_defs.DeleteRouteOutputTypeDef" = dataclasses.field()

    @cached_property
    def route(self):  # pragma: no cover
        return RouteData.make_one(self.boto3_raw_data["route"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteRouteOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRouteOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRouteOutput:
    boto3_raw_data: "type_defs.DescribeRouteOutputTypeDef" = dataclasses.field()

    @cached_property
    def route(self):  # pragma: no cover
        return RouteData.make_one(self.boto3_raw_data["route"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeRouteOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRouteOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRouteOutput:
    boto3_raw_data: "type_defs.UpdateRouteOutputTypeDef" = dataclasses.field()

    @cached_property
    def route(self):  # pragma: no cover
        return RouteData.make_one(self.boto3_raw_data["route"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateRouteOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRouteOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRouteInput:
    boto3_raw_data: "type_defs.CreateRouteInputTypeDef" = dataclasses.field()

    meshName = field("meshName")
    routeName = field("routeName")
    spec = field("spec")
    virtualRouterName = field("virtualRouterName")
    clientToken = field("clientToken")
    meshOwner = field("meshOwner")

    @cached_property
    def tags(self):  # pragma: no cover
        return TagRef.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateRouteInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRouteInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRouteInput:
    boto3_raw_data: "type_defs.UpdateRouteInputTypeDef" = dataclasses.field()

    meshName = field("meshName")
    routeName = field("routeName")
    spec = field("spec")
    virtualRouterName = field("virtualRouterName")
    clientToken = field("clientToken")
    meshOwner = field("meshOwner")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateRouteInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRouteInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VirtualNodeSpecOutput:
    boto3_raw_data: "type_defs.VirtualNodeSpecOutputTypeDef" = dataclasses.field()

    @cached_property
    def backendDefaults(self):  # pragma: no cover
        return BackendDefaultsOutput.make_one(self.boto3_raw_data["backendDefaults"])

    @cached_property
    def backends(self):  # pragma: no cover
        return BackendOutput.make_many(self.boto3_raw_data["backends"])

    @cached_property
    def listeners(self):  # pragma: no cover
        return ListenerOutput.make_many(self.boto3_raw_data["listeners"])

    @cached_property
    def logging(self):  # pragma: no cover
        return LoggingOutput.make_one(self.boto3_raw_data["logging"])

    @cached_property
    def serviceDiscovery(self):  # pragma: no cover
        return ServiceDiscoveryOutput.make_one(self.boto3_raw_data["serviceDiscovery"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VirtualNodeSpecOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VirtualNodeSpecOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VirtualNodeSpec:
    boto3_raw_data: "type_defs.VirtualNodeSpecTypeDef" = dataclasses.field()

    @cached_property
    def backendDefaults(self):  # pragma: no cover
        return BackendDefaults.make_one(self.boto3_raw_data["backendDefaults"])

    @cached_property
    def backends(self):  # pragma: no cover
        return Backend.make_many(self.boto3_raw_data["backends"])

    @cached_property
    def listeners(self):  # pragma: no cover
        return Listener.make_many(self.boto3_raw_data["listeners"])

    @cached_property
    def logging(self):  # pragma: no cover
        return Logging.make_one(self.boto3_raw_data["logging"])

    @cached_property
    def serviceDiscovery(self):  # pragma: no cover
        return ServiceDiscovery.make_one(self.boto3_raw_data["serviceDiscovery"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VirtualNodeSpecTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VirtualNodeSpecTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VirtualGatewayData:
    boto3_raw_data: "type_defs.VirtualGatewayDataTypeDef" = dataclasses.field()

    meshName = field("meshName")

    @cached_property
    def metadata(self):  # pragma: no cover
        return ResourceMetadata.make_one(self.boto3_raw_data["metadata"])

    @cached_property
    def spec(self):  # pragma: no cover
        return VirtualGatewaySpecOutput.make_one(self.boto3_raw_data["spec"])

    @cached_property
    def status(self):  # pragma: no cover
        return VirtualGatewayStatus.make_one(self.boto3_raw_data["status"])

    virtualGatewayName = field("virtualGatewayName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VirtualGatewayDataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VirtualGatewayDataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VirtualNodeData:
    boto3_raw_data: "type_defs.VirtualNodeDataTypeDef" = dataclasses.field()

    meshName = field("meshName")

    @cached_property
    def metadata(self):  # pragma: no cover
        return ResourceMetadata.make_one(self.boto3_raw_data["metadata"])

    @cached_property
    def spec(self):  # pragma: no cover
        return VirtualNodeSpecOutput.make_one(self.boto3_raw_data["spec"])

    @cached_property
    def status(self):  # pragma: no cover
        return VirtualNodeStatus.make_one(self.boto3_raw_data["status"])

    virtualNodeName = field("virtualNodeName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VirtualNodeDataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VirtualNodeDataTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateVirtualGatewayOutput:
    boto3_raw_data: "type_defs.CreateVirtualGatewayOutputTypeDef" = dataclasses.field()

    @cached_property
    def virtualGateway(self):  # pragma: no cover
        return VirtualGatewayData.make_one(self.boto3_raw_data["virtualGateway"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateVirtualGatewayOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateVirtualGatewayOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteVirtualGatewayOutput:
    boto3_raw_data: "type_defs.DeleteVirtualGatewayOutputTypeDef" = dataclasses.field()

    @cached_property
    def virtualGateway(self):  # pragma: no cover
        return VirtualGatewayData.make_one(self.boto3_raw_data["virtualGateway"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteVirtualGatewayOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteVirtualGatewayOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeVirtualGatewayOutput:
    boto3_raw_data: "type_defs.DescribeVirtualGatewayOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def virtualGateway(self):  # pragma: no cover
        return VirtualGatewayData.make_one(self.boto3_raw_data["virtualGateway"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeVirtualGatewayOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeVirtualGatewayOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateVirtualGatewayOutput:
    boto3_raw_data: "type_defs.UpdateVirtualGatewayOutputTypeDef" = dataclasses.field()

    @cached_property
    def virtualGateway(self):  # pragma: no cover
        return VirtualGatewayData.make_one(self.boto3_raw_data["virtualGateway"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateVirtualGatewayOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateVirtualGatewayOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateVirtualGatewayInput:
    boto3_raw_data: "type_defs.CreateVirtualGatewayInputTypeDef" = dataclasses.field()

    meshName = field("meshName")
    spec = field("spec")
    virtualGatewayName = field("virtualGatewayName")
    clientToken = field("clientToken")
    meshOwner = field("meshOwner")

    @cached_property
    def tags(self):  # pragma: no cover
        return TagRef.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateVirtualGatewayInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateVirtualGatewayInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateVirtualGatewayInput:
    boto3_raw_data: "type_defs.UpdateVirtualGatewayInputTypeDef" = dataclasses.field()

    meshName = field("meshName")
    spec = field("spec")
    virtualGatewayName = field("virtualGatewayName")
    clientToken = field("clientToken")
    meshOwner = field("meshOwner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateVirtualGatewayInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateVirtualGatewayInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateVirtualNodeOutput:
    boto3_raw_data: "type_defs.CreateVirtualNodeOutputTypeDef" = dataclasses.field()

    @cached_property
    def virtualNode(self):  # pragma: no cover
        return VirtualNodeData.make_one(self.boto3_raw_data["virtualNode"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateVirtualNodeOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateVirtualNodeOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteVirtualNodeOutput:
    boto3_raw_data: "type_defs.DeleteVirtualNodeOutputTypeDef" = dataclasses.field()

    @cached_property
    def virtualNode(self):  # pragma: no cover
        return VirtualNodeData.make_one(self.boto3_raw_data["virtualNode"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteVirtualNodeOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteVirtualNodeOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeVirtualNodeOutput:
    boto3_raw_data: "type_defs.DescribeVirtualNodeOutputTypeDef" = dataclasses.field()

    @cached_property
    def virtualNode(self):  # pragma: no cover
        return VirtualNodeData.make_one(self.boto3_raw_data["virtualNode"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeVirtualNodeOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeVirtualNodeOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateVirtualNodeOutput:
    boto3_raw_data: "type_defs.UpdateVirtualNodeOutputTypeDef" = dataclasses.field()

    @cached_property
    def virtualNode(self):  # pragma: no cover
        return VirtualNodeData.make_one(self.boto3_raw_data["virtualNode"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateVirtualNodeOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateVirtualNodeOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateVirtualNodeInput:
    boto3_raw_data: "type_defs.CreateVirtualNodeInputTypeDef" = dataclasses.field()

    meshName = field("meshName")
    spec = field("spec")
    virtualNodeName = field("virtualNodeName")
    clientToken = field("clientToken")
    meshOwner = field("meshOwner")

    @cached_property
    def tags(self):  # pragma: no cover
        return TagRef.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateVirtualNodeInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateVirtualNodeInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateVirtualNodeInput:
    boto3_raw_data: "type_defs.UpdateVirtualNodeInputTypeDef" = dataclasses.field()

    meshName = field("meshName")
    spec = field("spec")
    virtualNodeName = field("virtualNodeName")
    clientToken = field("clientToken")
    meshOwner = field("meshOwner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateVirtualNodeInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateVirtualNodeInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
