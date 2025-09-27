# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_codeguruprofiler import type_defs as bs_td


class CODEGURUPROFILERCaster:

    def add_notification_channels(
        self,
        res: "bs_td.AddNotificationChannelsResponseTypeDef",
    ) -> "dc_td.AddNotificationChannelsResponse":
        return dc_td.AddNotificationChannelsResponse.make_one(res)

    def batch_get_frame_metric_data(
        self,
        res: "bs_td.BatchGetFrameMetricDataResponseTypeDef",
    ) -> "dc_td.BatchGetFrameMetricDataResponse":
        return dc_td.BatchGetFrameMetricDataResponse.make_one(res)

    def configure_agent(
        self,
        res: "bs_td.ConfigureAgentResponseTypeDef",
    ) -> "dc_td.ConfigureAgentResponse":
        return dc_td.ConfigureAgentResponse.make_one(res)

    def create_profiling_group(
        self,
        res: "bs_td.CreateProfilingGroupResponseTypeDef",
    ) -> "dc_td.CreateProfilingGroupResponse":
        return dc_td.CreateProfilingGroupResponse.make_one(res)

    def describe_profiling_group(
        self,
        res: "bs_td.DescribeProfilingGroupResponseTypeDef",
    ) -> "dc_td.DescribeProfilingGroupResponse":
        return dc_td.DescribeProfilingGroupResponse.make_one(res)

    def get_findings_report_account_summary(
        self,
        res: "bs_td.GetFindingsReportAccountSummaryResponseTypeDef",
    ) -> "dc_td.GetFindingsReportAccountSummaryResponse":
        return dc_td.GetFindingsReportAccountSummaryResponse.make_one(res)

    def get_notification_configuration(
        self,
        res: "bs_td.GetNotificationConfigurationResponseTypeDef",
    ) -> "dc_td.GetNotificationConfigurationResponse":
        return dc_td.GetNotificationConfigurationResponse.make_one(res)

    def get_policy(
        self,
        res: "bs_td.GetPolicyResponseTypeDef",
    ) -> "dc_td.GetPolicyResponse":
        return dc_td.GetPolicyResponse.make_one(res)

    def get_profile(
        self,
        res: "bs_td.GetProfileResponseTypeDef",
    ) -> "dc_td.GetProfileResponse":
        return dc_td.GetProfileResponse.make_one(res)

    def get_recommendations(
        self,
        res: "bs_td.GetRecommendationsResponseTypeDef",
    ) -> "dc_td.GetRecommendationsResponse":
        return dc_td.GetRecommendationsResponse.make_one(res)

    def list_findings_reports(
        self,
        res: "bs_td.ListFindingsReportsResponseTypeDef",
    ) -> "dc_td.ListFindingsReportsResponse":
        return dc_td.ListFindingsReportsResponse.make_one(res)

    def list_profile_times(
        self,
        res: "bs_td.ListProfileTimesResponseTypeDef",
    ) -> "dc_td.ListProfileTimesResponse":
        return dc_td.ListProfileTimesResponse.make_one(res)

    def list_profiling_groups(
        self,
        res: "bs_td.ListProfilingGroupsResponseTypeDef",
    ) -> "dc_td.ListProfilingGroupsResponse":
        return dc_td.ListProfilingGroupsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def put_permission(
        self,
        res: "bs_td.PutPermissionResponseTypeDef",
    ) -> "dc_td.PutPermissionResponse":
        return dc_td.PutPermissionResponse.make_one(res)

    def remove_notification_channel(
        self,
        res: "bs_td.RemoveNotificationChannelResponseTypeDef",
    ) -> "dc_td.RemoveNotificationChannelResponse":
        return dc_td.RemoveNotificationChannelResponse.make_one(res)

    def remove_permission(
        self,
        res: "bs_td.RemovePermissionResponseTypeDef",
    ) -> "dc_td.RemovePermissionResponse":
        return dc_td.RemovePermissionResponse.make_one(res)

    def update_profiling_group(
        self,
        res: "bs_td.UpdateProfilingGroupResponseTypeDef",
    ) -> "dc_td.UpdateProfilingGroupResponse":
        return dc_td.UpdateProfilingGroupResponse.make_one(res)


codeguruprofiler_caster = CODEGURUPROFILERCaster()
