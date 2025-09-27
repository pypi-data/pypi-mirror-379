# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_cognito_identity import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class CognitoIdentityProvider:
    boto3_raw_data: "type_defs.CognitoIdentityProviderTypeDef" = dataclasses.field()

    ProviderName = field("ProviderName")
    ClientId = field("ClientId")
    ServerSideTokenCheck = field("ServerSideTokenCheck")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CognitoIdentityProviderTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CognitoIdentityProviderTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Credentials:
    boto3_raw_data: "type_defs.CredentialsTypeDef" = dataclasses.field()

    AccessKeyId = field("AccessKeyId")
    SecretKey = field("SecretKey")
    SessionToken = field("SessionToken")
    Expiration = field("Expiration")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CredentialsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CredentialsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteIdentitiesInput:
    boto3_raw_data: "type_defs.DeleteIdentitiesInputTypeDef" = dataclasses.field()

    IdentityIdsToDelete = field("IdentityIdsToDelete")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteIdentitiesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteIdentitiesInputTypeDef"]
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
class UnprocessedIdentityId:
    boto3_raw_data: "type_defs.UnprocessedIdentityIdTypeDef" = dataclasses.field()

    IdentityId = field("IdentityId")
    ErrorCode = field("ErrorCode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UnprocessedIdentityIdTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UnprocessedIdentityIdTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteIdentityPoolInput:
    boto3_raw_data: "type_defs.DeleteIdentityPoolInputTypeDef" = dataclasses.field()

    IdentityPoolId = field("IdentityPoolId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteIdentityPoolInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteIdentityPoolInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeIdentityInput:
    boto3_raw_data: "type_defs.DescribeIdentityInputTypeDef" = dataclasses.field()

    IdentityId = field("IdentityId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeIdentityInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeIdentityInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeIdentityPoolInput:
    boto3_raw_data: "type_defs.DescribeIdentityPoolInputTypeDef" = dataclasses.field()

    IdentityPoolId = field("IdentityPoolId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeIdentityPoolInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeIdentityPoolInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCredentialsForIdentityInput:
    boto3_raw_data: "type_defs.GetCredentialsForIdentityInputTypeDef" = (
        dataclasses.field()
    )

    IdentityId = field("IdentityId")
    Logins = field("Logins")
    CustomRoleArn = field("CustomRoleArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetCredentialsForIdentityInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCredentialsForIdentityInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetIdInput:
    boto3_raw_data: "type_defs.GetIdInputTypeDef" = dataclasses.field()

    IdentityPoolId = field("IdentityPoolId")
    AccountId = field("AccountId")
    Logins = field("Logins")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetIdInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetIdInputTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetIdentityPoolRolesInput:
    boto3_raw_data: "type_defs.GetIdentityPoolRolesInputTypeDef" = dataclasses.field()

    IdentityPoolId = field("IdentityPoolId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetIdentityPoolRolesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetIdentityPoolRolesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetOpenIdTokenForDeveloperIdentityInput:
    boto3_raw_data: "type_defs.GetOpenIdTokenForDeveloperIdentityInputTypeDef" = (
        dataclasses.field()
    )

    IdentityPoolId = field("IdentityPoolId")
    Logins = field("Logins")
    IdentityId = field("IdentityId")
    PrincipalTags = field("PrincipalTags")
    TokenDuration = field("TokenDuration")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetOpenIdTokenForDeveloperIdentityInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetOpenIdTokenForDeveloperIdentityInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetOpenIdTokenInput:
    boto3_raw_data: "type_defs.GetOpenIdTokenInputTypeDef" = dataclasses.field()

    IdentityId = field("IdentityId")
    Logins = field("Logins")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetOpenIdTokenInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetOpenIdTokenInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPrincipalTagAttributeMapInput:
    boto3_raw_data: "type_defs.GetPrincipalTagAttributeMapInputTypeDef" = (
        dataclasses.field()
    )

    IdentityPoolId = field("IdentityPoolId")
    IdentityProviderName = field("IdentityProviderName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetPrincipalTagAttributeMapInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPrincipalTagAttributeMapInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IdentityDescription:
    boto3_raw_data: "type_defs.IdentityDescriptionTypeDef" = dataclasses.field()

    IdentityId = field("IdentityId")
    Logins = field("Logins")
    CreationDate = field("CreationDate")
    LastModifiedDate = field("LastModifiedDate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IdentityDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IdentityDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IdentityPoolShortDescription:
    boto3_raw_data: "type_defs.IdentityPoolShortDescriptionTypeDef" = (
        dataclasses.field()
    )

    IdentityPoolId = field("IdentityPoolId")
    IdentityPoolName = field("IdentityPoolName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IdentityPoolShortDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IdentityPoolShortDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIdentitiesInput:
    boto3_raw_data: "type_defs.ListIdentitiesInputTypeDef" = dataclasses.field()

    IdentityPoolId = field("IdentityPoolId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    HideDisabled = field("HideDisabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListIdentitiesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIdentitiesInputTypeDef"]
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
class ListIdentityPoolsInput:
    boto3_raw_data: "type_defs.ListIdentityPoolsInputTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListIdentityPoolsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIdentityPoolsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceInput:
    boto3_raw_data: "type_defs.ListTagsForResourceInputTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")

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
class LookupDeveloperIdentityInput:
    boto3_raw_data: "type_defs.LookupDeveloperIdentityInputTypeDef" = (
        dataclasses.field()
    )

    IdentityPoolId = field("IdentityPoolId")
    IdentityId = field("IdentityId")
    DeveloperUserIdentifier = field("DeveloperUserIdentifier")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LookupDeveloperIdentityInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LookupDeveloperIdentityInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MappingRule:
    boto3_raw_data: "type_defs.MappingRuleTypeDef" = dataclasses.field()

    Claim = field("Claim")
    MatchType = field("MatchType")
    Value = field("Value")
    RoleARN = field("RoleARN")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MappingRuleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MappingRuleTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MergeDeveloperIdentitiesInput:
    boto3_raw_data: "type_defs.MergeDeveloperIdentitiesInputTypeDef" = (
        dataclasses.field()
    )

    SourceUserIdentifier = field("SourceUserIdentifier")
    DestinationUserIdentifier = field("DestinationUserIdentifier")
    DeveloperProviderName = field("DeveloperProviderName")
    IdentityPoolId = field("IdentityPoolId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.MergeDeveloperIdentitiesInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MergeDeveloperIdentitiesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetPrincipalTagAttributeMapInput:
    boto3_raw_data: "type_defs.SetPrincipalTagAttributeMapInputTypeDef" = (
        dataclasses.field()
    )

    IdentityPoolId = field("IdentityPoolId")
    IdentityProviderName = field("IdentityProviderName")
    UseDefaults = field("UseDefaults")
    PrincipalTags = field("PrincipalTags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SetPrincipalTagAttributeMapInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetPrincipalTagAttributeMapInputTypeDef"]
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

    ResourceArn = field("ResourceArn")
    Tags = field("Tags")

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
class UnlinkDeveloperIdentityInput:
    boto3_raw_data: "type_defs.UnlinkDeveloperIdentityInputTypeDef" = (
        dataclasses.field()
    )

    IdentityId = field("IdentityId")
    IdentityPoolId = field("IdentityPoolId")
    DeveloperProviderName = field("DeveloperProviderName")
    DeveloperUserIdentifier = field("DeveloperUserIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UnlinkDeveloperIdentityInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UnlinkDeveloperIdentityInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UnlinkIdentityInput:
    boto3_raw_data: "type_defs.UnlinkIdentityInputTypeDef" = dataclasses.field()

    IdentityId = field("IdentityId")
    Logins = field("Logins")
    LoginsToRemove = field("LoginsToRemove")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UnlinkIdentityInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UnlinkIdentityInputTypeDef"]
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

    ResourceArn = field("ResourceArn")
    TagKeys = field("TagKeys")

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
class CreateIdentityPoolInput:
    boto3_raw_data: "type_defs.CreateIdentityPoolInputTypeDef" = dataclasses.field()

    IdentityPoolName = field("IdentityPoolName")
    AllowUnauthenticatedIdentities = field("AllowUnauthenticatedIdentities")
    AllowClassicFlow = field("AllowClassicFlow")
    SupportedLoginProviders = field("SupportedLoginProviders")
    DeveloperProviderName = field("DeveloperProviderName")
    OpenIdConnectProviderARNs = field("OpenIdConnectProviderARNs")

    @cached_property
    def CognitoIdentityProviders(self):  # pragma: no cover
        return CognitoIdentityProvider.make_many(
            self.boto3_raw_data["CognitoIdentityProviders"]
        )

    SamlProviderARNs = field("SamlProviderARNs")
    IdentityPoolTags = field("IdentityPoolTags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateIdentityPoolInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateIdentityPoolInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IdentityPoolRequest:
    boto3_raw_data: "type_defs.IdentityPoolRequestTypeDef" = dataclasses.field()

    IdentityPoolId = field("IdentityPoolId")
    IdentityPoolName = field("IdentityPoolName")
    AllowUnauthenticatedIdentities = field("AllowUnauthenticatedIdentities")
    AllowClassicFlow = field("AllowClassicFlow")
    SupportedLoginProviders = field("SupportedLoginProviders")
    DeveloperProviderName = field("DeveloperProviderName")
    OpenIdConnectProviderARNs = field("OpenIdConnectProviderARNs")

    @cached_property
    def CognitoIdentityProviders(self):  # pragma: no cover
        return CognitoIdentityProvider.make_many(
            self.boto3_raw_data["CognitoIdentityProviders"]
        )

    SamlProviderARNs = field("SamlProviderARNs")
    IdentityPoolTags = field("IdentityPoolTags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IdentityPoolRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IdentityPoolRequestTypeDef"]
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
class GetCredentialsForIdentityResponse:
    boto3_raw_data: "type_defs.GetCredentialsForIdentityResponseTypeDef" = (
        dataclasses.field()
    )

    IdentityId = field("IdentityId")

    @cached_property
    def Credentials(self):  # pragma: no cover
        return Credentials.make_one(self.boto3_raw_data["Credentials"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCredentialsForIdentityResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCredentialsForIdentityResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetIdResponse:
    boto3_raw_data: "type_defs.GetIdResponseTypeDef" = dataclasses.field()

    IdentityId = field("IdentityId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetIdResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetIdResponseTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetOpenIdTokenForDeveloperIdentityResponse:
    boto3_raw_data: "type_defs.GetOpenIdTokenForDeveloperIdentityResponseTypeDef" = (
        dataclasses.field()
    )

    IdentityId = field("IdentityId")
    Token = field("Token")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetOpenIdTokenForDeveloperIdentityResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetOpenIdTokenForDeveloperIdentityResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetOpenIdTokenResponse:
    boto3_raw_data: "type_defs.GetOpenIdTokenResponseTypeDef" = dataclasses.field()

    IdentityId = field("IdentityId")
    Token = field("Token")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetOpenIdTokenResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetOpenIdTokenResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPrincipalTagAttributeMapResponse:
    boto3_raw_data: "type_defs.GetPrincipalTagAttributeMapResponseTypeDef" = (
        dataclasses.field()
    )

    IdentityPoolId = field("IdentityPoolId")
    IdentityProviderName = field("IdentityProviderName")
    UseDefaults = field("UseDefaults")
    PrincipalTags = field("PrincipalTags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetPrincipalTagAttributeMapResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPrincipalTagAttributeMapResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IdentityDescriptionResponse:
    boto3_raw_data: "type_defs.IdentityDescriptionResponseTypeDef" = dataclasses.field()

    IdentityId = field("IdentityId")
    Logins = field("Logins")
    CreationDate = field("CreationDate")
    LastModifiedDate = field("LastModifiedDate")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IdentityDescriptionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IdentityDescriptionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IdentityPool:
    boto3_raw_data: "type_defs.IdentityPoolTypeDef" = dataclasses.field()

    IdentityPoolId = field("IdentityPoolId")
    IdentityPoolName = field("IdentityPoolName")
    AllowUnauthenticatedIdentities = field("AllowUnauthenticatedIdentities")
    AllowClassicFlow = field("AllowClassicFlow")
    SupportedLoginProviders = field("SupportedLoginProviders")
    DeveloperProviderName = field("DeveloperProviderName")
    OpenIdConnectProviderARNs = field("OpenIdConnectProviderARNs")

    @cached_property
    def CognitoIdentityProviders(self):  # pragma: no cover
        return CognitoIdentityProvider.make_many(
            self.boto3_raw_data["CognitoIdentityProviders"]
        )

    SamlProviderARNs = field("SamlProviderARNs")
    IdentityPoolTags = field("IdentityPoolTags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IdentityPoolTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IdentityPoolTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceResponse:
    boto3_raw_data: "type_defs.ListTagsForResourceResponseTypeDef" = dataclasses.field()

    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForResourceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LookupDeveloperIdentityResponse:
    boto3_raw_data: "type_defs.LookupDeveloperIdentityResponseTypeDef" = (
        dataclasses.field()
    )

    IdentityId = field("IdentityId")
    DeveloperUserIdentifierList = field("DeveloperUserIdentifierList")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.LookupDeveloperIdentityResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LookupDeveloperIdentityResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MergeDeveloperIdentitiesResponse:
    boto3_raw_data: "type_defs.MergeDeveloperIdentitiesResponseTypeDef" = (
        dataclasses.field()
    )

    IdentityId = field("IdentityId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.MergeDeveloperIdentitiesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MergeDeveloperIdentitiesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetPrincipalTagAttributeMapResponse:
    boto3_raw_data: "type_defs.SetPrincipalTagAttributeMapResponseTypeDef" = (
        dataclasses.field()
    )

    IdentityPoolId = field("IdentityPoolId")
    IdentityProviderName = field("IdentityProviderName")
    UseDefaults = field("UseDefaults")
    PrincipalTags = field("PrincipalTags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SetPrincipalTagAttributeMapResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetPrincipalTagAttributeMapResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteIdentitiesResponse:
    boto3_raw_data: "type_defs.DeleteIdentitiesResponseTypeDef" = dataclasses.field()

    @cached_property
    def UnprocessedIdentityIds(self):  # pragma: no cover
        return UnprocessedIdentityId.make_many(
            self.boto3_raw_data["UnprocessedIdentityIds"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteIdentitiesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteIdentitiesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIdentitiesResponse:
    boto3_raw_data: "type_defs.ListIdentitiesResponseTypeDef" = dataclasses.field()

    IdentityPoolId = field("IdentityPoolId")

    @cached_property
    def Identities(self):  # pragma: no cover
        return IdentityDescription.make_many(self.boto3_raw_data["Identities"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListIdentitiesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIdentitiesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIdentityPoolsResponse:
    boto3_raw_data: "type_defs.ListIdentityPoolsResponseTypeDef" = dataclasses.field()

    @cached_property
    def IdentityPools(self):  # pragma: no cover
        return IdentityPoolShortDescription.make_many(
            self.boto3_raw_data["IdentityPools"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListIdentityPoolsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIdentityPoolsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIdentityPoolsInputPaginate:
    boto3_raw_data: "type_defs.ListIdentityPoolsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListIdentityPoolsInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIdentityPoolsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RulesConfigurationTypeOutput:
    boto3_raw_data: "type_defs.RulesConfigurationTypeOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Rules(self):  # pragma: no cover
        return MappingRule.make_many(self.boto3_raw_data["Rules"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RulesConfigurationTypeOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RulesConfigurationTypeOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RulesConfigurationType:
    boto3_raw_data: "type_defs.RulesConfigurationTypeTypeDef" = dataclasses.field()

    @cached_property
    def Rules(self):  # pragma: no cover
        return MappingRule.make_many(self.boto3_raw_data["Rules"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RulesConfigurationTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RulesConfigurationTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RoleMappingOutput:
    boto3_raw_data: "type_defs.RoleMappingOutputTypeDef" = dataclasses.field()

    Type = field("Type")
    AmbiguousRoleResolution = field("AmbiguousRoleResolution")

    @cached_property
    def RulesConfiguration(self):  # pragma: no cover
        return RulesConfigurationTypeOutput.make_one(
            self.boto3_raw_data["RulesConfiguration"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RoleMappingOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RoleMappingOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetIdentityPoolRolesResponse:
    boto3_raw_data: "type_defs.GetIdentityPoolRolesResponseTypeDef" = (
        dataclasses.field()
    )

    IdentityPoolId = field("IdentityPoolId")
    Roles = field("Roles")
    RoleMappings = field("RoleMappings")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetIdentityPoolRolesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetIdentityPoolRolesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RoleMapping:
    boto3_raw_data: "type_defs.RoleMappingTypeDef" = dataclasses.field()

    Type = field("Type")
    AmbiguousRoleResolution = field("AmbiguousRoleResolution")
    RulesConfiguration = field("RulesConfiguration")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RoleMappingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RoleMappingTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetIdentityPoolRolesInput:
    boto3_raw_data: "type_defs.SetIdentityPoolRolesInputTypeDef" = dataclasses.field()

    IdentityPoolId = field("IdentityPoolId")
    Roles = field("Roles")
    RoleMappings = field("RoleMappings")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SetIdentityPoolRolesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetIdentityPoolRolesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
