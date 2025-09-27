# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_cloudfront import type_defs as bs_td


class CLOUDFRONTCaster:

    def associate_alias(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def associate_distribution_tenant_web_acl(
        self,
        res: "bs_td.AssociateDistributionTenantWebACLResultTypeDef",
    ) -> "dc_td.AssociateDistributionTenantWebACLResult":
        return dc_td.AssociateDistributionTenantWebACLResult.make_one(res)

    def associate_distribution_web_acl(
        self,
        res: "bs_td.AssociateDistributionWebACLResultTypeDef",
    ) -> "dc_td.AssociateDistributionWebACLResult":
        return dc_td.AssociateDistributionWebACLResult.make_one(res)

    def copy_distribution(
        self,
        res: "bs_td.CopyDistributionResultTypeDef",
    ) -> "dc_td.CopyDistributionResult":
        return dc_td.CopyDistributionResult.make_one(res)

    def create_anycast_ip_list(
        self,
        res: "bs_td.CreateAnycastIpListResultTypeDef",
    ) -> "dc_td.CreateAnycastIpListResult":
        return dc_td.CreateAnycastIpListResult.make_one(res)

    def create_cache_policy(
        self,
        res: "bs_td.CreateCachePolicyResultTypeDef",
    ) -> "dc_td.CreateCachePolicyResult":
        return dc_td.CreateCachePolicyResult.make_one(res)

    def create_cloud_front_origin_access_identity(
        self,
        res: "bs_td.CreateCloudFrontOriginAccessIdentityResultTypeDef",
    ) -> "dc_td.CreateCloudFrontOriginAccessIdentityResult":
        return dc_td.CreateCloudFrontOriginAccessIdentityResult.make_one(res)

    def create_connection_group(
        self,
        res: "bs_td.CreateConnectionGroupResultTypeDef",
    ) -> "dc_td.CreateConnectionGroupResult":
        return dc_td.CreateConnectionGroupResult.make_one(res)

    def create_continuous_deployment_policy(
        self,
        res: "bs_td.CreateContinuousDeploymentPolicyResultTypeDef",
    ) -> "dc_td.CreateContinuousDeploymentPolicyResult":
        return dc_td.CreateContinuousDeploymentPolicyResult.make_one(res)

    def create_distribution(
        self,
        res: "bs_td.CreateDistributionResultTypeDef",
    ) -> "dc_td.CreateDistributionResult":
        return dc_td.CreateDistributionResult.make_one(res)

    def create_distribution_tenant(
        self,
        res: "bs_td.CreateDistributionTenantResultTypeDef",
    ) -> "dc_td.CreateDistributionTenantResult":
        return dc_td.CreateDistributionTenantResult.make_one(res)

    def create_distribution_with_tags(
        self,
        res: "bs_td.CreateDistributionWithTagsResultTypeDef",
    ) -> "dc_td.CreateDistributionWithTagsResult":
        return dc_td.CreateDistributionWithTagsResult.make_one(res)

    def create_field_level_encryption_config(
        self,
        res: "bs_td.CreateFieldLevelEncryptionConfigResultTypeDef",
    ) -> "dc_td.CreateFieldLevelEncryptionConfigResult":
        return dc_td.CreateFieldLevelEncryptionConfigResult.make_one(res)

    def create_field_level_encryption_profile(
        self,
        res: "bs_td.CreateFieldLevelEncryptionProfileResultTypeDef",
    ) -> "dc_td.CreateFieldLevelEncryptionProfileResult":
        return dc_td.CreateFieldLevelEncryptionProfileResult.make_one(res)

    def create_function(
        self,
        res: "bs_td.CreateFunctionResultTypeDef",
    ) -> "dc_td.CreateFunctionResult":
        return dc_td.CreateFunctionResult.make_one(res)

    def create_invalidation(
        self,
        res: "bs_td.CreateInvalidationResultTypeDef",
    ) -> "dc_td.CreateInvalidationResult":
        return dc_td.CreateInvalidationResult.make_one(res)

    def create_invalidation_for_distribution_tenant(
        self,
        res: "bs_td.CreateInvalidationForDistributionTenantResultTypeDef",
    ) -> "dc_td.CreateInvalidationForDistributionTenantResult":
        return dc_td.CreateInvalidationForDistributionTenantResult.make_one(res)

    def create_key_group(
        self,
        res: "bs_td.CreateKeyGroupResultTypeDef",
    ) -> "dc_td.CreateKeyGroupResult":
        return dc_td.CreateKeyGroupResult.make_one(res)

    def create_key_value_store(
        self,
        res: "bs_td.CreateKeyValueStoreResultTypeDef",
    ) -> "dc_td.CreateKeyValueStoreResult":
        return dc_td.CreateKeyValueStoreResult.make_one(res)

    def create_monitoring_subscription(
        self,
        res: "bs_td.CreateMonitoringSubscriptionResultTypeDef",
    ) -> "dc_td.CreateMonitoringSubscriptionResult":
        return dc_td.CreateMonitoringSubscriptionResult.make_one(res)

    def create_origin_access_control(
        self,
        res: "bs_td.CreateOriginAccessControlResultTypeDef",
    ) -> "dc_td.CreateOriginAccessControlResult":
        return dc_td.CreateOriginAccessControlResult.make_one(res)

    def create_origin_request_policy(
        self,
        res: "bs_td.CreateOriginRequestPolicyResultTypeDef",
    ) -> "dc_td.CreateOriginRequestPolicyResult":
        return dc_td.CreateOriginRequestPolicyResult.make_one(res)

    def create_public_key(
        self,
        res: "bs_td.CreatePublicKeyResultTypeDef",
    ) -> "dc_td.CreatePublicKeyResult":
        return dc_td.CreatePublicKeyResult.make_one(res)

    def create_realtime_log_config(
        self,
        res: "bs_td.CreateRealtimeLogConfigResultTypeDef",
    ) -> "dc_td.CreateRealtimeLogConfigResult":
        return dc_td.CreateRealtimeLogConfigResult.make_one(res)

    def create_response_headers_policy(
        self,
        res: "bs_td.CreateResponseHeadersPolicyResultTypeDef",
    ) -> "dc_td.CreateResponseHeadersPolicyResult":
        return dc_td.CreateResponseHeadersPolicyResult.make_one(res)

    def create_streaming_distribution(
        self,
        res: "bs_td.CreateStreamingDistributionResultTypeDef",
    ) -> "dc_td.CreateStreamingDistributionResult":
        return dc_td.CreateStreamingDistributionResult.make_one(res)

    def create_streaming_distribution_with_tags(
        self,
        res: "bs_td.CreateStreamingDistributionWithTagsResultTypeDef",
    ) -> "dc_td.CreateStreamingDistributionWithTagsResult":
        return dc_td.CreateStreamingDistributionWithTagsResult.make_one(res)

    def create_vpc_origin(
        self,
        res: "bs_td.CreateVpcOriginResultTypeDef",
    ) -> "dc_td.CreateVpcOriginResult":
        return dc_td.CreateVpcOriginResult.make_one(res)

    def delete_anycast_ip_list(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_cache_policy(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_cloud_front_origin_access_identity(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_connection_group(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_continuous_deployment_policy(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_distribution(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_distribution_tenant(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_field_level_encryption_config(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_field_level_encryption_profile(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_function(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_key_group(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_key_value_store(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_origin_access_control(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_origin_request_policy(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_public_key(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_realtime_log_config(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_response_headers_policy(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_streaming_distribution(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_vpc_origin(
        self,
        res: "bs_td.DeleteVpcOriginResultTypeDef",
    ) -> "dc_td.DeleteVpcOriginResult":
        return dc_td.DeleteVpcOriginResult.make_one(res)

    def describe_function(
        self,
        res: "bs_td.DescribeFunctionResultTypeDef",
    ) -> "dc_td.DescribeFunctionResult":
        return dc_td.DescribeFunctionResult.make_one(res)

    def describe_key_value_store(
        self,
        res: "bs_td.DescribeKeyValueStoreResultTypeDef",
    ) -> "dc_td.DescribeKeyValueStoreResult":
        return dc_td.DescribeKeyValueStoreResult.make_one(res)

    def disassociate_distribution_tenant_web_acl(
        self,
        res: "bs_td.DisassociateDistributionTenantWebACLResultTypeDef",
    ) -> "dc_td.DisassociateDistributionTenantWebACLResult":
        return dc_td.DisassociateDistributionTenantWebACLResult.make_one(res)

    def disassociate_distribution_web_acl(
        self,
        res: "bs_td.DisassociateDistributionWebACLResultTypeDef",
    ) -> "dc_td.DisassociateDistributionWebACLResult":
        return dc_td.DisassociateDistributionWebACLResult.make_one(res)

    def get_anycast_ip_list(
        self,
        res: "bs_td.GetAnycastIpListResultTypeDef",
    ) -> "dc_td.GetAnycastIpListResult":
        return dc_td.GetAnycastIpListResult.make_one(res)

    def get_cache_policy(
        self,
        res: "bs_td.GetCachePolicyResultTypeDef",
    ) -> "dc_td.GetCachePolicyResult":
        return dc_td.GetCachePolicyResult.make_one(res)

    def get_cache_policy_config(
        self,
        res: "bs_td.GetCachePolicyConfigResultTypeDef",
    ) -> "dc_td.GetCachePolicyConfigResult":
        return dc_td.GetCachePolicyConfigResult.make_one(res)

    def get_cloud_front_origin_access_identity(
        self,
        res: "bs_td.GetCloudFrontOriginAccessIdentityResultTypeDef",
    ) -> "dc_td.GetCloudFrontOriginAccessIdentityResult":
        return dc_td.GetCloudFrontOriginAccessIdentityResult.make_one(res)

    def get_cloud_front_origin_access_identity_config(
        self,
        res: "bs_td.GetCloudFrontOriginAccessIdentityConfigResultTypeDef",
    ) -> "dc_td.GetCloudFrontOriginAccessIdentityConfigResult":
        return dc_td.GetCloudFrontOriginAccessIdentityConfigResult.make_one(res)

    def get_connection_group(
        self,
        res: "bs_td.GetConnectionGroupResultTypeDef",
    ) -> "dc_td.GetConnectionGroupResult":
        return dc_td.GetConnectionGroupResult.make_one(res)

    def get_connection_group_by_routing_endpoint(
        self,
        res: "bs_td.GetConnectionGroupByRoutingEndpointResultTypeDef",
    ) -> "dc_td.GetConnectionGroupByRoutingEndpointResult":
        return dc_td.GetConnectionGroupByRoutingEndpointResult.make_one(res)

    def get_continuous_deployment_policy(
        self,
        res: "bs_td.GetContinuousDeploymentPolicyResultTypeDef",
    ) -> "dc_td.GetContinuousDeploymentPolicyResult":
        return dc_td.GetContinuousDeploymentPolicyResult.make_one(res)

    def get_continuous_deployment_policy_config(
        self,
        res: "bs_td.GetContinuousDeploymentPolicyConfigResultTypeDef",
    ) -> "dc_td.GetContinuousDeploymentPolicyConfigResult":
        return dc_td.GetContinuousDeploymentPolicyConfigResult.make_one(res)

    def get_distribution(
        self,
        res: "bs_td.GetDistributionResultTypeDef",
    ) -> "dc_td.GetDistributionResult":
        return dc_td.GetDistributionResult.make_one(res)

    def get_distribution_config(
        self,
        res: "bs_td.GetDistributionConfigResultTypeDef",
    ) -> "dc_td.GetDistributionConfigResult":
        return dc_td.GetDistributionConfigResult.make_one(res)

    def get_distribution_tenant(
        self,
        res: "bs_td.GetDistributionTenantResultTypeDef",
    ) -> "dc_td.GetDistributionTenantResult":
        return dc_td.GetDistributionTenantResult.make_one(res)

    def get_distribution_tenant_by_domain(
        self,
        res: "bs_td.GetDistributionTenantByDomainResultTypeDef",
    ) -> "dc_td.GetDistributionTenantByDomainResult":
        return dc_td.GetDistributionTenantByDomainResult.make_one(res)

    def get_field_level_encryption(
        self,
        res: "bs_td.GetFieldLevelEncryptionResultTypeDef",
    ) -> "dc_td.GetFieldLevelEncryptionResult":
        return dc_td.GetFieldLevelEncryptionResult.make_one(res)

    def get_field_level_encryption_config(
        self,
        res: "bs_td.GetFieldLevelEncryptionConfigResultTypeDef",
    ) -> "dc_td.GetFieldLevelEncryptionConfigResult":
        return dc_td.GetFieldLevelEncryptionConfigResult.make_one(res)

    def get_field_level_encryption_profile(
        self,
        res: "bs_td.GetFieldLevelEncryptionProfileResultTypeDef",
    ) -> "dc_td.GetFieldLevelEncryptionProfileResult":
        return dc_td.GetFieldLevelEncryptionProfileResult.make_one(res)

    def get_field_level_encryption_profile_config(
        self,
        res: "bs_td.GetFieldLevelEncryptionProfileConfigResultTypeDef",
    ) -> "dc_td.GetFieldLevelEncryptionProfileConfigResult":
        return dc_td.GetFieldLevelEncryptionProfileConfigResult.make_one(res)

    def get_function(
        self,
        res: "bs_td.GetFunctionResultTypeDef",
    ) -> "dc_td.GetFunctionResult":
        return dc_td.GetFunctionResult.make_one(res)

    def get_invalidation(
        self,
        res: "bs_td.GetInvalidationResultTypeDef",
    ) -> "dc_td.GetInvalidationResult":
        return dc_td.GetInvalidationResult.make_one(res)

    def get_invalidation_for_distribution_tenant(
        self,
        res: "bs_td.GetInvalidationForDistributionTenantResultTypeDef",
    ) -> "dc_td.GetInvalidationForDistributionTenantResult":
        return dc_td.GetInvalidationForDistributionTenantResult.make_one(res)

    def get_key_group(
        self,
        res: "bs_td.GetKeyGroupResultTypeDef",
    ) -> "dc_td.GetKeyGroupResult":
        return dc_td.GetKeyGroupResult.make_one(res)

    def get_key_group_config(
        self,
        res: "bs_td.GetKeyGroupConfigResultTypeDef",
    ) -> "dc_td.GetKeyGroupConfigResult":
        return dc_td.GetKeyGroupConfigResult.make_one(res)

    def get_managed_certificate_details(
        self,
        res: "bs_td.GetManagedCertificateDetailsResultTypeDef",
    ) -> "dc_td.GetManagedCertificateDetailsResult":
        return dc_td.GetManagedCertificateDetailsResult.make_one(res)

    def get_monitoring_subscription(
        self,
        res: "bs_td.GetMonitoringSubscriptionResultTypeDef",
    ) -> "dc_td.GetMonitoringSubscriptionResult":
        return dc_td.GetMonitoringSubscriptionResult.make_one(res)

    def get_origin_access_control(
        self,
        res: "bs_td.GetOriginAccessControlResultTypeDef",
    ) -> "dc_td.GetOriginAccessControlResult":
        return dc_td.GetOriginAccessControlResult.make_one(res)

    def get_origin_access_control_config(
        self,
        res: "bs_td.GetOriginAccessControlConfigResultTypeDef",
    ) -> "dc_td.GetOriginAccessControlConfigResult":
        return dc_td.GetOriginAccessControlConfigResult.make_one(res)

    def get_origin_request_policy(
        self,
        res: "bs_td.GetOriginRequestPolicyResultTypeDef",
    ) -> "dc_td.GetOriginRequestPolicyResult":
        return dc_td.GetOriginRequestPolicyResult.make_one(res)

    def get_origin_request_policy_config(
        self,
        res: "bs_td.GetOriginRequestPolicyConfigResultTypeDef",
    ) -> "dc_td.GetOriginRequestPolicyConfigResult":
        return dc_td.GetOriginRequestPolicyConfigResult.make_one(res)

    def get_public_key(
        self,
        res: "bs_td.GetPublicKeyResultTypeDef",
    ) -> "dc_td.GetPublicKeyResult":
        return dc_td.GetPublicKeyResult.make_one(res)

    def get_public_key_config(
        self,
        res: "bs_td.GetPublicKeyConfigResultTypeDef",
    ) -> "dc_td.GetPublicKeyConfigResult":
        return dc_td.GetPublicKeyConfigResult.make_one(res)

    def get_realtime_log_config(
        self,
        res: "bs_td.GetRealtimeLogConfigResultTypeDef",
    ) -> "dc_td.GetRealtimeLogConfigResult":
        return dc_td.GetRealtimeLogConfigResult.make_one(res)

    def get_response_headers_policy(
        self,
        res: "bs_td.GetResponseHeadersPolicyResultTypeDef",
    ) -> "dc_td.GetResponseHeadersPolicyResult":
        return dc_td.GetResponseHeadersPolicyResult.make_one(res)

    def get_response_headers_policy_config(
        self,
        res: "bs_td.GetResponseHeadersPolicyConfigResultTypeDef",
    ) -> "dc_td.GetResponseHeadersPolicyConfigResult":
        return dc_td.GetResponseHeadersPolicyConfigResult.make_one(res)

    def get_streaming_distribution(
        self,
        res: "bs_td.GetStreamingDistributionResultTypeDef",
    ) -> "dc_td.GetStreamingDistributionResult":
        return dc_td.GetStreamingDistributionResult.make_one(res)

    def get_streaming_distribution_config(
        self,
        res: "bs_td.GetStreamingDistributionConfigResultTypeDef",
    ) -> "dc_td.GetStreamingDistributionConfigResult":
        return dc_td.GetStreamingDistributionConfigResult.make_one(res)

    def get_vpc_origin(
        self,
        res: "bs_td.GetVpcOriginResultTypeDef",
    ) -> "dc_td.GetVpcOriginResult":
        return dc_td.GetVpcOriginResult.make_one(res)

    def list_anycast_ip_lists(
        self,
        res: "bs_td.ListAnycastIpListsResultTypeDef",
    ) -> "dc_td.ListAnycastIpListsResult":
        return dc_td.ListAnycastIpListsResult.make_one(res)

    def list_cache_policies(
        self,
        res: "bs_td.ListCachePoliciesResultTypeDef",
    ) -> "dc_td.ListCachePoliciesResult":
        return dc_td.ListCachePoliciesResult.make_one(res)

    def list_cloud_front_origin_access_identities(
        self,
        res: "bs_td.ListCloudFrontOriginAccessIdentitiesResultTypeDef",
    ) -> "dc_td.ListCloudFrontOriginAccessIdentitiesResult":
        return dc_td.ListCloudFrontOriginAccessIdentitiesResult.make_one(res)

    def list_conflicting_aliases(
        self,
        res: "bs_td.ListConflictingAliasesResultTypeDef",
    ) -> "dc_td.ListConflictingAliasesResult":
        return dc_td.ListConflictingAliasesResult.make_one(res)

    def list_connection_groups(
        self,
        res: "bs_td.ListConnectionGroupsResultTypeDef",
    ) -> "dc_td.ListConnectionGroupsResult":
        return dc_td.ListConnectionGroupsResult.make_one(res)

    def list_continuous_deployment_policies(
        self,
        res: "bs_td.ListContinuousDeploymentPoliciesResultTypeDef",
    ) -> "dc_td.ListContinuousDeploymentPoliciesResult":
        return dc_td.ListContinuousDeploymentPoliciesResult.make_one(res)

    def list_distribution_tenants(
        self,
        res: "bs_td.ListDistributionTenantsResultTypeDef",
    ) -> "dc_td.ListDistributionTenantsResult":
        return dc_td.ListDistributionTenantsResult.make_one(res)

    def list_distribution_tenants_by_customization(
        self,
        res: "bs_td.ListDistributionTenantsByCustomizationResultTypeDef",
    ) -> "dc_td.ListDistributionTenantsByCustomizationResult":
        return dc_td.ListDistributionTenantsByCustomizationResult.make_one(res)

    def list_distributions(
        self,
        res: "bs_td.ListDistributionsResultTypeDef",
    ) -> "dc_td.ListDistributionsResult":
        return dc_td.ListDistributionsResult.make_one(res)

    def list_distributions_by_anycast_ip_list_id(
        self,
        res: "bs_td.ListDistributionsByAnycastIpListIdResultTypeDef",
    ) -> "dc_td.ListDistributionsByAnycastIpListIdResult":
        return dc_td.ListDistributionsByAnycastIpListIdResult.make_one(res)

    def list_distributions_by_cache_policy_id(
        self,
        res: "bs_td.ListDistributionsByCachePolicyIdResultTypeDef",
    ) -> "dc_td.ListDistributionsByCachePolicyIdResult":
        return dc_td.ListDistributionsByCachePolicyIdResult.make_one(res)

    def list_distributions_by_connection_mode(
        self,
        res: "bs_td.ListDistributionsByConnectionModeResultTypeDef",
    ) -> "dc_td.ListDistributionsByConnectionModeResult":
        return dc_td.ListDistributionsByConnectionModeResult.make_one(res)

    def list_distributions_by_key_group(
        self,
        res: "bs_td.ListDistributionsByKeyGroupResultTypeDef",
    ) -> "dc_td.ListDistributionsByKeyGroupResult":
        return dc_td.ListDistributionsByKeyGroupResult.make_one(res)

    def list_distributions_by_origin_request_policy_id(
        self,
        res: "bs_td.ListDistributionsByOriginRequestPolicyIdResultTypeDef",
    ) -> "dc_td.ListDistributionsByOriginRequestPolicyIdResult":
        return dc_td.ListDistributionsByOriginRequestPolicyIdResult.make_one(res)

    def list_distributions_by_realtime_log_config(
        self,
        res: "bs_td.ListDistributionsByRealtimeLogConfigResultTypeDef",
    ) -> "dc_td.ListDistributionsByRealtimeLogConfigResult":
        return dc_td.ListDistributionsByRealtimeLogConfigResult.make_one(res)

    def list_distributions_by_response_headers_policy_id(
        self,
        res: "bs_td.ListDistributionsByResponseHeadersPolicyIdResultTypeDef",
    ) -> "dc_td.ListDistributionsByResponseHeadersPolicyIdResult":
        return dc_td.ListDistributionsByResponseHeadersPolicyIdResult.make_one(res)

    def list_distributions_by_vpc_origin_id(
        self,
        res: "bs_td.ListDistributionsByVpcOriginIdResultTypeDef",
    ) -> "dc_td.ListDistributionsByVpcOriginIdResult":
        return dc_td.ListDistributionsByVpcOriginIdResult.make_one(res)

    def list_distributions_by_web_acl_id(
        self,
        res: "bs_td.ListDistributionsByWebACLIdResultTypeDef",
    ) -> "dc_td.ListDistributionsByWebACLIdResult":
        return dc_td.ListDistributionsByWebACLIdResult.make_one(res)

    def list_domain_conflicts(
        self,
        res: "bs_td.ListDomainConflictsResultTypeDef",
    ) -> "dc_td.ListDomainConflictsResult":
        return dc_td.ListDomainConflictsResult.make_one(res)

    def list_field_level_encryption_configs(
        self,
        res: "bs_td.ListFieldLevelEncryptionConfigsResultTypeDef",
    ) -> "dc_td.ListFieldLevelEncryptionConfigsResult":
        return dc_td.ListFieldLevelEncryptionConfigsResult.make_one(res)

    def list_field_level_encryption_profiles(
        self,
        res: "bs_td.ListFieldLevelEncryptionProfilesResultTypeDef",
    ) -> "dc_td.ListFieldLevelEncryptionProfilesResult":
        return dc_td.ListFieldLevelEncryptionProfilesResult.make_one(res)

    def list_functions(
        self,
        res: "bs_td.ListFunctionsResultTypeDef",
    ) -> "dc_td.ListFunctionsResult":
        return dc_td.ListFunctionsResult.make_one(res)

    def list_invalidations(
        self,
        res: "bs_td.ListInvalidationsResultTypeDef",
    ) -> "dc_td.ListInvalidationsResult":
        return dc_td.ListInvalidationsResult.make_one(res)

    def list_invalidations_for_distribution_tenant(
        self,
        res: "bs_td.ListInvalidationsForDistributionTenantResultTypeDef",
    ) -> "dc_td.ListInvalidationsForDistributionTenantResult":
        return dc_td.ListInvalidationsForDistributionTenantResult.make_one(res)

    def list_key_groups(
        self,
        res: "bs_td.ListKeyGroupsResultTypeDef",
    ) -> "dc_td.ListKeyGroupsResult":
        return dc_td.ListKeyGroupsResult.make_one(res)

    def list_key_value_stores(
        self,
        res: "bs_td.ListKeyValueStoresResultTypeDef",
    ) -> "dc_td.ListKeyValueStoresResult":
        return dc_td.ListKeyValueStoresResult.make_one(res)

    def list_origin_access_controls(
        self,
        res: "bs_td.ListOriginAccessControlsResultTypeDef",
    ) -> "dc_td.ListOriginAccessControlsResult":
        return dc_td.ListOriginAccessControlsResult.make_one(res)

    def list_origin_request_policies(
        self,
        res: "bs_td.ListOriginRequestPoliciesResultTypeDef",
    ) -> "dc_td.ListOriginRequestPoliciesResult":
        return dc_td.ListOriginRequestPoliciesResult.make_one(res)

    def list_public_keys(
        self,
        res: "bs_td.ListPublicKeysResultTypeDef",
    ) -> "dc_td.ListPublicKeysResult":
        return dc_td.ListPublicKeysResult.make_one(res)

    def list_realtime_log_configs(
        self,
        res: "bs_td.ListRealtimeLogConfigsResultTypeDef",
    ) -> "dc_td.ListRealtimeLogConfigsResult":
        return dc_td.ListRealtimeLogConfigsResult.make_one(res)

    def list_response_headers_policies(
        self,
        res: "bs_td.ListResponseHeadersPoliciesResultTypeDef",
    ) -> "dc_td.ListResponseHeadersPoliciesResult":
        return dc_td.ListResponseHeadersPoliciesResult.make_one(res)

    def list_streaming_distributions(
        self,
        res: "bs_td.ListStreamingDistributionsResultTypeDef",
    ) -> "dc_td.ListStreamingDistributionsResult":
        return dc_td.ListStreamingDistributionsResult.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResultTypeDef",
    ) -> "dc_td.ListTagsForResourceResult":
        return dc_td.ListTagsForResourceResult.make_one(res)

    def list_vpc_origins(
        self,
        res: "bs_td.ListVpcOriginsResultTypeDef",
    ) -> "dc_td.ListVpcOriginsResult":
        return dc_td.ListVpcOriginsResult.make_one(res)

    def publish_function(
        self,
        res: "bs_td.PublishFunctionResultTypeDef",
    ) -> "dc_td.PublishFunctionResult":
        return dc_td.PublishFunctionResult.make_one(res)

    def tag_resource(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def test_function(
        self,
        res: "bs_td.TestFunctionResultTypeDef",
    ) -> "dc_td.TestFunctionResult":
        return dc_td.TestFunctionResult.make_one(res)

    def untag_resource(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_cache_policy(
        self,
        res: "bs_td.UpdateCachePolicyResultTypeDef",
    ) -> "dc_td.UpdateCachePolicyResult":
        return dc_td.UpdateCachePolicyResult.make_one(res)

    def update_cloud_front_origin_access_identity(
        self,
        res: "bs_td.UpdateCloudFrontOriginAccessIdentityResultTypeDef",
    ) -> "dc_td.UpdateCloudFrontOriginAccessIdentityResult":
        return dc_td.UpdateCloudFrontOriginAccessIdentityResult.make_one(res)

    def update_connection_group(
        self,
        res: "bs_td.UpdateConnectionGroupResultTypeDef",
    ) -> "dc_td.UpdateConnectionGroupResult":
        return dc_td.UpdateConnectionGroupResult.make_one(res)

    def update_continuous_deployment_policy(
        self,
        res: "bs_td.UpdateContinuousDeploymentPolicyResultTypeDef",
    ) -> "dc_td.UpdateContinuousDeploymentPolicyResult":
        return dc_td.UpdateContinuousDeploymentPolicyResult.make_one(res)

    def update_distribution(
        self,
        res: "bs_td.UpdateDistributionResultTypeDef",
    ) -> "dc_td.UpdateDistributionResult":
        return dc_td.UpdateDistributionResult.make_one(res)

    def update_distribution_tenant(
        self,
        res: "bs_td.UpdateDistributionTenantResultTypeDef",
    ) -> "dc_td.UpdateDistributionTenantResult":
        return dc_td.UpdateDistributionTenantResult.make_one(res)

    def update_distribution_with_staging_config(
        self,
        res: "bs_td.UpdateDistributionWithStagingConfigResultTypeDef",
    ) -> "dc_td.UpdateDistributionWithStagingConfigResult":
        return dc_td.UpdateDistributionWithStagingConfigResult.make_one(res)

    def update_domain_association(
        self,
        res: "bs_td.UpdateDomainAssociationResultTypeDef",
    ) -> "dc_td.UpdateDomainAssociationResult":
        return dc_td.UpdateDomainAssociationResult.make_one(res)

    def update_field_level_encryption_config(
        self,
        res: "bs_td.UpdateFieldLevelEncryptionConfigResultTypeDef",
    ) -> "dc_td.UpdateFieldLevelEncryptionConfigResult":
        return dc_td.UpdateFieldLevelEncryptionConfigResult.make_one(res)

    def update_field_level_encryption_profile(
        self,
        res: "bs_td.UpdateFieldLevelEncryptionProfileResultTypeDef",
    ) -> "dc_td.UpdateFieldLevelEncryptionProfileResult":
        return dc_td.UpdateFieldLevelEncryptionProfileResult.make_one(res)

    def update_function(
        self,
        res: "bs_td.UpdateFunctionResultTypeDef",
    ) -> "dc_td.UpdateFunctionResult":
        return dc_td.UpdateFunctionResult.make_one(res)

    def update_key_group(
        self,
        res: "bs_td.UpdateKeyGroupResultTypeDef",
    ) -> "dc_td.UpdateKeyGroupResult":
        return dc_td.UpdateKeyGroupResult.make_one(res)

    def update_key_value_store(
        self,
        res: "bs_td.UpdateKeyValueStoreResultTypeDef",
    ) -> "dc_td.UpdateKeyValueStoreResult":
        return dc_td.UpdateKeyValueStoreResult.make_one(res)

    def update_origin_access_control(
        self,
        res: "bs_td.UpdateOriginAccessControlResultTypeDef",
    ) -> "dc_td.UpdateOriginAccessControlResult":
        return dc_td.UpdateOriginAccessControlResult.make_one(res)

    def update_origin_request_policy(
        self,
        res: "bs_td.UpdateOriginRequestPolicyResultTypeDef",
    ) -> "dc_td.UpdateOriginRequestPolicyResult":
        return dc_td.UpdateOriginRequestPolicyResult.make_one(res)

    def update_public_key(
        self,
        res: "bs_td.UpdatePublicKeyResultTypeDef",
    ) -> "dc_td.UpdatePublicKeyResult":
        return dc_td.UpdatePublicKeyResult.make_one(res)

    def update_realtime_log_config(
        self,
        res: "bs_td.UpdateRealtimeLogConfigResultTypeDef",
    ) -> "dc_td.UpdateRealtimeLogConfigResult":
        return dc_td.UpdateRealtimeLogConfigResult.make_one(res)

    def update_response_headers_policy(
        self,
        res: "bs_td.UpdateResponseHeadersPolicyResultTypeDef",
    ) -> "dc_td.UpdateResponseHeadersPolicyResult":
        return dc_td.UpdateResponseHeadersPolicyResult.make_one(res)

    def update_streaming_distribution(
        self,
        res: "bs_td.UpdateStreamingDistributionResultTypeDef",
    ) -> "dc_td.UpdateStreamingDistributionResult":
        return dc_td.UpdateStreamingDistributionResult.make_one(res)

    def update_vpc_origin(
        self,
        res: "bs_td.UpdateVpcOriginResultTypeDef",
    ) -> "dc_td.UpdateVpcOriginResult":
        return dc_td.UpdateVpcOriginResult.make_one(res)

    def verify_dns_configuration(
        self,
        res: "bs_td.VerifyDnsConfigurationResultTypeDef",
    ) -> "dc_td.VerifyDnsConfigurationResult":
        return dc_td.VerifyDnsConfigurationResult.make_one(res)


cloudfront_caster = CLOUDFRONTCaster()
