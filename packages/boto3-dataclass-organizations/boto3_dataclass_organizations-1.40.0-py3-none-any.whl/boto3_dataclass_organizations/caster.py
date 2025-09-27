# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_organizations import type_defs as bs_td


class ORGANIZATIONSCaster:

    def accept_handshake(
        self,
        res: "bs_td.AcceptHandshakeResponseTypeDef",
    ) -> "dc_td.AcceptHandshakeResponse":
        return dc_td.AcceptHandshakeResponse.make_one(res)

    def attach_policy(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def cancel_handshake(
        self,
        res: "bs_td.CancelHandshakeResponseTypeDef",
    ) -> "dc_td.CancelHandshakeResponse":
        return dc_td.CancelHandshakeResponse.make_one(res)

    def close_account(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def create_account(
        self,
        res: "bs_td.CreateAccountResponseTypeDef",
    ) -> "dc_td.CreateAccountResponse":
        return dc_td.CreateAccountResponse.make_one(res)

    def create_gov_cloud_account(
        self,
        res: "bs_td.CreateGovCloudAccountResponseTypeDef",
    ) -> "dc_td.CreateGovCloudAccountResponse":
        return dc_td.CreateGovCloudAccountResponse.make_one(res)

    def create_organization(
        self,
        res: "bs_td.CreateOrganizationResponseTypeDef",
    ) -> "dc_td.CreateOrganizationResponse":
        return dc_td.CreateOrganizationResponse.make_one(res)

    def create_organizational_unit(
        self,
        res: "bs_td.CreateOrganizationalUnitResponseTypeDef",
    ) -> "dc_td.CreateOrganizationalUnitResponse":
        return dc_td.CreateOrganizationalUnitResponse.make_one(res)

    def create_policy(
        self,
        res: "bs_td.CreatePolicyResponseTypeDef",
    ) -> "dc_td.CreatePolicyResponse":
        return dc_td.CreatePolicyResponse.make_one(res)

    def decline_handshake(
        self,
        res: "bs_td.DeclineHandshakeResponseTypeDef",
    ) -> "dc_td.DeclineHandshakeResponse":
        return dc_td.DeclineHandshakeResponse.make_one(res)

    def delete_organization(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_organizational_unit(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_policy(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_resource_policy(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def deregister_delegated_administrator(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def describe_account(
        self,
        res: "bs_td.DescribeAccountResponseTypeDef",
    ) -> "dc_td.DescribeAccountResponse":
        return dc_td.DescribeAccountResponse.make_one(res)

    def describe_create_account_status(
        self,
        res: "bs_td.DescribeCreateAccountStatusResponseTypeDef",
    ) -> "dc_td.DescribeCreateAccountStatusResponse":
        return dc_td.DescribeCreateAccountStatusResponse.make_one(res)

    def describe_effective_policy(
        self,
        res: "bs_td.DescribeEffectivePolicyResponseTypeDef",
    ) -> "dc_td.DescribeEffectivePolicyResponse":
        return dc_td.DescribeEffectivePolicyResponse.make_one(res)

    def describe_handshake(
        self,
        res: "bs_td.DescribeHandshakeResponseTypeDef",
    ) -> "dc_td.DescribeHandshakeResponse":
        return dc_td.DescribeHandshakeResponse.make_one(res)

    def describe_organization(
        self,
        res: "bs_td.DescribeOrganizationResponseTypeDef",
    ) -> "dc_td.DescribeOrganizationResponse":
        return dc_td.DescribeOrganizationResponse.make_one(res)

    def describe_organizational_unit(
        self,
        res: "bs_td.DescribeOrganizationalUnitResponseTypeDef",
    ) -> "dc_td.DescribeOrganizationalUnitResponse":
        return dc_td.DescribeOrganizationalUnitResponse.make_one(res)

    def describe_policy(
        self,
        res: "bs_td.DescribePolicyResponseTypeDef",
    ) -> "dc_td.DescribePolicyResponse":
        return dc_td.DescribePolicyResponse.make_one(res)

    def describe_resource_policy(
        self,
        res: "bs_td.DescribeResourcePolicyResponseTypeDef",
    ) -> "dc_td.DescribeResourcePolicyResponse":
        return dc_td.DescribeResourcePolicyResponse.make_one(res)

    def detach_policy(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def disable_aws_service_access(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def disable_policy_type(
        self,
        res: "bs_td.DisablePolicyTypeResponseTypeDef",
    ) -> "dc_td.DisablePolicyTypeResponse":
        return dc_td.DisablePolicyTypeResponse.make_one(res)

    def enable_aws_service_access(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def enable_all_features(
        self,
        res: "bs_td.EnableAllFeaturesResponseTypeDef",
    ) -> "dc_td.EnableAllFeaturesResponse":
        return dc_td.EnableAllFeaturesResponse.make_one(res)

    def enable_policy_type(
        self,
        res: "bs_td.EnablePolicyTypeResponseTypeDef",
    ) -> "dc_td.EnablePolicyTypeResponse":
        return dc_td.EnablePolicyTypeResponse.make_one(res)

    def invite_account_to_organization(
        self,
        res: "bs_td.InviteAccountToOrganizationResponseTypeDef",
    ) -> "dc_td.InviteAccountToOrganizationResponse":
        return dc_td.InviteAccountToOrganizationResponse.make_one(res)

    def leave_organization(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def list_aws_service_access_for_organization(
        self,
        res: "bs_td.ListAWSServiceAccessForOrganizationResponseTypeDef",
    ) -> "dc_td.ListAWSServiceAccessForOrganizationResponse":
        return dc_td.ListAWSServiceAccessForOrganizationResponse.make_one(res)

    def list_accounts(
        self,
        res: "bs_td.ListAccountsResponseTypeDef",
    ) -> "dc_td.ListAccountsResponse":
        return dc_td.ListAccountsResponse.make_one(res)

    def list_accounts_for_parent(
        self,
        res: "bs_td.ListAccountsForParentResponseTypeDef",
    ) -> "dc_td.ListAccountsForParentResponse":
        return dc_td.ListAccountsForParentResponse.make_one(res)

    def list_accounts_with_invalid_effective_policy(
        self,
        res: "bs_td.ListAccountsWithInvalidEffectivePolicyResponseTypeDef",
    ) -> "dc_td.ListAccountsWithInvalidEffectivePolicyResponse":
        return dc_td.ListAccountsWithInvalidEffectivePolicyResponse.make_one(res)

    def list_children(
        self,
        res: "bs_td.ListChildrenResponseTypeDef",
    ) -> "dc_td.ListChildrenResponse":
        return dc_td.ListChildrenResponse.make_one(res)

    def list_create_account_status(
        self,
        res: "bs_td.ListCreateAccountStatusResponseTypeDef",
    ) -> "dc_td.ListCreateAccountStatusResponse":
        return dc_td.ListCreateAccountStatusResponse.make_one(res)

    def list_delegated_administrators(
        self,
        res: "bs_td.ListDelegatedAdministratorsResponseTypeDef",
    ) -> "dc_td.ListDelegatedAdministratorsResponse":
        return dc_td.ListDelegatedAdministratorsResponse.make_one(res)

    def list_delegated_services_for_account(
        self,
        res: "bs_td.ListDelegatedServicesForAccountResponseTypeDef",
    ) -> "dc_td.ListDelegatedServicesForAccountResponse":
        return dc_td.ListDelegatedServicesForAccountResponse.make_one(res)

    def list_effective_policy_validation_errors(
        self,
        res: "bs_td.ListEffectivePolicyValidationErrorsResponseTypeDef",
    ) -> "dc_td.ListEffectivePolicyValidationErrorsResponse":
        return dc_td.ListEffectivePolicyValidationErrorsResponse.make_one(res)

    def list_handshakes_for_account(
        self,
        res: "bs_td.ListHandshakesForAccountResponseTypeDef",
    ) -> "dc_td.ListHandshakesForAccountResponse":
        return dc_td.ListHandshakesForAccountResponse.make_one(res)

    def list_handshakes_for_organization(
        self,
        res: "bs_td.ListHandshakesForOrganizationResponseTypeDef",
    ) -> "dc_td.ListHandshakesForOrganizationResponse":
        return dc_td.ListHandshakesForOrganizationResponse.make_one(res)

    def list_organizational_units_for_parent(
        self,
        res: "bs_td.ListOrganizationalUnitsForParentResponseTypeDef",
    ) -> "dc_td.ListOrganizationalUnitsForParentResponse":
        return dc_td.ListOrganizationalUnitsForParentResponse.make_one(res)

    def list_parents(
        self,
        res: "bs_td.ListParentsResponseTypeDef",
    ) -> "dc_td.ListParentsResponse":
        return dc_td.ListParentsResponse.make_one(res)

    def list_policies(
        self,
        res: "bs_td.ListPoliciesResponseTypeDef",
    ) -> "dc_td.ListPoliciesResponse":
        return dc_td.ListPoliciesResponse.make_one(res)

    def list_policies_for_target(
        self,
        res: "bs_td.ListPoliciesForTargetResponseTypeDef",
    ) -> "dc_td.ListPoliciesForTargetResponse":
        return dc_td.ListPoliciesForTargetResponse.make_one(res)

    def list_roots(
        self,
        res: "bs_td.ListRootsResponseTypeDef",
    ) -> "dc_td.ListRootsResponse":
        return dc_td.ListRootsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def list_targets_for_policy(
        self,
        res: "bs_td.ListTargetsForPolicyResponseTypeDef",
    ) -> "dc_td.ListTargetsForPolicyResponse":
        return dc_td.ListTargetsForPolicyResponse.make_one(res)

    def move_account(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def put_resource_policy(
        self,
        res: "bs_td.PutResourcePolicyResponseTypeDef",
    ) -> "dc_td.PutResourcePolicyResponse":
        return dc_td.PutResourcePolicyResponse.make_one(res)

    def register_delegated_administrator(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def remove_account_from_organization(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def tag_resource(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def untag_resource(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_organizational_unit(
        self,
        res: "bs_td.UpdateOrganizationalUnitResponseTypeDef",
    ) -> "dc_td.UpdateOrganizationalUnitResponse":
        return dc_td.UpdateOrganizationalUnitResponse.make_one(res)

    def update_policy(
        self,
        res: "bs_td.UpdatePolicyResponseTypeDef",
    ) -> "dc_td.UpdatePolicyResponse":
        return dc_td.UpdatePolicyResponse.make_one(res)


organizations_caster = ORGANIZATIONSCaster()
