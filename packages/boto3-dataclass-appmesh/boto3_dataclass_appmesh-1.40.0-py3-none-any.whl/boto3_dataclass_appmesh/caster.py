# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_appmesh import type_defs as bs_td


class APPMESHCaster:

    def create_gateway_route(
        self,
        res: "bs_td.CreateGatewayRouteOutputTypeDef",
    ) -> "dc_td.CreateGatewayRouteOutput":
        return dc_td.CreateGatewayRouteOutput.make_one(res)

    def create_mesh(
        self,
        res: "bs_td.CreateMeshOutputTypeDef",
    ) -> "dc_td.CreateMeshOutput":
        return dc_td.CreateMeshOutput.make_one(res)

    def create_route(
        self,
        res: "bs_td.CreateRouteOutputTypeDef",
    ) -> "dc_td.CreateRouteOutput":
        return dc_td.CreateRouteOutput.make_one(res)

    def create_virtual_gateway(
        self,
        res: "bs_td.CreateVirtualGatewayOutputTypeDef",
    ) -> "dc_td.CreateVirtualGatewayOutput":
        return dc_td.CreateVirtualGatewayOutput.make_one(res)

    def create_virtual_node(
        self,
        res: "bs_td.CreateVirtualNodeOutputTypeDef",
    ) -> "dc_td.CreateVirtualNodeOutput":
        return dc_td.CreateVirtualNodeOutput.make_one(res)

    def create_virtual_router(
        self,
        res: "bs_td.CreateVirtualRouterOutputTypeDef",
    ) -> "dc_td.CreateVirtualRouterOutput":
        return dc_td.CreateVirtualRouterOutput.make_one(res)

    def create_virtual_service(
        self,
        res: "bs_td.CreateVirtualServiceOutputTypeDef",
    ) -> "dc_td.CreateVirtualServiceOutput":
        return dc_td.CreateVirtualServiceOutput.make_one(res)

    def delete_gateway_route(
        self,
        res: "bs_td.DeleteGatewayRouteOutputTypeDef",
    ) -> "dc_td.DeleteGatewayRouteOutput":
        return dc_td.DeleteGatewayRouteOutput.make_one(res)

    def delete_mesh(
        self,
        res: "bs_td.DeleteMeshOutputTypeDef",
    ) -> "dc_td.DeleteMeshOutput":
        return dc_td.DeleteMeshOutput.make_one(res)

    def delete_route(
        self,
        res: "bs_td.DeleteRouteOutputTypeDef",
    ) -> "dc_td.DeleteRouteOutput":
        return dc_td.DeleteRouteOutput.make_one(res)

    def delete_virtual_gateway(
        self,
        res: "bs_td.DeleteVirtualGatewayOutputTypeDef",
    ) -> "dc_td.DeleteVirtualGatewayOutput":
        return dc_td.DeleteVirtualGatewayOutput.make_one(res)

    def delete_virtual_node(
        self,
        res: "bs_td.DeleteVirtualNodeOutputTypeDef",
    ) -> "dc_td.DeleteVirtualNodeOutput":
        return dc_td.DeleteVirtualNodeOutput.make_one(res)

    def delete_virtual_router(
        self,
        res: "bs_td.DeleteVirtualRouterOutputTypeDef",
    ) -> "dc_td.DeleteVirtualRouterOutput":
        return dc_td.DeleteVirtualRouterOutput.make_one(res)

    def delete_virtual_service(
        self,
        res: "bs_td.DeleteVirtualServiceOutputTypeDef",
    ) -> "dc_td.DeleteVirtualServiceOutput":
        return dc_td.DeleteVirtualServiceOutput.make_one(res)

    def describe_gateway_route(
        self,
        res: "bs_td.DescribeGatewayRouteOutputTypeDef",
    ) -> "dc_td.DescribeGatewayRouteOutput":
        return dc_td.DescribeGatewayRouteOutput.make_one(res)

    def describe_mesh(
        self,
        res: "bs_td.DescribeMeshOutputTypeDef",
    ) -> "dc_td.DescribeMeshOutput":
        return dc_td.DescribeMeshOutput.make_one(res)

    def describe_route(
        self,
        res: "bs_td.DescribeRouteOutputTypeDef",
    ) -> "dc_td.DescribeRouteOutput":
        return dc_td.DescribeRouteOutput.make_one(res)

    def describe_virtual_gateway(
        self,
        res: "bs_td.DescribeVirtualGatewayOutputTypeDef",
    ) -> "dc_td.DescribeVirtualGatewayOutput":
        return dc_td.DescribeVirtualGatewayOutput.make_one(res)

    def describe_virtual_node(
        self,
        res: "bs_td.DescribeVirtualNodeOutputTypeDef",
    ) -> "dc_td.DescribeVirtualNodeOutput":
        return dc_td.DescribeVirtualNodeOutput.make_one(res)

    def describe_virtual_router(
        self,
        res: "bs_td.DescribeVirtualRouterOutputTypeDef",
    ) -> "dc_td.DescribeVirtualRouterOutput":
        return dc_td.DescribeVirtualRouterOutput.make_one(res)

    def describe_virtual_service(
        self,
        res: "bs_td.DescribeVirtualServiceOutputTypeDef",
    ) -> "dc_td.DescribeVirtualServiceOutput":
        return dc_td.DescribeVirtualServiceOutput.make_one(res)

    def list_gateway_routes(
        self,
        res: "bs_td.ListGatewayRoutesOutputTypeDef",
    ) -> "dc_td.ListGatewayRoutesOutput":
        return dc_td.ListGatewayRoutesOutput.make_one(res)

    def list_meshes(
        self,
        res: "bs_td.ListMeshesOutputTypeDef",
    ) -> "dc_td.ListMeshesOutput":
        return dc_td.ListMeshesOutput.make_one(res)

    def list_routes(
        self,
        res: "bs_td.ListRoutesOutputTypeDef",
    ) -> "dc_td.ListRoutesOutput":
        return dc_td.ListRoutesOutput.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceOutputTypeDef",
    ) -> "dc_td.ListTagsForResourceOutput":
        return dc_td.ListTagsForResourceOutput.make_one(res)

    def list_virtual_gateways(
        self,
        res: "bs_td.ListVirtualGatewaysOutputTypeDef",
    ) -> "dc_td.ListVirtualGatewaysOutput":
        return dc_td.ListVirtualGatewaysOutput.make_one(res)

    def list_virtual_nodes(
        self,
        res: "bs_td.ListVirtualNodesOutputTypeDef",
    ) -> "dc_td.ListVirtualNodesOutput":
        return dc_td.ListVirtualNodesOutput.make_one(res)

    def list_virtual_routers(
        self,
        res: "bs_td.ListVirtualRoutersOutputTypeDef",
    ) -> "dc_td.ListVirtualRoutersOutput":
        return dc_td.ListVirtualRoutersOutput.make_one(res)

    def list_virtual_services(
        self,
        res: "bs_td.ListVirtualServicesOutputTypeDef",
    ) -> "dc_td.ListVirtualServicesOutput":
        return dc_td.ListVirtualServicesOutput.make_one(res)

    def update_gateway_route(
        self,
        res: "bs_td.UpdateGatewayRouteOutputTypeDef",
    ) -> "dc_td.UpdateGatewayRouteOutput":
        return dc_td.UpdateGatewayRouteOutput.make_one(res)

    def update_mesh(
        self,
        res: "bs_td.UpdateMeshOutputTypeDef",
    ) -> "dc_td.UpdateMeshOutput":
        return dc_td.UpdateMeshOutput.make_one(res)

    def update_route(
        self,
        res: "bs_td.UpdateRouteOutputTypeDef",
    ) -> "dc_td.UpdateRouteOutput":
        return dc_td.UpdateRouteOutput.make_one(res)

    def update_virtual_gateway(
        self,
        res: "bs_td.UpdateVirtualGatewayOutputTypeDef",
    ) -> "dc_td.UpdateVirtualGatewayOutput":
        return dc_td.UpdateVirtualGatewayOutput.make_one(res)

    def update_virtual_node(
        self,
        res: "bs_td.UpdateVirtualNodeOutputTypeDef",
    ) -> "dc_td.UpdateVirtualNodeOutput":
        return dc_td.UpdateVirtualNodeOutput.make_one(res)

    def update_virtual_router(
        self,
        res: "bs_td.UpdateVirtualRouterOutputTypeDef",
    ) -> "dc_td.UpdateVirtualRouterOutput":
        return dc_td.UpdateVirtualRouterOutput.make_one(res)

    def update_virtual_service(
        self,
        res: "bs_td.UpdateVirtualServiceOutputTypeDef",
    ) -> "dc_td.UpdateVirtualServiceOutput":
        return dc_td.UpdateVirtualServiceOutput.make_one(res)


appmesh_caster = APPMESHCaster()
