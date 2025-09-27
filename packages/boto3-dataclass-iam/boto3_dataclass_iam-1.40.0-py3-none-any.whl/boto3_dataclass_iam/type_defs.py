# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_iam import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AccessDetail:
    boto3_raw_data: "type_defs.AccessDetailTypeDef" = dataclasses.field()

    ServiceName = field("ServiceName")
    ServiceNamespace = field("ServiceNamespace")
    Region = field("Region")
    EntityPath = field("EntityPath")
    LastAuthenticatedTime = field("LastAuthenticatedTime")
    TotalAuthenticatedEntities = field("TotalAuthenticatedEntities")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AccessDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AccessDetailTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccessKeyLastUsed:
    boto3_raw_data: "type_defs.AccessKeyLastUsedTypeDef" = dataclasses.field()

    ServiceName = field("ServiceName")
    Region = field("Region")
    LastUsedDate = field("LastUsedDate")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AccessKeyLastUsedTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccessKeyLastUsedTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccessKeyMetadata:
    boto3_raw_data: "type_defs.AccessKeyMetadataTypeDef" = dataclasses.field()

    UserName = field("UserName")
    AccessKeyId = field("AccessKeyId")
    Status = field("Status")
    CreateDate = field("CreateDate")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AccessKeyMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccessKeyMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccessKey:
    boto3_raw_data: "type_defs.AccessKeyTypeDef" = dataclasses.field()

    UserName = field("UserName")
    AccessKeyId = field("AccessKeyId")
    Status = field("Status")
    SecretAccessKey = field("SecretAccessKey")
    CreateDate = field("CreateDate")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AccessKeyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AccessKeyTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddClientIDToOpenIDConnectProviderRequest:
    boto3_raw_data: "type_defs.AddClientIDToOpenIDConnectProviderRequestTypeDef" = (
        dataclasses.field()
    )

    OpenIDConnectProviderArn = field("OpenIDConnectProviderArn")
    ClientID = field("ClientID")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AddClientIDToOpenIDConnectProviderRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddClientIDToOpenIDConnectProviderRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddRoleToInstanceProfileRequestInstanceProfileAddRole:
    boto3_raw_data: (
        "type_defs.AddRoleToInstanceProfileRequestInstanceProfileAddRoleTypeDef"
    ) = dataclasses.field()

    RoleName = field("RoleName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AddRoleToInstanceProfileRequestInstanceProfileAddRoleTypeDef"
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
                "type_defs.AddRoleToInstanceProfileRequestInstanceProfileAddRoleTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddRoleToInstanceProfileRequest:
    boto3_raw_data: "type_defs.AddRoleToInstanceProfileRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceProfileName = field("InstanceProfileName")
    RoleName = field("RoleName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AddRoleToInstanceProfileRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddRoleToInstanceProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddUserToGroupRequestGroupAddUser:
    boto3_raw_data: "type_defs.AddUserToGroupRequestGroupAddUserTypeDef" = (
        dataclasses.field()
    )

    UserName = field("UserName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AddUserToGroupRequestGroupAddUserTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddUserToGroupRequestGroupAddUserTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddUserToGroupRequest:
    boto3_raw_data: "type_defs.AddUserToGroupRequestTypeDef" = dataclasses.field()

    GroupName = field("GroupName")
    UserName = field("UserName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddUserToGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddUserToGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddUserToGroupRequestUserAddGroup:
    boto3_raw_data: "type_defs.AddUserToGroupRequestUserAddGroupTypeDef" = (
        dataclasses.field()
    )

    GroupName = field("GroupName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AddUserToGroupRequestUserAddGroupTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddUserToGroupRequestUserAddGroupTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttachGroupPolicyRequestGroupAttachPolicy:
    boto3_raw_data: "type_defs.AttachGroupPolicyRequestGroupAttachPolicyTypeDef" = (
        dataclasses.field()
    )

    PolicyArn = field("PolicyArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AttachGroupPolicyRequestGroupAttachPolicyTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttachGroupPolicyRequestGroupAttachPolicyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttachGroupPolicyRequestPolicyAttachGroup:
    boto3_raw_data: "type_defs.AttachGroupPolicyRequestPolicyAttachGroupTypeDef" = (
        dataclasses.field()
    )

    GroupName = field("GroupName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AttachGroupPolicyRequestPolicyAttachGroupTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttachGroupPolicyRequestPolicyAttachGroupTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttachGroupPolicyRequest:
    boto3_raw_data: "type_defs.AttachGroupPolicyRequestTypeDef" = dataclasses.field()

    GroupName = field("GroupName")
    PolicyArn = field("PolicyArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AttachGroupPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttachGroupPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttachRolePolicyRequestPolicyAttachRole:
    boto3_raw_data: "type_defs.AttachRolePolicyRequestPolicyAttachRoleTypeDef" = (
        dataclasses.field()
    )

    RoleName = field("RoleName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AttachRolePolicyRequestPolicyAttachRoleTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttachRolePolicyRequestPolicyAttachRoleTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttachRolePolicyRequestRoleAttachPolicy:
    boto3_raw_data: "type_defs.AttachRolePolicyRequestRoleAttachPolicyTypeDef" = (
        dataclasses.field()
    )

    PolicyArn = field("PolicyArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AttachRolePolicyRequestRoleAttachPolicyTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttachRolePolicyRequestRoleAttachPolicyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttachRolePolicyRequest:
    boto3_raw_data: "type_defs.AttachRolePolicyRequestTypeDef" = dataclasses.field()

    RoleName = field("RoleName")
    PolicyArn = field("PolicyArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AttachRolePolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttachRolePolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttachUserPolicyRequestPolicyAttachUser:
    boto3_raw_data: "type_defs.AttachUserPolicyRequestPolicyAttachUserTypeDef" = (
        dataclasses.field()
    )

    UserName = field("UserName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AttachUserPolicyRequestPolicyAttachUserTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttachUserPolicyRequestPolicyAttachUserTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttachUserPolicyRequest:
    boto3_raw_data: "type_defs.AttachUserPolicyRequestTypeDef" = dataclasses.field()

    UserName = field("UserName")
    PolicyArn = field("PolicyArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AttachUserPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttachUserPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttachUserPolicyRequestUserAttachPolicy:
    boto3_raw_data: "type_defs.AttachUserPolicyRequestUserAttachPolicyTypeDef" = (
        dataclasses.field()
    )

    PolicyArn = field("PolicyArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AttachUserPolicyRequestUserAttachPolicyTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttachUserPolicyRequestUserAttachPolicyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttachedPermissionsBoundary:
    boto3_raw_data: "type_defs.AttachedPermissionsBoundaryTypeDef" = dataclasses.field()

    PermissionsBoundaryType = field("PermissionsBoundaryType")
    PermissionsBoundaryArn = field("PermissionsBoundaryArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AttachedPermissionsBoundaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttachedPermissionsBoundaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttachedPolicy:
    boto3_raw_data: "type_defs.AttachedPolicyTypeDef" = dataclasses.field()

    PolicyName = field("PolicyName")
    PolicyArn = field("PolicyArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AttachedPolicyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AttachedPolicyTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChangePasswordRequestServiceResourceChangePassword:
    boto3_raw_data: (
        "type_defs.ChangePasswordRequestServiceResourceChangePasswordTypeDef"
    ) = dataclasses.field()

    OldPassword = field("OldPassword")
    NewPassword = field("NewPassword")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ChangePasswordRequestServiceResourceChangePasswordTypeDef"
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
                "type_defs.ChangePasswordRequestServiceResourceChangePasswordTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChangePasswordRequest:
    boto3_raw_data: "type_defs.ChangePasswordRequestTypeDef" = dataclasses.field()

    OldPassword = field("OldPassword")
    NewPassword = field("NewPassword")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ChangePasswordRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ChangePasswordRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContextEntry:
    boto3_raw_data: "type_defs.ContextEntryTypeDef" = dataclasses.field()

    ContextKeyName = field("ContextKeyName")
    ContextKeyValues = field("ContextKeyValues")
    ContextKeyType = field("ContextKeyType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ContextEntryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ContextEntryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAccessKeyRequest:
    boto3_raw_data: "type_defs.CreateAccessKeyRequestTypeDef" = dataclasses.field()

    UserName = field("UserName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAccessKeyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAccessKeyRequestTypeDef"]
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
class CreateAccountAliasRequestServiceResourceCreateAccountAlias:
    boto3_raw_data: (
        "type_defs.CreateAccountAliasRequestServiceResourceCreateAccountAliasTypeDef"
    ) = dataclasses.field()

    AccountAlias = field("AccountAlias")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateAccountAliasRequestServiceResourceCreateAccountAliasTypeDef"
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
                "type_defs.CreateAccountAliasRequestServiceResourceCreateAccountAliasTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAccountAliasRequest:
    boto3_raw_data: "type_defs.CreateAccountAliasRequestTypeDef" = dataclasses.field()

    AccountAlias = field("AccountAlias")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAccountAliasRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAccountAliasRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateGroupRequestGroupCreate:
    boto3_raw_data: "type_defs.CreateGroupRequestGroupCreateTypeDef" = (
        dataclasses.field()
    )

    Path = field("Path")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateGroupRequestGroupCreateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateGroupRequestGroupCreateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateGroupRequestServiceResourceCreateGroup:
    boto3_raw_data: "type_defs.CreateGroupRequestServiceResourceCreateGroupTypeDef" = (
        dataclasses.field()
    )

    GroupName = field("GroupName")
    Path = field("Path")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateGroupRequestServiceResourceCreateGroupTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateGroupRequestServiceResourceCreateGroupTypeDef"]
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

    GroupName = field("GroupName")
    Path = field("Path")

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
class Group:
    boto3_raw_data: "type_defs.GroupTypeDef" = dataclasses.field()

    Path = field("Path")
    GroupName = field("GroupName")
    GroupId = field("GroupId")
    Arn = field("Arn")
    CreateDate = field("CreateDate")

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
class Tag:
    boto3_raw_data: "type_defs.TagTypeDef" = dataclasses.field()

    Key = field("Key")
    Value = field("Value")

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
class CreateLoginProfileRequestLoginProfileCreate:
    boto3_raw_data: "type_defs.CreateLoginProfileRequestLoginProfileCreateTypeDef" = (
        dataclasses.field()
    )

    Password = field("Password")
    PasswordResetRequired = field("PasswordResetRequired")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateLoginProfileRequestLoginProfileCreateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLoginProfileRequestLoginProfileCreateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLoginProfileRequest:
    boto3_raw_data: "type_defs.CreateLoginProfileRequestTypeDef" = dataclasses.field()

    UserName = field("UserName")
    Password = field("Password")
    PasswordResetRequired = field("PasswordResetRequired")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateLoginProfileRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLoginProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLoginProfileRequestUserCreateLoginProfile:
    boto3_raw_data: (
        "type_defs.CreateLoginProfileRequestUserCreateLoginProfileTypeDef"
    ) = dataclasses.field()

    Password = field("Password")
    PasswordResetRequired = field("PasswordResetRequired")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateLoginProfileRequestUserCreateLoginProfileTypeDef"
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
                "type_defs.CreateLoginProfileRequestUserCreateLoginProfileTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoginProfile:
    boto3_raw_data: "type_defs.LoginProfileTypeDef" = dataclasses.field()

    UserName = field("UserName")
    CreateDate = field("CreateDate")
    PasswordResetRequired = field("PasswordResetRequired")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LoginProfileTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LoginProfileTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePolicyVersionRequestPolicyCreateVersion:
    boto3_raw_data: "type_defs.CreatePolicyVersionRequestPolicyCreateVersionTypeDef" = (
        dataclasses.field()
    )

    PolicyDocument = field("PolicyDocument")
    SetAsDefault = field("SetAsDefault")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreatePolicyVersionRequestPolicyCreateVersionTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePolicyVersionRequestPolicyCreateVersionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePolicyVersionRequest:
    boto3_raw_data: "type_defs.CreatePolicyVersionRequestTypeDef" = dataclasses.field()

    PolicyArn = field("PolicyArn")
    PolicyDocument = field("PolicyDocument")
    SetAsDefault = field("SetAsDefault")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePolicyVersionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePolicyVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateServiceLinkedRoleRequest:
    boto3_raw_data: "type_defs.CreateServiceLinkedRoleRequestTypeDef" = (
        dataclasses.field()
    )

    AWSServiceName = field("AWSServiceName")
    Description = field("Description")
    CustomSuffix = field("CustomSuffix")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateServiceLinkedRoleRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateServiceLinkedRoleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateServiceSpecificCredentialRequest:
    boto3_raw_data: "type_defs.CreateServiceSpecificCredentialRequestTypeDef" = (
        dataclasses.field()
    )

    UserName = field("UserName")
    ServiceName = field("ServiceName")
    CredentialAgeDays = field("CredentialAgeDays")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateServiceSpecificCredentialRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateServiceSpecificCredentialRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceSpecificCredential:
    boto3_raw_data: "type_defs.ServiceSpecificCredentialTypeDef" = dataclasses.field()

    CreateDate = field("CreateDate")
    ServiceName = field("ServiceName")
    ServiceSpecificCredentialId = field("ServiceSpecificCredentialId")
    UserName = field("UserName")
    Status = field("Status")
    ExpirationDate = field("ExpirationDate")
    ServiceUserName = field("ServiceUserName")
    ServicePassword = field("ServicePassword")
    ServiceCredentialAlias = field("ServiceCredentialAlias")
    ServiceCredentialSecret = field("ServiceCredentialSecret")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ServiceSpecificCredentialTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceSpecificCredentialTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeactivateMFADeviceRequest:
    boto3_raw_data: "type_defs.DeactivateMFADeviceRequestTypeDef" = dataclasses.field()

    SerialNumber = field("SerialNumber")
    UserName = field("UserName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeactivateMFADeviceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeactivateMFADeviceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAccessKeyRequest:
    boto3_raw_data: "type_defs.DeleteAccessKeyRequestTypeDef" = dataclasses.field()

    AccessKeyId = field("AccessKeyId")
    UserName = field("UserName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAccessKeyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAccessKeyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAccountAliasRequest:
    boto3_raw_data: "type_defs.DeleteAccountAliasRequestTypeDef" = dataclasses.field()

    AccountAlias = field("AccountAlias")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAccountAliasRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAccountAliasRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteGroupPolicyRequest:
    boto3_raw_data: "type_defs.DeleteGroupPolicyRequestTypeDef" = dataclasses.field()

    GroupName = field("GroupName")
    PolicyName = field("PolicyName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteGroupPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteGroupPolicyRequestTypeDef"]
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

    GroupName = field("GroupName")

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
class DeleteInstanceProfileRequest:
    boto3_raw_data: "type_defs.DeleteInstanceProfileRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceProfileName = field("InstanceProfileName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteInstanceProfileRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteInstanceProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteLoginProfileRequest:
    boto3_raw_data: "type_defs.DeleteLoginProfileRequestTypeDef" = dataclasses.field()

    UserName = field("UserName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteLoginProfileRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteLoginProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteOpenIDConnectProviderRequest:
    boto3_raw_data: "type_defs.DeleteOpenIDConnectProviderRequestTypeDef" = (
        dataclasses.field()
    )

    OpenIDConnectProviderArn = field("OpenIDConnectProviderArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteOpenIDConnectProviderRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteOpenIDConnectProviderRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePolicyRequest:
    boto3_raw_data: "type_defs.DeletePolicyRequestTypeDef" = dataclasses.field()

    PolicyArn = field("PolicyArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeletePolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePolicyVersionRequest:
    boto3_raw_data: "type_defs.DeletePolicyVersionRequestTypeDef" = dataclasses.field()

    PolicyArn = field("PolicyArn")
    VersionId = field("VersionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeletePolicyVersionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePolicyVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRolePermissionsBoundaryRequest:
    boto3_raw_data: "type_defs.DeleteRolePermissionsBoundaryRequestTypeDef" = (
        dataclasses.field()
    )

    RoleName = field("RoleName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteRolePermissionsBoundaryRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRolePermissionsBoundaryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRolePolicyRequest:
    boto3_raw_data: "type_defs.DeleteRolePolicyRequestTypeDef" = dataclasses.field()

    RoleName = field("RoleName")
    PolicyName = field("PolicyName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteRolePolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRolePolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRoleRequest:
    boto3_raw_data: "type_defs.DeleteRoleRequestTypeDef" = dataclasses.field()

    RoleName = field("RoleName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteRoleRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRoleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSAMLProviderRequest:
    boto3_raw_data: "type_defs.DeleteSAMLProviderRequestTypeDef" = dataclasses.field()

    SAMLProviderArn = field("SAMLProviderArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteSAMLProviderRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSAMLProviderRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSSHPublicKeyRequest:
    boto3_raw_data: "type_defs.DeleteSSHPublicKeyRequestTypeDef" = dataclasses.field()

    UserName = field("UserName")
    SSHPublicKeyId = field("SSHPublicKeyId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteSSHPublicKeyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSSHPublicKeyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteServerCertificateRequest:
    boto3_raw_data: "type_defs.DeleteServerCertificateRequestTypeDef" = (
        dataclasses.field()
    )

    ServerCertificateName = field("ServerCertificateName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteServerCertificateRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteServerCertificateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteServiceLinkedRoleRequest:
    boto3_raw_data: "type_defs.DeleteServiceLinkedRoleRequestTypeDef" = (
        dataclasses.field()
    )

    RoleName = field("RoleName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteServiceLinkedRoleRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteServiceLinkedRoleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteServiceSpecificCredentialRequest:
    boto3_raw_data: "type_defs.DeleteServiceSpecificCredentialRequestTypeDef" = (
        dataclasses.field()
    )

    ServiceSpecificCredentialId = field("ServiceSpecificCredentialId")
    UserName = field("UserName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteServiceSpecificCredentialRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteServiceSpecificCredentialRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSigningCertificateRequest:
    boto3_raw_data: "type_defs.DeleteSigningCertificateRequestTypeDef" = (
        dataclasses.field()
    )

    CertificateId = field("CertificateId")
    UserName = field("UserName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteSigningCertificateRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSigningCertificateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteUserPermissionsBoundaryRequest:
    boto3_raw_data: "type_defs.DeleteUserPermissionsBoundaryRequestTypeDef" = (
        dataclasses.field()
    )

    UserName = field("UserName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteUserPermissionsBoundaryRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteUserPermissionsBoundaryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteUserPolicyRequest:
    boto3_raw_data: "type_defs.DeleteUserPolicyRequestTypeDef" = dataclasses.field()

    UserName = field("UserName")
    PolicyName = field("PolicyName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteUserPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteUserPolicyRequestTypeDef"]
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

    UserName = field("UserName")

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
class DeleteVirtualMFADeviceRequest:
    boto3_raw_data: "type_defs.DeleteVirtualMFADeviceRequestTypeDef" = (
        dataclasses.field()
    )

    SerialNumber = field("SerialNumber")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteVirtualMFADeviceRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteVirtualMFADeviceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RoleUsageType:
    boto3_raw_data: "type_defs.RoleUsageTypeTypeDef" = dataclasses.field()

    Region = field("Region")
    Resources = field("Resources")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RoleUsageTypeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RoleUsageTypeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetachGroupPolicyRequestGroupDetachPolicy:
    boto3_raw_data: "type_defs.DetachGroupPolicyRequestGroupDetachPolicyTypeDef" = (
        dataclasses.field()
    )

    PolicyArn = field("PolicyArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DetachGroupPolicyRequestGroupDetachPolicyTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetachGroupPolicyRequestGroupDetachPolicyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetachGroupPolicyRequestPolicyDetachGroup:
    boto3_raw_data: "type_defs.DetachGroupPolicyRequestPolicyDetachGroupTypeDef" = (
        dataclasses.field()
    )

    GroupName = field("GroupName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DetachGroupPolicyRequestPolicyDetachGroupTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetachGroupPolicyRequestPolicyDetachGroupTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetachGroupPolicyRequest:
    boto3_raw_data: "type_defs.DetachGroupPolicyRequestTypeDef" = dataclasses.field()

    GroupName = field("GroupName")
    PolicyArn = field("PolicyArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DetachGroupPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetachGroupPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetachRolePolicyRequestPolicyDetachRole:
    boto3_raw_data: "type_defs.DetachRolePolicyRequestPolicyDetachRoleTypeDef" = (
        dataclasses.field()
    )

    RoleName = field("RoleName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DetachRolePolicyRequestPolicyDetachRoleTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetachRolePolicyRequestPolicyDetachRoleTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetachRolePolicyRequestRoleDetachPolicy:
    boto3_raw_data: "type_defs.DetachRolePolicyRequestRoleDetachPolicyTypeDef" = (
        dataclasses.field()
    )

    PolicyArn = field("PolicyArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DetachRolePolicyRequestRoleDetachPolicyTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetachRolePolicyRequestRoleDetachPolicyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetachRolePolicyRequest:
    boto3_raw_data: "type_defs.DetachRolePolicyRequestTypeDef" = dataclasses.field()

    RoleName = field("RoleName")
    PolicyArn = field("PolicyArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DetachRolePolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetachRolePolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetachUserPolicyRequestPolicyDetachUser:
    boto3_raw_data: "type_defs.DetachUserPolicyRequestPolicyDetachUserTypeDef" = (
        dataclasses.field()
    )

    UserName = field("UserName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DetachUserPolicyRequestPolicyDetachUserTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetachUserPolicyRequestPolicyDetachUserTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetachUserPolicyRequest:
    boto3_raw_data: "type_defs.DetachUserPolicyRequestTypeDef" = dataclasses.field()

    UserName = field("UserName")
    PolicyArn = field("PolicyArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DetachUserPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetachUserPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetachUserPolicyRequestUserDetachPolicy:
    boto3_raw_data: "type_defs.DetachUserPolicyRequestUserDetachPolicyTypeDef" = (
        dataclasses.field()
    )

    PolicyArn = field("PolicyArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DetachUserPolicyRequestUserDetachPolicyTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetachUserPolicyRequestUserDetachPolicyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnableMFADeviceRequestMfaDeviceAssociate:
    boto3_raw_data: "type_defs.EnableMFADeviceRequestMfaDeviceAssociateTypeDef" = (
        dataclasses.field()
    )

    AuthenticationCode1 = field("AuthenticationCode1")
    AuthenticationCode2 = field("AuthenticationCode2")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.EnableMFADeviceRequestMfaDeviceAssociateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnableMFADeviceRequestMfaDeviceAssociateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnableMFADeviceRequest:
    boto3_raw_data: "type_defs.EnableMFADeviceRequestTypeDef" = dataclasses.field()

    UserName = field("UserName")
    SerialNumber = field("SerialNumber")
    AuthenticationCode1 = field("AuthenticationCode1")
    AuthenticationCode2 = field("AuthenticationCode2")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EnableMFADeviceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnableMFADeviceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnableMFADeviceRequestUserEnableMfa:
    boto3_raw_data: "type_defs.EnableMFADeviceRequestUserEnableMfaTypeDef" = (
        dataclasses.field()
    )

    SerialNumber = field("SerialNumber")
    AuthenticationCode1 = field("AuthenticationCode1")
    AuthenticationCode2 = field("AuthenticationCode2")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.EnableMFADeviceRequestUserEnableMfaTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnableMFADeviceRequestUserEnableMfaTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EntityInfo:
    boto3_raw_data: "type_defs.EntityInfoTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Name = field("Name")
    Type = field("Type")
    Id = field("Id")
    Path = field("Path")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EntityInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EntityInfoTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ErrorDetails:
    boto3_raw_data: "type_defs.ErrorDetailsTypeDef" = dataclasses.field()

    Message = field("Message")
    Code = field("Code")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ErrorDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ErrorDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OrganizationsDecisionDetail:
    boto3_raw_data: "type_defs.OrganizationsDecisionDetailTypeDef" = dataclasses.field()

    AllowedByOrganizations = field("AllowedByOrganizations")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OrganizationsDecisionDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OrganizationsDecisionDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PermissionsBoundaryDecisionDetail:
    boto3_raw_data: "type_defs.PermissionsBoundaryDecisionDetailTypeDef" = (
        dataclasses.field()
    )

    AllowedByPermissionsBoundary = field("AllowedByPermissionsBoundary")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PermissionsBoundaryDecisionDetailTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PermissionsBoundaryDecisionDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GenerateOrganizationsAccessReportRequest:
    boto3_raw_data: "type_defs.GenerateOrganizationsAccessReportRequestTypeDef" = (
        dataclasses.field()
    )

    EntityPath = field("EntityPath")
    OrganizationsPolicyId = field("OrganizationsPolicyId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GenerateOrganizationsAccessReportRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GenerateOrganizationsAccessReportRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GenerateServiceLastAccessedDetailsRequest:
    boto3_raw_data: "type_defs.GenerateServiceLastAccessedDetailsRequestTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    Granularity = field("Granularity")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GenerateServiceLastAccessedDetailsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GenerateServiceLastAccessedDetailsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAccessKeyLastUsedRequest:
    boto3_raw_data: "type_defs.GetAccessKeyLastUsedRequestTypeDef" = dataclasses.field()

    AccessKeyId = field("AccessKeyId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAccessKeyLastUsedRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAccessKeyLastUsedRequestTypeDef"]
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
class GetAccountAuthorizationDetailsRequest:
    boto3_raw_data: "type_defs.GetAccountAuthorizationDetailsRequestTypeDef" = (
        dataclasses.field()
    )

    Filter = field("Filter")
    MaxItems = field("MaxItems")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetAccountAuthorizationDetailsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAccountAuthorizationDetailsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PasswordPolicy:
    boto3_raw_data: "type_defs.PasswordPolicyTypeDef" = dataclasses.field()

    MinimumPasswordLength = field("MinimumPasswordLength")
    RequireSymbols = field("RequireSymbols")
    RequireNumbers = field("RequireNumbers")
    RequireUppercaseCharacters = field("RequireUppercaseCharacters")
    RequireLowercaseCharacters = field("RequireLowercaseCharacters")
    AllowUsersToChangePassword = field("AllowUsersToChangePassword")
    ExpirePasswords = field("ExpirePasswords")
    MaxPasswordAge = field("MaxPasswordAge")
    PasswordReusePrevention = field("PasswordReusePrevention")
    HardExpiry = field("HardExpiry")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PasswordPolicyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PasswordPolicyTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetContextKeysForCustomPolicyRequest:
    boto3_raw_data: "type_defs.GetContextKeysForCustomPolicyRequestTypeDef" = (
        dataclasses.field()
    )

    PolicyInputList = field("PolicyInputList")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetContextKeysForCustomPolicyRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetContextKeysForCustomPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetContextKeysForPrincipalPolicyRequest:
    boto3_raw_data: "type_defs.GetContextKeysForPrincipalPolicyRequestTypeDef" = (
        dataclasses.field()
    )

    PolicySourceArn = field("PolicySourceArn")
    PolicyInputList = field("PolicyInputList")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetContextKeysForPrincipalPolicyRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetContextKeysForPrincipalPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetGroupPolicyRequest:
    boto3_raw_data: "type_defs.GetGroupPolicyRequestTypeDef" = dataclasses.field()

    GroupName = field("GroupName")
    PolicyName = field("PolicyName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetGroupPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetGroupPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetGroupRequest:
    boto3_raw_data: "type_defs.GetGroupRequestTypeDef" = dataclasses.field()

    GroupName = field("GroupName")
    Marker = field("Marker")
    MaxItems = field("MaxItems")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetGroupRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetGroupRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetInstanceProfileRequest:
    boto3_raw_data: "type_defs.GetInstanceProfileRequestTypeDef" = dataclasses.field()

    InstanceProfileName = field("InstanceProfileName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetInstanceProfileRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetInstanceProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WaiterConfig:
    boto3_raw_data: "type_defs.WaiterConfigTypeDef" = dataclasses.field()

    Delay = field("Delay")
    MaxAttempts = field("MaxAttempts")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WaiterConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WaiterConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLoginProfileRequest:
    boto3_raw_data: "type_defs.GetLoginProfileRequestTypeDef" = dataclasses.field()

    UserName = field("UserName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetLoginProfileRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLoginProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMFADeviceRequest:
    boto3_raw_data: "type_defs.GetMFADeviceRequestTypeDef" = dataclasses.field()

    SerialNumber = field("SerialNumber")
    UserName = field("UserName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMFADeviceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMFADeviceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetOpenIDConnectProviderRequest:
    boto3_raw_data: "type_defs.GetOpenIDConnectProviderRequestTypeDef" = (
        dataclasses.field()
    )

    OpenIDConnectProviderArn = field("OpenIDConnectProviderArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetOpenIDConnectProviderRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetOpenIDConnectProviderRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetOrganizationsAccessReportRequest:
    boto3_raw_data: "type_defs.GetOrganizationsAccessReportRequestTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")
    MaxItems = field("MaxItems")
    Marker = field("Marker")
    SortKey = field("SortKey")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetOrganizationsAccessReportRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetOrganizationsAccessReportRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPolicyRequest:
    boto3_raw_data: "type_defs.GetPolicyRequestTypeDef" = dataclasses.field()

    PolicyArn = field("PolicyArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetPolicyRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPolicyVersionRequest:
    boto3_raw_data: "type_defs.GetPolicyVersionRequestTypeDef" = dataclasses.field()

    PolicyArn = field("PolicyArn")
    VersionId = field("VersionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetPolicyVersionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPolicyVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRolePolicyRequest:
    boto3_raw_data: "type_defs.GetRolePolicyRequestTypeDef" = dataclasses.field()

    RoleName = field("RoleName")
    PolicyName = field("PolicyName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetRolePolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRolePolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRoleRequest:
    boto3_raw_data: "type_defs.GetRoleRequestTypeDef" = dataclasses.field()

    RoleName = field("RoleName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetRoleRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetRoleRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSAMLProviderRequest:
    boto3_raw_data: "type_defs.GetSAMLProviderRequestTypeDef" = dataclasses.field()

    SAMLProviderArn = field("SAMLProviderArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSAMLProviderRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSAMLProviderRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SAMLPrivateKey:
    boto3_raw_data: "type_defs.SAMLPrivateKeyTypeDef" = dataclasses.field()

    KeyId = field("KeyId")
    Timestamp = field("Timestamp")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SAMLPrivateKeyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SAMLPrivateKeyTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSSHPublicKeyRequest:
    boto3_raw_data: "type_defs.GetSSHPublicKeyRequestTypeDef" = dataclasses.field()

    UserName = field("UserName")
    SSHPublicKeyId = field("SSHPublicKeyId")
    Encoding = field("Encoding")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSSHPublicKeyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSSHPublicKeyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SSHPublicKey:
    boto3_raw_data: "type_defs.SSHPublicKeyTypeDef" = dataclasses.field()

    UserName = field("UserName")
    SSHPublicKeyId = field("SSHPublicKeyId")
    Fingerprint = field("Fingerprint")
    SSHPublicKeyBody = field("SSHPublicKeyBody")
    Status = field("Status")
    UploadDate = field("UploadDate")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SSHPublicKeyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SSHPublicKeyTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetServerCertificateRequest:
    boto3_raw_data: "type_defs.GetServerCertificateRequestTypeDef" = dataclasses.field()

    ServerCertificateName = field("ServerCertificateName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetServerCertificateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetServerCertificateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetServiceLastAccessedDetailsRequest:
    boto3_raw_data: "type_defs.GetServiceLastAccessedDetailsRequestTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")
    MaxItems = field("MaxItems")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetServiceLastAccessedDetailsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetServiceLastAccessedDetailsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetServiceLastAccessedDetailsWithEntitiesRequest:
    boto3_raw_data: (
        "type_defs.GetServiceLastAccessedDetailsWithEntitiesRequestTypeDef"
    ) = dataclasses.field()

    JobId = field("JobId")
    ServiceNamespace = field("ServiceNamespace")
    MaxItems = field("MaxItems")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetServiceLastAccessedDetailsWithEntitiesRequestTypeDef"
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
                "type_defs.GetServiceLastAccessedDetailsWithEntitiesRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetServiceLinkedRoleDeletionStatusRequest:
    boto3_raw_data: "type_defs.GetServiceLinkedRoleDeletionStatusRequestTypeDef" = (
        dataclasses.field()
    )

    DeletionTaskId = field("DeletionTaskId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetServiceLinkedRoleDeletionStatusRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetServiceLinkedRoleDeletionStatusRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetUserPolicyRequest:
    boto3_raw_data: "type_defs.GetUserPolicyRequestTypeDef" = dataclasses.field()

    UserName = field("UserName")
    PolicyName = field("PolicyName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetUserPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetUserPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetUserRequest:
    boto3_raw_data: "type_defs.GetUserRequestTypeDef" = dataclasses.field()

    UserName = field("UserName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetUserRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetUserRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAccessKeysRequest:
    boto3_raw_data: "type_defs.ListAccessKeysRequestTypeDef" = dataclasses.field()

    UserName = field("UserName")
    Marker = field("Marker")
    MaxItems = field("MaxItems")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAccessKeysRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAccessKeysRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAccountAliasesRequest:
    boto3_raw_data: "type_defs.ListAccountAliasesRequestTypeDef" = dataclasses.field()

    Marker = field("Marker")
    MaxItems = field("MaxItems")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAccountAliasesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAccountAliasesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAttachedGroupPoliciesRequest:
    boto3_raw_data: "type_defs.ListAttachedGroupPoliciesRequestTypeDef" = (
        dataclasses.field()
    )

    GroupName = field("GroupName")
    PathPrefix = field("PathPrefix")
    Marker = field("Marker")
    MaxItems = field("MaxItems")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAttachedGroupPoliciesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAttachedGroupPoliciesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAttachedRolePoliciesRequest:
    boto3_raw_data: "type_defs.ListAttachedRolePoliciesRequestTypeDef" = (
        dataclasses.field()
    )

    RoleName = field("RoleName")
    PathPrefix = field("PathPrefix")
    Marker = field("Marker")
    MaxItems = field("MaxItems")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAttachedRolePoliciesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAttachedRolePoliciesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAttachedUserPoliciesRequest:
    boto3_raw_data: "type_defs.ListAttachedUserPoliciesRequestTypeDef" = (
        dataclasses.field()
    )

    UserName = field("UserName")
    PathPrefix = field("PathPrefix")
    Marker = field("Marker")
    MaxItems = field("MaxItems")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAttachedUserPoliciesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAttachedUserPoliciesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEntitiesForPolicyRequest:
    boto3_raw_data: "type_defs.ListEntitiesForPolicyRequestTypeDef" = (
        dataclasses.field()
    )

    PolicyArn = field("PolicyArn")
    EntityFilter = field("EntityFilter")
    PathPrefix = field("PathPrefix")
    PolicyUsageFilter = field("PolicyUsageFilter")
    Marker = field("Marker")
    MaxItems = field("MaxItems")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEntitiesForPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEntitiesForPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PolicyGroup:
    boto3_raw_data: "type_defs.PolicyGroupTypeDef" = dataclasses.field()

    GroupName = field("GroupName")
    GroupId = field("GroupId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PolicyGroupTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PolicyGroupTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PolicyRole:
    boto3_raw_data: "type_defs.PolicyRoleTypeDef" = dataclasses.field()

    RoleName = field("RoleName")
    RoleId = field("RoleId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PolicyRoleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PolicyRoleTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PolicyUser:
    boto3_raw_data: "type_defs.PolicyUserTypeDef" = dataclasses.field()

    UserName = field("UserName")
    UserId = field("UserId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PolicyUserTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PolicyUserTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGroupPoliciesRequest:
    boto3_raw_data: "type_defs.ListGroupPoliciesRequestTypeDef" = dataclasses.field()

    GroupName = field("GroupName")
    Marker = field("Marker")
    MaxItems = field("MaxItems")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListGroupPoliciesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGroupPoliciesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGroupsForUserRequest:
    boto3_raw_data: "type_defs.ListGroupsForUserRequestTypeDef" = dataclasses.field()

    UserName = field("UserName")
    Marker = field("Marker")
    MaxItems = field("MaxItems")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListGroupsForUserRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGroupsForUserRequestTypeDef"]
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

    PathPrefix = field("PathPrefix")
    Marker = field("Marker")
    MaxItems = field("MaxItems")

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
class ListInstanceProfileTagsRequest:
    boto3_raw_data: "type_defs.ListInstanceProfileTagsRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceProfileName = field("InstanceProfileName")
    Marker = field("Marker")
    MaxItems = field("MaxItems")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListInstanceProfileTagsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInstanceProfileTagsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInstanceProfilesForRoleRequest:
    boto3_raw_data: "type_defs.ListInstanceProfilesForRoleRequestTypeDef" = (
        dataclasses.field()
    )

    RoleName = field("RoleName")
    Marker = field("Marker")
    MaxItems = field("MaxItems")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListInstanceProfilesForRoleRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInstanceProfilesForRoleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInstanceProfilesRequest:
    boto3_raw_data: "type_defs.ListInstanceProfilesRequestTypeDef" = dataclasses.field()

    PathPrefix = field("PathPrefix")
    Marker = field("Marker")
    MaxItems = field("MaxItems")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListInstanceProfilesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInstanceProfilesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMFADeviceTagsRequest:
    boto3_raw_data: "type_defs.ListMFADeviceTagsRequestTypeDef" = dataclasses.field()

    SerialNumber = field("SerialNumber")
    Marker = field("Marker")
    MaxItems = field("MaxItems")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMFADeviceTagsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMFADeviceTagsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMFADevicesRequest:
    boto3_raw_data: "type_defs.ListMFADevicesRequestTypeDef" = dataclasses.field()

    UserName = field("UserName")
    Marker = field("Marker")
    MaxItems = field("MaxItems")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMFADevicesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMFADevicesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MFADevice:
    boto3_raw_data: "type_defs.MFADeviceTypeDef" = dataclasses.field()

    UserName = field("UserName")
    SerialNumber = field("SerialNumber")
    EnableDate = field("EnableDate")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MFADeviceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MFADeviceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOpenIDConnectProviderTagsRequest:
    boto3_raw_data: "type_defs.ListOpenIDConnectProviderTagsRequestTypeDef" = (
        dataclasses.field()
    )

    OpenIDConnectProviderArn = field("OpenIDConnectProviderArn")
    Marker = field("Marker")
    MaxItems = field("MaxItems")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListOpenIDConnectProviderTagsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOpenIDConnectProviderTagsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpenIDConnectProviderListEntry:
    boto3_raw_data: "type_defs.OpenIDConnectProviderListEntryTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.OpenIDConnectProviderListEntryTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OpenIDConnectProviderListEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PolicyGrantingServiceAccess:
    boto3_raw_data: "type_defs.PolicyGrantingServiceAccessTypeDef" = dataclasses.field()

    PolicyName = field("PolicyName")
    PolicyType = field("PolicyType")
    PolicyArn = field("PolicyArn")
    EntityType = field("EntityType")
    EntityName = field("EntityName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PolicyGrantingServiceAccessTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PolicyGrantingServiceAccessTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPoliciesGrantingServiceAccessRequest:
    boto3_raw_data: "type_defs.ListPoliciesGrantingServiceAccessRequestTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    ServiceNamespaces = field("ServiceNamespaces")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListPoliciesGrantingServiceAccessRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPoliciesGrantingServiceAccessRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPoliciesRequest:
    boto3_raw_data: "type_defs.ListPoliciesRequestTypeDef" = dataclasses.field()

    Scope = field("Scope")
    OnlyAttached = field("OnlyAttached")
    PathPrefix = field("PathPrefix")
    PolicyUsageFilter = field("PolicyUsageFilter")
    Marker = field("Marker")
    MaxItems = field("MaxItems")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPoliciesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPoliciesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPolicyTagsRequest:
    boto3_raw_data: "type_defs.ListPolicyTagsRequestTypeDef" = dataclasses.field()

    PolicyArn = field("PolicyArn")
    Marker = field("Marker")
    MaxItems = field("MaxItems")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPolicyTagsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPolicyTagsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPolicyVersionsRequest:
    boto3_raw_data: "type_defs.ListPolicyVersionsRequestTypeDef" = dataclasses.field()

    PolicyArn = field("PolicyArn")
    Marker = field("Marker")
    MaxItems = field("MaxItems")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPolicyVersionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPolicyVersionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRolePoliciesRequest:
    boto3_raw_data: "type_defs.ListRolePoliciesRequestTypeDef" = dataclasses.field()

    RoleName = field("RoleName")
    Marker = field("Marker")
    MaxItems = field("MaxItems")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRolePoliciesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRolePoliciesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRoleTagsRequest:
    boto3_raw_data: "type_defs.ListRoleTagsRequestTypeDef" = dataclasses.field()

    RoleName = field("RoleName")
    Marker = field("Marker")
    MaxItems = field("MaxItems")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRoleTagsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRoleTagsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRolesRequest:
    boto3_raw_data: "type_defs.ListRolesRequestTypeDef" = dataclasses.field()

    PathPrefix = field("PathPrefix")
    Marker = field("Marker")
    MaxItems = field("MaxItems")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListRolesRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRolesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSAMLProviderTagsRequest:
    boto3_raw_data: "type_defs.ListSAMLProviderTagsRequestTypeDef" = dataclasses.field()

    SAMLProviderArn = field("SAMLProviderArn")
    Marker = field("Marker")
    MaxItems = field("MaxItems")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSAMLProviderTagsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSAMLProviderTagsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SAMLProviderListEntry:
    boto3_raw_data: "type_defs.SAMLProviderListEntryTypeDef" = dataclasses.field()

    Arn = field("Arn")
    ValidUntil = field("ValidUntil")
    CreateDate = field("CreateDate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SAMLProviderListEntryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SAMLProviderListEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSSHPublicKeysRequest:
    boto3_raw_data: "type_defs.ListSSHPublicKeysRequestTypeDef" = dataclasses.field()

    UserName = field("UserName")
    Marker = field("Marker")
    MaxItems = field("MaxItems")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSSHPublicKeysRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSSHPublicKeysRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SSHPublicKeyMetadata:
    boto3_raw_data: "type_defs.SSHPublicKeyMetadataTypeDef" = dataclasses.field()

    UserName = field("UserName")
    SSHPublicKeyId = field("SSHPublicKeyId")
    Status = field("Status")
    UploadDate = field("UploadDate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SSHPublicKeyMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SSHPublicKeyMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServerCertificateTagsRequest:
    boto3_raw_data: "type_defs.ListServerCertificateTagsRequestTypeDef" = (
        dataclasses.field()
    )

    ServerCertificateName = field("ServerCertificateName")
    Marker = field("Marker")
    MaxItems = field("MaxItems")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListServerCertificateTagsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServerCertificateTagsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServerCertificatesRequest:
    boto3_raw_data: "type_defs.ListServerCertificatesRequestTypeDef" = (
        dataclasses.field()
    )

    PathPrefix = field("PathPrefix")
    Marker = field("Marker")
    MaxItems = field("MaxItems")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListServerCertificatesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServerCertificatesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServerCertificateMetadata:
    boto3_raw_data: "type_defs.ServerCertificateMetadataTypeDef" = dataclasses.field()

    Path = field("Path")
    ServerCertificateName = field("ServerCertificateName")
    ServerCertificateId = field("ServerCertificateId")
    Arn = field("Arn")
    UploadDate = field("UploadDate")
    Expiration = field("Expiration")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ServerCertificateMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServerCertificateMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServiceSpecificCredentialsRequest:
    boto3_raw_data: "type_defs.ListServiceSpecificCredentialsRequestTypeDef" = (
        dataclasses.field()
    )

    UserName = field("UserName")
    ServiceName = field("ServiceName")
    AllUsers = field("AllUsers")
    Marker = field("Marker")
    MaxItems = field("MaxItems")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListServiceSpecificCredentialsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServiceSpecificCredentialsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceSpecificCredentialMetadata:
    boto3_raw_data: "type_defs.ServiceSpecificCredentialMetadataTypeDef" = (
        dataclasses.field()
    )

    UserName = field("UserName")
    Status = field("Status")
    CreateDate = field("CreateDate")
    ServiceSpecificCredentialId = field("ServiceSpecificCredentialId")
    ServiceName = field("ServiceName")
    ServiceUserName = field("ServiceUserName")
    ServiceCredentialAlias = field("ServiceCredentialAlias")
    ExpirationDate = field("ExpirationDate")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ServiceSpecificCredentialMetadataTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceSpecificCredentialMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSigningCertificatesRequest:
    boto3_raw_data: "type_defs.ListSigningCertificatesRequestTypeDef" = (
        dataclasses.field()
    )

    UserName = field("UserName")
    Marker = field("Marker")
    MaxItems = field("MaxItems")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListSigningCertificatesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSigningCertificatesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SigningCertificate:
    boto3_raw_data: "type_defs.SigningCertificateTypeDef" = dataclasses.field()

    UserName = field("UserName")
    CertificateId = field("CertificateId")
    CertificateBody = field("CertificateBody")
    Status = field("Status")
    UploadDate = field("UploadDate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SigningCertificateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SigningCertificateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListUserPoliciesRequest:
    boto3_raw_data: "type_defs.ListUserPoliciesRequestTypeDef" = dataclasses.field()

    UserName = field("UserName")
    Marker = field("Marker")
    MaxItems = field("MaxItems")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListUserPoliciesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListUserPoliciesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListUserTagsRequest:
    boto3_raw_data: "type_defs.ListUserTagsRequestTypeDef" = dataclasses.field()

    UserName = field("UserName")
    Marker = field("Marker")
    MaxItems = field("MaxItems")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListUserTagsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListUserTagsRequestTypeDef"]
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

    PathPrefix = field("PathPrefix")
    Marker = field("Marker")
    MaxItems = field("MaxItems")

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
class ListVirtualMFADevicesRequest:
    boto3_raw_data: "type_defs.ListVirtualMFADevicesRequestTypeDef" = (
        dataclasses.field()
    )

    AssignmentStatus = field("AssignmentStatus")
    Marker = field("Marker")
    MaxItems = field("MaxItems")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListVirtualMFADevicesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVirtualMFADevicesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PolicyDocumentStatement:
    boto3_raw_data: "type_defs.PolicyDocumentStatementTypeDef" = dataclasses.field()

    Effect = field("Effect")
    Resource = field("Resource")
    Sid = field("Sid")
    Action = field("Action")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PolicyDocumentStatementTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PolicyDocumentStatementTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Position:
    boto3_raw_data: "type_defs.PositionTypeDef" = dataclasses.field()

    Line = field("Line")
    Column = field("Column")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PositionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PositionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutGroupPolicyRequestGroupCreatePolicy:
    boto3_raw_data: "type_defs.PutGroupPolicyRequestGroupCreatePolicyTypeDef" = (
        dataclasses.field()
    )

    PolicyName = field("PolicyName")
    PolicyDocument = field("PolicyDocument")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutGroupPolicyRequestGroupCreatePolicyTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutGroupPolicyRequestGroupCreatePolicyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutGroupPolicyRequestGroupPolicyPut:
    boto3_raw_data: "type_defs.PutGroupPolicyRequestGroupPolicyPutTypeDef" = (
        dataclasses.field()
    )

    PolicyDocument = field("PolicyDocument")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutGroupPolicyRequestGroupPolicyPutTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutGroupPolicyRequestGroupPolicyPutTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutGroupPolicyRequest:
    boto3_raw_data: "type_defs.PutGroupPolicyRequestTypeDef" = dataclasses.field()

    GroupName = field("GroupName")
    PolicyName = field("PolicyName")
    PolicyDocument = field("PolicyDocument")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutGroupPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutGroupPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutRolePermissionsBoundaryRequest:
    boto3_raw_data: "type_defs.PutRolePermissionsBoundaryRequestTypeDef" = (
        dataclasses.field()
    )

    RoleName = field("RoleName")
    PermissionsBoundary = field("PermissionsBoundary")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutRolePermissionsBoundaryRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutRolePermissionsBoundaryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutRolePolicyRequestRolePolicyPut:
    boto3_raw_data: "type_defs.PutRolePolicyRequestRolePolicyPutTypeDef" = (
        dataclasses.field()
    )

    PolicyDocument = field("PolicyDocument")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutRolePolicyRequestRolePolicyPutTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutRolePolicyRequestRolePolicyPutTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutRolePolicyRequest:
    boto3_raw_data: "type_defs.PutRolePolicyRequestTypeDef" = dataclasses.field()

    RoleName = field("RoleName")
    PolicyName = field("PolicyName")
    PolicyDocument = field("PolicyDocument")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutRolePolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutRolePolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutUserPermissionsBoundaryRequest:
    boto3_raw_data: "type_defs.PutUserPermissionsBoundaryRequestTypeDef" = (
        dataclasses.field()
    )

    UserName = field("UserName")
    PermissionsBoundary = field("PermissionsBoundary")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutUserPermissionsBoundaryRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutUserPermissionsBoundaryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutUserPolicyRequest:
    boto3_raw_data: "type_defs.PutUserPolicyRequestTypeDef" = dataclasses.field()

    UserName = field("UserName")
    PolicyName = field("PolicyName")
    PolicyDocument = field("PolicyDocument")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutUserPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutUserPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutUserPolicyRequestUserCreatePolicy:
    boto3_raw_data: "type_defs.PutUserPolicyRequestUserCreatePolicyTypeDef" = (
        dataclasses.field()
    )

    PolicyName = field("PolicyName")
    PolicyDocument = field("PolicyDocument")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutUserPolicyRequestUserCreatePolicyTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutUserPolicyRequestUserCreatePolicyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutUserPolicyRequestUserPolicyPut:
    boto3_raw_data: "type_defs.PutUserPolicyRequestUserPolicyPutTypeDef" = (
        dataclasses.field()
    )

    PolicyDocument = field("PolicyDocument")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutUserPolicyRequestUserPolicyPutTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutUserPolicyRequestUserPolicyPutTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveClientIDFromOpenIDConnectProviderRequest:
    boto3_raw_data: (
        "type_defs.RemoveClientIDFromOpenIDConnectProviderRequestTypeDef"
    ) = dataclasses.field()

    OpenIDConnectProviderArn = field("OpenIDConnectProviderArn")
    ClientID = field("ClientID")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RemoveClientIDFromOpenIDConnectProviderRequestTypeDef"
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
                "type_defs.RemoveClientIDFromOpenIDConnectProviderRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveRoleFromInstanceProfileRequestInstanceProfileRemoveRole:
    boto3_raw_data: (
        "type_defs.RemoveRoleFromInstanceProfileRequestInstanceProfileRemoveRoleTypeDef"
    ) = dataclasses.field()

    RoleName = field("RoleName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RemoveRoleFromInstanceProfileRequestInstanceProfileRemoveRoleTypeDef"
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
                "type_defs.RemoveRoleFromInstanceProfileRequestInstanceProfileRemoveRoleTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveRoleFromInstanceProfileRequest:
    boto3_raw_data: "type_defs.RemoveRoleFromInstanceProfileRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceProfileName = field("InstanceProfileName")
    RoleName = field("RoleName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RemoveRoleFromInstanceProfileRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveRoleFromInstanceProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveUserFromGroupRequestGroupRemoveUser:
    boto3_raw_data: "type_defs.RemoveUserFromGroupRequestGroupRemoveUserTypeDef" = (
        dataclasses.field()
    )

    UserName = field("UserName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RemoveUserFromGroupRequestGroupRemoveUserTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveUserFromGroupRequestGroupRemoveUserTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveUserFromGroupRequest:
    boto3_raw_data: "type_defs.RemoveUserFromGroupRequestTypeDef" = dataclasses.field()

    GroupName = field("GroupName")
    UserName = field("UserName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RemoveUserFromGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveUserFromGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveUserFromGroupRequestUserRemoveGroup:
    boto3_raw_data: "type_defs.RemoveUserFromGroupRequestUserRemoveGroupTypeDef" = (
        dataclasses.field()
    )

    GroupName = field("GroupName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RemoveUserFromGroupRequestUserRemoveGroupTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveUserFromGroupRequestUserRemoveGroupTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResetServiceSpecificCredentialRequest:
    boto3_raw_data: "type_defs.ResetServiceSpecificCredentialRequestTypeDef" = (
        dataclasses.field()
    )

    ServiceSpecificCredentialId = field("ServiceSpecificCredentialId")
    UserName = field("UserName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ResetServiceSpecificCredentialRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResetServiceSpecificCredentialRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResyncMFADeviceRequestMfaDeviceResync:
    boto3_raw_data: "type_defs.ResyncMFADeviceRequestMfaDeviceResyncTypeDef" = (
        dataclasses.field()
    )

    AuthenticationCode1 = field("AuthenticationCode1")
    AuthenticationCode2 = field("AuthenticationCode2")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ResyncMFADeviceRequestMfaDeviceResyncTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResyncMFADeviceRequestMfaDeviceResyncTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResyncMFADeviceRequest:
    boto3_raw_data: "type_defs.ResyncMFADeviceRequestTypeDef" = dataclasses.field()

    UserName = field("UserName")
    SerialNumber = field("SerialNumber")
    AuthenticationCode1 = field("AuthenticationCode1")
    AuthenticationCode2 = field("AuthenticationCode2")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResyncMFADeviceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResyncMFADeviceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RoleLastUsed:
    boto3_raw_data: "type_defs.RoleLastUsedTypeDef" = dataclasses.field()

    LastUsedDate = field("LastUsedDate")
    Region = field("Region")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RoleLastUsedTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RoleLastUsedTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TrackedActionLastAccessed:
    boto3_raw_data: "type_defs.TrackedActionLastAccessedTypeDef" = dataclasses.field()

    ActionName = field("ActionName")
    LastAccessedEntity = field("LastAccessedEntity")
    LastAccessedTime = field("LastAccessedTime")
    LastAccessedRegion = field("LastAccessedRegion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TrackedActionLastAccessedTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TrackedActionLastAccessedTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetDefaultPolicyVersionRequest:
    boto3_raw_data: "type_defs.SetDefaultPolicyVersionRequestTypeDef" = (
        dataclasses.field()
    )

    PolicyArn = field("PolicyArn")
    VersionId = field("VersionId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SetDefaultPolicyVersionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetDefaultPolicyVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetSecurityTokenServicePreferencesRequest:
    boto3_raw_data: "type_defs.SetSecurityTokenServicePreferencesRequestTypeDef" = (
        dataclasses.field()
    )

    GlobalEndpointTokenVersion = field("GlobalEndpointTokenVersion")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SetSecurityTokenServicePreferencesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetSecurityTokenServicePreferencesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UntagInstanceProfileRequest:
    boto3_raw_data: "type_defs.UntagInstanceProfileRequestTypeDef" = dataclasses.field()

    InstanceProfileName = field("InstanceProfileName")
    TagKeys = field("TagKeys")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UntagInstanceProfileRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UntagInstanceProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UntagMFADeviceRequest:
    boto3_raw_data: "type_defs.UntagMFADeviceRequestTypeDef" = dataclasses.field()

    SerialNumber = field("SerialNumber")
    TagKeys = field("TagKeys")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UntagMFADeviceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UntagMFADeviceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UntagOpenIDConnectProviderRequest:
    boto3_raw_data: "type_defs.UntagOpenIDConnectProviderRequestTypeDef" = (
        dataclasses.field()
    )

    OpenIDConnectProviderArn = field("OpenIDConnectProviderArn")
    TagKeys = field("TagKeys")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UntagOpenIDConnectProviderRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UntagOpenIDConnectProviderRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UntagPolicyRequest:
    boto3_raw_data: "type_defs.UntagPolicyRequestTypeDef" = dataclasses.field()

    PolicyArn = field("PolicyArn")
    TagKeys = field("TagKeys")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UntagPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UntagPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UntagRoleRequest:
    boto3_raw_data: "type_defs.UntagRoleRequestTypeDef" = dataclasses.field()

    RoleName = field("RoleName")
    TagKeys = field("TagKeys")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UntagRoleRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UntagRoleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UntagSAMLProviderRequest:
    boto3_raw_data: "type_defs.UntagSAMLProviderRequestTypeDef" = dataclasses.field()

    SAMLProviderArn = field("SAMLProviderArn")
    TagKeys = field("TagKeys")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UntagSAMLProviderRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UntagSAMLProviderRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UntagServerCertificateRequest:
    boto3_raw_data: "type_defs.UntagServerCertificateRequestTypeDef" = (
        dataclasses.field()
    )

    ServerCertificateName = field("ServerCertificateName")
    TagKeys = field("TagKeys")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UntagServerCertificateRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UntagServerCertificateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UntagUserRequest:
    boto3_raw_data: "type_defs.UntagUserRequestTypeDef" = dataclasses.field()

    UserName = field("UserName")
    TagKeys = field("TagKeys")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UntagUserRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UntagUserRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAccessKeyRequestAccessKeyActivate:
    boto3_raw_data: "type_defs.UpdateAccessKeyRequestAccessKeyActivateTypeDef" = (
        dataclasses.field()
    )

    Status = field("Status")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateAccessKeyRequestAccessKeyActivateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAccessKeyRequestAccessKeyActivateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAccessKeyRequestAccessKeyDeactivate:
    boto3_raw_data: "type_defs.UpdateAccessKeyRequestAccessKeyDeactivateTypeDef" = (
        dataclasses.field()
    )

    Status = field("Status")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateAccessKeyRequestAccessKeyDeactivateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAccessKeyRequestAccessKeyDeactivateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAccessKeyRequestAccessKeyPairActivate:
    boto3_raw_data: "type_defs.UpdateAccessKeyRequestAccessKeyPairActivateTypeDef" = (
        dataclasses.field()
    )

    Status = field("Status")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateAccessKeyRequestAccessKeyPairActivateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAccessKeyRequestAccessKeyPairActivateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAccessKeyRequestAccessKeyPairDeactivate:
    boto3_raw_data: "type_defs.UpdateAccessKeyRequestAccessKeyPairDeactivateTypeDef" = (
        dataclasses.field()
    )

    Status = field("Status")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateAccessKeyRequestAccessKeyPairDeactivateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAccessKeyRequestAccessKeyPairDeactivateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAccessKeyRequest:
    boto3_raw_data: "type_defs.UpdateAccessKeyRequestTypeDef" = dataclasses.field()

    AccessKeyId = field("AccessKeyId")
    Status = field("Status")
    UserName = field("UserName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAccessKeyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAccessKeyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAccountPasswordPolicyRequestAccountPasswordPolicyUpdate:
    boto3_raw_data: (
        "type_defs.UpdateAccountPasswordPolicyRequestAccountPasswordPolicyUpdateTypeDef"
    ) = dataclasses.field()

    MinimumPasswordLength = field("MinimumPasswordLength")
    RequireSymbols = field("RequireSymbols")
    RequireNumbers = field("RequireNumbers")
    RequireUppercaseCharacters = field("RequireUppercaseCharacters")
    RequireLowercaseCharacters = field("RequireLowercaseCharacters")
    AllowUsersToChangePassword = field("AllowUsersToChangePassword")
    MaxPasswordAge = field("MaxPasswordAge")
    PasswordReusePrevention = field("PasswordReusePrevention")
    HardExpiry = field("HardExpiry")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateAccountPasswordPolicyRequestAccountPasswordPolicyUpdateTypeDef"
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
                "type_defs.UpdateAccountPasswordPolicyRequestAccountPasswordPolicyUpdateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAccountPasswordPolicyRequestServiceResourceCreateAccountPasswordPolicy:
    boto3_raw_data: "type_defs.UpdateAccountPasswordPolicyRequestServiceResourceCreateAccountPasswordPolicyTypeDef" = (dataclasses.field())

    MinimumPasswordLength = field("MinimumPasswordLength")
    RequireSymbols = field("RequireSymbols")
    RequireNumbers = field("RequireNumbers")
    RequireUppercaseCharacters = field("RequireUppercaseCharacters")
    RequireLowercaseCharacters = field("RequireLowercaseCharacters")
    AllowUsersToChangePassword = field("AllowUsersToChangePassword")
    MaxPasswordAge = field("MaxPasswordAge")
    PasswordReusePrevention = field("PasswordReusePrevention")
    HardExpiry = field("HardExpiry")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateAccountPasswordPolicyRequestServiceResourceCreateAccountPasswordPolicyTypeDef"
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
                "type_defs.UpdateAccountPasswordPolicyRequestServiceResourceCreateAccountPasswordPolicyTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAccountPasswordPolicyRequest:
    boto3_raw_data: "type_defs.UpdateAccountPasswordPolicyRequestTypeDef" = (
        dataclasses.field()
    )

    MinimumPasswordLength = field("MinimumPasswordLength")
    RequireSymbols = field("RequireSymbols")
    RequireNumbers = field("RequireNumbers")
    RequireUppercaseCharacters = field("RequireUppercaseCharacters")
    RequireLowercaseCharacters = field("RequireLowercaseCharacters")
    AllowUsersToChangePassword = field("AllowUsersToChangePassword")
    MaxPasswordAge = field("MaxPasswordAge")
    PasswordReusePrevention = field("PasswordReusePrevention")
    HardExpiry = field("HardExpiry")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateAccountPasswordPolicyRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAccountPasswordPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAssumeRolePolicyRequestAssumeRolePolicyUpdate:
    boto3_raw_data: (
        "type_defs.UpdateAssumeRolePolicyRequestAssumeRolePolicyUpdateTypeDef"
    ) = dataclasses.field()

    PolicyDocument = field("PolicyDocument")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateAssumeRolePolicyRequestAssumeRolePolicyUpdateTypeDef"
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
                "type_defs.UpdateAssumeRolePolicyRequestAssumeRolePolicyUpdateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAssumeRolePolicyRequest:
    boto3_raw_data: "type_defs.UpdateAssumeRolePolicyRequestTypeDef" = (
        dataclasses.field()
    )

    RoleName = field("RoleName")
    PolicyDocument = field("PolicyDocument")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateAssumeRolePolicyRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAssumeRolePolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateGroupRequestGroupUpdate:
    boto3_raw_data: "type_defs.UpdateGroupRequestGroupUpdateTypeDef" = (
        dataclasses.field()
    )

    NewPath = field("NewPath")
    NewGroupName = field("NewGroupName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateGroupRequestGroupUpdateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateGroupRequestGroupUpdateTypeDef"]
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

    GroupName = field("GroupName")
    NewPath = field("NewPath")
    NewGroupName = field("NewGroupName")

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
class UpdateLoginProfileRequestLoginProfileUpdate:
    boto3_raw_data: "type_defs.UpdateLoginProfileRequestLoginProfileUpdateTypeDef" = (
        dataclasses.field()
    )

    Password = field("Password")
    PasswordResetRequired = field("PasswordResetRequired")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateLoginProfileRequestLoginProfileUpdateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateLoginProfileRequestLoginProfileUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateLoginProfileRequest:
    boto3_raw_data: "type_defs.UpdateLoginProfileRequestTypeDef" = dataclasses.field()

    UserName = field("UserName")
    Password = field("Password")
    PasswordResetRequired = field("PasswordResetRequired")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateLoginProfileRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateLoginProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateOpenIDConnectProviderThumbprintRequest:
    boto3_raw_data: "type_defs.UpdateOpenIDConnectProviderThumbprintRequestTypeDef" = (
        dataclasses.field()
    )

    OpenIDConnectProviderArn = field("OpenIDConnectProviderArn")
    ThumbprintList = field("ThumbprintList")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateOpenIDConnectProviderThumbprintRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateOpenIDConnectProviderThumbprintRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRoleDescriptionRequest:
    boto3_raw_data: "type_defs.UpdateRoleDescriptionRequestTypeDef" = (
        dataclasses.field()
    )

    RoleName = field("RoleName")
    Description = field("Description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateRoleDescriptionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRoleDescriptionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRoleRequest:
    boto3_raw_data: "type_defs.UpdateRoleRequestTypeDef" = dataclasses.field()

    RoleName = field("RoleName")
    Description = field("Description")
    MaxSessionDuration = field("MaxSessionDuration")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateRoleRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRoleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSAMLProviderRequestSamlProviderUpdate:
    boto3_raw_data: "type_defs.UpdateSAMLProviderRequestSamlProviderUpdateTypeDef" = (
        dataclasses.field()
    )

    SAMLMetadataDocument = field("SAMLMetadataDocument")
    AssertionEncryptionMode = field("AssertionEncryptionMode")
    AddPrivateKey = field("AddPrivateKey")
    RemovePrivateKey = field("RemovePrivateKey")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateSAMLProviderRequestSamlProviderUpdateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSAMLProviderRequestSamlProviderUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSAMLProviderRequest:
    boto3_raw_data: "type_defs.UpdateSAMLProviderRequestTypeDef" = dataclasses.field()

    SAMLProviderArn = field("SAMLProviderArn")
    SAMLMetadataDocument = field("SAMLMetadataDocument")
    AssertionEncryptionMode = field("AssertionEncryptionMode")
    AddPrivateKey = field("AddPrivateKey")
    RemovePrivateKey = field("RemovePrivateKey")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateSAMLProviderRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSAMLProviderRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSSHPublicKeyRequest:
    boto3_raw_data: "type_defs.UpdateSSHPublicKeyRequestTypeDef" = dataclasses.field()

    UserName = field("UserName")
    SSHPublicKeyId = field("SSHPublicKeyId")
    Status = field("Status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateSSHPublicKeyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSSHPublicKeyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateServerCertificateRequestServerCertificateUpdate:
    boto3_raw_data: (
        "type_defs.UpdateServerCertificateRequestServerCertificateUpdateTypeDef"
    ) = dataclasses.field()

    NewPath = field("NewPath")
    NewServerCertificateName = field("NewServerCertificateName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateServerCertificateRequestServerCertificateUpdateTypeDef"
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
                "type_defs.UpdateServerCertificateRequestServerCertificateUpdateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateServerCertificateRequest:
    boto3_raw_data: "type_defs.UpdateServerCertificateRequestTypeDef" = (
        dataclasses.field()
    )

    ServerCertificateName = field("ServerCertificateName")
    NewPath = field("NewPath")
    NewServerCertificateName = field("NewServerCertificateName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateServerCertificateRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateServerCertificateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateServiceSpecificCredentialRequest:
    boto3_raw_data: "type_defs.UpdateServiceSpecificCredentialRequestTypeDef" = (
        dataclasses.field()
    )

    ServiceSpecificCredentialId = field("ServiceSpecificCredentialId")
    Status = field("Status")
    UserName = field("UserName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateServiceSpecificCredentialRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateServiceSpecificCredentialRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSigningCertificateRequestSigningCertificateActivate:
    boto3_raw_data: (
        "type_defs.UpdateSigningCertificateRequestSigningCertificateActivateTypeDef"
    ) = dataclasses.field()

    Status = field("Status")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateSigningCertificateRequestSigningCertificateActivateTypeDef"
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
                "type_defs.UpdateSigningCertificateRequestSigningCertificateActivateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSigningCertificateRequestSigningCertificateDeactivate:
    boto3_raw_data: (
        "type_defs.UpdateSigningCertificateRequestSigningCertificateDeactivateTypeDef"
    ) = dataclasses.field()

    Status = field("Status")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateSigningCertificateRequestSigningCertificateDeactivateTypeDef"
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
                "type_defs.UpdateSigningCertificateRequestSigningCertificateDeactivateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSigningCertificateRequest:
    boto3_raw_data: "type_defs.UpdateSigningCertificateRequestTypeDef" = (
        dataclasses.field()
    )

    CertificateId = field("CertificateId")
    Status = field("Status")
    UserName = field("UserName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateSigningCertificateRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSigningCertificateRequestTypeDef"]
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

    UserName = field("UserName")
    NewPath = field("NewPath")
    NewUserName = field("NewUserName")

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


@dataclasses.dataclass(frozen=True)
class UpdateUserRequestUserUpdate:
    boto3_raw_data: "type_defs.UpdateUserRequestUserUpdateTypeDef" = dataclasses.field()

    NewPath = field("NewPath")
    NewUserName = field("NewUserName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateUserRequestUserUpdateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateUserRequestUserUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UploadSSHPublicKeyRequest:
    boto3_raw_data: "type_defs.UploadSSHPublicKeyRequestTypeDef" = dataclasses.field()

    UserName = field("UserName")
    SSHPublicKeyBody = field("SSHPublicKeyBody")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UploadSSHPublicKeyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UploadSSHPublicKeyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UploadSigningCertificateRequestServiceResourceCreateSigningCertificate:
    boto3_raw_data: "type_defs.UploadSigningCertificateRequestServiceResourceCreateSigningCertificateTypeDef" = (dataclasses.field())

    CertificateBody = field("CertificateBody")
    UserName = field("UserName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UploadSigningCertificateRequestServiceResourceCreateSigningCertificateTypeDef"
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
                "type_defs.UploadSigningCertificateRequestServiceResourceCreateSigningCertificateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UploadSigningCertificateRequest:
    boto3_raw_data: "type_defs.UploadSigningCertificateRequestTypeDef" = (
        dataclasses.field()
    )

    CertificateBody = field("CertificateBody")
    UserName = field("UserName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UploadSigningCertificateRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UploadSigningCertificateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SimulateCustomPolicyRequest:
    boto3_raw_data: "type_defs.SimulateCustomPolicyRequestTypeDef" = dataclasses.field()

    PolicyInputList = field("PolicyInputList")
    ActionNames = field("ActionNames")
    PermissionsBoundaryPolicyInputList = field("PermissionsBoundaryPolicyInputList")
    ResourceArns = field("ResourceArns")
    ResourcePolicy = field("ResourcePolicy")
    ResourceOwner = field("ResourceOwner")
    CallerArn = field("CallerArn")

    @cached_property
    def ContextEntries(self):  # pragma: no cover
        return ContextEntry.make_many(self.boto3_raw_data["ContextEntries"])

    ResourceHandlingOption = field("ResourceHandlingOption")
    MaxItems = field("MaxItems")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SimulateCustomPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SimulateCustomPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SimulatePrincipalPolicyRequest:
    boto3_raw_data: "type_defs.SimulatePrincipalPolicyRequestTypeDef" = (
        dataclasses.field()
    )

    PolicySourceArn = field("PolicySourceArn")
    ActionNames = field("ActionNames")
    PolicyInputList = field("PolicyInputList")
    PermissionsBoundaryPolicyInputList = field("PermissionsBoundaryPolicyInputList")
    ResourceArns = field("ResourceArns")
    ResourcePolicy = field("ResourcePolicy")
    ResourceOwner = field("ResourceOwner")
    CallerArn = field("CallerArn")

    @cached_property
    def ContextEntries(self):  # pragma: no cover
        return ContextEntry.make_many(self.boto3_raw_data["ContextEntries"])

    ResourceHandlingOption = field("ResourceHandlingOption")
    MaxItems = field("MaxItems")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SimulatePrincipalPolicyRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SimulatePrincipalPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAccessKeyResponse:
    boto3_raw_data: "type_defs.CreateAccessKeyResponseTypeDef" = dataclasses.field()

    @cached_property
    def AccessKey(self):  # pragma: no cover
        return AccessKey.make_one(self.boto3_raw_data["AccessKey"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAccessKeyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAccessKeyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteServiceLinkedRoleResponse:
    boto3_raw_data: "type_defs.DeleteServiceLinkedRoleResponseTypeDef" = (
        dataclasses.field()
    )

    DeletionTaskId = field("DeletionTaskId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteServiceLinkedRoleResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteServiceLinkedRoleResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisableOrganizationsRootCredentialsManagementResponse:
    boto3_raw_data: (
        "type_defs.DisableOrganizationsRootCredentialsManagementResponseTypeDef"
    ) = dataclasses.field()

    OrganizationId = field("OrganizationId")
    EnabledFeatures = field("EnabledFeatures")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisableOrganizationsRootCredentialsManagementResponseTypeDef"
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
                "type_defs.DisableOrganizationsRootCredentialsManagementResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisableOrganizationsRootSessionsResponse:
    boto3_raw_data: "type_defs.DisableOrganizationsRootSessionsResponseTypeDef" = (
        dataclasses.field()
    )

    OrganizationId = field("OrganizationId")
    EnabledFeatures = field("EnabledFeatures")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisableOrganizationsRootSessionsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisableOrganizationsRootSessionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EmptyResponseMetadata:
    boto3_raw_data: "type_defs.EmptyResponseMetadataTypeDef" = dataclasses.field()

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EmptyResponseMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EmptyResponseMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnableOrganizationsRootCredentialsManagementResponse:
    boto3_raw_data: (
        "type_defs.EnableOrganizationsRootCredentialsManagementResponseTypeDef"
    ) = dataclasses.field()

    OrganizationId = field("OrganizationId")
    EnabledFeatures = field("EnabledFeatures")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.EnableOrganizationsRootCredentialsManagementResponseTypeDef"
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
                "type_defs.EnableOrganizationsRootCredentialsManagementResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnableOrganizationsRootSessionsResponse:
    boto3_raw_data: "type_defs.EnableOrganizationsRootSessionsResponseTypeDef" = (
        dataclasses.field()
    )

    OrganizationId = field("OrganizationId")
    EnabledFeatures = field("EnabledFeatures")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.EnableOrganizationsRootSessionsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnableOrganizationsRootSessionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GenerateCredentialReportResponse:
    boto3_raw_data: "type_defs.GenerateCredentialReportResponseTypeDef" = (
        dataclasses.field()
    )

    State = field("State")
    Description = field("Description")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GenerateCredentialReportResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GenerateCredentialReportResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GenerateOrganizationsAccessReportResponse:
    boto3_raw_data: "type_defs.GenerateOrganizationsAccessReportResponseTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GenerateOrganizationsAccessReportResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GenerateOrganizationsAccessReportResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GenerateServiceLastAccessedDetailsResponse:
    boto3_raw_data: "type_defs.GenerateServiceLastAccessedDetailsResponseTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GenerateServiceLastAccessedDetailsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GenerateServiceLastAccessedDetailsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAccessKeyLastUsedResponse:
    boto3_raw_data: "type_defs.GetAccessKeyLastUsedResponseTypeDef" = (
        dataclasses.field()
    )

    UserName = field("UserName")

    @cached_property
    def AccessKeyLastUsed(self):  # pragma: no cover
        return AccessKeyLastUsed.make_one(self.boto3_raw_data["AccessKeyLastUsed"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAccessKeyLastUsedResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAccessKeyLastUsedResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAccountSummaryResponse:
    boto3_raw_data: "type_defs.GetAccountSummaryResponseTypeDef" = dataclasses.field()

    SummaryMap = field("SummaryMap")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAccountSummaryResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAccountSummaryResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetContextKeysForPolicyResponse:
    boto3_raw_data: "type_defs.GetContextKeysForPolicyResponseTypeDef" = (
        dataclasses.field()
    )

    ContextKeyNames = field("ContextKeyNames")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetContextKeysForPolicyResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetContextKeysForPolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCredentialReportResponse:
    boto3_raw_data: "type_defs.GetCredentialReportResponseTypeDef" = dataclasses.field()

    Content = field("Content")
    ReportFormat = field("ReportFormat")
    GeneratedTime = field("GeneratedTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCredentialReportResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCredentialReportResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMFADeviceResponse:
    boto3_raw_data: "type_defs.GetMFADeviceResponseTypeDef" = dataclasses.field()

    UserName = field("UserName")
    SerialNumber = field("SerialNumber")
    EnableDate = field("EnableDate")
    Certifications = field("Certifications")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMFADeviceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMFADeviceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAccessKeysResponse:
    boto3_raw_data: "type_defs.ListAccessKeysResponseTypeDef" = dataclasses.field()

    @cached_property
    def AccessKeyMetadata(self):  # pragma: no cover
        return AccessKeyMetadata.make_many(self.boto3_raw_data["AccessKeyMetadata"])

    IsTruncated = field("IsTruncated")
    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAccessKeysResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAccessKeysResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAccountAliasesResponse:
    boto3_raw_data: "type_defs.ListAccountAliasesResponseTypeDef" = dataclasses.field()

    AccountAliases = field("AccountAliases")
    IsTruncated = field("IsTruncated")
    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAccountAliasesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAccountAliasesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAttachedGroupPoliciesResponse:
    boto3_raw_data: "type_defs.ListAttachedGroupPoliciesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AttachedPolicies(self):  # pragma: no cover
        return AttachedPolicy.make_many(self.boto3_raw_data["AttachedPolicies"])

    IsTruncated = field("IsTruncated")
    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAttachedGroupPoliciesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAttachedGroupPoliciesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAttachedRolePoliciesResponse:
    boto3_raw_data: "type_defs.ListAttachedRolePoliciesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AttachedPolicies(self):  # pragma: no cover
        return AttachedPolicy.make_many(self.boto3_raw_data["AttachedPolicies"])

    IsTruncated = field("IsTruncated")
    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAttachedRolePoliciesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAttachedRolePoliciesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAttachedUserPoliciesResponse:
    boto3_raw_data: "type_defs.ListAttachedUserPoliciesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AttachedPolicies(self):  # pragma: no cover
        return AttachedPolicy.make_many(self.boto3_raw_data["AttachedPolicies"])

    IsTruncated = field("IsTruncated")
    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAttachedUserPoliciesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAttachedUserPoliciesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGroupPoliciesResponse:
    boto3_raw_data: "type_defs.ListGroupPoliciesResponseTypeDef" = dataclasses.field()

    PolicyNames = field("PolicyNames")
    IsTruncated = field("IsTruncated")
    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListGroupPoliciesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGroupPoliciesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOrganizationsFeaturesResponse:
    boto3_raw_data: "type_defs.ListOrganizationsFeaturesResponseTypeDef" = (
        dataclasses.field()
    )

    OrganizationId = field("OrganizationId")
    EnabledFeatures = field("EnabledFeatures")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListOrganizationsFeaturesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOrganizationsFeaturesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRolePoliciesResponse:
    boto3_raw_data: "type_defs.ListRolePoliciesResponseTypeDef" = dataclasses.field()

    PolicyNames = field("PolicyNames")
    IsTruncated = field("IsTruncated")
    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRolePoliciesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRolePoliciesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListUserPoliciesResponse:
    boto3_raw_data: "type_defs.ListUserPoliciesResponseTypeDef" = dataclasses.field()

    PolicyNames = field("PolicyNames")
    IsTruncated = field("IsTruncated")
    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListUserPoliciesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListUserPoliciesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSAMLProviderResponse:
    boto3_raw_data: "type_defs.UpdateSAMLProviderResponseTypeDef" = dataclasses.field()

    SAMLProviderArn = field("SAMLProviderArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateSAMLProviderResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSAMLProviderResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateGroupResponse:
    boto3_raw_data: "type_defs.CreateGroupResponseTypeDef" = dataclasses.field()

    @cached_property
    def Group(self):  # pragma: no cover
        return Group.make_one(self.boto3_raw_data["Group"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateGroupResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGroupsForUserResponse:
    boto3_raw_data: "type_defs.ListGroupsForUserResponseTypeDef" = dataclasses.field()

    @cached_property
    def Groups(self):  # pragma: no cover
        return Group.make_many(self.boto3_raw_data["Groups"])

    IsTruncated = field("IsTruncated")
    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListGroupsForUserResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGroupsForUserResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGroupsResponse:
    boto3_raw_data: "type_defs.ListGroupsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Groups(self):  # pragma: no cover
        return Group.make_many(self.boto3_raw_data["Groups"])

    IsTruncated = field("IsTruncated")
    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListGroupsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGroupsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateInstanceProfileRequestServiceResourceCreateInstanceProfile:
    boto3_raw_data: "type_defs.CreateInstanceProfileRequestServiceResourceCreateInstanceProfileTypeDef" = (dataclasses.field())

    InstanceProfileName = field("InstanceProfileName")
    Path = field("Path")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateInstanceProfileRequestServiceResourceCreateInstanceProfileTypeDef"
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
                "type_defs.CreateInstanceProfileRequestServiceResourceCreateInstanceProfileTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateInstanceProfileRequest:
    boto3_raw_data: "type_defs.CreateInstanceProfileRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceProfileName = field("InstanceProfileName")
    Path = field("Path")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateInstanceProfileRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateInstanceProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateOpenIDConnectProviderRequest:
    boto3_raw_data: "type_defs.CreateOpenIDConnectProviderRequestTypeDef" = (
        dataclasses.field()
    )

    Url = field("Url")
    ClientIDList = field("ClientIDList")
    ThumbprintList = field("ThumbprintList")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateOpenIDConnectProviderRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateOpenIDConnectProviderRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateOpenIDConnectProviderResponse:
    boto3_raw_data: "type_defs.CreateOpenIDConnectProviderResponseTypeDef" = (
        dataclasses.field()
    )

    OpenIDConnectProviderArn = field("OpenIDConnectProviderArn")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateOpenIDConnectProviderResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateOpenIDConnectProviderResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePolicyRequestServiceResourceCreatePolicy:
    boto3_raw_data: (
        "type_defs.CreatePolicyRequestServiceResourceCreatePolicyTypeDef"
    ) = dataclasses.field()

    PolicyName = field("PolicyName")
    PolicyDocument = field("PolicyDocument")
    Path = field("Path")
    Description = field("Description")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreatePolicyRequestServiceResourceCreatePolicyTypeDef"
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
                "type_defs.CreatePolicyRequestServiceResourceCreatePolicyTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePolicyRequest:
    boto3_raw_data: "type_defs.CreatePolicyRequestTypeDef" = dataclasses.field()

    PolicyName = field("PolicyName")
    PolicyDocument = field("PolicyDocument")
    Path = field("Path")
    Description = field("Description")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRoleRequestServiceResourceCreateRole:
    boto3_raw_data: "type_defs.CreateRoleRequestServiceResourceCreateRoleTypeDef" = (
        dataclasses.field()
    )

    RoleName = field("RoleName")
    AssumeRolePolicyDocument = field("AssumeRolePolicyDocument")
    Path = field("Path")
    Description = field("Description")
    MaxSessionDuration = field("MaxSessionDuration")
    PermissionsBoundary = field("PermissionsBoundary")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateRoleRequestServiceResourceCreateRoleTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRoleRequestServiceResourceCreateRoleTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRoleRequest:
    boto3_raw_data: "type_defs.CreateRoleRequestTypeDef" = dataclasses.field()

    RoleName = field("RoleName")
    AssumeRolePolicyDocument = field("AssumeRolePolicyDocument")
    Path = field("Path")
    Description = field("Description")
    MaxSessionDuration = field("MaxSessionDuration")
    PermissionsBoundary = field("PermissionsBoundary")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateRoleRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRoleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSAMLProviderRequestServiceResourceCreateSamlProvider:
    boto3_raw_data: (
        "type_defs.CreateSAMLProviderRequestServiceResourceCreateSamlProviderTypeDef"
    ) = dataclasses.field()

    SAMLMetadataDocument = field("SAMLMetadataDocument")
    Name = field("Name")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    AssertionEncryptionMode = field("AssertionEncryptionMode")
    AddPrivateKey = field("AddPrivateKey")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateSAMLProviderRequestServiceResourceCreateSamlProviderTypeDef"
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
                "type_defs.CreateSAMLProviderRequestServiceResourceCreateSamlProviderTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSAMLProviderRequest:
    boto3_raw_data: "type_defs.CreateSAMLProviderRequestTypeDef" = dataclasses.field()

    SAMLMetadataDocument = field("SAMLMetadataDocument")
    Name = field("Name")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    AssertionEncryptionMode = field("AssertionEncryptionMode")
    AddPrivateKey = field("AddPrivateKey")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSAMLProviderRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSAMLProviderRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSAMLProviderResponse:
    boto3_raw_data: "type_defs.CreateSAMLProviderResponseTypeDef" = dataclasses.field()

    SAMLProviderArn = field("SAMLProviderArn")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSAMLProviderResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSAMLProviderResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateUserRequestServiceResourceCreateUser:
    boto3_raw_data: "type_defs.CreateUserRequestServiceResourceCreateUserTypeDef" = (
        dataclasses.field()
    )

    UserName = field("UserName")
    Path = field("Path")
    PermissionsBoundary = field("PermissionsBoundary")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateUserRequestServiceResourceCreateUserTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateUserRequestServiceResourceCreateUserTypeDef"]
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

    UserName = field("UserName")
    Path = field("Path")
    PermissionsBoundary = field("PermissionsBoundary")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

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
class CreateUserRequestUserCreate:
    boto3_raw_data: "type_defs.CreateUserRequestUserCreateTypeDef" = dataclasses.field()

    Path = field("Path")
    PermissionsBoundary = field("PermissionsBoundary")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateUserRequestUserCreateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateUserRequestUserCreateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateVirtualMFADeviceRequestServiceResourceCreateVirtualMfaDevice:
    boto3_raw_data: "type_defs.CreateVirtualMFADeviceRequestServiceResourceCreateVirtualMfaDeviceTypeDef" = (dataclasses.field())

    VirtualMFADeviceName = field("VirtualMFADeviceName")
    Path = field("Path")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateVirtualMFADeviceRequestServiceResourceCreateVirtualMfaDeviceTypeDef"
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
                "type_defs.CreateVirtualMFADeviceRequestServiceResourceCreateVirtualMfaDeviceTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateVirtualMFADeviceRequest:
    boto3_raw_data: "type_defs.CreateVirtualMFADeviceRequestTypeDef" = (
        dataclasses.field()
    )

    VirtualMFADeviceName = field("VirtualMFADeviceName")
    Path = field("Path")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateVirtualMFADeviceRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateVirtualMFADeviceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetOpenIDConnectProviderResponse:
    boto3_raw_data: "type_defs.GetOpenIDConnectProviderResponseTypeDef" = (
        dataclasses.field()
    )

    Url = field("Url")
    ClientIDList = field("ClientIDList")
    ThumbprintList = field("ThumbprintList")
    CreateDate = field("CreateDate")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetOpenIDConnectProviderResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetOpenIDConnectProviderResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInstanceProfileTagsResponse:
    boto3_raw_data: "type_defs.ListInstanceProfileTagsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    IsTruncated = field("IsTruncated")
    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListInstanceProfileTagsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInstanceProfileTagsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMFADeviceTagsResponse:
    boto3_raw_data: "type_defs.ListMFADeviceTagsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    IsTruncated = field("IsTruncated")
    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMFADeviceTagsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMFADeviceTagsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOpenIDConnectProviderTagsResponse:
    boto3_raw_data: "type_defs.ListOpenIDConnectProviderTagsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    IsTruncated = field("IsTruncated")
    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListOpenIDConnectProviderTagsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOpenIDConnectProviderTagsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPolicyTagsResponse:
    boto3_raw_data: "type_defs.ListPolicyTagsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    IsTruncated = field("IsTruncated")
    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPolicyTagsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPolicyTagsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRoleTagsResponse:
    boto3_raw_data: "type_defs.ListRoleTagsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    IsTruncated = field("IsTruncated")
    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRoleTagsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRoleTagsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSAMLProviderTagsResponse:
    boto3_raw_data: "type_defs.ListSAMLProviderTagsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    IsTruncated = field("IsTruncated")
    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSAMLProviderTagsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSAMLProviderTagsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServerCertificateTagsResponse:
    boto3_raw_data: "type_defs.ListServerCertificateTagsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    IsTruncated = field("IsTruncated")
    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListServerCertificateTagsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServerCertificateTagsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListUserTagsResponse:
    boto3_raw_data: "type_defs.ListUserTagsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    IsTruncated = field("IsTruncated")
    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListUserTagsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListUserTagsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Policy:
    boto3_raw_data: "type_defs.PolicyTypeDef" = dataclasses.field()

    PolicyName = field("PolicyName")
    PolicyId = field("PolicyId")
    Arn = field("Arn")
    Path = field("Path")
    DefaultVersionId = field("DefaultVersionId")
    AttachmentCount = field("AttachmentCount")
    PermissionsBoundaryUsageCount = field("PermissionsBoundaryUsageCount")
    IsAttachable = field("IsAttachable")
    Description = field("Description")
    CreateDate = field("CreateDate")
    UpdateDate = field("UpdateDate")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PolicyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PolicyTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagInstanceProfileRequest:
    boto3_raw_data: "type_defs.TagInstanceProfileRequestTypeDef" = dataclasses.field()

    InstanceProfileName = field("InstanceProfileName")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TagInstanceProfileRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TagInstanceProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagMFADeviceRequest:
    boto3_raw_data: "type_defs.TagMFADeviceRequestTypeDef" = dataclasses.field()

    SerialNumber = field("SerialNumber")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TagMFADeviceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TagMFADeviceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagOpenIDConnectProviderRequest:
    boto3_raw_data: "type_defs.TagOpenIDConnectProviderRequestTypeDef" = (
        dataclasses.field()
    )

    OpenIDConnectProviderArn = field("OpenIDConnectProviderArn")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.TagOpenIDConnectProviderRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TagOpenIDConnectProviderRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagPolicyRequest:
    boto3_raw_data: "type_defs.TagPolicyRequestTypeDef" = dataclasses.field()

    PolicyArn = field("PolicyArn")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TagPolicyRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TagPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagRoleRequest:
    boto3_raw_data: "type_defs.TagRoleRequestTypeDef" = dataclasses.field()

    RoleName = field("RoleName")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TagRoleRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TagRoleRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagSAMLProviderRequest:
    boto3_raw_data: "type_defs.TagSAMLProviderRequestTypeDef" = dataclasses.field()

    SAMLProviderArn = field("SAMLProviderArn")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TagSAMLProviderRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TagSAMLProviderRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagServerCertificateRequest:
    boto3_raw_data: "type_defs.TagServerCertificateRequestTypeDef" = dataclasses.field()

    ServerCertificateName = field("ServerCertificateName")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TagServerCertificateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TagServerCertificateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagUserRequest:
    boto3_raw_data: "type_defs.TagUserRequestTypeDef" = dataclasses.field()

    UserName = field("UserName")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TagUserRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TagUserRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UploadServerCertificateRequestServiceResourceCreateServerCertificate:
    boto3_raw_data: "type_defs.UploadServerCertificateRequestServiceResourceCreateServerCertificateTypeDef" = (dataclasses.field())

    ServerCertificateName = field("ServerCertificateName")
    CertificateBody = field("CertificateBody")
    PrivateKey = field("PrivateKey")
    Path = field("Path")
    CertificateChain = field("CertificateChain")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UploadServerCertificateRequestServiceResourceCreateServerCertificateTypeDef"
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
                "type_defs.UploadServerCertificateRequestServiceResourceCreateServerCertificateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UploadServerCertificateRequest:
    boto3_raw_data: "type_defs.UploadServerCertificateRequestTypeDef" = (
        dataclasses.field()
    )

    ServerCertificateName = field("ServerCertificateName")
    CertificateBody = field("CertificateBody")
    PrivateKey = field("PrivateKey")
    Path = field("Path")
    CertificateChain = field("CertificateChain")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UploadServerCertificateRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UploadServerCertificateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class User:
    boto3_raw_data: "type_defs.UserTypeDef" = dataclasses.field()

    Path = field("Path")
    UserName = field("UserName")
    UserId = field("UserId")
    Arn = field("Arn")
    CreateDate = field("CreateDate")
    PasswordLastUsed = field("PasswordLastUsed")

    @cached_property
    def PermissionsBoundary(self):  # pragma: no cover
        return AttachedPermissionsBoundary.make_one(
            self.boto3_raw_data["PermissionsBoundary"]
        )

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

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
class CreateLoginProfileResponse:
    boto3_raw_data: "type_defs.CreateLoginProfileResponseTypeDef" = dataclasses.field()

    @cached_property
    def LoginProfile(self):  # pragma: no cover
        return LoginProfile.make_one(self.boto3_raw_data["LoginProfile"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateLoginProfileResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLoginProfileResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLoginProfileResponse:
    boto3_raw_data: "type_defs.GetLoginProfileResponseTypeDef" = dataclasses.field()

    @cached_property
    def LoginProfile(self):  # pragma: no cover
        return LoginProfile.make_one(self.boto3_raw_data["LoginProfile"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetLoginProfileResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLoginProfileResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateServiceSpecificCredentialResponse:
    boto3_raw_data: "type_defs.CreateServiceSpecificCredentialResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ServiceSpecificCredential(self):  # pragma: no cover
        return ServiceSpecificCredential.make_one(
            self.boto3_raw_data["ServiceSpecificCredential"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateServiceSpecificCredentialResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateServiceSpecificCredentialResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResetServiceSpecificCredentialResponse:
    boto3_raw_data: "type_defs.ResetServiceSpecificCredentialResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ServiceSpecificCredential(self):  # pragma: no cover
        return ServiceSpecificCredential.make_one(
            self.boto3_raw_data["ServiceSpecificCredential"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ResetServiceSpecificCredentialResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResetServiceSpecificCredentialResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletionTaskFailureReasonType:
    boto3_raw_data: "type_defs.DeletionTaskFailureReasonTypeTypeDef" = (
        dataclasses.field()
    )

    Reason = field("Reason")

    @cached_property
    def RoleUsageList(self):  # pragma: no cover
        return RoleUsageType.make_many(self.boto3_raw_data["RoleUsageList"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeletionTaskFailureReasonTypeTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletionTaskFailureReasonTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EntityDetails:
    boto3_raw_data: "type_defs.EntityDetailsTypeDef" = dataclasses.field()

    @cached_property
    def EntityInfo(self):  # pragma: no cover
        return EntityInfo.make_one(self.boto3_raw_data["EntityInfo"])

    LastAuthenticated = field("LastAuthenticated")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EntityDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EntityDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetOrganizationsAccessReportResponse:
    boto3_raw_data: "type_defs.GetOrganizationsAccessReportResponseTypeDef" = (
        dataclasses.field()
    )

    JobStatus = field("JobStatus")
    JobCreationDate = field("JobCreationDate")
    JobCompletionDate = field("JobCompletionDate")
    NumberOfServicesAccessible = field("NumberOfServicesAccessible")
    NumberOfServicesNotAccessed = field("NumberOfServicesNotAccessed")

    @cached_property
    def AccessDetails(self):  # pragma: no cover
        return AccessDetail.make_many(self.boto3_raw_data["AccessDetails"])

    IsTruncated = field("IsTruncated")
    Marker = field("Marker")

    @cached_property
    def ErrorDetails(self):  # pragma: no cover
        return ErrorDetails.make_one(self.boto3_raw_data["ErrorDetails"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetOrganizationsAccessReportResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetOrganizationsAccessReportResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAccountAuthorizationDetailsRequestPaginate:
    boto3_raw_data: "type_defs.GetAccountAuthorizationDetailsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    Filter = field("Filter")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetAccountAuthorizationDetailsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAccountAuthorizationDetailsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetGroupRequestPaginate:
    boto3_raw_data: "type_defs.GetGroupRequestPaginateTypeDef" = dataclasses.field()

    GroupName = field("GroupName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetGroupRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetGroupRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAccessKeysRequestPaginate:
    boto3_raw_data: "type_defs.ListAccessKeysRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    UserName = field("UserName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAccessKeysRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAccessKeysRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAccountAliasesRequestPaginate:
    boto3_raw_data: "type_defs.ListAccountAliasesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAccountAliasesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAccountAliasesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAttachedGroupPoliciesRequestPaginate:
    boto3_raw_data: "type_defs.ListAttachedGroupPoliciesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    GroupName = field("GroupName")
    PathPrefix = field("PathPrefix")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAttachedGroupPoliciesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAttachedGroupPoliciesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAttachedRolePoliciesRequestPaginate:
    boto3_raw_data: "type_defs.ListAttachedRolePoliciesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    RoleName = field("RoleName")
    PathPrefix = field("PathPrefix")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAttachedRolePoliciesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAttachedRolePoliciesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAttachedUserPoliciesRequestPaginate:
    boto3_raw_data: "type_defs.ListAttachedUserPoliciesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    UserName = field("UserName")
    PathPrefix = field("PathPrefix")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAttachedUserPoliciesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAttachedUserPoliciesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEntitiesForPolicyRequestPaginate:
    boto3_raw_data: "type_defs.ListEntitiesForPolicyRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    PolicyArn = field("PolicyArn")
    EntityFilter = field("EntityFilter")
    PathPrefix = field("PathPrefix")
    PolicyUsageFilter = field("PolicyUsageFilter")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListEntitiesForPolicyRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEntitiesForPolicyRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGroupPoliciesRequestPaginate:
    boto3_raw_data: "type_defs.ListGroupPoliciesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    GroupName = field("GroupName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListGroupPoliciesRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGroupPoliciesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGroupsForUserRequestPaginate:
    boto3_raw_data: "type_defs.ListGroupsForUserRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    UserName = field("UserName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListGroupsForUserRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGroupsForUserRequestPaginateTypeDef"]
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

    PathPrefix = field("PathPrefix")

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
class ListInstanceProfileTagsRequestPaginate:
    boto3_raw_data: "type_defs.ListInstanceProfileTagsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    InstanceProfileName = field("InstanceProfileName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListInstanceProfileTagsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInstanceProfileTagsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInstanceProfilesForRoleRequestPaginate:
    boto3_raw_data: "type_defs.ListInstanceProfilesForRoleRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    RoleName = field("RoleName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListInstanceProfilesForRoleRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInstanceProfilesForRoleRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInstanceProfilesRequestPaginate:
    boto3_raw_data: "type_defs.ListInstanceProfilesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    PathPrefix = field("PathPrefix")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListInstanceProfilesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInstanceProfilesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMFADeviceTagsRequestPaginate:
    boto3_raw_data: "type_defs.ListMFADeviceTagsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    SerialNumber = field("SerialNumber")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListMFADeviceTagsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMFADeviceTagsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMFADevicesRequestPaginate:
    boto3_raw_data: "type_defs.ListMFADevicesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    UserName = field("UserName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListMFADevicesRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMFADevicesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOpenIDConnectProviderTagsRequestPaginate:
    boto3_raw_data: "type_defs.ListOpenIDConnectProviderTagsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    OpenIDConnectProviderArn = field("OpenIDConnectProviderArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListOpenIDConnectProviderTagsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOpenIDConnectProviderTagsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPoliciesRequestPaginate:
    boto3_raw_data: "type_defs.ListPoliciesRequestPaginateTypeDef" = dataclasses.field()

    Scope = field("Scope")
    OnlyAttached = field("OnlyAttached")
    PathPrefix = field("PathPrefix")
    PolicyUsageFilter = field("PolicyUsageFilter")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPoliciesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPoliciesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPolicyTagsRequestPaginate:
    boto3_raw_data: "type_defs.ListPolicyTagsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    PolicyArn = field("PolicyArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListPolicyTagsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPolicyTagsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPolicyVersionsRequestPaginate:
    boto3_raw_data: "type_defs.ListPolicyVersionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    PolicyArn = field("PolicyArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListPolicyVersionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPolicyVersionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRolePoliciesRequestPaginate:
    boto3_raw_data: "type_defs.ListRolePoliciesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    RoleName = field("RoleName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListRolePoliciesRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRolePoliciesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRoleTagsRequestPaginate:
    boto3_raw_data: "type_defs.ListRoleTagsRequestPaginateTypeDef" = dataclasses.field()

    RoleName = field("RoleName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRoleTagsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRoleTagsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRolesRequestPaginate:
    boto3_raw_data: "type_defs.ListRolesRequestPaginateTypeDef" = dataclasses.field()

    PathPrefix = field("PathPrefix")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRolesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRolesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSAMLProviderTagsRequestPaginate:
    boto3_raw_data: "type_defs.ListSAMLProviderTagsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    SAMLProviderArn = field("SAMLProviderArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSAMLProviderTagsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSAMLProviderTagsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSSHPublicKeysRequestPaginate:
    boto3_raw_data: "type_defs.ListSSHPublicKeysRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    UserName = field("UserName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListSSHPublicKeysRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSSHPublicKeysRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServerCertificateTagsRequestPaginate:
    boto3_raw_data: "type_defs.ListServerCertificateTagsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ServerCertificateName = field("ServerCertificateName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListServerCertificateTagsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServerCertificateTagsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServerCertificatesRequestPaginate:
    boto3_raw_data: "type_defs.ListServerCertificatesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    PathPrefix = field("PathPrefix")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListServerCertificatesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServerCertificatesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSigningCertificatesRequestPaginate:
    boto3_raw_data: "type_defs.ListSigningCertificatesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    UserName = field("UserName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSigningCertificatesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSigningCertificatesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListUserPoliciesRequestPaginate:
    boto3_raw_data: "type_defs.ListUserPoliciesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    UserName = field("UserName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListUserPoliciesRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListUserPoliciesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListUserTagsRequestPaginate:
    boto3_raw_data: "type_defs.ListUserTagsRequestPaginateTypeDef" = dataclasses.field()

    UserName = field("UserName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListUserTagsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListUserTagsRequestPaginateTypeDef"]
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

    PathPrefix = field("PathPrefix")

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
class ListVirtualMFADevicesRequestPaginate:
    boto3_raw_data: "type_defs.ListVirtualMFADevicesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    AssignmentStatus = field("AssignmentStatus")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListVirtualMFADevicesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVirtualMFADevicesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SimulateCustomPolicyRequestPaginate:
    boto3_raw_data: "type_defs.SimulateCustomPolicyRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    PolicyInputList = field("PolicyInputList")
    ActionNames = field("ActionNames")
    PermissionsBoundaryPolicyInputList = field("PermissionsBoundaryPolicyInputList")
    ResourceArns = field("ResourceArns")
    ResourcePolicy = field("ResourcePolicy")
    ResourceOwner = field("ResourceOwner")
    CallerArn = field("CallerArn")

    @cached_property
    def ContextEntries(self):  # pragma: no cover
        return ContextEntry.make_many(self.boto3_raw_data["ContextEntries"])

    ResourceHandlingOption = field("ResourceHandlingOption")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SimulateCustomPolicyRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SimulateCustomPolicyRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SimulatePrincipalPolicyRequestPaginate:
    boto3_raw_data: "type_defs.SimulatePrincipalPolicyRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    PolicySourceArn = field("PolicySourceArn")
    ActionNames = field("ActionNames")
    PolicyInputList = field("PolicyInputList")
    PermissionsBoundaryPolicyInputList = field("PermissionsBoundaryPolicyInputList")
    ResourceArns = field("ResourceArns")
    ResourcePolicy = field("ResourcePolicy")
    ResourceOwner = field("ResourceOwner")
    CallerArn = field("CallerArn")

    @cached_property
    def ContextEntries(self):  # pragma: no cover
        return ContextEntry.make_many(self.boto3_raw_data["ContextEntries"])

    ResourceHandlingOption = field("ResourceHandlingOption")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SimulatePrincipalPolicyRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SimulatePrincipalPolicyRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAccountPasswordPolicyResponse:
    boto3_raw_data: "type_defs.GetAccountPasswordPolicyResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PasswordPolicy(self):  # pragma: no cover
        return PasswordPolicy.make_one(self.boto3_raw_data["PasswordPolicy"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetAccountPasswordPolicyResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAccountPasswordPolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetInstanceProfileRequestWait:
    boto3_raw_data: "type_defs.GetInstanceProfileRequestWaitTypeDef" = (
        dataclasses.field()
    )

    InstanceProfileName = field("InstanceProfileName")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetInstanceProfileRequestWaitTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetInstanceProfileRequestWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPolicyRequestWait:
    boto3_raw_data: "type_defs.GetPolicyRequestWaitTypeDef" = dataclasses.field()

    PolicyArn = field("PolicyArn")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetPolicyRequestWaitTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPolicyRequestWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRoleRequestWait:
    boto3_raw_data: "type_defs.GetRoleRequestWaitTypeDef" = dataclasses.field()

    RoleName = field("RoleName")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetRoleRequestWaitTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRoleRequestWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetUserRequestWait:
    boto3_raw_data: "type_defs.GetUserRequestWaitTypeDef" = dataclasses.field()

    UserName = field("UserName")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetUserRequestWaitTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetUserRequestWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSAMLProviderResponse:
    boto3_raw_data: "type_defs.GetSAMLProviderResponseTypeDef" = dataclasses.field()

    SAMLProviderUUID = field("SAMLProviderUUID")
    SAMLMetadataDocument = field("SAMLMetadataDocument")
    CreateDate = field("CreateDate")
    ValidUntil = field("ValidUntil")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    AssertionEncryptionMode = field("AssertionEncryptionMode")

    @cached_property
    def PrivateKeyList(self):  # pragma: no cover
        return SAMLPrivateKey.make_many(self.boto3_raw_data["PrivateKeyList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSAMLProviderResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSAMLProviderResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSSHPublicKeyResponse:
    boto3_raw_data: "type_defs.GetSSHPublicKeyResponseTypeDef" = dataclasses.field()

    @cached_property
    def SSHPublicKey(self):  # pragma: no cover
        return SSHPublicKey.make_one(self.boto3_raw_data["SSHPublicKey"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSSHPublicKeyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSSHPublicKeyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UploadSSHPublicKeyResponse:
    boto3_raw_data: "type_defs.UploadSSHPublicKeyResponseTypeDef" = dataclasses.field()

    @cached_property
    def SSHPublicKey(self):  # pragma: no cover
        return SSHPublicKey.make_one(self.boto3_raw_data["SSHPublicKey"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UploadSSHPublicKeyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UploadSSHPublicKeyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEntitiesForPolicyResponse:
    boto3_raw_data: "type_defs.ListEntitiesForPolicyResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PolicyGroups(self):  # pragma: no cover
        return PolicyGroup.make_many(self.boto3_raw_data["PolicyGroups"])

    @cached_property
    def PolicyUsers(self):  # pragma: no cover
        return PolicyUser.make_many(self.boto3_raw_data["PolicyUsers"])

    @cached_property
    def PolicyRoles(self):  # pragma: no cover
        return PolicyRole.make_many(self.boto3_raw_data["PolicyRoles"])

    IsTruncated = field("IsTruncated")
    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListEntitiesForPolicyResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEntitiesForPolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMFADevicesResponse:
    boto3_raw_data: "type_defs.ListMFADevicesResponseTypeDef" = dataclasses.field()

    @cached_property
    def MFADevices(self):  # pragma: no cover
        return MFADevice.make_many(self.boto3_raw_data["MFADevices"])

    IsTruncated = field("IsTruncated")
    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMFADevicesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMFADevicesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOpenIDConnectProvidersResponse:
    boto3_raw_data: "type_defs.ListOpenIDConnectProvidersResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def OpenIDConnectProviderList(self):  # pragma: no cover
        return OpenIDConnectProviderListEntry.make_many(
            self.boto3_raw_data["OpenIDConnectProviderList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListOpenIDConnectProvidersResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOpenIDConnectProvidersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPoliciesGrantingServiceAccessEntry:
    boto3_raw_data: "type_defs.ListPoliciesGrantingServiceAccessEntryTypeDef" = (
        dataclasses.field()
    )

    ServiceNamespace = field("ServiceNamespace")

    @cached_property
    def Policies(self):  # pragma: no cover
        return PolicyGrantingServiceAccess.make_many(self.boto3_raw_data["Policies"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListPoliciesGrantingServiceAccessEntryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPoliciesGrantingServiceAccessEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSAMLProvidersResponse:
    boto3_raw_data: "type_defs.ListSAMLProvidersResponseTypeDef" = dataclasses.field()

    @cached_property
    def SAMLProviderList(self):  # pragma: no cover
        return SAMLProviderListEntry.make_many(self.boto3_raw_data["SAMLProviderList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSAMLProvidersResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSAMLProvidersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSSHPublicKeysResponse:
    boto3_raw_data: "type_defs.ListSSHPublicKeysResponseTypeDef" = dataclasses.field()

    @cached_property
    def SSHPublicKeys(self):  # pragma: no cover
        return SSHPublicKeyMetadata.make_many(self.boto3_raw_data["SSHPublicKeys"])

    IsTruncated = field("IsTruncated")
    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSSHPublicKeysResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSSHPublicKeysResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServerCertificatesResponse:
    boto3_raw_data: "type_defs.ListServerCertificatesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ServerCertificateMetadataList(self):  # pragma: no cover
        return ServerCertificateMetadata.make_many(
            self.boto3_raw_data["ServerCertificateMetadataList"]
        )

    IsTruncated = field("IsTruncated")
    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListServerCertificatesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServerCertificatesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServerCertificate:
    boto3_raw_data: "type_defs.ServerCertificateTypeDef" = dataclasses.field()

    @cached_property
    def ServerCertificateMetadata(self):  # pragma: no cover
        return ServerCertificateMetadata.make_one(
            self.boto3_raw_data["ServerCertificateMetadata"]
        )

    CertificateBody = field("CertificateBody")
    CertificateChain = field("CertificateChain")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ServerCertificateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServerCertificateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UploadServerCertificateResponse:
    boto3_raw_data: "type_defs.UploadServerCertificateResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ServerCertificateMetadata(self):  # pragma: no cover
        return ServerCertificateMetadata.make_one(
            self.boto3_raw_data["ServerCertificateMetadata"]
        )

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UploadServerCertificateResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UploadServerCertificateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServiceSpecificCredentialsResponse:
    boto3_raw_data: "type_defs.ListServiceSpecificCredentialsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ServiceSpecificCredentials(self):  # pragma: no cover
        return ServiceSpecificCredentialMetadata.make_many(
            self.boto3_raw_data["ServiceSpecificCredentials"]
        )

    Marker = field("Marker")
    IsTruncated = field("IsTruncated")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListServiceSpecificCredentialsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServiceSpecificCredentialsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSigningCertificatesResponse:
    boto3_raw_data: "type_defs.ListSigningCertificatesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Certificates(self):  # pragma: no cover
        return SigningCertificate.make_many(self.boto3_raw_data["Certificates"])

    IsTruncated = field("IsTruncated")
    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListSigningCertificatesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSigningCertificatesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UploadSigningCertificateResponse:
    boto3_raw_data: "type_defs.UploadSigningCertificateResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Certificate(self):  # pragma: no cover
        return SigningCertificate.make_one(self.boto3_raw_data["Certificate"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UploadSigningCertificateResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UploadSigningCertificateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PolicyDocumentDict:
    boto3_raw_data: "type_defs.PolicyDocumentDictTypeDef" = dataclasses.field()

    Version = field("Version")

    @cached_property
    def Statement(self):  # pragma: no cover
        return PolicyDocumentStatement.make_many(self.boto3_raw_data["Statement"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PolicyDocumentDictTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PolicyDocumentDictTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Statement:
    boto3_raw_data: "type_defs.StatementTypeDef" = dataclasses.field()

    SourcePolicyId = field("SourcePolicyId")
    SourcePolicyType = field("SourcePolicyType")

    @cached_property
    def StartPosition(self):  # pragma: no cover
        return Position.make_one(self.boto3_raw_data["StartPosition"])

    @cached_property
    def EndPosition(self):  # pragma: no cover
        return Position.make_one(self.boto3_raw_data["EndPosition"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StatementTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StatementTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceLastAccessed:
    boto3_raw_data: "type_defs.ServiceLastAccessedTypeDef" = dataclasses.field()

    ServiceName = field("ServiceName")
    ServiceNamespace = field("ServiceNamespace")
    LastAuthenticated = field("LastAuthenticated")
    LastAuthenticatedEntity = field("LastAuthenticatedEntity")
    LastAuthenticatedRegion = field("LastAuthenticatedRegion")
    TotalAuthenticatedEntities = field("TotalAuthenticatedEntities")

    @cached_property
    def TrackedActionsLastAccessed(self):  # pragma: no cover
        return TrackedActionLastAccessed.make_many(
            self.boto3_raw_data["TrackedActionsLastAccessed"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ServiceLastAccessedTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceLastAccessedTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePolicyResponse:
    boto3_raw_data: "type_defs.CreatePolicyResponseTypeDef" = dataclasses.field()

    @cached_property
    def Policy(self):  # pragma: no cover
        return Policy.make_one(self.boto3_raw_data["Policy"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePolicyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPolicyResponse:
    boto3_raw_data: "type_defs.GetPolicyResponseTypeDef" = dataclasses.field()

    @cached_property
    def Policy(self):  # pragma: no cover
        return Policy.make_one(self.boto3_raw_data["Policy"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetPolicyResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPoliciesResponse:
    boto3_raw_data: "type_defs.ListPoliciesResponseTypeDef" = dataclasses.field()

    @cached_property
    def Policies(self):  # pragma: no cover
        return Policy.make_many(self.boto3_raw_data["Policies"])

    IsTruncated = field("IsTruncated")
    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPoliciesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPoliciesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateUserResponse:
    boto3_raw_data: "type_defs.CreateUserResponseTypeDef" = dataclasses.field()

    @cached_property
    def User(self):  # pragma: no cover
        return User.make_one(self.boto3_raw_data["User"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateUserResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateUserResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetGroupResponse:
    boto3_raw_data: "type_defs.GetGroupResponseTypeDef" = dataclasses.field()

    @cached_property
    def Group(self):  # pragma: no cover
        return Group.make_one(self.boto3_raw_data["Group"])

    @cached_property
    def Users(self):  # pragma: no cover
        return User.make_many(self.boto3_raw_data["Users"])

    IsTruncated = field("IsTruncated")
    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetGroupResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetUserResponse:
    boto3_raw_data: "type_defs.GetUserResponseTypeDef" = dataclasses.field()

    @cached_property
    def User(self):  # pragma: no cover
        return User.make_one(self.boto3_raw_data["User"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetUserResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetUserResponseTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListUsersResponse:
    boto3_raw_data: "type_defs.ListUsersResponseTypeDef" = dataclasses.field()

    @cached_property
    def Users(self):  # pragma: no cover
        return User.make_many(self.boto3_raw_data["Users"])

    IsTruncated = field("IsTruncated")
    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListUsersResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListUsersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VirtualMFADevice:
    boto3_raw_data: "type_defs.VirtualMFADeviceTypeDef" = dataclasses.field()

    SerialNumber = field("SerialNumber")
    Base32StringSeed = field("Base32StringSeed")
    QRCodePNG = field("QRCodePNG")

    @cached_property
    def User(self):  # pragma: no cover
        return User.make_one(self.boto3_raw_data["User"])

    EnableDate = field("EnableDate")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VirtualMFADeviceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VirtualMFADeviceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetServiceLinkedRoleDeletionStatusResponse:
    boto3_raw_data: "type_defs.GetServiceLinkedRoleDeletionStatusResponseTypeDef" = (
        dataclasses.field()
    )

    Status = field("Status")

    @cached_property
    def Reason(self):  # pragma: no cover
        return DeletionTaskFailureReasonType.make_one(self.boto3_raw_data["Reason"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetServiceLinkedRoleDeletionStatusResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetServiceLinkedRoleDeletionStatusResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetServiceLastAccessedDetailsWithEntitiesResponse:
    boto3_raw_data: (
        "type_defs.GetServiceLastAccessedDetailsWithEntitiesResponseTypeDef"
    ) = dataclasses.field()

    JobStatus = field("JobStatus")
    JobCreationDate = field("JobCreationDate")
    JobCompletionDate = field("JobCompletionDate")

    @cached_property
    def EntityDetailsList(self):  # pragma: no cover
        return EntityDetails.make_many(self.boto3_raw_data["EntityDetailsList"])

    IsTruncated = field("IsTruncated")
    Marker = field("Marker")

    @cached_property
    def Error(self):  # pragma: no cover
        return ErrorDetails.make_one(self.boto3_raw_data["Error"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetServiceLastAccessedDetailsWithEntitiesResponseTypeDef"
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
                "type_defs.GetServiceLastAccessedDetailsWithEntitiesResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPoliciesGrantingServiceAccessResponse:
    boto3_raw_data: "type_defs.ListPoliciesGrantingServiceAccessResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PoliciesGrantingServiceAccess(self):  # pragma: no cover
        return ListPoliciesGrantingServiceAccessEntry.make_many(
            self.boto3_raw_data["PoliciesGrantingServiceAccess"]
        )

    IsTruncated = field("IsTruncated")
    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListPoliciesGrantingServiceAccessResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPoliciesGrantingServiceAccessResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetServerCertificateResponse:
    boto3_raw_data: "type_defs.GetServerCertificateResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ServerCertificate(self):  # pragma: no cover
        return ServerCertificate.make_one(self.boto3_raw_data["ServerCertificate"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetServerCertificateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetServerCertificateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceSpecificResult:
    boto3_raw_data: "type_defs.ResourceSpecificResultTypeDef" = dataclasses.field()

    EvalResourceName = field("EvalResourceName")
    EvalResourceDecision = field("EvalResourceDecision")

    @cached_property
    def MatchedStatements(self):  # pragma: no cover
        return Statement.make_many(self.boto3_raw_data["MatchedStatements"])

    MissingContextValues = field("MissingContextValues")
    EvalDecisionDetails = field("EvalDecisionDetails")

    @cached_property
    def PermissionsBoundaryDecisionDetail(self):  # pragma: no cover
        return PermissionsBoundaryDecisionDetail.make_one(
            self.boto3_raw_data["PermissionsBoundaryDecisionDetail"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResourceSpecificResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceSpecificResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetServiceLastAccessedDetailsResponse:
    boto3_raw_data: "type_defs.GetServiceLastAccessedDetailsResponseTypeDef" = (
        dataclasses.field()
    )

    JobStatus = field("JobStatus")
    JobType = field("JobType")
    JobCreationDate = field("JobCreationDate")

    @cached_property
    def ServicesLastAccessed(self):  # pragma: no cover
        return ServiceLastAccessed.make_many(
            self.boto3_raw_data["ServicesLastAccessed"]
        )

    JobCompletionDate = field("JobCompletionDate")
    IsTruncated = field("IsTruncated")
    Marker = field("Marker")

    @cached_property
    def Error(self):  # pragma: no cover
        return ErrorDetails.make_one(self.boto3_raw_data["Error"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetServiceLastAccessedDetailsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetServiceLastAccessedDetailsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateVirtualMFADeviceResponse:
    boto3_raw_data: "type_defs.CreateVirtualMFADeviceResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def VirtualMFADevice(self):  # pragma: no cover
        return VirtualMFADevice.make_one(self.boto3_raw_data["VirtualMFADevice"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateVirtualMFADeviceResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateVirtualMFADeviceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVirtualMFADevicesResponse:
    boto3_raw_data: "type_defs.ListVirtualMFADevicesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def VirtualMFADevices(self):  # pragma: no cover
        return VirtualMFADevice.make_many(self.boto3_raw_data["VirtualMFADevices"])

    IsTruncated = field("IsTruncated")
    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListVirtualMFADevicesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVirtualMFADevicesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetGroupPolicyResponse:
    boto3_raw_data: "type_defs.GetGroupPolicyResponseTypeDef" = dataclasses.field()

    GroupName = field("GroupName")
    PolicyName = field("PolicyName")
    PolicyDocument = field("PolicyDocument")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetGroupPolicyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetGroupPolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRolePolicyResponse:
    boto3_raw_data: "type_defs.GetRolePolicyResponseTypeDef" = dataclasses.field()

    RoleName = field("RoleName")
    PolicyName = field("PolicyName")
    PolicyDocument = field("PolicyDocument")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetRolePolicyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRolePolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetUserPolicyResponse:
    boto3_raw_data: "type_defs.GetUserPolicyResponseTypeDef" = dataclasses.field()

    UserName = field("UserName")
    PolicyName = field("PolicyName")
    PolicyDocument = field("PolicyDocument")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetUserPolicyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetUserPolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PolicyDetail:
    boto3_raw_data: "type_defs.PolicyDetailTypeDef" = dataclasses.field()

    PolicyName = field("PolicyName")
    PolicyDocument = field("PolicyDocument")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PolicyDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PolicyDetailTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PolicyVersion:
    boto3_raw_data: "type_defs.PolicyVersionTypeDef" = dataclasses.field()

    Document = field("Document")
    VersionId = field("VersionId")
    IsDefaultVersion = field("IsDefaultVersion")
    CreateDate = field("CreateDate")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PolicyVersionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PolicyVersionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Role:
    boto3_raw_data: "type_defs.RoleTypeDef" = dataclasses.field()

    Path = field("Path")
    RoleName = field("RoleName")
    RoleId = field("RoleId")
    Arn = field("Arn")
    CreateDate = field("CreateDate")
    AssumeRolePolicyDocument = field("AssumeRolePolicyDocument")
    Description = field("Description")
    MaxSessionDuration = field("MaxSessionDuration")

    @cached_property
    def PermissionsBoundary(self):  # pragma: no cover
        return AttachedPermissionsBoundary.make_one(
            self.boto3_raw_data["PermissionsBoundary"]
        )

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def RoleLastUsed(self):  # pragma: no cover
        return RoleLastUsed.make_one(self.boto3_raw_data["RoleLastUsed"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RoleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RoleTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvaluationResult:
    boto3_raw_data: "type_defs.EvaluationResultTypeDef" = dataclasses.field()

    EvalActionName = field("EvalActionName")
    EvalDecision = field("EvalDecision")
    EvalResourceName = field("EvalResourceName")

    @cached_property
    def MatchedStatements(self):  # pragma: no cover
        return Statement.make_many(self.boto3_raw_data["MatchedStatements"])

    MissingContextValues = field("MissingContextValues")

    @cached_property
    def OrganizationsDecisionDetail(self):  # pragma: no cover
        return OrganizationsDecisionDetail.make_one(
            self.boto3_raw_data["OrganizationsDecisionDetail"]
        )

    @cached_property
    def PermissionsBoundaryDecisionDetail(self):  # pragma: no cover
        return PermissionsBoundaryDecisionDetail.make_one(
            self.boto3_raw_data["PermissionsBoundaryDecisionDetail"]
        )

    EvalDecisionDetails = field("EvalDecisionDetails")

    @cached_property
    def ResourceSpecificResults(self):  # pragma: no cover
        return ResourceSpecificResult.make_many(
            self.boto3_raw_data["ResourceSpecificResults"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EvaluationResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EvaluationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GroupDetail:
    boto3_raw_data: "type_defs.GroupDetailTypeDef" = dataclasses.field()

    Path = field("Path")
    GroupName = field("GroupName")
    GroupId = field("GroupId")
    Arn = field("Arn")
    CreateDate = field("CreateDate")

    @cached_property
    def GroupPolicyList(self):  # pragma: no cover
        return PolicyDetail.make_many(self.boto3_raw_data["GroupPolicyList"])

    @cached_property
    def AttachedManagedPolicies(self):  # pragma: no cover
        return AttachedPolicy.make_many(self.boto3_raw_data["AttachedManagedPolicies"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GroupDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GroupDetailTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserDetail:
    boto3_raw_data: "type_defs.UserDetailTypeDef" = dataclasses.field()

    Path = field("Path")
    UserName = field("UserName")
    UserId = field("UserId")
    Arn = field("Arn")
    CreateDate = field("CreateDate")

    @cached_property
    def UserPolicyList(self):  # pragma: no cover
        return PolicyDetail.make_many(self.boto3_raw_data["UserPolicyList"])

    GroupList = field("GroupList")

    @cached_property
    def AttachedManagedPolicies(self):  # pragma: no cover
        return AttachedPolicy.make_many(self.boto3_raw_data["AttachedManagedPolicies"])

    @cached_property
    def PermissionsBoundary(self):  # pragma: no cover
        return AttachedPermissionsBoundary.make_one(
            self.boto3_raw_data["PermissionsBoundary"]
        )

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UserDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UserDetailTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePolicyVersionResponse:
    boto3_raw_data: "type_defs.CreatePolicyVersionResponseTypeDef" = dataclasses.field()

    @cached_property
    def PolicyVersion(self):  # pragma: no cover
        return PolicyVersion.make_one(self.boto3_raw_data["PolicyVersion"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePolicyVersionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePolicyVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPolicyVersionResponse:
    boto3_raw_data: "type_defs.GetPolicyVersionResponseTypeDef" = dataclasses.field()

    @cached_property
    def PolicyVersion(self):  # pragma: no cover
        return PolicyVersion.make_one(self.boto3_raw_data["PolicyVersion"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetPolicyVersionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPolicyVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPolicyVersionsResponse:
    boto3_raw_data: "type_defs.ListPolicyVersionsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Versions(self):  # pragma: no cover
        return PolicyVersion.make_many(self.boto3_raw_data["Versions"])

    IsTruncated = field("IsTruncated")
    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPolicyVersionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPolicyVersionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ManagedPolicyDetail:
    boto3_raw_data: "type_defs.ManagedPolicyDetailTypeDef" = dataclasses.field()

    PolicyName = field("PolicyName")
    PolicyId = field("PolicyId")
    Arn = field("Arn")
    Path = field("Path")
    DefaultVersionId = field("DefaultVersionId")
    AttachmentCount = field("AttachmentCount")
    PermissionsBoundaryUsageCount = field("PermissionsBoundaryUsageCount")
    IsAttachable = field("IsAttachable")
    Description = field("Description")
    CreateDate = field("CreateDate")
    UpdateDate = field("UpdateDate")

    @cached_property
    def PolicyVersionList(self):  # pragma: no cover
        return PolicyVersion.make_many(self.boto3_raw_data["PolicyVersionList"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ManagedPolicyDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ManagedPolicyDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRoleResponse:
    boto3_raw_data: "type_defs.CreateRoleResponseTypeDef" = dataclasses.field()

    @cached_property
    def Role(self):  # pragma: no cover
        return Role.make_one(self.boto3_raw_data["Role"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateRoleResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRoleResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateServiceLinkedRoleResponse:
    boto3_raw_data: "type_defs.CreateServiceLinkedRoleResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Role(self):  # pragma: no cover
        return Role.make_one(self.boto3_raw_data["Role"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateServiceLinkedRoleResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateServiceLinkedRoleResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRoleResponse:
    boto3_raw_data: "type_defs.GetRoleResponseTypeDef" = dataclasses.field()

    @cached_property
    def Role(self):  # pragma: no cover
        return Role.make_one(self.boto3_raw_data["Role"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetRoleResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetRoleResponseTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceProfile:
    boto3_raw_data: "type_defs.InstanceProfileTypeDef" = dataclasses.field()

    Path = field("Path")
    InstanceProfileName = field("InstanceProfileName")
    InstanceProfileId = field("InstanceProfileId")
    Arn = field("Arn")
    CreateDate = field("CreateDate")

    @cached_property
    def Roles(self):  # pragma: no cover
        return Role.make_many(self.boto3_raw_data["Roles"])

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InstanceProfileTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InstanceProfileTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRolesResponse:
    boto3_raw_data: "type_defs.ListRolesResponseTypeDef" = dataclasses.field()

    @cached_property
    def Roles(self):  # pragma: no cover
        return Role.make_many(self.boto3_raw_data["Roles"])

    IsTruncated = field("IsTruncated")
    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListRolesResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRolesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRoleDescriptionResponse:
    boto3_raw_data: "type_defs.UpdateRoleDescriptionResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Role(self):  # pragma: no cover
        return Role.make_one(self.boto3_raw_data["Role"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateRoleDescriptionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRoleDescriptionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SimulatePolicyResponse:
    boto3_raw_data: "type_defs.SimulatePolicyResponseTypeDef" = dataclasses.field()

    @cached_property
    def EvaluationResults(self):  # pragma: no cover
        return EvaluationResult.make_many(self.boto3_raw_data["EvaluationResults"])

    IsTruncated = field("IsTruncated")
    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SimulatePolicyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SimulatePolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateInstanceProfileResponse:
    boto3_raw_data: "type_defs.CreateInstanceProfileResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def InstanceProfile(self):  # pragma: no cover
        return InstanceProfile.make_one(self.boto3_raw_data["InstanceProfile"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateInstanceProfileResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateInstanceProfileResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetInstanceProfileResponse:
    boto3_raw_data: "type_defs.GetInstanceProfileResponseTypeDef" = dataclasses.field()

    @cached_property
    def InstanceProfile(self):  # pragma: no cover
        return InstanceProfile.make_one(self.boto3_raw_data["InstanceProfile"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetInstanceProfileResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetInstanceProfileResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInstanceProfilesForRoleResponse:
    boto3_raw_data: "type_defs.ListInstanceProfilesForRoleResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def InstanceProfiles(self):  # pragma: no cover
        return InstanceProfile.make_many(self.boto3_raw_data["InstanceProfiles"])

    IsTruncated = field("IsTruncated")
    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListInstanceProfilesForRoleResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInstanceProfilesForRoleResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInstanceProfilesResponse:
    boto3_raw_data: "type_defs.ListInstanceProfilesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def InstanceProfiles(self):  # pragma: no cover
        return InstanceProfile.make_many(self.boto3_raw_data["InstanceProfiles"])

    IsTruncated = field("IsTruncated")
    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListInstanceProfilesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInstanceProfilesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RoleDetail:
    boto3_raw_data: "type_defs.RoleDetailTypeDef" = dataclasses.field()

    Path = field("Path")
    RoleName = field("RoleName")
    RoleId = field("RoleId")
    Arn = field("Arn")
    CreateDate = field("CreateDate")
    AssumeRolePolicyDocument = field("AssumeRolePolicyDocument")

    @cached_property
    def InstanceProfileList(self):  # pragma: no cover
        return InstanceProfile.make_many(self.boto3_raw_data["InstanceProfileList"])

    @cached_property
    def RolePolicyList(self):  # pragma: no cover
        return PolicyDetail.make_many(self.boto3_raw_data["RolePolicyList"])

    @cached_property
    def AttachedManagedPolicies(self):  # pragma: no cover
        return AttachedPolicy.make_many(self.boto3_raw_data["AttachedManagedPolicies"])

    @cached_property
    def PermissionsBoundary(self):  # pragma: no cover
        return AttachedPermissionsBoundary.make_one(
            self.boto3_raw_data["PermissionsBoundary"]
        )

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def RoleLastUsed(self):  # pragma: no cover
        return RoleLastUsed.make_one(self.boto3_raw_data["RoleLastUsed"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RoleDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RoleDetailTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAccountAuthorizationDetailsResponse:
    boto3_raw_data: "type_defs.GetAccountAuthorizationDetailsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def UserDetailList(self):  # pragma: no cover
        return UserDetail.make_many(self.boto3_raw_data["UserDetailList"])

    @cached_property
    def GroupDetailList(self):  # pragma: no cover
        return GroupDetail.make_many(self.boto3_raw_data["GroupDetailList"])

    @cached_property
    def RoleDetailList(self):  # pragma: no cover
        return RoleDetail.make_many(self.boto3_raw_data["RoleDetailList"])

    @cached_property
    def Policies(self):  # pragma: no cover
        return ManagedPolicyDetail.make_many(self.boto3_raw_data["Policies"])

    IsTruncated = field("IsTruncated")
    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetAccountAuthorizationDetailsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAccountAuthorizationDetailsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
