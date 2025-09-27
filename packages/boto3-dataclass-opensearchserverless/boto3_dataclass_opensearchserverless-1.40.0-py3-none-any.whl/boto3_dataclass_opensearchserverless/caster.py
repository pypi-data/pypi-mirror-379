# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_opensearchserverless import type_defs as bs_td


class OPENSEARCHSERVERLESSCaster:

    def batch_get_collection(
        self,
        res: "bs_td.BatchGetCollectionResponseTypeDef",
    ) -> "dc_td.BatchGetCollectionResponse":
        return dc_td.BatchGetCollectionResponse.make_one(res)

    def batch_get_effective_lifecycle_policy(
        self,
        res: "bs_td.BatchGetEffectiveLifecyclePolicyResponseTypeDef",
    ) -> "dc_td.BatchGetEffectiveLifecyclePolicyResponse":
        return dc_td.BatchGetEffectiveLifecyclePolicyResponse.make_one(res)

    def batch_get_lifecycle_policy(
        self,
        res: "bs_td.BatchGetLifecyclePolicyResponseTypeDef",
    ) -> "dc_td.BatchGetLifecyclePolicyResponse":
        return dc_td.BatchGetLifecyclePolicyResponse.make_one(res)

    def batch_get_vpc_endpoint(
        self,
        res: "bs_td.BatchGetVpcEndpointResponseTypeDef",
    ) -> "dc_td.BatchGetVpcEndpointResponse":
        return dc_td.BatchGetVpcEndpointResponse.make_one(res)

    def create_access_policy(
        self,
        res: "bs_td.CreateAccessPolicyResponseTypeDef",
    ) -> "dc_td.CreateAccessPolicyResponse":
        return dc_td.CreateAccessPolicyResponse.make_one(res)

    def create_collection(
        self,
        res: "bs_td.CreateCollectionResponseTypeDef",
    ) -> "dc_td.CreateCollectionResponse":
        return dc_td.CreateCollectionResponse.make_one(res)

    def create_lifecycle_policy(
        self,
        res: "bs_td.CreateLifecyclePolicyResponseTypeDef",
    ) -> "dc_td.CreateLifecyclePolicyResponse":
        return dc_td.CreateLifecyclePolicyResponse.make_one(res)

    def create_security_config(
        self,
        res: "bs_td.CreateSecurityConfigResponseTypeDef",
    ) -> "dc_td.CreateSecurityConfigResponse":
        return dc_td.CreateSecurityConfigResponse.make_one(res)

    def create_security_policy(
        self,
        res: "bs_td.CreateSecurityPolicyResponseTypeDef",
    ) -> "dc_td.CreateSecurityPolicyResponse":
        return dc_td.CreateSecurityPolicyResponse.make_one(res)

    def create_vpc_endpoint(
        self,
        res: "bs_td.CreateVpcEndpointResponseTypeDef",
    ) -> "dc_td.CreateVpcEndpointResponse":
        return dc_td.CreateVpcEndpointResponse.make_one(res)

    def delete_collection(
        self,
        res: "bs_td.DeleteCollectionResponseTypeDef",
    ) -> "dc_td.DeleteCollectionResponse":
        return dc_td.DeleteCollectionResponse.make_one(res)

    def delete_vpc_endpoint(
        self,
        res: "bs_td.DeleteVpcEndpointResponseTypeDef",
    ) -> "dc_td.DeleteVpcEndpointResponse":
        return dc_td.DeleteVpcEndpointResponse.make_one(res)

    def get_access_policy(
        self,
        res: "bs_td.GetAccessPolicyResponseTypeDef",
    ) -> "dc_td.GetAccessPolicyResponse":
        return dc_td.GetAccessPolicyResponse.make_one(res)

    def get_account_settings(
        self,
        res: "bs_td.GetAccountSettingsResponseTypeDef",
    ) -> "dc_td.GetAccountSettingsResponse":
        return dc_td.GetAccountSettingsResponse.make_one(res)

    def get_index(
        self,
        res: "bs_td.GetIndexResponseTypeDef",
    ) -> "dc_td.GetIndexResponse":
        return dc_td.GetIndexResponse.make_one(res)

    def get_policies_stats(
        self,
        res: "bs_td.GetPoliciesStatsResponseTypeDef",
    ) -> "dc_td.GetPoliciesStatsResponse":
        return dc_td.GetPoliciesStatsResponse.make_one(res)

    def get_security_config(
        self,
        res: "bs_td.GetSecurityConfigResponseTypeDef",
    ) -> "dc_td.GetSecurityConfigResponse":
        return dc_td.GetSecurityConfigResponse.make_one(res)

    def get_security_policy(
        self,
        res: "bs_td.GetSecurityPolicyResponseTypeDef",
    ) -> "dc_td.GetSecurityPolicyResponse":
        return dc_td.GetSecurityPolicyResponse.make_one(res)

    def list_access_policies(
        self,
        res: "bs_td.ListAccessPoliciesResponseTypeDef",
    ) -> "dc_td.ListAccessPoliciesResponse":
        return dc_td.ListAccessPoliciesResponse.make_one(res)

    def list_collections(
        self,
        res: "bs_td.ListCollectionsResponseTypeDef",
    ) -> "dc_td.ListCollectionsResponse":
        return dc_td.ListCollectionsResponse.make_one(res)

    def list_lifecycle_policies(
        self,
        res: "bs_td.ListLifecyclePoliciesResponseTypeDef",
    ) -> "dc_td.ListLifecyclePoliciesResponse":
        return dc_td.ListLifecyclePoliciesResponse.make_one(res)

    def list_security_configs(
        self,
        res: "bs_td.ListSecurityConfigsResponseTypeDef",
    ) -> "dc_td.ListSecurityConfigsResponse":
        return dc_td.ListSecurityConfigsResponse.make_one(res)

    def list_security_policies(
        self,
        res: "bs_td.ListSecurityPoliciesResponseTypeDef",
    ) -> "dc_td.ListSecurityPoliciesResponse":
        return dc_td.ListSecurityPoliciesResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def list_vpc_endpoints(
        self,
        res: "bs_td.ListVpcEndpointsResponseTypeDef",
    ) -> "dc_td.ListVpcEndpointsResponse":
        return dc_td.ListVpcEndpointsResponse.make_one(res)

    def update_access_policy(
        self,
        res: "bs_td.UpdateAccessPolicyResponseTypeDef",
    ) -> "dc_td.UpdateAccessPolicyResponse":
        return dc_td.UpdateAccessPolicyResponse.make_one(res)

    def update_account_settings(
        self,
        res: "bs_td.UpdateAccountSettingsResponseTypeDef",
    ) -> "dc_td.UpdateAccountSettingsResponse":
        return dc_td.UpdateAccountSettingsResponse.make_one(res)

    def update_collection(
        self,
        res: "bs_td.UpdateCollectionResponseTypeDef",
    ) -> "dc_td.UpdateCollectionResponse":
        return dc_td.UpdateCollectionResponse.make_one(res)

    def update_lifecycle_policy(
        self,
        res: "bs_td.UpdateLifecyclePolicyResponseTypeDef",
    ) -> "dc_td.UpdateLifecyclePolicyResponse":
        return dc_td.UpdateLifecyclePolicyResponse.make_one(res)

    def update_security_config(
        self,
        res: "bs_td.UpdateSecurityConfigResponseTypeDef",
    ) -> "dc_td.UpdateSecurityConfigResponse":
        return dc_td.UpdateSecurityConfigResponse.make_one(res)

    def update_security_policy(
        self,
        res: "bs_td.UpdateSecurityPolicyResponseTypeDef",
    ) -> "dc_td.UpdateSecurityPolicyResponse":
        return dc_td.UpdateSecurityPolicyResponse.make_one(res)

    def update_vpc_endpoint(
        self,
        res: "bs_td.UpdateVpcEndpointResponseTypeDef",
    ) -> "dc_td.UpdateVpcEndpointResponse":
        return dc_td.UpdateVpcEndpointResponse.make_one(res)


opensearchserverless_caster = OPENSEARCHSERVERLESSCaster()
