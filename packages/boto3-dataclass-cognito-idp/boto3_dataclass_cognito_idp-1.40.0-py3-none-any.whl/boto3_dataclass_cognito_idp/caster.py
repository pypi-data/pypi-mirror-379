# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_cognito_idp import type_defs as bs_td


class COGNITO_IDPCaster:

    def admin_add_user_to_group(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def admin_create_user(
        self,
        res: "bs_td.AdminCreateUserResponseTypeDef",
    ) -> "dc_td.AdminCreateUserResponse":
        return dc_td.AdminCreateUserResponse.make_one(res)

    def admin_delete_user(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def admin_forget_device(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def admin_get_device(
        self,
        res: "bs_td.AdminGetDeviceResponseTypeDef",
    ) -> "dc_td.AdminGetDeviceResponse":
        return dc_td.AdminGetDeviceResponse.make_one(res)

    def admin_get_user(
        self,
        res: "bs_td.AdminGetUserResponseTypeDef",
    ) -> "dc_td.AdminGetUserResponse":
        return dc_td.AdminGetUserResponse.make_one(res)

    def admin_initiate_auth(
        self,
        res: "bs_td.AdminInitiateAuthResponseTypeDef",
    ) -> "dc_td.AdminInitiateAuthResponse":
        return dc_td.AdminInitiateAuthResponse.make_one(res)

    def admin_list_devices(
        self,
        res: "bs_td.AdminListDevicesResponseTypeDef",
    ) -> "dc_td.AdminListDevicesResponse":
        return dc_td.AdminListDevicesResponse.make_one(res)

    def admin_list_groups_for_user(
        self,
        res: "bs_td.AdminListGroupsForUserResponseTypeDef",
    ) -> "dc_td.AdminListGroupsForUserResponse":
        return dc_td.AdminListGroupsForUserResponse.make_one(res)

    def admin_list_user_auth_events(
        self,
        res: "bs_td.AdminListUserAuthEventsResponseTypeDef",
    ) -> "dc_td.AdminListUserAuthEventsResponse":
        return dc_td.AdminListUserAuthEventsResponse.make_one(res)

    def admin_remove_user_from_group(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def admin_respond_to_auth_challenge(
        self,
        res: "bs_td.AdminRespondToAuthChallengeResponseTypeDef",
    ) -> "dc_td.AdminRespondToAuthChallengeResponse":
        return dc_td.AdminRespondToAuthChallengeResponse.make_one(res)

    def associate_software_token(
        self,
        res: "bs_td.AssociateSoftwareTokenResponseTypeDef",
    ) -> "dc_td.AssociateSoftwareTokenResponse":
        return dc_td.AssociateSoftwareTokenResponse.make_one(res)

    def confirm_device(
        self,
        res: "bs_td.ConfirmDeviceResponseTypeDef",
    ) -> "dc_td.ConfirmDeviceResponse":
        return dc_td.ConfirmDeviceResponse.make_one(res)

    def confirm_sign_up(
        self,
        res: "bs_td.ConfirmSignUpResponseTypeDef",
    ) -> "dc_td.ConfirmSignUpResponse":
        return dc_td.ConfirmSignUpResponse.make_one(res)

    def create_group(
        self,
        res: "bs_td.CreateGroupResponseTypeDef",
    ) -> "dc_td.CreateGroupResponse":
        return dc_td.CreateGroupResponse.make_one(res)

    def create_identity_provider(
        self,
        res: "bs_td.CreateIdentityProviderResponseTypeDef",
    ) -> "dc_td.CreateIdentityProviderResponse":
        return dc_td.CreateIdentityProviderResponse.make_one(res)

    def create_managed_login_branding(
        self,
        res: "bs_td.CreateManagedLoginBrandingResponseTypeDef",
    ) -> "dc_td.CreateManagedLoginBrandingResponse":
        return dc_td.CreateManagedLoginBrandingResponse.make_one(res)

    def create_resource_server(
        self,
        res: "bs_td.CreateResourceServerResponseTypeDef",
    ) -> "dc_td.CreateResourceServerResponse":
        return dc_td.CreateResourceServerResponse.make_one(res)

    def create_terms(
        self,
        res: "bs_td.CreateTermsResponseTypeDef",
    ) -> "dc_td.CreateTermsResponse":
        return dc_td.CreateTermsResponse.make_one(res)

    def create_user_import_job(
        self,
        res: "bs_td.CreateUserImportJobResponseTypeDef",
    ) -> "dc_td.CreateUserImportJobResponse":
        return dc_td.CreateUserImportJobResponse.make_one(res)

    def create_user_pool(
        self,
        res: "bs_td.CreateUserPoolResponseTypeDef",
    ) -> "dc_td.CreateUserPoolResponse":
        return dc_td.CreateUserPoolResponse.make_one(res)

    def create_user_pool_client(
        self,
        res: "bs_td.CreateUserPoolClientResponseTypeDef",
    ) -> "dc_td.CreateUserPoolClientResponse":
        return dc_td.CreateUserPoolClientResponse.make_one(res)

    def create_user_pool_domain(
        self,
        res: "bs_td.CreateUserPoolDomainResponseTypeDef",
    ) -> "dc_td.CreateUserPoolDomainResponse":
        return dc_td.CreateUserPoolDomainResponse.make_one(res)

    def delete_group(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_identity_provider(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_managed_login_branding(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_resource_server(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_terms(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_user(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_user_pool(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_user_pool_client(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def describe_identity_provider(
        self,
        res: "bs_td.DescribeIdentityProviderResponseTypeDef",
    ) -> "dc_td.DescribeIdentityProviderResponse":
        return dc_td.DescribeIdentityProviderResponse.make_one(res)

    def describe_managed_login_branding(
        self,
        res: "bs_td.DescribeManagedLoginBrandingResponseTypeDef",
    ) -> "dc_td.DescribeManagedLoginBrandingResponse":
        return dc_td.DescribeManagedLoginBrandingResponse.make_one(res)

    def describe_managed_login_branding_by_client(
        self,
        res: "bs_td.DescribeManagedLoginBrandingByClientResponseTypeDef",
    ) -> "dc_td.DescribeManagedLoginBrandingByClientResponse":
        return dc_td.DescribeManagedLoginBrandingByClientResponse.make_one(res)

    def describe_resource_server(
        self,
        res: "bs_td.DescribeResourceServerResponseTypeDef",
    ) -> "dc_td.DescribeResourceServerResponse":
        return dc_td.DescribeResourceServerResponse.make_one(res)

    def describe_risk_configuration(
        self,
        res: "bs_td.DescribeRiskConfigurationResponseTypeDef",
    ) -> "dc_td.DescribeRiskConfigurationResponse":
        return dc_td.DescribeRiskConfigurationResponse.make_one(res)

    def describe_terms(
        self,
        res: "bs_td.DescribeTermsResponseTypeDef",
    ) -> "dc_td.DescribeTermsResponse":
        return dc_td.DescribeTermsResponse.make_one(res)

    def describe_user_import_job(
        self,
        res: "bs_td.DescribeUserImportJobResponseTypeDef",
    ) -> "dc_td.DescribeUserImportJobResponse":
        return dc_td.DescribeUserImportJobResponse.make_one(res)

    def describe_user_pool(
        self,
        res: "bs_td.DescribeUserPoolResponseTypeDef",
    ) -> "dc_td.DescribeUserPoolResponse":
        return dc_td.DescribeUserPoolResponse.make_one(res)

    def describe_user_pool_client(
        self,
        res: "bs_td.DescribeUserPoolClientResponseTypeDef",
    ) -> "dc_td.DescribeUserPoolClientResponse":
        return dc_td.DescribeUserPoolClientResponse.make_one(res)

    def describe_user_pool_domain(
        self,
        res: "bs_td.DescribeUserPoolDomainResponseTypeDef",
    ) -> "dc_td.DescribeUserPoolDomainResponse":
        return dc_td.DescribeUserPoolDomainResponse.make_one(res)

    def forget_device(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def forgot_password(
        self,
        res: "bs_td.ForgotPasswordResponseTypeDef",
    ) -> "dc_td.ForgotPasswordResponse":
        return dc_td.ForgotPasswordResponse.make_one(res)

    def get_csv_header(
        self,
        res: "bs_td.GetCSVHeaderResponseTypeDef",
    ) -> "dc_td.GetCSVHeaderResponse":
        return dc_td.GetCSVHeaderResponse.make_one(res)

    def get_device(
        self,
        res: "bs_td.GetDeviceResponseTypeDef",
    ) -> "dc_td.GetDeviceResponse":
        return dc_td.GetDeviceResponse.make_one(res)

    def get_group(
        self,
        res: "bs_td.GetGroupResponseTypeDef",
    ) -> "dc_td.GetGroupResponse":
        return dc_td.GetGroupResponse.make_one(res)

    def get_identity_provider_by_identifier(
        self,
        res: "bs_td.GetIdentityProviderByIdentifierResponseTypeDef",
    ) -> "dc_td.GetIdentityProviderByIdentifierResponse":
        return dc_td.GetIdentityProviderByIdentifierResponse.make_one(res)

    def get_log_delivery_configuration(
        self,
        res: "bs_td.GetLogDeliveryConfigurationResponseTypeDef",
    ) -> "dc_td.GetLogDeliveryConfigurationResponse":
        return dc_td.GetLogDeliveryConfigurationResponse.make_one(res)

    def get_signing_certificate(
        self,
        res: "bs_td.GetSigningCertificateResponseTypeDef",
    ) -> "dc_td.GetSigningCertificateResponse":
        return dc_td.GetSigningCertificateResponse.make_one(res)

    def get_tokens_from_refresh_token(
        self,
        res: "bs_td.GetTokensFromRefreshTokenResponseTypeDef",
    ) -> "dc_td.GetTokensFromRefreshTokenResponse":
        return dc_td.GetTokensFromRefreshTokenResponse.make_one(res)

    def get_ui_customization(
        self,
        res: "bs_td.GetUICustomizationResponseTypeDef",
    ) -> "dc_td.GetUICustomizationResponse":
        return dc_td.GetUICustomizationResponse.make_one(res)

    def get_user(
        self,
        res: "bs_td.GetUserResponseTypeDef",
    ) -> "dc_td.GetUserResponse":
        return dc_td.GetUserResponse.make_one(res)

    def get_user_attribute_verification_code(
        self,
        res: "bs_td.GetUserAttributeVerificationCodeResponseTypeDef",
    ) -> "dc_td.GetUserAttributeVerificationCodeResponse":
        return dc_td.GetUserAttributeVerificationCodeResponse.make_one(res)

    def get_user_auth_factors(
        self,
        res: "bs_td.GetUserAuthFactorsResponseTypeDef",
    ) -> "dc_td.GetUserAuthFactorsResponse":
        return dc_td.GetUserAuthFactorsResponse.make_one(res)

    def get_user_pool_mfa_config(
        self,
        res: "bs_td.GetUserPoolMfaConfigResponseTypeDef",
    ) -> "dc_td.GetUserPoolMfaConfigResponse":
        return dc_td.GetUserPoolMfaConfigResponse.make_one(res)

    def initiate_auth(
        self,
        res: "bs_td.InitiateAuthResponseTypeDef",
    ) -> "dc_td.InitiateAuthResponse":
        return dc_td.InitiateAuthResponse.make_one(res)

    def list_devices(
        self,
        res: "bs_td.ListDevicesResponseTypeDef",
    ) -> "dc_td.ListDevicesResponse":
        return dc_td.ListDevicesResponse.make_one(res)

    def list_groups(
        self,
        res: "bs_td.ListGroupsResponseTypeDef",
    ) -> "dc_td.ListGroupsResponse":
        return dc_td.ListGroupsResponse.make_one(res)

    def list_identity_providers(
        self,
        res: "bs_td.ListIdentityProvidersResponseTypeDef",
    ) -> "dc_td.ListIdentityProvidersResponse":
        return dc_td.ListIdentityProvidersResponse.make_one(res)

    def list_resource_servers(
        self,
        res: "bs_td.ListResourceServersResponseTypeDef",
    ) -> "dc_td.ListResourceServersResponse":
        return dc_td.ListResourceServersResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def list_terms(
        self,
        res: "bs_td.ListTermsResponseTypeDef",
    ) -> "dc_td.ListTermsResponse":
        return dc_td.ListTermsResponse.make_one(res)

    def list_user_import_jobs(
        self,
        res: "bs_td.ListUserImportJobsResponseTypeDef",
    ) -> "dc_td.ListUserImportJobsResponse":
        return dc_td.ListUserImportJobsResponse.make_one(res)

    def list_user_pool_clients(
        self,
        res: "bs_td.ListUserPoolClientsResponseTypeDef",
    ) -> "dc_td.ListUserPoolClientsResponse":
        return dc_td.ListUserPoolClientsResponse.make_one(res)

    def list_user_pools(
        self,
        res: "bs_td.ListUserPoolsResponseTypeDef",
    ) -> "dc_td.ListUserPoolsResponse":
        return dc_td.ListUserPoolsResponse.make_one(res)

    def list_users(
        self,
        res: "bs_td.ListUsersResponseTypeDef",
    ) -> "dc_td.ListUsersResponse":
        return dc_td.ListUsersResponse.make_one(res)

    def list_users_in_group(
        self,
        res: "bs_td.ListUsersInGroupResponseTypeDef",
    ) -> "dc_td.ListUsersInGroupResponse":
        return dc_td.ListUsersInGroupResponse.make_one(res)

    def list_web_authn_credentials(
        self,
        res: "bs_td.ListWebAuthnCredentialsResponseTypeDef",
    ) -> "dc_td.ListWebAuthnCredentialsResponse":
        return dc_td.ListWebAuthnCredentialsResponse.make_one(res)

    def resend_confirmation_code(
        self,
        res: "bs_td.ResendConfirmationCodeResponseTypeDef",
    ) -> "dc_td.ResendConfirmationCodeResponse":
        return dc_td.ResendConfirmationCodeResponse.make_one(res)

    def respond_to_auth_challenge(
        self,
        res: "bs_td.RespondToAuthChallengeResponseTypeDef",
    ) -> "dc_td.RespondToAuthChallengeResponse":
        return dc_td.RespondToAuthChallengeResponse.make_one(res)

    def set_log_delivery_configuration(
        self,
        res: "bs_td.SetLogDeliveryConfigurationResponseTypeDef",
    ) -> "dc_td.SetLogDeliveryConfigurationResponse":
        return dc_td.SetLogDeliveryConfigurationResponse.make_one(res)

    def set_risk_configuration(
        self,
        res: "bs_td.SetRiskConfigurationResponseTypeDef",
    ) -> "dc_td.SetRiskConfigurationResponse":
        return dc_td.SetRiskConfigurationResponse.make_one(res)

    def set_ui_customization(
        self,
        res: "bs_td.SetUICustomizationResponseTypeDef",
    ) -> "dc_td.SetUICustomizationResponse":
        return dc_td.SetUICustomizationResponse.make_one(res)

    def set_user_pool_mfa_config(
        self,
        res: "bs_td.SetUserPoolMfaConfigResponseTypeDef",
    ) -> "dc_td.SetUserPoolMfaConfigResponse":
        return dc_td.SetUserPoolMfaConfigResponse.make_one(res)

    def sign_up(
        self,
        res: "bs_td.SignUpResponseTypeDef",
    ) -> "dc_td.SignUpResponse":
        return dc_td.SignUpResponse.make_one(res)

    def start_user_import_job(
        self,
        res: "bs_td.StartUserImportJobResponseTypeDef",
    ) -> "dc_td.StartUserImportJobResponse":
        return dc_td.StartUserImportJobResponse.make_one(res)

    def start_web_authn_registration(
        self,
        res: "bs_td.StartWebAuthnRegistrationResponseTypeDef",
    ) -> "dc_td.StartWebAuthnRegistrationResponse":
        return dc_td.StartWebAuthnRegistrationResponse.make_one(res)

    def stop_user_import_job(
        self,
        res: "bs_td.StopUserImportJobResponseTypeDef",
    ) -> "dc_td.StopUserImportJobResponse":
        return dc_td.StopUserImportJobResponse.make_one(res)

    def update_group(
        self,
        res: "bs_td.UpdateGroupResponseTypeDef",
    ) -> "dc_td.UpdateGroupResponse":
        return dc_td.UpdateGroupResponse.make_one(res)

    def update_identity_provider(
        self,
        res: "bs_td.UpdateIdentityProviderResponseTypeDef",
    ) -> "dc_td.UpdateIdentityProviderResponse":
        return dc_td.UpdateIdentityProviderResponse.make_one(res)

    def update_managed_login_branding(
        self,
        res: "bs_td.UpdateManagedLoginBrandingResponseTypeDef",
    ) -> "dc_td.UpdateManagedLoginBrandingResponse":
        return dc_td.UpdateManagedLoginBrandingResponse.make_one(res)

    def update_resource_server(
        self,
        res: "bs_td.UpdateResourceServerResponseTypeDef",
    ) -> "dc_td.UpdateResourceServerResponse":
        return dc_td.UpdateResourceServerResponse.make_one(res)

    def update_terms(
        self,
        res: "bs_td.UpdateTermsResponseTypeDef",
    ) -> "dc_td.UpdateTermsResponse":
        return dc_td.UpdateTermsResponse.make_one(res)

    def update_user_attributes(
        self,
        res: "bs_td.UpdateUserAttributesResponseTypeDef",
    ) -> "dc_td.UpdateUserAttributesResponse":
        return dc_td.UpdateUserAttributesResponse.make_one(res)

    def update_user_pool_client(
        self,
        res: "bs_td.UpdateUserPoolClientResponseTypeDef",
    ) -> "dc_td.UpdateUserPoolClientResponse":
        return dc_td.UpdateUserPoolClientResponse.make_one(res)

    def update_user_pool_domain(
        self,
        res: "bs_td.UpdateUserPoolDomainResponseTypeDef",
    ) -> "dc_td.UpdateUserPoolDomainResponse":
        return dc_td.UpdateUserPoolDomainResponse.make_one(res)

    def verify_software_token(
        self,
        res: "bs_td.VerifySoftwareTokenResponseTypeDef",
    ) -> "dc_td.VerifySoftwareTokenResponse":
        return dc_td.VerifySoftwareTokenResponse.make_one(res)


cognito_idp_caster = COGNITO_IDPCaster()
