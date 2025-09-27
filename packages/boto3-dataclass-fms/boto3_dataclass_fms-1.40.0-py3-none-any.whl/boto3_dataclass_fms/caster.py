# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_fms import type_defs as bs_td


class FMSCaster:

    def associate_admin_account(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def associate_third_party_firewall(
        self,
        res: "bs_td.AssociateThirdPartyFirewallResponseTypeDef",
    ) -> "dc_td.AssociateThirdPartyFirewallResponse":
        return dc_td.AssociateThirdPartyFirewallResponse.make_one(res)

    def batch_associate_resource(
        self,
        res: "bs_td.BatchAssociateResourceResponseTypeDef",
    ) -> "dc_td.BatchAssociateResourceResponse":
        return dc_td.BatchAssociateResourceResponse.make_one(res)

    def batch_disassociate_resource(
        self,
        res: "bs_td.BatchDisassociateResourceResponseTypeDef",
    ) -> "dc_td.BatchDisassociateResourceResponse":
        return dc_td.BatchDisassociateResourceResponse.make_one(res)

    def delete_apps_list(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_notification_channel(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_policy(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_protocols_list(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_resource_set(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def disassociate_admin_account(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def disassociate_third_party_firewall(
        self,
        res: "bs_td.DisassociateThirdPartyFirewallResponseTypeDef",
    ) -> "dc_td.DisassociateThirdPartyFirewallResponse":
        return dc_td.DisassociateThirdPartyFirewallResponse.make_one(res)

    def get_admin_account(
        self,
        res: "bs_td.GetAdminAccountResponseTypeDef",
    ) -> "dc_td.GetAdminAccountResponse":
        return dc_td.GetAdminAccountResponse.make_one(res)

    def get_admin_scope(
        self,
        res: "bs_td.GetAdminScopeResponseTypeDef",
    ) -> "dc_td.GetAdminScopeResponse":
        return dc_td.GetAdminScopeResponse.make_one(res)

    def get_apps_list(
        self,
        res: "bs_td.GetAppsListResponseTypeDef",
    ) -> "dc_td.GetAppsListResponse":
        return dc_td.GetAppsListResponse.make_one(res)

    def get_compliance_detail(
        self,
        res: "bs_td.GetComplianceDetailResponseTypeDef",
    ) -> "dc_td.GetComplianceDetailResponse":
        return dc_td.GetComplianceDetailResponse.make_one(res)

    def get_notification_channel(
        self,
        res: "bs_td.GetNotificationChannelResponseTypeDef",
    ) -> "dc_td.GetNotificationChannelResponse":
        return dc_td.GetNotificationChannelResponse.make_one(res)

    def get_policy(
        self,
        res: "bs_td.GetPolicyResponseTypeDef",
    ) -> "dc_td.GetPolicyResponse":
        return dc_td.GetPolicyResponse.make_one(res)

    def get_protection_status(
        self,
        res: "bs_td.GetProtectionStatusResponseTypeDef",
    ) -> "dc_td.GetProtectionStatusResponse":
        return dc_td.GetProtectionStatusResponse.make_one(res)

    def get_protocols_list(
        self,
        res: "bs_td.GetProtocolsListResponseTypeDef",
    ) -> "dc_td.GetProtocolsListResponse":
        return dc_td.GetProtocolsListResponse.make_one(res)

    def get_resource_set(
        self,
        res: "bs_td.GetResourceSetResponseTypeDef",
    ) -> "dc_td.GetResourceSetResponse":
        return dc_td.GetResourceSetResponse.make_one(res)

    def get_third_party_firewall_association_status(
        self,
        res: "bs_td.GetThirdPartyFirewallAssociationStatusResponseTypeDef",
    ) -> "dc_td.GetThirdPartyFirewallAssociationStatusResponse":
        return dc_td.GetThirdPartyFirewallAssociationStatusResponse.make_one(res)

    def get_violation_details(
        self,
        res: "bs_td.GetViolationDetailsResponseTypeDef",
    ) -> "dc_td.GetViolationDetailsResponse":
        return dc_td.GetViolationDetailsResponse.make_one(res)

    def list_admin_accounts_for_organization(
        self,
        res: "bs_td.ListAdminAccountsForOrganizationResponseTypeDef",
    ) -> "dc_td.ListAdminAccountsForOrganizationResponse":
        return dc_td.ListAdminAccountsForOrganizationResponse.make_one(res)

    def list_admins_managing_account(
        self,
        res: "bs_td.ListAdminsManagingAccountResponseTypeDef",
    ) -> "dc_td.ListAdminsManagingAccountResponse":
        return dc_td.ListAdminsManagingAccountResponse.make_one(res)

    def list_apps_lists(
        self,
        res: "bs_td.ListAppsListsResponseTypeDef",
    ) -> "dc_td.ListAppsListsResponse":
        return dc_td.ListAppsListsResponse.make_one(res)

    def list_compliance_status(
        self,
        res: "bs_td.ListComplianceStatusResponseTypeDef",
    ) -> "dc_td.ListComplianceStatusResponse":
        return dc_td.ListComplianceStatusResponse.make_one(res)

    def list_discovered_resources(
        self,
        res: "bs_td.ListDiscoveredResourcesResponseTypeDef",
    ) -> "dc_td.ListDiscoveredResourcesResponse":
        return dc_td.ListDiscoveredResourcesResponse.make_one(res)

    def list_member_accounts(
        self,
        res: "bs_td.ListMemberAccountsResponseTypeDef",
    ) -> "dc_td.ListMemberAccountsResponse":
        return dc_td.ListMemberAccountsResponse.make_one(res)

    def list_policies(
        self,
        res: "bs_td.ListPoliciesResponseTypeDef",
    ) -> "dc_td.ListPoliciesResponse":
        return dc_td.ListPoliciesResponse.make_one(res)

    def list_protocols_lists(
        self,
        res: "bs_td.ListProtocolsListsResponseTypeDef",
    ) -> "dc_td.ListProtocolsListsResponse":
        return dc_td.ListProtocolsListsResponse.make_one(res)

    def list_resource_set_resources(
        self,
        res: "bs_td.ListResourceSetResourcesResponseTypeDef",
    ) -> "dc_td.ListResourceSetResourcesResponse":
        return dc_td.ListResourceSetResourcesResponse.make_one(res)

    def list_resource_sets(
        self,
        res: "bs_td.ListResourceSetsResponseTypeDef",
    ) -> "dc_td.ListResourceSetsResponse":
        return dc_td.ListResourceSetsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def list_third_party_firewall_firewall_policies(
        self,
        res: "bs_td.ListThirdPartyFirewallFirewallPoliciesResponseTypeDef",
    ) -> "dc_td.ListThirdPartyFirewallFirewallPoliciesResponse":
        return dc_td.ListThirdPartyFirewallFirewallPoliciesResponse.make_one(res)

    def put_admin_account(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def put_apps_list(
        self,
        res: "bs_td.PutAppsListResponseTypeDef",
    ) -> "dc_td.PutAppsListResponse":
        return dc_td.PutAppsListResponse.make_one(res)

    def put_notification_channel(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def put_policy(
        self,
        res: "bs_td.PutPolicyResponseTypeDef",
    ) -> "dc_td.PutPolicyResponse":
        return dc_td.PutPolicyResponse.make_one(res)

    def put_protocols_list(
        self,
        res: "bs_td.PutProtocolsListResponseTypeDef",
    ) -> "dc_td.PutProtocolsListResponse":
        return dc_td.PutProtocolsListResponse.make_one(res)

    def put_resource_set(
        self,
        res: "bs_td.PutResourceSetResponseTypeDef",
    ) -> "dc_td.PutResourceSetResponse":
        return dc_td.PutResourceSetResponse.make_one(res)


fms_caster = FMSCaster()
