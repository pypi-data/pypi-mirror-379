# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_cognito_identity import type_defs as bs_td


class COGNITO_IDENTITYCaster:

    def create_identity_pool(
        self,
        res: "bs_td.IdentityPoolTypeDef",
    ) -> "dc_td.IdentityPool":
        return dc_td.IdentityPool.make_one(res)

    def delete_identities(
        self,
        res: "bs_td.DeleteIdentitiesResponseTypeDef",
    ) -> "dc_td.DeleteIdentitiesResponse":
        return dc_td.DeleteIdentitiesResponse.make_one(res)

    def delete_identity_pool(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def describe_identity(
        self,
        res: "bs_td.IdentityDescriptionResponseTypeDef",
    ) -> "dc_td.IdentityDescriptionResponse":
        return dc_td.IdentityDescriptionResponse.make_one(res)

    def describe_identity_pool(
        self,
        res: "bs_td.IdentityPoolTypeDef",
    ) -> "dc_td.IdentityPool":
        return dc_td.IdentityPool.make_one(res)

    def get_credentials_for_identity(
        self,
        res: "bs_td.GetCredentialsForIdentityResponseTypeDef",
    ) -> "dc_td.GetCredentialsForIdentityResponse":
        return dc_td.GetCredentialsForIdentityResponse.make_one(res)

    def get_id(
        self,
        res: "bs_td.GetIdResponseTypeDef",
    ) -> "dc_td.GetIdResponse":
        return dc_td.GetIdResponse.make_one(res)

    def get_identity_pool_roles(
        self,
        res: "bs_td.GetIdentityPoolRolesResponseTypeDef",
    ) -> "dc_td.GetIdentityPoolRolesResponse":
        return dc_td.GetIdentityPoolRolesResponse.make_one(res)

    def get_open_id_token(
        self,
        res: "bs_td.GetOpenIdTokenResponseTypeDef",
    ) -> "dc_td.GetOpenIdTokenResponse":
        return dc_td.GetOpenIdTokenResponse.make_one(res)

    def get_open_id_token_for_developer_identity(
        self,
        res: "bs_td.GetOpenIdTokenForDeveloperIdentityResponseTypeDef",
    ) -> "dc_td.GetOpenIdTokenForDeveloperIdentityResponse":
        return dc_td.GetOpenIdTokenForDeveloperIdentityResponse.make_one(res)

    def get_principal_tag_attribute_map(
        self,
        res: "bs_td.GetPrincipalTagAttributeMapResponseTypeDef",
    ) -> "dc_td.GetPrincipalTagAttributeMapResponse":
        return dc_td.GetPrincipalTagAttributeMapResponse.make_one(res)

    def list_identities(
        self,
        res: "bs_td.ListIdentitiesResponseTypeDef",
    ) -> "dc_td.ListIdentitiesResponse":
        return dc_td.ListIdentitiesResponse.make_one(res)

    def list_identity_pools(
        self,
        res: "bs_td.ListIdentityPoolsResponseTypeDef",
    ) -> "dc_td.ListIdentityPoolsResponse":
        return dc_td.ListIdentityPoolsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def lookup_developer_identity(
        self,
        res: "bs_td.LookupDeveloperIdentityResponseTypeDef",
    ) -> "dc_td.LookupDeveloperIdentityResponse":
        return dc_td.LookupDeveloperIdentityResponse.make_one(res)

    def merge_developer_identities(
        self,
        res: "bs_td.MergeDeveloperIdentitiesResponseTypeDef",
    ) -> "dc_td.MergeDeveloperIdentitiesResponse":
        return dc_td.MergeDeveloperIdentitiesResponse.make_one(res)

    def set_identity_pool_roles(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def set_principal_tag_attribute_map(
        self,
        res: "bs_td.SetPrincipalTagAttributeMapResponseTypeDef",
    ) -> "dc_td.SetPrincipalTagAttributeMapResponse":
        return dc_td.SetPrincipalTagAttributeMapResponse.make_one(res)

    def unlink_developer_identity(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def unlink_identity(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_identity_pool(
        self,
        res: "bs_td.IdentityPoolTypeDef",
    ) -> "dc_td.IdentityPool":
        return dc_td.IdentityPool.make_one(res)


cognito_identity_caster = COGNITO_IDENTITYCaster()
