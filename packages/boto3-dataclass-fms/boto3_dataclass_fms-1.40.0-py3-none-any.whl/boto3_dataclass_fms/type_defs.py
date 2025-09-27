# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_fms import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AccountScopeOutput:
    boto3_raw_data: "type_defs.AccountScopeOutputTypeDef" = dataclasses.field()

    Accounts = field("Accounts")
    AllAccountsEnabled = field("AllAccountsEnabled")
    ExcludeSpecifiedAccounts = field("ExcludeSpecifiedAccounts")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AccountScopeOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccountScopeOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccountScope:
    boto3_raw_data: "type_defs.AccountScopeTypeDef" = dataclasses.field()

    Accounts = field("Accounts")
    AllAccountsEnabled = field("AllAccountsEnabled")
    ExcludeSpecifiedAccounts = field("ExcludeSpecifiedAccounts")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AccountScopeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AccountScopeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActionTarget:
    boto3_raw_data: "type_defs.ActionTargetTypeDef" = dataclasses.field()

    ResourceId = field("ResourceId")
    Description = field("Description")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ActionTargetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ActionTargetTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AdminAccountSummary:
    boto3_raw_data: "type_defs.AdminAccountSummaryTypeDef" = dataclasses.field()

    AdminAccount = field("AdminAccount")
    DefaultAdmin = field("DefaultAdmin")
    Status = field("Status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AdminAccountSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AdminAccountSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OrganizationalUnitScopeOutput:
    boto3_raw_data: "type_defs.OrganizationalUnitScopeOutputTypeDef" = (
        dataclasses.field()
    )

    OrganizationalUnits = field("OrganizationalUnits")
    AllOrganizationalUnitsEnabled = field("AllOrganizationalUnitsEnabled")
    ExcludeSpecifiedOrganizationalUnits = field("ExcludeSpecifiedOrganizationalUnits")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.OrganizationalUnitScopeOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OrganizationalUnitScopeOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PolicyTypeScopeOutput:
    boto3_raw_data: "type_defs.PolicyTypeScopeOutputTypeDef" = dataclasses.field()

    PolicyTypes = field("PolicyTypes")
    AllPolicyTypesEnabled = field("AllPolicyTypesEnabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PolicyTypeScopeOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PolicyTypeScopeOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegionScopeOutput:
    boto3_raw_data: "type_defs.RegionScopeOutputTypeDef" = dataclasses.field()

    Regions = field("Regions")
    AllRegionsEnabled = field("AllRegionsEnabled")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RegionScopeOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegionScopeOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OrganizationalUnitScope:
    boto3_raw_data: "type_defs.OrganizationalUnitScopeTypeDef" = dataclasses.field()

    OrganizationalUnits = field("OrganizationalUnits")
    AllOrganizationalUnitsEnabled = field("AllOrganizationalUnitsEnabled")
    ExcludeSpecifiedOrganizationalUnits = field("ExcludeSpecifiedOrganizationalUnits")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OrganizationalUnitScopeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OrganizationalUnitScopeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PolicyTypeScope:
    boto3_raw_data: "type_defs.PolicyTypeScopeTypeDef" = dataclasses.field()

    PolicyTypes = field("PolicyTypes")
    AllPolicyTypesEnabled = field("AllPolicyTypesEnabled")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PolicyTypeScopeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PolicyTypeScopeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegionScope:
    boto3_raw_data: "type_defs.RegionScopeTypeDef" = dataclasses.field()

    Regions = field("Regions")
    AllRegionsEnabled = field("AllRegionsEnabled")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RegionScopeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RegionScopeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class App:
    boto3_raw_data: "type_defs.AppTypeDef" = dataclasses.field()

    AppName = field("AppName")
    Protocol = field("Protocol")
    Port = field("Port")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AppTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AppTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateAdminAccountRequest:
    boto3_raw_data: "type_defs.AssociateAdminAccountRequestTypeDef" = (
        dataclasses.field()
    )

    AdminAccount = field("AdminAccount")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociateAdminAccountRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateAdminAccountRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateThirdPartyFirewallRequest:
    boto3_raw_data: "type_defs.AssociateThirdPartyFirewallRequestTypeDef" = (
        dataclasses.field()
    )

    ThirdPartyFirewall = field("ThirdPartyFirewall")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateThirdPartyFirewallRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateThirdPartyFirewallRequestTypeDef"]
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
class AwsEc2NetworkInterfaceViolation:
    boto3_raw_data: "type_defs.AwsEc2NetworkInterfaceViolationTypeDef" = (
        dataclasses.field()
    )

    ViolationTarget = field("ViolationTarget")
    ViolatingSecurityGroups = field("ViolatingSecurityGroups")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AwsEc2NetworkInterfaceViolationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AwsEc2NetworkInterfaceViolationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PartialMatch:
    boto3_raw_data: "type_defs.PartialMatchTypeDef" = dataclasses.field()

    Reference = field("Reference")
    TargetViolationReasons = field("TargetViolationReasons")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PartialMatchTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PartialMatchTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchAssociateResourceRequest:
    boto3_raw_data: "type_defs.BatchAssociateResourceRequestTypeDef" = (
        dataclasses.field()
    )

    ResourceSetIdentifier = field("ResourceSetIdentifier")
    Items = field("Items")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchAssociateResourceRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchAssociateResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FailedItem:
    boto3_raw_data: "type_defs.FailedItemTypeDef" = dataclasses.field()

    URI = field("URI")
    Reason = field("Reason")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FailedItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FailedItemTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDisassociateResourceRequest:
    boto3_raw_data: "type_defs.BatchDisassociateResourceRequestTypeDef" = (
        dataclasses.field()
    )

    ResourceSetIdentifier = field("ResourceSetIdentifier")
    Items = field("Items")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchDisassociateResourceRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDisassociateResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComplianceViolator:
    boto3_raw_data: "type_defs.ComplianceViolatorTypeDef" = dataclasses.field()

    ResourceId = field("ResourceId")
    ViolationReason = field("ViolationReason")
    ResourceType = field("ResourceType")
    Metadata = field("Metadata")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ComplianceViolatorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComplianceViolatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAppsListRequest:
    boto3_raw_data: "type_defs.DeleteAppsListRequestTypeDef" = dataclasses.field()

    ListId = field("ListId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAppsListRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAppsListRequestTypeDef"]
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

    PolicyId = field("PolicyId")
    DeleteAllPolicyResources = field("DeleteAllPolicyResources")

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
class DeleteProtocolsListRequest:
    boto3_raw_data: "type_defs.DeleteProtocolsListRequestTypeDef" = dataclasses.field()

    ListId = field("ListId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteProtocolsListRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteProtocolsListRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteResourceSetRequest:
    boto3_raw_data: "type_defs.DeleteResourceSetRequestTypeDef" = dataclasses.field()

    Identifier = field("Identifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteResourceSetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteResourceSetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateThirdPartyFirewallRequest:
    boto3_raw_data: "type_defs.DisassociateThirdPartyFirewallRequestTypeDef" = (
        dataclasses.field()
    )

    ThirdPartyFirewall = field("ThirdPartyFirewall")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateThirdPartyFirewallRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateThirdPartyFirewallRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DiscoveredResource:
    boto3_raw_data: "type_defs.DiscoveredResourceTypeDef" = dataclasses.field()

    URI = field("URI")
    AccountId = field("AccountId")
    Type = field("Type")
    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DiscoveredResourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DiscoveredResourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DnsDuplicateRuleGroupViolation:
    boto3_raw_data: "type_defs.DnsDuplicateRuleGroupViolationTypeDef" = (
        dataclasses.field()
    )

    ViolationTarget = field("ViolationTarget")
    ViolationTargetDescription = field("ViolationTargetDescription")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DnsDuplicateRuleGroupViolationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DnsDuplicateRuleGroupViolationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DnsRuleGroupLimitExceededViolation:
    boto3_raw_data: "type_defs.DnsRuleGroupLimitExceededViolationTypeDef" = (
        dataclasses.field()
    )

    ViolationTarget = field("ViolationTarget")
    ViolationTargetDescription = field("ViolationTargetDescription")
    NumberOfRuleGroupsAlreadyAssociated = field("NumberOfRuleGroupsAlreadyAssociated")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DnsRuleGroupLimitExceededViolationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DnsRuleGroupLimitExceededViolationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DnsRuleGroupPriorityConflictViolation:
    boto3_raw_data: "type_defs.DnsRuleGroupPriorityConflictViolationTypeDef" = (
        dataclasses.field()
    )

    ViolationTarget = field("ViolationTarget")
    ViolationTargetDescription = field("ViolationTargetDescription")
    ConflictingPriority = field("ConflictingPriority")
    ConflictingPolicyId = field("ConflictingPolicyId")
    UnavailablePriorities = field("UnavailablePriorities")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DnsRuleGroupPriorityConflictViolationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DnsRuleGroupPriorityConflictViolationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvaluationResult:
    boto3_raw_data: "type_defs.EvaluationResultTypeDef" = dataclasses.field()

    ComplianceStatus = field("ComplianceStatus")
    ViolatorCount = field("ViolatorCount")
    EvaluationLimitExceeded = field("EvaluationLimitExceeded")

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
class ExpectedRoute:
    boto3_raw_data: "type_defs.ExpectedRouteTypeDef" = dataclasses.field()

    IpV4Cidr = field("IpV4Cidr")
    PrefixListId = field("PrefixListId")
    IpV6Cidr = field("IpV6Cidr")
    ContributingSubnets = field("ContributingSubnets")
    AllowedTargets = field("AllowedTargets")
    RouteTableId = field("RouteTableId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExpectedRouteTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ExpectedRouteTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FMSPolicyUpdateFirewallCreationConfigAction:
    boto3_raw_data: "type_defs.FMSPolicyUpdateFirewallCreationConfigActionTypeDef" = (
        dataclasses.field()
    )

    Description = field("Description")
    FirewallCreationConfig = field("FirewallCreationConfig")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.FMSPolicyUpdateFirewallCreationConfigActionTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FMSPolicyUpdateFirewallCreationConfigActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FirewallSubnetIsOutOfScopeViolation:
    boto3_raw_data: "type_defs.FirewallSubnetIsOutOfScopeViolationTypeDef" = (
        dataclasses.field()
    )

    FirewallSubnetId = field("FirewallSubnetId")
    VpcId = field("VpcId")
    SubnetAvailabilityZone = field("SubnetAvailabilityZone")
    SubnetAvailabilityZoneId = field("SubnetAvailabilityZoneId")
    VpcEndpointId = field("VpcEndpointId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.FirewallSubnetIsOutOfScopeViolationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FirewallSubnetIsOutOfScopeViolationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FirewallSubnetMissingVPCEndpointViolation:
    boto3_raw_data: "type_defs.FirewallSubnetMissingVPCEndpointViolationTypeDef" = (
        dataclasses.field()
    )

    FirewallSubnetId = field("FirewallSubnetId")
    VpcId = field("VpcId")
    SubnetAvailabilityZone = field("SubnetAvailabilityZone")
    SubnetAvailabilityZoneId = field("SubnetAvailabilityZoneId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.FirewallSubnetMissingVPCEndpointViolationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FirewallSubnetMissingVPCEndpointViolationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAdminScopeRequest:
    boto3_raw_data: "type_defs.GetAdminScopeRequestTypeDef" = dataclasses.field()

    AdminAccount = field("AdminAccount")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAdminScopeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAdminScopeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAppsListRequest:
    boto3_raw_data: "type_defs.GetAppsListRequestTypeDef" = dataclasses.field()

    ListId = field("ListId")
    DefaultList = field("DefaultList")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAppsListRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAppsListRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetComplianceDetailRequest:
    boto3_raw_data: "type_defs.GetComplianceDetailRequestTypeDef" = dataclasses.field()

    PolicyId = field("PolicyId")
    MemberAccount = field("MemberAccount")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetComplianceDetailRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetComplianceDetailRequestTypeDef"]
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

    PolicyId = field("PolicyId")

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
class GetProtocolsListRequest:
    boto3_raw_data: "type_defs.GetProtocolsListRequestTypeDef" = dataclasses.field()

    ListId = field("ListId")
    DefaultList = field("DefaultList")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetProtocolsListRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetProtocolsListRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProtocolsListDataOutput:
    boto3_raw_data: "type_defs.ProtocolsListDataOutputTypeDef" = dataclasses.field()

    ListName = field("ListName")
    ProtocolsList = field("ProtocolsList")
    ListId = field("ListId")
    ListUpdateToken = field("ListUpdateToken")
    CreateTime = field("CreateTime")
    LastUpdateTime = field("LastUpdateTime")
    PreviousProtocolsList = field("PreviousProtocolsList")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProtocolsListDataOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProtocolsListDataOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResourceSetRequest:
    boto3_raw_data: "type_defs.GetResourceSetRequestTypeDef" = dataclasses.field()

    Identifier = field("Identifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetResourceSetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResourceSetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceSetOutput:
    boto3_raw_data: "type_defs.ResourceSetOutputTypeDef" = dataclasses.field()

    Name = field("Name")
    ResourceTypeList = field("ResourceTypeList")
    Id = field("Id")
    Description = field("Description")
    UpdateToken = field("UpdateToken")
    LastUpdateTime = field("LastUpdateTime")
    ResourceSetStatus = field("ResourceSetStatus")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResourceSetOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceSetOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetThirdPartyFirewallAssociationStatusRequest:
    boto3_raw_data: "type_defs.GetThirdPartyFirewallAssociationStatusRequestTypeDef" = (
        dataclasses.field()
    )

    ThirdPartyFirewall = field("ThirdPartyFirewall")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetThirdPartyFirewallAssociationStatusRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetThirdPartyFirewallAssociationStatusRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetViolationDetailsRequest:
    boto3_raw_data: "type_defs.GetViolationDetailsRequestTypeDef" = dataclasses.field()

    PolicyId = field("PolicyId")
    MemberAccount = field("MemberAccount")
    ResourceId = field("ResourceId")
    ResourceType = field("ResourceType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetViolationDetailsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetViolationDetailsRequestTypeDef"]
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
class ListAdminAccountsForOrganizationRequest:
    boto3_raw_data: "type_defs.ListAdminAccountsForOrganizationRequestTypeDef" = (
        dataclasses.field()
    )

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAdminAccountsForOrganizationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAdminAccountsForOrganizationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAdminsManagingAccountRequest:
    boto3_raw_data: "type_defs.ListAdminsManagingAccountRequestTypeDef" = (
        dataclasses.field()
    )

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAdminsManagingAccountRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAdminsManagingAccountRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAppsListsRequest:
    boto3_raw_data: "type_defs.ListAppsListsRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    DefaultLists = field("DefaultLists")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAppsListsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAppsListsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListComplianceStatusRequest:
    boto3_raw_data: "type_defs.ListComplianceStatusRequestTypeDef" = dataclasses.field()

    PolicyId = field("PolicyId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListComplianceStatusRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListComplianceStatusRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDiscoveredResourcesRequest:
    boto3_raw_data: "type_defs.ListDiscoveredResourcesRequestTypeDef" = (
        dataclasses.field()
    )

    MemberAccountIds = field("MemberAccountIds")
    ResourceType = field("ResourceType")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListDiscoveredResourcesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDiscoveredResourcesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMemberAccountsRequest:
    boto3_raw_data: "type_defs.ListMemberAccountsRequestTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMemberAccountsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMemberAccountsRequestTypeDef"]
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

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

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
class PolicySummary:
    boto3_raw_data: "type_defs.PolicySummaryTypeDef" = dataclasses.field()

    PolicyArn = field("PolicyArn")
    PolicyId = field("PolicyId")
    PolicyName = field("PolicyName")
    ResourceType = field("ResourceType")
    SecurityServiceType = field("SecurityServiceType")
    RemediationEnabled = field("RemediationEnabled")
    DeleteUnusedFMManagedResources = field("DeleteUnusedFMManagedResources")
    PolicyStatus = field("PolicyStatus")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PolicySummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PolicySummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProtocolsListsRequest:
    boto3_raw_data: "type_defs.ListProtocolsListsRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    DefaultLists = field("DefaultLists")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListProtocolsListsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProtocolsListsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProtocolsListDataSummary:
    boto3_raw_data: "type_defs.ProtocolsListDataSummaryTypeDef" = dataclasses.field()

    ListArn = field("ListArn")
    ListId = field("ListId")
    ListName = field("ListName")
    ProtocolsList = field("ProtocolsList")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProtocolsListDataSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProtocolsListDataSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourceSetResourcesRequest:
    boto3_raw_data: "type_defs.ListResourceSetResourcesRequestTypeDef" = (
        dataclasses.field()
    )

    Identifier = field("Identifier")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListResourceSetResourcesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourceSetResourcesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Resource:
    boto3_raw_data: "type_defs.ResourceTypeDef" = dataclasses.field()

    URI = field("URI")
    AccountId = field("AccountId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResourceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourceSetsRequest:
    boto3_raw_data: "type_defs.ListResourceSetsRequestTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListResourceSetsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourceSetsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceSetSummary:
    boto3_raw_data: "type_defs.ResourceSetSummaryTypeDef" = dataclasses.field()

    Id = field("Id")
    Name = field("Name")
    Description = field("Description")
    LastUpdateTime = field("LastUpdateTime")
    ResourceSetStatus = field("ResourceSetStatus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResourceSetSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceSetSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceRequest:
    boto3_raw_data: "type_defs.ListTagsForResourceRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForResourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceRequestTypeDef"]
        ],
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
class ListThirdPartyFirewallFirewallPoliciesRequest:
    boto3_raw_data: "type_defs.ListThirdPartyFirewallFirewallPoliciesRequestTypeDef" = (
        dataclasses.field()
    )

    ThirdPartyFirewall = field("ThirdPartyFirewall")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListThirdPartyFirewallFirewallPoliciesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListThirdPartyFirewallFirewallPoliciesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ThirdPartyFirewallFirewallPolicy:
    boto3_raw_data: "type_defs.ThirdPartyFirewallFirewallPolicyTypeDef" = (
        dataclasses.field()
    )

    FirewallPolicyId = field("FirewallPolicyId")
    FirewallPolicyName = field("FirewallPolicyName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ThirdPartyFirewallFirewallPolicyTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ThirdPartyFirewallFirewallPolicyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NetworkAclIcmpTypeCode:
    boto3_raw_data: "type_defs.NetworkAclIcmpTypeCodeTypeDef" = dataclasses.field()

    Code = field("Code")
    Type = field("Type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NetworkAclIcmpTypeCodeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NetworkAclIcmpTypeCodeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NetworkAclPortRange:
    boto3_raw_data: "type_defs.NetworkAclPortRangeTypeDef" = dataclasses.field()

    From = field("From")
    To = field("To")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NetworkAclPortRangeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NetworkAclPortRangeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Route:
    boto3_raw_data: "type_defs.RouteTypeDef" = dataclasses.field()

    DestinationType = field("DestinationType")
    TargetType = field("TargetType")
    Destination = field("Destination")
    Target = field("Target")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RouteTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RouteTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NetworkFirewallMissingExpectedRTViolation:
    boto3_raw_data: "type_defs.NetworkFirewallMissingExpectedRTViolationTypeDef" = (
        dataclasses.field()
    )

    ViolationTarget = field("ViolationTarget")
    VPC = field("VPC")
    AvailabilityZone = field("AvailabilityZone")
    CurrentRouteTable = field("CurrentRouteTable")
    ExpectedRouteTable = field("ExpectedRouteTable")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.NetworkFirewallMissingExpectedRTViolationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NetworkFirewallMissingExpectedRTViolationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NetworkFirewallMissingFirewallViolation:
    boto3_raw_data: "type_defs.NetworkFirewallMissingFirewallViolationTypeDef" = (
        dataclasses.field()
    )

    ViolationTarget = field("ViolationTarget")
    VPC = field("VPC")
    AvailabilityZone = field("AvailabilityZone")
    TargetViolationReason = field("TargetViolationReason")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.NetworkFirewallMissingFirewallViolationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NetworkFirewallMissingFirewallViolationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NetworkFirewallMissingSubnetViolation:
    boto3_raw_data: "type_defs.NetworkFirewallMissingSubnetViolationTypeDef" = (
        dataclasses.field()
    )

    ViolationTarget = field("ViolationTarget")
    VPC = field("VPC")
    AvailabilityZone = field("AvailabilityZone")
    TargetViolationReason = field("TargetViolationReason")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.NetworkFirewallMissingSubnetViolationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NetworkFirewallMissingSubnetViolationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StatefulEngineOptions:
    boto3_raw_data: "type_defs.StatefulEngineOptionsTypeDef" = dataclasses.field()

    RuleOrder = field("RuleOrder")
    StreamExceptionPolicy = field("StreamExceptionPolicy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StatefulEngineOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StatefulEngineOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StatelessRuleGroup:
    boto3_raw_data: "type_defs.StatelessRuleGroupTypeDef" = dataclasses.field()

    RuleGroupName = field("RuleGroupName")
    ResourceId = field("ResourceId")
    Priority = field("Priority")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StatelessRuleGroupTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StatelessRuleGroupTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NetworkFirewallPolicy:
    boto3_raw_data: "type_defs.NetworkFirewallPolicyTypeDef" = dataclasses.field()

    FirewallDeploymentModel = field("FirewallDeploymentModel")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NetworkFirewallPolicyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NetworkFirewallPolicyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NetworkFirewallStatefulRuleGroupOverride:
    boto3_raw_data: "type_defs.NetworkFirewallStatefulRuleGroupOverrideTypeDef" = (
        dataclasses.field()
    )

    Action = field("Action")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.NetworkFirewallStatefulRuleGroupOverrideTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NetworkFirewallStatefulRuleGroupOverrideTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ThirdPartyFirewallPolicy:
    boto3_raw_data: "type_defs.ThirdPartyFirewallPolicyTypeDef" = dataclasses.field()

    FirewallDeploymentModel = field("FirewallDeploymentModel")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ThirdPartyFirewallPolicyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ThirdPartyFirewallPolicyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceTag:
    boto3_raw_data: "type_defs.ResourceTagTypeDef" = dataclasses.field()

    Key = field("Key")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResourceTagTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResourceTagTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutNotificationChannelRequest:
    boto3_raw_data: "type_defs.PutNotificationChannelRequestTypeDef" = (
        dataclasses.field()
    )

    SnsTopicArn = field("SnsTopicArn")
    SnsRoleName = field("SnsRoleName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PutNotificationChannelRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutNotificationChannelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ThirdPartyFirewallMissingExpectedRouteTableViolation:
    boto3_raw_data: (
        "type_defs.ThirdPartyFirewallMissingExpectedRouteTableViolationTypeDef"
    ) = dataclasses.field()

    ViolationTarget = field("ViolationTarget")
    VPC = field("VPC")
    AvailabilityZone = field("AvailabilityZone")
    CurrentRouteTable = field("CurrentRouteTable")
    ExpectedRouteTable = field("ExpectedRouteTable")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ThirdPartyFirewallMissingExpectedRouteTableViolationTypeDef"
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
                "type_defs.ThirdPartyFirewallMissingExpectedRouteTableViolationTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ThirdPartyFirewallMissingFirewallViolation:
    boto3_raw_data: "type_defs.ThirdPartyFirewallMissingFirewallViolationTypeDef" = (
        dataclasses.field()
    )

    ViolationTarget = field("ViolationTarget")
    VPC = field("VPC")
    AvailabilityZone = field("AvailabilityZone")
    TargetViolationReason = field("TargetViolationReason")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ThirdPartyFirewallMissingFirewallViolationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ThirdPartyFirewallMissingFirewallViolationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ThirdPartyFirewallMissingSubnetViolation:
    boto3_raw_data: "type_defs.ThirdPartyFirewallMissingSubnetViolationTypeDef" = (
        dataclasses.field()
    )

    ViolationTarget = field("ViolationTarget")
    VPC = field("VPC")
    AvailabilityZone = field("AvailabilityZone")
    TargetViolationReason = field("TargetViolationReason")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ThirdPartyFirewallMissingSubnetViolationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ThirdPartyFirewallMissingSubnetViolationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WebACLHasIncompatibleConfigurationViolation:
    boto3_raw_data: "type_defs.WebACLHasIncompatibleConfigurationViolationTypeDef" = (
        dataclasses.field()
    )

    WebACLArn = field("WebACLArn")
    Description = field("Description")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.WebACLHasIncompatibleConfigurationViolationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WebACLHasIncompatibleConfigurationViolationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WebACLHasOutOfScopeResourcesViolation:
    boto3_raw_data: "type_defs.WebACLHasOutOfScopeResourcesViolationTypeDef" = (
        dataclasses.field()
    )

    WebACLArn = field("WebACLArn")
    OutOfScopeResourceList = field("OutOfScopeResourceList")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.WebACLHasOutOfScopeResourcesViolationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WebACLHasOutOfScopeResourcesViolationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SecurityGroupRuleDescription:
    boto3_raw_data: "type_defs.SecurityGroupRuleDescriptionTypeDef" = (
        dataclasses.field()
    )

    IPV4Range = field("IPV4Range")
    IPV6Range = field("IPV6Range")
    PrefixListId = field("PrefixListId")
    Protocol = field("Protocol")
    FromPort = field("FromPort")
    ToPort = field("ToPort")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SecurityGroupRuleDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SecurityGroupRuleDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UntagResourceRequest:
    boto3_raw_data: "type_defs.UntagResourceRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")
    TagKeys = field("TagKeys")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UntagResourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UntagResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateNetworkAclAction:
    boto3_raw_data: "type_defs.CreateNetworkAclActionTypeDef" = dataclasses.field()

    Description = field("Description")

    @cached_property
    def Vpc(self):  # pragma: no cover
        return ActionTarget.make_one(self.boto3_raw_data["Vpc"])

    FMSCanRemediate = field("FMSCanRemediate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateNetworkAclActionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateNetworkAclActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EC2AssociateRouteTableAction:
    boto3_raw_data: "type_defs.EC2AssociateRouteTableActionTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def RouteTableId(self):  # pragma: no cover
        return ActionTarget.make_one(self.boto3_raw_data["RouteTableId"])

    Description = field("Description")

    @cached_property
    def SubnetId(self):  # pragma: no cover
        return ActionTarget.make_one(self.boto3_raw_data["SubnetId"])

    @cached_property
    def GatewayId(self):  # pragma: no cover
        return ActionTarget.make_one(self.boto3_raw_data["GatewayId"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EC2AssociateRouteTableActionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EC2AssociateRouteTableActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EC2CopyRouteTableAction:
    boto3_raw_data: "type_defs.EC2CopyRouteTableActionTypeDef" = dataclasses.field()

    @cached_property
    def VpcId(self):  # pragma: no cover
        return ActionTarget.make_one(self.boto3_raw_data["VpcId"])

    @cached_property
    def RouteTableId(self):  # pragma: no cover
        return ActionTarget.make_one(self.boto3_raw_data["RouteTableId"])

    Description = field("Description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EC2CopyRouteTableActionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EC2CopyRouteTableActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EC2CreateRouteAction:
    boto3_raw_data: "type_defs.EC2CreateRouteActionTypeDef" = dataclasses.field()

    @cached_property
    def RouteTableId(self):  # pragma: no cover
        return ActionTarget.make_one(self.boto3_raw_data["RouteTableId"])

    Description = field("Description")
    DestinationCidrBlock = field("DestinationCidrBlock")
    DestinationPrefixListId = field("DestinationPrefixListId")
    DestinationIpv6CidrBlock = field("DestinationIpv6CidrBlock")

    @cached_property
    def VpcEndpointId(self):  # pragma: no cover
        return ActionTarget.make_one(self.boto3_raw_data["VpcEndpointId"])

    @cached_property
    def GatewayId(self):  # pragma: no cover
        return ActionTarget.make_one(self.boto3_raw_data["GatewayId"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EC2CreateRouteActionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EC2CreateRouteActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EC2CreateRouteTableAction:
    boto3_raw_data: "type_defs.EC2CreateRouteTableActionTypeDef" = dataclasses.field()

    @cached_property
    def VpcId(self):  # pragma: no cover
        return ActionTarget.make_one(self.boto3_raw_data["VpcId"])

    Description = field("Description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EC2CreateRouteTableActionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EC2CreateRouteTableActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EC2DeleteRouteAction:
    boto3_raw_data: "type_defs.EC2DeleteRouteActionTypeDef" = dataclasses.field()

    @cached_property
    def RouteTableId(self):  # pragma: no cover
        return ActionTarget.make_one(self.boto3_raw_data["RouteTableId"])

    Description = field("Description")
    DestinationCidrBlock = field("DestinationCidrBlock")
    DestinationPrefixListId = field("DestinationPrefixListId")
    DestinationIpv6CidrBlock = field("DestinationIpv6CidrBlock")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EC2DeleteRouteActionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EC2DeleteRouteActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EC2ReplaceRouteAction:
    boto3_raw_data: "type_defs.EC2ReplaceRouteActionTypeDef" = dataclasses.field()

    @cached_property
    def RouteTableId(self):  # pragma: no cover
        return ActionTarget.make_one(self.boto3_raw_data["RouteTableId"])

    Description = field("Description")
    DestinationCidrBlock = field("DestinationCidrBlock")
    DestinationPrefixListId = field("DestinationPrefixListId")
    DestinationIpv6CidrBlock = field("DestinationIpv6CidrBlock")

    @cached_property
    def GatewayId(self):  # pragma: no cover
        return ActionTarget.make_one(self.boto3_raw_data["GatewayId"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EC2ReplaceRouteActionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EC2ReplaceRouteActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EC2ReplaceRouteTableAssociationAction:
    boto3_raw_data: "type_defs.EC2ReplaceRouteTableAssociationActionTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AssociationId(self):  # pragma: no cover
        return ActionTarget.make_one(self.boto3_raw_data["AssociationId"])

    @cached_property
    def RouteTableId(self):  # pragma: no cover
        return ActionTarget.make_one(self.boto3_raw_data["RouteTableId"])

    Description = field("Description")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.EC2ReplaceRouteTableAssociationActionTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EC2ReplaceRouteTableAssociationActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplaceNetworkAclAssociationAction:
    boto3_raw_data: "type_defs.ReplaceNetworkAclAssociationActionTypeDef" = (
        dataclasses.field()
    )

    Description = field("Description")

    @cached_property
    def AssociationId(self):  # pragma: no cover
        return ActionTarget.make_one(self.boto3_raw_data["AssociationId"])

    @cached_property
    def NetworkAclId(self):  # pragma: no cover
        return ActionTarget.make_one(self.boto3_raw_data["NetworkAclId"])

    FMSCanRemediate = field("FMSCanRemediate")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ReplaceNetworkAclAssociationActionTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplaceNetworkAclAssociationActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AdminScopeOutput:
    boto3_raw_data: "type_defs.AdminScopeOutputTypeDef" = dataclasses.field()

    @cached_property
    def AccountScope(self):  # pragma: no cover
        return AccountScopeOutput.make_one(self.boto3_raw_data["AccountScope"])

    @cached_property
    def OrganizationalUnitScope(self):  # pragma: no cover
        return OrganizationalUnitScopeOutput.make_one(
            self.boto3_raw_data["OrganizationalUnitScope"]
        )

    @cached_property
    def RegionScope(self):  # pragma: no cover
        return RegionScopeOutput.make_one(self.boto3_raw_data["RegionScope"])

    @cached_property
    def PolicyTypeScope(self):  # pragma: no cover
        return PolicyTypeScopeOutput.make_one(self.boto3_raw_data["PolicyTypeScope"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AdminScopeOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AdminScopeOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AdminScope:
    boto3_raw_data: "type_defs.AdminScopeTypeDef" = dataclasses.field()

    @cached_property
    def AccountScope(self):  # pragma: no cover
        return AccountScope.make_one(self.boto3_raw_data["AccountScope"])

    @cached_property
    def OrganizationalUnitScope(self):  # pragma: no cover
        return OrganizationalUnitScope.make_one(
            self.boto3_raw_data["OrganizationalUnitScope"]
        )

    @cached_property
    def RegionScope(self):  # pragma: no cover
        return RegionScope.make_one(self.boto3_raw_data["RegionScope"])

    @cached_property
    def PolicyTypeScope(self):  # pragma: no cover
        return PolicyTypeScope.make_one(self.boto3_raw_data["PolicyTypeScope"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AdminScopeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AdminScopeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AppsListDataOutput:
    boto3_raw_data: "type_defs.AppsListDataOutputTypeDef" = dataclasses.field()

    ListName = field("ListName")

    @cached_property
    def AppsList(self):  # pragma: no cover
        return App.make_many(self.boto3_raw_data["AppsList"])

    ListId = field("ListId")
    ListUpdateToken = field("ListUpdateToken")
    CreateTime = field("CreateTime")
    LastUpdateTime = field("LastUpdateTime")
    PreviousAppsList = field("PreviousAppsList")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AppsListDataOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AppsListDataOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AppsListDataSummary:
    boto3_raw_data: "type_defs.AppsListDataSummaryTypeDef" = dataclasses.field()

    ListArn = field("ListArn")
    ListId = field("ListId")
    ListName = field("ListName")

    @cached_property
    def AppsList(self):  # pragma: no cover
        return App.make_many(self.boto3_raw_data["AppsList"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AppsListDataSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AppsListDataSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AppsListData:
    boto3_raw_data: "type_defs.AppsListDataTypeDef" = dataclasses.field()

    ListName = field("ListName")

    @cached_property
    def AppsList(self):  # pragma: no cover
        return App.make_many(self.boto3_raw_data["AppsList"])

    ListId = field("ListId")
    ListUpdateToken = field("ListUpdateToken")
    CreateTime = field("CreateTime")
    LastUpdateTime = field("LastUpdateTime")
    PreviousAppsList = field("PreviousAppsList")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AppsListDataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AppsListDataTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetProtectionStatusRequest:
    boto3_raw_data: "type_defs.GetProtectionStatusRequestTypeDef" = dataclasses.field()

    PolicyId = field("PolicyId")
    MemberAccountId = field("MemberAccountId")
    StartTime = field("StartTime")
    EndTime = field("EndTime")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetProtectionStatusRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetProtectionStatusRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProtocolsListData:
    boto3_raw_data: "type_defs.ProtocolsListDataTypeDef" = dataclasses.field()

    ListName = field("ListName")
    ProtocolsList = field("ProtocolsList")
    ListId = field("ListId")
    ListUpdateToken = field("ListUpdateToken")
    CreateTime = field("CreateTime")
    LastUpdateTime = field("LastUpdateTime")
    PreviousProtocolsList = field("PreviousProtocolsList")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ProtocolsListDataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProtocolsListDataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceSet:
    boto3_raw_data: "type_defs.ResourceSetTypeDef" = dataclasses.field()

    Name = field("Name")
    ResourceTypeList = field("ResourceTypeList")
    Id = field("Id")
    Description = field("Description")
    UpdateToken = field("UpdateToken")
    LastUpdateTime = field("LastUpdateTime")
    ResourceSetStatus = field("ResourceSetStatus")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResourceSetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResourceSetTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateThirdPartyFirewallResponse:
    boto3_raw_data: "type_defs.AssociateThirdPartyFirewallResponseTypeDef" = (
        dataclasses.field()
    )

    ThirdPartyFirewallStatus = field("ThirdPartyFirewallStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateThirdPartyFirewallResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateThirdPartyFirewallResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateThirdPartyFirewallResponse:
    boto3_raw_data: "type_defs.DisassociateThirdPartyFirewallResponseTypeDef" = (
        dataclasses.field()
    )

    ThirdPartyFirewallStatus = field("ThirdPartyFirewallStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateThirdPartyFirewallResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateThirdPartyFirewallResponseTypeDef"]
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
class GetAdminAccountResponse:
    boto3_raw_data: "type_defs.GetAdminAccountResponseTypeDef" = dataclasses.field()

    AdminAccount = field("AdminAccount")
    RoleStatus = field("RoleStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAdminAccountResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAdminAccountResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetNotificationChannelResponse:
    boto3_raw_data: "type_defs.GetNotificationChannelResponseTypeDef" = (
        dataclasses.field()
    )

    SnsTopicArn = field("SnsTopicArn")
    SnsRoleName = field("SnsRoleName")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetNotificationChannelResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetNotificationChannelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetProtectionStatusResponse:
    boto3_raw_data: "type_defs.GetProtectionStatusResponseTypeDef" = dataclasses.field()

    AdminAccountId = field("AdminAccountId")
    ServiceType = field("ServiceType")
    Data = field("Data")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetProtectionStatusResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetProtectionStatusResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetThirdPartyFirewallAssociationStatusResponse:
    boto3_raw_data: (
        "type_defs.GetThirdPartyFirewallAssociationStatusResponseTypeDef"
    ) = dataclasses.field()

    ThirdPartyFirewallStatus = field("ThirdPartyFirewallStatus")
    MarketplaceOnboardingStatus = field("MarketplaceOnboardingStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetThirdPartyFirewallAssociationStatusResponseTypeDef"
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
                "type_defs.GetThirdPartyFirewallAssociationStatusResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAdminAccountsForOrganizationResponse:
    boto3_raw_data: "type_defs.ListAdminAccountsForOrganizationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AdminAccounts(self):  # pragma: no cover
        return AdminAccountSummary.make_many(self.boto3_raw_data["AdminAccounts"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAdminAccountsForOrganizationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAdminAccountsForOrganizationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAdminsManagingAccountResponse:
    boto3_raw_data: "type_defs.ListAdminsManagingAccountResponseTypeDef" = (
        dataclasses.field()
    )

    AdminAccounts = field("AdminAccounts")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAdminsManagingAccountResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAdminsManagingAccountResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMemberAccountsResponse:
    boto3_raw_data: "type_defs.ListMemberAccountsResponseTypeDef" = dataclasses.field()

    MemberAccounts = field("MemberAccounts")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMemberAccountsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMemberAccountsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AwsEc2InstanceViolation:
    boto3_raw_data: "type_defs.AwsEc2InstanceViolationTypeDef" = dataclasses.field()

    ViolationTarget = field("ViolationTarget")

    @cached_property
    def AwsEc2NetworkInterfaceViolations(self):  # pragma: no cover
        return AwsEc2NetworkInterfaceViolation.make_many(
            self.boto3_raw_data["AwsEc2NetworkInterfaceViolations"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AwsEc2InstanceViolationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AwsEc2InstanceViolationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchAssociateResourceResponse:
    boto3_raw_data: "type_defs.BatchAssociateResourceResponseTypeDef" = (
        dataclasses.field()
    )

    ResourceSetIdentifier = field("ResourceSetIdentifier")

    @cached_property
    def FailedItems(self):  # pragma: no cover
        return FailedItem.make_many(self.boto3_raw_data["FailedItems"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchAssociateResourceResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchAssociateResourceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDisassociateResourceResponse:
    boto3_raw_data: "type_defs.BatchDisassociateResourceResponseTypeDef" = (
        dataclasses.field()
    )

    ResourceSetIdentifier = field("ResourceSetIdentifier")

    @cached_property
    def FailedItems(self):  # pragma: no cover
        return FailedItem.make_many(self.boto3_raw_data["FailedItems"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchDisassociateResourceResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDisassociateResourceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PolicyComplianceDetail:
    boto3_raw_data: "type_defs.PolicyComplianceDetailTypeDef" = dataclasses.field()

    PolicyOwner = field("PolicyOwner")
    PolicyId = field("PolicyId")
    MemberAccount = field("MemberAccount")

    @cached_property
    def Violators(self):  # pragma: no cover
        return ComplianceViolator.make_many(self.boto3_raw_data["Violators"])

    EvaluationLimitExceeded = field("EvaluationLimitExceeded")
    ExpiredAt = field("ExpiredAt")
    IssueInfoMap = field("IssueInfoMap")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PolicyComplianceDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PolicyComplianceDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDiscoveredResourcesResponse:
    boto3_raw_data: "type_defs.ListDiscoveredResourcesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Items(self):  # pragma: no cover
        return DiscoveredResource.make_many(self.boto3_raw_data["Items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListDiscoveredResourcesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDiscoveredResourcesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PolicyComplianceStatus:
    boto3_raw_data: "type_defs.PolicyComplianceStatusTypeDef" = dataclasses.field()

    PolicyOwner = field("PolicyOwner")
    PolicyId = field("PolicyId")
    PolicyName = field("PolicyName")
    MemberAccount = field("MemberAccount")

    @cached_property
    def EvaluationResults(self):  # pragma: no cover
        return EvaluationResult.make_many(self.boto3_raw_data["EvaluationResults"])

    LastUpdated = field("LastUpdated")
    IssueInfoMap = field("IssueInfoMap")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PolicyComplianceStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PolicyComplianceStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NetworkFirewallMissingExpectedRoutesViolation:
    boto3_raw_data: "type_defs.NetworkFirewallMissingExpectedRoutesViolationTypeDef" = (
        dataclasses.field()
    )

    ViolationTarget = field("ViolationTarget")

    @cached_property
    def ExpectedRoutes(self):  # pragma: no cover
        return ExpectedRoute.make_many(self.boto3_raw_data["ExpectedRoutes"])

    VpcId = field("VpcId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.NetworkFirewallMissingExpectedRoutesViolationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NetworkFirewallMissingExpectedRoutesViolationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetProtocolsListResponse:
    boto3_raw_data: "type_defs.GetProtocolsListResponseTypeDef" = dataclasses.field()

    @cached_property
    def ProtocolsList(self):  # pragma: no cover
        return ProtocolsListDataOutput.make_one(self.boto3_raw_data["ProtocolsList"])

    ProtocolsListArn = field("ProtocolsListArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetProtocolsListResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetProtocolsListResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutProtocolsListResponse:
    boto3_raw_data: "type_defs.PutProtocolsListResponseTypeDef" = dataclasses.field()

    @cached_property
    def ProtocolsList(self):  # pragma: no cover
        return ProtocolsListDataOutput.make_one(self.boto3_raw_data["ProtocolsList"])

    ProtocolsListArn = field("ProtocolsListArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutProtocolsListResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutProtocolsListResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResourceSetResponse:
    boto3_raw_data: "type_defs.GetResourceSetResponseTypeDef" = dataclasses.field()

    @cached_property
    def ResourceSet(self):  # pragma: no cover
        return ResourceSetOutput.make_one(self.boto3_raw_data["ResourceSet"])

    ResourceSetArn = field("ResourceSetArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetResourceSetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResourceSetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutResourceSetResponse:
    boto3_raw_data: "type_defs.PutResourceSetResponseTypeDef" = dataclasses.field()

    @cached_property
    def ResourceSet(self):  # pragma: no cover
        return ResourceSetOutput.make_one(self.boto3_raw_data["ResourceSet"])

    ResourceSetArn = field("ResourceSetArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutResourceSetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutResourceSetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAdminAccountsForOrganizationRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListAdminAccountsForOrganizationRequestPaginateTypeDef"
    ) = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAdminAccountsForOrganizationRequestPaginateTypeDef"
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
                "type_defs.ListAdminAccountsForOrganizationRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAdminsManagingAccountRequestPaginate:
    boto3_raw_data: "type_defs.ListAdminsManagingAccountRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAdminsManagingAccountRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAdminsManagingAccountRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAppsListsRequestPaginate:
    boto3_raw_data: "type_defs.ListAppsListsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    DefaultLists = field("DefaultLists")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAppsListsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAppsListsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListComplianceStatusRequestPaginate:
    boto3_raw_data: "type_defs.ListComplianceStatusRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    PolicyId = field("PolicyId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListComplianceStatusRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListComplianceStatusRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMemberAccountsRequestPaginate:
    boto3_raw_data: "type_defs.ListMemberAccountsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListMemberAccountsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMemberAccountsRequestPaginateTypeDef"]
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
class ListProtocolsListsRequestPaginate:
    boto3_raw_data: "type_defs.ListProtocolsListsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    DefaultLists = field("DefaultLists")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListProtocolsListsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProtocolsListsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListThirdPartyFirewallFirewallPoliciesRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListThirdPartyFirewallFirewallPoliciesRequestPaginateTypeDef"
    ) = dataclasses.field()

    ThirdPartyFirewall = field("ThirdPartyFirewall")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListThirdPartyFirewallFirewallPoliciesRequestPaginateTypeDef"
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
                "type_defs.ListThirdPartyFirewallFirewallPoliciesRequestPaginateTypeDef"
            ]
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
    def PolicyList(self):  # pragma: no cover
        return PolicySummary.make_many(self.boto3_raw_data["PolicyList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

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
class ListProtocolsListsResponse:
    boto3_raw_data: "type_defs.ListProtocolsListsResponseTypeDef" = dataclasses.field()

    @cached_property
    def ProtocolsLists(self):  # pragma: no cover
        return ProtocolsListDataSummary.make_many(self.boto3_raw_data["ProtocolsLists"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListProtocolsListsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProtocolsListsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourceSetResourcesResponse:
    boto3_raw_data: "type_defs.ListResourceSetResourcesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Items(self):  # pragma: no cover
        return Resource.make_many(self.boto3_raw_data["Items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListResourceSetResourcesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourceSetResourcesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourceSetsResponse:
    boto3_raw_data: "type_defs.ListResourceSetsResponseTypeDef" = dataclasses.field()

    @cached_property
    def ResourceSets(self):  # pragma: no cover
        return ResourceSetSummary.make_many(self.boto3_raw_data["ResourceSets"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListResourceSetsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourceSetsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceResponse:
    boto3_raw_data: "type_defs.ListTagsForResourceResponseTypeDef" = dataclasses.field()

    @cached_property
    def TagList(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["TagList"])

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
class TagResourceRequest:
    boto3_raw_data: "type_defs.TagResourceRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")

    @cached_property
    def TagList(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["TagList"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TagResourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TagResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListThirdPartyFirewallFirewallPoliciesResponse:
    boto3_raw_data: (
        "type_defs.ListThirdPartyFirewallFirewallPoliciesResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def ThirdPartyFirewallFirewallPolicies(self):  # pragma: no cover
        return ThirdPartyFirewallFirewallPolicy.make_many(
            self.boto3_raw_data["ThirdPartyFirewallFirewallPolicies"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListThirdPartyFirewallFirewallPoliciesResponseTypeDef"
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
                "type_defs.ListThirdPartyFirewallFirewallPoliciesResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NetworkAclEntry:
    boto3_raw_data: "type_defs.NetworkAclEntryTypeDef" = dataclasses.field()

    Protocol = field("Protocol")
    RuleAction = field("RuleAction")
    Egress = field("Egress")

    @cached_property
    def IcmpTypeCode(self):  # pragma: no cover
        return NetworkAclIcmpTypeCode.make_one(self.boto3_raw_data["IcmpTypeCode"])

    @cached_property
    def PortRange(self):  # pragma: no cover
        return NetworkAclPortRange.make_one(self.boto3_raw_data["PortRange"])

    CidrBlock = field("CidrBlock")
    Ipv6CidrBlock = field("Ipv6CidrBlock")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NetworkAclEntryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.NetworkAclEntryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NetworkFirewallBlackHoleRouteDetectedViolation:
    boto3_raw_data: (
        "type_defs.NetworkFirewallBlackHoleRouteDetectedViolationTypeDef"
    ) = dataclasses.field()

    ViolationTarget = field("ViolationTarget")
    RouteTableId = field("RouteTableId")
    VpcId = field("VpcId")

    @cached_property
    def ViolatingRoutes(self):  # pragma: no cover
        return Route.make_many(self.boto3_raw_data["ViolatingRoutes"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.NetworkFirewallBlackHoleRouteDetectedViolationTypeDef"
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
                "type_defs.NetworkFirewallBlackHoleRouteDetectedViolationTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NetworkFirewallInternetTrafficNotInspectedViolation:
    boto3_raw_data: (
        "type_defs.NetworkFirewallInternetTrafficNotInspectedViolationTypeDef"
    ) = dataclasses.field()

    SubnetId = field("SubnetId")
    SubnetAvailabilityZone = field("SubnetAvailabilityZone")
    RouteTableId = field("RouteTableId")

    @cached_property
    def ViolatingRoutes(self):  # pragma: no cover
        return Route.make_many(self.boto3_raw_data["ViolatingRoutes"])

    IsRouteTableUsedInDifferentAZ = field("IsRouteTableUsedInDifferentAZ")
    CurrentFirewallSubnetRouteTable = field("CurrentFirewallSubnetRouteTable")
    ExpectedFirewallEndpoint = field("ExpectedFirewallEndpoint")
    FirewallSubnetId = field("FirewallSubnetId")

    @cached_property
    def ExpectedFirewallSubnetRoutes(self):  # pragma: no cover
        return ExpectedRoute.make_many(
            self.boto3_raw_data["ExpectedFirewallSubnetRoutes"]
        )

    @cached_property
    def ActualFirewallSubnetRoutes(self):  # pragma: no cover
        return Route.make_many(self.boto3_raw_data["ActualFirewallSubnetRoutes"])

    InternetGatewayId = field("InternetGatewayId")
    CurrentInternetGatewayRouteTable = field("CurrentInternetGatewayRouteTable")

    @cached_property
    def ExpectedInternetGatewayRoutes(self):  # pragma: no cover
        return ExpectedRoute.make_many(
            self.boto3_raw_data["ExpectedInternetGatewayRoutes"]
        )

    @cached_property
    def ActualInternetGatewayRoutes(self):  # pragma: no cover
        return Route.make_many(self.boto3_raw_data["ActualInternetGatewayRoutes"])

    VpcId = field("VpcId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.NetworkFirewallInternetTrafficNotInspectedViolationTypeDef"
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
                "type_defs.NetworkFirewallInternetTrafficNotInspectedViolationTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NetworkFirewallInvalidRouteConfigurationViolation:
    boto3_raw_data: (
        "type_defs.NetworkFirewallInvalidRouteConfigurationViolationTypeDef"
    ) = dataclasses.field()

    AffectedSubnets = field("AffectedSubnets")
    RouteTableId = field("RouteTableId")
    IsRouteTableUsedInDifferentAZ = field("IsRouteTableUsedInDifferentAZ")

    @cached_property
    def ViolatingRoute(self):  # pragma: no cover
        return Route.make_one(self.boto3_raw_data["ViolatingRoute"])

    CurrentFirewallSubnetRouteTable = field("CurrentFirewallSubnetRouteTable")
    ExpectedFirewallEndpoint = field("ExpectedFirewallEndpoint")
    ActualFirewallEndpoint = field("ActualFirewallEndpoint")
    ExpectedFirewallSubnetId = field("ExpectedFirewallSubnetId")
    ActualFirewallSubnetId = field("ActualFirewallSubnetId")

    @cached_property
    def ExpectedFirewallSubnetRoutes(self):  # pragma: no cover
        return ExpectedRoute.make_many(
            self.boto3_raw_data["ExpectedFirewallSubnetRoutes"]
        )

    @cached_property
    def ActualFirewallSubnetRoutes(self):  # pragma: no cover
        return Route.make_many(self.boto3_raw_data["ActualFirewallSubnetRoutes"])

    InternetGatewayId = field("InternetGatewayId")
    CurrentInternetGatewayRouteTable = field("CurrentInternetGatewayRouteTable")

    @cached_property
    def ExpectedInternetGatewayRoutes(self):  # pragma: no cover
        return ExpectedRoute.make_many(
            self.boto3_raw_data["ExpectedInternetGatewayRoutes"]
        )

    @cached_property
    def ActualInternetGatewayRoutes(self):  # pragma: no cover
        return Route.make_many(self.boto3_raw_data["ActualInternetGatewayRoutes"])

    VpcId = field("VpcId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.NetworkFirewallInvalidRouteConfigurationViolationTypeDef"
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
                "type_defs.NetworkFirewallInvalidRouteConfigurationViolationTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NetworkFirewallUnexpectedFirewallRoutesViolation:
    boto3_raw_data: (
        "type_defs.NetworkFirewallUnexpectedFirewallRoutesViolationTypeDef"
    ) = dataclasses.field()

    FirewallSubnetId = field("FirewallSubnetId")

    @cached_property
    def ViolatingRoutes(self):  # pragma: no cover
        return Route.make_many(self.boto3_raw_data["ViolatingRoutes"])

    RouteTableId = field("RouteTableId")
    FirewallEndpoint = field("FirewallEndpoint")
    VpcId = field("VpcId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.NetworkFirewallUnexpectedFirewallRoutesViolationTypeDef"
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
                "type_defs.NetworkFirewallUnexpectedFirewallRoutesViolationTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NetworkFirewallUnexpectedGatewayRoutesViolation:
    boto3_raw_data: (
        "type_defs.NetworkFirewallUnexpectedGatewayRoutesViolationTypeDef"
    ) = dataclasses.field()

    GatewayId = field("GatewayId")

    @cached_property
    def ViolatingRoutes(self):  # pragma: no cover
        return Route.make_many(self.boto3_raw_data["ViolatingRoutes"])

    RouteTableId = field("RouteTableId")
    VpcId = field("VpcId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.NetworkFirewallUnexpectedGatewayRoutesViolationTypeDef"
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
                "type_defs.NetworkFirewallUnexpectedGatewayRoutesViolationTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteHasOutOfScopeEndpointViolation:
    boto3_raw_data: "type_defs.RouteHasOutOfScopeEndpointViolationTypeDef" = (
        dataclasses.field()
    )

    SubnetId = field("SubnetId")
    VpcId = field("VpcId")
    RouteTableId = field("RouteTableId")

    @cached_property
    def ViolatingRoutes(self):  # pragma: no cover
        return Route.make_many(self.boto3_raw_data["ViolatingRoutes"])

    SubnetAvailabilityZone = field("SubnetAvailabilityZone")
    SubnetAvailabilityZoneId = field("SubnetAvailabilityZoneId")
    CurrentFirewallSubnetRouteTable = field("CurrentFirewallSubnetRouteTable")
    FirewallSubnetId = field("FirewallSubnetId")

    @cached_property
    def FirewallSubnetRoutes(self):  # pragma: no cover
        return Route.make_many(self.boto3_raw_data["FirewallSubnetRoutes"])

    InternetGatewayId = field("InternetGatewayId")
    CurrentInternetGatewayRouteTable = field("CurrentInternetGatewayRouteTable")

    @cached_property
    def InternetGatewayRoutes(self):  # pragma: no cover
        return Route.make_many(self.boto3_raw_data["InternetGatewayRoutes"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RouteHasOutOfScopeEndpointViolationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RouteHasOutOfScopeEndpointViolationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StatefulRuleGroup:
    boto3_raw_data: "type_defs.StatefulRuleGroupTypeDef" = dataclasses.field()

    RuleGroupName = field("RuleGroupName")
    ResourceId = field("ResourceId")
    Priority = field("Priority")

    @cached_property
    def Override(self):  # pragma: no cover
        return NetworkFirewallStatefulRuleGroupOverride.make_one(
            self.boto3_raw_data["Override"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StatefulRuleGroupTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StatefulRuleGroupTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SecurityGroupRemediationAction:
    boto3_raw_data: "type_defs.SecurityGroupRemediationActionTypeDef" = (
        dataclasses.field()
    )

    RemediationActionType = field("RemediationActionType")
    Description = field("Description")

    @cached_property
    def RemediationResult(self):  # pragma: no cover
        return SecurityGroupRuleDescription.make_one(
            self.boto3_raw_data["RemediationResult"]
        )

    IsDefaultAction = field("IsDefaultAction")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SecurityGroupRemediationActionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SecurityGroupRemediationActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAdminScopeResponse:
    boto3_raw_data: "type_defs.GetAdminScopeResponseTypeDef" = dataclasses.field()

    @cached_property
    def AdminScope(self):  # pragma: no cover
        return AdminScopeOutput.make_one(self.boto3_raw_data["AdminScope"])

    Status = field("Status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAdminScopeResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAdminScopeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAppsListResponse:
    boto3_raw_data: "type_defs.GetAppsListResponseTypeDef" = dataclasses.field()

    @cached_property
    def AppsList(self):  # pragma: no cover
        return AppsListDataOutput.make_one(self.boto3_raw_data["AppsList"])

    AppsListArn = field("AppsListArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAppsListResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAppsListResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutAppsListResponse:
    boto3_raw_data: "type_defs.PutAppsListResponseTypeDef" = dataclasses.field()

    @cached_property
    def AppsList(self):  # pragma: no cover
        return AppsListDataOutput.make_one(self.boto3_raw_data["AppsList"])

    AppsListArn = field("AppsListArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutAppsListResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutAppsListResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAppsListsResponse:
    boto3_raw_data: "type_defs.ListAppsListsResponseTypeDef" = dataclasses.field()

    @cached_property
    def AppsLists(self):  # pragma: no cover
        return AppsListDataSummary.make_many(self.boto3_raw_data["AppsLists"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAppsListsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAppsListsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetComplianceDetailResponse:
    boto3_raw_data: "type_defs.GetComplianceDetailResponseTypeDef" = dataclasses.field()

    @cached_property
    def PolicyComplianceDetail(self):  # pragma: no cover
        return PolicyComplianceDetail.make_one(
            self.boto3_raw_data["PolicyComplianceDetail"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetComplianceDetailResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetComplianceDetailResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListComplianceStatusResponse:
    boto3_raw_data: "type_defs.ListComplianceStatusResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PolicyComplianceStatusList(self):  # pragma: no cover
        return PolicyComplianceStatus.make_many(
            self.boto3_raw_data["PolicyComplianceStatusList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListComplianceStatusResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListComplianceStatusResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EntryDescription:
    boto3_raw_data: "type_defs.EntryDescriptionTypeDef" = dataclasses.field()

    @cached_property
    def EntryDetail(self):  # pragma: no cover
        return NetworkAclEntry.make_one(self.boto3_raw_data["EntryDetail"])

    EntryRuleNumber = field("EntryRuleNumber")
    EntryType = field("EntryType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EntryDescriptionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EntryDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NetworkAclEntrySetOutput:
    boto3_raw_data: "type_defs.NetworkAclEntrySetOutputTypeDef" = dataclasses.field()

    ForceRemediateForFirstEntries = field("ForceRemediateForFirstEntries")
    ForceRemediateForLastEntries = field("ForceRemediateForLastEntries")

    @cached_property
    def FirstEntries(self):  # pragma: no cover
        return NetworkAclEntry.make_many(self.boto3_raw_data["FirstEntries"])

    @cached_property
    def LastEntries(self):  # pragma: no cover
        return NetworkAclEntry.make_many(self.boto3_raw_data["LastEntries"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NetworkAclEntrySetOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NetworkAclEntrySetOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NetworkAclEntrySet:
    boto3_raw_data: "type_defs.NetworkAclEntrySetTypeDef" = dataclasses.field()

    ForceRemediateForFirstEntries = field("ForceRemediateForFirstEntries")
    ForceRemediateForLastEntries = field("ForceRemediateForLastEntries")

    @cached_property
    def FirstEntries(self):  # pragma: no cover
        return NetworkAclEntry.make_many(self.boto3_raw_data["FirstEntries"])

    @cached_property
    def LastEntries(self):  # pragma: no cover
        return NetworkAclEntry.make_many(self.boto3_raw_data["LastEntries"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NetworkAclEntrySetTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NetworkAclEntrySetTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NetworkFirewallPolicyDescription:
    boto3_raw_data: "type_defs.NetworkFirewallPolicyDescriptionTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def StatelessRuleGroups(self):  # pragma: no cover
        return StatelessRuleGroup.make_many(self.boto3_raw_data["StatelessRuleGroups"])

    StatelessDefaultActions = field("StatelessDefaultActions")
    StatelessFragmentDefaultActions = field("StatelessFragmentDefaultActions")
    StatelessCustomActions = field("StatelessCustomActions")

    @cached_property
    def StatefulRuleGroups(self):  # pragma: no cover
        return StatefulRuleGroup.make_many(self.boto3_raw_data["StatefulRuleGroups"])

    StatefulDefaultActions = field("StatefulDefaultActions")

    @cached_property
    def StatefulEngineOptions(self):  # pragma: no cover
        return StatefulEngineOptions.make_one(
            self.boto3_raw_data["StatefulEngineOptions"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.NetworkFirewallPolicyDescriptionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NetworkFirewallPolicyDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AwsVPCSecurityGroupViolation:
    boto3_raw_data: "type_defs.AwsVPCSecurityGroupViolationTypeDef" = (
        dataclasses.field()
    )

    ViolationTarget = field("ViolationTarget")
    ViolationTargetDescription = field("ViolationTargetDescription")

    @cached_property
    def PartialMatches(self):  # pragma: no cover
        return PartialMatch.make_many(self.boto3_raw_data["PartialMatches"])

    @cached_property
    def PossibleSecurityGroupRemediationActions(self):  # pragma: no cover
        return SecurityGroupRemediationAction.make_many(
            self.boto3_raw_data["PossibleSecurityGroupRemediationActions"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AwsVPCSecurityGroupViolationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AwsVPCSecurityGroupViolationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutAdminAccountRequest:
    boto3_raw_data: "type_defs.PutAdminAccountRequestTypeDef" = dataclasses.field()

    AdminAccount = field("AdminAccount")
    AdminScope = field("AdminScope")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutAdminAccountRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutAdminAccountRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutAppsListRequest:
    boto3_raw_data: "type_defs.PutAppsListRequestTypeDef" = dataclasses.field()

    AppsList = field("AppsList")

    @cached_property
    def TagList(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["TagList"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutAppsListRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutAppsListRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutProtocolsListRequest:
    boto3_raw_data: "type_defs.PutProtocolsListRequestTypeDef" = dataclasses.field()

    ProtocolsList = field("ProtocolsList")

    @cached_property
    def TagList(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["TagList"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutProtocolsListRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutProtocolsListRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutResourceSetRequest:
    boto3_raw_data: "type_defs.PutResourceSetRequestTypeDef" = dataclasses.field()

    ResourceSet = field("ResourceSet")

    @cached_property
    def TagList(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["TagList"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutResourceSetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutResourceSetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateNetworkAclEntriesAction:
    boto3_raw_data: "type_defs.CreateNetworkAclEntriesActionTypeDef" = (
        dataclasses.field()
    )

    Description = field("Description")

    @cached_property
    def NetworkAclId(self):  # pragma: no cover
        return ActionTarget.make_one(self.boto3_raw_data["NetworkAclId"])

    @cached_property
    def NetworkAclEntriesToBeCreated(self):  # pragma: no cover
        return EntryDescription.make_many(
            self.boto3_raw_data["NetworkAclEntriesToBeCreated"]
        )

    FMSCanRemediate = field("FMSCanRemediate")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateNetworkAclEntriesActionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateNetworkAclEntriesActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteNetworkAclEntriesAction:
    boto3_raw_data: "type_defs.DeleteNetworkAclEntriesActionTypeDef" = (
        dataclasses.field()
    )

    Description = field("Description")

    @cached_property
    def NetworkAclId(self):  # pragma: no cover
        return ActionTarget.make_one(self.boto3_raw_data["NetworkAclId"])

    @cached_property
    def NetworkAclEntriesToBeDeleted(self):  # pragma: no cover
        return EntryDescription.make_many(
            self.boto3_raw_data["NetworkAclEntriesToBeDeleted"]
        )

    FMSCanRemediate = field("FMSCanRemediate")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteNetworkAclEntriesActionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteNetworkAclEntriesActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EntryViolation:
    boto3_raw_data: "type_defs.EntryViolationTypeDef" = dataclasses.field()

    @cached_property
    def ExpectedEntry(self):  # pragma: no cover
        return EntryDescription.make_one(self.boto3_raw_data["ExpectedEntry"])

    ExpectedEvaluationOrder = field("ExpectedEvaluationOrder")
    ActualEvaluationOrder = field("ActualEvaluationOrder")

    @cached_property
    def EntryAtExpectedEvaluationOrder(self):  # pragma: no cover
        return EntryDescription.make_one(
            self.boto3_raw_data["EntryAtExpectedEvaluationOrder"]
        )

    @cached_property
    def EntriesWithConflicts(self):  # pragma: no cover
        return EntryDescription.make_many(self.boto3_raw_data["EntriesWithConflicts"])

    EntryViolationReasons = field("EntryViolationReasons")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EntryViolationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EntryViolationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NetworkAclCommonPolicyOutput:
    boto3_raw_data: "type_defs.NetworkAclCommonPolicyOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def NetworkAclEntrySet(self):  # pragma: no cover
        return NetworkAclEntrySetOutput.make_one(
            self.boto3_raw_data["NetworkAclEntrySet"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NetworkAclCommonPolicyOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NetworkAclCommonPolicyOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NetworkAclCommonPolicy:
    boto3_raw_data: "type_defs.NetworkAclCommonPolicyTypeDef" = dataclasses.field()

    @cached_property
    def NetworkAclEntrySet(self):  # pragma: no cover
        return NetworkAclEntrySet.make_one(self.boto3_raw_data["NetworkAclEntrySet"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NetworkAclCommonPolicyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NetworkAclCommonPolicyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NetworkFirewallPolicyModifiedViolation:
    boto3_raw_data: "type_defs.NetworkFirewallPolicyModifiedViolationTypeDef" = (
        dataclasses.field()
    )

    ViolationTarget = field("ViolationTarget")

    @cached_property
    def CurrentPolicyDescription(self):  # pragma: no cover
        return NetworkFirewallPolicyDescription.make_one(
            self.boto3_raw_data["CurrentPolicyDescription"]
        )

    @cached_property
    def ExpectedPolicyDescription(self):  # pragma: no cover
        return NetworkFirewallPolicyDescription.make_one(
            self.boto3_raw_data["ExpectedPolicyDescription"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.NetworkFirewallPolicyModifiedViolationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NetworkFirewallPolicyModifiedViolationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemediationAction:
    boto3_raw_data: "type_defs.RemediationActionTypeDef" = dataclasses.field()

    Description = field("Description")

    @cached_property
    def EC2CreateRouteAction(self):  # pragma: no cover
        return EC2CreateRouteAction.make_one(
            self.boto3_raw_data["EC2CreateRouteAction"]
        )

    @cached_property
    def EC2ReplaceRouteAction(self):  # pragma: no cover
        return EC2ReplaceRouteAction.make_one(
            self.boto3_raw_data["EC2ReplaceRouteAction"]
        )

    @cached_property
    def EC2DeleteRouteAction(self):  # pragma: no cover
        return EC2DeleteRouteAction.make_one(
            self.boto3_raw_data["EC2DeleteRouteAction"]
        )

    @cached_property
    def EC2CopyRouteTableAction(self):  # pragma: no cover
        return EC2CopyRouteTableAction.make_one(
            self.boto3_raw_data["EC2CopyRouteTableAction"]
        )

    @cached_property
    def EC2ReplaceRouteTableAssociationAction(self):  # pragma: no cover
        return EC2ReplaceRouteTableAssociationAction.make_one(
            self.boto3_raw_data["EC2ReplaceRouteTableAssociationAction"]
        )

    @cached_property
    def EC2AssociateRouteTableAction(self):  # pragma: no cover
        return EC2AssociateRouteTableAction.make_one(
            self.boto3_raw_data["EC2AssociateRouteTableAction"]
        )

    @cached_property
    def EC2CreateRouteTableAction(self):  # pragma: no cover
        return EC2CreateRouteTableAction.make_one(
            self.boto3_raw_data["EC2CreateRouteTableAction"]
        )

    @cached_property
    def FMSPolicyUpdateFirewallCreationConfigAction(self):  # pragma: no cover
        return FMSPolicyUpdateFirewallCreationConfigAction.make_one(
            self.boto3_raw_data["FMSPolicyUpdateFirewallCreationConfigAction"]
        )

    @cached_property
    def CreateNetworkAclAction(self):  # pragma: no cover
        return CreateNetworkAclAction.make_one(
            self.boto3_raw_data["CreateNetworkAclAction"]
        )

    @cached_property
    def ReplaceNetworkAclAssociationAction(self):  # pragma: no cover
        return ReplaceNetworkAclAssociationAction.make_one(
            self.boto3_raw_data["ReplaceNetworkAclAssociationAction"]
        )

    @cached_property
    def CreateNetworkAclEntriesAction(self):  # pragma: no cover
        return CreateNetworkAclEntriesAction.make_one(
            self.boto3_raw_data["CreateNetworkAclEntriesAction"]
        )

    @cached_property
    def DeleteNetworkAclEntriesAction(self):  # pragma: no cover
        return DeleteNetworkAclEntriesAction.make_one(
            self.boto3_raw_data["DeleteNetworkAclEntriesAction"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RemediationActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemediationActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InvalidNetworkAclEntriesViolation:
    boto3_raw_data: "type_defs.InvalidNetworkAclEntriesViolationTypeDef" = (
        dataclasses.field()
    )

    Vpc = field("Vpc")
    Subnet = field("Subnet")
    SubnetAvailabilityZone = field("SubnetAvailabilityZone")
    CurrentAssociatedNetworkAcl = field("CurrentAssociatedNetworkAcl")

    @cached_property
    def EntryViolations(self):  # pragma: no cover
        return EntryViolation.make_many(self.boto3_raw_data["EntryViolations"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.InvalidNetworkAclEntriesViolationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InvalidNetworkAclEntriesViolationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PolicyOptionOutput:
    boto3_raw_data: "type_defs.PolicyOptionOutputTypeDef" = dataclasses.field()

    @cached_property
    def NetworkFirewallPolicy(self):  # pragma: no cover
        return NetworkFirewallPolicy.make_one(
            self.boto3_raw_data["NetworkFirewallPolicy"]
        )

    @cached_property
    def ThirdPartyFirewallPolicy(self):  # pragma: no cover
        return ThirdPartyFirewallPolicy.make_one(
            self.boto3_raw_data["ThirdPartyFirewallPolicy"]
        )

    @cached_property
    def NetworkAclCommonPolicy(self):  # pragma: no cover
        return NetworkAclCommonPolicyOutput.make_one(
            self.boto3_raw_data["NetworkAclCommonPolicy"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PolicyOptionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PolicyOptionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PolicyOption:
    boto3_raw_data: "type_defs.PolicyOptionTypeDef" = dataclasses.field()

    @cached_property
    def NetworkFirewallPolicy(self):  # pragma: no cover
        return NetworkFirewallPolicy.make_one(
            self.boto3_raw_data["NetworkFirewallPolicy"]
        )

    @cached_property
    def ThirdPartyFirewallPolicy(self):  # pragma: no cover
        return ThirdPartyFirewallPolicy.make_one(
            self.boto3_raw_data["ThirdPartyFirewallPolicy"]
        )

    @cached_property
    def NetworkAclCommonPolicy(self):  # pragma: no cover
        return NetworkAclCommonPolicy.make_one(
            self.boto3_raw_data["NetworkAclCommonPolicy"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PolicyOptionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PolicyOptionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemediationActionWithOrder:
    boto3_raw_data: "type_defs.RemediationActionWithOrderTypeDef" = dataclasses.field()

    @cached_property
    def RemediationAction(self):  # pragma: no cover
        return RemediationAction.make_one(self.boto3_raw_data["RemediationAction"])

    Order = field("Order")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RemediationActionWithOrderTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemediationActionWithOrderTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SecurityServicePolicyDataOutput:
    boto3_raw_data: "type_defs.SecurityServicePolicyDataOutputTypeDef" = (
        dataclasses.field()
    )

    Type = field("Type")
    ManagedServiceData = field("ManagedServiceData")

    @cached_property
    def PolicyOption(self):  # pragma: no cover
        return PolicyOptionOutput.make_one(self.boto3_raw_data["PolicyOption"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SecurityServicePolicyDataOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SecurityServicePolicyDataOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SecurityServicePolicyData:
    boto3_raw_data: "type_defs.SecurityServicePolicyDataTypeDef" = dataclasses.field()

    Type = field("Type")
    ManagedServiceData = field("ManagedServiceData")

    @cached_property
    def PolicyOption(self):  # pragma: no cover
        return PolicyOption.make_one(self.boto3_raw_data["PolicyOption"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SecurityServicePolicyDataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SecurityServicePolicyDataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PossibleRemediationAction:
    boto3_raw_data: "type_defs.PossibleRemediationActionTypeDef" = dataclasses.field()

    @cached_property
    def OrderedRemediationActions(self):  # pragma: no cover
        return RemediationActionWithOrder.make_many(
            self.boto3_raw_data["OrderedRemediationActions"]
        )

    Description = field("Description")
    IsDefaultAction = field("IsDefaultAction")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PossibleRemediationActionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PossibleRemediationActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PolicyOutput:
    boto3_raw_data: "type_defs.PolicyOutputTypeDef" = dataclasses.field()

    PolicyName = field("PolicyName")

    @cached_property
    def SecurityServicePolicyData(self):  # pragma: no cover
        return SecurityServicePolicyDataOutput.make_one(
            self.boto3_raw_data["SecurityServicePolicyData"]
        )

    ResourceType = field("ResourceType")
    ExcludeResourceTags = field("ExcludeResourceTags")
    RemediationEnabled = field("RemediationEnabled")
    PolicyId = field("PolicyId")
    PolicyUpdateToken = field("PolicyUpdateToken")
    ResourceTypeList = field("ResourceTypeList")

    @cached_property
    def ResourceTags(self):  # pragma: no cover
        return ResourceTag.make_many(self.boto3_raw_data["ResourceTags"])

    DeleteUnusedFMManagedResources = field("DeleteUnusedFMManagedResources")
    IncludeMap = field("IncludeMap")
    ExcludeMap = field("ExcludeMap")
    ResourceSetIds = field("ResourceSetIds")
    PolicyDescription = field("PolicyDescription")
    PolicyStatus = field("PolicyStatus")
    ResourceTagLogicalOperator = field("ResourceTagLogicalOperator")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PolicyOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PolicyOutputTypeDef"]],
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

    @cached_property
    def SecurityServicePolicyData(self):  # pragma: no cover
        return SecurityServicePolicyData.make_one(
            self.boto3_raw_data["SecurityServicePolicyData"]
        )

    ResourceType = field("ResourceType")
    ExcludeResourceTags = field("ExcludeResourceTags")
    RemediationEnabled = field("RemediationEnabled")
    PolicyId = field("PolicyId")
    PolicyUpdateToken = field("PolicyUpdateToken")
    ResourceTypeList = field("ResourceTypeList")

    @cached_property
    def ResourceTags(self):  # pragma: no cover
        return ResourceTag.make_many(self.boto3_raw_data["ResourceTags"])

    DeleteUnusedFMManagedResources = field("DeleteUnusedFMManagedResources")
    IncludeMap = field("IncludeMap")
    ExcludeMap = field("ExcludeMap")
    ResourceSetIds = field("ResourceSetIds")
    PolicyDescription = field("PolicyDescription")
    PolicyStatus = field("PolicyStatus")
    ResourceTagLogicalOperator = field("ResourceTagLogicalOperator")

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
class PossibleRemediationActions:
    boto3_raw_data: "type_defs.PossibleRemediationActionsTypeDef" = dataclasses.field()

    Description = field("Description")

    @cached_property
    def Actions(self):  # pragma: no cover
        return PossibleRemediationAction.make_many(self.boto3_raw_data["Actions"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PossibleRemediationActionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PossibleRemediationActionsTypeDef"]
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
        return PolicyOutput.make_one(self.boto3_raw_data["Policy"])

    PolicyArn = field("PolicyArn")

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
class PutPolicyResponse:
    boto3_raw_data: "type_defs.PutPolicyResponseTypeDef" = dataclasses.field()

    @cached_property
    def Policy(self):  # pragma: no cover
        return PolicyOutput.make_one(self.boto3_raw_data["Policy"])

    PolicyArn = field("PolicyArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PutPolicyResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutPolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceViolation:
    boto3_raw_data: "type_defs.ResourceViolationTypeDef" = dataclasses.field()

    @cached_property
    def AwsVPCSecurityGroupViolation(self):  # pragma: no cover
        return AwsVPCSecurityGroupViolation.make_one(
            self.boto3_raw_data["AwsVPCSecurityGroupViolation"]
        )

    @cached_property
    def AwsEc2NetworkInterfaceViolation(self):  # pragma: no cover
        return AwsEc2NetworkInterfaceViolation.make_one(
            self.boto3_raw_data["AwsEc2NetworkInterfaceViolation"]
        )

    @cached_property
    def AwsEc2InstanceViolation(self):  # pragma: no cover
        return AwsEc2InstanceViolation.make_one(
            self.boto3_raw_data["AwsEc2InstanceViolation"]
        )

    @cached_property
    def NetworkFirewallMissingFirewallViolation(self):  # pragma: no cover
        return NetworkFirewallMissingFirewallViolation.make_one(
            self.boto3_raw_data["NetworkFirewallMissingFirewallViolation"]
        )

    @cached_property
    def NetworkFirewallMissingSubnetViolation(self):  # pragma: no cover
        return NetworkFirewallMissingSubnetViolation.make_one(
            self.boto3_raw_data["NetworkFirewallMissingSubnetViolation"]
        )

    @cached_property
    def NetworkFirewallMissingExpectedRTViolation(self):  # pragma: no cover
        return NetworkFirewallMissingExpectedRTViolation.make_one(
            self.boto3_raw_data["NetworkFirewallMissingExpectedRTViolation"]
        )

    @cached_property
    def NetworkFirewallPolicyModifiedViolation(self):  # pragma: no cover
        return NetworkFirewallPolicyModifiedViolation.make_one(
            self.boto3_raw_data["NetworkFirewallPolicyModifiedViolation"]
        )

    @cached_property
    def NetworkFirewallInternetTrafficNotInspectedViolation(self):  # pragma: no cover
        return NetworkFirewallInternetTrafficNotInspectedViolation.make_one(
            self.boto3_raw_data["NetworkFirewallInternetTrafficNotInspectedViolation"]
        )

    @cached_property
    def NetworkFirewallInvalidRouteConfigurationViolation(self):  # pragma: no cover
        return NetworkFirewallInvalidRouteConfigurationViolation.make_one(
            self.boto3_raw_data["NetworkFirewallInvalidRouteConfigurationViolation"]
        )

    @cached_property
    def NetworkFirewallBlackHoleRouteDetectedViolation(self):  # pragma: no cover
        return NetworkFirewallBlackHoleRouteDetectedViolation.make_one(
            self.boto3_raw_data["NetworkFirewallBlackHoleRouteDetectedViolation"]
        )

    @cached_property
    def NetworkFirewallUnexpectedFirewallRoutesViolation(self):  # pragma: no cover
        return NetworkFirewallUnexpectedFirewallRoutesViolation.make_one(
            self.boto3_raw_data["NetworkFirewallUnexpectedFirewallRoutesViolation"]
        )

    @cached_property
    def NetworkFirewallUnexpectedGatewayRoutesViolation(self):  # pragma: no cover
        return NetworkFirewallUnexpectedGatewayRoutesViolation.make_one(
            self.boto3_raw_data["NetworkFirewallUnexpectedGatewayRoutesViolation"]
        )

    @cached_property
    def NetworkFirewallMissingExpectedRoutesViolation(self):  # pragma: no cover
        return NetworkFirewallMissingExpectedRoutesViolation.make_one(
            self.boto3_raw_data["NetworkFirewallMissingExpectedRoutesViolation"]
        )

    @cached_property
    def DnsRuleGroupPriorityConflictViolation(self):  # pragma: no cover
        return DnsRuleGroupPriorityConflictViolation.make_one(
            self.boto3_raw_data["DnsRuleGroupPriorityConflictViolation"]
        )

    @cached_property
    def DnsDuplicateRuleGroupViolation(self):  # pragma: no cover
        return DnsDuplicateRuleGroupViolation.make_one(
            self.boto3_raw_data["DnsDuplicateRuleGroupViolation"]
        )

    @cached_property
    def DnsRuleGroupLimitExceededViolation(self):  # pragma: no cover
        return DnsRuleGroupLimitExceededViolation.make_one(
            self.boto3_raw_data["DnsRuleGroupLimitExceededViolation"]
        )

    @cached_property
    def FirewallSubnetIsOutOfScopeViolation(self):  # pragma: no cover
        return FirewallSubnetIsOutOfScopeViolation.make_one(
            self.boto3_raw_data["FirewallSubnetIsOutOfScopeViolation"]
        )

    @cached_property
    def RouteHasOutOfScopeEndpointViolation(self):  # pragma: no cover
        return RouteHasOutOfScopeEndpointViolation.make_one(
            self.boto3_raw_data["RouteHasOutOfScopeEndpointViolation"]
        )

    @cached_property
    def ThirdPartyFirewallMissingFirewallViolation(self):  # pragma: no cover
        return ThirdPartyFirewallMissingFirewallViolation.make_one(
            self.boto3_raw_data["ThirdPartyFirewallMissingFirewallViolation"]
        )

    @cached_property
    def ThirdPartyFirewallMissingSubnetViolation(self):  # pragma: no cover
        return ThirdPartyFirewallMissingSubnetViolation.make_one(
            self.boto3_raw_data["ThirdPartyFirewallMissingSubnetViolation"]
        )

    @cached_property
    def ThirdPartyFirewallMissingExpectedRouteTableViolation(self):  # pragma: no cover
        return ThirdPartyFirewallMissingExpectedRouteTableViolation.make_one(
            self.boto3_raw_data["ThirdPartyFirewallMissingExpectedRouteTableViolation"]
        )

    @cached_property
    def FirewallSubnetMissingVPCEndpointViolation(self):  # pragma: no cover
        return FirewallSubnetMissingVPCEndpointViolation.make_one(
            self.boto3_raw_data["FirewallSubnetMissingVPCEndpointViolation"]
        )

    @cached_property
    def InvalidNetworkAclEntriesViolation(self):  # pragma: no cover
        return InvalidNetworkAclEntriesViolation.make_one(
            self.boto3_raw_data["InvalidNetworkAclEntriesViolation"]
        )

    @cached_property
    def PossibleRemediationActions(self):  # pragma: no cover
        return PossibleRemediationActions.make_one(
            self.boto3_raw_data["PossibleRemediationActions"]
        )

    @cached_property
    def WebACLHasIncompatibleConfigurationViolation(self):  # pragma: no cover
        return WebACLHasIncompatibleConfigurationViolation.make_one(
            self.boto3_raw_data["WebACLHasIncompatibleConfigurationViolation"]
        )

    @cached_property
    def WebACLHasOutOfScopeResourcesViolation(self):  # pragma: no cover
        return WebACLHasOutOfScopeResourcesViolation.make_one(
            self.boto3_raw_data["WebACLHasOutOfScopeResourcesViolation"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResourceViolationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceViolationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutPolicyRequest:
    boto3_raw_data: "type_defs.PutPolicyRequestTypeDef" = dataclasses.field()

    Policy = field("Policy")

    @cached_property
    def TagList(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["TagList"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PutPolicyRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ViolationDetail:
    boto3_raw_data: "type_defs.ViolationDetailTypeDef" = dataclasses.field()

    PolicyId = field("PolicyId")
    MemberAccount = field("MemberAccount")
    ResourceId = field("ResourceId")
    ResourceType = field("ResourceType")

    @cached_property
    def ResourceViolations(self):  # pragma: no cover
        return ResourceViolation.make_many(self.boto3_raw_data["ResourceViolations"])

    @cached_property
    def ResourceTags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["ResourceTags"])

    ResourceDescription = field("ResourceDescription")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ViolationDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ViolationDetailTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetViolationDetailsResponse:
    boto3_raw_data: "type_defs.GetViolationDetailsResponseTypeDef" = dataclasses.field()

    @cached_property
    def ViolationDetail(self):  # pragma: no cover
        return ViolationDetail.make_one(self.boto3_raw_data["ViolationDetail"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetViolationDetailsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetViolationDetailsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
