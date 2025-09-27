# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_bcm_pricing_calculator import type_defs as bs_td


class BCM_PRICING_CALCULATORCaster:

    def batch_create_bill_scenario_commitment_modification(
        self,
        res: "bs_td.BatchCreateBillScenarioCommitmentModificationResponseTypeDef",
    ) -> "dc_td.BatchCreateBillScenarioCommitmentModificationResponse":
        return dc_td.BatchCreateBillScenarioCommitmentModificationResponse.make_one(res)

    def batch_create_bill_scenario_usage_modification(
        self,
        res: "bs_td.BatchCreateBillScenarioUsageModificationResponseTypeDef",
    ) -> "dc_td.BatchCreateBillScenarioUsageModificationResponse":
        return dc_td.BatchCreateBillScenarioUsageModificationResponse.make_one(res)

    def batch_create_workload_estimate_usage(
        self,
        res: "bs_td.BatchCreateWorkloadEstimateUsageResponseTypeDef",
    ) -> "dc_td.BatchCreateWorkloadEstimateUsageResponse":
        return dc_td.BatchCreateWorkloadEstimateUsageResponse.make_one(res)

    def batch_delete_bill_scenario_commitment_modification(
        self,
        res: "bs_td.BatchDeleteBillScenarioCommitmentModificationResponseTypeDef",
    ) -> "dc_td.BatchDeleteBillScenarioCommitmentModificationResponse":
        return dc_td.BatchDeleteBillScenarioCommitmentModificationResponse.make_one(res)

    def batch_delete_bill_scenario_usage_modification(
        self,
        res: "bs_td.BatchDeleteBillScenarioUsageModificationResponseTypeDef",
    ) -> "dc_td.BatchDeleteBillScenarioUsageModificationResponse":
        return dc_td.BatchDeleteBillScenarioUsageModificationResponse.make_one(res)

    def batch_delete_workload_estimate_usage(
        self,
        res: "bs_td.BatchDeleteWorkloadEstimateUsageResponseTypeDef",
    ) -> "dc_td.BatchDeleteWorkloadEstimateUsageResponse":
        return dc_td.BatchDeleteWorkloadEstimateUsageResponse.make_one(res)

    def batch_update_bill_scenario_commitment_modification(
        self,
        res: "bs_td.BatchUpdateBillScenarioCommitmentModificationResponseTypeDef",
    ) -> "dc_td.BatchUpdateBillScenarioCommitmentModificationResponse":
        return dc_td.BatchUpdateBillScenarioCommitmentModificationResponse.make_one(res)

    def batch_update_bill_scenario_usage_modification(
        self,
        res: "bs_td.BatchUpdateBillScenarioUsageModificationResponseTypeDef",
    ) -> "dc_td.BatchUpdateBillScenarioUsageModificationResponse":
        return dc_td.BatchUpdateBillScenarioUsageModificationResponse.make_one(res)

    def batch_update_workload_estimate_usage(
        self,
        res: "bs_td.BatchUpdateWorkloadEstimateUsageResponseTypeDef",
    ) -> "dc_td.BatchUpdateWorkloadEstimateUsageResponse":
        return dc_td.BatchUpdateWorkloadEstimateUsageResponse.make_one(res)

    def create_bill_estimate(
        self,
        res: "bs_td.CreateBillEstimateResponseTypeDef",
    ) -> "dc_td.CreateBillEstimateResponse":
        return dc_td.CreateBillEstimateResponse.make_one(res)

    def create_bill_scenario(
        self,
        res: "bs_td.CreateBillScenarioResponseTypeDef",
    ) -> "dc_td.CreateBillScenarioResponse":
        return dc_td.CreateBillScenarioResponse.make_one(res)

    def create_workload_estimate(
        self,
        res: "bs_td.CreateWorkloadEstimateResponseTypeDef",
    ) -> "dc_td.CreateWorkloadEstimateResponse":
        return dc_td.CreateWorkloadEstimateResponse.make_one(res)

    def get_bill_estimate(
        self,
        res: "bs_td.GetBillEstimateResponseTypeDef",
    ) -> "dc_td.GetBillEstimateResponse":
        return dc_td.GetBillEstimateResponse.make_one(res)

    def get_bill_scenario(
        self,
        res: "bs_td.GetBillScenarioResponseTypeDef",
    ) -> "dc_td.GetBillScenarioResponse":
        return dc_td.GetBillScenarioResponse.make_one(res)

    def get_preferences(
        self,
        res: "bs_td.GetPreferencesResponseTypeDef",
    ) -> "dc_td.GetPreferencesResponse":
        return dc_td.GetPreferencesResponse.make_one(res)

    def get_workload_estimate(
        self,
        res: "bs_td.GetWorkloadEstimateResponseTypeDef",
    ) -> "dc_td.GetWorkloadEstimateResponse":
        return dc_td.GetWorkloadEstimateResponse.make_one(res)

    def list_bill_estimate_commitments(
        self,
        res: "bs_td.ListBillEstimateCommitmentsResponseTypeDef",
    ) -> "dc_td.ListBillEstimateCommitmentsResponse":
        return dc_td.ListBillEstimateCommitmentsResponse.make_one(res)

    def list_bill_estimate_input_commitment_modifications(
        self,
        res: "bs_td.ListBillEstimateInputCommitmentModificationsResponseTypeDef",
    ) -> "dc_td.ListBillEstimateInputCommitmentModificationsResponse":
        return dc_td.ListBillEstimateInputCommitmentModificationsResponse.make_one(res)

    def list_bill_estimate_input_usage_modifications(
        self,
        res: "bs_td.ListBillEstimateInputUsageModificationsResponseTypeDef",
    ) -> "dc_td.ListBillEstimateInputUsageModificationsResponse":
        return dc_td.ListBillEstimateInputUsageModificationsResponse.make_one(res)

    def list_bill_estimate_line_items(
        self,
        res: "bs_td.ListBillEstimateLineItemsResponseTypeDef",
    ) -> "dc_td.ListBillEstimateLineItemsResponse":
        return dc_td.ListBillEstimateLineItemsResponse.make_one(res)

    def list_bill_estimates(
        self,
        res: "bs_td.ListBillEstimatesResponseTypeDef",
    ) -> "dc_td.ListBillEstimatesResponse":
        return dc_td.ListBillEstimatesResponse.make_one(res)

    def list_bill_scenario_commitment_modifications(
        self,
        res: "bs_td.ListBillScenarioCommitmentModificationsResponseTypeDef",
    ) -> "dc_td.ListBillScenarioCommitmentModificationsResponse":
        return dc_td.ListBillScenarioCommitmentModificationsResponse.make_one(res)

    def list_bill_scenario_usage_modifications(
        self,
        res: "bs_td.ListBillScenarioUsageModificationsResponseTypeDef",
    ) -> "dc_td.ListBillScenarioUsageModificationsResponse":
        return dc_td.ListBillScenarioUsageModificationsResponse.make_one(res)

    def list_bill_scenarios(
        self,
        res: "bs_td.ListBillScenariosResponseTypeDef",
    ) -> "dc_td.ListBillScenariosResponse":
        return dc_td.ListBillScenariosResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def list_workload_estimate_usage(
        self,
        res: "bs_td.ListWorkloadEstimateUsageResponseTypeDef",
    ) -> "dc_td.ListWorkloadEstimateUsageResponse":
        return dc_td.ListWorkloadEstimateUsageResponse.make_one(res)

    def list_workload_estimates(
        self,
        res: "bs_td.ListWorkloadEstimatesResponseTypeDef",
    ) -> "dc_td.ListWorkloadEstimatesResponse":
        return dc_td.ListWorkloadEstimatesResponse.make_one(res)

    def update_bill_estimate(
        self,
        res: "bs_td.UpdateBillEstimateResponseTypeDef",
    ) -> "dc_td.UpdateBillEstimateResponse":
        return dc_td.UpdateBillEstimateResponse.make_one(res)

    def update_bill_scenario(
        self,
        res: "bs_td.UpdateBillScenarioResponseTypeDef",
    ) -> "dc_td.UpdateBillScenarioResponse":
        return dc_td.UpdateBillScenarioResponse.make_one(res)

    def update_preferences(
        self,
        res: "bs_td.UpdatePreferencesResponseTypeDef",
    ) -> "dc_td.UpdatePreferencesResponse":
        return dc_td.UpdatePreferencesResponse.make_one(res)

    def update_workload_estimate(
        self,
        res: "bs_td.UpdateWorkloadEstimateResponseTypeDef",
    ) -> "dc_td.UpdateWorkloadEstimateResponse":
        return dc_td.UpdateWorkloadEstimateResponse.make_one(res)


bcm_pricing_calculator_caster = BCM_PRICING_CALCULATORCaster()
