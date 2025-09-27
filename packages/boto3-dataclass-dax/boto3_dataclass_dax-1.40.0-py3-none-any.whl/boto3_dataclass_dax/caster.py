# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_dax import type_defs as bs_td


class DAXCaster:

    def create_cluster(
        self,
        res: "bs_td.CreateClusterResponseTypeDef",
    ) -> "dc_td.CreateClusterResponse":
        return dc_td.CreateClusterResponse.make_one(res)

    def create_parameter_group(
        self,
        res: "bs_td.CreateParameterGroupResponseTypeDef",
    ) -> "dc_td.CreateParameterGroupResponse":
        return dc_td.CreateParameterGroupResponse.make_one(res)

    def create_subnet_group(
        self,
        res: "bs_td.CreateSubnetGroupResponseTypeDef",
    ) -> "dc_td.CreateSubnetGroupResponse":
        return dc_td.CreateSubnetGroupResponse.make_one(res)

    def decrease_replication_factor(
        self,
        res: "bs_td.DecreaseReplicationFactorResponseTypeDef",
    ) -> "dc_td.DecreaseReplicationFactorResponse":
        return dc_td.DecreaseReplicationFactorResponse.make_one(res)

    def delete_cluster(
        self,
        res: "bs_td.DeleteClusterResponseTypeDef",
    ) -> "dc_td.DeleteClusterResponse":
        return dc_td.DeleteClusterResponse.make_one(res)

    def delete_parameter_group(
        self,
        res: "bs_td.DeleteParameterGroupResponseTypeDef",
    ) -> "dc_td.DeleteParameterGroupResponse":
        return dc_td.DeleteParameterGroupResponse.make_one(res)

    def delete_subnet_group(
        self,
        res: "bs_td.DeleteSubnetGroupResponseTypeDef",
    ) -> "dc_td.DeleteSubnetGroupResponse":
        return dc_td.DeleteSubnetGroupResponse.make_one(res)

    def describe_clusters(
        self,
        res: "bs_td.DescribeClustersResponseTypeDef",
    ) -> "dc_td.DescribeClustersResponse":
        return dc_td.DescribeClustersResponse.make_one(res)

    def describe_default_parameters(
        self,
        res: "bs_td.DescribeDefaultParametersResponseTypeDef",
    ) -> "dc_td.DescribeDefaultParametersResponse":
        return dc_td.DescribeDefaultParametersResponse.make_one(res)

    def describe_events(
        self,
        res: "bs_td.DescribeEventsResponseTypeDef",
    ) -> "dc_td.DescribeEventsResponse":
        return dc_td.DescribeEventsResponse.make_one(res)

    def describe_parameter_groups(
        self,
        res: "bs_td.DescribeParameterGroupsResponseTypeDef",
    ) -> "dc_td.DescribeParameterGroupsResponse":
        return dc_td.DescribeParameterGroupsResponse.make_one(res)

    def describe_parameters(
        self,
        res: "bs_td.DescribeParametersResponseTypeDef",
    ) -> "dc_td.DescribeParametersResponse":
        return dc_td.DescribeParametersResponse.make_one(res)

    def describe_subnet_groups(
        self,
        res: "bs_td.DescribeSubnetGroupsResponseTypeDef",
    ) -> "dc_td.DescribeSubnetGroupsResponse":
        return dc_td.DescribeSubnetGroupsResponse.make_one(res)

    def increase_replication_factor(
        self,
        res: "bs_td.IncreaseReplicationFactorResponseTypeDef",
    ) -> "dc_td.IncreaseReplicationFactorResponse":
        return dc_td.IncreaseReplicationFactorResponse.make_one(res)

    def list_tags(
        self,
        res: "bs_td.ListTagsResponseTypeDef",
    ) -> "dc_td.ListTagsResponse":
        return dc_td.ListTagsResponse.make_one(res)

    def reboot_node(
        self,
        res: "bs_td.RebootNodeResponseTypeDef",
    ) -> "dc_td.RebootNodeResponse":
        return dc_td.RebootNodeResponse.make_one(res)

    def tag_resource(
        self,
        res: "bs_td.TagResourceResponseTypeDef",
    ) -> "dc_td.TagResourceResponse":
        return dc_td.TagResourceResponse.make_one(res)

    def untag_resource(
        self,
        res: "bs_td.UntagResourceResponseTypeDef",
    ) -> "dc_td.UntagResourceResponse":
        return dc_td.UntagResourceResponse.make_one(res)

    def update_cluster(
        self,
        res: "bs_td.UpdateClusterResponseTypeDef",
    ) -> "dc_td.UpdateClusterResponse":
        return dc_td.UpdateClusterResponse.make_one(res)

    def update_parameter_group(
        self,
        res: "bs_td.UpdateParameterGroupResponseTypeDef",
    ) -> "dc_td.UpdateParameterGroupResponse":
        return dc_td.UpdateParameterGroupResponse.make_one(res)

    def update_subnet_group(
        self,
        res: "bs_td.UpdateSubnetGroupResponseTypeDef",
    ) -> "dc_td.UpdateSubnetGroupResponse":
        return dc_td.UpdateSubnetGroupResponse.make_one(res)


dax_caster = DAXCaster()
