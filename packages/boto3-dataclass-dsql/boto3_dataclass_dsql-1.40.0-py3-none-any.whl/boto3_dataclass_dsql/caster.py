# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_dsql import type_defs as bs_td


class DSQLCaster:

    def create_cluster(
        self,
        res: "bs_td.CreateClusterOutputTypeDef",
    ) -> "dc_td.CreateClusterOutput":
        return dc_td.CreateClusterOutput.make_one(res)

    def delete_cluster(
        self,
        res: "bs_td.DeleteClusterOutputTypeDef",
    ) -> "dc_td.DeleteClusterOutput":
        return dc_td.DeleteClusterOutput.make_one(res)

    def get_cluster(
        self,
        res: "bs_td.GetClusterOutputTypeDef",
    ) -> "dc_td.GetClusterOutput":
        return dc_td.GetClusterOutput.make_one(res)

    def get_vpc_endpoint_service_name(
        self,
        res: "bs_td.GetVpcEndpointServiceNameOutputTypeDef",
    ) -> "dc_td.GetVpcEndpointServiceNameOutput":
        return dc_td.GetVpcEndpointServiceNameOutput.make_one(res)

    def list_clusters(
        self,
        res: "bs_td.ListClustersOutputTypeDef",
    ) -> "dc_td.ListClustersOutput":
        return dc_td.ListClustersOutput.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceOutputTypeDef",
    ) -> "dc_td.ListTagsForResourceOutput":
        return dc_td.ListTagsForResourceOutput.make_one(res)

    def tag_resource(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def untag_resource(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_cluster(
        self,
        res: "bs_td.UpdateClusterOutputTypeDef",
    ) -> "dc_td.UpdateClusterOutput":
        return dc_td.UpdateClusterOutput.make_one(res)


dsql_caster = DSQLCaster()
