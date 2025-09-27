# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_ce import type_defs as bs_td


class CECaster:

    def create_anomaly_monitor(
        self,
        res: "bs_td.CreateAnomalyMonitorResponseTypeDef",
    ) -> "dc_td.CreateAnomalyMonitorResponse":
        return dc_td.CreateAnomalyMonitorResponse.make_one(res)

    def create_anomaly_subscription(
        self,
        res: "bs_td.CreateAnomalySubscriptionResponseTypeDef",
    ) -> "dc_td.CreateAnomalySubscriptionResponse":
        return dc_td.CreateAnomalySubscriptionResponse.make_one(res)

    def create_cost_category_definition(
        self,
        res: "bs_td.CreateCostCategoryDefinitionResponseTypeDef",
    ) -> "dc_td.CreateCostCategoryDefinitionResponse":
        return dc_td.CreateCostCategoryDefinitionResponse.make_one(res)

    def delete_cost_category_definition(
        self,
        res: "bs_td.DeleteCostCategoryDefinitionResponseTypeDef",
    ) -> "dc_td.DeleteCostCategoryDefinitionResponse":
        return dc_td.DeleteCostCategoryDefinitionResponse.make_one(res)

    def describe_cost_category_definition(
        self,
        res: "bs_td.DescribeCostCategoryDefinitionResponseTypeDef",
    ) -> "dc_td.DescribeCostCategoryDefinitionResponse":
        return dc_td.DescribeCostCategoryDefinitionResponse.make_one(res)

    def get_anomalies(
        self,
        res: "bs_td.GetAnomaliesResponseTypeDef",
    ) -> "dc_td.GetAnomaliesResponse":
        return dc_td.GetAnomaliesResponse.make_one(res)

    def get_anomaly_monitors(
        self,
        res: "bs_td.GetAnomalyMonitorsResponseTypeDef",
    ) -> "dc_td.GetAnomalyMonitorsResponse":
        return dc_td.GetAnomalyMonitorsResponse.make_one(res)

    def get_anomaly_subscriptions(
        self,
        res: "bs_td.GetAnomalySubscriptionsResponseTypeDef",
    ) -> "dc_td.GetAnomalySubscriptionsResponse":
        return dc_td.GetAnomalySubscriptionsResponse.make_one(res)

    def get_approximate_usage_records(
        self,
        res: "bs_td.GetApproximateUsageRecordsResponseTypeDef",
    ) -> "dc_td.GetApproximateUsageRecordsResponse":
        return dc_td.GetApproximateUsageRecordsResponse.make_one(res)

    def get_commitment_purchase_analysis(
        self,
        res: "bs_td.GetCommitmentPurchaseAnalysisResponseTypeDef",
    ) -> "dc_td.GetCommitmentPurchaseAnalysisResponse":
        return dc_td.GetCommitmentPurchaseAnalysisResponse.make_one(res)

    def get_cost_and_usage(
        self,
        res: "bs_td.GetCostAndUsageResponseTypeDef",
    ) -> "dc_td.GetCostAndUsageResponse":
        return dc_td.GetCostAndUsageResponse.make_one(res)

    def get_cost_and_usage_comparisons(
        self,
        res: "bs_td.GetCostAndUsageComparisonsResponseTypeDef",
    ) -> "dc_td.GetCostAndUsageComparisonsResponse":
        return dc_td.GetCostAndUsageComparisonsResponse.make_one(res)

    def get_cost_and_usage_with_resources(
        self,
        res: "bs_td.GetCostAndUsageWithResourcesResponseTypeDef",
    ) -> "dc_td.GetCostAndUsageWithResourcesResponse":
        return dc_td.GetCostAndUsageWithResourcesResponse.make_one(res)

    def get_cost_categories(
        self,
        res: "bs_td.GetCostCategoriesResponseTypeDef",
    ) -> "dc_td.GetCostCategoriesResponse":
        return dc_td.GetCostCategoriesResponse.make_one(res)

    def get_cost_comparison_drivers(
        self,
        res: "bs_td.GetCostComparisonDriversResponseTypeDef",
    ) -> "dc_td.GetCostComparisonDriversResponse":
        return dc_td.GetCostComparisonDriversResponse.make_one(res)

    def get_cost_forecast(
        self,
        res: "bs_td.GetCostForecastResponseTypeDef",
    ) -> "dc_td.GetCostForecastResponse":
        return dc_td.GetCostForecastResponse.make_one(res)

    def get_dimension_values(
        self,
        res: "bs_td.GetDimensionValuesResponseTypeDef",
    ) -> "dc_td.GetDimensionValuesResponse":
        return dc_td.GetDimensionValuesResponse.make_one(res)

    def get_reservation_coverage(
        self,
        res: "bs_td.GetReservationCoverageResponseTypeDef",
    ) -> "dc_td.GetReservationCoverageResponse":
        return dc_td.GetReservationCoverageResponse.make_one(res)

    def get_reservation_purchase_recommendation(
        self,
        res: "bs_td.GetReservationPurchaseRecommendationResponseTypeDef",
    ) -> "dc_td.GetReservationPurchaseRecommendationResponse":
        return dc_td.GetReservationPurchaseRecommendationResponse.make_one(res)

    def get_reservation_utilization(
        self,
        res: "bs_td.GetReservationUtilizationResponseTypeDef",
    ) -> "dc_td.GetReservationUtilizationResponse":
        return dc_td.GetReservationUtilizationResponse.make_one(res)

    def get_rightsizing_recommendation(
        self,
        res: "bs_td.GetRightsizingRecommendationResponseTypeDef",
    ) -> "dc_td.GetRightsizingRecommendationResponse":
        return dc_td.GetRightsizingRecommendationResponse.make_one(res)

    def get_savings_plan_purchase_recommendation_details(
        self,
        res: "bs_td.GetSavingsPlanPurchaseRecommendationDetailsResponseTypeDef",
    ) -> "dc_td.GetSavingsPlanPurchaseRecommendationDetailsResponse":
        return dc_td.GetSavingsPlanPurchaseRecommendationDetailsResponse.make_one(res)

    def get_savings_plans_coverage(
        self,
        res: "bs_td.GetSavingsPlansCoverageResponseTypeDef",
    ) -> "dc_td.GetSavingsPlansCoverageResponse":
        return dc_td.GetSavingsPlansCoverageResponse.make_one(res)

    def get_savings_plans_purchase_recommendation(
        self,
        res: "bs_td.GetSavingsPlansPurchaseRecommendationResponseTypeDef",
    ) -> "dc_td.GetSavingsPlansPurchaseRecommendationResponse":
        return dc_td.GetSavingsPlansPurchaseRecommendationResponse.make_one(res)

    def get_savings_plans_utilization(
        self,
        res: "bs_td.GetSavingsPlansUtilizationResponseTypeDef",
    ) -> "dc_td.GetSavingsPlansUtilizationResponse":
        return dc_td.GetSavingsPlansUtilizationResponse.make_one(res)

    def get_savings_plans_utilization_details(
        self,
        res: "bs_td.GetSavingsPlansUtilizationDetailsResponseTypeDef",
    ) -> "dc_td.GetSavingsPlansUtilizationDetailsResponse":
        return dc_td.GetSavingsPlansUtilizationDetailsResponse.make_one(res)

    def get_tags(
        self,
        res: "bs_td.GetTagsResponseTypeDef",
    ) -> "dc_td.GetTagsResponse":
        return dc_td.GetTagsResponse.make_one(res)

    def get_usage_forecast(
        self,
        res: "bs_td.GetUsageForecastResponseTypeDef",
    ) -> "dc_td.GetUsageForecastResponse":
        return dc_td.GetUsageForecastResponse.make_one(res)

    def list_commitment_purchase_analyses(
        self,
        res: "bs_td.ListCommitmentPurchaseAnalysesResponseTypeDef",
    ) -> "dc_td.ListCommitmentPurchaseAnalysesResponse":
        return dc_td.ListCommitmentPurchaseAnalysesResponse.make_one(res)

    def list_cost_allocation_tag_backfill_history(
        self,
        res: "bs_td.ListCostAllocationTagBackfillHistoryResponseTypeDef",
    ) -> "dc_td.ListCostAllocationTagBackfillHistoryResponse":
        return dc_td.ListCostAllocationTagBackfillHistoryResponse.make_one(res)

    def list_cost_allocation_tags(
        self,
        res: "bs_td.ListCostAllocationTagsResponseTypeDef",
    ) -> "dc_td.ListCostAllocationTagsResponse":
        return dc_td.ListCostAllocationTagsResponse.make_one(res)

    def list_cost_category_definitions(
        self,
        res: "bs_td.ListCostCategoryDefinitionsResponseTypeDef",
    ) -> "dc_td.ListCostCategoryDefinitionsResponse":
        return dc_td.ListCostCategoryDefinitionsResponse.make_one(res)

    def list_savings_plans_purchase_recommendation_generation(
        self,
        res: "bs_td.ListSavingsPlansPurchaseRecommendationGenerationResponseTypeDef",
    ) -> "dc_td.ListSavingsPlansPurchaseRecommendationGenerationResponse":
        return dc_td.ListSavingsPlansPurchaseRecommendationGenerationResponse.make_one(
            res
        )

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def provide_anomaly_feedback(
        self,
        res: "bs_td.ProvideAnomalyFeedbackResponseTypeDef",
    ) -> "dc_td.ProvideAnomalyFeedbackResponse":
        return dc_td.ProvideAnomalyFeedbackResponse.make_one(res)

    def start_commitment_purchase_analysis(
        self,
        res: "bs_td.StartCommitmentPurchaseAnalysisResponseTypeDef",
    ) -> "dc_td.StartCommitmentPurchaseAnalysisResponse":
        return dc_td.StartCommitmentPurchaseAnalysisResponse.make_one(res)

    def start_cost_allocation_tag_backfill(
        self,
        res: "bs_td.StartCostAllocationTagBackfillResponseTypeDef",
    ) -> "dc_td.StartCostAllocationTagBackfillResponse":
        return dc_td.StartCostAllocationTagBackfillResponse.make_one(res)

    def start_savings_plans_purchase_recommendation_generation(
        self,
        res: "bs_td.StartSavingsPlansPurchaseRecommendationGenerationResponseTypeDef",
    ) -> "dc_td.StartSavingsPlansPurchaseRecommendationGenerationResponse":
        return dc_td.StartSavingsPlansPurchaseRecommendationGenerationResponse.make_one(
            res
        )

    def update_anomaly_monitor(
        self,
        res: "bs_td.UpdateAnomalyMonitorResponseTypeDef",
    ) -> "dc_td.UpdateAnomalyMonitorResponse":
        return dc_td.UpdateAnomalyMonitorResponse.make_one(res)

    def update_anomaly_subscription(
        self,
        res: "bs_td.UpdateAnomalySubscriptionResponseTypeDef",
    ) -> "dc_td.UpdateAnomalySubscriptionResponse":
        return dc_td.UpdateAnomalySubscriptionResponse.make_one(res)

    def update_cost_allocation_tags_status(
        self,
        res: "bs_td.UpdateCostAllocationTagsStatusResponseTypeDef",
    ) -> "dc_td.UpdateCostAllocationTagsStatusResponse":
        return dc_td.UpdateCostAllocationTagsStatusResponse.make_one(res)

    def update_cost_category_definition(
        self,
        res: "bs_td.UpdateCostCategoryDefinitionResponseTypeDef",
    ) -> "dc_td.UpdateCostCategoryDefinitionResponse":
        return dc_td.UpdateCostCategoryDefinitionResponse.make_one(res)


ce_caster = CECaster()
