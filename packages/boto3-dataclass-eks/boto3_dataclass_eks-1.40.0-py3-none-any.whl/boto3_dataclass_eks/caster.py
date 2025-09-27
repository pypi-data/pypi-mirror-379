# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_eks import type_defs as bs_td


class EKSCaster:

    def associate_access_policy(
        self,
        res: "bs_td.AssociateAccessPolicyResponseTypeDef",
    ) -> "dc_td.AssociateAccessPolicyResponse":
        return dc_td.AssociateAccessPolicyResponse.make_one(res)

    def associate_encryption_config(
        self,
        res: "bs_td.AssociateEncryptionConfigResponseTypeDef",
    ) -> "dc_td.AssociateEncryptionConfigResponse":
        return dc_td.AssociateEncryptionConfigResponse.make_one(res)

    def associate_identity_provider_config(
        self,
        res: "bs_td.AssociateIdentityProviderConfigResponseTypeDef",
    ) -> "dc_td.AssociateIdentityProviderConfigResponse":
        return dc_td.AssociateIdentityProviderConfigResponse.make_one(res)

    def create_access_entry(
        self,
        res: "bs_td.CreateAccessEntryResponseTypeDef",
    ) -> "dc_td.CreateAccessEntryResponse":
        return dc_td.CreateAccessEntryResponse.make_one(res)

    def create_addon(
        self,
        res: "bs_td.CreateAddonResponseTypeDef",
    ) -> "dc_td.CreateAddonResponse":
        return dc_td.CreateAddonResponse.make_one(res)

    def create_cluster(
        self,
        res: "bs_td.CreateClusterResponseTypeDef",
    ) -> "dc_td.CreateClusterResponse":
        return dc_td.CreateClusterResponse.make_one(res)

    def create_eks_anywhere_subscription(
        self,
        res: "bs_td.CreateEksAnywhereSubscriptionResponseTypeDef",
    ) -> "dc_td.CreateEksAnywhereSubscriptionResponse":
        return dc_td.CreateEksAnywhereSubscriptionResponse.make_one(res)

    def create_fargate_profile(
        self,
        res: "bs_td.CreateFargateProfileResponseTypeDef",
    ) -> "dc_td.CreateFargateProfileResponse":
        return dc_td.CreateFargateProfileResponse.make_one(res)

    def create_nodegroup(
        self,
        res: "bs_td.CreateNodegroupResponseTypeDef",
    ) -> "dc_td.CreateNodegroupResponse":
        return dc_td.CreateNodegroupResponse.make_one(res)

    def create_pod_identity_association(
        self,
        res: "bs_td.CreatePodIdentityAssociationResponseTypeDef",
    ) -> "dc_td.CreatePodIdentityAssociationResponse":
        return dc_td.CreatePodIdentityAssociationResponse.make_one(res)

    def delete_addon(
        self,
        res: "bs_td.DeleteAddonResponseTypeDef",
    ) -> "dc_td.DeleteAddonResponse":
        return dc_td.DeleteAddonResponse.make_one(res)

    def delete_cluster(
        self,
        res: "bs_td.DeleteClusterResponseTypeDef",
    ) -> "dc_td.DeleteClusterResponse":
        return dc_td.DeleteClusterResponse.make_one(res)

    def delete_eks_anywhere_subscription(
        self,
        res: "bs_td.DeleteEksAnywhereSubscriptionResponseTypeDef",
    ) -> "dc_td.DeleteEksAnywhereSubscriptionResponse":
        return dc_td.DeleteEksAnywhereSubscriptionResponse.make_one(res)

    def delete_fargate_profile(
        self,
        res: "bs_td.DeleteFargateProfileResponseTypeDef",
    ) -> "dc_td.DeleteFargateProfileResponse":
        return dc_td.DeleteFargateProfileResponse.make_one(res)

    def delete_nodegroup(
        self,
        res: "bs_td.DeleteNodegroupResponseTypeDef",
    ) -> "dc_td.DeleteNodegroupResponse":
        return dc_td.DeleteNodegroupResponse.make_one(res)

    def delete_pod_identity_association(
        self,
        res: "bs_td.DeletePodIdentityAssociationResponseTypeDef",
    ) -> "dc_td.DeletePodIdentityAssociationResponse":
        return dc_td.DeletePodIdentityAssociationResponse.make_one(res)

    def deregister_cluster(
        self,
        res: "bs_td.DeregisterClusterResponseTypeDef",
    ) -> "dc_td.DeregisterClusterResponse":
        return dc_td.DeregisterClusterResponse.make_one(res)

    def describe_access_entry(
        self,
        res: "bs_td.DescribeAccessEntryResponseTypeDef",
    ) -> "dc_td.DescribeAccessEntryResponse":
        return dc_td.DescribeAccessEntryResponse.make_one(res)

    def describe_addon(
        self,
        res: "bs_td.DescribeAddonResponseTypeDef",
    ) -> "dc_td.DescribeAddonResponse":
        return dc_td.DescribeAddonResponse.make_one(res)

    def describe_addon_configuration(
        self,
        res: "bs_td.DescribeAddonConfigurationResponseTypeDef",
    ) -> "dc_td.DescribeAddonConfigurationResponse":
        return dc_td.DescribeAddonConfigurationResponse.make_one(res)

    def describe_addon_versions(
        self,
        res: "bs_td.DescribeAddonVersionsResponseTypeDef",
    ) -> "dc_td.DescribeAddonVersionsResponse":
        return dc_td.DescribeAddonVersionsResponse.make_one(res)

    def describe_cluster(
        self,
        res: "bs_td.DescribeClusterResponseTypeDef",
    ) -> "dc_td.DescribeClusterResponse":
        return dc_td.DescribeClusterResponse.make_one(res)

    def describe_cluster_versions(
        self,
        res: "bs_td.DescribeClusterVersionsResponseTypeDef",
    ) -> "dc_td.DescribeClusterVersionsResponse":
        return dc_td.DescribeClusterVersionsResponse.make_one(res)

    def describe_eks_anywhere_subscription(
        self,
        res: "bs_td.DescribeEksAnywhereSubscriptionResponseTypeDef",
    ) -> "dc_td.DescribeEksAnywhereSubscriptionResponse":
        return dc_td.DescribeEksAnywhereSubscriptionResponse.make_one(res)

    def describe_fargate_profile(
        self,
        res: "bs_td.DescribeFargateProfileResponseTypeDef",
    ) -> "dc_td.DescribeFargateProfileResponse":
        return dc_td.DescribeFargateProfileResponse.make_one(res)

    def describe_identity_provider_config(
        self,
        res: "bs_td.DescribeIdentityProviderConfigResponseTypeDef",
    ) -> "dc_td.DescribeIdentityProviderConfigResponse":
        return dc_td.DescribeIdentityProviderConfigResponse.make_one(res)

    def describe_insight(
        self,
        res: "bs_td.DescribeInsightResponseTypeDef",
    ) -> "dc_td.DescribeInsightResponse":
        return dc_td.DescribeInsightResponse.make_one(res)

    def describe_insights_refresh(
        self,
        res: "bs_td.DescribeInsightsRefreshResponseTypeDef",
    ) -> "dc_td.DescribeInsightsRefreshResponse":
        return dc_td.DescribeInsightsRefreshResponse.make_one(res)

    def describe_nodegroup(
        self,
        res: "bs_td.DescribeNodegroupResponseTypeDef",
    ) -> "dc_td.DescribeNodegroupResponse":
        return dc_td.DescribeNodegroupResponse.make_one(res)

    def describe_pod_identity_association(
        self,
        res: "bs_td.DescribePodIdentityAssociationResponseTypeDef",
    ) -> "dc_td.DescribePodIdentityAssociationResponse":
        return dc_td.DescribePodIdentityAssociationResponse.make_one(res)

    def describe_update(
        self,
        res: "bs_td.DescribeUpdateResponseTypeDef",
    ) -> "dc_td.DescribeUpdateResponse":
        return dc_td.DescribeUpdateResponse.make_one(res)

    def disassociate_identity_provider_config(
        self,
        res: "bs_td.DisassociateIdentityProviderConfigResponseTypeDef",
    ) -> "dc_td.DisassociateIdentityProviderConfigResponse":
        return dc_td.DisassociateIdentityProviderConfigResponse.make_one(res)

    def list_access_entries(
        self,
        res: "bs_td.ListAccessEntriesResponseTypeDef",
    ) -> "dc_td.ListAccessEntriesResponse":
        return dc_td.ListAccessEntriesResponse.make_one(res)

    def list_access_policies(
        self,
        res: "bs_td.ListAccessPoliciesResponseTypeDef",
    ) -> "dc_td.ListAccessPoliciesResponse":
        return dc_td.ListAccessPoliciesResponse.make_one(res)

    def list_addons(
        self,
        res: "bs_td.ListAddonsResponseTypeDef",
    ) -> "dc_td.ListAddonsResponse":
        return dc_td.ListAddonsResponse.make_one(res)

    def list_associated_access_policies(
        self,
        res: "bs_td.ListAssociatedAccessPoliciesResponseTypeDef",
    ) -> "dc_td.ListAssociatedAccessPoliciesResponse":
        return dc_td.ListAssociatedAccessPoliciesResponse.make_one(res)

    def list_clusters(
        self,
        res: "bs_td.ListClustersResponseTypeDef",
    ) -> "dc_td.ListClustersResponse":
        return dc_td.ListClustersResponse.make_one(res)

    def list_eks_anywhere_subscriptions(
        self,
        res: "bs_td.ListEksAnywhereSubscriptionsResponseTypeDef",
    ) -> "dc_td.ListEksAnywhereSubscriptionsResponse":
        return dc_td.ListEksAnywhereSubscriptionsResponse.make_one(res)

    def list_fargate_profiles(
        self,
        res: "bs_td.ListFargateProfilesResponseTypeDef",
    ) -> "dc_td.ListFargateProfilesResponse":
        return dc_td.ListFargateProfilesResponse.make_one(res)

    def list_identity_provider_configs(
        self,
        res: "bs_td.ListIdentityProviderConfigsResponseTypeDef",
    ) -> "dc_td.ListIdentityProviderConfigsResponse":
        return dc_td.ListIdentityProviderConfigsResponse.make_one(res)

    def list_insights(
        self,
        res: "bs_td.ListInsightsResponseTypeDef",
    ) -> "dc_td.ListInsightsResponse":
        return dc_td.ListInsightsResponse.make_one(res)

    def list_nodegroups(
        self,
        res: "bs_td.ListNodegroupsResponseTypeDef",
    ) -> "dc_td.ListNodegroupsResponse":
        return dc_td.ListNodegroupsResponse.make_one(res)

    def list_pod_identity_associations(
        self,
        res: "bs_td.ListPodIdentityAssociationsResponseTypeDef",
    ) -> "dc_td.ListPodIdentityAssociationsResponse":
        return dc_td.ListPodIdentityAssociationsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def list_updates(
        self,
        res: "bs_td.ListUpdatesResponseTypeDef",
    ) -> "dc_td.ListUpdatesResponse":
        return dc_td.ListUpdatesResponse.make_one(res)

    def register_cluster(
        self,
        res: "bs_td.RegisterClusterResponseTypeDef",
    ) -> "dc_td.RegisterClusterResponse":
        return dc_td.RegisterClusterResponse.make_one(res)

    def start_insights_refresh(
        self,
        res: "bs_td.StartInsightsRefreshResponseTypeDef",
    ) -> "dc_td.StartInsightsRefreshResponse":
        return dc_td.StartInsightsRefreshResponse.make_one(res)

    def update_access_entry(
        self,
        res: "bs_td.UpdateAccessEntryResponseTypeDef",
    ) -> "dc_td.UpdateAccessEntryResponse":
        return dc_td.UpdateAccessEntryResponse.make_one(res)

    def update_addon(
        self,
        res: "bs_td.UpdateAddonResponseTypeDef",
    ) -> "dc_td.UpdateAddonResponse":
        return dc_td.UpdateAddonResponse.make_one(res)

    def update_cluster_config(
        self,
        res: "bs_td.UpdateClusterConfigResponseTypeDef",
    ) -> "dc_td.UpdateClusterConfigResponse":
        return dc_td.UpdateClusterConfigResponse.make_one(res)

    def update_cluster_version(
        self,
        res: "bs_td.UpdateClusterVersionResponseTypeDef",
    ) -> "dc_td.UpdateClusterVersionResponse":
        return dc_td.UpdateClusterVersionResponse.make_one(res)

    def update_eks_anywhere_subscription(
        self,
        res: "bs_td.UpdateEksAnywhereSubscriptionResponseTypeDef",
    ) -> "dc_td.UpdateEksAnywhereSubscriptionResponse":
        return dc_td.UpdateEksAnywhereSubscriptionResponse.make_one(res)

    def update_nodegroup_config(
        self,
        res: "bs_td.UpdateNodegroupConfigResponseTypeDef",
    ) -> "dc_td.UpdateNodegroupConfigResponse":
        return dc_td.UpdateNodegroupConfigResponse.make_one(res)

    def update_nodegroup_version(
        self,
        res: "bs_td.UpdateNodegroupVersionResponseTypeDef",
    ) -> "dc_td.UpdateNodegroupVersionResponse":
        return dc_td.UpdateNodegroupVersionResponse.make_one(res)

    def update_pod_identity_association(
        self,
        res: "bs_td.UpdatePodIdentityAssociationResponseTypeDef",
    ) -> "dc_td.UpdatePodIdentityAssociationResponse":
        return dc_td.UpdatePodIdentityAssociationResponse.make_one(res)


eks_caster = EKSCaster()
