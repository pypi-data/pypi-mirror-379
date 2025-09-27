# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_codeguruprofiler import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


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
class AgentConfiguration:
    boto3_raw_data: "type_defs.AgentConfigurationTypeDef" = dataclasses.field()

    periodInSeconds = field("periodInSeconds")
    shouldProfile = field("shouldProfile")
    agentParameters = field("agentParameters")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AgentConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AgentConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AgentOrchestrationConfig:
    boto3_raw_data: "type_defs.AgentOrchestrationConfigTypeDef" = dataclasses.field()

    profilingEnabled = field("profilingEnabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AgentOrchestrationConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AgentOrchestrationConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AggregatedProfileTime:
    boto3_raw_data: "type_defs.AggregatedProfileTimeTypeDef" = dataclasses.field()

    period = field("period")
    start = field("start")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AggregatedProfileTimeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AggregatedProfileTimeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserFeedback:
    boto3_raw_data: "type_defs.UserFeedbackTypeDef" = dataclasses.field()

    type = field("type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UserFeedbackTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UserFeedbackTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Metric:
    boto3_raw_data: "type_defs.MetricTypeDef" = dataclasses.field()

    frameName = field("frameName")
    threadStates = field("threadStates")
    type = field("type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MetricTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MetricTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TimestampStructure:
    boto3_raw_data: "type_defs.TimestampStructureTypeDef" = dataclasses.field()

    value = field("value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TimestampStructureTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TimestampStructureTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChannelOutput:
    boto3_raw_data: "type_defs.ChannelOutputTypeDef" = dataclasses.field()

    eventPublishers = field("eventPublishers")
    uri = field("uri")
    id = field("id")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ChannelOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ChannelOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Channel:
    boto3_raw_data: "type_defs.ChannelTypeDef" = dataclasses.field()

    eventPublishers = field("eventPublishers")
    uri = field("uri")
    id = field("id")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ChannelTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ChannelTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfigureAgentRequest:
    boto3_raw_data: "type_defs.ConfigureAgentRequestTypeDef" = dataclasses.field()

    profilingGroupName = field("profilingGroupName")
    fleetInstanceId = field("fleetInstanceId")
    metadata = field("metadata")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConfigureAgentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfigureAgentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteProfilingGroupRequest:
    boto3_raw_data: "type_defs.DeleteProfilingGroupRequestTypeDef" = dataclasses.field()

    profilingGroupName = field("profilingGroupName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteProfilingGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteProfilingGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeProfilingGroupRequest:
    boto3_raw_data: "type_defs.DescribeProfilingGroupRequestTypeDef" = (
        dataclasses.field()
    )

    profilingGroupName = field("profilingGroupName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeProfilingGroupRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeProfilingGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FindingsReportSummary:
    boto3_raw_data: "type_defs.FindingsReportSummaryTypeDef" = dataclasses.field()

    id = field("id")
    profileEndTime = field("profileEndTime")
    profileStartTime = field("profileStartTime")
    profilingGroupName = field("profilingGroupName")
    totalNumberOfFindings = field("totalNumberOfFindings")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FindingsReportSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FindingsReportSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FrameMetricOutput:
    boto3_raw_data: "type_defs.FrameMetricOutputTypeDef" = dataclasses.field()

    frameName = field("frameName")
    threadStates = field("threadStates")
    type = field("type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FrameMetricOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FrameMetricOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FrameMetric:
    boto3_raw_data: "type_defs.FrameMetricTypeDef" = dataclasses.field()

    frameName = field("frameName")
    threadStates = field("threadStates")
    type = field("type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FrameMetricTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FrameMetricTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFindingsReportAccountSummaryRequest:
    boto3_raw_data: "type_defs.GetFindingsReportAccountSummaryRequestTypeDef" = (
        dataclasses.field()
    )

    dailyReportsOnly = field("dailyReportsOnly")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetFindingsReportAccountSummaryRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFindingsReportAccountSummaryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetNotificationConfigurationRequest:
    boto3_raw_data: "type_defs.GetNotificationConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    profilingGroupName = field("profilingGroupName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetNotificationConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetNotificationConfigurationRequestTypeDef"]
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

    profilingGroupName = field("profilingGroupName")

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
class ProfileTime:
    boto3_raw_data: "type_defs.ProfileTimeTypeDef" = dataclasses.field()

    start = field("start")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ProfileTimeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ProfileTimeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProfilingGroupsRequest:
    boto3_raw_data: "type_defs.ListProfilingGroupsRequestTypeDef" = dataclasses.field()

    includeDescription = field("includeDescription")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListProfilingGroupsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProfilingGroupsRequestTypeDef"]
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

    resourceArn = field("resourceArn")

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
class Match:
    boto3_raw_data: "type_defs.MatchTypeDef" = dataclasses.field()

    frameAddress = field("frameAddress")
    targetFramesIndex = field("targetFramesIndex")
    thresholdBreachValue = field("thresholdBreachValue")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MatchTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MatchTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Pattern:
    boto3_raw_data: "type_defs.PatternTypeDef" = dataclasses.field()

    countersToAggregate = field("countersToAggregate")
    description = field("description")
    id = field("id")
    name = field("name")
    resolutionSteps = field("resolutionSteps")
    targetFrames = field("targetFrames")
    thresholdPercent = field("thresholdPercent")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PatternTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PatternTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutPermissionRequest:
    boto3_raw_data: "type_defs.PutPermissionRequestTypeDef" = dataclasses.field()

    actionGroup = field("actionGroup")
    principals = field("principals")
    profilingGroupName = field("profilingGroupName")
    revisionId = field("revisionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutPermissionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutPermissionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveNotificationChannelRequest:
    boto3_raw_data: "type_defs.RemoveNotificationChannelRequestTypeDef" = (
        dataclasses.field()
    )

    channelId = field("channelId")
    profilingGroupName = field("profilingGroupName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RemoveNotificationChannelRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveNotificationChannelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemovePermissionRequest:
    boto3_raw_data: "type_defs.RemovePermissionRequestTypeDef" = dataclasses.field()

    actionGroup = field("actionGroup")
    profilingGroupName = field("profilingGroupName")
    revisionId = field("revisionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RemovePermissionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemovePermissionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SubmitFeedbackRequest:
    boto3_raw_data: "type_defs.SubmitFeedbackRequestTypeDef" = dataclasses.field()

    anomalyInstanceId = field("anomalyInstanceId")
    profilingGroupName = field("profilingGroupName")
    type = field("type")
    comment = field("comment")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SubmitFeedbackRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SubmitFeedbackRequestTypeDef"]
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

    resourceArn = field("resourceArn")
    tags = field("tags")

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

    resourceArn = field("resourceArn")
    tagKeys = field("tagKeys")

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
class GetPolicyResponse:
    boto3_raw_data: "type_defs.GetPolicyResponseTypeDef" = dataclasses.field()

    policy = field("policy")
    revisionId = field("revisionId")

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
class GetProfileResponse:
    boto3_raw_data: "type_defs.GetProfileResponseTypeDef" = dataclasses.field()

    contentEncoding = field("contentEncoding")
    contentType = field("contentType")
    profile = field("profile")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetProfileResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetProfileResponseTypeDef"]
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

    tags = field("tags")

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
class PutPermissionResponse:
    boto3_raw_data: "type_defs.PutPermissionResponseTypeDef" = dataclasses.field()

    policy = field("policy")
    revisionId = field("revisionId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutPermissionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutPermissionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemovePermissionResponse:
    boto3_raw_data: "type_defs.RemovePermissionResponseTypeDef" = dataclasses.field()

    policy = field("policy")
    revisionId = field("revisionId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RemovePermissionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemovePermissionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfigureAgentResponse:
    boto3_raw_data: "type_defs.ConfigureAgentResponseTypeDef" = dataclasses.field()

    @cached_property
    def configuration(self):  # pragma: no cover
        return AgentConfiguration.make_one(self.boto3_raw_data["configuration"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConfigureAgentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfigureAgentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateProfilingGroupRequest:
    boto3_raw_data: "type_defs.CreateProfilingGroupRequestTypeDef" = dataclasses.field()

    clientToken = field("clientToken")
    profilingGroupName = field("profilingGroupName")

    @cached_property
    def agentOrchestrationConfig(self):  # pragma: no cover
        return AgentOrchestrationConfig.make_one(
            self.boto3_raw_data["agentOrchestrationConfig"]
        )

    computePlatform = field("computePlatform")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateProfilingGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateProfilingGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateProfilingGroupRequest:
    boto3_raw_data: "type_defs.UpdateProfilingGroupRequestTypeDef" = dataclasses.field()

    @cached_property
    def agentOrchestrationConfig(self):  # pragma: no cover
        return AgentOrchestrationConfig.make_one(
            self.boto3_raw_data["agentOrchestrationConfig"]
        )

    profilingGroupName = field("profilingGroupName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateProfilingGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateProfilingGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProfilingStatus:
    boto3_raw_data: "type_defs.ProfilingStatusTypeDef" = dataclasses.field()

    latestAgentOrchestratedAt = field("latestAgentOrchestratedAt")
    latestAgentProfileReportedAt = field("latestAgentProfileReportedAt")

    @cached_property
    def latestAggregatedProfile(self):  # pragma: no cover
        return AggregatedProfileTime.make_one(
            self.boto3_raw_data["latestAggregatedProfile"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ProfilingStatusTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ProfilingStatusTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnomalyInstance:
    boto3_raw_data: "type_defs.AnomalyInstanceTypeDef" = dataclasses.field()

    id = field("id")
    startTime = field("startTime")
    endTime = field("endTime")

    @cached_property
    def userFeedback(self):  # pragma: no cover
        return UserFeedback.make_one(self.boto3_raw_data["userFeedback"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AnomalyInstanceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AnomalyInstanceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetProfileRequest:
    boto3_raw_data: "type_defs.GetProfileRequestTypeDef" = dataclasses.field()

    profilingGroupName = field("profilingGroupName")
    accept = field("accept")
    endTime = field("endTime")
    maxDepth = field("maxDepth")
    period = field("period")
    startTime = field("startTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetProfileRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRecommendationsRequest:
    boto3_raw_data: "type_defs.GetRecommendationsRequestTypeDef" = dataclasses.field()

    endTime = field("endTime")
    profilingGroupName = field("profilingGroupName")
    startTime = field("startTime")
    locale = field("locale")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetRecommendationsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRecommendationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFindingsReportsRequest:
    boto3_raw_data: "type_defs.ListFindingsReportsRequestTypeDef" = dataclasses.field()

    endTime = field("endTime")
    profilingGroupName = field("profilingGroupName")
    startTime = field("startTime")
    dailyReportsOnly = field("dailyReportsOnly")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFindingsReportsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFindingsReportsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProfileTimesRequest:
    boto3_raw_data: "type_defs.ListProfileTimesRequestTypeDef" = dataclasses.field()

    endTime = field("endTime")
    period = field("period")
    profilingGroupName = field("profilingGroupName")
    startTime = field("startTime")
    maxResults = field("maxResults")
    nextToken = field("nextToken")
    orderBy = field("orderBy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListProfileTimesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProfileTimesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PostAgentProfileRequest:
    boto3_raw_data: "type_defs.PostAgentProfileRequestTypeDef" = dataclasses.field()

    agentProfile = field("agentProfile")
    contentType = field("contentType")
    profilingGroupName = field("profilingGroupName")
    profileToken = field("profileToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PostAgentProfileRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PostAgentProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NotificationConfiguration:
    boto3_raw_data: "type_defs.NotificationConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def channels(self):  # pragma: no cover
        return ChannelOutput.make_many(self.boto3_raw_data["channels"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NotificationConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NotificationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFindingsReportAccountSummaryResponse:
    boto3_raw_data: "type_defs.GetFindingsReportAccountSummaryResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def reportSummaries(self):  # pragma: no cover
        return FindingsReportSummary.make_many(self.boto3_raw_data["reportSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetFindingsReportAccountSummaryResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFindingsReportAccountSummaryResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFindingsReportsResponse:
    boto3_raw_data: "type_defs.ListFindingsReportsResponseTypeDef" = dataclasses.field()

    @cached_property
    def findingsReportSummaries(self):  # pragma: no cover
        return FindingsReportSummary.make_many(
            self.boto3_raw_data["findingsReportSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFindingsReportsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFindingsReportsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FrameMetricDatum:
    boto3_raw_data: "type_defs.FrameMetricDatumTypeDef" = dataclasses.field()

    @cached_property
    def frameMetric(self):  # pragma: no cover
        return FrameMetricOutput.make_one(self.boto3_raw_data["frameMetric"])

    values = field("values")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FrameMetricDatumTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FrameMetricDatumTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProfileTimesRequestPaginate:
    boto3_raw_data: "type_defs.ListProfileTimesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    endTime = field("endTime")
    period = field("period")
    profilingGroupName = field("profilingGroupName")
    startTime = field("startTime")
    orderBy = field("orderBy")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListProfileTimesRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProfileTimesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProfileTimesResponse:
    boto3_raw_data: "type_defs.ListProfileTimesResponseTypeDef" = dataclasses.field()

    @cached_property
    def profileTimes(self):  # pragma: no cover
        return ProfileTime.make_many(self.boto3_raw_data["profileTimes"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListProfileTimesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProfileTimesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Recommendation:
    boto3_raw_data: "type_defs.RecommendationTypeDef" = dataclasses.field()

    allMatchesCount = field("allMatchesCount")
    allMatchesSum = field("allMatchesSum")
    endTime = field("endTime")

    @cached_property
    def pattern(self):  # pragma: no cover
        return Pattern.make_one(self.boto3_raw_data["pattern"])

    startTime = field("startTime")

    @cached_property
    def topMatches(self):  # pragma: no cover
        return Match.make_many(self.boto3_raw_data["topMatches"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RecommendationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RecommendationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProfilingGroupDescription:
    boto3_raw_data: "type_defs.ProfilingGroupDescriptionTypeDef" = dataclasses.field()

    @cached_property
    def agentOrchestrationConfig(self):  # pragma: no cover
        return AgentOrchestrationConfig.make_one(
            self.boto3_raw_data["agentOrchestrationConfig"]
        )

    arn = field("arn")
    computePlatform = field("computePlatform")
    createdAt = field("createdAt")
    name = field("name")

    @cached_property
    def profilingStatus(self):  # pragma: no cover
        return ProfilingStatus.make_one(self.boto3_raw_data["profilingStatus"])

    tags = field("tags")
    updatedAt = field("updatedAt")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProfilingGroupDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProfilingGroupDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Anomaly:
    boto3_raw_data: "type_defs.AnomalyTypeDef" = dataclasses.field()

    @cached_property
    def instances(self):  # pragma: no cover
        return AnomalyInstance.make_many(self.boto3_raw_data["instances"])

    @cached_property
    def metric(self):  # pragma: no cover
        return Metric.make_one(self.boto3_raw_data["metric"])

    reason = field("reason")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AnomalyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AnomalyTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddNotificationChannelsResponse:
    boto3_raw_data: "type_defs.AddNotificationChannelsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def notificationConfiguration(self):  # pragma: no cover
        return NotificationConfiguration.make_one(
            self.boto3_raw_data["notificationConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AddNotificationChannelsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddNotificationChannelsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetNotificationConfigurationResponse:
    boto3_raw_data: "type_defs.GetNotificationConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def notificationConfiguration(self):  # pragma: no cover
        return NotificationConfiguration.make_one(
            self.boto3_raw_data["notificationConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetNotificationConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetNotificationConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveNotificationChannelResponse:
    boto3_raw_data: "type_defs.RemoveNotificationChannelResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def notificationConfiguration(self):  # pragma: no cover
        return NotificationConfiguration.make_one(
            self.boto3_raw_data["notificationConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RemoveNotificationChannelResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveNotificationChannelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddNotificationChannelsRequest:
    boto3_raw_data: "type_defs.AddNotificationChannelsRequestTypeDef" = (
        dataclasses.field()
    )

    channels = field("channels")
    profilingGroupName = field("profilingGroupName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AddNotificationChannelsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddNotificationChannelsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetFrameMetricDataResponse:
    boto3_raw_data: "type_defs.BatchGetFrameMetricDataResponseTypeDef" = (
        dataclasses.field()
    )

    endTime = field("endTime")

    @cached_property
    def endTimes(self):  # pragma: no cover
        return TimestampStructure.make_many(self.boto3_raw_data["endTimes"])

    @cached_property
    def frameMetricData(self):  # pragma: no cover
        return FrameMetricDatum.make_many(self.boto3_raw_data["frameMetricData"])

    resolution = field("resolution")
    startTime = field("startTime")
    unprocessedEndTimes = field("unprocessedEndTimes")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchGetFrameMetricDataResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetFrameMetricDataResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetFrameMetricDataRequest:
    boto3_raw_data: "type_defs.BatchGetFrameMetricDataRequestTypeDef" = (
        dataclasses.field()
    )

    profilingGroupName = field("profilingGroupName")
    endTime = field("endTime")
    frameMetrics = field("frameMetrics")
    period = field("period")
    startTime = field("startTime")
    targetResolution = field("targetResolution")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchGetFrameMetricDataRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetFrameMetricDataRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateProfilingGroupResponse:
    boto3_raw_data: "type_defs.CreateProfilingGroupResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def profilingGroup(self):  # pragma: no cover
        return ProfilingGroupDescription.make_one(self.boto3_raw_data["profilingGroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateProfilingGroupResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateProfilingGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeProfilingGroupResponse:
    boto3_raw_data: "type_defs.DescribeProfilingGroupResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def profilingGroup(self):  # pragma: no cover
        return ProfilingGroupDescription.make_one(self.boto3_raw_data["profilingGroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeProfilingGroupResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeProfilingGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProfilingGroupsResponse:
    boto3_raw_data: "type_defs.ListProfilingGroupsResponseTypeDef" = dataclasses.field()

    profilingGroupNames = field("profilingGroupNames")

    @cached_property
    def profilingGroups(self):  # pragma: no cover
        return ProfilingGroupDescription.make_many(
            self.boto3_raw_data["profilingGroups"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListProfilingGroupsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProfilingGroupsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateProfilingGroupResponse:
    boto3_raw_data: "type_defs.UpdateProfilingGroupResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def profilingGroup(self):  # pragma: no cover
        return ProfilingGroupDescription.make_one(self.boto3_raw_data["profilingGroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateProfilingGroupResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateProfilingGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRecommendationsResponse:
    boto3_raw_data: "type_defs.GetRecommendationsResponseTypeDef" = dataclasses.field()

    @cached_property
    def anomalies(self):  # pragma: no cover
        return Anomaly.make_many(self.boto3_raw_data["anomalies"])

    profileEndTime = field("profileEndTime")
    profileStartTime = field("profileStartTime")
    profilingGroupName = field("profilingGroupName")

    @cached_property
    def recommendations(self):  # pragma: no cover
        return Recommendation.make_many(self.boto3_raw_data["recommendations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetRecommendationsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRecommendationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
