# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_cloudtrail import type_defs as bs_td


class CLOUDTRAILCaster:

    def cancel_query(
        self,
        res: "bs_td.CancelQueryResponseTypeDef",
    ) -> "dc_td.CancelQueryResponse":
        return dc_td.CancelQueryResponse.make_one(res)

    def create_channel(
        self,
        res: "bs_td.CreateChannelResponseTypeDef",
    ) -> "dc_td.CreateChannelResponse":
        return dc_td.CreateChannelResponse.make_one(res)

    def create_dashboard(
        self,
        res: "bs_td.CreateDashboardResponseTypeDef",
    ) -> "dc_td.CreateDashboardResponse":
        return dc_td.CreateDashboardResponse.make_one(res)

    def create_event_data_store(
        self,
        res: "bs_td.CreateEventDataStoreResponseTypeDef",
    ) -> "dc_td.CreateEventDataStoreResponse":
        return dc_td.CreateEventDataStoreResponse.make_one(res)

    def create_trail(
        self,
        res: "bs_td.CreateTrailResponseTypeDef",
    ) -> "dc_td.CreateTrailResponse":
        return dc_td.CreateTrailResponse.make_one(res)

    def describe_query(
        self,
        res: "bs_td.DescribeQueryResponseTypeDef",
    ) -> "dc_td.DescribeQueryResponse":
        return dc_td.DescribeQueryResponse.make_one(res)

    def describe_trails(
        self,
        res: "bs_td.DescribeTrailsResponseTypeDef",
    ) -> "dc_td.DescribeTrailsResponse":
        return dc_td.DescribeTrailsResponse.make_one(res)

    def disable_federation(
        self,
        res: "bs_td.DisableFederationResponseTypeDef",
    ) -> "dc_td.DisableFederationResponse":
        return dc_td.DisableFederationResponse.make_one(res)

    def enable_federation(
        self,
        res: "bs_td.EnableFederationResponseTypeDef",
    ) -> "dc_td.EnableFederationResponse":
        return dc_td.EnableFederationResponse.make_one(res)

    def generate_query(
        self,
        res: "bs_td.GenerateQueryResponseTypeDef",
    ) -> "dc_td.GenerateQueryResponse":
        return dc_td.GenerateQueryResponse.make_one(res)

    def get_channel(
        self,
        res: "bs_td.GetChannelResponseTypeDef",
    ) -> "dc_td.GetChannelResponse":
        return dc_td.GetChannelResponse.make_one(res)

    def get_dashboard(
        self,
        res: "bs_td.GetDashboardResponseTypeDef",
    ) -> "dc_td.GetDashboardResponse":
        return dc_td.GetDashboardResponse.make_one(res)

    def get_event_configuration(
        self,
        res: "bs_td.GetEventConfigurationResponseTypeDef",
    ) -> "dc_td.GetEventConfigurationResponse":
        return dc_td.GetEventConfigurationResponse.make_one(res)

    def get_event_data_store(
        self,
        res: "bs_td.GetEventDataStoreResponseTypeDef",
    ) -> "dc_td.GetEventDataStoreResponse":
        return dc_td.GetEventDataStoreResponse.make_one(res)

    def get_event_selectors(
        self,
        res: "bs_td.GetEventSelectorsResponseTypeDef",
    ) -> "dc_td.GetEventSelectorsResponse":
        return dc_td.GetEventSelectorsResponse.make_one(res)

    def get_import(
        self,
        res: "bs_td.GetImportResponseTypeDef",
    ) -> "dc_td.GetImportResponse":
        return dc_td.GetImportResponse.make_one(res)

    def get_insight_selectors(
        self,
        res: "bs_td.GetInsightSelectorsResponseTypeDef",
    ) -> "dc_td.GetInsightSelectorsResponse":
        return dc_td.GetInsightSelectorsResponse.make_one(res)

    def get_query_results(
        self,
        res: "bs_td.GetQueryResultsResponseTypeDef",
    ) -> "dc_td.GetQueryResultsResponse":
        return dc_td.GetQueryResultsResponse.make_one(res)

    def get_resource_policy(
        self,
        res: "bs_td.GetResourcePolicyResponseTypeDef",
    ) -> "dc_td.GetResourcePolicyResponse":
        return dc_td.GetResourcePolicyResponse.make_one(res)

    def get_trail(
        self,
        res: "bs_td.GetTrailResponseTypeDef",
    ) -> "dc_td.GetTrailResponse":
        return dc_td.GetTrailResponse.make_one(res)

    def get_trail_status(
        self,
        res: "bs_td.GetTrailStatusResponseTypeDef",
    ) -> "dc_td.GetTrailStatusResponse":
        return dc_td.GetTrailStatusResponse.make_one(res)

    def list_channels(
        self,
        res: "bs_td.ListChannelsResponseTypeDef",
    ) -> "dc_td.ListChannelsResponse":
        return dc_td.ListChannelsResponse.make_one(res)

    def list_dashboards(
        self,
        res: "bs_td.ListDashboardsResponseTypeDef",
    ) -> "dc_td.ListDashboardsResponse":
        return dc_td.ListDashboardsResponse.make_one(res)

    def list_event_data_stores(
        self,
        res: "bs_td.ListEventDataStoresResponseTypeDef",
    ) -> "dc_td.ListEventDataStoresResponse":
        return dc_td.ListEventDataStoresResponse.make_one(res)

    def list_import_failures(
        self,
        res: "bs_td.ListImportFailuresResponseTypeDef",
    ) -> "dc_td.ListImportFailuresResponse":
        return dc_td.ListImportFailuresResponse.make_one(res)

    def list_imports(
        self,
        res: "bs_td.ListImportsResponseTypeDef",
    ) -> "dc_td.ListImportsResponse":
        return dc_td.ListImportsResponse.make_one(res)

    def list_insights_metric_data(
        self,
        res: "bs_td.ListInsightsMetricDataResponseTypeDef",
    ) -> "dc_td.ListInsightsMetricDataResponse":
        return dc_td.ListInsightsMetricDataResponse.make_one(res)

    def list_public_keys(
        self,
        res: "bs_td.ListPublicKeysResponseTypeDef",
    ) -> "dc_td.ListPublicKeysResponse":
        return dc_td.ListPublicKeysResponse.make_one(res)

    def list_queries(
        self,
        res: "bs_td.ListQueriesResponseTypeDef",
    ) -> "dc_td.ListQueriesResponse":
        return dc_td.ListQueriesResponse.make_one(res)

    def list_tags(
        self,
        res: "bs_td.ListTagsResponseTypeDef",
    ) -> "dc_td.ListTagsResponse":
        return dc_td.ListTagsResponse.make_one(res)

    def list_trails(
        self,
        res: "bs_td.ListTrailsResponseTypeDef",
    ) -> "dc_td.ListTrailsResponse":
        return dc_td.ListTrailsResponse.make_one(res)

    def lookup_events(
        self,
        res: "bs_td.LookupEventsResponseTypeDef",
    ) -> "dc_td.LookupEventsResponse":
        return dc_td.LookupEventsResponse.make_one(res)

    def put_event_configuration(
        self,
        res: "bs_td.PutEventConfigurationResponseTypeDef",
    ) -> "dc_td.PutEventConfigurationResponse":
        return dc_td.PutEventConfigurationResponse.make_one(res)

    def put_event_selectors(
        self,
        res: "bs_td.PutEventSelectorsResponseTypeDef",
    ) -> "dc_td.PutEventSelectorsResponse":
        return dc_td.PutEventSelectorsResponse.make_one(res)

    def put_insight_selectors(
        self,
        res: "bs_td.PutInsightSelectorsResponseTypeDef",
    ) -> "dc_td.PutInsightSelectorsResponse":
        return dc_td.PutInsightSelectorsResponse.make_one(res)

    def put_resource_policy(
        self,
        res: "bs_td.PutResourcePolicyResponseTypeDef",
    ) -> "dc_td.PutResourcePolicyResponse":
        return dc_td.PutResourcePolicyResponse.make_one(res)

    def restore_event_data_store(
        self,
        res: "bs_td.RestoreEventDataStoreResponseTypeDef",
    ) -> "dc_td.RestoreEventDataStoreResponse":
        return dc_td.RestoreEventDataStoreResponse.make_one(res)

    def search_sample_queries(
        self,
        res: "bs_td.SearchSampleQueriesResponseTypeDef",
    ) -> "dc_td.SearchSampleQueriesResponse":
        return dc_td.SearchSampleQueriesResponse.make_one(res)

    def start_dashboard_refresh(
        self,
        res: "bs_td.StartDashboardRefreshResponseTypeDef",
    ) -> "dc_td.StartDashboardRefreshResponse":
        return dc_td.StartDashboardRefreshResponse.make_one(res)

    def start_import(
        self,
        res: "bs_td.StartImportResponseTypeDef",
    ) -> "dc_td.StartImportResponse":
        return dc_td.StartImportResponse.make_one(res)

    def start_query(
        self,
        res: "bs_td.StartQueryResponseTypeDef",
    ) -> "dc_td.StartQueryResponse":
        return dc_td.StartQueryResponse.make_one(res)

    def stop_import(
        self,
        res: "bs_td.StopImportResponseTypeDef",
    ) -> "dc_td.StopImportResponse":
        return dc_td.StopImportResponse.make_one(res)

    def update_channel(
        self,
        res: "bs_td.UpdateChannelResponseTypeDef",
    ) -> "dc_td.UpdateChannelResponse":
        return dc_td.UpdateChannelResponse.make_one(res)

    def update_dashboard(
        self,
        res: "bs_td.UpdateDashboardResponseTypeDef",
    ) -> "dc_td.UpdateDashboardResponse":
        return dc_td.UpdateDashboardResponse.make_one(res)

    def update_event_data_store(
        self,
        res: "bs_td.UpdateEventDataStoreResponseTypeDef",
    ) -> "dc_td.UpdateEventDataStoreResponse":
        return dc_td.UpdateEventDataStoreResponse.make_one(res)

    def update_trail(
        self,
        res: "bs_td.UpdateTrailResponseTypeDef",
    ) -> "dc_td.UpdateTrailResponse":
        return dc_td.UpdateTrailResponse.make_one(res)


cloudtrail_caster = CLOUDTRAILCaster()
