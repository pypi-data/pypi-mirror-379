# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_devops_guru import type_defs as bs_td


class DEVOPS_GURUCaster:

    def add_notification_channel(
        self,
        res: "bs_td.AddNotificationChannelResponseTypeDef",
    ) -> "dc_td.AddNotificationChannelResponse":
        return dc_td.AddNotificationChannelResponse.make_one(res)

    def describe_account_health(
        self,
        res: "bs_td.DescribeAccountHealthResponseTypeDef",
    ) -> "dc_td.DescribeAccountHealthResponse":
        return dc_td.DescribeAccountHealthResponse.make_one(res)

    def describe_account_overview(
        self,
        res: "bs_td.DescribeAccountOverviewResponseTypeDef",
    ) -> "dc_td.DescribeAccountOverviewResponse":
        return dc_td.DescribeAccountOverviewResponse.make_one(res)

    def describe_anomaly(
        self,
        res: "bs_td.DescribeAnomalyResponseTypeDef",
    ) -> "dc_td.DescribeAnomalyResponse":
        return dc_td.DescribeAnomalyResponse.make_one(res)

    def describe_event_sources_config(
        self,
        res: "bs_td.DescribeEventSourcesConfigResponseTypeDef",
    ) -> "dc_td.DescribeEventSourcesConfigResponse":
        return dc_td.DescribeEventSourcesConfigResponse.make_one(res)

    def describe_feedback(
        self,
        res: "bs_td.DescribeFeedbackResponseTypeDef",
    ) -> "dc_td.DescribeFeedbackResponse":
        return dc_td.DescribeFeedbackResponse.make_one(res)

    def describe_insight(
        self,
        res: "bs_td.DescribeInsightResponseTypeDef",
    ) -> "dc_td.DescribeInsightResponse":
        return dc_td.DescribeInsightResponse.make_one(res)

    def describe_organization_health(
        self,
        res: "bs_td.DescribeOrganizationHealthResponseTypeDef",
    ) -> "dc_td.DescribeOrganizationHealthResponse":
        return dc_td.DescribeOrganizationHealthResponse.make_one(res)

    def describe_organization_overview(
        self,
        res: "bs_td.DescribeOrganizationOverviewResponseTypeDef",
    ) -> "dc_td.DescribeOrganizationOverviewResponse":
        return dc_td.DescribeOrganizationOverviewResponse.make_one(res)

    def describe_organization_resource_collection_health(
        self,
        res: "bs_td.DescribeOrganizationResourceCollectionHealthResponseTypeDef",
    ) -> "dc_td.DescribeOrganizationResourceCollectionHealthResponse":
        return dc_td.DescribeOrganizationResourceCollectionHealthResponse.make_one(res)

    def describe_resource_collection_health(
        self,
        res: "bs_td.DescribeResourceCollectionHealthResponseTypeDef",
    ) -> "dc_td.DescribeResourceCollectionHealthResponse":
        return dc_td.DescribeResourceCollectionHealthResponse.make_one(res)

    def describe_service_integration(
        self,
        res: "bs_td.DescribeServiceIntegrationResponseTypeDef",
    ) -> "dc_td.DescribeServiceIntegrationResponse":
        return dc_td.DescribeServiceIntegrationResponse.make_one(res)

    def get_cost_estimation(
        self,
        res: "bs_td.GetCostEstimationResponseTypeDef",
    ) -> "dc_td.GetCostEstimationResponse":
        return dc_td.GetCostEstimationResponse.make_one(res)

    def get_resource_collection(
        self,
        res: "bs_td.GetResourceCollectionResponseTypeDef",
    ) -> "dc_td.GetResourceCollectionResponse":
        return dc_td.GetResourceCollectionResponse.make_one(res)

    def list_anomalies_for_insight(
        self,
        res: "bs_td.ListAnomaliesForInsightResponseTypeDef",
    ) -> "dc_td.ListAnomaliesForInsightResponse":
        return dc_td.ListAnomaliesForInsightResponse.make_one(res)

    def list_anomalous_log_groups(
        self,
        res: "bs_td.ListAnomalousLogGroupsResponseTypeDef",
    ) -> "dc_td.ListAnomalousLogGroupsResponse":
        return dc_td.ListAnomalousLogGroupsResponse.make_one(res)

    def list_events(
        self,
        res: "bs_td.ListEventsResponseTypeDef",
    ) -> "dc_td.ListEventsResponse":
        return dc_td.ListEventsResponse.make_one(res)

    def list_insights(
        self,
        res: "bs_td.ListInsightsResponseTypeDef",
    ) -> "dc_td.ListInsightsResponse":
        return dc_td.ListInsightsResponse.make_one(res)

    def list_monitored_resources(
        self,
        res: "bs_td.ListMonitoredResourcesResponseTypeDef",
    ) -> "dc_td.ListMonitoredResourcesResponse":
        return dc_td.ListMonitoredResourcesResponse.make_one(res)

    def list_notification_channels(
        self,
        res: "bs_td.ListNotificationChannelsResponseTypeDef",
    ) -> "dc_td.ListNotificationChannelsResponse":
        return dc_td.ListNotificationChannelsResponse.make_one(res)

    def list_organization_insights(
        self,
        res: "bs_td.ListOrganizationInsightsResponseTypeDef",
    ) -> "dc_td.ListOrganizationInsightsResponse":
        return dc_td.ListOrganizationInsightsResponse.make_one(res)

    def list_recommendations(
        self,
        res: "bs_td.ListRecommendationsResponseTypeDef",
    ) -> "dc_td.ListRecommendationsResponse":
        return dc_td.ListRecommendationsResponse.make_one(res)

    def search_insights(
        self,
        res: "bs_td.SearchInsightsResponseTypeDef",
    ) -> "dc_td.SearchInsightsResponse":
        return dc_td.SearchInsightsResponse.make_one(res)

    def search_organization_insights(
        self,
        res: "bs_td.SearchOrganizationInsightsResponseTypeDef",
    ) -> "dc_td.SearchOrganizationInsightsResponse":
        return dc_td.SearchOrganizationInsightsResponse.make_one(res)


devops_guru_caster = DEVOPS_GURUCaster()
