# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_billingconductor import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AccountAssociationsListElement:
    boto3_raw_data: "type_defs.AccountAssociationsListElementTypeDef" = (
        dataclasses.field()
    )

    AccountId = field("AccountId")
    BillingGroupArn = field("BillingGroupArn")
    AccountName = field("AccountName")
    AccountEmail = field("AccountEmail")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AccountAssociationsListElementTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccountAssociationsListElementTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccountGrouping:
    boto3_raw_data: "type_defs.AccountGroupingTypeDef" = dataclasses.field()

    LinkedAccountIds = field("LinkedAccountIds")
    AutoAssociate = field("AutoAssociate")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AccountGroupingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AccountGroupingTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateAccountsInput:
    boto3_raw_data: "type_defs.AssociateAccountsInputTypeDef" = dataclasses.field()

    Arn = field("Arn")
    AccountIds = field("AccountIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociateAccountsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateAccountsInputTypeDef"]
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
class AssociatePricingRulesInput:
    boto3_raw_data: "type_defs.AssociatePricingRulesInputTypeDef" = dataclasses.field()

    Arn = field("Arn")
    PricingRuleArns = field("PricingRuleArns")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociatePricingRulesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociatePricingRulesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateResourceError:
    boto3_raw_data: "type_defs.AssociateResourceErrorTypeDef" = dataclasses.field()

    Message = field("Message")
    Reason = field("Reason")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociateResourceErrorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateResourceErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Attribute:
    boto3_raw_data: "type_defs.AttributeTypeDef" = dataclasses.field()

    Key = field("Key")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AttributeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AttributeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomLineItemBillingPeriodRange:
    boto3_raw_data: "type_defs.CustomLineItemBillingPeriodRangeTypeDef" = (
        dataclasses.field()
    )

    InclusiveStartBillingPeriod = field("InclusiveStartBillingPeriod")
    ExclusiveEndBillingPeriod = field("ExclusiveEndBillingPeriod")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CustomLineItemBillingPeriodRangeTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomLineItemBillingPeriodRangeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BillingGroupCostReportElement:
    boto3_raw_data: "type_defs.BillingGroupCostReportElementTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    AWSCost = field("AWSCost")
    ProformaCost = field("ProformaCost")
    Margin = field("Margin")
    MarginPercentage = field("MarginPercentage")
    Currency = field("Currency")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BillingGroupCostReportElementTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BillingGroupCostReportElementTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComputationPreference:
    boto3_raw_data: "type_defs.ComputationPreferenceTypeDef" = dataclasses.field()

    PricingPlanArn = field("PricingPlanArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ComputationPreferenceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComputationPreferenceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBillingGroupAccountGrouping:
    boto3_raw_data: "type_defs.ListBillingGroupAccountGroupingTypeDef" = (
        dataclasses.field()
    )

    AutoAssociate = field("AutoAssociate")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListBillingGroupAccountGroupingTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBillingGroupAccountGroupingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BillingPeriodRange:
    boto3_raw_data: "type_defs.BillingPeriodRangeTypeDef" = dataclasses.field()

    InclusiveStartBillingPeriod = field("InclusiveStartBillingPeriod")
    ExclusiveEndBillingPeriod = field("ExclusiveEndBillingPeriod")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BillingPeriodRangeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BillingPeriodRangeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFreeTierConfig:
    boto3_raw_data: "type_defs.CreateFreeTierConfigTypeDef" = dataclasses.field()

    Activated = field("Activated")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateFreeTierConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFreeTierConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePricingPlanInput:
    boto3_raw_data: "type_defs.CreatePricingPlanInputTypeDef" = dataclasses.field()

    Name = field("Name")
    ClientToken = field("ClientToken")
    Description = field("Description")
    PricingRuleArns = field("PricingRuleArns")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePricingPlanInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePricingPlanInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomLineItemFlatChargeDetails:
    boto3_raw_data: "type_defs.CustomLineItemFlatChargeDetailsTypeDef" = (
        dataclasses.field()
    )

    ChargeValue = field("ChargeValue")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CustomLineItemFlatChargeDetailsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomLineItemFlatChargeDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomLineItemPercentageChargeDetails:
    boto3_raw_data: "type_defs.CustomLineItemPercentageChargeDetailsTypeDef" = (
        dataclasses.field()
    )

    PercentageValue = field("PercentageValue")
    AssociatedValues = field("AssociatedValues")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CustomLineItemPercentageChargeDetailsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomLineItemPercentageChargeDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBillingGroupInput:
    boto3_raw_data: "type_defs.DeleteBillingGroupInputTypeDef" = dataclasses.field()

    Arn = field("Arn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteBillingGroupInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBillingGroupInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePricingPlanInput:
    boto3_raw_data: "type_defs.DeletePricingPlanInputTypeDef" = dataclasses.field()

    Arn = field("Arn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeletePricingPlanInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePricingPlanInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePricingRuleInput:
    boto3_raw_data: "type_defs.DeletePricingRuleInputTypeDef" = dataclasses.field()

    Arn = field("Arn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeletePricingRuleInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePricingRuleInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateAccountsInput:
    boto3_raw_data: "type_defs.DisassociateAccountsInputTypeDef" = dataclasses.field()

    Arn = field("Arn")
    AccountIds = field("AccountIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DisassociateAccountsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateAccountsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociatePricingRulesInput:
    boto3_raw_data: "type_defs.DisassociatePricingRulesInputTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    PricingRuleArns = field("PricingRuleArns")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DisassociatePricingRulesInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociatePricingRulesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FreeTierConfig:
    boto3_raw_data: "type_defs.FreeTierConfigTypeDef" = dataclasses.field()

    Activated = field("Activated")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FreeTierConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FreeTierConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LineItemFilterOutput:
    boto3_raw_data: "type_defs.LineItemFilterOutputTypeDef" = dataclasses.field()

    Attribute = field("Attribute")
    MatchOption = field("MatchOption")
    Values = field("Values")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LineItemFilterOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LineItemFilterOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LineItemFilter:
    boto3_raw_data: "type_defs.LineItemFilterTypeDef" = dataclasses.field()

    Attribute = field("Attribute")
    MatchOption = field("MatchOption")
    Values = field("Values")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LineItemFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LineItemFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAccountAssociationsFilter:
    boto3_raw_data: "type_defs.ListAccountAssociationsFilterTypeDef" = (
        dataclasses.field()
    )

    Association = field("Association")
    AccountId = field("AccountId")
    AccountIds = field("AccountIds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAccountAssociationsFilterTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAccountAssociationsFilterTypeDef"]
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
class ListBillingGroupCostReportsFilter:
    boto3_raw_data: "type_defs.ListBillingGroupCostReportsFilterTypeDef" = (
        dataclasses.field()
    )

    BillingGroupArns = field("BillingGroupArns")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListBillingGroupCostReportsFilterTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBillingGroupCostReportsFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBillingGroupsFilter:
    boto3_raw_data: "type_defs.ListBillingGroupsFilterTypeDef" = dataclasses.field()

    Arns = field("Arns")
    PricingPlan = field("PricingPlan")
    Statuses = field("Statuses")
    AutoAssociate = field("AutoAssociate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBillingGroupsFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBillingGroupsFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCustomLineItemFlatChargeDetails:
    boto3_raw_data: "type_defs.ListCustomLineItemFlatChargeDetailsTypeDef" = (
        dataclasses.field()
    )

    ChargeValue = field("ChargeValue")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCustomLineItemFlatChargeDetailsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCustomLineItemFlatChargeDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCustomLineItemPercentageChargeDetails:
    boto3_raw_data: "type_defs.ListCustomLineItemPercentageChargeDetailsTypeDef" = (
        dataclasses.field()
    )

    PercentageValue = field("PercentageValue")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCustomLineItemPercentageChargeDetailsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCustomLineItemPercentageChargeDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCustomLineItemVersionsBillingPeriodRangeFilter:
    boto3_raw_data: (
        "type_defs.ListCustomLineItemVersionsBillingPeriodRangeFilterTypeDef"
    ) = dataclasses.field()

    StartBillingPeriod = field("StartBillingPeriod")
    EndBillingPeriod = field("EndBillingPeriod")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCustomLineItemVersionsBillingPeriodRangeFilterTypeDef"
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
                "type_defs.ListCustomLineItemVersionsBillingPeriodRangeFilterTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCustomLineItemsFilter:
    boto3_raw_data: "type_defs.ListCustomLineItemsFilterTypeDef" = dataclasses.field()

    Names = field("Names")
    BillingGroups = field("BillingGroups")
    Arns = field("Arns")
    AccountIds = field("AccountIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCustomLineItemsFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCustomLineItemsFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPricingPlansAssociatedWithPricingRuleInput:
    boto3_raw_data: (
        "type_defs.ListPricingPlansAssociatedWithPricingRuleInputTypeDef"
    ) = dataclasses.field()

    PricingRuleArn = field("PricingRuleArn")
    BillingPeriod = field("BillingPeriod")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListPricingPlansAssociatedWithPricingRuleInputTypeDef"
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
                "type_defs.ListPricingPlansAssociatedWithPricingRuleInputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPricingPlansFilter:
    boto3_raw_data: "type_defs.ListPricingPlansFilterTypeDef" = dataclasses.field()

    Arns = field("Arns")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPricingPlansFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPricingPlansFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PricingPlanListElement:
    boto3_raw_data: "type_defs.PricingPlanListElementTypeDef" = dataclasses.field()

    Name = field("Name")
    Arn = field("Arn")
    Description = field("Description")
    Size = field("Size")
    CreationTime = field("CreationTime")
    LastModifiedTime = field("LastModifiedTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PricingPlanListElementTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PricingPlanListElementTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPricingRulesAssociatedToPricingPlanInput:
    boto3_raw_data: "type_defs.ListPricingRulesAssociatedToPricingPlanInputTypeDef" = (
        dataclasses.field()
    )

    PricingPlanArn = field("PricingPlanArn")
    BillingPeriod = field("BillingPeriod")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListPricingRulesAssociatedToPricingPlanInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPricingRulesAssociatedToPricingPlanInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPricingRulesFilter:
    boto3_raw_data: "type_defs.ListPricingRulesFilterTypeDef" = dataclasses.field()

    Arns = field("Arns")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPricingRulesFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPricingRulesFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourcesAssociatedToCustomLineItemFilter:
    boto3_raw_data: "type_defs.ListResourcesAssociatedToCustomLineItemFilterTypeDef" = (
        dataclasses.field()
    )

    Relationship = field("Relationship")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListResourcesAssociatedToCustomLineItemFilterTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourcesAssociatedToCustomLineItemFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourcesAssociatedToCustomLineItemResponseElement:
    boto3_raw_data: (
        "type_defs.ListResourcesAssociatedToCustomLineItemResponseElementTypeDef"
    ) = dataclasses.field()

    Arn = field("Arn")
    Relationship = field("Relationship")
    EndBillingPeriod = field("EndBillingPeriod")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListResourcesAssociatedToCustomLineItemResponseElementTypeDef"
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
                "type_defs.ListResourcesAssociatedToCustomLineItemResponseElementTypeDef"
            ]
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
class TagResourceRequest:
    boto3_raw_data: "type_defs.TagResourceRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")
    Tags = field("Tags")

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
class UpdateBillingGroupAccountGrouping:
    boto3_raw_data: "type_defs.UpdateBillingGroupAccountGroupingTypeDef" = (
        dataclasses.field()
    )

    AutoAssociate = field("AutoAssociate")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateBillingGroupAccountGroupingTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateBillingGroupAccountGroupingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCustomLineItemFlatChargeDetails:
    boto3_raw_data: "type_defs.UpdateCustomLineItemFlatChargeDetailsTypeDef" = (
        dataclasses.field()
    )

    ChargeValue = field("ChargeValue")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateCustomLineItemFlatChargeDetailsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCustomLineItemFlatChargeDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCustomLineItemPercentageChargeDetails:
    boto3_raw_data: "type_defs.UpdateCustomLineItemPercentageChargeDetailsTypeDef" = (
        dataclasses.field()
    )

    PercentageValue = field("PercentageValue")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateCustomLineItemPercentageChargeDetailsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCustomLineItemPercentageChargeDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFreeTierConfig:
    boto3_raw_data: "type_defs.UpdateFreeTierConfigTypeDef" = dataclasses.field()

    Activated = field("Activated")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateFreeTierConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFreeTierConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePricingPlanInput:
    boto3_raw_data: "type_defs.UpdatePricingPlanInputTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Name = field("Name")
    Description = field("Description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdatePricingPlanInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePricingPlanInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateAccountsOutput:
    boto3_raw_data: "type_defs.AssociateAccountsOutputTypeDef" = dataclasses.field()

    Arn = field("Arn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociateAccountsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateAccountsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociatePricingRulesOutput:
    boto3_raw_data: "type_defs.AssociatePricingRulesOutputTypeDef" = dataclasses.field()

    Arn = field("Arn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociatePricingRulesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociatePricingRulesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBillingGroupOutput:
    boto3_raw_data: "type_defs.CreateBillingGroupOutputTypeDef" = dataclasses.field()

    Arn = field("Arn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateBillingGroupOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBillingGroupOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCustomLineItemOutput:
    boto3_raw_data: "type_defs.CreateCustomLineItemOutputTypeDef" = dataclasses.field()

    Arn = field("Arn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateCustomLineItemOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCustomLineItemOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePricingPlanOutput:
    boto3_raw_data: "type_defs.CreatePricingPlanOutputTypeDef" = dataclasses.field()

    Arn = field("Arn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePricingPlanOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePricingPlanOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePricingRuleOutput:
    boto3_raw_data: "type_defs.CreatePricingRuleOutputTypeDef" = dataclasses.field()

    Arn = field("Arn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePricingRuleOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePricingRuleOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBillingGroupOutput:
    boto3_raw_data: "type_defs.DeleteBillingGroupOutputTypeDef" = dataclasses.field()

    Arn = field("Arn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteBillingGroupOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBillingGroupOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCustomLineItemOutput:
    boto3_raw_data: "type_defs.DeleteCustomLineItemOutputTypeDef" = dataclasses.field()

    Arn = field("Arn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteCustomLineItemOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCustomLineItemOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePricingPlanOutput:
    boto3_raw_data: "type_defs.DeletePricingPlanOutputTypeDef" = dataclasses.field()

    Arn = field("Arn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeletePricingPlanOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePricingPlanOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePricingRuleOutput:
    boto3_raw_data: "type_defs.DeletePricingRuleOutputTypeDef" = dataclasses.field()

    Arn = field("Arn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeletePricingRuleOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePricingRuleOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateAccountsOutput:
    boto3_raw_data: "type_defs.DisassociateAccountsOutputTypeDef" = dataclasses.field()

    Arn = field("Arn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DisassociateAccountsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateAccountsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociatePricingRulesOutput:
    boto3_raw_data: "type_defs.DisassociatePricingRulesOutputTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DisassociatePricingRulesOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociatePricingRulesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAccountAssociationsOutput:
    boto3_raw_data: "type_defs.ListAccountAssociationsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def LinkedAccounts(self):  # pragma: no cover
        return AccountAssociationsListElement.make_many(
            self.boto3_raw_data["LinkedAccounts"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAccountAssociationsOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAccountAssociationsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPricingPlansAssociatedWithPricingRuleOutput:
    boto3_raw_data: (
        "type_defs.ListPricingPlansAssociatedWithPricingRuleOutputTypeDef"
    ) = dataclasses.field()

    BillingPeriod = field("BillingPeriod")
    PricingRuleArn = field("PricingRuleArn")
    PricingPlanArns = field("PricingPlanArns")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListPricingPlansAssociatedWithPricingRuleOutputTypeDef"
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
                "type_defs.ListPricingPlansAssociatedWithPricingRuleOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPricingRulesAssociatedToPricingPlanOutput:
    boto3_raw_data: "type_defs.ListPricingRulesAssociatedToPricingPlanOutputTypeDef" = (
        dataclasses.field()
    )

    BillingPeriod = field("BillingPeriod")
    PricingPlanArn = field("PricingPlanArn")
    PricingRuleArns = field("PricingRuleArns")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListPricingRulesAssociatedToPricingPlanOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPricingRulesAssociatedToPricingPlanOutputTypeDef"]
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
class UpdatePricingPlanOutput:
    boto3_raw_data: "type_defs.UpdatePricingPlanOutputTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Name = field("Name")
    Description = field("Description")
    Size = field("Size")
    LastModifiedTime = field("LastModifiedTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdatePricingPlanOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePricingPlanOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateResourceResponseElement:
    boto3_raw_data: "type_defs.AssociateResourceResponseElementTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")

    @cached_property
    def Error(self):  # pragma: no cover
        return AssociateResourceError.make_one(self.boto3_raw_data["Error"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AssociateResourceResponseElementTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateResourceResponseElementTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateResourceResponseElement:
    boto3_raw_data: "type_defs.DisassociateResourceResponseElementTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")

    @cached_property
    def Error(self):  # pragma: no cover
        return AssociateResourceError.make_one(self.boto3_raw_data["Error"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateResourceResponseElementTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateResourceResponseElementTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BillingGroupCostReportResultElement:
    boto3_raw_data: "type_defs.BillingGroupCostReportResultElementTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    AWSCost = field("AWSCost")
    ProformaCost = field("ProformaCost")
    Margin = field("Margin")
    MarginPercentage = field("MarginPercentage")
    Currency = field("Currency")

    @cached_property
    def Attributes(self):  # pragma: no cover
        return Attribute.make_many(self.boto3_raw_data["Attributes"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BillingGroupCostReportResultElementTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BillingGroupCostReportResultElementTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchAssociateResourcesToCustomLineItemInput:
    boto3_raw_data: "type_defs.BatchAssociateResourcesToCustomLineItemInputTypeDef" = (
        dataclasses.field()
    )

    TargetArn = field("TargetArn")
    ResourceArns = field("ResourceArns")

    @cached_property
    def BillingPeriodRange(self):  # pragma: no cover
        return CustomLineItemBillingPeriodRange.make_one(
            self.boto3_raw_data["BillingPeriodRange"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchAssociateResourcesToCustomLineItemInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchAssociateResourcesToCustomLineItemInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDisassociateResourcesFromCustomLineItemInput:
    boto3_raw_data: (
        "type_defs.BatchDisassociateResourcesFromCustomLineItemInputTypeDef"
    ) = dataclasses.field()

    TargetArn = field("TargetArn")
    ResourceArns = field("ResourceArns")

    @cached_property
    def BillingPeriodRange(self):  # pragma: no cover
        return CustomLineItemBillingPeriodRange.make_one(
            self.boto3_raw_data["BillingPeriodRange"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchDisassociateResourcesFromCustomLineItemInputTypeDef"
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
                "type_defs.BatchDisassociateResourcesFromCustomLineItemInputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCustomLineItemInput:
    boto3_raw_data: "type_defs.DeleteCustomLineItemInputTypeDef" = dataclasses.field()

    Arn = field("Arn")

    @cached_property
    def BillingPeriodRange(self):  # pragma: no cover
        return CustomLineItemBillingPeriodRange.make_one(
            self.boto3_raw_data["BillingPeriodRange"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteCustomLineItemInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCustomLineItemInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBillingGroupCostReportsOutput:
    boto3_raw_data: "type_defs.ListBillingGroupCostReportsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def BillingGroupCostReports(self):  # pragma: no cover
        return BillingGroupCostReportElement.make_many(
            self.boto3_raw_data["BillingGroupCostReports"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListBillingGroupCostReportsOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBillingGroupCostReportsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBillingGroupInput:
    boto3_raw_data: "type_defs.CreateBillingGroupInputTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def AccountGrouping(self):  # pragma: no cover
        return AccountGrouping.make_one(self.boto3_raw_data["AccountGrouping"])

    @cached_property
    def ComputationPreference(self):  # pragma: no cover
        return ComputationPreference.make_one(
            self.boto3_raw_data["ComputationPreference"]
        )

    ClientToken = field("ClientToken")
    PrimaryAccountId = field("PrimaryAccountId")
    Description = field("Description")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateBillingGroupInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBillingGroupInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BillingGroupListElement:
    boto3_raw_data: "type_defs.BillingGroupListElementTypeDef" = dataclasses.field()

    Name = field("Name")
    Arn = field("Arn")
    Description = field("Description")
    PrimaryAccountId = field("PrimaryAccountId")

    @cached_property
    def ComputationPreference(self):  # pragma: no cover
        return ComputationPreference.make_one(
            self.boto3_raw_data["ComputationPreference"]
        )

    Size = field("Size")
    CreationTime = field("CreationTime")
    LastModifiedTime = field("LastModifiedTime")
    Status = field("Status")
    StatusReason = field("StatusReason")

    @cached_property
    def AccountGrouping(self):  # pragma: no cover
        return ListBillingGroupAccountGrouping.make_one(
            self.boto3_raw_data["AccountGrouping"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BillingGroupListElementTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BillingGroupListElementTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBillingGroupCostReportInput:
    boto3_raw_data: "type_defs.GetBillingGroupCostReportInputTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")

    @cached_property
    def BillingPeriodRange(self):  # pragma: no cover
        return BillingPeriodRange.make_one(self.boto3_raw_data["BillingPeriodRange"])

    GroupBy = field("GroupBy")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetBillingGroupCostReportInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBillingGroupCostReportInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTieringInput:
    boto3_raw_data: "type_defs.CreateTieringInputTypeDef" = dataclasses.field()

    @cached_property
    def FreeTier(self):  # pragma: no cover
        return CreateFreeTierConfig.make_one(self.boto3_raw_data["FreeTier"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateTieringInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTieringInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Tiering:
    boto3_raw_data: "type_defs.TieringTypeDef" = dataclasses.field()

    @cached_property
    def FreeTier(self):  # pragma: no cover
        return FreeTierConfig.make_one(self.boto3_raw_data["FreeTier"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TieringTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TieringTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAccountAssociationsInput:
    boto3_raw_data: "type_defs.ListAccountAssociationsInputTypeDef" = (
        dataclasses.field()
    )

    BillingPeriod = field("BillingPeriod")

    @cached_property
    def Filters(self):  # pragma: no cover
        return ListAccountAssociationsFilter.make_one(self.boto3_raw_data["Filters"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAccountAssociationsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAccountAssociationsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAccountAssociationsInputPaginate:
    boto3_raw_data: "type_defs.ListAccountAssociationsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    BillingPeriod = field("BillingPeriod")

    @cached_property
    def Filters(self):  # pragma: no cover
        return ListAccountAssociationsFilter.make_one(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAccountAssociationsInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAccountAssociationsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPricingPlansAssociatedWithPricingRuleInputPaginate:
    boto3_raw_data: (
        "type_defs.ListPricingPlansAssociatedWithPricingRuleInputPaginateTypeDef"
    ) = dataclasses.field()

    PricingRuleArn = field("PricingRuleArn")
    BillingPeriod = field("BillingPeriod")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListPricingPlansAssociatedWithPricingRuleInputPaginateTypeDef"
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
                "type_defs.ListPricingPlansAssociatedWithPricingRuleInputPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPricingRulesAssociatedToPricingPlanInputPaginate:
    boto3_raw_data: (
        "type_defs.ListPricingRulesAssociatedToPricingPlanInputPaginateTypeDef"
    ) = dataclasses.field()

    PricingPlanArn = field("PricingPlanArn")
    BillingPeriod = field("BillingPeriod")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListPricingRulesAssociatedToPricingPlanInputPaginateTypeDef"
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
                "type_defs.ListPricingRulesAssociatedToPricingPlanInputPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBillingGroupCostReportsInputPaginate:
    boto3_raw_data: "type_defs.ListBillingGroupCostReportsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    BillingPeriod = field("BillingPeriod")

    @cached_property
    def Filters(self):  # pragma: no cover
        return ListBillingGroupCostReportsFilter.make_one(
            self.boto3_raw_data["Filters"]
        )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListBillingGroupCostReportsInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBillingGroupCostReportsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBillingGroupCostReportsInput:
    boto3_raw_data: "type_defs.ListBillingGroupCostReportsInputTypeDef" = (
        dataclasses.field()
    )

    BillingPeriod = field("BillingPeriod")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @cached_property
    def Filters(self):  # pragma: no cover
        return ListBillingGroupCostReportsFilter.make_one(
            self.boto3_raw_data["Filters"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListBillingGroupCostReportsInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBillingGroupCostReportsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBillingGroupsInputPaginate:
    boto3_raw_data: "type_defs.ListBillingGroupsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    BillingPeriod = field("BillingPeriod")

    @cached_property
    def Filters(self):  # pragma: no cover
        return ListBillingGroupsFilter.make_one(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListBillingGroupsInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBillingGroupsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBillingGroupsInput:
    boto3_raw_data: "type_defs.ListBillingGroupsInputTypeDef" = dataclasses.field()

    BillingPeriod = field("BillingPeriod")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @cached_property
    def Filters(self):  # pragma: no cover
        return ListBillingGroupsFilter.make_one(self.boto3_raw_data["Filters"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBillingGroupsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBillingGroupsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCustomLineItemChargeDetails:
    boto3_raw_data: "type_defs.ListCustomLineItemChargeDetailsTypeDef" = (
        dataclasses.field()
    )

    Type = field("Type")

    @cached_property
    def Flat(self):  # pragma: no cover
        return ListCustomLineItemFlatChargeDetails.make_one(self.boto3_raw_data["Flat"])

    @cached_property
    def Percentage(self):  # pragma: no cover
        return ListCustomLineItemPercentageChargeDetails.make_one(
            self.boto3_raw_data["Percentage"]
        )

    @cached_property
    def LineItemFilters(self):  # pragma: no cover
        return LineItemFilterOutput.make_many(self.boto3_raw_data["LineItemFilters"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListCustomLineItemChargeDetailsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCustomLineItemChargeDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCustomLineItemVersionsFilter:
    boto3_raw_data: "type_defs.ListCustomLineItemVersionsFilterTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def BillingPeriodRange(self):  # pragma: no cover
        return ListCustomLineItemVersionsBillingPeriodRangeFilter.make_one(
            self.boto3_raw_data["BillingPeriodRange"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListCustomLineItemVersionsFilterTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCustomLineItemVersionsFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCustomLineItemsInputPaginate:
    boto3_raw_data: "type_defs.ListCustomLineItemsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    BillingPeriod = field("BillingPeriod")

    @cached_property
    def Filters(self):  # pragma: no cover
        return ListCustomLineItemsFilter.make_one(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListCustomLineItemsInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCustomLineItemsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCustomLineItemsInput:
    boto3_raw_data: "type_defs.ListCustomLineItemsInputTypeDef" = dataclasses.field()

    BillingPeriod = field("BillingPeriod")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @cached_property
    def Filters(self):  # pragma: no cover
        return ListCustomLineItemsFilter.make_one(self.boto3_raw_data["Filters"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCustomLineItemsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCustomLineItemsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPricingPlansInputPaginate:
    boto3_raw_data: "type_defs.ListPricingPlansInputPaginateTypeDef" = (
        dataclasses.field()
    )

    BillingPeriod = field("BillingPeriod")

    @cached_property
    def Filters(self):  # pragma: no cover
        return ListPricingPlansFilter.make_one(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListPricingPlansInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPricingPlansInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPricingPlansInput:
    boto3_raw_data: "type_defs.ListPricingPlansInputTypeDef" = dataclasses.field()

    BillingPeriod = field("BillingPeriod")

    @cached_property
    def Filters(self):  # pragma: no cover
        return ListPricingPlansFilter.make_one(self.boto3_raw_data["Filters"])

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPricingPlansInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPricingPlansInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPricingPlansOutput:
    boto3_raw_data: "type_defs.ListPricingPlansOutputTypeDef" = dataclasses.field()

    BillingPeriod = field("BillingPeriod")

    @cached_property
    def PricingPlans(self):  # pragma: no cover
        return PricingPlanListElement.make_many(self.boto3_raw_data["PricingPlans"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPricingPlansOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPricingPlansOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPricingRulesInputPaginate:
    boto3_raw_data: "type_defs.ListPricingRulesInputPaginateTypeDef" = (
        dataclasses.field()
    )

    BillingPeriod = field("BillingPeriod")

    @cached_property
    def Filters(self):  # pragma: no cover
        return ListPricingRulesFilter.make_one(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListPricingRulesInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPricingRulesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPricingRulesInput:
    boto3_raw_data: "type_defs.ListPricingRulesInputTypeDef" = dataclasses.field()

    BillingPeriod = field("BillingPeriod")

    @cached_property
    def Filters(self):  # pragma: no cover
        return ListPricingRulesFilter.make_one(self.boto3_raw_data["Filters"])

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPricingRulesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPricingRulesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourcesAssociatedToCustomLineItemInputPaginate:
    boto3_raw_data: (
        "type_defs.ListResourcesAssociatedToCustomLineItemInputPaginateTypeDef"
    ) = dataclasses.field()

    Arn = field("Arn")
    BillingPeriod = field("BillingPeriod")

    @cached_property
    def Filters(self):  # pragma: no cover
        return ListResourcesAssociatedToCustomLineItemFilter.make_one(
            self.boto3_raw_data["Filters"]
        )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListResourcesAssociatedToCustomLineItemInputPaginateTypeDef"
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
                "type_defs.ListResourcesAssociatedToCustomLineItemInputPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourcesAssociatedToCustomLineItemInput:
    boto3_raw_data: "type_defs.ListResourcesAssociatedToCustomLineItemInputTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    BillingPeriod = field("BillingPeriod")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @cached_property
    def Filters(self):  # pragma: no cover
        return ListResourcesAssociatedToCustomLineItemFilter.make_one(
            self.boto3_raw_data["Filters"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListResourcesAssociatedToCustomLineItemInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourcesAssociatedToCustomLineItemInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourcesAssociatedToCustomLineItemOutput:
    boto3_raw_data: "type_defs.ListResourcesAssociatedToCustomLineItemOutputTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")

    @cached_property
    def AssociatedResources(self):  # pragma: no cover
        return ListResourcesAssociatedToCustomLineItemResponseElement.make_many(
            self.boto3_raw_data["AssociatedResources"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListResourcesAssociatedToCustomLineItemOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourcesAssociatedToCustomLineItemOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateBillingGroupInput:
    boto3_raw_data: "type_defs.UpdateBillingGroupInputTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Name = field("Name")
    Status = field("Status")

    @cached_property
    def ComputationPreference(self):  # pragma: no cover
        return ComputationPreference.make_one(
            self.boto3_raw_data["ComputationPreference"]
        )

    Description = field("Description")

    @cached_property
    def AccountGrouping(self):  # pragma: no cover
        return UpdateBillingGroupAccountGrouping.make_one(
            self.boto3_raw_data["AccountGrouping"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateBillingGroupInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateBillingGroupInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateBillingGroupOutput:
    boto3_raw_data: "type_defs.UpdateBillingGroupOutputTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Name = field("Name")
    Description = field("Description")
    PrimaryAccountId = field("PrimaryAccountId")
    PricingPlanArn = field("PricingPlanArn")
    Size = field("Size")
    LastModifiedTime = field("LastModifiedTime")
    Status = field("Status")
    StatusReason = field("StatusReason")

    @cached_property
    def AccountGrouping(self):  # pragma: no cover
        return UpdateBillingGroupAccountGrouping.make_one(
            self.boto3_raw_data["AccountGrouping"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateBillingGroupOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateBillingGroupOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateTieringInput:
    boto3_raw_data: "type_defs.UpdateTieringInputTypeDef" = dataclasses.field()

    @cached_property
    def FreeTier(self):  # pragma: no cover
        return UpdateFreeTierConfig.make_one(self.boto3_raw_data["FreeTier"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateTieringInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTieringInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchAssociateResourcesToCustomLineItemOutput:
    boto3_raw_data: "type_defs.BatchAssociateResourcesToCustomLineItemOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def SuccessfullyAssociatedResources(self):  # pragma: no cover
        return AssociateResourceResponseElement.make_many(
            self.boto3_raw_data["SuccessfullyAssociatedResources"]
        )

    @cached_property
    def FailedAssociatedResources(self):  # pragma: no cover
        return AssociateResourceResponseElement.make_many(
            self.boto3_raw_data["FailedAssociatedResources"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchAssociateResourcesToCustomLineItemOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchAssociateResourcesToCustomLineItemOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDisassociateResourcesFromCustomLineItemOutput:
    boto3_raw_data: (
        "type_defs.BatchDisassociateResourcesFromCustomLineItemOutputTypeDef"
    ) = dataclasses.field()

    @cached_property
    def SuccessfullyDisassociatedResources(self):  # pragma: no cover
        return DisassociateResourceResponseElement.make_many(
            self.boto3_raw_data["SuccessfullyDisassociatedResources"]
        )

    @cached_property
    def FailedDisassociatedResources(self):  # pragma: no cover
        return DisassociateResourceResponseElement.make_many(
            self.boto3_raw_data["FailedDisassociatedResources"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchDisassociateResourcesFromCustomLineItemOutputTypeDef"
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
                "type_defs.BatchDisassociateResourcesFromCustomLineItemOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBillingGroupCostReportOutput:
    boto3_raw_data: "type_defs.GetBillingGroupCostReportOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def BillingGroupCostReportResults(self):  # pragma: no cover
        return BillingGroupCostReportResultElement.make_many(
            self.boto3_raw_data["BillingGroupCostReportResults"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetBillingGroupCostReportOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBillingGroupCostReportOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBillingGroupsOutput:
    boto3_raw_data: "type_defs.ListBillingGroupsOutputTypeDef" = dataclasses.field()

    @cached_property
    def BillingGroups(self):  # pragma: no cover
        return BillingGroupListElement.make_many(self.boto3_raw_data["BillingGroups"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBillingGroupsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBillingGroupsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePricingRuleInput:
    boto3_raw_data: "type_defs.CreatePricingRuleInputTypeDef" = dataclasses.field()

    Name = field("Name")
    Scope = field("Scope")
    Type = field("Type")
    ClientToken = field("ClientToken")
    Description = field("Description")
    ModifierPercentage = field("ModifierPercentage")
    Service = field("Service")
    Tags = field("Tags")
    BillingEntity = field("BillingEntity")

    @cached_property
    def Tiering(self):  # pragma: no cover
        return CreateTieringInput.make_one(self.boto3_raw_data["Tiering"])

    UsageType = field("UsageType")
    Operation = field("Operation")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePricingRuleInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePricingRuleInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PricingRuleListElement:
    boto3_raw_data: "type_defs.PricingRuleListElementTypeDef" = dataclasses.field()

    Name = field("Name")
    Arn = field("Arn")
    Description = field("Description")
    Scope = field("Scope")
    Type = field("Type")
    ModifierPercentage = field("ModifierPercentage")
    Service = field("Service")
    AssociatedPricingPlanCount = field("AssociatedPricingPlanCount")
    CreationTime = field("CreationTime")
    LastModifiedTime = field("LastModifiedTime")
    BillingEntity = field("BillingEntity")

    @cached_property
    def Tiering(self):  # pragma: no cover
        return Tiering.make_one(self.boto3_raw_data["Tiering"])

    UsageType = field("UsageType")
    Operation = field("Operation")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PricingRuleListElementTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PricingRuleListElementTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomLineItemChargeDetails:
    boto3_raw_data: "type_defs.CustomLineItemChargeDetailsTypeDef" = dataclasses.field()

    Type = field("Type")

    @cached_property
    def Flat(self):  # pragma: no cover
        return CustomLineItemFlatChargeDetails.make_one(self.boto3_raw_data["Flat"])

    @cached_property
    def Percentage(self):  # pragma: no cover
        return CustomLineItemPercentageChargeDetails.make_one(
            self.boto3_raw_data["Percentage"]
        )

    LineItemFilters = field("LineItemFilters")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CustomLineItemChargeDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomLineItemChargeDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCustomLineItemChargeDetails:
    boto3_raw_data: "type_defs.UpdateCustomLineItemChargeDetailsTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Flat(self):  # pragma: no cover
        return UpdateCustomLineItemFlatChargeDetails.make_one(
            self.boto3_raw_data["Flat"]
        )

    @cached_property
    def Percentage(self):  # pragma: no cover
        return UpdateCustomLineItemPercentageChargeDetails.make_one(
            self.boto3_raw_data["Percentage"]
        )

    LineItemFilters = field("LineItemFilters")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateCustomLineItemChargeDetailsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCustomLineItemChargeDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomLineItemListElement:
    boto3_raw_data: "type_defs.CustomLineItemListElementTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Name = field("Name")

    @cached_property
    def ChargeDetails(self):  # pragma: no cover
        return ListCustomLineItemChargeDetails.make_one(
            self.boto3_raw_data["ChargeDetails"]
        )

    CurrencyCode = field("CurrencyCode")
    Description = field("Description")
    ProductCode = field("ProductCode")
    BillingGroupArn = field("BillingGroupArn")
    CreationTime = field("CreationTime")
    LastModifiedTime = field("LastModifiedTime")
    AssociationSize = field("AssociationSize")
    AccountId = field("AccountId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CustomLineItemListElementTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomLineItemListElementTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomLineItemVersionListElement:
    boto3_raw_data: "type_defs.CustomLineItemVersionListElementTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")

    @cached_property
    def ChargeDetails(self):  # pragma: no cover
        return ListCustomLineItemChargeDetails.make_one(
            self.boto3_raw_data["ChargeDetails"]
        )

    CurrencyCode = field("CurrencyCode")
    Description = field("Description")
    ProductCode = field("ProductCode")
    BillingGroupArn = field("BillingGroupArn")
    CreationTime = field("CreationTime")
    LastModifiedTime = field("LastModifiedTime")
    AssociationSize = field("AssociationSize")
    StartBillingPeriod = field("StartBillingPeriod")
    EndBillingPeriod = field("EndBillingPeriod")
    Arn = field("Arn")
    StartTime = field("StartTime")
    AccountId = field("AccountId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CustomLineItemVersionListElementTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomLineItemVersionListElementTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCustomLineItemOutput:
    boto3_raw_data: "type_defs.UpdateCustomLineItemOutputTypeDef" = dataclasses.field()

    Arn = field("Arn")
    BillingGroupArn = field("BillingGroupArn")
    Name = field("Name")
    Description = field("Description")

    @cached_property
    def ChargeDetails(self):  # pragma: no cover
        return ListCustomLineItemChargeDetails.make_one(
            self.boto3_raw_data["ChargeDetails"]
        )

    LastModifiedTime = field("LastModifiedTime")
    AssociationSize = field("AssociationSize")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateCustomLineItemOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCustomLineItemOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCustomLineItemVersionsInputPaginate:
    boto3_raw_data: "type_defs.ListCustomLineItemVersionsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")

    @cached_property
    def Filters(self):  # pragma: no cover
        return ListCustomLineItemVersionsFilter.make_one(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCustomLineItemVersionsInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCustomLineItemVersionsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCustomLineItemVersionsInput:
    boto3_raw_data: "type_defs.ListCustomLineItemVersionsInputTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @cached_property
    def Filters(self):  # pragma: no cover
        return ListCustomLineItemVersionsFilter.make_one(self.boto3_raw_data["Filters"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListCustomLineItemVersionsInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCustomLineItemVersionsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePricingRuleInput:
    boto3_raw_data: "type_defs.UpdatePricingRuleInputTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Name = field("Name")
    Description = field("Description")
    Type = field("Type")
    ModifierPercentage = field("ModifierPercentage")

    @cached_property
    def Tiering(self):  # pragma: no cover
        return UpdateTieringInput.make_one(self.boto3_raw_data["Tiering"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdatePricingRuleInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePricingRuleInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePricingRuleOutput:
    boto3_raw_data: "type_defs.UpdatePricingRuleOutputTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Name = field("Name")
    Description = field("Description")
    Scope = field("Scope")
    Type = field("Type")
    ModifierPercentage = field("ModifierPercentage")
    Service = field("Service")
    AssociatedPricingPlanCount = field("AssociatedPricingPlanCount")
    LastModifiedTime = field("LastModifiedTime")
    BillingEntity = field("BillingEntity")

    @cached_property
    def Tiering(self):  # pragma: no cover
        return UpdateTieringInput.make_one(self.boto3_raw_data["Tiering"])

    UsageType = field("UsageType")
    Operation = field("Operation")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdatePricingRuleOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePricingRuleOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPricingRulesOutput:
    boto3_raw_data: "type_defs.ListPricingRulesOutputTypeDef" = dataclasses.field()

    BillingPeriod = field("BillingPeriod")

    @cached_property
    def PricingRules(self):  # pragma: no cover
        return PricingRuleListElement.make_many(self.boto3_raw_data["PricingRules"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPricingRulesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPricingRulesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCustomLineItemInput:
    boto3_raw_data: "type_defs.CreateCustomLineItemInputTypeDef" = dataclasses.field()

    Name = field("Name")
    Description = field("Description")
    BillingGroupArn = field("BillingGroupArn")

    @cached_property
    def ChargeDetails(self):  # pragma: no cover
        return CustomLineItemChargeDetails.make_one(
            self.boto3_raw_data["ChargeDetails"]
        )

    ClientToken = field("ClientToken")

    @cached_property
    def BillingPeriodRange(self):  # pragma: no cover
        return CustomLineItemBillingPeriodRange.make_one(
            self.boto3_raw_data["BillingPeriodRange"]
        )

    Tags = field("Tags")
    AccountId = field("AccountId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateCustomLineItemInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCustomLineItemInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCustomLineItemInput:
    boto3_raw_data: "type_defs.UpdateCustomLineItemInputTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Name = field("Name")
    Description = field("Description")

    @cached_property
    def ChargeDetails(self):  # pragma: no cover
        return UpdateCustomLineItemChargeDetails.make_one(
            self.boto3_raw_data["ChargeDetails"]
        )

    @cached_property
    def BillingPeriodRange(self):  # pragma: no cover
        return CustomLineItemBillingPeriodRange.make_one(
            self.boto3_raw_data["BillingPeriodRange"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateCustomLineItemInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCustomLineItemInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCustomLineItemsOutput:
    boto3_raw_data: "type_defs.ListCustomLineItemsOutputTypeDef" = dataclasses.field()

    @cached_property
    def CustomLineItems(self):  # pragma: no cover
        return CustomLineItemListElement.make_many(
            self.boto3_raw_data["CustomLineItems"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCustomLineItemsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCustomLineItemsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCustomLineItemVersionsOutput:
    boto3_raw_data: "type_defs.ListCustomLineItemVersionsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CustomLineItemVersions(self):  # pragma: no cover
        return CustomLineItemVersionListElement.make_many(
            self.boto3_raw_data["CustomLineItemVersions"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListCustomLineItemVersionsOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCustomLineItemVersionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
