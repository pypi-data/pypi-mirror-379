# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_application_insights import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class WorkloadConfiguration:
    boto3_raw_data: "type_defs.WorkloadConfigurationTypeDef" = dataclasses.field()

    WorkloadName = field("WorkloadName")
    Tier = field("Tier")
    Configuration = field("Configuration")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WorkloadConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkloadConfigurationTypeDef"]
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
class ApplicationComponent:
    boto3_raw_data: "type_defs.ApplicationComponentTypeDef" = dataclasses.field()

    ComponentName = field("ComponentName")
    ComponentRemarks = field("ComponentRemarks")
    ResourceType = field("ResourceType")
    OsType = field("OsType")
    Tier = field("Tier")
    Monitor = field("Monitor")
    DetectedWorkload = field("DetectedWorkload")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ApplicationComponentTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplicationComponentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplicationInfo:
    boto3_raw_data: "type_defs.ApplicationInfoTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    ResourceGroupName = field("ResourceGroupName")
    LifeCycle = field("LifeCycle")
    OpsItemSNSTopicArn = field("OpsItemSNSTopicArn")
    SNSNotificationArn = field("SNSNotificationArn")
    OpsCenterEnabled = field("OpsCenterEnabled")
    CWEMonitorEnabled = field("CWEMonitorEnabled")
    Remarks = field("Remarks")
    AutoConfigEnabled = field("AutoConfigEnabled")
    DiscoveryType = field("DiscoveryType")
    AttachMissingPermission = field("AttachMissingPermission")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ApplicationInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ApplicationInfoTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfigurationEvent:
    boto3_raw_data: "type_defs.ConfigurationEventTypeDef" = dataclasses.field()

    ResourceGroupName = field("ResourceGroupName")
    AccountId = field("AccountId")
    MonitoredResourceARN = field("MonitoredResourceARN")
    EventStatus = field("EventStatus")
    EventResourceType = field("EventResourceType")
    EventTime = field("EventTime")
    EventDetail = field("EventDetail")
    EventResourceName = field("EventResourceName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConfigurationEventTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfigurationEventTypeDef"]
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
class CreateComponentRequest:
    boto3_raw_data: "type_defs.CreateComponentRequestTypeDef" = dataclasses.field()

    ResourceGroupName = field("ResourceGroupName")
    ComponentName = field("ComponentName")
    ResourceList = field("ResourceList")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateComponentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateComponentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLogPatternRequest:
    boto3_raw_data: "type_defs.CreateLogPatternRequestTypeDef" = dataclasses.field()

    ResourceGroupName = field("ResourceGroupName")
    PatternSetName = field("PatternSetName")
    PatternName = field("PatternName")
    Pattern = field("Pattern")
    Rank = field("Rank")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateLogPatternRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLogPatternRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LogPattern:
    boto3_raw_data: "type_defs.LogPatternTypeDef" = dataclasses.field()

    PatternSetName = field("PatternSetName")
    PatternName = field("PatternName")
    Pattern = field("Pattern")
    Rank = field("Rank")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LogPatternTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LogPatternTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteApplicationRequest:
    boto3_raw_data: "type_defs.DeleteApplicationRequestTypeDef" = dataclasses.field()

    ResourceGroupName = field("ResourceGroupName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteApplicationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteApplicationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteComponentRequest:
    boto3_raw_data: "type_defs.DeleteComponentRequestTypeDef" = dataclasses.field()

    ResourceGroupName = field("ResourceGroupName")
    ComponentName = field("ComponentName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteComponentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteComponentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteLogPatternRequest:
    boto3_raw_data: "type_defs.DeleteLogPatternRequestTypeDef" = dataclasses.field()

    ResourceGroupName = field("ResourceGroupName")
    PatternSetName = field("PatternSetName")
    PatternName = field("PatternName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteLogPatternRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteLogPatternRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeApplicationRequest:
    boto3_raw_data: "type_defs.DescribeApplicationRequestTypeDef" = dataclasses.field()

    ResourceGroupName = field("ResourceGroupName")
    AccountId = field("AccountId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeApplicationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeApplicationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeComponentConfigurationRecommendationRequest:
    boto3_raw_data: (
        "type_defs.DescribeComponentConfigurationRecommendationRequestTypeDef"
    ) = dataclasses.field()

    ResourceGroupName = field("ResourceGroupName")
    ComponentName = field("ComponentName")
    Tier = field("Tier")
    WorkloadName = field("WorkloadName")
    RecommendationType = field("RecommendationType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeComponentConfigurationRecommendationRequestTypeDef"
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
                "type_defs.DescribeComponentConfigurationRecommendationRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeComponentConfigurationRequest:
    boto3_raw_data: "type_defs.DescribeComponentConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    ResourceGroupName = field("ResourceGroupName")
    ComponentName = field("ComponentName")
    AccountId = field("AccountId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeComponentConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeComponentConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeComponentRequest:
    boto3_raw_data: "type_defs.DescribeComponentRequestTypeDef" = dataclasses.field()

    ResourceGroupName = field("ResourceGroupName")
    ComponentName = field("ComponentName")
    AccountId = field("AccountId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeComponentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeComponentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeLogPatternRequest:
    boto3_raw_data: "type_defs.DescribeLogPatternRequestTypeDef" = dataclasses.field()

    ResourceGroupName = field("ResourceGroupName")
    PatternSetName = field("PatternSetName")
    PatternName = field("PatternName")
    AccountId = field("AccountId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeLogPatternRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeLogPatternRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeObservationRequest:
    boto3_raw_data: "type_defs.DescribeObservationRequestTypeDef" = dataclasses.field()

    ObservationId = field("ObservationId")
    AccountId = field("AccountId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeObservationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeObservationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Observation:
    boto3_raw_data: "type_defs.ObservationTypeDef" = dataclasses.field()

    Id = field("Id")
    StartTime = field("StartTime")
    EndTime = field("EndTime")
    SourceType = field("SourceType")
    SourceARN = field("SourceARN")
    LogGroup = field("LogGroup")
    LineTime = field("LineTime")
    LogText = field("LogText")
    LogFilter = field("LogFilter")
    MetricNamespace = field("MetricNamespace")
    MetricName = field("MetricName")
    Unit = field("Unit")
    Value = field("Value")
    CloudWatchEventId = field("CloudWatchEventId")
    CloudWatchEventSource = field("CloudWatchEventSource")
    CloudWatchEventDetailType = field("CloudWatchEventDetailType")
    HealthEventArn = field("HealthEventArn")
    HealthService = field("HealthService")
    HealthEventTypeCode = field("HealthEventTypeCode")
    HealthEventTypeCategory = field("HealthEventTypeCategory")
    HealthEventDescription = field("HealthEventDescription")
    CodeDeployDeploymentId = field("CodeDeployDeploymentId")
    CodeDeployDeploymentGroup = field("CodeDeployDeploymentGroup")
    CodeDeployState = field("CodeDeployState")
    CodeDeployApplication = field("CodeDeployApplication")
    CodeDeployInstanceGroupId = field("CodeDeployInstanceGroupId")
    Ec2State = field("Ec2State")
    RdsEventCategories = field("RdsEventCategories")
    RdsEventMessage = field("RdsEventMessage")
    S3EventName = field("S3EventName")
    StatesExecutionArn = field("StatesExecutionArn")
    StatesArn = field("StatesArn")
    StatesStatus = field("StatesStatus")
    StatesInput = field("StatesInput")
    EbsEvent = field("EbsEvent")
    EbsResult = field("EbsResult")
    EbsCause = field("EbsCause")
    EbsRequestId = field("EbsRequestId")
    XRayFaultPercent = field("XRayFaultPercent")
    XRayThrottlePercent = field("XRayThrottlePercent")
    XRayErrorPercent = field("XRayErrorPercent")
    XRayRequestCount = field("XRayRequestCount")
    XRayRequestAverageLatency = field("XRayRequestAverageLatency")
    XRayNodeName = field("XRayNodeName")
    XRayNodeType = field("XRayNodeType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ObservationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ObservationTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeProblemObservationsRequest:
    boto3_raw_data: "type_defs.DescribeProblemObservationsRequestTypeDef" = (
        dataclasses.field()
    )

    ProblemId = field("ProblemId")
    AccountId = field("AccountId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeProblemObservationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeProblemObservationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeProblemRequest:
    boto3_raw_data: "type_defs.DescribeProblemRequestTypeDef" = dataclasses.field()

    ProblemId = field("ProblemId")
    AccountId = field("AccountId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeProblemRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeProblemRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Problem:
    boto3_raw_data: "type_defs.ProblemTypeDef" = dataclasses.field()

    Id = field("Id")
    Title = field("Title")
    ShortName = field("ShortName")
    Insights = field("Insights")
    Status = field("Status")
    AffectedResource = field("AffectedResource")
    StartTime = field("StartTime")
    EndTime = field("EndTime")
    SeverityLevel = field("SeverityLevel")
    AccountId = field("AccountId")
    ResourceGroupName = field("ResourceGroupName")
    Feedback = field("Feedback")
    RecurringCount = field("RecurringCount")
    LastRecurrenceTime = field("LastRecurrenceTime")
    Visibility = field("Visibility")
    ResolutionMethod = field("ResolutionMethod")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ProblemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ProblemTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeWorkloadRequest:
    boto3_raw_data: "type_defs.DescribeWorkloadRequestTypeDef" = dataclasses.field()

    ResourceGroupName = field("ResourceGroupName")
    ComponentName = field("ComponentName")
    WorkloadId = field("WorkloadId")
    AccountId = field("AccountId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeWorkloadRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeWorkloadRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListApplicationsRequest:
    boto3_raw_data: "type_defs.ListApplicationsRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    AccountId = field("AccountId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListApplicationsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApplicationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListComponentsRequest:
    boto3_raw_data: "type_defs.ListComponentsRequestTypeDef" = dataclasses.field()

    ResourceGroupName = field("ResourceGroupName")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    AccountId = field("AccountId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListComponentsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListComponentsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLogPatternSetsRequest:
    boto3_raw_data: "type_defs.ListLogPatternSetsRequestTypeDef" = dataclasses.field()

    ResourceGroupName = field("ResourceGroupName")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    AccountId = field("AccountId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListLogPatternSetsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLogPatternSetsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLogPatternsRequest:
    boto3_raw_data: "type_defs.ListLogPatternsRequestTypeDef" = dataclasses.field()

    ResourceGroupName = field("ResourceGroupName")
    PatternSetName = field("PatternSetName")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    AccountId = field("AccountId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListLogPatternsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLogPatternsRequestTypeDef"]
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

    ResourceARN = field("ResourceARN")

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
class ListWorkloadsRequest:
    boto3_raw_data: "type_defs.ListWorkloadsRequestTypeDef" = dataclasses.field()

    ResourceGroupName = field("ResourceGroupName")
    ComponentName = field("ComponentName")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    AccountId = field("AccountId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListWorkloadsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorkloadsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Workload:
    boto3_raw_data: "type_defs.WorkloadTypeDef" = dataclasses.field()

    WorkloadId = field("WorkloadId")
    ComponentName = field("ComponentName")
    WorkloadName = field("WorkloadName")
    Tier = field("Tier")
    WorkloadRemarks = field("WorkloadRemarks")
    MissingWorkloadConfig = field("MissingWorkloadConfig")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WorkloadTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WorkloadTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveWorkloadRequest:
    boto3_raw_data: "type_defs.RemoveWorkloadRequestTypeDef" = dataclasses.field()

    ResourceGroupName = field("ResourceGroupName")
    ComponentName = field("ComponentName")
    WorkloadId = field("WorkloadId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RemoveWorkloadRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveWorkloadRequestTypeDef"]
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

    ResourceARN = field("ResourceARN")
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
class UpdateApplicationRequest:
    boto3_raw_data: "type_defs.UpdateApplicationRequestTypeDef" = dataclasses.field()

    ResourceGroupName = field("ResourceGroupName")
    OpsCenterEnabled = field("OpsCenterEnabled")
    CWEMonitorEnabled = field("CWEMonitorEnabled")
    OpsItemSNSTopicArn = field("OpsItemSNSTopicArn")
    SNSNotificationArn = field("SNSNotificationArn")
    RemoveSNSTopic = field("RemoveSNSTopic")
    AutoConfigEnabled = field("AutoConfigEnabled")
    AttachMissingPermission = field("AttachMissingPermission")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateApplicationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateApplicationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateComponentConfigurationRequest:
    boto3_raw_data: "type_defs.UpdateComponentConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    ResourceGroupName = field("ResourceGroupName")
    ComponentName = field("ComponentName")
    Monitor = field("Monitor")
    Tier = field("Tier")
    ComponentConfiguration = field("ComponentConfiguration")
    AutoConfigEnabled = field("AutoConfigEnabled")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateComponentConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateComponentConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateComponentRequest:
    boto3_raw_data: "type_defs.UpdateComponentRequestTypeDef" = dataclasses.field()

    ResourceGroupName = field("ResourceGroupName")
    ComponentName = field("ComponentName")
    NewComponentName = field("NewComponentName")
    ResourceList = field("ResourceList")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateComponentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateComponentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateLogPatternRequest:
    boto3_raw_data: "type_defs.UpdateLogPatternRequestTypeDef" = dataclasses.field()

    ResourceGroupName = field("ResourceGroupName")
    PatternSetName = field("PatternSetName")
    PatternName = field("PatternName")
    Pattern = field("Pattern")
    Rank = field("Rank")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateLogPatternRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateLogPatternRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateProblemRequest:
    boto3_raw_data: "type_defs.UpdateProblemRequestTypeDef" = dataclasses.field()

    ProblemId = field("ProblemId")
    UpdateStatus = field("UpdateStatus")
    Visibility = field("Visibility")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateProblemRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateProblemRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddWorkloadRequest:
    boto3_raw_data: "type_defs.AddWorkloadRequestTypeDef" = dataclasses.field()

    ResourceGroupName = field("ResourceGroupName")
    ComponentName = field("ComponentName")

    @cached_property
    def WorkloadConfiguration(self):  # pragma: no cover
        return WorkloadConfiguration.make_one(
            self.boto3_raw_data["WorkloadConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddWorkloadRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddWorkloadRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateWorkloadRequest:
    boto3_raw_data: "type_defs.UpdateWorkloadRequestTypeDef" = dataclasses.field()

    ResourceGroupName = field("ResourceGroupName")
    ComponentName = field("ComponentName")

    @cached_property
    def WorkloadConfiguration(self):  # pragma: no cover
        return WorkloadConfiguration.make_one(
            self.boto3_raw_data["WorkloadConfiguration"]
        )

    WorkloadId = field("WorkloadId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateWorkloadRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateWorkloadRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddWorkloadResponse:
    boto3_raw_data: "type_defs.AddWorkloadResponseTypeDef" = dataclasses.field()

    WorkloadId = field("WorkloadId")

    @cached_property
    def WorkloadConfiguration(self):  # pragma: no cover
        return WorkloadConfiguration.make_one(
            self.boto3_raw_data["WorkloadConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddWorkloadResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddWorkloadResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeComponentConfigurationRecommendationResponse:
    boto3_raw_data: (
        "type_defs.DescribeComponentConfigurationRecommendationResponseTypeDef"
    ) = dataclasses.field()

    ComponentConfiguration = field("ComponentConfiguration")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeComponentConfigurationRecommendationResponseTypeDef"
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
                "type_defs.DescribeComponentConfigurationRecommendationResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeComponentConfigurationResponse:
    boto3_raw_data: "type_defs.DescribeComponentConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    Monitor = field("Monitor")
    Tier = field("Tier")
    ComponentConfiguration = field("ComponentConfiguration")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeComponentConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeComponentConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeWorkloadResponse:
    boto3_raw_data: "type_defs.DescribeWorkloadResponseTypeDef" = dataclasses.field()

    WorkloadId = field("WorkloadId")
    WorkloadRemarks = field("WorkloadRemarks")

    @cached_property
    def WorkloadConfiguration(self):  # pragma: no cover
        return WorkloadConfiguration.make_one(
            self.boto3_raw_data["WorkloadConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeWorkloadResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeWorkloadResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLogPatternSetsResponse:
    boto3_raw_data: "type_defs.ListLogPatternSetsResponseTypeDef" = dataclasses.field()

    ResourceGroupName = field("ResourceGroupName")
    AccountId = field("AccountId")
    LogPatternSets = field("LogPatternSets")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListLogPatternSetsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLogPatternSetsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateWorkloadResponse:
    boto3_raw_data: "type_defs.UpdateWorkloadResponseTypeDef" = dataclasses.field()

    WorkloadId = field("WorkloadId")

    @cached_property
    def WorkloadConfiguration(self):  # pragma: no cover
        return WorkloadConfiguration.make_one(
            self.boto3_raw_data["WorkloadConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateWorkloadResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateWorkloadResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeComponentResponse:
    boto3_raw_data: "type_defs.DescribeComponentResponseTypeDef" = dataclasses.field()

    @cached_property
    def ApplicationComponent(self):  # pragma: no cover
        return ApplicationComponent.make_one(
            self.boto3_raw_data["ApplicationComponent"]
        )

    ResourceList = field("ResourceList")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeComponentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeComponentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListComponentsResponse:
    boto3_raw_data: "type_defs.ListComponentsResponseTypeDef" = dataclasses.field()

    @cached_property
    def ApplicationComponentList(self):  # pragma: no cover
        return ApplicationComponent.make_many(
            self.boto3_raw_data["ApplicationComponentList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListComponentsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListComponentsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateApplicationResponse:
    boto3_raw_data: "type_defs.CreateApplicationResponseTypeDef" = dataclasses.field()

    @cached_property
    def ApplicationInfo(self):  # pragma: no cover
        return ApplicationInfo.make_one(self.boto3_raw_data["ApplicationInfo"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateApplicationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateApplicationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeApplicationResponse:
    boto3_raw_data: "type_defs.DescribeApplicationResponseTypeDef" = dataclasses.field()

    @cached_property
    def ApplicationInfo(self):  # pragma: no cover
        return ApplicationInfo.make_one(self.boto3_raw_data["ApplicationInfo"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeApplicationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeApplicationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListApplicationsResponse:
    boto3_raw_data: "type_defs.ListApplicationsResponseTypeDef" = dataclasses.field()

    @cached_property
    def ApplicationInfoList(self):  # pragma: no cover
        return ApplicationInfo.make_many(self.boto3_raw_data["ApplicationInfoList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListApplicationsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApplicationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateApplicationResponse:
    boto3_raw_data: "type_defs.UpdateApplicationResponseTypeDef" = dataclasses.field()

    @cached_property
    def ApplicationInfo(self):  # pragma: no cover
        return ApplicationInfo.make_one(self.boto3_raw_data["ApplicationInfo"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateApplicationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateApplicationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConfigurationHistoryResponse:
    boto3_raw_data: "type_defs.ListConfigurationHistoryResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def EventList(self):  # pragma: no cover
        return ConfigurationEvent.make_many(self.boto3_raw_data["EventList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListConfigurationHistoryResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConfigurationHistoryResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateApplicationRequest:
    boto3_raw_data: "type_defs.CreateApplicationRequestTypeDef" = dataclasses.field()

    ResourceGroupName = field("ResourceGroupName")
    OpsCenterEnabled = field("OpsCenterEnabled")
    CWEMonitorEnabled = field("CWEMonitorEnabled")
    OpsItemSNSTopicArn = field("OpsItemSNSTopicArn")
    SNSNotificationArn = field("SNSNotificationArn")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    AutoConfigEnabled = field("AutoConfigEnabled")
    AutoCreate = field("AutoCreate")
    GroupingType = field("GroupingType")
    AttachMissingPermission = field("AttachMissingPermission")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateApplicationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateApplicationRequestTypeDef"]
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
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

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

    ResourceARN = field("ResourceARN")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

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
class CreateLogPatternResponse:
    boto3_raw_data: "type_defs.CreateLogPatternResponseTypeDef" = dataclasses.field()

    @cached_property
    def LogPattern(self):  # pragma: no cover
        return LogPattern.make_one(self.boto3_raw_data["LogPattern"])

    ResourceGroupName = field("ResourceGroupName")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateLogPatternResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLogPatternResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeLogPatternResponse:
    boto3_raw_data: "type_defs.DescribeLogPatternResponseTypeDef" = dataclasses.field()

    ResourceGroupName = field("ResourceGroupName")
    AccountId = field("AccountId")

    @cached_property
    def LogPattern(self):  # pragma: no cover
        return LogPattern.make_one(self.boto3_raw_data["LogPattern"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeLogPatternResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeLogPatternResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLogPatternsResponse:
    boto3_raw_data: "type_defs.ListLogPatternsResponseTypeDef" = dataclasses.field()

    ResourceGroupName = field("ResourceGroupName")
    AccountId = field("AccountId")

    @cached_property
    def LogPatterns(self):  # pragma: no cover
        return LogPattern.make_many(self.boto3_raw_data["LogPatterns"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListLogPatternsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLogPatternsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateLogPatternResponse:
    boto3_raw_data: "type_defs.UpdateLogPatternResponseTypeDef" = dataclasses.field()

    ResourceGroupName = field("ResourceGroupName")

    @cached_property
    def LogPattern(self):  # pragma: no cover
        return LogPattern.make_one(self.boto3_raw_data["LogPattern"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateLogPatternResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateLogPatternResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeObservationResponse:
    boto3_raw_data: "type_defs.DescribeObservationResponseTypeDef" = dataclasses.field()

    @cached_property
    def Observation(self):  # pragma: no cover
        return Observation.make_one(self.boto3_raw_data["Observation"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeObservationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeObservationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RelatedObservations:
    boto3_raw_data: "type_defs.RelatedObservationsTypeDef" = dataclasses.field()

    @cached_property
    def ObservationList(self):  # pragma: no cover
        return Observation.make_many(self.boto3_raw_data["ObservationList"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RelatedObservationsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RelatedObservationsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeProblemResponse:
    boto3_raw_data: "type_defs.DescribeProblemResponseTypeDef" = dataclasses.field()

    @cached_property
    def Problem(self):  # pragma: no cover
        return Problem.make_one(self.boto3_raw_data["Problem"])

    SNSNotificationArn = field("SNSNotificationArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeProblemResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeProblemResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProblemsResponse:
    boto3_raw_data: "type_defs.ListProblemsResponseTypeDef" = dataclasses.field()

    @cached_property
    def ProblemList(self):  # pragma: no cover
        return Problem.make_many(self.boto3_raw_data["ProblemList"])

    ResourceGroupName = field("ResourceGroupName")
    AccountId = field("AccountId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListProblemsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProblemsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConfigurationHistoryRequest:
    boto3_raw_data: "type_defs.ListConfigurationHistoryRequestTypeDef" = (
        dataclasses.field()
    )

    ResourceGroupName = field("ResourceGroupName")
    StartTime = field("StartTime")
    EndTime = field("EndTime")
    EventStatus = field("EventStatus")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    AccountId = field("AccountId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListConfigurationHistoryRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConfigurationHistoryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProblemsRequest:
    boto3_raw_data: "type_defs.ListProblemsRequestTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    ResourceGroupName = field("ResourceGroupName")
    StartTime = field("StartTime")
    EndTime = field("EndTime")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    ComponentName = field("ComponentName")
    Visibility = field("Visibility")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListProblemsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProblemsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWorkloadsResponse:
    boto3_raw_data: "type_defs.ListWorkloadsResponseTypeDef" = dataclasses.field()

    @cached_property
    def WorkloadList(self):  # pragma: no cover
        return Workload.make_many(self.boto3_raw_data["WorkloadList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListWorkloadsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorkloadsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeProblemObservationsResponse:
    boto3_raw_data: "type_defs.DescribeProblemObservationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def RelatedObservations(self):  # pragma: no cover
        return RelatedObservations.make_one(self.boto3_raw_data["RelatedObservations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeProblemObservationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeProblemObservationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
