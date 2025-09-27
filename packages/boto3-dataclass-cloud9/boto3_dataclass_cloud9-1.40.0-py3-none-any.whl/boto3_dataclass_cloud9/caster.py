# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_cloud9 import type_defs as bs_td


class CLOUD9Caster:

    def create_environment_ec2(
        self,
        res: "bs_td.CreateEnvironmentEC2ResultTypeDef",
    ) -> "dc_td.CreateEnvironmentEC2Result":
        return dc_td.CreateEnvironmentEC2Result.make_one(res)

    def create_environment_membership(
        self,
        res: "bs_td.CreateEnvironmentMembershipResultTypeDef",
    ) -> "dc_td.CreateEnvironmentMembershipResult":
        return dc_td.CreateEnvironmentMembershipResult.make_one(res)

    def describe_environment_memberships(
        self,
        res: "bs_td.DescribeEnvironmentMembershipsResultTypeDef",
    ) -> "dc_td.DescribeEnvironmentMembershipsResult":
        return dc_td.DescribeEnvironmentMembershipsResult.make_one(res)

    def describe_environment_status(
        self,
        res: "bs_td.DescribeEnvironmentStatusResultTypeDef",
    ) -> "dc_td.DescribeEnvironmentStatusResult":
        return dc_td.DescribeEnvironmentStatusResult.make_one(res)

    def describe_environments(
        self,
        res: "bs_td.DescribeEnvironmentsResultTypeDef",
    ) -> "dc_td.DescribeEnvironmentsResult":
        return dc_td.DescribeEnvironmentsResult.make_one(res)

    def list_environments(
        self,
        res: "bs_td.ListEnvironmentsResultTypeDef",
    ) -> "dc_td.ListEnvironmentsResult":
        return dc_td.ListEnvironmentsResult.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def update_environment_membership(
        self,
        res: "bs_td.UpdateEnvironmentMembershipResultTypeDef",
    ) -> "dc_td.UpdateEnvironmentMembershipResult":
        return dc_td.UpdateEnvironmentMembershipResult.make_one(res)


cloud9_caster = CLOUD9Caster()
