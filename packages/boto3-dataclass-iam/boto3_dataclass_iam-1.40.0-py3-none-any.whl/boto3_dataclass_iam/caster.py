# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_iam import type_defs as bs_td


class IAMCaster:

    def add_client_id_to_open_id_connect_provider(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def add_role_to_instance_profile(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def add_user_to_group(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def attach_group_policy(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def attach_role_policy(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def attach_user_policy(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def change_password(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def create_access_key(
        self,
        res: "bs_td.CreateAccessKeyResponseTypeDef",
    ) -> "dc_td.CreateAccessKeyResponse":
        return dc_td.CreateAccessKeyResponse.make_one(res)

    def create_account_alias(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def create_group(
        self,
        res: "bs_td.CreateGroupResponseTypeDef",
    ) -> "dc_td.CreateGroupResponse":
        return dc_td.CreateGroupResponse.make_one(res)

    def create_instance_profile(
        self,
        res: "bs_td.CreateInstanceProfileResponseTypeDef",
    ) -> "dc_td.CreateInstanceProfileResponse":
        return dc_td.CreateInstanceProfileResponse.make_one(res)

    def create_login_profile(
        self,
        res: "bs_td.CreateLoginProfileResponseTypeDef",
    ) -> "dc_td.CreateLoginProfileResponse":
        return dc_td.CreateLoginProfileResponse.make_one(res)

    def create_open_id_connect_provider(
        self,
        res: "bs_td.CreateOpenIDConnectProviderResponseTypeDef",
    ) -> "dc_td.CreateOpenIDConnectProviderResponse":
        return dc_td.CreateOpenIDConnectProviderResponse.make_one(res)

    def create_policy(
        self,
        res: "bs_td.CreatePolicyResponseTypeDef",
    ) -> "dc_td.CreatePolicyResponse":
        return dc_td.CreatePolicyResponse.make_one(res)

    def create_policy_version(
        self,
        res: "bs_td.CreatePolicyVersionResponseTypeDef",
    ) -> "dc_td.CreatePolicyVersionResponse":
        return dc_td.CreatePolicyVersionResponse.make_one(res)

    def create_role(
        self,
        res: "bs_td.CreateRoleResponseTypeDef",
    ) -> "dc_td.CreateRoleResponse":
        return dc_td.CreateRoleResponse.make_one(res)

    def create_saml_provider(
        self,
        res: "bs_td.CreateSAMLProviderResponseTypeDef",
    ) -> "dc_td.CreateSAMLProviderResponse":
        return dc_td.CreateSAMLProviderResponse.make_one(res)

    def create_service_linked_role(
        self,
        res: "bs_td.CreateServiceLinkedRoleResponseTypeDef",
    ) -> "dc_td.CreateServiceLinkedRoleResponse":
        return dc_td.CreateServiceLinkedRoleResponse.make_one(res)

    def create_service_specific_credential(
        self,
        res: "bs_td.CreateServiceSpecificCredentialResponseTypeDef",
    ) -> "dc_td.CreateServiceSpecificCredentialResponse":
        return dc_td.CreateServiceSpecificCredentialResponse.make_one(res)

    def create_user(
        self,
        res: "bs_td.CreateUserResponseTypeDef",
    ) -> "dc_td.CreateUserResponse":
        return dc_td.CreateUserResponse.make_one(res)

    def create_virtual_mfa_device(
        self,
        res: "bs_td.CreateVirtualMFADeviceResponseTypeDef",
    ) -> "dc_td.CreateVirtualMFADeviceResponse":
        return dc_td.CreateVirtualMFADeviceResponse.make_one(res)

    def deactivate_mfa_device(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_access_key(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_account_alias(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_account_password_policy(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_group(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_group_policy(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_instance_profile(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_login_profile(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_open_id_connect_provider(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_policy(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_policy_version(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_role(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_role_permissions_boundary(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_role_policy(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_saml_provider(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_ssh_public_key(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_server_certificate(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_service_linked_role(
        self,
        res: "bs_td.DeleteServiceLinkedRoleResponseTypeDef",
    ) -> "dc_td.DeleteServiceLinkedRoleResponse":
        return dc_td.DeleteServiceLinkedRoleResponse.make_one(res)

    def delete_service_specific_credential(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_signing_certificate(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_user(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_user_permissions_boundary(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_user_policy(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_virtual_mfa_device(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def detach_group_policy(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def detach_role_policy(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def detach_user_policy(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def disable_organizations_root_credentials_management(
        self,
        res: "bs_td.DisableOrganizationsRootCredentialsManagementResponseTypeDef",
    ) -> "dc_td.DisableOrganizationsRootCredentialsManagementResponse":
        return dc_td.DisableOrganizationsRootCredentialsManagementResponse.make_one(res)

    def disable_organizations_root_sessions(
        self,
        res: "bs_td.DisableOrganizationsRootSessionsResponseTypeDef",
    ) -> "dc_td.DisableOrganizationsRootSessionsResponse":
        return dc_td.DisableOrganizationsRootSessionsResponse.make_one(res)

    def enable_mfa_device(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def enable_organizations_root_credentials_management(
        self,
        res: "bs_td.EnableOrganizationsRootCredentialsManagementResponseTypeDef",
    ) -> "dc_td.EnableOrganizationsRootCredentialsManagementResponse":
        return dc_td.EnableOrganizationsRootCredentialsManagementResponse.make_one(res)

    def enable_organizations_root_sessions(
        self,
        res: "bs_td.EnableOrganizationsRootSessionsResponseTypeDef",
    ) -> "dc_td.EnableOrganizationsRootSessionsResponse":
        return dc_td.EnableOrganizationsRootSessionsResponse.make_one(res)

    def generate_credential_report(
        self,
        res: "bs_td.GenerateCredentialReportResponseTypeDef",
    ) -> "dc_td.GenerateCredentialReportResponse":
        return dc_td.GenerateCredentialReportResponse.make_one(res)

    def generate_organizations_access_report(
        self,
        res: "bs_td.GenerateOrganizationsAccessReportResponseTypeDef",
    ) -> "dc_td.GenerateOrganizationsAccessReportResponse":
        return dc_td.GenerateOrganizationsAccessReportResponse.make_one(res)

    def generate_service_last_accessed_details(
        self,
        res: "bs_td.GenerateServiceLastAccessedDetailsResponseTypeDef",
    ) -> "dc_td.GenerateServiceLastAccessedDetailsResponse":
        return dc_td.GenerateServiceLastAccessedDetailsResponse.make_one(res)

    def get_access_key_last_used(
        self,
        res: "bs_td.GetAccessKeyLastUsedResponseTypeDef",
    ) -> "dc_td.GetAccessKeyLastUsedResponse":
        return dc_td.GetAccessKeyLastUsedResponse.make_one(res)

    def get_account_authorization_details(
        self,
        res: "bs_td.GetAccountAuthorizationDetailsResponseTypeDef",
    ) -> "dc_td.GetAccountAuthorizationDetailsResponse":
        return dc_td.GetAccountAuthorizationDetailsResponse.make_one(res)

    def get_account_password_policy(
        self,
        res: "bs_td.GetAccountPasswordPolicyResponseTypeDef",
    ) -> "dc_td.GetAccountPasswordPolicyResponse":
        return dc_td.GetAccountPasswordPolicyResponse.make_one(res)

    def get_account_summary(
        self,
        res: "bs_td.GetAccountSummaryResponseTypeDef",
    ) -> "dc_td.GetAccountSummaryResponse":
        return dc_td.GetAccountSummaryResponse.make_one(res)

    def get_context_keys_for_custom_policy(
        self,
        res: "bs_td.GetContextKeysForPolicyResponseTypeDef",
    ) -> "dc_td.GetContextKeysForPolicyResponse":
        return dc_td.GetContextKeysForPolicyResponse.make_one(res)

    def get_context_keys_for_principal_policy(
        self,
        res: "bs_td.GetContextKeysForPolicyResponseTypeDef",
    ) -> "dc_td.GetContextKeysForPolicyResponse":
        return dc_td.GetContextKeysForPolicyResponse.make_one(res)

    def get_credential_report(
        self,
        res: "bs_td.GetCredentialReportResponseTypeDef",
    ) -> "dc_td.GetCredentialReportResponse":
        return dc_td.GetCredentialReportResponse.make_one(res)

    def get_group(
        self,
        res: "bs_td.GetGroupResponseTypeDef",
    ) -> "dc_td.GetGroupResponse":
        return dc_td.GetGroupResponse.make_one(res)

    def get_group_policy(
        self,
        res: "bs_td.GetGroupPolicyResponseTypeDef",
    ) -> "dc_td.GetGroupPolicyResponse":
        return dc_td.GetGroupPolicyResponse.make_one(res)

    def get_instance_profile(
        self,
        res: "bs_td.GetInstanceProfileResponseTypeDef",
    ) -> "dc_td.GetInstanceProfileResponse":
        return dc_td.GetInstanceProfileResponse.make_one(res)

    def get_login_profile(
        self,
        res: "bs_td.GetLoginProfileResponseTypeDef",
    ) -> "dc_td.GetLoginProfileResponse":
        return dc_td.GetLoginProfileResponse.make_one(res)

    def get_mfa_device(
        self,
        res: "bs_td.GetMFADeviceResponseTypeDef",
    ) -> "dc_td.GetMFADeviceResponse":
        return dc_td.GetMFADeviceResponse.make_one(res)

    def get_open_id_connect_provider(
        self,
        res: "bs_td.GetOpenIDConnectProviderResponseTypeDef",
    ) -> "dc_td.GetOpenIDConnectProviderResponse":
        return dc_td.GetOpenIDConnectProviderResponse.make_one(res)

    def get_organizations_access_report(
        self,
        res: "bs_td.GetOrganizationsAccessReportResponseTypeDef",
    ) -> "dc_td.GetOrganizationsAccessReportResponse":
        return dc_td.GetOrganizationsAccessReportResponse.make_one(res)

    def get_policy(
        self,
        res: "bs_td.GetPolicyResponseTypeDef",
    ) -> "dc_td.GetPolicyResponse":
        return dc_td.GetPolicyResponse.make_one(res)

    def get_policy_version(
        self,
        res: "bs_td.GetPolicyVersionResponseTypeDef",
    ) -> "dc_td.GetPolicyVersionResponse":
        return dc_td.GetPolicyVersionResponse.make_one(res)

    def get_role(
        self,
        res: "bs_td.GetRoleResponseTypeDef",
    ) -> "dc_td.GetRoleResponse":
        return dc_td.GetRoleResponse.make_one(res)

    def get_role_policy(
        self,
        res: "bs_td.GetRolePolicyResponseTypeDef",
    ) -> "dc_td.GetRolePolicyResponse":
        return dc_td.GetRolePolicyResponse.make_one(res)

    def get_saml_provider(
        self,
        res: "bs_td.GetSAMLProviderResponseTypeDef",
    ) -> "dc_td.GetSAMLProviderResponse":
        return dc_td.GetSAMLProviderResponse.make_one(res)

    def get_ssh_public_key(
        self,
        res: "bs_td.GetSSHPublicKeyResponseTypeDef",
    ) -> "dc_td.GetSSHPublicKeyResponse":
        return dc_td.GetSSHPublicKeyResponse.make_one(res)

    def get_server_certificate(
        self,
        res: "bs_td.GetServerCertificateResponseTypeDef",
    ) -> "dc_td.GetServerCertificateResponse":
        return dc_td.GetServerCertificateResponse.make_one(res)

    def get_service_last_accessed_details(
        self,
        res: "bs_td.GetServiceLastAccessedDetailsResponseTypeDef",
    ) -> "dc_td.GetServiceLastAccessedDetailsResponse":
        return dc_td.GetServiceLastAccessedDetailsResponse.make_one(res)

    def get_service_last_accessed_details_with_entities(
        self,
        res: "bs_td.GetServiceLastAccessedDetailsWithEntitiesResponseTypeDef",
    ) -> "dc_td.GetServiceLastAccessedDetailsWithEntitiesResponse":
        return dc_td.GetServiceLastAccessedDetailsWithEntitiesResponse.make_one(res)

    def get_service_linked_role_deletion_status(
        self,
        res: "bs_td.GetServiceLinkedRoleDeletionStatusResponseTypeDef",
    ) -> "dc_td.GetServiceLinkedRoleDeletionStatusResponse":
        return dc_td.GetServiceLinkedRoleDeletionStatusResponse.make_one(res)

    def get_user(
        self,
        res: "bs_td.GetUserResponseTypeDef",
    ) -> "dc_td.GetUserResponse":
        return dc_td.GetUserResponse.make_one(res)

    def get_user_policy(
        self,
        res: "bs_td.GetUserPolicyResponseTypeDef",
    ) -> "dc_td.GetUserPolicyResponse":
        return dc_td.GetUserPolicyResponse.make_one(res)

    def list_access_keys(
        self,
        res: "bs_td.ListAccessKeysResponseTypeDef",
    ) -> "dc_td.ListAccessKeysResponse":
        return dc_td.ListAccessKeysResponse.make_one(res)

    def list_account_aliases(
        self,
        res: "bs_td.ListAccountAliasesResponseTypeDef",
    ) -> "dc_td.ListAccountAliasesResponse":
        return dc_td.ListAccountAliasesResponse.make_one(res)

    def list_attached_group_policies(
        self,
        res: "bs_td.ListAttachedGroupPoliciesResponseTypeDef",
    ) -> "dc_td.ListAttachedGroupPoliciesResponse":
        return dc_td.ListAttachedGroupPoliciesResponse.make_one(res)

    def list_attached_role_policies(
        self,
        res: "bs_td.ListAttachedRolePoliciesResponseTypeDef",
    ) -> "dc_td.ListAttachedRolePoliciesResponse":
        return dc_td.ListAttachedRolePoliciesResponse.make_one(res)

    def list_attached_user_policies(
        self,
        res: "bs_td.ListAttachedUserPoliciesResponseTypeDef",
    ) -> "dc_td.ListAttachedUserPoliciesResponse":
        return dc_td.ListAttachedUserPoliciesResponse.make_one(res)

    def list_entities_for_policy(
        self,
        res: "bs_td.ListEntitiesForPolicyResponseTypeDef",
    ) -> "dc_td.ListEntitiesForPolicyResponse":
        return dc_td.ListEntitiesForPolicyResponse.make_one(res)

    def list_group_policies(
        self,
        res: "bs_td.ListGroupPoliciesResponseTypeDef",
    ) -> "dc_td.ListGroupPoliciesResponse":
        return dc_td.ListGroupPoliciesResponse.make_one(res)

    def list_groups(
        self,
        res: "bs_td.ListGroupsResponseTypeDef",
    ) -> "dc_td.ListGroupsResponse":
        return dc_td.ListGroupsResponse.make_one(res)

    def list_groups_for_user(
        self,
        res: "bs_td.ListGroupsForUserResponseTypeDef",
    ) -> "dc_td.ListGroupsForUserResponse":
        return dc_td.ListGroupsForUserResponse.make_one(res)

    def list_instance_profile_tags(
        self,
        res: "bs_td.ListInstanceProfileTagsResponseTypeDef",
    ) -> "dc_td.ListInstanceProfileTagsResponse":
        return dc_td.ListInstanceProfileTagsResponse.make_one(res)

    def list_instance_profiles(
        self,
        res: "bs_td.ListInstanceProfilesResponseTypeDef",
    ) -> "dc_td.ListInstanceProfilesResponse":
        return dc_td.ListInstanceProfilesResponse.make_one(res)

    def list_instance_profiles_for_role(
        self,
        res: "bs_td.ListInstanceProfilesForRoleResponseTypeDef",
    ) -> "dc_td.ListInstanceProfilesForRoleResponse":
        return dc_td.ListInstanceProfilesForRoleResponse.make_one(res)

    def list_mfa_device_tags(
        self,
        res: "bs_td.ListMFADeviceTagsResponseTypeDef",
    ) -> "dc_td.ListMFADeviceTagsResponse":
        return dc_td.ListMFADeviceTagsResponse.make_one(res)

    def list_mfa_devices(
        self,
        res: "bs_td.ListMFADevicesResponseTypeDef",
    ) -> "dc_td.ListMFADevicesResponse":
        return dc_td.ListMFADevicesResponse.make_one(res)

    def list_open_id_connect_provider_tags(
        self,
        res: "bs_td.ListOpenIDConnectProviderTagsResponseTypeDef",
    ) -> "dc_td.ListOpenIDConnectProviderTagsResponse":
        return dc_td.ListOpenIDConnectProviderTagsResponse.make_one(res)

    def list_open_id_connect_providers(
        self,
        res: "bs_td.ListOpenIDConnectProvidersResponseTypeDef",
    ) -> "dc_td.ListOpenIDConnectProvidersResponse":
        return dc_td.ListOpenIDConnectProvidersResponse.make_one(res)

    def list_organizations_features(
        self,
        res: "bs_td.ListOrganizationsFeaturesResponseTypeDef",
    ) -> "dc_td.ListOrganizationsFeaturesResponse":
        return dc_td.ListOrganizationsFeaturesResponse.make_one(res)

    def list_policies(
        self,
        res: "bs_td.ListPoliciesResponseTypeDef",
    ) -> "dc_td.ListPoliciesResponse":
        return dc_td.ListPoliciesResponse.make_one(res)

    def list_policies_granting_service_access(
        self,
        res: "bs_td.ListPoliciesGrantingServiceAccessResponseTypeDef",
    ) -> "dc_td.ListPoliciesGrantingServiceAccessResponse":
        return dc_td.ListPoliciesGrantingServiceAccessResponse.make_one(res)

    def list_policy_tags(
        self,
        res: "bs_td.ListPolicyTagsResponseTypeDef",
    ) -> "dc_td.ListPolicyTagsResponse":
        return dc_td.ListPolicyTagsResponse.make_one(res)

    def list_policy_versions(
        self,
        res: "bs_td.ListPolicyVersionsResponseTypeDef",
    ) -> "dc_td.ListPolicyVersionsResponse":
        return dc_td.ListPolicyVersionsResponse.make_one(res)

    def list_role_policies(
        self,
        res: "bs_td.ListRolePoliciesResponseTypeDef",
    ) -> "dc_td.ListRolePoliciesResponse":
        return dc_td.ListRolePoliciesResponse.make_one(res)

    def list_role_tags(
        self,
        res: "bs_td.ListRoleTagsResponseTypeDef",
    ) -> "dc_td.ListRoleTagsResponse":
        return dc_td.ListRoleTagsResponse.make_one(res)

    def list_roles(
        self,
        res: "bs_td.ListRolesResponseTypeDef",
    ) -> "dc_td.ListRolesResponse":
        return dc_td.ListRolesResponse.make_one(res)

    def list_saml_provider_tags(
        self,
        res: "bs_td.ListSAMLProviderTagsResponseTypeDef",
    ) -> "dc_td.ListSAMLProviderTagsResponse":
        return dc_td.ListSAMLProviderTagsResponse.make_one(res)

    def list_saml_providers(
        self,
        res: "bs_td.ListSAMLProvidersResponseTypeDef",
    ) -> "dc_td.ListSAMLProvidersResponse":
        return dc_td.ListSAMLProvidersResponse.make_one(res)

    def list_ssh_public_keys(
        self,
        res: "bs_td.ListSSHPublicKeysResponseTypeDef",
    ) -> "dc_td.ListSSHPublicKeysResponse":
        return dc_td.ListSSHPublicKeysResponse.make_one(res)

    def list_server_certificate_tags(
        self,
        res: "bs_td.ListServerCertificateTagsResponseTypeDef",
    ) -> "dc_td.ListServerCertificateTagsResponse":
        return dc_td.ListServerCertificateTagsResponse.make_one(res)

    def list_server_certificates(
        self,
        res: "bs_td.ListServerCertificatesResponseTypeDef",
    ) -> "dc_td.ListServerCertificatesResponse":
        return dc_td.ListServerCertificatesResponse.make_one(res)

    def list_service_specific_credentials(
        self,
        res: "bs_td.ListServiceSpecificCredentialsResponseTypeDef",
    ) -> "dc_td.ListServiceSpecificCredentialsResponse":
        return dc_td.ListServiceSpecificCredentialsResponse.make_one(res)

    def list_signing_certificates(
        self,
        res: "bs_td.ListSigningCertificatesResponseTypeDef",
    ) -> "dc_td.ListSigningCertificatesResponse":
        return dc_td.ListSigningCertificatesResponse.make_one(res)

    def list_user_policies(
        self,
        res: "bs_td.ListUserPoliciesResponseTypeDef",
    ) -> "dc_td.ListUserPoliciesResponse":
        return dc_td.ListUserPoliciesResponse.make_one(res)

    def list_user_tags(
        self,
        res: "bs_td.ListUserTagsResponseTypeDef",
    ) -> "dc_td.ListUserTagsResponse":
        return dc_td.ListUserTagsResponse.make_one(res)

    def list_users(
        self,
        res: "bs_td.ListUsersResponseTypeDef",
    ) -> "dc_td.ListUsersResponse":
        return dc_td.ListUsersResponse.make_one(res)

    def list_virtual_mfa_devices(
        self,
        res: "bs_td.ListVirtualMFADevicesResponseTypeDef",
    ) -> "dc_td.ListVirtualMFADevicesResponse":
        return dc_td.ListVirtualMFADevicesResponse.make_one(res)

    def put_group_policy(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def put_role_permissions_boundary(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def put_role_policy(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def put_user_permissions_boundary(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def put_user_policy(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def remove_client_id_from_open_id_connect_provider(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def remove_role_from_instance_profile(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def remove_user_from_group(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def reset_service_specific_credential(
        self,
        res: "bs_td.ResetServiceSpecificCredentialResponseTypeDef",
    ) -> "dc_td.ResetServiceSpecificCredentialResponse":
        return dc_td.ResetServiceSpecificCredentialResponse.make_one(res)

    def resync_mfa_device(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def set_default_policy_version(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def set_security_token_service_preferences(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def simulate_custom_policy(
        self,
        res: "bs_td.SimulatePolicyResponseTypeDef",
    ) -> "dc_td.SimulatePolicyResponse":
        return dc_td.SimulatePolicyResponse.make_one(res)

    def simulate_principal_policy(
        self,
        res: "bs_td.SimulatePolicyResponseTypeDef",
    ) -> "dc_td.SimulatePolicyResponse":
        return dc_td.SimulatePolicyResponse.make_one(res)

    def tag_instance_profile(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def tag_mfa_device(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def tag_open_id_connect_provider(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def tag_policy(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def tag_role(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def tag_saml_provider(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def tag_server_certificate(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def tag_user(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def untag_instance_profile(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def untag_mfa_device(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def untag_open_id_connect_provider(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def untag_policy(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def untag_role(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def untag_saml_provider(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def untag_server_certificate(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def untag_user(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_access_key(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_account_password_policy(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_assume_role_policy(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_group(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_login_profile(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_open_id_connect_provider_thumbprint(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_role_description(
        self,
        res: "bs_td.UpdateRoleDescriptionResponseTypeDef",
    ) -> "dc_td.UpdateRoleDescriptionResponse":
        return dc_td.UpdateRoleDescriptionResponse.make_one(res)

    def update_saml_provider(
        self,
        res: "bs_td.UpdateSAMLProviderResponseTypeDef",
    ) -> "dc_td.UpdateSAMLProviderResponse":
        return dc_td.UpdateSAMLProviderResponse.make_one(res)

    def update_ssh_public_key(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_server_certificate(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_service_specific_credential(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_signing_certificate(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_user(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def upload_ssh_public_key(
        self,
        res: "bs_td.UploadSSHPublicKeyResponseTypeDef",
    ) -> "dc_td.UploadSSHPublicKeyResponse":
        return dc_td.UploadSSHPublicKeyResponse.make_one(res)

    def upload_server_certificate(
        self,
        res: "bs_td.UploadServerCertificateResponseTypeDef",
    ) -> "dc_td.UploadServerCertificateResponse":
        return dc_td.UploadServerCertificateResponse.make_one(res)

    def upload_signing_certificate(
        self,
        res: "bs_td.UploadSigningCertificateResponseTypeDef",
    ) -> "dc_td.UploadSigningCertificateResponse":
        return dc_td.UploadSigningCertificateResponse.make_one(res)


iam_caster = IAMCaster()
