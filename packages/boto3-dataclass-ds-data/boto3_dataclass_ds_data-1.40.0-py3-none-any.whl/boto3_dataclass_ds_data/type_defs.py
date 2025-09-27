# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_ds_data import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AddGroupMemberRequest:
    boto3_raw_data: "type_defs.AddGroupMemberRequestTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")
    GroupName = field("GroupName")
    MemberName = field("MemberName")
    ClientToken = field("ClientToken")
    MemberRealm = field("MemberRealm")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddGroupMemberRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddGroupMemberRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttributeValueOutput:
    boto3_raw_data: "type_defs.AttributeValueOutputTypeDef" = dataclasses.field()

    BOOL = field("BOOL")
    N = field("N")
    S = field("S")
    SS = field("SS")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AttributeValueOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttributeValueOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttributeValue:
    boto3_raw_data: "type_defs.AttributeValueTypeDef" = dataclasses.field()

    BOOL = field("BOOL")
    N = field("N")
    S = field("S")
    SS = field("SS")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AttributeValueTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AttributeValueTypeDef"]],
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
class DeleteGroupRequest:
    boto3_raw_data: "type_defs.DeleteGroupRequestTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")
    SAMAccountName = field("SAMAccountName")
    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteUserRequest:
    boto3_raw_data: "type_defs.DeleteUserRequestTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")
    SAMAccountName = field("SAMAccountName")
    ClientToken = field("ClientToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteUserRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteUserRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeGroupRequest:
    boto3_raw_data: "type_defs.DescribeGroupRequestTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")
    SAMAccountName = field("SAMAccountName")
    OtherAttributes = field("OtherAttributes")
    Realm = field("Realm")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeUserRequest:
    boto3_raw_data: "type_defs.DescribeUserRequestTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")
    SAMAccountName = field("SAMAccountName")
    OtherAttributes = field("OtherAttributes")
    Realm = field("Realm")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeUserRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeUserRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisableUserRequest:
    boto3_raw_data: "type_defs.DisableUserRequestTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")
    SAMAccountName = field("SAMAccountName")
    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DisableUserRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisableUserRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GroupSummary:
    boto3_raw_data: "type_defs.GroupSummaryTypeDef" = dataclasses.field()

    GroupScope = field("GroupScope")
    GroupType = field("GroupType")
    SAMAccountName = field("SAMAccountName")
    SID = field("SID")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GroupSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GroupSummaryTypeDef"]],
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
class ListGroupMembersRequest:
    boto3_raw_data: "type_defs.ListGroupMembersRequestTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")
    SAMAccountName = field("SAMAccountName")
    MaxResults = field("MaxResults")
    MemberRealm = field("MemberRealm")
    NextToken = field("NextToken")
    Realm = field("Realm")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListGroupMembersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGroupMembersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Member:
    boto3_raw_data: "type_defs.MemberTypeDef" = dataclasses.field()

    MemberType = field("MemberType")
    SAMAccountName = field("SAMAccountName")
    SID = field("SID")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MemberTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MemberTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGroupsForMemberRequest:
    boto3_raw_data: "type_defs.ListGroupsForMemberRequestTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")
    SAMAccountName = field("SAMAccountName")
    MaxResults = field("MaxResults")
    MemberRealm = field("MemberRealm")
    NextToken = field("NextToken")
    Realm = field("Realm")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListGroupsForMemberRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGroupsForMemberRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGroupsRequest:
    boto3_raw_data: "type_defs.ListGroupsRequestTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    Realm = field("Realm")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListGroupsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGroupsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListUsersRequest:
    boto3_raw_data: "type_defs.ListUsersRequestTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    Realm = field("Realm")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListUsersRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListUsersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserSummary:
    boto3_raw_data: "type_defs.UserSummaryTypeDef" = dataclasses.field()

    Enabled = field("Enabled")
    SAMAccountName = field("SAMAccountName")
    SID = field("SID")
    GivenName = field("GivenName")
    Surname = field("Surname")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UserSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UserSummaryTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveGroupMemberRequest:
    boto3_raw_data: "type_defs.RemoveGroupMemberRequestTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")
    GroupName = field("GroupName")
    MemberName = field("MemberName")
    ClientToken = field("ClientToken")
    MemberRealm = field("MemberRealm")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RemoveGroupMemberRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveGroupMemberRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchGroupsRequest:
    boto3_raw_data: "type_defs.SearchGroupsRequestTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")
    SearchAttributes = field("SearchAttributes")
    SearchString = field("SearchString")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    Realm = field("Realm")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchGroupsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchGroupsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchUsersRequest:
    boto3_raw_data: "type_defs.SearchUsersRequestTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")
    SearchAttributes = field("SearchAttributes")
    SearchString = field("SearchString")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    Realm = field("Realm")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchUsersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchUsersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Group:
    boto3_raw_data: "type_defs.GroupTypeDef" = dataclasses.field()

    SAMAccountName = field("SAMAccountName")
    DistinguishedName = field("DistinguishedName")
    GroupScope = field("GroupScope")
    GroupType = field("GroupType")
    OtherAttributes = field("OtherAttributes")
    SID = field("SID")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GroupTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GroupTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class User:
    boto3_raw_data: "type_defs.UserTypeDef" = dataclasses.field()

    SAMAccountName = field("SAMAccountName")
    DistinguishedName = field("DistinguishedName")
    EmailAddress = field("EmailAddress")
    Enabled = field("Enabled")
    GivenName = field("GivenName")
    OtherAttributes = field("OtherAttributes")
    SID = field("SID")
    Surname = field("Surname")
    UserPrincipalName = field("UserPrincipalName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UserTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UserTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateGroupResult:
    boto3_raw_data: "type_defs.CreateGroupResultTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")
    SAMAccountName = field("SAMAccountName")
    SID = field("SID")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateGroupResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateGroupResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateUserResult:
    boto3_raw_data: "type_defs.CreateUserResultTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")
    SAMAccountName = field("SAMAccountName")
    SID = field("SID")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateUserResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateUserResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeGroupResult:
    boto3_raw_data: "type_defs.DescribeGroupResultTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")
    DistinguishedName = field("DistinguishedName")
    GroupScope = field("GroupScope")
    GroupType = field("GroupType")
    OtherAttributes = field("OtherAttributes")
    Realm = field("Realm")
    SAMAccountName = field("SAMAccountName")
    SID = field("SID")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeGroupResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeGroupResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeUserResult:
    boto3_raw_data: "type_defs.DescribeUserResultTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")
    DistinguishedName = field("DistinguishedName")
    EmailAddress = field("EmailAddress")
    Enabled = field("Enabled")
    GivenName = field("GivenName")
    OtherAttributes = field("OtherAttributes")
    Realm = field("Realm")
    SAMAccountName = field("SAMAccountName")
    SID = field("SID")
    Surname = field("Surname")
    UserPrincipalName = field("UserPrincipalName")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeUserResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeUserResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGroupsForMemberResult:
    boto3_raw_data: "type_defs.ListGroupsForMemberResultTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")

    @cached_property
    def Groups(self):  # pragma: no cover
        return GroupSummary.make_many(self.boto3_raw_data["Groups"])

    MemberRealm = field("MemberRealm")
    Realm = field("Realm")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListGroupsForMemberResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGroupsForMemberResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGroupsResult:
    boto3_raw_data: "type_defs.ListGroupsResultTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")

    @cached_property
    def Groups(self):  # pragma: no cover
        return GroupSummary.make_many(self.boto3_raw_data["Groups"])

    Realm = field("Realm")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListGroupsResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGroupsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGroupMembersRequestPaginate:
    boto3_raw_data: "type_defs.ListGroupMembersRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    DirectoryId = field("DirectoryId")
    SAMAccountName = field("SAMAccountName")
    MemberRealm = field("MemberRealm")
    Realm = field("Realm")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListGroupMembersRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGroupMembersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGroupsForMemberRequestPaginate:
    boto3_raw_data: "type_defs.ListGroupsForMemberRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    DirectoryId = field("DirectoryId")
    SAMAccountName = field("SAMAccountName")
    MemberRealm = field("MemberRealm")
    Realm = field("Realm")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListGroupsForMemberRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGroupsForMemberRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGroupsRequestPaginate:
    boto3_raw_data: "type_defs.ListGroupsRequestPaginateTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")
    Realm = field("Realm")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListGroupsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGroupsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListUsersRequestPaginate:
    boto3_raw_data: "type_defs.ListUsersRequestPaginateTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")
    Realm = field("Realm")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListUsersRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListUsersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchGroupsRequestPaginate:
    boto3_raw_data: "type_defs.SearchGroupsRequestPaginateTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")
    SearchAttributes = field("SearchAttributes")
    SearchString = field("SearchString")
    Realm = field("Realm")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchGroupsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchGroupsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchUsersRequestPaginate:
    boto3_raw_data: "type_defs.SearchUsersRequestPaginateTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")
    SearchAttributes = field("SearchAttributes")
    SearchString = field("SearchString")
    Realm = field("Realm")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchUsersRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchUsersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGroupMembersResult:
    boto3_raw_data: "type_defs.ListGroupMembersResultTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")
    MemberRealm = field("MemberRealm")

    @cached_property
    def Members(self):  # pragma: no cover
        return Member.make_many(self.boto3_raw_data["Members"])

    Realm = field("Realm")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListGroupMembersResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGroupMembersResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListUsersResult:
    boto3_raw_data: "type_defs.ListUsersResultTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")
    Realm = field("Realm")

    @cached_property
    def Users(self):  # pragma: no cover
        return UserSummary.make_many(self.boto3_raw_data["Users"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListUsersResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListUsersResultTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchGroupsResult:
    boto3_raw_data: "type_defs.SearchGroupsResultTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")

    @cached_property
    def Groups(self):  # pragma: no cover
        return Group.make_many(self.boto3_raw_data["Groups"])

    Realm = field("Realm")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchGroupsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchGroupsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchUsersResult:
    boto3_raw_data: "type_defs.SearchUsersResultTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")
    Realm = field("Realm")

    @cached_property
    def Users(self):  # pragma: no cover
        return User.make_many(self.boto3_raw_data["Users"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SearchUsersResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchUsersResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateGroupRequest:
    boto3_raw_data: "type_defs.CreateGroupRequestTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")
    SAMAccountName = field("SAMAccountName")
    ClientToken = field("ClientToken")
    GroupScope = field("GroupScope")
    GroupType = field("GroupType")
    OtherAttributes = field("OtherAttributes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateUserRequest:
    boto3_raw_data: "type_defs.CreateUserRequestTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")
    SAMAccountName = field("SAMAccountName")
    ClientToken = field("ClientToken")
    EmailAddress = field("EmailAddress")
    GivenName = field("GivenName")
    OtherAttributes = field("OtherAttributes")
    Surname = field("Surname")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateUserRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateUserRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateGroupRequest:
    boto3_raw_data: "type_defs.UpdateGroupRequestTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")
    SAMAccountName = field("SAMAccountName")
    ClientToken = field("ClientToken")
    GroupScope = field("GroupScope")
    GroupType = field("GroupType")
    OtherAttributes = field("OtherAttributes")
    UpdateType = field("UpdateType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateUserRequest:
    boto3_raw_data: "type_defs.UpdateUserRequestTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")
    SAMAccountName = field("SAMAccountName")
    ClientToken = field("ClientToken")
    EmailAddress = field("EmailAddress")
    GivenName = field("GivenName")
    OtherAttributes = field("OtherAttributes")
    Surname = field("Surname")
    UpdateType = field("UpdateType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateUserRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateUserRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
