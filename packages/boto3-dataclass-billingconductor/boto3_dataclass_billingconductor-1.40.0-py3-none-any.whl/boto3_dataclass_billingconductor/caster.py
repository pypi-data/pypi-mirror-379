# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_billingconductor import type_defs as bs_td


class BILLINGCONDUCTORCaster:

    def associate_accounts(
        self,
        res: "bs_td.AssociateAccountsOutputTypeDef",
    ) -> "dc_td.AssociateAccountsOutput":
        return dc_td.AssociateAccountsOutput.make_one(res)

    def associate_pricing_rules(
        self,
        res: "bs_td.AssociatePricingRulesOutputTypeDef",
    ) -> "dc_td.AssociatePricingRulesOutput":
        return dc_td.AssociatePricingRulesOutput.make_one(res)

    def batch_associate_resources_to_custom_line_item(
        self,
        res: "bs_td.BatchAssociateResourcesToCustomLineItemOutputTypeDef",
    ) -> "dc_td.BatchAssociateResourcesToCustomLineItemOutput":
        return dc_td.BatchAssociateResourcesToCustomLineItemOutput.make_one(res)

    def batch_disassociate_resources_from_custom_line_item(
        self,
        res: "bs_td.BatchDisassociateResourcesFromCustomLineItemOutputTypeDef",
    ) -> "dc_td.BatchDisassociateResourcesFromCustomLineItemOutput":
        return dc_td.BatchDisassociateResourcesFromCustomLineItemOutput.make_one(res)

    def create_billing_group(
        self,
        res: "bs_td.CreateBillingGroupOutputTypeDef",
    ) -> "dc_td.CreateBillingGroupOutput":
        return dc_td.CreateBillingGroupOutput.make_one(res)

    def create_custom_line_item(
        self,
        res: "bs_td.CreateCustomLineItemOutputTypeDef",
    ) -> "dc_td.CreateCustomLineItemOutput":
        return dc_td.CreateCustomLineItemOutput.make_one(res)

    def create_pricing_plan(
        self,
        res: "bs_td.CreatePricingPlanOutputTypeDef",
    ) -> "dc_td.CreatePricingPlanOutput":
        return dc_td.CreatePricingPlanOutput.make_one(res)

    def create_pricing_rule(
        self,
        res: "bs_td.CreatePricingRuleOutputTypeDef",
    ) -> "dc_td.CreatePricingRuleOutput":
        return dc_td.CreatePricingRuleOutput.make_one(res)

    def delete_billing_group(
        self,
        res: "bs_td.DeleteBillingGroupOutputTypeDef",
    ) -> "dc_td.DeleteBillingGroupOutput":
        return dc_td.DeleteBillingGroupOutput.make_one(res)

    def delete_custom_line_item(
        self,
        res: "bs_td.DeleteCustomLineItemOutputTypeDef",
    ) -> "dc_td.DeleteCustomLineItemOutput":
        return dc_td.DeleteCustomLineItemOutput.make_one(res)

    def delete_pricing_plan(
        self,
        res: "bs_td.DeletePricingPlanOutputTypeDef",
    ) -> "dc_td.DeletePricingPlanOutput":
        return dc_td.DeletePricingPlanOutput.make_one(res)

    def delete_pricing_rule(
        self,
        res: "bs_td.DeletePricingRuleOutputTypeDef",
    ) -> "dc_td.DeletePricingRuleOutput":
        return dc_td.DeletePricingRuleOutput.make_one(res)

    def disassociate_accounts(
        self,
        res: "bs_td.DisassociateAccountsOutputTypeDef",
    ) -> "dc_td.DisassociateAccountsOutput":
        return dc_td.DisassociateAccountsOutput.make_one(res)

    def disassociate_pricing_rules(
        self,
        res: "bs_td.DisassociatePricingRulesOutputTypeDef",
    ) -> "dc_td.DisassociatePricingRulesOutput":
        return dc_td.DisassociatePricingRulesOutput.make_one(res)

    def get_billing_group_cost_report(
        self,
        res: "bs_td.GetBillingGroupCostReportOutputTypeDef",
    ) -> "dc_td.GetBillingGroupCostReportOutput":
        return dc_td.GetBillingGroupCostReportOutput.make_one(res)

    def list_account_associations(
        self,
        res: "bs_td.ListAccountAssociationsOutputTypeDef",
    ) -> "dc_td.ListAccountAssociationsOutput":
        return dc_td.ListAccountAssociationsOutput.make_one(res)

    def list_billing_group_cost_reports(
        self,
        res: "bs_td.ListBillingGroupCostReportsOutputTypeDef",
    ) -> "dc_td.ListBillingGroupCostReportsOutput":
        return dc_td.ListBillingGroupCostReportsOutput.make_one(res)

    def list_billing_groups(
        self,
        res: "bs_td.ListBillingGroupsOutputTypeDef",
    ) -> "dc_td.ListBillingGroupsOutput":
        return dc_td.ListBillingGroupsOutput.make_one(res)

    def list_custom_line_item_versions(
        self,
        res: "bs_td.ListCustomLineItemVersionsOutputTypeDef",
    ) -> "dc_td.ListCustomLineItemVersionsOutput":
        return dc_td.ListCustomLineItemVersionsOutput.make_one(res)

    def list_custom_line_items(
        self,
        res: "bs_td.ListCustomLineItemsOutputTypeDef",
    ) -> "dc_td.ListCustomLineItemsOutput":
        return dc_td.ListCustomLineItemsOutput.make_one(res)

    def list_pricing_plans(
        self,
        res: "bs_td.ListPricingPlansOutputTypeDef",
    ) -> "dc_td.ListPricingPlansOutput":
        return dc_td.ListPricingPlansOutput.make_one(res)

    def list_pricing_plans_associated_with_pricing_rule(
        self,
        res: "bs_td.ListPricingPlansAssociatedWithPricingRuleOutputTypeDef",
    ) -> "dc_td.ListPricingPlansAssociatedWithPricingRuleOutput":
        return dc_td.ListPricingPlansAssociatedWithPricingRuleOutput.make_one(res)

    def list_pricing_rules(
        self,
        res: "bs_td.ListPricingRulesOutputTypeDef",
    ) -> "dc_td.ListPricingRulesOutput":
        return dc_td.ListPricingRulesOutput.make_one(res)

    def list_pricing_rules_associated_to_pricing_plan(
        self,
        res: "bs_td.ListPricingRulesAssociatedToPricingPlanOutputTypeDef",
    ) -> "dc_td.ListPricingRulesAssociatedToPricingPlanOutput":
        return dc_td.ListPricingRulesAssociatedToPricingPlanOutput.make_one(res)

    def list_resources_associated_to_custom_line_item(
        self,
        res: "bs_td.ListResourcesAssociatedToCustomLineItemOutputTypeDef",
    ) -> "dc_td.ListResourcesAssociatedToCustomLineItemOutput":
        return dc_td.ListResourcesAssociatedToCustomLineItemOutput.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def update_billing_group(
        self,
        res: "bs_td.UpdateBillingGroupOutputTypeDef",
    ) -> "dc_td.UpdateBillingGroupOutput":
        return dc_td.UpdateBillingGroupOutput.make_one(res)

    def update_custom_line_item(
        self,
        res: "bs_td.UpdateCustomLineItemOutputTypeDef",
    ) -> "dc_td.UpdateCustomLineItemOutput":
        return dc_td.UpdateCustomLineItemOutput.make_one(res)

    def update_pricing_plan(
        self,
        res: "bs_td.UpdatePricingPlanOutputTypeDef",
    ) -> "dc_td.UpdatePricingPlanOutput":
        return dc_td.UpdatePricingPlanOutput.make_one(res)

    def update_pricing_rule(
        self,
        res: "bs_td.UpdatePricingRuleOutputTypeDef",
    ) -> "dc_td.UpdatePricingRuleOutput":
        return dc_td.UpdatePricingRuleOutput.make_one(res)


billingconductor_caster = BILLINGCONDUCTORCaster()
