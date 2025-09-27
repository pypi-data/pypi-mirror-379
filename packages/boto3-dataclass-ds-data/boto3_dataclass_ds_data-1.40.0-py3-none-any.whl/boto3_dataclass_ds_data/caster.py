# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_ds_data import type_defs as bs_td


class DS_DATACaster:

    def create_group(
        self,
        res: "bs_td.CreateGroupResultTypeDef",
    ) -> "dc_td.CreateGroupResult":
        return dc_td.CreateGroupResult.make_one(res)

    def create_user(
        self,
        res: "bs_td.CreateUserResultTypeDef",
    ) -> "dc_td.CreateUserResult":
        return dc_td.CreateUserResult.make_one(res)

    def describe_group(
        self,
        res: "bs_td.DescribeGroupResultTypeDef",
    ) -> "dc_td.DescribeGroupResult":
        return dc_td.DescribeGroupResult.make_one(res)

    def describe_user(
        self,
        res: "bs_td.DescribeUserResultTypeDef",
    ) -> "dc_td.DescribeUserResult":
        return dc_td.DescribeUserResult.make_one(res)

    def list_group_members(
        self,
        res: "bs_td.ListGroupMembersResultTypeDef",
    ) -> "dc_td.ListGroupMembersResult":
        return dc_td.ListGroupMembersResult.make_one(res)

    def list_groups(
        self,
        res: "bs_td.ListGroupsResultTypeDef",
    ) -> "dc_td.ListGroupsResult":
        return dc_td.ListGroupsResult.make_one(res)

    def list_groups_for_member(
        self,
        res: "bs_td.ListGroupsForMemberResultTypeDef",
    ) -> "dc_td.ListGroupsForMemberResult":
        return dc_td.ListGroupsForMemberResult.make_one(res)

    def list_users(
        self,
        res: "bs_td.ListUsersResultTypeDef",
    ) -> "dc_td.ListUsersResult":
        return dc_td.ListUsersResult.make_one(res)

    def search_groups(
        self,
        res: "bs_td.SearchGroupsResultTypeDef",
    ) -> "dc_td.SearchGroupsResult":
        return dc_td.SearchGroupsResult.make_one(res)

    def search_users(
        self,
        res: "bs_td.SearchUsersResultTypeDef",
    ) -> "dc_td.SearchUsersResult":
        return dc_td.SearchUsersResult.make_one(res)


ds_data_caster = DS_DATACaster()
